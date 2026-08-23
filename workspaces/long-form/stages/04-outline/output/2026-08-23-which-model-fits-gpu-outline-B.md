---
slug: 2026-08-23-which-model-fits-gpu
series: benchmarks
structure: concept-deep-dive
value_types: EQUIPS, TEACHES
target_minutes: 12
---

# Outline: Which model actually fits the card you own

## Angle
Whether a model fits your card is decided by its file size plus the cache it grows, never by its parameter count.

## Value brief
- TEACHES: what actually occupies a graphics card when a model loads, which is the weights file at its measured width, the cache computed on key-value heads rather than attention heads, and a runtime slice nobody publishes.
- EQUIPS: a rule for picking tonight's build from two numbers you can read off a page, plus the one command that tells you whether you got it right instead of guessing at headroom.
- Hook: "You own a card with twelve gigabytes on it. The model page says twenty-seven billion parameters, and that number cannot tell you whether it runs. Somebody has published that exact model as a file weighing six point one nine gigabytes."
- Payoff: "Take the biggest build whose file and cache both fit, then let the layer split settle it." (last spoken sentence; nothing follows it)
- The number by 0:20: six point one nine gigabytes, the smallest published build of the dense twenty-seven-billion-parameter Qwen3.8-27B, from the Unsloth model card. It arrives about sixteen seconds in and collides head on with the twenty-seven billion printed on the same page.

## Chapters
| # | Chapter | Target s | The one idea | Measurement shown | Muted viewer understands |
|---|---------|----------|--------------|-------------------|--------------------------|
| 1 | Two Files, One Model | 105 | The parameter count cannot answer "does it fit", because one model ships as many files of very different size. | Unsloth's Qwen3.8-27B file table: published builds from 6.19 GB (UD-IQ1_S) up to 25.3 GB (UD-Q6_K_XL) | A publisher's file table beside one capacity bar for a 12 GB card; the smallest row drops in and fits, the largest row drops in and overflows a 24 GB bar too. |
| 2 | Where The Arithmetic Breaks | 150 | Parameters times bits is the wrong sum twice, because the payload is not the whole file and the label is not the width. | llama.cpp's quantize table: Q4_K_M measures 4.8944 bits per weight (Q6_K 6.5633, Q8_0 8.5008, F16 16.0005); Llama-3.1-8B falls 14.96 GiB to 4.58 GiB | The label column and the measured bits-per-weight column set side by side, every row off by its block scales, with the hand-done sum crossed out beside them. |
| 3 | What Your Card Actually Holds | 195 | Three things occupy the card: the weights file, the cache that grows with the conversation, and a runtime slice nobody publishes. | NVIDIA's published cache formula worked to about 2 GB for Llama 2 7B at 4,096 tokens; Qwen3-8B's config.json showing 32 query heads against 8 key-value heads, so the printed formula overstates it fourfold | The bar fills in three blocks: a solid weights block, a cache block that grows as a chat scrolls beside it, then a hatched block at the top carrying no number at all. |
| 4 | Long Context And Experts | 165 | The same arithmetic bites in two places, where the cache line keeps growing and where the weights line is the whole expert set rather than the active slice. | Long-context study: about 0.8% accuracy drop at 8-bit against up to 59% loss for 4-bit methods; Hugging Face on Mixtral 8x7B, resident like a dense 47B while computing like a 12B; DeepSeek V4 Flash's smallest published quant at 82.5 GB | The same bar twice: first the cache block grows until it shoves the weights past the end, then the weights block widens to the full expert set with a single sliver lit. |
| 5 | What To Download Tonight | 105 | You pick the build from two numbers you can read, then let the runtime confirm it instead of trusting headroom folklore. | Ollama's documented layer split, values such as 48% CPU and 52% GPU in `ollama ps`; the 2025 study across roughly 1,700 scenarios where 8B at 8-bit beats 14B at 4-bit | The finished ledger with the chosen row ticked, then one quoted docs frame showing a CPU and GPU percentage split. |

