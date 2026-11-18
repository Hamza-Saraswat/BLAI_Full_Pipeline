---
slug: 2026-11-18-deepseek-v4-pro-nvfp4-which-gp
stage: 04-script
generated_at: 2026-11-18T13:20:00Z
---

# Drafts: 2026-11-18-deepseek-v4-pro-nvfp4-which-gp

Writer A: number-first, hook "Which GPUs can load DeepSeek?" (decision).
Writer B: contrarian-take, hook "Your GPU was never the problem." (situation).
Both boards passed validator (0 blockers) and all nine eval gates before judging.

## Draft A (number-first)
| Scene | Role | Narration | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-----------|----------------|--------------|------|--------|-------|
| s01 | hook | Nine hundred forty-one gigabytes on disk. That's the four-bit cut of DeepSeek's biggest model you want on your gaming rig. | 941 GB / DeepSeek V4 Pro NVFP4 / the 4-bit cut | Frame 1: pinned headline 'Which GPUs can load DeepSeek?' on top, giant silver '941 GB' centered on dark silicon with a faint die shot behind. At t=0.30 the digits fade from dim to full with a slight scale-up. On 'four-bit cut' a small '4-bit' chip tag fades in beneath; on 'gaming rig' a desktop tower outline rises in place, dwarfed by the number. | hyperframes | giant-number | 6.9 |
| s02 | explain | It's a company of specialists with a receptionist. She wakes only the few each word needs, forty-nine billion weights per word. She re-picks every word, never one hand-off. Every specialist stays on staff. | mixture of experts / receptionist = router / 49B weights per word / every expert stays in memory | Diagram-flow on dark silicon: on 'company of specialists' a grid of many dim office doors fades in; on 'receptionist' a front-desk dot pulses at the edge. On 'wakes only the few each word needs' two doors light per tick while the rest stay dim, '49B' fading in over the lit pair. On 're-picking every word' the lit pair swaps. On 'stays on staff' the whole grid brightens, everyone resident. | hyperframes | diagram-flow | 11.4 |
| s03 | explain | Ninety-six gigabytes of memory, NVIDIA's biggest workstation card, falls short. One hundred twenty-eight gigabytes in NVIDIA's Spark box: still short. Only a Mac Studio with five hundred twelve gigabytes clears it. | RTX PRO 6000: 96 GB / short / DGX Spark: 128 GB / still short / Mac Studio M5 Ultra: 512 GB / clears it | Split-compare: a tall ghost bar labeled '941 GB' fixed on the left as the line to beat. On 'ninety-six gigabytes' an RTX PRO 6000 bar rises in place to a sliver of it; on 'one hundred twenty-eight' a DGX Spark bar rises slightly higher, still below; on 'five hundred twelve' the Mac Studio bar rises past the checkpoint line and flashes 'clears it'. | hyperframes | split-compare | 10.7 |
| s04 | explain | NVIDIA validated it on Blackwell datacenter chips; older cards run it slower. | validated: Blackwell datacenter / older GPUs: slower weight-only path | Thin horizontal timeline, two nodes, no numbers. On 'validated it on Blackwell datacenter chips' the first node lights bright, a datacenter Blackwell chip icon fading in above it. On 'older cards run it slower' the second node lights dim amber with a slow-crawling progress bar beneath, contrasting the first node's full bar. | hyperframes | timeline | 4.1 |
| s05 | payoff_close | So match your memory tier first, because four-bit never promised fit. | match your memory tier / 4-bit never promised fit | Centered-stack on a clean dark background: on 'match your memory tier first' a checklist card fades in with 'memory tier' ticked at the top. On 'four-bit never promised fit' a grayed '4-bit' badge sinks to the bottom of the stack. The final frame holds the stack still, nothing after it. | hyperframes | centered-stack | 3.8 |

