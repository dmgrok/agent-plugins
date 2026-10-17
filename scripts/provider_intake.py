#!/usr/bin/env python3
"""
Parse and validate new-provider submissions from GitHub issues.

Issue bodies are attacker-controlled. Every field is validated against a strict
allowlist and all URLs are regenerated from the validated owner/repo/branch, so
the workflow never forwards user-supplied URLs (which would receive the
GITHUB_TOKEN in scripts/test_provider.py) or raw text into code.

Usage (from GitHub Actions):
    ISSUE_BODY=... ISSUE_NUMBER=... ISSUE_USER=... python scripts/provider_intake.py parse
    PROVIDER_CONFIG_JSON=... python scripts/provider_intake.py add-provider
    SKILLS_PATH_PREFIX=... python scripts/provider_intake.py stage-lgtm --source DIR --dest DIR
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AGGREGATE = ROOT / "scripts" / "aggregate.py"

PROVIDER_ID_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,48}[a-z0-9])?$")
PROVIDER_NAME_RE = re.compile(r"^\w[\w .,:&'()+/-]{0,79}$")
OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
REPO_NAME_RE = re.compile(r"^[A-Za-z0-9._-]{1,100}$")
BRANCH_RE = re.compile(r"^[A-Za-z0-9._/-]{1,100}$")
PATH_SEGMENT_RE = re.compile(r"^[A-Za-z0-9._-]+$")
REPO_URL_RE = re.compile(
    r"^https://github\.com/(?P<owner>[^/\s]+)/(?P<repo>[^/\s]+?)(?:\.git)?/?$"
)
ISSUE_NUMBER_RE = re.compile(r"^[1-9][0-9]{0,9}$")
ISSUE_USER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})(?:\[bot\])?$")

FENCED_BLOCK_RE = re.compile(r"^[ \t]*```([^\n`]*)\n([\s\S]*?)^[ \t]*```[ \t]*$", re.MULTILINE)

ROOT_LOCATION_MARKER = "Root directory"
NO_RESPONSE = "_No response_"


class IntakeError(ValueError):
    """Submission is malformed or unsafe. Messages never echo raw input."""


class ProviderExistsError(IntakeError):
    pass


@dataclass(frozen=True)
class ProviderSubmission:
    provider_id: str
    name: str
    owner: str
    repo_name: str
    branch: str
    skills_path_prefix: str

    @property
    def repo_url(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo_name}"

    @property
    def api_tree_url(self) -> str:
        return (
            f"https://api.github.com/repos/{self.owner}/{self.repo_name}"
            f"/git/trees/{self.branch}?recursive=1"
        )

    @property
    def raw_base(self) -> str:
        return f"https://raw.githubusercontent.com/{self.owner}/{self.repo_name}/{self.branch}"

    def to_provider_config(self) -> Dict[str, Dict[str, str]]:
        return {
            self.provider_id: {
                "name": self.name,
                "repo": self.repo_url,
                "api_tree_url": self.api_tree_url,
                "raw_base": self.raw_base,
                "skills_path_prefix": self.skills_path_prefix,
            }
        }

    def outputs(self) -> Dict[str, str]:
        return {
            "provider_id": self.provider_id,
            "provider_name": self.name,
            "repo_url": self.repo_url,
            "repo_owner": self.owner,
            "repo_name": self.repo_name,
            "branch": self.branch,
            "api_tree_url": self.api_tree_url,
            "raw_base": self.raw_base,
            "skills_path_prefix": self.skills_path_prefix,
            "config_json": json.dumps(self.to_provider_config(), ensure_ascii=True),
        }


def _validate_provider_id(value: str) -> str:
    if not PROVIDER_ID_RE.match(value):
        raise IntakeError(
            "Provider ID must be 1-50 lowercase letters, digits or hyphens, "
            "and cannot start or end with a hyphen."
        )
    return value


def _validate_name(value: str) -> str:
    if not PROVIDER_NAME_RE.match(value):
        raise IntakeError(
            "Provider Name must be 1-80 characters: letters, digits, spaces and . , : & ' ( ) + / -"
        )
    return value


def _validate_branch(value: str) -> str:
    if (
        not BRANCH_RE.match(value)
        or value.startswith(("-", "/", "."))
        or value.endswith(("/", ".", ".lock"))
        or ".." in value
        or "//" in value
    ):
        raise IntakeError("Default Branch is not a valid branch name.")
    return value


def _validate_skills_prefix(value: str) -> str:
    if value == "":
        return value
    if not value.endswith("/") or value.startswith("/"):
        raise IntakeError("Skills path must be empty or a relative directory ending with '/'.")
    segments = value[:-1].split("/")
    if any(seg in ("", ".", "..") or not PATH_SEGMENT_RE.match(seg) for seg in segments):
        raise IntakeError("Skills path contains an invalid directory segment.")
    return value


def _parse_repo_url(value: str) -> tuple:
    match = REPO_URL_RE.match(value)
    if not match:
        raise IntakeError("Repository URL must look like https://github.com/<owner>/<repo>.")
    owner, repo = match.group("owner"), match.group("repo")
    if not OWNER_RE.match(owner) or not REPO_NAME_RE.match(repo) or repo in (".", ".."):
        raise IntakeError("Repository URL contains an invalid owner or repository name.")
    return owner, repo


def _form_field(body: str, label: str) -> Optional[str]:
    pattern = re.compile(
        rf"^###[ \t]+{re.escape(label)}[ \t]*$\n(?:[ \t]*\n)*[ \t]*(?!###)(\S[^\n]*?)[ \t]*$",
        re.MULTILINE,
    )
    match = pattern.search(body)
    if not match or match.group(1) == NO_RESPONSE:
        return None
    return match.group(1)


def _parse_form(body: str) -> Optional[ProviderSubmission]:
    fields = {
        label: _form_field(body, label)
        for label in ("Repository URL", "Provider Name", "Provider ID", "Default Branch")
    }
    if not all(fields.values()):
        return None
    owner, repo = _parse_repo_url(fields["Repository URL"])
    location = _form_field(body, "Skills Location") or ""
    return ProviderSubmission(
        provider_id=_validate_provider_id(fields["Provider ID"]),
        name=_validate_name(fields["Provider Name"]),
        owner=owner,
        repo_name=repo,
        branch=_validate_branch(fields["Default Branch"]),
        skills_path_prefix="" if ROOT_LOCATION_MARKER in location else "skills/",
    )


def _branch_from_url(url: str, prefix: str, suffix: str = "") -> str:
    if not url.startswith(prefix) or not url.endswith(suffix):
        raise IntakeError("Provider URLs must point at the submitted GitHub repository.")
    return url[len(prefix): len(url) - len(suffix)]


def submission_from_config(config: dict) -> ProviderSubmission:
    """Validate a `{provider_id: {...}}` mapping and rebuild canonical URLs."""
    if not isinstance(config, dict) or len(config) != 1:
        raise IntakeError("Provider configuration must contain exactly one provider.")
    provider_id, data = next(iter(config.items()))
    if not isinstance(data, dict) or not all(
        isinstance(data.get(key), str) for key in ("name", "repo")
    ):
        raise IntakeError("Provider configuration requires string 'name' and 'repo' fields.")

    owner, repo = _parse_repo_url(data["repo"])
    branches = set()
    if isinstance(data.get("api_tree_url"), str):
        branches.add(_branch_from_url(
            data["api_tree_url"],
            f"https://api.github.com/repos/{owner}/{repo}/git/trees/",
            "?recursive=1",
        ))
    if isinstance(data.get("raw_base"), str):
        branches.add(_branch_from_url(
            data["raw_base"], f"https://raw.githubusercontent.com/{owner}/{repo}/"
        ))
    if isinstance(data.get("branch"), str):
        branches.add(data["branch"])
    if len(branches) != 1:
        raise IntakeError("Provider URLs must reference exactly one branch.")

    prefix = data.get("skills_path_prefix", "skills/")
    if not isinstance(prefix, str):
        raise IntakeError("Skills path must be a string.")

    return ProviderSubmission(
        provider_id=_validate_provider_id(provider_id),
        name=_validate_name(data["name"]),
        owner=owner,
        repo_name=repo,
        branch=_validate_branch(branches.pop()),
        skills_path_prefix=_validate_skills_prefix(prefix),
    )


def _parse_code_block(body: str) -> Optional[ProviderSubmission]:
    # Walk fences in order so the closing fence of an unrelated block (for
    # example ```text) is never mistaken for the opening of the config block.
    for match in FENCED_BLOCK_RE.finditer(body):
        if match.group(1).strip().lower() in ("", "json", "python") and '"repo"' in match.group(2):
            text = match.group(2).strip()
            break
    else:
        return None
    if not text.startswith("{"):
        text = "{" + text + "}"
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    try:
        config = json.loads(text)
    except json.JSONDecodeError:
        raise IntakeError("Provider Configuration block is not valid JSON.") from None
    return submission_from_config(config)


def parse_issue_body(body: str) -> ProviderSubmission:
    body = (body or "").replace("\r\n", "\n")
    submission = _parse_form(body) or _parse_code_block(body)
    if submission is None:
        raise IntakeError(
            "Could not find the required fields (Repository URL, Provider Name, "
            "Provider ID, Default Branch). Please use the New Provider issue form."
        )
    return submission


def write_github_output(path, outputs: Dict[str, str]) -> None:
    for key, value in outputs.items():
        if "\n" in value or "\r" in value:
            raise IntakeError(f"Output '{key}' must be a single line.")
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in outputs.items():
            handle.write(f"{key}={value}\n")


def _providers_bounds(source: str) -> tuple:
    start = re.search(r"^PROVIDERS = \{\n", source, re.MULTILINE)
    if not start:
        raise IntakeError("Could not find PROVIDERS in aggregate.py.")
    end = re.compile(r"^\}", re.MULTILINE).search(source, start.end())
    if not end:
        raise IntakeError("Could not find the end of PROVIDERS in aggregate.py.")
    return start.end(), end.start()


def add_provider_to_source(source: str, submission: ProviderSubmission) -> str:
    """Return aggregate.py source with the provider appended to PROVIDERS."""
    body_start, body_end = _providers_bounds(source)
    key_re = re.compile(rf'^    "{re.escape(submission.provider_id)}"\s*:', re.MULTILINE)
    if key_re.search(source, body_start, body_end):
        raise ProviderExistsError(f"Provider '{submission.provider_id}' already exists.")

    fields = submission.to_provider_config()[submission.provider_id]
    lines = [f"    {json.dumps(submission.provider_id)}: {{"]
    lines += [f"        {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}," for k, v in fields.items()]
    lines.append("    },\n")
    return source[:body_end] + "\n".join(lines) + source[body_end:]


SKILL_NAME_RE = re.compile(r"^name:[ \t]*([\"']?)([a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?)\1[ \t]*$", re.MULTILINE)


def _root_skill_name(skill_md: Path) -> Optional[str]:
    try:
        text = skill_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    parts = text.split("---", 2)
    if not text.startswith("---") or len(parts) < 3:
        return None
    match = SKILL_NAME_RE.search(parts[1])
    return match.group(2) if match else None


def stage_lgtm_input(source: Path, skills_path_prefix: str, dest: Path) -> Path:
    """Return the directory the skill linter should scan.

    The linter requires each skill's `name` to match its parent directory. A
    root-level SKILL.md sits in the checkout directory, whose name the workflow
    chooses, so it is copied into `dest/<name>` first. Symlinks are copied as
    links so a submission cannot pull runner files into the scanned tree.
    """
    prefix = _validate_skills_prefix(skills_path_prefix)
    if prefix:
        return source / prefix.rstrip("/")
    name = _root_skill_name(source / "SKILL.md")
    if name is None:
        return source
    shutil.copytree(source, dest / name, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    return dest


def _env(*names: str) -> str:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return ""


def _cmd_parse() -> int:
    output_path = os.environ.get("GITHUB_OUTPUT")
    try:
        issue_number = _env("ISSUE_NUMBER", "DISPATCH_ISSUE_NUMBER")
        issue_user = _env("ISSUE_USER", "DISPATCH_ISSUE_USER")
        if not ISSUE_NUMBER_RE.match(issue_number):
            raise IntakeError("Issue number is missing or invalid.")
        if not ISSUE_USER_RE.match(issue_user):
            raise IntakeError("Issue author login is missing or invalid.")
        submission = parse_issue_body(_env("ISSUE_BODY", "DISPATCH_ISSUE_BODY"))
        outputs = submission.outputs()
        outputs.update(issue_number=issue_number, issue_user=issue_user)
    except IntakeError as exc:
        print(f"::error::{exc}")
        if output_path:
            write_github_output(output_path, {"error": str(exc)})
        return 1

    if output_path:
        write_github_output(output_path, outputs)
    print(f"Parsed provider '{submission.provider_id}' ({submission.repo_url})")
    return 0


def _cmd_add_provider(aggregate: Path) -> int:
    try:
        submission = submission_from_config(json.loads(os.environ.get("PROVIDER_CONFIG_JSON", "")))
        source = aggregate.read_text(encoding="utf-8")
        updated = add_provider_to_source(source, submission)
        compile(updated, str(aggregate), "exec")
    except ProviderExistsError as exc:
        print(exc)
        return 0
    except (IntakeError, json.JSONDecodeError, SyntaxError) as exc:
        print(f"::error::Could not add provider: {exc}")
        return 1
    aggregate.write_text(updated, encoding="utf-8")
    print(f"Added provider '{submission.provider_id}' to {aggregate.name}")
    return 0


def _cmd_stage_lgtm(source: Path, dest: Path) -> int:
    try:
        path = stage_lgtm_input(source, os.environ.get("SKILLS_PATH_PREFIX", ""), dest)
    except IntakeError as exc:
        print(f"::error::{exc}")
        return 1
    lgtm_path = f"./{path.as_posix().rstrip('/')}/"
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        write_github_output(output_path, {"lgtm_path": lgtm_path})
    print(f"LGTM will scan {lgtm_path}")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("parse", help="Parse ISSUE_BODY and write step outputs")
    add = sub.add_parser("add-provider", help="Insert PROVIDER_CONFIG_JSON into aggregate.py")
    add.add_argument("--aggregate", type=Path, default=DEFAULT_AGGREGATE)
    stage = sub.add_parser("stage-lgtm", help="Prepare the directory scanned by the skill linter")
    stage.add_argument("--source", type=Path, required=True)
    stage.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args(argv)

    if args.command == "parse":
        return _cmd_parse()
    if args.command == "stage-lgtm":
        return _cmd_stage_lgtm(args.source, args.dest)
    return _cmd_add_provider(args.aggregate)


if __name__ == "__main__":
    sys.exit(main())
