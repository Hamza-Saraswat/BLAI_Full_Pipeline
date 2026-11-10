---
slug: 2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre
format: classic
structure: number-first
style_pack: silicon
value_types: TEACHES,PROVES
promise: After this you can say which MacBook wins the long-prompt wait and why, and what it does not win.
target_duration_s: 32
brief: 2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre-brief.md
drafts: 2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre-drafts.md
---

# 374 tok/s Prefill on M5 Pro: A First-Word Upgrade

## Decisions
- Structures tried: comparison-ladder (A) and number-first (B); both cleared rotation (last two were worked-example and news-react-so-what). B won 22-20 on the judge rubric: one number per beat, the SSD-streaming mechanism shown, repeatable catchline last. No grafts.
- Hook: number-shock (candidate 2) over decision (candidate 1): 374 lands at second zero with the prefill qualifier; decision pattern went to draft A and lost with it.
- Value lines: TEACHES "His explanation: not the GPU, not even memory bandwidth, but a faster SSD streaming in the experts each token needs." PROVES "Decode, the actual writing, only reaches thirteen point one four tokens a second."
- Machine gates: validator 0 blockers 0 advisories on the winner (after 7 fix passes: layout_archetype, digits in narration, chip-name spoken forms, hook word count, tail collapse, on-screen number forms); eval all gates pass; sameness ok vs last 5; normalizer scenes_changed=1 (M4/M5 spoken forms).

## Hook candidates
1. M4 Pro or M5 Pro? One number decides.
2. Three hundred seventy four tokens a second, and not one is the answer.
3. Your Mac reads the prompt fast. Writing the answer is the slow part.
4. A 125 billion parameter model on a 24 GB Mac, at 8.5 GB of RAM.
5. Same model, same quant, same memory. Double the speed.
6. The new MacBook's SSD just doubled your prefill.
7. 199 versus 374. The chip didn't get twice as fast.
8. You paste a long document. The cursor blinks. That's prefill.
9. The wait before the first word is the benchmark nobody runs.
10. Faster storage, not a faster GPU, moved this number.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Three hundred seventy four tokens a second. None of them is the answer. | 374 tok/s, all prefill | Frame 1: giant digits '374 tok/s' centered on dark silicon background, fully legible; on 'and not one', caption 'all prefill, no answer' fades in below; scale-settle of the digits within 0.5 s, first and last 8 frames stable. | manim | giant-number | 4.5 |
| s02 | explain | Prefill reads your whole prompt before answering. You know that blinking cursor; everyone says only the newest chip fixes it. | Prefill: the wait before word one | On 'reads your whole prompt', a long document fades in with a pulsing caret at its end; on 'blinking cursor' the caption fades in beneath it. | hyperframes | diagram-flow | 6.9 |
| s03 | explain | MoEShift's author ran both chips himself, same model, same quant. M four Pro prefill: one hundred ninety nine tokens a second. | M4 Pro: 199 tok/s prefill | On 'one hundred ninety nine', a single bar rises in place labeled '199 tok/s' under an 'M4 Pro' tag, sitting short against conspicuous empty headroom. | manim | split-compare | 7.2 |
| s04 | explain | His explanation: not the GPU, not even memory bandwidth, but a faster SSD streaming in the experts each token needs. | 307 vs 273 GB/s | On 'streaming in the experts', an SSD icon fades in at left and small blocks labeled 'experts' drift from it toward a RAM pool icon at right; a dimmed 'GPU' label stays static. | hyperframes | diagram-flow | 6.9 |
| s05 | payoff_close | Decode, the actual writing, only reaches thirteen point one four tokens a second. A first-word upgrade, not a chat-speed upgrade. | Decode: 13.14 tok/s | On 'thirteen point one four' the decode number card fades in; on 'A first-word upgrade' a hard cut swaps to a plain card reading 'A first-word upgrade, not a chat-speed upgrade', held static to the end. | hyperframes | centered-stack | 6.9 |

## Notes for review
- The 374 figure is the runtime author's own HN benchmark (community tier); narration says "MoEShift's author ran both chips himself", never an independent-verification claim.
- Decode numbers (13.14) are rounded to "thirteen point one four" verbatim in narration; on screen carries digits.
- Rounds spoken: "one hundred twenty five billion parameters" (125B), "six billion active" (6B). Bandwidth pair (307/273) is on screen only, never spoken, to respect the 2-5 number budget.
