---
slug: 2026-09-23-best-coding-models-on-dgx-spar
stage: 04-script
generated_at: 2026-09-23
winner: A (comparison-ladder)
---

# Drafts: The Two-Model Spark: Fast Coder vs Smart Coder

Judge: kimi-k3 blind call, rubric verbatim as system file, both storyboards as user file; packet slimmed to narration plus 90-char visual-brief heads after two failed calls (a network read-timeout and a max-tokens overrun with no verdict).

## Draft A (winner, comparison-ladder)

**s1 (hook, 10.0s)** You run coding agents against a chat API every day. You have been eyeing a DGX Spark to bring that work home. Two open coders now fit that box, and they pull in opposite directions.

**s2 (foreshadow, 9.7s)** Here's the axis: what your agent's day actually feels like. Every follow-up resends a twenty-three-thousand-token prompt, tokens being the word-pieces models read. So the whole day taxes both speed and smarts.

**s3 (explain, 14.7s)** On speed, Qwen's Coder Next writes at eighty-five tokens a second on this one box. It's a mixture-of-experts coder, a big staff where each token asks only a few specialists. That's autocomplete speed for your agent's tight loops.

**s4 (explain, 6.6s)** But your day also has hard code. On the coding benchmark both model cards report, Coder Next scores forty-four point three.

**s5 (explain, 9.1s)** Qwen's twenty-seven billion thinker scores sixty-one point seven on that same benchmark. It thinks through the tickets that make the fast one guess. Same tests, harder tickets closed.

**s6 (explain, 10.3s)** What fits settles the rest. GLM's Flash runs only as a heavily shrunk copy that eats most of the box. DeepSeek's Flash is twice the box even shrunk, so it stays a science project.

**s7 (explain, 11.6s)** The honest catch is the platform. Street prices climbed past NVIDIA's own list. The certified driver you want is still an unanswered forum thread. The newer Ubuntu path is a hand-rolled recipe, not a vendor upgrade.

**s8 (explain, 12.2s)** Back on the box, configuration decides your day. Give the thinker a prefix cache, the engine's memory of what it already read. Without it, follow-ups took twenty-two seconds. With it, point-three. Same box, same model, nothing changed but configuration.

**s9 (payoff_close, 4.4s)** Send the loops to Coder Next, and send the hard code to the thinker.

## Draft B (myth-bust)

**s1 (hook, 7.8s)** You want the biggest coder that fits. You run coding agents against a chat API every day, and the Spark is your way home.

**s2 (explain, 7.2s)** The fastest coder here is Qwen's Coder Next: eighty-five tokens a second. Tokens are word pieces of code. Speed is not the score.

**s3 (explain, 4.4s)** On the coding benchmark both model cards report, Coder Next scores forty-four point three.

**s4 (explain, 5.6s)** Qwen's twenty-seven billion thinker, a model a third its size, scores sixty-one point seven on the same benchmark.

**s5 (explain, 11.9s)** Coder Next is a mixture-of-experts, a design that stores many specialists but activates only a few per token. That is why it flies, and why hard code beats it. The fix is not one model; it is two.

**s6 (explain, 13.1s)** Your agent resends a twenty-three-thousand-token repository prompt on every follow-up. A prefix cache, the engine's memory of what it already read, should make that cheap. It pays only if the memory is kept.

**s7 (explain, 6.6s)** Misconfigured, the thinker's follow-up took twenty-two seconds. With the cache kept warm, point-three. Same box, same model, nothing changed but configuration.

**s8 (explain, 15.6s)** The myth survives here: hard code wants the strongest model that fits, and that is the thinker. GLM's Flash runs only as a squeezed quant, weights cut to fewer bits, eating three quarters of the box. DeepSeek's Flash needs twice the box.

**s9 (explain, 14.7s)** The honest catch: street prices have climbed past NVIDIA's own list. The certified driver request sits unanswered since spring, and the newer Ubuntu path is a hand-rolled forum recipe. Every speed figure comes from one reviewer on nightly builds he says expire in days.

**s10 (payoff_close, 8.4s)** So run two: Qwen's Coder Next for the tight loop, the twenty-seven billion thinker for the hard files. The box stopped being the bottleneck; your configuration is.

## Score table (judge, verbatim)

| Row | A (comparison-ladder) | B (myth-bust) |
|---|---|---|
| 1 Hook | 2 — names the Spark and a two-coder tension, but not in the first five words | 1 — "biggest coder that fits" names the topic only |
| 2 Payoff | 1 — first concrete (23k prompt) lands ~10s, first coder named ~20s | 1 — break lands ~14s ("Speed is not the score"), after 8 even from the break |
| 3 Specificity | 3 — each beat earns one specific; the two GLM/DeepSeek fit beats carry facts, not numbers | 2 — s8 and s9 cram (quant + three-quarters + twice-the-box; price + driver + Ubuntu + provenance in one beat) |
| 4 Voice | 3 — clean second person, "it stays a science project" is wry and unexplained | 2 — clean and correct, no wry beat that lands |
| 5 Navigation | 3 — "But your day also has hard code" / "What fits settles the rest" / "Back on the box"; ladder order is load-bearing | 2 — transitions carry content, but s8's "The myth survives here" reopens rather than advances |
| 6 Difference | 3 — new shape, choice-framed hook, routing-rule landing; none match the last two | 2 — myth-bust already ran three entries ago; opening rhythm echoes it |
| 7 Repeat test | 3 — the routing rule is the last thing heard and is quotable | 3 — "your configuration is" is repeatable and last |
| 8 Teaching | 3 — the speed/smarts axis plus routing rule lets you place a model the script never mentions | 2 — MoE tradeoff is asserted ("why hard code beats it") but never shown |

TOTAL A: 21 — TOTAL B: 15

WINNER: A

Grafts:
- From B s7 into A s8, after "With it, point-three.": "Same box, same model, nothing changed but configuration." Reason: B names the controlled experiment A only implies; adds no numbers, fits person and structure.
- Hook graft not permitted (B wins row 1 by zero).

What the losing shape needed: the break had to arrive by second five with the counter-claim attached (name the thinker and its score at the moment the myth cracks), and s8 needed to spend its beats showing why the fast design loses on hard code instead of restating the myth it already broke.

## Outcome
Winner: A, grafted as named above. Loser B's shape notes recorded by the judge: the break had to land by second five with the counter-claim attached, and its fit beat needed to show why the fast design loses on hard code instead of restating the myth.
