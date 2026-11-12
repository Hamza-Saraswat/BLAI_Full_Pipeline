---
slug: 2026-11-12-deepseek-coder-v2-lite-on-a-6g
stage: 04-script
decision: draft B (myth-bust) wins 23/24 over draft A (worked-example) 19/24
generated_at: 2026-11-12
---

# Drafts: 2026-11-12-deepseek-coder-v2-lite-on-a-6g

Two blind writers on kimi-k3, two structures, two hook patterns. Judge: kimi-k3 with the
rubric and the last five ledger entries. Both drafts passed validator (0 blockers, 0
advisories) and eval gates before judging.

## Score table

| Row | Draft A (worked-example) | Draft B (myth-bust) |
|---|---|---|
| 1 Hook | 3 | 3 |
| 2 Payoff timing | 2 | 3 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 2 | 3 |
| 5 Navigation | 3 | 3 |
| 6 Difference | 2 | 2 |
| 7 Repeat test | 2 | 3 |
| 8 Teaching | 2 | 3 |
| TOTAL | 19/24 | 23/24 |

## Winner: Draft B

Rows 7 and 8 decide it. B's payoff line ("Your card wasn't too small; the file was too big")
is the repeatable sentence and it is the last thing spoken, while A ends on an instruction a
viewer would not say aloud. B also teaches the mechanism (sixteen billion stored, two point
four billion awake, memory pays for all), so a viewer can predict why pruning sleepy experts
is cheap. Row 2: B's break lands with the four point eight three gigabyte file by about
second four; A's promise stays unpaid until the rebuild beat near second eighteen.

## Grafts

None. A's hook does not beat B's by two points (3 vs 3). A's "Layers spill to your CPU" beat
would add a beat, a number and a transition rewrite to B's closed structure, so it stays out.

## Losing shape

The worked-example needed to pay its hook earlier: the rebuild answer arrives around second
eighteen, while B proves its claim inside five seconds. It also needed a payoff line built to
be repeated and the mechanism for why dropping experts is safe, instead of the undefined
"experts that rarely wake".

## Draft A (worked-example, hook pattern: situation)

Hook: "Your old card can still code with DeepSeek."

| Scene | Role | Narration | On-screen | Layout | Est s |
|---|---|---|---|---|---|
| s1 | hook | Your old card can still code with DeepSeek. | DeepSeek wants your old card | centered-stack | 2.8 |
| s2 | explain | DeepSeek Coder V two Lite packs sixteen billion parameters. The usual download is ten point three six gigabytes of weights. Your card holds six gigabytes of memory. It does not fit. | 10.36 GB download | 6 GB card | split-compare | 10.4 |
| s3 | explain | Layers spill to your CPU. That's four point five to ten tokens a second. | 4.5-10 tok/s offload | diagram-flow | 4.9 |
| s4 | explain | A rebuild shrinks every weight and drops the experts that rarely wake. It lands at four point eight three gigabytes of model, all on your card. | 4.83 GB, all in VRAM | giant-number | 9.0 |
| s5 | explain | Grab the file, then hand Ollama a one-line Modelfile. | FROM ./deepseek.gguf | ollama create | timeline | 3.2 |
| s6 | payoff_close | One author's laptop hit sixty-five to seventy-six tokens a second. Wire Continue to autocomplete, and your card writes the next line. | 65.6-76.3 tok/s | one author's run | centered-stack | 7.3 |

Value lines: TEACHES "A rebuild shrinks every weight and drops the experts that rarely wake."
PROVES "One author's laptop hit sixty-five to seventy-six tokens a second."
Words: 109, target 38s.

## Draft B (myth-bust, hook pattern: named-contradiction) -- WINNER

Hook: "Your old GPU isn't too small for DeepSeek."

| Scene | Role | Narration | On-screen | Layout | Est s |
|---|---|---|---|---|---|
| s1 | hook | Your old GPU isn't too small for DeepSeek. The rebuilt file: four point eight three gigabytes of weights. | Your GPU isn't too small | then: 4.83 GB | giant-number | 6.3 |
| s2 | explain | One author ran every layer on a six-gigabyte laptop card. The speed: sixty-five to seventy-six tokens a second. The belief it breaks: big models need big cards. | 6 GB, all on the card | 65.6-76.3 tok/s | one author's run | split-compare | 9.4 |
| s3 | explain | DeepSeek Coder V two Lite does store sixteen billion parameters. Two point four billion wake per word. Mixture of experts: many specialists, few called per word. Memory pays them all. | 16B stored | 2.4B awake per word | diagram-flow | 10.1 |
| s4 | explain | The rebuild rounds weights down and cuts the ten least-called experts. | MAPLE rebuild: 4.50 GB | -10 experts per layer | grid | 3.8 |
| s5 | payoff_close | The myth survives: nobody re-measured the pruned file's accuracy, and that speed is one self-reported run. Your card wasn't too small; the file was too big. | your 6 GB card | the 4.83 GB file | centered-stack | 9.0 |

Value lines: TEACHES "Mixture of experts: many specialists, few called per word. Memory pays them all."
PROVES "One author ran every layer on a six-gigabyte laptop card. The speed: sixty-five to seventy-six tokens a second."
Words: 112, target 39s.
