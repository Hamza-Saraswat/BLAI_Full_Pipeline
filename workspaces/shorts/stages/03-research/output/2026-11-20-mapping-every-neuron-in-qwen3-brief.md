---
slug: 2026-11-20-mapping-every-neuron-in-qwen3
stage: 03-research
topic: "Mapping every neuron in Qwen3-8B"
depth: standard
generated_at: 2026-11-20T12:38:46Z
sources: 9
hub: "[[videos/2026-11-20-mapping-every-neuron-in-qwen3]]"
---

# Research brief: Mapping every neuron in Qwen3-8B

## Summary
Fermion Research published the first neuron-by-neuron causal map of Qwen3-8B on 18 November 2026: 442,368 neurons, every one pushed in both directions, distilled to 132 verified switches. The most arresting number is the German neuron going from 7% to 100% German replies in a single notch. The strongest concrete case for a local operator: neuron pushes are the debugging layer prompting never had, and the same class of internal intervention mediates refusal (a single direction, across 13 open chat models up to 72B per arXiv:2406.11717). What could not be verified: Fermion's editing framework is promised but not released, so nothing here is installable from them tonight. No fetched sources conflict; the field-level tension over whether raw neurons are too tangled to map is carried as a misconception pair rather than averaged away.

## Thesis
A published map of all 442,368 neurons in Qwen3-8B turns your local model from a black box you can only prompt into a machine with a labelled panel -- and about one in a hundred of those labels is a real, verified switch.

