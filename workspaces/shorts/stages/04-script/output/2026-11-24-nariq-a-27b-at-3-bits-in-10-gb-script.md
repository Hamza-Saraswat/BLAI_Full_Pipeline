---
slug: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb
format: smooth-explainer
structure: contrarian-take
style_pack: silicon
value_types: TEACHES,REFRAMES
promise: after this Short the viewer knows why a 3-bit file can hold a 27B model's quality, and that memory, not intelligence, is the wall
target_duration_s: 127
brief: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb-brief.md
drafts: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb-drafts.md
---

# NariQ: a 27B at 3 bits, in 10 GB

## Decisions
- Two structures tried: news-react-so-what (draft A) and contrarian-take (draft B); both cleared the rotation rule against the last two ledger entries (myth-bust 2026-11-22, worked-example 2026-11-23). Judge total A=19 B=20; winner draft B (contrarian-take).
- Hook: Not the card. The file. (named-contradiction pattern; 10 candidates scored, the two picks from two different patterns).
- Round 1 was withdrawn by the rotation gate: worked-example and myth-bust both repeat the last two ledger entries (11-23 and 11-22), and number-shock repeats 11-22's hook; both drafts were re-assigned legal shapes (news-react-so-what / contrarian-take, situation / named-contradiction) and re-written blind on 2026-11-24.
- Grafts: Move A's opening sentence, "You downloaded a twenty-seven billion parameter model and it would not fit," to the top of B's first scene, before "Your card isn't too small." Allowed because the loser's hook scores 3 against the winner's 1 (at least 2 higher), it is a single sentence, it is the same second person, scene one's heard numbers go from two to three which sits at the cap, and the named-contradiction still lands inside scene one so B's contrarian spine and its "card was never the problem" callback stay intact. LOSER_NEEDS: A reported the scores without the mechanism that explains them -- the trellis coding and agent-trace calibration -- so it could teach bits-as-size but never why this quant broke the 3-bit curse. It also needed a payoff that stands alone as one quotable sentence, on a shape and a wall-callback landing the recent run hadn't already spent. REPEAT_LINE: The only question left is what memory you have.
- Gates: validator zero blockers; eval hard gates pass; variety check clean vs last 5; normalized narration written.
- Value delivery: TEACHES = the quantization mechanism scene; REFRAMES = the payoff line.
- Analogy: rounding pi, one analogy, limit stated in the same breath.

