#!/usr/bin/env python3
"""Score staged SKILL.md files with a pinned local classifier.

The gate replaces the Lakera Guard API. It downloads one public ONNX model,
checks its sha256, and fails closed when the download or the runtime fails.
See docs/prompt-injection.md for the threat model, the threshold, and the
limits. This module does not execute skill scripts.
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


class PromptInjectionError(RuntimeError):
    """The check could not produce a score. Callers must fail closed."""


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


def scan_skill_tree(path: Path, score_text: Optional[ScoreFn] = None) -> Dict[str, object]:
    """Return a pass/fail summary. `score_text` is for tests; production loads the model.

    `score_text` returns the injection probability of one whole file. The
    production scorer windows the file itself. A scorer exception fails the
    tree. There is no skip status.
    """
    if not path.is_dir():
        raise PromptInjectionError(f"Scan path is not a directory: {path}")
    scorer: Optional[DebertaOnnxScorer] = None
    if score_text is None:
        scorer = DebertaOnnxScorer()

    records: List[Dict[str, object]] = []
    blocking: List[str] = []
    for skill_md in _skill_files(path):
        raw = skill_md.read_bytes()
        text = raw.decode("utf-8", errors="replace")
        rel = skill_md.relative_to(path).as_posix()
        try:
            if score_text is not None:
                score, windows = float(score_text(text)), 1
            else:
                assert scorer is not None
                score, windows = scorer.score(text)
        except PromptInjectionError:
            raise
        except Exception as exc:
            raise PromptInjectionError(f"Inference failed for {rel}: {type(exc).__name__}") from exc
        record = {
            "path": rel,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "score": round(score, 6),
            "windows": windows,
        }
        records.append(record)
        if score >= THRESHOLD:
            blocking.append(f"{rel}: {record['score']}")

    summary: Dict[str, object] = {
        "status": "failed" if blocking else "passed",
        "model_id": MODEL_ID,
        "revision": MODEL_REVISION,
        "license": MODEL_LICENSE,
        "onnx_sha256": ONNX_SHA256,
        "tokenizer_sha256": TOKENIZER_SHA256,
        "threshold": THRESHOLD,
        "window_body_tokens": WINDOW_BODY_TOKENS,
        "window_stride_tokens": WINDOW_STRIDE_TOKENS,
        "blocking": blocking,
        "files": records,
    }
    return summary


def write_report(summary: Dict[str, object], dest: Path) -> None:
    dest.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def format_log(summary: Dict[str, object]) -> str:
    lines = [
        f"Prompt-injection model: {summary['model_id']}@{summary['revision']}",
        f"Threshold: {summary['threshold']} (window {summary['window_body_tokens']}/{summary['window_stride_tokens']})",
    ]
    files = summary.get("files")
    if isinstance(files, Sequence):
        for record in files:
            if isinstance(record, dict):
                lines.append(
                    f"file {record['path']} score={record['score']} "
                    f"windows={record['windows']} sha256={record['sha256']}"
                )
    for entry in summary.get("blocking") or []:
        lines.append(f"::error::Prompt-injection score at or above threshold in {entry}")
    lines.append(f"Prompt-injection check: {summary['status']}")
    return "\n".join(lines)
