# Prompt-injection check

The provider workflow scores every staged `SKILL.md` on CPU and, when the
result needs a person, adds the `needs-review` label and a one-line summary.
That signal does not fail validation and does not block the add-provider pull
request. LGTM and gitleaks remain the hard gates. A score under the threshold
is not proof of safety. This check does not execute files from the submission.

## Threat model

A skill file is untrusted text that this directory later hands to an agent as
instructions. "This file tells an agent what to do" is the product, so
instruction-heavy writing is not evidence of an attack.

The gate is aimed at a narrower boundary:

- text that tells the agent to override a higher-priority instruction, including
  the developer policy or the user's approval
- text that tells the agent to copy credentials, tokens, or private keys out to
  a destination the skill author controls

A sentence such as "ignore the previous draft formatting" or "do not paste
private keys into the chat" stays on the benign side of that boundary.

## Choice

Checked on 8 Nov 2026.

| Candidate | License | Access | Maintenance | Result |
| --- | --- | --- | --- | --- |
| Llama Prompt Guard 2 (22M and 86M) | Llama 4 Community License, not an OSI license | Hugging Face `gated: manual`. A token is required. | Weights published 29 Apr 2025 | Not usable here. No secret is available, and the license is not open source. |
| ProtectAI DeBERTa v2 | Apache-2.0 | Public, ungated | Model card archived 9 Jul 2026. Weights are the 2024 fine-tune. | Selected. It is the only listed model that is OSI-licensed, ungated, and CPU-sized, and it is the one that separated clear attacks from short English skill text. |
| LLM Guard | MIT code | Public | Repository archived 8 Jul 2026. Last release 19 May 2025. The injection scanner is the DeBERTa model above. | Not selected. It adds a frozen toolkit around the same weights. |
| Rebuff | Apache-2.0 | Public | Archived 16 May 2025. Last release 20 Jan 2024. | Not selected. The default detector calls OpenAI. |
| Vigil | Apache-2.0 | Public | Last push 31 Jan 2024. Last release 31 Dec 2023. Alpha. | Not selected. Unmaintained, and its transformer path points at an older DeBERTa checkpoint. |
| PromptPurify (`Securelayer7/promptpurify`) | MIT | Public ONNX, ungated | Last push 31 May 2026. 80 GitHub stars. 0 Hugging Face downloads at measurement time. | Measured and rejected. See below. |

Prompt Guard 2's own card describes the right label ("explicitly attempts to
override prior instructions") but the weights cannot be downloaded without
accepting a gated license. Granite Guardian 4.1 is Apache-2.0 and maintained,
and it is an 8B generative model, which is the wrong shape for a CPU Actions
job.

Pinned artifact:

- model: `protectai/deberta-v3-base-prompt-injection-v2`
- revision: `90c9989b1a342275dd0d1a95aad283c04e075671`
- ONNX sha256: `f0ea7f239f765aedbde7c9e163a7cb38a79c5b8853d3f76db5152172047b228c`
- tokenizer.json sha256: `752fe5f0d5678ad563e1bd2ecc1ddf7a3ba7e2024d0ac1dba1a72975e26dff2f`
- runtime: `onnxruntime==1.31.1`, `tokenizers==0.23.3`, one intra-op thread
- loader: `tokenizers.Tokenizer.from_file` and ONNX Runtime. `trust_remote_code` is not used.

The model card says the classifier is English-only, does not target jailbreaks
as a separate label, and should not be used on system prompts because it false
positives. Those limits showed up in the measurements.

## Threshold

`0.99` sits in the gap measured on fixtures written for this check, before the
seven submissions were used to choose it.

- strongest benign instruction fixture that does not quote an attack
  (`skill_long_procedure`): **0.982893**
- weakest clear attack fixture (`exfil_keys`, read secrets and POST them):
  **0.999646**

Other clear attacks (`override_system`, `approval_bypass`, holdout
`paraphrase_exfil`) scored 0.9998 to 1.0. Short English skill fixtures scored
below 0.01. The threshold was not moved to change the seven submissions.

## What the measurements showed

PromptPurify, at its own 500-character windows, scored the credential-exfil
fixture at **0.000048** and the approval-bypass fixture at **0.000002**. The
same model scored an ordinary deploy-notes skill at **0.969** and a review
skill at **0.767**. No threshold both catches those attacks and lets ordinary
skill text through. Its classic "ignore previous instructions / DAN" fixture
did score 0.9999, so a demo that only uses that sentence overstates it.

DeBERTa at a 510-token window (the model maximum, stride 256, tail always
included):

| Fixture | Score |
| --- | --- |
| changelog skill | 0.000813 |
| review skill | 0.000095 |
| deploy notes | 0.008656 |
| long repeated procedure | 0.982893 |
| skill that quotes an attack in order to explain it | 1.0 |
| override / DAN | 1.0 |
| exfiltrate keys | 0.999646 |
| skip approval and export tokens | 0.999843 |
| paraphrased exfil (holdout) | 1.0 |
| short attack appended to the changelog skill | 0.004756 |
| short attack inserted into the review skill | 0.000310 |

