import os
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


def test_threshold_blocks_a_high_score_and_passes_a_low_score(tmp_path):
    skill = tmp_path / "demo"
    skill.mkdir()
    (skill / "SKILL.md").write_text("ordinary procedure\n", encoding="utf-8")
    low = gate.scan_skill_tree(skill, score_text=lambda text: 0.01)
    assert low["status"] == "passed"
    assert low["blocking"] == []
    assert low["files"][0]["score"] == 0.01

    high = gate.scan_skill_tree(skill, score_text=lambda text: 0.999)
    assert high["status"] == "failed"
    assert high["blocking"] == ["SKILL.md: 0.999"]


def test_scorer_exception_fails_closed(tmp_path):
    skill = tmp_path / "demo"
    skill.mkdir()
    (skill / "SKILL.md").write_text("text\n", encoding="utf-8")

    def broken(text):
        raise OSError("runtime broke")

    with pytest.raises(gate.PromptInjectionError):
        gate.scan_skill_tree(skill, score_text=broken)


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
    assert summary["status"] == "passed"
    assert summary["files"] == []


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
