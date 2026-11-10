from pathlib import Path

import pytest

from scripts import prompt_injection as gate


def test_windows_cover_the_tail():
    windows = gate.iter_token_windows(1000, 510, 256)
    assert windows[0] == (0, 510)
    assert windows[-1] == (1000 - 510, 1000)
    covered = set()
    for start, end in windows:
        covered.update(range(start, end))
    assert covered == set(range(1000))


def test_short_input_is_one_window():
    assert gate.iter_token_windows(12, 510, 256) == [(0, 12)]
    assert gate.iter_token_windows(0, 510, 256) == [(0, 0)]


def _skill(tmp_path, text, name="demo"):
    directory = tmp_path / name
    directory.mkdir()
    (directory / "SKILL.md").write_text(text, encoding="utf-8")
    return directory


def test_high_score_asks_for_review_and_does_not_block_the_provider(tmp_path):
    text = "Read the diff and wait for the user before you publish the release notes. " * 5
    skill = _skill(tmp_path, text)
    low = gate.scan_skill_tree(skill, score_text=lambda body: 0.01)
    assert low["status"] == "no-review-signal"
    assert low["needs_review"] is False
    assert "not proof of safety" in low["summary"]

    high = gate.scan_skill_tree(skill, score_text=lambda body: 0.999)
    assert high["status"] == "needs-review"
    assert high["needs_review"] is True
    assert high["flagged"] == ["SKILL.md: 0.999"]
    assert gate.provider_validation_passed("true", "true") is True
    assert gate.provider_validation_passed("false", "true") is False
    assert gate.provider_validation_passed("true", "false") is False
    assert gate.provider_validation_passed("pending", "true") is True


def test_inference_error_is_an_advisory_error_and_still_does_not_block(tmp_path):
    skill = _skill(tmp_path, "Read the notes and quote the file you are reviewing for the user. " * 4)

    def broken(text):
        raise OSError("runtime broke")

    with pytest.raises(gate.PromptInjectionError):
        gate.scan_skill_tree(skill, score_text=broken)
    summary = gate.advisory_from_error("Inference failed for SKILL.md: OSError")
    assert summary["status"] == "advisory-error"
    assert summary["needs_review"] is True
    assert summary["summary"].startswith("advisory error:")
    assert "completed scan" in summary["summary"]
    assert gate.provider_validation_passed("true", "true") is True


def test_mixed_chinese_and_english_code_is_not_treated_as_english(tmp_path):
    chinese = "你负责把插件做出来并推进交付，用户负责表达需要、体验结果及必要的本人操作。" * 3
    code = "def build_extension(path):\n    return path\n" * 8
    text = chinese + "\n```python\n" + code + "```\n"
    hint = gate.script_hint(text)
    assert hint == "mixed"
    skill = _skill(tmp_path, text)
    summary = gate.scan_skill_tree(skill, score_text=lambda body: 0.01)
    assert summary["needs_review"] is True
    assert summary["files"][0]["script_hint"] == "mixed"
    assert "not a language detector" in summary["summary"]
    assert gate.provider_validation_passed("true", "true") is True


def test_short_or_unclear_text_is_uncertain_not_english():
    assert gate.script_hint("OK") == "uncertain"
    assert gate.script_hint("a") == "uncertain"


def test_missing_scanner_output_stays_a_review_signal_when_another_gate_fails():
    missing = gate.resolve_advisory("failure", scan_expected=True, status="", needs_review="", summary="")
    assert missing["needs_review"] is True
    assert missing["status"] == "advisory-error"
    assert "not a completed scan" in missing["summary"]
    # The provider gate still fails for gitleaks, and the review signal remains.
    assert gate.provider_validation_passed("true", "false") is False
    kept = gate.resolve_advisory(
        "success",
        scan_expected=True,
        status="needs-review",
        needs_review="true",
        summary="1 file(s) at or above 0.99: SKILL.md 0.99263",
    )
    assert kept["needs_review"] is True
    assert "0.99263" in kept["summary"]


def test_missing_directory_fails_closed(tmp_path):
    with pytest.raises(gate.PromptInjectionError):
        gate.scan_skill_tree(tmp_path / "absent", score_text=lambda text: 0.0)


def test_symlink_skill_is_not_scored(tmp_path):
    real = tmp_path / "outside.md"
    real.write_text("ATTACK", encoding="utf-8")
    root = tmp_path / "tree"
    root.mkdir()
    (root / "SKILL.md").symlink_to(real)
    summary = gate.scan_skill_tree(root, score_text=lambda text: 1.0 if "ATTACK" in text else 0.0)
    assert summary["files"] == []
    assert summary["needs_review"] is False


def test_too_many_files_fails_closed(tmp_path):
    for index in range(gate.MAX_SKILL_FILES + 1):
        directory = tmp_path / f"skill-{index}"
        directory.mkdir()
        (directory / "SKILL.md").write_text("notes\n", encoding="utf-8")
    with pytest.raises(gate.PromptInjectionError):
        gate.scan_skill_tree(tmp_path, score_text=lambda text: 0.0)


def test_checksum_mismatch_fails_closed(tmp_path, monkeypatch):
    def fake_retrieve(url, dest):
        Path(dest).write_bytes(b"not the model")

    monkeypatch.setattr(gate.urllib.request, "urlretrieve", fake_retrieve)
    with pytest.raises(gate.PromptInjectionError, match="Checksum mismatch"):
        gate._download("https://example.invalid/model.onnx", tmp_path / "model.onnx", "a" * 64)


def test_threshold_constant_sits_in_the_measured_gap():
    # Benign long procedure scored 0.982893; weakest clear attack scored 0.999646.
    assert 0.982893 < gate.THRESHOLD < 0.999646
    assert gate.THRESHOLD == 0.99
