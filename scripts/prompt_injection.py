#!/usr/bin/env python3
"""Score staged SKILL.md files with a pinned local classifier.

The score is a review signal. It does not decide whether a provider is added.
A high score, a scanner error, or text the script heuristic does not treat as
English asks a reviewer to look. A low score is not proof of safety.
See docs/prompt-injection.md. This module does not execute skill scripts.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import urllib.request
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

MODEL_ID = "protectai/deberta-v3-base-prompt-injection-v2"
MODEL_REVISION = "90c9989b1a342275dd0d1a95aad283c04e075671"
MODEL_LICENSE = "Apache-2.0"
ONNX_SHA256 = "f0ea7f239f765aedbde7c9e163a7cb38a79c5b8853d3f76db5152172047b228c"
TOKENIZER_SHA256 = "752fe5f0d5678ad563e1bd2ecc1ddf7a3ba7e2024d0ac1dba1a72975e26dff2f"
# Round value inside the measured gap between the strongest benign
# instruction-heavy fixture that does not quote an attack (0.9829) and the
# weakest clear trust-boundary attack (0.9996). Not fitted to submissions.
THRESHOLD = 0.99
# Model context is 512 tokens. Two tokens are reserved for [CLS] and [SEP].
WINDOW_BODY_TOKENS = 510
WINDOW_STRIDE_TOKENS = 256
MAX_SKILL_FILES = 200
# Above this, scanning would truncate. Fail closed instead of dropping a tail.
MAX_BODY_TOKENS = 200_000
CLS_ID = 1
SEP_ID = 2
INJECTION_INDEX = 1

HUGGINGFACE_BASE = "https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2/resolve"
ScoreFn = Callable[[str], float]


REVIEW_LABEL = "needs-review"
# Letter counts below this are too small for the script heuristic to call the
# file English. The heuristic is not a language identifier.
MIN_LETTERS = 40

class PromptInjectionError(RuntimeError):
    """The scorer could not produce a score. The workflow records this; it does not block."""


def iter_token_windows(n_tokens: int, width: int, stride: int) -> List[Tuple[int, int]]:
    """Cover every token. The last window always ends on the final token."""
    if n_tokens <= 0:
        return [(0, 0)]
    if width < 1 or stride < 1:
        raise PromptInjectionError("Window width and stride must be positive.")
    if n_tokens <= width:
        return [(0, n_tokens)]
    last = n_tokens - width
    starts = list(range(0, last, stride))
    if not starts or starts[-1] != last:
        starts.append(last)
    return [(start, start + width) for start in starts]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _cache_dir() -> Path:
    override = os.environ.get("PROMPT_INJECTION_CACHE", "")
    if override:
        return Path(override)
    return Path.home() / ".cache" / "agent-plugins" / "prompt-injection" / MODEL_REVISION


def _download(url: str, dest: Path, expected_sha256: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file() and _sha256(dest) == expected_sha256:
        return
    partial = dest.with_suffix(dest.suffix + ".partial")
    try:
        urllib.request.urlretrieve(url, partial)
    except Exception as exc:
        partial.unlink(missing_ok=True)
        raise PromptInjectionError(f"Could not download {url}: {type(exc).__name__}") from exc
    actual = _sha256(partial)
    if actual != expected_sha256:
        partial.unlink(missing_ok=True)
        raise PromptInjectionError(
            f"Checksum mismatch for {dest.name}: expected {expected_sha256}, got {actual}"
        )
    partial.replace(dest)


def _artifact_url(filename: str) -> str:
    return f"{HUGGINGFACE_BASE}/{MODEL_REVISION}/onnx/{filename}"


def _softmax_injection(logit_safe: float, logit_injection: float) -> float:
    shift = max(logit_safe, logit_injection)
    safe = math.exp(logit_safe - shift)
    injection = math.exp(logit_injection - shift)
    return injection / (safe + injection)


class DebertaOnnxScorer:
    """CPU scorer. Loads tokenizer.json with the tokenizers library, not Transformers."""

    def __init__(self, cache: Optional[Path] = None) -> None:
        try:
            import onnxruntime as ort
            from tokenizers import Tokenizer
        except Exception as exc:
            raise PromptInjectionError(
                "onnxruntime and tokenizers are required for the prompt-injection check"
            ) from exc
        cache = cache or _cache_dir()
        model_path = cache / "model.onnx"
        tokenizer_path = cache / "tokenizer.json"
        _download(_artifact_url("model.onnx"), model_path, ONNX_SHA256)
        _download(_artifact_url("tokenizer.json"), tokenizer_path, TOKENIZER_SHA256)
        self._tokenizer = Tokenizer.from_file(str(tokenizer_path))
        self._tokenizer.no_padding()
        self._tokenizer.no_truncation()
        try:
            import numpy as np
        except Exception as exc:
            raise PromptInjectionError("numpy is required to run the ONNX model") from exc
        self._np = np
        options = ort.SessionOptions()
        options.intra_op_num_threads = 1
        options.inter_op_num_threads = 1
        try:
            self._session = ort.InferenceSession(
                str(model_path), options, providers=["CPUExecutionProvider"]
            )
        except Exception as exc:
            raise PromptInjectionError(f"Could not load the ONNX model: {type(exc).__name__}") from exc

    def _body_ids(self, text: str) -> List[int]:
        ids = self._tokenizer.encode(text).ids
        if ids and ids[0] == CLS_ID and ids[-1] == SEP_ID:
            return list(ids[1:-1])
        return list(ids)

    def score(self, text: str) -> Tuple[float, int]:
        body = self._body_ids(text)
        if len(body) > MAX_BODY_TOKENS:
            raise PromptInjectionError(
                f"SKILL.md is too long to scan without truncating ({len(body)} tokens)"
            )
        best = 0.0
        windows = iter_token_windows(len(body), WINDOW_BODY_TOKENS, WINDOW_STRIDE_TOKENS)
        for start, end in windows:
            piece = body[start:end]
            ids = [CLS_ID, *piece, SEP_ID]
            np = self._np
            logits = self._session.run(
                None,
                {
                    "input_ids": np.asarray([ids], dtype=np.int64),
                    "attention_mask": np.ones((1, len(ids)), dtype=np.int64),
                },
            )[0][0]
            best = max(best, _softmax_injection(float(logits[0]), float(logits[INJECTION_INDEX])))
        return best, len(windows)


def script_hint(text: str) -> str:
    """Count letter scripts. Returns english, non_english, mixed, or uncertain.

    This is not a language detector. English source code next to a Chinese
    explanation counts as mixed, so the Chinese text is not ignored. A file
    with too few letters is uncertain rather than treated as English.
    """
    latin = cjk = other = 0
    for char in text:
        if not char.isalpha():
            continue
        code = ord(char)
        if code <= 0x02FF or 0x1E00 <= code <= 0x1EFF:
            latin += 1
        elif (
            0x3400 <= code <= 0x9FFF
            or 0x3040 <= code <= 0x30FF
            or 0x31F0 <= code <= 0x31FF
            or 0xAC00 <= code <= 0xD7AF
            or 0xF900 <= code <= 0xFAFF
        ):
            cjk += 1
        else:
            other += 1
    letters = latin + cjk + other
    if letters < MIN_LETTERS:
        return "uncertain"
    non_latin = cjk + other
    if non_latin >= MIN_LETTERS and latin >= MIN_LETTERS:
        return "mixed"
    if non_latin >= MIN_LETTERS:
        return "non_english"
    if latin / letters >= 0.9:
        return "english"
    return "uncertain"


def classify_advisory(files: Sequence[dict], error: str = "") -> Dict[str, object]:
    """Turn scores and script hints into a review signal. Never a safety verdict."""
    flagged = [item for item in files if float(item.get("score") or 0) >= THRESHOLD]
    outside = [item for item in files if item.get("script_hint") != "english"]
    if error:
        reason = f"advisory error: {error}. This is not a completed scan."
        return {"needs_review": True, "status": "advisory-error", "summary": _one_line(reason)}
    parts: List[str] = []
    if flagged:
        shown = ", ".join(f"{item['path']} {item['score']}" for item in flagged[:5])
        extra = "" if len(flagged) <= 5 else f" (+{len(flagged) - 5} more)"
        parts.append(f"{len(flagged)} file(s) at or above {THRESHOLD}: {shown}{extra}")
    if outside:
        shown = ", ".join(
            f"{item['path']} heuristic={item['script_hint']}" for item in outside[:5]
        )
        extra = "" if len(outside) <= 5 else f" (+{len(outside) - 5} more)"
        parts.append(
            "script heuristic (not a language detector) is outside English on "
            f"{len(outside)} file(s): {shown}{extra}. Scores there are not evidence"
        )
    if parts:
        return {"needs_review": True, "status": "needs-review", "summary": _one_line(" ".join(parts))}
    if files:
        top = max(files, key=lambda item: float(item.get("score") or 0))
        text = (
            f"no review signal. Highest score {top['score']} on {top['path']}, under {THRESHOLD}. "
            "A score under the threshold is not proof of safety."
        )
    else:
        text = "no SKILL.md files were scored. That is not proof of safety."
    return {"needs_review": False, "status": "no-review-signal", "summary": _one_line(text)}


def resolve_advisory(
    step_outcome: str,
    scan_expected: bool,
    status: str = "",
    needs_review: str = "",
    summary: str = "",
) -> Dict[str, object]:
    """Keep a missing or crashed scan visible. Do not turn it into a clear result."""
    status = (status or "").strip()
    summary = (summary or "").strip()
    flag = (needs_review or "").strip().lower()
    known = status in {"needs-review", "no-review-signal", "advisory-error"}
    if known and summary and flag in {"true", "false"}:
        review = flag == "true" or status in {"needs-review", "advisory-error"}
        return {"needs_review": review, "status": status, "summary": _one_line(summary)}
    if scan_expected:
        why = "failed" if (step_outcome or "").strip() == "failure" else "wrote no usable result"
        text = (
            f"advisory error: the prompt-injection step {why}. "
            "This is not a completed scan."
        )
        return {"needs_review": True, "status": "advisory-error", "summary": text}
    return {
        "needs_review": False,
        "status": "not-run",
        "summary": "Prompt-injection scan did not run because there was no staged skill path.",
    }


def provider_validation_passed(lgtm_passed: str, gitleaks_passed: str) -> bool:
    """LGTM and gitleaks are the hard gates. The classifier is not one of them."""
    lgtm = (lgtm_passed or "").strip()
    leaks = (gitleaks_passed or "").strip()
    return lgtm in {"true", "pending"} and leaks == "true"


def _one_line(text: str) -> str:
    cleaned = " ".join(str(text).replace("\r", " ").replace("\n", " ").split())
    return cleaned[:500]


def _skill_files(path: Path) -> List[Path]:
    files = sorted(
        candidate
        for candidate in path.rglob("SKILL.md")
        if candidate.is_file() and not candidate.is_symlink() and ".git" not in candidate.parts
    )
    if len(files) > MAX_SKILL_FILES:
        raise PromptInjectionError(
            f"Refusing to scan a prefix of {len(files)} SKILL.md files (cap {MAX_SKILL_FILES})"
        )
    return files


def _record(path: Path, root: Path, text: str, score: float, windows: int) -> Dict[str, object]:
    raw = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "score": round(float(score), 6),
        "windows": windows,
        "script_hint": script_hint(text),
    }


def scan_skill_tree(path: Path, score_text: Optional[ScoreFn] = None) -> Dict[str, object]:
    """Score the tree. Operational failures raise; `annotate` records the review signal.

    `score_text` returns one file's probability and is for tests. The production
    scorer windows the file itself.
    """
    if not path.is_dir():
        raise PromptInjectionError(f"Scan path is not a directory: {path}")
    scorer: Optional[DebertaOnnxScorer] = None
    if score_text is None:
        scorer = DebertaOnnxScorer()

    records: List[Dict[str, object]] = []
    for skill_md in _skill_files(path):
        raw_text = skill_md.read_text(encoding="utf-8", errors="replace")
        rel = skill_md.relative_to(path).as_posix()
        try:
            if score_text is not None:
                score, windows = float(score_text(raw_text)), 1
            else:
                assert scorer is not None
                score, windows = scorer.score(raw_text)
        except PromptInjectionError:
            raise
        except Exception as exc:
            raise PromptInjectionError(f"Inference failed for {rel}: {type(exc).__name__}") from exc
        records.append(_record(skill_md, path, raw_text, score, windows))
    return annotate(records)


def annotate(files: Sequence[dict], error: str = "") -> Dict[str, object]:
    advisory = classify_advisory(files, error)
    flagged = [
        f"{item['path']}: {item['score']}"
        for item in files
        if float(item.get("score") or 0) >= THRESHOLD
    ]
    summary: Dict[str, object] = {
        "status": advisory["status"],
        "needs_review": advisory["needs_review"],
        "summary": advisory["summary"],
        "model_id": MODEL_ID,
        "revision": MODEL_REVISION,
        "license": MODEL_LICENSE,
        "onnx_sha256": ONNX_SHA256,
        "tokenizer_sha256": TOKENIZER_SHA256,
        "threshold": THRESHOLD,
        "window_body_tokens": WINDOW_BODY_TOKENS,
        "window_stride_tokens": WINDOW_STRIDE_TOKENS,
        "flagged": flagged,
        "files": list(files),
    }
    if error:
        summary["reason"] = error
    return summary


def advisory_from_error(reason: str) -> Dict[str, object]:
    return annotate([], reason)


def write_report(summary: Dict[str, object], dest: Path) -> None:
    dest.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def format_log(summary: Dict[str, object]) -> str:
    lines = [
        f"Prompt-injection model: {summary.get('model_id', '')}@{summary.get('revision', '')}",
        (
            f"Review threshold: {summary.get('threshold', THRESHOLD)} "
            f"(window {summary.get('window_body_tokens', WINDOW_BODY_TOKENS)}/"
            f"{summary.get('window_stride_tokens', WINDOW_STRIDE_TOKENS)}). "
            "This does not block provider validation."
        ),
    ]
    files = summary.get("files")
    if isinstance(files, Sequence):
        for record in files:
            if isinstance(record, dict):
                lines.append(
                    f"file {record.get('path')} score={record.get('score')} "
                    f"windows={record.get('windows')} script_hint={record.get('script_hint')} "
                    f"sha256={record.get('sha256')}"
                )
    marker = "::error::" if summary.get("status") == "advisory-error" else "::warning::"
    if summary.get("needs_review"):
        lines.append(f"{marker}{summary.get('summary')}")
    lines.append(f"Prompt-injection advisory: {summary.get('status')}")
    lines.append("A score under the threshold is not proof of safety.")
    return "\n".join(lines)
