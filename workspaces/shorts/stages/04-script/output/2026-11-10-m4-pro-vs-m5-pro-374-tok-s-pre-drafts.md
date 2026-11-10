---
slug: 2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre
stage: 04-script
winner: B
scores: A 20 - B 22
generated_at: 2026-11-10T13:20:00Z
hub: "[[videos/2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre]]"
---

# Drafts and judge verdict

## Draft A (comparison-ladder, hook: decision)
hook: M4 Pro or M5 Pro? One number.

| Scene | Role | Narration | On-screen | Visual brief | Tool | Layout | Est s |
|-------|------|-----------|-----------|--------------|------|--------|-------|
| s01 | hook | M four Pro or M five Pro? One number decides. Three hundred seventy four tokens a second, your tiebreaker. | 374 tok/s prefill | Frame 1: two chip cards 'M4 Pro' and 'M5 Pro' side by side on dark silicon background, both fully legible; on 'One number decides', the digits '374' scale in between them; motion onset at 0.30 s, cards hold stable first and last 8 frames. | hyperframes | giant-number | 6.6 |
| s02 | explain | Prefill: your pasted document, read before the first word appears. | prefill on Apple Silicon | On 'your pasted document', a page icon rises in place at left and its text streams into a block at right where a cursor waits; only the stream animates while the caption fades in, ending static. | hyperframes | diagram-flow | 3.4 |
| s03 | explain | The runtime's own benchmark: eighty three point nine seconds on M four Pro. M five Pro: fifty five point one. | long prompt 83.9 vs 55.1 s | On 'eighty three point nine seconds', a long horizontal wait bar labeled M4 Pro 83.9 s rises in place; on 'fifty five point one', a shorter M5 Pro 55.1 s bar rises beside it; both hold static. | hyperframes | split-compare | 6.9 |
| s04 | explain | Prefill made the gap: one hundred ninety nine on M four Pro, three hundred seventy four on M five Pro. | 199 vs 374 tok/s prefill | Hard cut from the wait bars to two speed bars flipped in meaning: on 'one hundred ninety nine' a short M4 Pro bar scales in labeled 199 tok/s, and on 'three hundred seventy four' a long M5 Pro bar scales in labeled 374 tok/s. | hyperframes | timeline | 6.9 |
| s05 | explain | Its author credits the SSD, not the GPU. The model is one hundred twenty five billion parameters, six billion active per word, on either chip. | 125B parameters 6B active | On 'credits the SSD', an SSD chip icon streams small expert blocks along a dotted path into two identical laptop silhouettes that both glow to show the same model fits; the caption fades in beneath, two elements moving at most. | hyperframes | diagram-flow | 8.6 |
| s06 | explain | The catch: answers still type out in no hurry. First-word upgrade, not chat-speed. | decode: 13.14 tok/s | On 'answers still type out in no hurry', a single answer line types itself out slowly one token at a time under the static caption, deliberately unhurried, then freezes. | hyperframes | grid | 4.5 |
| s07 | payoff_close | Long documents make the M five Pro your chip; short prompts run fine on either. | long docs: M5 Pro | On 'The M5 Pro is your chip', the decision line rises in place center screen with the M5 Pro card from the hook beside it; everything holds static through the final word. | hyperframes | centered-stack | 5.2 |

## Draft B (number-first, hook: number-shock)
hook: 374 tok/s. None is the answer.

| Scene | Role | Narration | On-screen | Visual brief | Tool | Layout | Est s |
|-------|------|-----------|-----------|--------------|------|--------|-------|
| s01 | hook | Three hundred seventy four tokens a second. None of them is the answer. | 374 tok/s, all prefill | Frame 1: giant digits '374 tok/s' centered on dark silicon background, fully legible; on 'and not one', caption 'all prefill, no answer' fades in below; scale-settle of the digits within 0.5 s, first and last 8 frames stable. | manim | giant-number | 4.5 |
| s02 | explain | Prefill reads your whole prompt before answering. You know that blinking cursor; everyone says only the newest chip fixes it. | Prefill: the wait before word one | On 'reads your whole prompt', a long document fades in with a pulsing caret at its end; on 'blinking cursor' the caption fades in beneath it. | hyperframes | diagram-flow | 6.9 |
| s03 | explain | MoEShift's author ran both chips himself, same model, same quant. M four Pro prefill: one hundred ninety nine tokens a second. | M4 Pro: 199 tok/s prefill | On 'one hundred ninety nine', a single bar rises in place labeled '199 tok/s' under an 'M4 Pro' tag, sitting short against conspicuous empty headroom. | manim | split-compare | 7.2 |
| s04 | explain | His explanation: not the GPU, not even memory bandwidth, but a faster SSD streaming in the experts each token needs. | 307 vs 273 GB/s | On 'streaming in the experts', an SSD icon fades in at left and small blocks labeled 'experts' drift from it toward a RAM pool icon at right; a dimmed 'GPU' label stays static. | hyperframes | diagram-flow | 6.9 |
| s05 | payoff_close | Decode, the actual writing, only reaches thirteen point one four tokens a second. A first-word upgrade, not a chat-speed upgrade. | Decode: 13.14 tok/s | On 'thirteen point one four' the decode number card fades in; on 'A first-word upgrade' a hard cut swaps to a plain card reading 'A first-word upgrade, not a chat-speed upgrade', held static to the end. | hyperframes | centered-stack | 6.9 |

## Scores
| Row | A | B |
|-----|---|---|
| hook | 3 | 3 |
| payoff_timing | 2 | 2 |
| specificity | 2 | 3 |
| voice | 3 | 3 |
| navigation | 3 | 3 |
| difference | 3 | 2 |
| repeat | 2 | 3 |
| teaching | 2 | 3 |
| total | 20 | 22 |
| **total** | **20** | **22** |

## Winner: B
B paces one number per beat, shows the SSD-streaming-experts mechanism concretely enough to transfer to unmentioned cases, and lands its repeatable catchline as the last thing heard, while A restates the same gap twice in different units, leaves the SSD mechanism asserted rather than shown, and spends its best line one beat before the close.

## Grafts
none

## Losing shape postmortem
The ladder needed its final rung to be the catchline — ending on the verdict instead of 'First-word upgrade, not chat-speed' wasted its most repeatable phrase. It also needed to say the mechanism aloud (experts streaming per token) rather than hoping the 125B/6B juxtaposition would do the work, and to pick either wall-clock or rate for the gap instead of both.

## Value lines (winner)
- TEACHES: His explanation: not the GPU, not even memory bandwidth, but a faster SSD streaming in the experts each token needs.
- PROVES: Decode, the actual writing, only reaches thirteen point one four tokens a second.