Shrinking the window to 128 or 256 tokens did not catch the buried attacks
(0.064 and 0.005). It did flag ordinary English skills: at 128 tokens the
tree-ring skill scored 1.0 and the Magic Hour image-edit skill scored 0.9945.
The 510-token window is the one that keeps those two under the threshold.
Full-file coverage is still required so a hostile file is not truncated away.
Coverage is not the same as detecting one hostile sentence inside a benign file.

## The seven submissions

Scored from the commits that were `origin/main` at the 8 Nov 2026 Lakera runs.
Issue 109 was closed by its author and was not scored. Bodies are not stored
here. Hashes, scores, and window counts are in
[prompt-injection-benchmark.json](prompt-injection-benchmark.json).

| Issue | Commit | Files | Max score | At 0.99 | CPU seconds |
| --- | --- | --- | --- | --- | --- |
| 136 | `34c027026b65` | 1 | 0.992630 | fail | 12.2 |
| 132 | `9f1e7df4051e` | 22 | 0.654701 | pass | 81.9 |
| 130 | `23cddf05c49c` | 1 | 0.046281 | pass | 18.7 |
| 125 | `5d608cd58ed5` | 33 | 0.023205 | pass | 74.3 |
| 113 | `cbab58188611` | 83 | 0.489605 | pass | 124.8 |
| 111 | `9462f1e546b9` | 1 | 0.488560 | pass | 4.5 |
| 92 | `930446519f8d` | 1 | 0.013054 | pass | 15.2 |

Loading the ONNX session from a warm disk took 3.2 seconds. Downloading the
704 MB ONNX file on this host took about 6 seconds; GitHub-hosted runners will
be slower. These times are one thread, on top of `pip install`.

Issue 136 is a Chinese browser-extension workflow. The model card says the
classifier does not handle non-English text. The score is above the threshold,
so the gate fails the file. That failure is not, by itself, evidence of an
attack, and a lower score on another non-English file would not be evidence of
safety. Issue 111 is also Chinese and scored 0.49, under the threshold.

The highest English score among the other six is Magic Hour's image-edit skill
at 0.65. Read as data, that file tells the agent how to edit an image and says
not to send the API token to storage. It is under the threshold. The old Lakera
`prompt_attack` labels on these seven had no spans and no scores, so this run
does not confirm or dismiss those labels.

## Advisory interpretation

The numbers above are unchanged. They come from the blocking experiment: at
0.99 used as a hard gate, issue 136 would have failed validation and the other
six would have passed. David then asked for an advisory detector. The same
scores now only ask for review.

A file asks for review when its score is at least 0.99, when the scanner
errors, or when a character-script heuristic does not call the file English.
The heuristic counts Latin letters against CJK and other letters. It is not a
language identifier. A Chinese explanation with English code is `mixed`, so
the Chinese text is not dropped. Too few letters is `uncertain`, not English.
Non-English, mixed, and uncertain text asks for review even when the score is
under 0.99, and the summary says the score is not evidence there.

Applied to the same files, without rescoring the model:

| Issue | Max score | Script heuristic | Advisory | Blocks the provider? |
| --- | --- | --- | --- | --- |
| 136 | 0.992630 | mixed (Chinese workflow plus English code words) | needs-review | no |
| 132 | 0.654701 | english on all 22 files | no review signal | no |
| 130 | 0.046281 | english | no review signal | no |
| 125 | 0.023205 | english on all 33 files | no review signal | no |
| 113 | 0.489605 | mixed on `douyin-research`, `weibo-research`, and `xiaohongshu-research`; english on the other 80 | needs-review | no |
| 111 | 0.488560 | mixed (Chinese reader plus English markup) | needs-review | no |
| 92 | 0.013054 | english | no review signal | no |

Issues 132, 130, 125, and 92 do not ask for review. That is not an approval
and not proof of safety. LGTM and gitleaks on the 8 Nov runs had already
passed; those two gates are what would still block a provider.

## Limits

This is a single English classifier score. It is not a guarantee.

- A short hostile sentence inside a longer benign skill scored under 0.07 at
  every window size that did not also flag ordinary skills.
- A skill that quotes an attack, in order to tell the agent not to follow it,
  scored 1.0.
- Repetitive imperative text scored 0.983, just under the threshold.
- The model is archived. New attack wording will not be trained in.
- Non-English text is outside the training scope described by the model card.
- The other gates still matter. This one does not look for secrets or for
  skill-spec errors.

## Failure behavior

A missing dependency, a failed download, a checksum mismatch, an over-long
file, an inference error, or a scanner step that crashes before it writes a
result is an advisory error. The log marks it with `::error::`, the status is
`advisory-error`, and `needs-review` is still requested. It is not reported as
a completed scan, and it does not by itself stop the add-provider pull request.
If gitleaks or LGTM fail, their failure still blocks, and the review signal
stays on the issue.