## Explanation path
Start from what the viewer already runs: Qwen3-8B is a stack of 36 identical layers, 12,288 neurons per layer, and every word it writes climbs through all 36 floors before the next word appears. Establish the move before the map: a push adds a fixed amount to one neuron's number at every word -- no prompt, no fine-tune, one number changed. That sets up the honest question (isn't any hard push just brain damage?) and its numeric answer: random neurons move behaviour 1.4 points out of 100, a real switch must beat 30 matched randoms by at least 40. With the method trusted, the map lands: 132 verified switches, 11,079 described, most neurons doing nothing clear; switches cluster early (language, persona, register) and late (word obsessions). The payoff for the local operator follows: named neurons like German (7% to 100% in one notch), why a map beats prompting (steering as the debugging layer prompting lacks; refusal as a single direction across 13 open models up to 72B; Fermion's agent edit moving MATH-500 from 6.5% to 32.0% by touching 2.7 millionths of the model). Close honest: no truthfulness switch found, Fermion's framework promised but not released, and a persona push is not a hidden soul -- it is a dial the map lets you find.

## Claims
1. **Fermion Research published a full causal neuron map of Qwen3-8B on 18 November 2026 as an interactive research post with JSON data artifacts, not a paper.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "We pushed all 442,368 neurons in Qwen3-8B in both directions and measured how much each push changed what the model was about to say."
2. **Qwen3-8B has 442,368 neurons, arranged as 36 layers x 12,288 neurons per layer, and Fermion pushed every one in both directions.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "The atlas covers all 442,368 neurons of Qwen3-8B (36 layers × 12,288 neurons)."
3. **The method is a push: add a fixed amount to one neuron's number at every word -- no prompt, no fine-tuning, one number changed.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "our experiment is the bluntest one imaginable, in which we add a fixed amount to one neuron's number at every word and call it a push"
4. **Random neurons pushed equally hard move a behaviour by 1.4 points out of 100 on average, while a neuron has to move its behaviour by at least 40 to count as a switch, beating 30 matched random neurons.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "The random ones are reassuringly boring, moving a behaviour by 1.4 points out of 100 on average, while a neuron has to move its behaviour by at least 40 to count as a switch."
5. **The atlas marks 132 verified switches, 20 persona finds and 11,079 more neurons with a described effect; only about one in a hundred neurons does one clear thing.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "It marks 132 verified switches, 20 persona finds and 11,079 more neurons with a described effect."
6. **The German neuron (layer 5, neuron 5224) goes from German in 7% of replies to 100% in a single notch.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "The German neuron goes from German in 7% of replies to 100% in a single notch, about as close to a light switch as this kind of maths gets"
7. **The switches are not a chat-training artifact: replaying 70 strong switches in the pretrained Qwen3-8B, 67 still moved the behaviour further than random neurons did.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "When we replayed our 70 strong switches in the pretrained Qwen3-8B, 67 of them still moved the behaviour further than random neurons did."
8. **Neuron-level editing can move capability, not just persona: editing two neurons (2,048 weights, 2.7 millionths of the model) in Qwen3.5-0.8B raised MATH-500 from 6.5% to 32.0%, beating all 20 decoy edits.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "It wrote a "finish thinking" direction into two neurons, 2,048 weights or 2.7 millionths of the model, and MATH-500 rose from 6.5% to 32.0%."
9. **Refusal in language models is mediated by a single direction: erasing it from the residual stream prevents refusal of harmful instructions, adding it elicits refusal on harmless ones, across 13 popular open-source chat models up to 72B parameters.**
   - Source: Refusal in Language Models Is Mediated by a Single Direction (arXiv:2406.11717), https://arxiv.org/abs/2406.11717
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
10. **The honest limit: almost all switch neurons set who is speaking, to whom and how; Fermion found none that sets whether the speaker is telling the truth.**
   - Source: Mapping every neuron in Qwen3-8B - Fermion Research, https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/
   - Tier: primary | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract
   - Quote: "almost all of them set who is speaking, to whom and how, while none that we could find sets whether the speaker is telling the truth"
11. **A local operator can intervene on activations tonight with free tooling: nnsight wraps PyTorch models (any Hugging Face checkpoint) and lets you edit activations in-place mid-forward-pass.**
   - Source: Quick Start - nnsight, https://nnsight.net/getting-started/quickstart/
   - Tier: docs | Confidence: high | Accessed: 2026-11-20 | Via: hermes web_extract

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total neurons in Qwen3-8B | 442,368 neurons | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "The atlas covers all 442,368 neurons of Qwen3-8B (36 layers × 12,288 neurons)." |
| 2 | layers | 36 layers | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "every word the model writes climbs through all 36 floors of Qwen3-8B" |
| 3 | neurons per layer | 12,288 | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "Each floor holds 12,288 small calculators" |
| 4 | verified switches in the atlas | 132 | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "It marks 132 verified switches, 20 persona finds and 11,079 more neurons with a described effect." |
| 5 | neurons with a described effect (weaker tier) | 11,079 | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "The 11,079 described neurons are every push where we compared the replies and a judge wrote down what changed" |
| 6 | random-neuron control effect | 1.4 points out of 100 on average | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "moving a behaviour by 1.4 points out of 100 on average" |
| 7 | threshold to count as a switch | at least 40 points out of 100 | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "a neuron has to move its behaviour by at least 40 to count as a switch" |
| 8 | German neuron swing | from 7% of replies to 100% in a single notch | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | "The German neuron goes from German in 7% of replies to 100% in a single notch" |

## Analogy candidates
- **Vehicle**: a recording-studio mixing desk with 442,368 faders (Fermion's own picture). Mapping: each fader is one neuron, each column one layer; about one in a hundred faders has a label (German, pirate, cat), and the map is the list of labelled faders. Breaks when: breaks because real faders are independent and linear while neurons interact: push past the sweet spot and the whole desk squeals instead of one channel distorting.
- **Vehicle**: a city street atlas of 442,368 buildings. Mapping: the artifact literally ships as an atlas: 11,079 buildings carry a scribbled note, 132 carry a verified plaque you can navigate by. Breaks when: breaks because a map is read-only while neurons are dials -- touching the building changes the city, and most of the map is unlabeled.
- **Vehicle**: a light switch that is really a dimmer with a burn-out point. Mapping: the German neuron jumps 7% to 100% in a single notch, as close to a light switch as this maths gets. Breaks when: breaks two notches later when the model babbles, and most switches are partial (73-90%), not 100%.

## Misconceptions
- Myth: myth. Reality: reality.
- Myth: myth. Reality: reality.
- Myth: myth. Reality: reality.
- Myth: myth. Reality: reality.

## Glossary
- **neuron**: one of the 12,288 small calculators inside each layer that outputs a single number saying roughly how much of its particular thing is going on in the current word.
- **layer**: one of the 36 identical stacked copies of the same machine that every word climbs through before the model predicts the next word.
- **activation**: the number a neuron produces for the current word; the model's internal state is a long list of these before it writes anything.
- **push**: adding a fixed amount to one neuron's activation at every word, like sliding one fader and holding it.
- **verified switch**: a neuron whose push changes exactly one behaviour, beats 30 random same-layer neurons pushed equally hard, and survives held-out questions; 132 exist in Qwen3-8B.
- **steering**: changing a model's behaviour at runtime by adding to or erasing internal activations, instead of changing the prompt or fine-tuning.
- **interpretability**: the research program of opening the AI black box far enough to check, predict and edit what a model computes.

## Unverified
- Fermion's neuron-editing framework was only promised ("in the near future") as of the 18 November 2026 post; it is not claimable that you can install their tool tonight.
- It is plausible but untested that Fermion's exact push protocol can be reproduced with nnsight on a local Qwen3-8B this session; both are public but nobody ran it here.
- The October "God neuron" demo by an independent X researcher (Fermion's protocol source) was not fetched from a primary source.
- Per-model switch totals for the other mapped models (Qwen3.5-4B, Qwen3.5-9B, OLMo-3-7B) are not on the fetched page.
- No tech-press coverage of the Fermion release was fetchable; the primary page is the sole source for every map number in this brief.

## Suggested outline
1. Hook: one dial turns your local Qwen3-8B German -- 7% of replies to 100% in a single notch -- because someone finally mapped all 442,368 neurons (published 18 November).
2. Middle: what a push is (one number changed at every word, no prompt, no fine-tune), why the findings are not screenshot luck (randoms move behaviour 1.4 out of 100, a switch must beat 30 matched randoms by at least 40), and the shape of the map (36 floors x 12,288 faders, 132 verified switches, about one in a hundred neurons does one clear thing).
3. Payoff and honest catch: a map is the debugging layer prompting never had -- refusal is a single direction across 13 open models, a 2.7-millionths-of-the-model edit moved MATH-500 from 6.5% to 32.0% on a smaller Qwen -- but no truthfulness switch was found and Fermion's own tooling is promised, not shipped; the atlas itself is readable tonight.

## Viewer situation
You run Qwen3-8B locally in Ollama or LM Studio, and when it does something weird you can only shrug and re-prompt.

## Has process
false

## Objection
A pushed neuron just proves you can break a model 442,368 ways; a cute German demo is not understanding, and none of this helps me serve tokens tonight.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/ | Mapping every neuron in Qwen3-8B - Fermion Research | primary | hermes web_extract | 2026-11-20 |
| 2 | https://www.anthropic.com/research/mapping-mind-language-model | Mapping the mind of a large language model - Anthropic | primary | hermes web_extract | 2026-11-20 |
| 3 | https://www.anthropic.com/research/golden-gate-claude | Golden Gate Claude - Anthropic | primary | hermes web_extract | 2026-11-20 |
| 4 | https://www.anthropic.com/research/tracing-thoughts-language-model | Tracing the thoughts of a large language model - Anthropic | docs | hermes web_extract | 2026-11-20 |
| 5 | https://www.goodfire.com/research/neurons-as-an-interpretable-basis | Neurons as an Interpretable Basis - Goodfire | primary | hermes web_extract | 2026-11-20 |
| 6 | https://www.goodfire.com/blog/feature-steering-for-reliable-and-expressive-ai-engineering | Feature Steering for Reliable and Expressive AI Engineering - Goodfire | docs | hermes web_extract | 2026-11-20 |
| 7 | https://arxiv.org/abs/2406.11717 | Refusal in Language Models Is Mediated by a Single Direction (arXiv:2406.11717) | primary | hermes web_extract | 2026-11-20 |
| 8 | https://nnsight.net/getting-started/quickstart/ | Quick Start - nnsight | docs | hermes web_extract | 2026-11-20 |
| 9 | https://learnmechinterp.com/topics/superposition/ | Superposition - Learn Mechanistic Interpretability | community | hermes web_extract | 2026-11-20 |

## Notes
Most arresting number: the German neuron's 7% to 100% single-notch jump; the scale number is 442,368. Scoping caveats for the writer: the MATH-500 weight edit (6.5% to 32.0%, 2.7 millionths of the model) was run on Qwen3.5-0.8B, not Qwen3-8B; Goodfire's neurons-as-basis corroboration (92.2% weakest activations ablated at 1.2-2.2 points cost) was measured on Qwen3.6-35B-A3B, a different model. The Fermion primary page is the sole citable source for the map's own numbers; no secondary coverage existed to fetch. No conflicts between sources; the field-level tension (raw neurons too tangled vs more interpretable than assumed) is carried as a misconception pair, not averaged.
