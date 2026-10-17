import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
INTAKE = WORKFLOWS / "validate-new-provider.yml"
GATE_LABEL = "run-provider-validation"

# Attacker-controllable contexts that must never be expanded inline in shell or
# github-script code; pass them through `env:` instead.
UNTRUSTED_EXPR = re.compile(
    r"\$\{\{[^}]*\b(github\.event\.(issue|comment|pull_request|review)|"
    r"github\.head_ref|steps\.parse\.outputs)"
)


def load(path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    # PyYAML parses the bare `on` key as boolean True.
    if True in data:
        data["on"] = data.pop(True)
    return data


def code_blocks(workflow):
    for job_id, job in workflow.get("jobs", {}).items():
        for index, step in enumerate(job.get("steps", [])):
            label = f"{job_id}/{step.get('name', index)}"
            if "run" in step:
                yield label, step["run"]
            script = (step.get("with") or {}).get("script")
            if script:
                yield label, script


@pytest.mark.parametrize("path", sorted(WORKFLOWS.glob("*.yml")), ids=lambda p: p.name)
def test_workflows_do_not_inline_untrusted_input_in_code(path):
    offenders = [label for label, code in code_blocks(load(path)) if UNTRUSTED_EXPR.search(code)]
    assert offenders == []


def test_intake_code_steps_use_no_inline_expressions():
    offenders = [label for label, code in code_blocks(load(INTAKE)) if "${{" in code]
    assert offenders == []


def test_intake_validation_requires_dedicated_maintainer_label():
    workflow = load(INTAKE)
    assert "edited" not in workflow["on"]["issues"]["types"]

    job = workflow["jobs"]["validate-provider"]
    condition = job["if"]
    assert GATE_LABEL in condition
    assert "new-source" not in condition
    assert "issue.body" not in condition

    steps = job["steps"]
    assert "permission" in steps[0]["name"].lower()


def test_gate_label_is_never_auto_applied_by_issue_templates():
    for template in (ROOT / ".github" / "ISSUE_TEMPLATE").iterdir():
        assert GATE_LABEL not in template.read_text(encoding="utf-8"), template.name


def test_intake_permissions_are_scoped_per_job():
    workflow = load(INTAKE)
    assert workflow["permissions"] == {}
    for job_id, job in workflow["jobs"].items():
        assert "permissions" in job, job_id


def test_contributor_checkout_does_not_persist_credentials():
    steps = load(INTAKE)["jobs"]["validate-provider"]["steps"]
    checkouts = [
        s for s in steps
        if str(s.get("uses", "")).startswith("actions/checkout") and "repository" in s.get("with", {})
    ]
    assert checkouts
    assert all(s["with"].get("persist-credentials") is False for s in checkouts)


def test_tests_workflow_runs_pytest_with_read_only_token():
    workflow = load(WORKFLOWS / "tests.yml")
    assert workflow["permissions"] == {"contents": "read"}
    assert {"push", "pull_request"} <= set(workflow["on"])
    runs = " ".join(code for _, code in code_blocks(workflow))
    assert "pytest" in runs


def test_gitleaks_scan_fails_when_leaks_are_found():
    steps = load(INTAKE)["jobs"]["validate-provider"]["steps"]
    scan = next(s for s in steps if "gitleaks detect" in s.get("run", ""))
    # `--exit-code 0` makes gitleaks succeed even when it finds secrets, so the
    # `gitleaks_passed=false` branch could never run.
    assert not re.search(r"--exit-code[ =]0\b", scan["run"])
