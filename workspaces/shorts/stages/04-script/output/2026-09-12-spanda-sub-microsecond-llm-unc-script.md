---
slug: 2026-09-12-spanda-sub-microsecond-llm-unc
format: classic
structure: number-first
style_pack: signal
value_types: TEACHES,REFRAMES
promise: after 38 seconds you can stamp every local-model reply with a guess-or-knows score, and you know the one case where that stamp lies
target_duration_s: 38
brief: 2026-09-12-spanda-sub-microsecond-llm-unc-brief.md
drafts: 2026-09-12-spanda-sub-microsecond-llm-unc-drafts.md
---

# Spanda: sub-microsecond LLM uncertainty explained

## Decisions
- Structures tried: number-first (draft A) vs worked-example (draft B); the last two ledger
  scripts were news-react-so-what and how-to-three-moves, so both cleared the rotation rule.
  Draft A won 21 to 19 on the judge rubric: same hook and voice quality, but A showed the
  Confident Mode Collapse limit concretely while B asserted it, and B's wrong-diagnosis hook
  text classifies as named-contradiction, the 2026-09-10 pattern (row 6 zero). No grafts.
- Hook: "Six hundred fifty-two nanoseconds. Spanda just ratted your local model out." Number
  shock, pattern number-shock, last seen in the ledger window only via this run. Picks of the
  10: number-shock for A, wrong-diagnosis for B, two different patterns per the divergence rule.
- Value lines: TEACHES on the sampling trick ("Agreement means trust; scatter means guessing"),
  REFRAMES on the catch ("a tuned giant repeats one wrong answer every time, Confident Mode
  Collapse. Agreement is evidence, not truth.").
- Gate repairs inside each draft (one round each): A named Spanda in the hook and defined
  epistemic uncertainty in s02; B added the 652 ns payoff inside s01, defined confabulation and
  exact-match clustering, and labeled the s04 on-screen number "Spanda kernel: 652.1 ns" so the
  matched-number gate reads it.

## Hook candidates
1. * "Six hundred fifty-two nanoseconds. Spanda just ratted your local model out." (number-shock; A's)
2. "Under a microsecond, your model confesses it's guessing."
3. "A millionth of a second to catch a guessing model."
4. * "Your Ollama isn't lying. Its memory of facts is." (wrong-diagnosis; B's)
5. "Ninety thousand times faster, and the GPU is optional."
6. "Spanda: a Rust gateway that stamps every guess your model makes."
7. "Zero GPU. One CPU core. Every reply stamped."
8. "Your local model has a tell. It's free to check."
9. "Semantic entropy caught hallucinations. It needed a second brain."
10. "Three answers, one question: that's the whole lie detector."

Scoring (one point each): payoff word in first five words; named product or number; length in
band; legible as frame-1 text in 8 words or fewer; no hype word; true per the brief; names the
viewer's situation. Candidate 1 scored 7 (situation via "your local model"), candidate 4 scored
6 (situation via "Your Ollama", no number), candidates 2/3/9 lost the product/number point or
the legibility point, 5/7 spent two numbers, 6 was Spanda-named but generic-promise, 8 and 10
were situation-true but carried no number or product. The two picks are different patterns, per
finding 12.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Six hundred fifty-two nanoseconds. Spanda just ratted your local model out. | 652 ns / no GPU | Frame 1: "652 ns" fills the safe area, "no GPU" beneath, fully legible. On "ratted itself out" a small stamp scales onto a chat reply card lower-center. Motion onset at t=0.30s: digits scale-settle into place, no edge travel. | hyperframes | giant-number | 3.4 |
| s02 | explain | You run Ollama on your PC; every answer sounds equally sure. That calm hides epistemic uncertainty, the model's own lack of knowledge. Ask the same question three times, like three friends asked separately. Agreement means trust; scatter means guessing. | 3 asks / agree = trust / scatter = guess (staged swaps) | On "Ask the same question three times" three reply cards rise in place side by side. On "Agreement means trust" the three cards snap to identical text with a check; on "scatter means guessing" the card texts diverge. | hyperframes | centered-stack | 12.2 |
| s03 | explain | Semantic entropy, the established detector, compares meanings with a second neural network. Its judge burns ninety-two thousand four hundred microseconds per query. Spanda, a small gateway, matches exact text, no GPU. | 92,400 µs · GPU judge / exact match · no GPU (split) | On "a second neural network" a heavy judge icon fades in beside a long bar labeled "92,400 µs". On "matches exact text, no GPU" the bar collapses to a thin sliver and a small CPU chip icon rises in place. | hyperframes | split-compare | 9.7 |
| s04 | explain | It sits beside Ollama at two point nine eight megabytes, stamping every reply. One pip install tonight; the stamp stays on. | pip install spnda / 2.98 MB · every reply stamped | On "sits beside Ollama" a gateway box fades in between an app icon and the model. On "stamping every reply" each passing reply card gets a header stamp. On "pip install tonight" the command appears in a terminal card. | hyperframes | diagram-flow | 6.6 |
| s05 | payoff_close | The catch: your model still writes all three answers first. And a tuned giant repeats one wrong answer every time, Confident Mode Collapse. Agreement is evidence, not truth. | same wrong answer ×3 / agreement = evidence, not truth | On "writes all three answers first" three generation cards replay in sequence. On "one wrong answer every time" the three cards collapse into identical wrong cards. On the payoff line "agreement = evidence, not truth" settles as the last frame, rhyming with the frame-1 stamp. | hyperframes | giant-number | 8.8 |

Sum of estimates: 40.7 s at 3.2 wps (the writer's prose sits at 132 words; the voice engine's
measured rate will decide the real clock, and render lint re-checks the band).

## Notes for review
Every latency and memory figure is the author's own unreplicated benchmark; the hook states
"six hundred fifty-two nanoseconds" flatly, so consider an "as published" caption on frame 1 if
the hedge should be visible, not just in the description. Confirm "a tuned giant" in s05 reads
as the 120B Confident Mode Collapse case (AUROC 0.091, TriviaQA) from the brief. The s02
definition of epistemic uncertainty is the one beat with no number; it is the budgeted generic
scene.
