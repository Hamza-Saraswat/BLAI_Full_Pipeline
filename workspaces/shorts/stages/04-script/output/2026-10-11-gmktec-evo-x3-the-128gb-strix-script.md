---
slug: 2026-10-11-gmktec-evo-x3-the-128gb-strix
format: classic
structure: contrarian-take
style_pack: signal
value_types: TEACHES,PROVES
promise: After 35 seconds you can say what the DGX Spark's premium actually buys (prompt processing, not chat speed) and check your own workload against it.
target_duration_s: 35
brief: 2026-10-11-gmktec-evo-x3-the-128gb-strix-brief.md
drafts: 2026-10-11-gmktec-evo-x3-the-128gb-strix-drafts.md
---

# DGX Spark vs Strix Halo: Speed Myth?

## Decisions
- Two structures tried: comparison-ladder (draft A) and contrarian-take (draft B); the judge (kimi-k3) picked B, 21 to 18, no grafts.
- Hook: wrong-diagnosis pick ("You think $6,950 buys speed. It buys prompt processing."), scored highest of the 10; draft A carried the decision hook ("EVO-X3 or DGX Spark? One number decides.") to force divergence.
- Judge row 6 (difference) scored B low for family resemblance to the ledger (a contrarian-take on 10-07, a number-shock close on 10-10). The sameness gate passed clean on every hard rule: structure, hook pattern, closing move, duration and opener bigrams all differ from the last five. Proceeded because the gate is the rule and the resemblance is family, not wording.
- Lexicon: added say entries for EVO-X3, EVO-X2, EVO, GMKtec (normalizer self-test 159/159 after the edit).

## Hook candidates
1. EVO-X3 or DGX Spark? One number decides.
2. You think $6,950 buys speed. It buys prompt processing. *
3. Thirty-one hundred dollars apart. Same chat speed.
4. 128GB for $3,799. The Spark costs $6,950.
5. Same highway. Same speed. Different loading dock.
6. Forty-five percent cheaper. Same chat speed.
7. The $6,950 box is faster. Barely, where it counts.
8. One model fits both. One wallet disagrees.
9. The mini-PC that runs 120B like the Spark.
10. Same tokens per second. Very different receipts.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | You think six thousand nine hundred fifty buys speed. It buys prompt processing. | You think $6,950 buys speed. | It buys prompt processing. | Frame 1: charcoal background, giant white '$6,950' centered, the line 'You think $6,950 bu | hyperframes | centered-stack | 4.5 |
| s02 | explain | You want one home box for giant open models. The spec sheet crowns the Spark. | One box, biggest open models | Spec sheet crowns the Spark | On 'You want one home box' a left card fades in showing a small desk with one mini-PC silh | hyperframes | split-compare | 5.2 |
| s03 | explain | An owner benched both on one model. The Spark wrote fifty-six word-pieces a second, the mini-PC forty-seven. | Same model, both boxes | DGX SPARK 56 tokens/sec | STRIX HALO 47 tokens/sec | On 'An owner benched both on one model' a small tag reading 'Same model, both boxes' fades | hyperframes | giant-number | 5.9 |
| s04 | explain | Writing rides on bandwidth, how fast weights stream. Two hundred fifty-six versus two hundred seventy-three gigabytes per second. Same doorway. | CHEF = compute | DOORWAY = memory bandwidth | On 'memory bandwidth' a doorway outline fades in right of center, labeled 'DOORWAY = memor | manim | diagram-flow | 6.9 |
| s05 | explain | Prefill, the pass reading your whole prompt, is one big math block, no doorway. There the Spark runs roughly two to five times faster. | PREFILL reads the whole prompt | Spark 2-5x faster | On 'the pass reading your whole prompt' a document icon fades in above two empty horizonta | manim | split-compare | 8.3 |
| s06 | foreshadow | Giant prompts and agent loops earn the Spark. Everyday chat does not. | Earns it: long prompts, agents, CUDA | One owner's run, not a lab | On 'Giant prompts and agent loops' two checklist rows rise in place, 'LONG PROMPTS' and 'A | hyperframes | centered-stack | 4.1 |
| s07 | payoff_close | Same chat speed, much faster prompt processing. That is the Spark's premium, three thousand one hundred dollars. | Same chat, faster prompts | $3,100 premium | BUILD LOCAL AI | On 'Same chat speed, much faster prompt processing' two short lines settle center screen.  | hyperframes | giant-number | 5.9 |

## Notes for review
The 47/56 tokens-per-second pair is one forum owner's llama-bench run on an EVO-X2 (same Strix Halo SoC), spoken in the script as "an owner benched both"; the brief carries it as community-tier, medium confidence. The 2-5x prefill range is rounded from the same run. Prices are sale-price ($3,799.99) as fetched 2026-10-11. The doorway analogy's limit (prefill has no doorway) is stated in scene s05's clause.
