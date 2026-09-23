---
slug: 2026-09-23-best-coding-models-on-dgx-spar
format: smooth-explainer
structure: comparison-ladder
style_pack: silicon
value_types: TEACHES,EQUIPS
promise: After this Short you can route your coding-agent work on a DGX Spark to the right open model, and configure the thinker so follow-ups stop costing seconds.
target_duration_s: 86
brief: 2026-09-23-best-coding-models-on-dgx-spar-brief.md
drafts: 2026-09-23-best-coding-models-on-dgx-spar-drafts.md
---

# The Two-Model Spark: Fast Coder vs Smart Coder

## Decisions
- Structures tried: comparison-ladder (draft A) and myth-bust (draft B); both cleared rotation (last two were worked-example and number-first). A won 21 to 15 on the judge rubric.
- Hook: "Speed or smarts: pick your coder" (decision pattern) over "You want the biggest coder that fits" (situation); last two hook patterns price and number-shock were banned, and the two picks had to differ in kind.
- Graft from B: "Same box, same model, nothing changed but configuration." appended to s8 after "With it, point-three."; names the controlled experiment A only implied, adds no numbers.
- Gates: validator 0 blockers 0 advisories; eval gate1_ready true, failures none, entity_spend soft advisory only (script narrows entities to the models it teaches); sameness clean against 5 entries; normalizer scenes_changed 4.
- Validator warnings kept with reasons: title 46 chars (package stage rewrites it); FK 5.2 (band target 5, driven by benchmark phrasing); "actually" appears once in mid-script dialogue; hook scene brief names the 0.30 s onset (patched post-judge).

## Hook candidates
Qwen3-Coder-Next hits 85 tok/s on a Spark
Speed or smarts: pick your coder *
Your Spark deserves a smarter coder
You want the biggest coder that fits
The fastest coder here scores worst
85 tok/s of code, one catch
One box, two coders, no waiting
Stop paying the API tab for agents
GLM Flash eats the whole box
DeepSeek doesn't fit. What does?

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | You run coding agents against a chat API every day. Two open coders now fit the DGX Spark you have been eyeing. They pull in opposite directions. | Speed or smarts: pick your coder | Frame 1: matte-black board, two empty chip footprints side by side, hook line in Chakra Petch centered above them. At 0.35s a copper trace lights from each footprint, pulling left ... | hyperframes | centered-stack | 10.0 |
| s2 | foreshadow | Here's the axis: what your agent's day actually feels like. Every follow-up resends a twenty-three-thousand-token prompt, tokens being the word-pieces models read. So the whole day taxes both speed and smarts. | 23,000-token prompt | resent every follow-up | A loop diagram routed at 45 and 90 degrees: an AGENT block and a MODEL block joined by two copper traces. On 'every follow-up resends' a thick packet of light travels the request t... | manim | diagram-flow | 9.7 |
| s3 | explain | On speed, Qwen's Coder Next writes at eighty-five tokens a second on this one box. It's a mixture-of-experts coder, a big staff where each token asks only a few specialists. That's autocomplete speed for your agent's tight loops. | Qwen3-Coder-Next | 85 tok/s decode | The CODER A chip from s1 drops onto its footprint with a pick-and-place settle on 'Qwen's Coder Next'. On 'eighty-five tokens a second' the giant digits 85 tok/s stamp in copper at... | hyperframes | giant-number | 14.7 |
| s4 | explain | But your day also has hard code. On the coding benchmark both model cards report, Coder Next scores forty-four point three. | SWE-bench Pro | Qwen3-Coder-Next: 44.3 | Board splits left and right along a routed copper divider. Left panel header reads SWE-bench Pro in mono. On 'hard code' a tangled trace maze appears on the right, harder routing t... | hyperframes | split-compare | 6.6 |
| s5 | explain | Qwen's twenty-seven billion thinker scores sixty-one point seven on that same benchmark. It thinks through the tickets that make the fast one guess. Same tests, harder tickets closed. | SWE-bench Pro | Qwen3.8-27B: 61.7 | The CODER B chip drops onto its footprint on 'twenty-seven billion thinker'. On 'sixty-one point seven' the giant digits 61.7 stamp at center, and the copper bar under it runs visi... | hyperframes | giant-number | 9.1 |
| s6 | explain | What fits settles the rest. GLM's Flash runs only as a heavily shrunk copy that eats most of the box. DeepSeek's Flash is twice the box even shrunk, so it stays a science project. | GLM-5.3-Flash: shrunk, most of box | DeepSeek V4.1 Flash: no fit | A grid of memory cells represents the box's shared pool. On 'heavily shrunk copy' a GLM-5.3-Flash chip compresses with a squash animation and lands, flooding most of the grid coppe... | hyperframes | grid | 10.3 |
| s7 | explain | The honest catch is the platform. Street prices climbed past NVIDIA's own list. The certified driver you want is still an unanswered forum thread. The newer Ubuntu path is a hand-rolled recipe, not a vendor upgrade. | the catch | price above list | driver: open thread | Ubuntu: recipe | A horizontal copper timeline routes across the board with three flagged vias. On 'street prices climbed' the first via raises a price tag above a crossed-out list tag, no digits, j... | hyperframes | timeline | 11.6 |
| s8 | explain | Back on the box, configuration decides your day. Give the thinker a prefix cache, the engine's memory of what it already read. Without it, follow-ups took twenty-two seconds. With it, point-three. Same box, same model, nothing changed but configuration. | prefix cache on | follow-up: 22 s → 0.3 s | The s2 loop returns, now with a CACHE block tapped off the MODEL's input trace. On 'a prefix cache, the engine's memory' the CACHE block lights and stores a copy of the incoming pr... | manim | diagram-flow | 12.2 |
| s9 | payoff_close | Send the loops to Coder Next, and send the hard code to the thinker. | loops → Coder Next | hard code → the thinker | Both chips now seated on their footprints. On 'send the loops to Coder Next' a fast pulse train routes left into the Coder Next chip. On 'send the hard code to the thinker' a singl... | hyperframes | centered-stack | 4.4 |

## Notes for review
Every speed figure traces to one survey author and one forum author on nightly builds with no first-party tok/s confirmation, so the September 2026 date-stamp matters. The two benchmark scores are vendor-reported on the model cards, not independently reproduced. Confirm the catch beat stays numeral-free: street price, driver thread, and Ubuntu recipe are all prose-only per the numbers law.
