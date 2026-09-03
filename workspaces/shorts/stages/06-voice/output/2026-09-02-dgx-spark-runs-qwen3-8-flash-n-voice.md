---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
duration_s: 33.96
chars: 690
chunks: 2
wer: 0.0171
model: chatterbox
---

# Voice: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n

## Timing
| Scene | Starts at | Ends at | Seconds |
|-------|-----------|---------|---------|
| s01 | 0.00 | 5.61 | 5.61 |
| s02 | 5.61 | 11.28 | 5.67 |
| s03 | 11.28 | 17.03 | 5.75 |
| s04 | 17.03 | 22.48 | 5.45 |
| s05 | 22.48 | 30.64 | 8.16 |
| s06 | 30.64 | 34.96 | 4.32 |

## QA
- WER: 0.0171 (threshold 0.03) -- PASS, whisper.cpp ggml-base.en
- Engine: chatterbox (stock voice am_eric stand-in, seed default), alignment whisper, 3.298 wps, duration 33.96 s inside the classic vo_band_s 32-38
- Mismatches are base.en homophone/inflection variants, no synthesis error: "chwen" heard as "quen" at 8.8 s (the alias itself, correctly spoken); "quadruples" heard as "quadruple" at 29.6 s

## Normalizer expansions
- 2 scenes changed (words 114, scenes 6, scenes_changed 2): DGX -> "D G X" and Qwen3.8-Flash-Next -> "chwen three point eight Flash Next" come from the tts_lexicon aliases, counted as alias hits, not script bugs; numbers were already spoken-form

## Rounds
1. generated 2 chunks, 33.96 s, whisper alignment, QA WER 0.0171 PASS first pass
