---
slug: 2026-09-26-ollaya-runs-decision-models-th
stage: 04-script
---

# Drafts: 2026-09-26-ollaya-runs-decision-models-th

Two blind writers (Kimi K3, separate processes, private scratch dirs), the judge a third. Drafts reproduced from their storyboards; the judge's verdict follows verbatim.

### Draft A (winner, after graft) (contrarian-take, hook: 421M. Just a classifier?)

| Scene | Narration | On-screen | Layout | Est s |
|-------|-----------|-----------|--------|-------|
| s01 hook | Everyone says Ollaya is just a classifier. The model you'd pull packs four hundred twenty-one million parameters. | 421M. Just a classifier? | centered-stack | 5.9 |
| s02 foreshadow | The math part is true. Their chart says ten milliseconds for five typed questions. | 10 ms, five questions | giant-number | 4.8 |
| s03 explain | What's new is the shape: typed answers with probabilities attached, one open binary, fully offline. Answers cost one forward pass, a single run through the network. | typed answers, one pass | diagram-flow | 9.0 |
| s04 explain | Ollaya's demo flags a force-push at point nine zero. That verdict took one hundred seventy-eight milliseconds on their card. | destructive: 0.90 | timeline | 6.6 |
| s05 explain | The catch: base laya sits near chance on typed decisions. The tuned checkpoint reaches point seven six six on its model card. Calibrate before you trust it. | tuned checkpoint: 0.766 | split-compare | 9.3 |
| s06 payoff_close | Old math, new shape, your call. Pull laya with one command and time it on your own GPU. | $ time ollaya run laya | centered-stack | 6.2 |

### Draft B (number-first, hook: 10 ms. Your GPU.)

| Scene | Narration | On-screen | Layout | Est s |
|-------|-----------|-----------|--------|-------|
| s01 hook | Ten milliseconds, on your own GPU. That's Ollaya's benchmark for five typed questions on their forty-ninety card. | 10 ms. Your GPU. | giant-number | 5.9 |
| s02 explain | Laya is a decision model: it never writes text, it returns probabilities. The whole thing is four hundred twenty-one million parameters. | no words out, only probabilities | diagram-flow | 7.2 |
| s03 explain | Answers cost one forward pass, a single run through the network. Ollaya serves that Ollama-style: one binary, Apache licensed, fully offline. | 421M params. One forward pass. | giant-number | 7.2 |
| s04 foreshadow | On laya's model card, base accuracy on typed decisions is zero point three six two, near chance. Fine-tuning reaches zero point seven six six. | base 0.362 vs tuned 0.766 | split-compare | 8.3 |
| s05 payoff_close | Run ollaya run laya tonight. Your app's cheap questions stop paying the LLM token meter. | $ ollaya run laya | centered-stack | 5.2 |


## Judge verdict (verbatim)

```
===SCORES===
1 | 3 | 3 | A: "just a classifier" tension + 421M; B: 10ms + own-GPU tension.
2 | 2 | 3 | A pays at break (~s3); B pays inside the hook itself.
3 | 3 | 3 | Both attribute vendor numbers correctly; every beat earns its figure.
4 | 3 | 2 | A: "The math part is true" wry concession lands; B reads slightly manual.
5 | 3 | 2 | A's concession→novelty→catch→verdict unreorderable; B's middle scenes could swap.
6 | 3 | 1 | B repeats 09-22's number-first/number-shock and "tonight" close; A is a fresh shape.
7 | 2 | 3 | B's payoff line is last and repeatable; A's repeatable line precedes the close.
8 | 2 | 3 | B's forward-pass mechanism lets viewers predict other cases; A only names shape.
===TOTALS===
A: 21/24 | B: 20/24
===WINNER===
A | Contrarian shape wins on difference, navigation, and voice despite B's faster payoff.
===GRAFTS===
B's "Answers cost one forward pass, a single run through the network" moves into A s03 after "probabilities attached" — gives A the mechanism it lacks, adds no new number, fits the same breath.
===LOSER_ADVICE===
Number-first needed a hook and close not recycled from the 09-22 number-shock and the recent "tonight" closings. It also needed one wry beat and transitions that lock the middle scenes in place.
```

## Outcome
- Winner: draft A (contrarian-take), 21-24 vs 20-24, on difference (row 6), navigation (row 5) and voice (row 4); B took payoff timing, repeat test and teaching.
- Graft applied: B's forward-pass sentence into A s03; A s03 then split into s03 (shape) + s04 (demo verdict, timeline layout) to respect the 12-second scene advisory and the one-number-per-scene rhythm.
- Both drafts passed validator (0 blockers) and all eval gates before judging; A had failed hook_concrete + scene_specificity at first eval and was repaired inside its own draft before the judge ran.
