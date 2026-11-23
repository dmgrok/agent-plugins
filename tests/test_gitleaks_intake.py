import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from scripts import provider_intake as intake  # noqa: E402

CONFIG = ROOT / "scripts" / "provider-intake.gitleaks.toml"
SHA256_A = "4454afd8c6f1e2a3b4c5d6e7f8091a2b3c4d5e6f708192a3b4c5d6e7f809e516"
SHA256_B = "62d121c2a0b1c2d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f6071828391c2"
SHA1 = "0123456789abcdef0123456789abcdef01234567"


def _gitleaks_bin():
    env = os.environ.get("GITLEAKS")
    if env:
        return env
    pinned = Path("/tmp/gitleaks-8.18.1/gitleaks")
    if pinned.is_file():
        return str(pinned)
    return shutil.which("gitleaks")


def _run_gitleaks(source: Path, report: Path):
    binary = _gitleaks_bin()
    if not binary:
        pytest.skip("gitleaks is not installed")
    completed = subprocess.run(
        [
            binary,
            "detect",
            "--source",
            str(source),
            "--no-git",
            "--exit-code",
            "1",
            "--config",
            str(CONFIG),
            "--report-path",
            str(report),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    findings = []
    if report.is_file() and report.stat().st_size:
        findings = json.loads(report.read_text(encoding="utf-8"))
    return completed.returncode, findings


def test_hash_manifest_passes_gitleaks_and_tokens_still_fail(tmp_path):
    manifest_dir = tmp_path / "manifest"
    secrets_dir = tmp_path / "secrets"
    manifest_dir.mkdir()
    secrets_dir.mkdir()

    (manifest_dir / "artefact-hashes.json").write_text(
        json.dumps(
            {
                "adr-access.json": SHA256_A,
                "marketing-access.json": SHA256_B,
                "readme.md": SHA256_A,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (manifest_dir / "checksums.txt").write_text(f"{SHA256_A}  payload.bin\n", encoding="utf-8")
    (manifest_dir / "lock-sample.json").write_text(
        json.dumps({"integrity": "sha512-" + "A" * 86 + "=="}) + "\n",
        encoding="utf-8",
    )

    aws = "AKIA" + "Q7" * 8
    github = "ghp_" + "Zy9" * 12
    (secrets_dir / "config.env").write_text(
        f"AWS_ACCESS_KEY_ID={aws}\nGITHUB_TOKEN={github}\n",
        encoding="utf-8",
    )

    manifest_code, manifest_findings = _run_gitleaks(manifest_dir, tmp_path / "manifest.json")
    assert manifest_code == 0, manifest_findings
    assert manifest_findings == []

    secret_code, secret_findings = _run_gitleaks(secrets_dir, tmp_path / "secrets.json")
    assert secret_code == 1
    rules = {item["RuleID"] for item in secret_findings}
    assert "aws-access-token" in rules
    assert "github-pat" in rules
    for item in secret_findings:
        assert item.get("Secret") not in {SHA256_A, SHA256_B}

    combined = tmp_path / "combined"
    combined.mkdir()
    shutil.copytree(manifest_dir, combined / "hashes")
    shutil.copytree(secrets_dir, combined / "secrets")
    combined_code, combined_findings = _run_gitleaks(combined, tmp_path / "combined.json")
    assert combined_code == 1
    assert {item["RuleID"] for item in combined_findings} >= {"aws-access-token", "github-pat"}
    assert all(
        "hashes" not in item.get("File", "")
        for item in combined_findings
    )


def test_gitleaks_summary_redacts_secrets_and_explains_false_positives(tmp_path):
    aws = "AKIA" + "Q7" * 8
    report = [
        {
            "RuleID": "generic-api-key",
            "File": "contributor-repo/evaluations/skill-selection/artefact-hashes.json",
            "StartLine": 2,
            "Secret": SHA256_A,
        },
        {
            "RuleID": "aws-access-token",
            "File": "contributor-repo/.env",
            "StartLine": 4,
            "Secret": aws,
        },
    ]
    path = tmp_path / "gitleaks-report.json"
    path.write_text(json.dumps(report), encoding="utf-8")
    output = tmp_path / "summary.md"
    assert intake.main(["gitleaks-summary", "--report", str(path), "--output", str(output)]) == 0
    text = output.read_text(encoding="utf-8")
    assert "generic-api-key" in text
    assert "evaluations/skill-selection/artefact-hashes.json:2" in text
    assert "64-char hex" in text
    assert SHA256_A not in text
    assert aws not in text
    assert "aws-access-token" in text
    assert "AKIA… (redacted)" in text
    assert "false positive" in text
    assert "comment on this issue" in text


def test_gitleaks_summary_handles_a_missing_report(tmp_path):
    output = tmp_path / "summary.md"
    text = intake.summarise_gitleaks_report(tmp_path / "missing.json")
    output.write_text(text, encoding="utf-8")
    assert "could not be read" in text
    assert "false positive" in text
    assert SHA256_A not in text