## Hook candidates
- Not the card. The file. (named-contradiction, 6/7 *) -- wrong diagnosis in five words; frame-1 legs; the grafted hook's frame-1 form
- You downloaded a 27B model and it would not fit. (situation, 6/7) -- the grafted winner's opener; situation + product + wall
- 27B in 10 GB, at 3 bits. (number-shock, 5/7) -- three specifics in five words; frame-1 legs
- Ten gigabytes now holds a twenty-seven billion parameter model. (number-shock, 6/7) -- the arresting fact, words not digits, repeatable
- A 27B model that fits a 12 GB card. (number-shock, 5/7) -- product+capability+number; the viewer's own box
- Quantization didn't wreck this one. (wrong-diagnosis, 4/7) -- contradiction but no number; requires setup
- The 3-bit file that benchmarks like BF16. (named-contradiction, 5/7) -- the claim itself; 'like' is honest
- 10.12 GB. That's the whole 27B. (number-shock, 5/7) -- verbatim number first; repeatable
- NariQ: 27B at 3 bits, in 10 GB. (named-contradiction, 5/7) -- name+numbers; catalog-style
- The memory wall just moved. (other, 3/7) -- metaphor, no specific; weak

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You downloaded a twenty-seven billion parameter model and it would not fit. Your card isn't too small. The file is. The full-precision original of the model you gave up on needs about fifty-three gigabytes. Your card holds twelve gigabytes. | Not the card. The file. \| 53.8 GB full file \| 12 GB your card | SILICON die shot, finished composition at frame one: a dark substrate, a giant dimmed '27B' etched on the die with a red 'didn't fit' chip beside it. On 'Your card isn't too small', the chip clears to amber and the etched '53.8 GB' numeral scales in above a small '12 GB' memory bar. On 'twelve gigabytes', the bar rises-in-place and pulses once. Fades and scale only, motion starts after the opening beat. | hyperframes | giant-number | 13.4 |
| s02 | explain | Everyone running local models learned the rule. Quantization, fewer bits per stored number, always costs quality. Below four bits a model is supposed to fall apart. A twenty-seven billion parameter model is supposed to need a workstation. | quantization costs quality \| under 4 bits falls apart \| 27B params need a workstation | Centered stack on a dark PCB field: three etched rule cards stack vertically, each fading in on its own phrase: 'quantization costs quality', then 'under 4 bits falls apart', then '27B needs a workstation'. As 'supposed to need a workstation' lands, a hairline crack fades across the whole stack. Hard cut in from the previous scene, no sliding elements. | hyperframes | centered-stack | 12.8 |
| s03 | explain | Here is the evidence against it. NariQ is a three-bit compression of Qwen3.8-27B, built by Nari Labs. The GGUF, the single file your local tools load, is ten point one two gigabytes. On DeepSWE, a benchmark of real software tasks, it scored forty-one against the original's thirty-nine point eight. Every earlier attempt at or below three bits fell further behind. | NariQ 3-bit GGUF \| 10.12 GB \| DeepSWE 41.0 vs 39.8 | Split-compare of two die packages on one substrate. Left: a slim die labeled 'NariQ 3-bit'; its size bar fills on 'ten point one two gigabytes' under a '10.12 GB' tag. Right: a tall die for the original. On 'forty-one against', the numerals '41.0' and '39.8' scale in above the dies beneath a 'DeepSWE' header. | hyperframes | split-compare | 20.7 |
| s04 | explain | Why does it hold up? The original stores every parameter, each a stored number, in BF16, the model's full sixteen-bit memory. Quantization rounds each number down to three bits. Picture rounding pi from five decimal places to three point one. Close enough for most work; exact math notices first, casual chat never does. NariQ's twist is trellis coding, choosing which numbers to flatten together so the rounding errors cancel instead of stacking. It was tuned on tokens the full model wrote during real agent sessions. | BF16: full memory \| quant: 3 bits \| pi: 5 decimals to 3.1 \| trellis: errors cancel | Diagram-flow across a die cross-section: a left column of memory cells marked 'full', arrows converging right into compact cells marked '3 bits'. On 'rounds each number down to three bits', the cells scale down in place. On the pi phrase, a margin annotation 'pi: 5 decimals to 3.1' fades in. On 'errors cancel instead of stacking', paired plus and minus ticks along the arrows fade out in pairs. At most two elements animate at once. | hyperframes | diagram-flow | 25.0 |
| s05 | explain | Now the narrower claim this earns. One file, one benchmark family, four days old. Every quality number comes from the publisher's own tests, so the only referee so far is grading its own homework. | 1 file \| 1 benchmark family \| 4 days old \| scores self-graded | Timeline archetype: a short horizontal track etched like a circuit trace, a single die icon labeled 'NariQ GGUF' at its left end and a 'today' marker at the right; the gap tag '4 days' fades in on 'four days old'. Above the track, the tags '1 file' and '1 benchmark family' fade in on their phrases. On 'grading its own homework', a magnifier lens rises-in-place over a stamp reading 'self-graded'. | hyperframes | timeline | 11.7 |
| s06 | explain | Stock llama.cpp, the engine under the usual local tools, cannot load the file yet. Neither can Ollama or LM Studio; you would need the Nari Labs fork. That fork is slower than stock quants, the usual compressed files, on most hardware, with one exception, a workstation-class GPU. Support in stock tools has no date. | stock llama.cpp cannot load \| Ollama, LM Studio: no \| Nari Labs fork required \| slower except 1 workstation GPU | Grid of four runtime tiles on a PCB background: 'stock llama.cpp', 'Ollama', 'LM Studio', 'Nari Labs fork'. On 'cannot load the file yet', grey X marks fade onto the first three tiles. On 'Nari Labs fork', the fourth tile lights up. On 'slower than stock quants', a small gauge fades in with its needle low; on 'one exception', a green tag reading '1 workstation GPU' pops at the gauge corner. | hyperframes | grid | 18.6 |
| s07 | foreshadow | Who should stay put? If you need the last fraction of a point, or long exact math, stay on BF16. If your card is a GeForce, the publisher says it plainly: GeForce cards have not been tested yet. | need the last fraction? stay on BF16 \| GeForce cards: not tested yet | Split-compare: left panel etched 'stay on BF16' with a full-height memory bar and an exact-math glyph; right panel 'NariQ file' with a compact bar. On 'GeForce cards have not been tested yet', a graphics-card outline rises-in-place below center and a grey tag reading 'not tested yet' fades over it. One accent moves at a time; the bars hold static. | hyperframes | split-compare | 13.1 |
| s08 | payoff_close | The card was never the problem, and three bits was never the real question. The old question was whether three bits is good enough. The only question left is what memory you have. | old question: is 3 bits enough? \| new question: what memory do you have? | Centered-stack payoff on a near-black die field. A card etched 'is 3 bits good enough?' fades down on 'The old question' as a second card, 'what memory do you have?', scales up to fill the frame on 'The only question left', backlit like a lit die with circuit traces brightening outward. The final frame holds static on the second card with no further motion. | hyperframes | centered-stack | 11.4 |

