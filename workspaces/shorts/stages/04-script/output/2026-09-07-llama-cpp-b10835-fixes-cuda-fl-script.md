---
slug: 2026-09-07-llama-cpp-b10835-fixes-cuda-fl
format: classic
structure: news-react-so-what
style_pack: signal
value_types: TEACHES,EQUIPS
promise: After thirty-five seconds you know which bug llama.cpp b10835 fixed, why it mattered even when output looked fine, and the one move that gets you the fix tonight.
target_duration_s: 35
brief: 2026-09-07-llama-cpp-b10835-fixes-cuda-fl-brief.md
drafts: 2026-09-07-llama-cpp-b10835-fixes-cuda-fl-drafts.md
---

# llama.cpp b10835 fixes its fast lane

## Decisions
- Structures tried: news-react-so-what (draft A) vs myth-bust (draft B). A won 21-18 on the judge rubric; no grafts (B's hook only one point lower; B's best lines would have forced a rewrite of A's hook or overrun the payoff).
- Hook: candidate 1 (named-contradiction, "llama.cpp just fixed its fast lane"), merged with candidate 3's number under gate pressure: the concrete-hook gate needed a digit-carrying number in sentence one, so the final opening line is "llama.cpp fixed three thousand two hundred thirty-two errors to zero."
- Gates on the winner: validator 0 blockers 0 advisories; eval gate1_ready true (number_spend 2, hook_concrete via number, scene_specificity 4/5, sameness clean); normalize scenes_changed 0.
- Value lines: TEACHES lands in scenes s02-s03 (what flash attention is, what the skipped barrier risked); EQUIPS lands in s05 ("So tonight, pull the newest llama.cpp build and keep flash attention on").
- Judge's row-3 cap on B recorded in the drafts note: "No garbled text, nothing you'd see" spoke the brief's absence-of-evidence as an assertion (finding 17).

## Hook candidates
1. llama.cpp just fixed its fast lane. * (picked; merged with 3 under the concrete-hook gate)
2. Your model file is fine. llama.cpp wasn't.
3. 3232 errors to zero, in one update.
4. Three llama.cpp releases in seventy-seven minutes.
5. llama.cpp's fast lane was breaking GPU rules.
6. You updated the model. The engine was the bug.
7. Flash attention has been skipping checkpoints since February.
8. Your GPU's fast path was reading unfinished work.
9. b10835 fixes a bug older than your last download.
10. Same speed tonight, minus three thousand errors.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|--------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | llama.cpp fixed three thousand two hundred thirty-two errors to zero. | llama.cpp fixed its fast lane \| 3232 to 0 | Frame 1: the hook text sits fully legible over a dark lane graphic. On "three thousand two hundred thirty-two" a counter scales in beneath it showing 3232; on "zero" it flips to 0 in place. | hyperframes | centered-stack | 3.4 |
| s02 | explain | Your card's fast mode is flash attention, a fused math path that skips a giant intermediate write. It's been broken since February. | fast mode, broken since Feb | On "flash attention" a fused-path icon rises in place at left; on "broken since February" a right panel fades in with a hairline crack through the icon. | hyperframes | split-compare | 7.6 |
| s03 | explain | The program doing that math skipped a barrier, a checkpoint where one chunk of your card waits for another. Chunks could read unfinished work, risking wrong answers. | one chunk raced ahead | On "a checkpoint where one chunk of your card waits for another" two glowing blocks rise in place with a dotted gate between them; on "unfinished work" the gate fades out and the right block flickers. | hyperframes | diagram-flow | 10.3 |
| s04 | explain | The catch is the price. Prompt speed moved point one five percent, inside measurement noise. Your card was speeding. Now it speeds legally. | -0.15% prompt speed | On "point one five percent" a giant -0.15% scales in center; on "speeds legally" a small speedometer fades in beneath it, needle steady. | hyperframes | giant-number | 8.6 |
| s05 | payoff_close | So tonight, pull the newest llama.cpp build and keep flash attention on. Same speed, no broken rules. | fast lane, fixed tonight | On "pull the newest llama.cpp build" the text rises in place; on "no broken rules" the frame settles into the same centered lane stack as frame one. | hyperframes | centered-stack | 5.9 |

## Notes for review
- Numbers rounded: the PR's 1390.27 to 1388.10 t/s is spoken as "point one five percent, inside measurement noise," matching its own "No measurable performance regression."
- The bug is hedged as "risking wrong answers": the brief's evidence is sanitizer errors (3232 to 0) plus crash-adjacent reports, not observed garbled output.
- The fast-lane picture is the hook's framing only, not a sustained analogy; "speeds legally" is the single wry beat.