Total 720 s (12:00), about 1,800 narration words at 150 wpm. Word budget by chapter: 260 / 375 / 490 / 415 / 260.

## Visual philosophy
One memory ledger carries the episode: a single capacity bar for a twelve-gigabyte card that fills, empties and refills from the opening frame to the closing one, with the publishers' own artefacts cut in beside it, a model card file table, the llama.cpp quantize table, a config file, never replacing the bar. Terminal frames appear only as sourced documentation excerpts, labelled with their publisher and never presented as our own run, because nothing in this episode was measured on our hardware and the episode says so out loud in the first chapter. Everything numeric stays typographic, with digits, units and the publisher's name set as on-screen type beside the bar, since the narration speaks every number as words and never reads a digit.

## Decisions
- Angle chosen: the deciding number is file size plus cache, not parameter count. It is one sentence a viewer repeats at a keyboard, it survives every model in the brief, and it is the only claim the episode can make without a first-party measurement. Rejected: "four-bit is a trap for reasoning work", which is a real result in the brief but is a myth-bust argument, not a mechanism, and would put the payoff in chapter four; rejected: "bandwidth, not capacity, is what you actually buy", which opens a second thesis this episode never closes.
- Worked example: Qwen3.8-27B against a twelve-gigabyte card. Its published ladder spans every consumer tier, so some rungs fit and some do not, which keeps a live decision on screen for twelve minutes, and a dense twenty-seven billion is where the naive parameter arithmetic is most badly wrong. Rejected as the carrier: Llama-3.1-8B, which fits everything so nothing is at stake, and Ornith 1.5 9B, whose whole ladder stays under ten gigabytes.
- The carried example is the ledger plus that one model, and it is never swapped. The llama.cpp table (measured on Llama-3.1-8B), NVIDIA's Llama 2 7B cache figure, Qwen3-8B's config and the Mixtral and DeepSeek exhibits appear beside the bar as cited evidence for a step in the arithmetic, and the bar itself stays Qwen3.8-27B on twelve gigabytes throughout, including in chapter four.
- Value types EQUIPS and TEACHES, not PROVES: the DGX Spark was unreachable, so every number here is published by somebody else. Chapter one states that on the record and every on-screen figure carries its publisher, which is a visual commitment, not a closing disclaimer, because nothing may follow the payoff.
- The hook uses the 6.19 GB build without implying it is a good build. It is named on screen as UD-IQ1_S, a one-bit-class build, and the quality cost lands in chapter two and again in the rule in chapter five.
- Nothing from the Unverified list is asserted. No headroom figure is spoken, so chapter five replaces the folklore gigabyte with the llama.cpp maintainer's statement that the runtime's slice is not calculable and with the `ollama ps` split as the check. No multiple is given for CPU offload, only llama.cpp's own "much slower". No claim that four-bit is indistinguishable in conversation. Units stay as published, GiB from llama.cpp and GB from the model cards, and are never mixed inside one comparison.
- No positional labels anywhere. Chapter breaks use one legal move each: into two, contradict the expectation ("That reads like a file size problem. The label lies too."); into three, jump to the consequence ("That is only the first line. The conversation writes the second."); into four, name what changes ("Now the context is long."); into five, answer the question the last chapter raised ("So which file do you actually pull?").
- Deliberately left out: the Spark's 128 GB at 273 GB/s bandwidth fact, the llama.cpp perplexity table, the Apple unified-memory reserve, and the contradictory model cards. The four-bit rule reversal is demoted from its own chapter to the qualifier inside the chapter five rule, because this structure spends chapter four on the two edge cases.
- Structure and series are paired by assignment: `benchmarks` would normally suggest `buyers-guide`, and the deep dive earns its place here because the brief carries a mechanism with one worked example rather than two contenders on a shared axis.