## Notes for review
- Numbers rounded for the ear from the brief's verbatim table (10.12 GB, 41.0 vs 39.8, 72% ceiling).
- The quality numbers are the publisher's own harness (4-day-old release); the objection scene carries it.
- GeForce untested; upstream llama.cpp merge is a hope; both live in the fine-print scene and Unverified.
- The 53.8 GB original appears on screen only where the packet said so.
- style_pack silicon chosen by style_rotation keyword fit; previous pack was halftone.

## Judge verdict (verbatim)
SCORES:
row 1 Hook: A=3 B=1 -- A lands "twenty-seven billion" plus the felt "would not fit" pain in the opening breath; B's "Your card isn't too small" has tension but no product or number in the first five words.
row 2 Payoff timing: A=3 B=2 -- A's promised concrete (27B didn't fit, numbers attached) lands by second 4; B's first hard number (fifty-three gigabytes) doesn't arrive until about second 7.
row 3 Specificity without cramming: A=2 B=2 -- A mostly spends one number per sentence but crams four-days/three-bit/27B/10.12 into the news beat; B is disciplined except the triple-stack "One file, one benchmark family, four days old." Neither drifts an Unverified claim into assertion.
row 4 Voice: A=3 B=3 -- Both clean second person with glosses folded into apposition and the dry "grading its own homework" beat landing unexplained.
row 5 Navigation: A=2 B=3 -- B's pivots each name the turn ("Here is the evidence against it," "Who should stay put?") and the order is locked; A's mechanism and score scenes could swap without breaking, and "The fine print:" is a bare signpost.
row 6 Difference: A=2 B=3 -- A reuses the news-react-so-what shape from three scripts back; B's contrarian-take, paradox opening rhythm, and question-swap landing are all absent from the recent run.
row 7 The repeat test: A=2 B=3 -- B's last thing heard is a standalone quotable line; A's last words ("It was whether your memory could hold it") are a fragment that only works attached to its setup.
row 8 Teaching: A=2 B=3 -- B shows why this quant holds (trellis errors cancel, calibrated on the model's own agent tokens), so a viewer can predict the next calibration-matched quant; A shows bits-as-size concretely but never explains why this 3-bit escaped the old failure mode.
TOTAL: A=19 B=20
WINNER: B
GRAFTS: Move A's opening sentence, "You downloaded a twenty-seven billion parameter model and it would not fit," to the top of B's first scene, before "Your card isn't too small." Allowed because the loser's hook scores 3 against the winner's 1 (at least 2 higher), it is a single sentence, it is the same second person, scene one's heard numbers go from two to three which sits at the cap, and the named-contradiction still lands inside scene one so B's contrarian spine and its "card was never the problem" callback stay intact.
LOSER_NEEDS: A reported the scores without the mechanism that explains them -- the trellis coding and agent-trace calibration -- so it could teach bits-as-size but never why this quant broke the 3-bit curse. It also needed a payoff that stands alone as one quotable sentence, on a shape and a wall-callback landing the recent run hadn't already spent.
REPEAT_LINE: The only question left is what memory you have.
