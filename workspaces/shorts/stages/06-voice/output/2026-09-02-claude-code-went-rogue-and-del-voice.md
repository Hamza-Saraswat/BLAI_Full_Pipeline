---
slug: 2026-09-02-claude-code-went-rogue-and-del
duration_s: 122.16
chars: 2469
chunks: 5
wer: 0.0243
model: chatterbox
---

# Voice: 2026-09-02-claude-code-went-rogue-and-del

## Timing
| Scene | Starts at | Ends at | Seconds |
|-------|-----------|---------|---------|
| s01 | 0.00 | 5.84 | 5.84 |
| s02 | 5.84 | 18.72 | 12.88 |
| s03 | 18.72 | 33.76 | 15.04 |
| s04 | 33.76 | 41.04 | 7.28 |
| s05 | 41.04 | 50.48 | 9.44 |
| s06 | 50.48 | 62.72 | 12.24 |
| s07 | 62.72 | 73.36 | 10.64 |
| s08 | 73.36 | 84.88 | 11.52 |
| s09 | 85.06 | 91.04 | 5.98 |
| s10 | 91.04 | 101.76 | 10.72 |
| s11 | 101.76 | 114.40 | 12.64 |
| s12 | 114.65 | 121.92 | 7.27 |

## QA
- WER: 0.0243 (threshold 0.03) -- PASS, whisper.cpp ggml-base.en
- Engine: chatterbox (stock voice am_eric stand-in, seed 5150), alignment whisper, 3.332 wps, duration 122.16 s inside the smooth-explainer vo_band_s 60-165
- Remaining mismatches are base.en homophone/spelling variants, no synthesis error: "urbanisation" heard as "urbanization" at 26.1 s; "bug" as "bud" at 61.0 s; "and offsite" as "an off site" at 90.0 s; "ask" as "asked" at 95.1 s; "survived" as "survive" at 117.1 s
- Real fix applied: dictionary alias "Anthropic -> an-throp-ik" garbled in two separate runs (heard "and threw up icky's", "and drop its"); entry removed so the engine reads Anthropic natively, chunks 02 and 04 regenerated -- clean since

## Normalizer expansions
- None: normalize_narration.py reported 0 expansions (words 407, scenes 12, scenes_changed 0); script numbers were already spoken-form

## Rounds
1. generated 5 chunks, 125.16 s proportional alignment (whisper env vars not exported); QA WER 0.0361 FAIL
2. whisper alignment on regen, chunk 02 new seed 4243: WER 0.0312 FAIL (alias garbling persisted in two chunks)
3. removed the Anthropic alias, chunks 02+04 seed 5150: WER 0.0243 PASS, 122.16 s