## Draft B (contrarian-take, pre-graft)
| Scene | Role | Narration | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-----------|----------------|--------------|------|--------|-------|
| s01 | hook | You checked if DeepSeek's biggest model fits your card. It is nine hundred forty-one gigabytes on disk. | DeepSeek-V4-Pro-0813-NVFP4  /  941 GB on disk  /  will it fit? | Frame 1: pinned headline 'Your GPU was never the problem.' sits top-center above a giant '941 GB' numeral on a dark silicon-die texture. At t=0.30 the numeral fades in with a slow scale-up as 'nine hundred forty-one gigabytes' lands. On 'fits your card' a small graphics-card outline rises-in-place below, visibly dwarfed by the digits. Circuit traces pulse faintly at the edges. | hyperframes | centered-stack | 5.9 |
| s02 | explain | The consensus: four-bit, so it fits. Quantization stores weights in fewer bits; the file shrinks, not the count. | 4-bit, so it fits?  /  file shrinks  /  weight count doesn't | Split screen. On 'The consensus', left panel shows a bold '4-bit' badge over a gaming card, right panel shows a shelf of weight tiles. On 'stores weights in fewer bits' the left file icon compresses to a quarter of its size. On 'not the count' the right tiles hold their grid, then replicate until the wall is full. Labels swap with a soft tick. | hyperframes | split-compare | 6.2 |
| s03 | explain | Picture a company of specialists; a receptionist wakes the few each word needs. She re-picks every time. Forty-nine billion parameters answer one word; the whole staff fills memory. | specialists: all resident  /  receptionist routes each word  /  49B params per token | Diagram flow on dark silicon. On 'company of specialists' a grid of glowing specialist chips fades in. On 'a receptionist wakes the few' a router node lights paths to a few chips; each word-token pulse re-lights a different few ('re-picking every time'). On 'the whole staff fills memory' the entire grid sinks into a memory block that fills to the brim. | hyperframes | diagram-flow | 9.7 |
| s04 | explain | NVIDIA's biggest workstation card: ninety-six gigabytes of memory. A desktop box reaches one hundred twenty-eight gigabytes of memory. | 96 GB RTX PRO 6000  /  128 GB DGX Spark unified  /  both fall short | Giant number stage. On 'ninety-six gigabytes' the numeral '96 GB' scales in over a workstation-card silhouette while an unlabeled checkpoint bar beside it towers far taller. On 'one hundred twenty-eight' the numeral swaps to '128 GB' over a small desktop box, still short of the same bar. End: both labels dim beneath the persistent bar. | hyperframes | giant-number | 6.2 |
| s05 | payoff_close | Only a Mac Studio with five hundred twelve gigabytes of memory clears the weights alone, before the chat's memory joins. Add up the memory tier before trusting a format name. | 512 GB Mac Studio M5 Ultra  /  + KV cache on top  /  count memory first | Centered stack. On 'five hundred twelve gigabytes' the numeral '512 GB' rises-in-place over a Mac Studio outline and finally tops the checkpoint bar behind it. On 'conversation memory joins' a small block labeled 'KV cache' stacks above the weights, eating the headroom. Final frame: 'count memory first' fades in centered and holds on clean silicon. | hyperframes | centered-stack | 10.3 |

## Judge scores (kimi-k3, blind)
| Row | A (number-first) | B (contrarian-take) |
|-----|------------------|----------------------|
| 1. Hook | 3 | 3 |
| 2. Payoff timing | 3 | 2 |
| 3. Specificity | 3 | 3 |
| 4. Voice | 3 | 3 |
| 5. Navigation | 2 | 3 |
| 6. Difference | 1 | 2 |
| 7. Repeat test | 3 | 2 |
| 8. Teaching | 2 | 3 |
| Totals | 20 | 21 |

## Winner
B, by 1 (21 to 20). B's arc (consensus stated, broken, mechanism shown, ladder climbed, verdict) has no detachable beat, where A's Blackwell caveat deletes clean (row 5); B teaches the actual mechanism so a viewer can predict cases the script never mentions (row 8); B's situation open is a fresh rhythm against a ledger whose last two entries opened number-shock and named-contradiction (row 6). A kept the faster payoff (number by second 2) and the best single line, which the graft recovers.

## Grafts
- Sentence graft (1 of max 2): A's "So match your memory tier first, because four-bit never promised fit." replaces B's s05 close "Add up the memory tier before trusting a format name." Same lesson, measurably better line, lands as the last thing heard (row 7); no numbers, person, or structure change.
- No hook graft: row-1 margin is 0, not the required 2.
- A's Blackwell-validation sentence rejected as a graft: would add a beat and force transitions.

## What the loser needed
Number-first needed to spend its instant-payoff dividend somewhere the ledger was not already spent (11-14 and 11-17 both opened on a shock number; runtime 0.1 s off 11-13's 37.0; rule-imperative close). It also needed B's mechanism taught explicitly, which would have made the Blackwell beat load-bearing instead of ornamental.
