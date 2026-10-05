---
slug: 2026-10-05-dgx-spark-64gb-vs-128gb-which
stage: 04-script
generated_at: 2026-10-05
hub: "[[videos/2026-10-05-dgx-spark-64gb-vs-128gb-which]]"
---

# Drafts and judge verdict

Draft A: comparison-ladder, Decision hook. Draft B: myth-bust, Number shock hook.
Both drafted blind by separate Kimi K3 calls from the same brief and packet law; neither saw the other.

## Draft A (winner, comparison-ladder)
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | Which DGX Spark should you buy? The sixty-four gigabyte box starts at four thousand nine hundred ninety-nine dollars. | Which Spark? Your model decides. | 64GB from $4,999 | Frame 1: hook text 'Which Spark? Your model decides.' fully legible, centered above a two-box lineup; motion onset at 0.3 s: the right-hand box label fades up. On 'four thousand nine hundred ninety-nine dollars' the price '$4,999' stamps under the left box with a scale-in; on 'sixty-four gigabyte' the '64GB' label pops beside it. | hyperframes | giant-number | 6.2 |
| s2 | explain | You waited. The one hundred twenty-eight gigabyte box just hit six thousand nine hundred fifty dollars. Same chip, same speed. Neither is faster. | 64GB vs 128GB: $6,950 | same chip, same speed | On "You waited", hard cut to a split screen: left card labeled "64GB" sits dim, right card "128GB" rises in place carrying "$6,950" in amber. On "Same chip, same speed", one shared bar fades in across both cards reading "same chip, same speed". On "Neither is faster" the bar pulses once, then everything holds. Never more than two elements moving. | hyperframes | split-compare | 7.9 |
| s3 | foreshadow | NVIDIA claims one hundred billion parameters for the small box. That assumes quantization, storing weights in fewer bits. | 100B, NVIDIA's ceiling | only if heavily quantized | On "NVIDIA claims", cut to a centered stack: "100B" in giant amber numerals with the caption "NVIDIA's ceiling" beneath. On "That assumes quantization", a second line rises in place: "only if heavily quantized", while the 100B numerals dim a notch. One text block animates at a time; last beat is static. | hyperframes | centered-stack | 6.2 |
| s4 | explain | Meet GLM four point five Air. Four-bit, the quality floor, is a seventy-three gigabyte download. More than the whole pool. | GLM-4.5-Air at Q4_K_M | 73 GB, over the pool | On "Meet GLM four point five Air", cut to a model card header "GLM-4.5-Air" with a "Q4_K_M" tag. On "seventy-three gigabyte download", a giant amber "73 GB" scales in beside a thin vertical bar marked "64 GB pool"; the 73 GB block clearly overruns the bar top. On "More than the whole pool" the overrun flashes once, then holds. | manim | giant-number | 6.9 |
| s5 | explain | At three-bit it's fifty-seven point two gigabytes of memory. It fits, crumbs left for chat history. | Q3_K_M: 57.2 GB | it fits, crumbs left | On "three-bit", cut to a centered "Q3_K_M" tag above "57.2 GB" in amber, rising in place. On "It fits", the same 64 GB pool bar fades in with the 57.2 GB block now inside it and only a sliver of empty space above, captioned "crumbs left". Fade-ins only, one element at a time, static tail. | manim | centered-stack | 5.5 |
| s6 | payoff_close | Name your biggest real model. Its four-bit download picks the box. | used cards cost less per GB | your 4-bit download picks the box | On "Used cards", a dim side note "used cards cost less per GB" fades in at lower left. On "Name your biggest real model", cut to a three-node flow: "biggest model" to "4-bit size" to "your box", connectors drawing in one at a time; the final node glows amber on "picks the box". In the last half second the nodes fade and the amber wordmark settles center, echoing the centered composition of frame 1. | hyperframes | diagram-flow | 3.8 |

narration_full: Which DGX Spark should you buy? The sixty-four gigabyte box starts at four thousand nine hundred ninety-nine dollars. You waited. The one hundred twenty-eight gigabyte box just hit six thousand nine hundred fifty dollars. Same chip, same speed. Neither is faster. NVIDIA claims one hundred billion parameters for the small box. That assumes quantization, storing weights in fewer bits. Meet GLM four point five Air. Four-bit, the quality floor, is a seventy-three gigabyte download. More than the whole pool. At three-bit it's fifty-seven point two gigabytes of memory. It fits, crumbs left for chat history. Name your biggest real model. Its four-bit download picks the box.

## Draft B (myth-bust)
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | NVIDIA promises one hundred billion parameters on the little box. Seventy-three gigabytes is the four-bit download. | 100B promise, 73 GB file | Frame 1: '100B promise, 73 GB file' fully legible; motion onset at 0.3 s: the '73 GB' half scales up once. On 'seventy-three gigabytes' the file-size bar sweeps in under the text; on 'four-bit download' the 'Q4' chip label fades up beside it. | hyperframes | centered-stack | 6.2 |
| s2 | foreshadow | You waited for a Spark. The sixty-four gigabyte box, four thousand nine hundred ninety-nine dollars. The one hundred twenty-eight gigabyte box, six thousand nine hundred fifty. | 64GB: $4,999 | 128GB: $6,950 | Split-compare: two panels, left "64GB" over "$4,999", right "128GB" over "$6,950". Left panel rises in place on "four thousand nine hundred ninety-nine dollars"; right panel rises in place on "six thousand nine hundred fifty", single amber edge on the right card only. Both panels hold to scene end. | hyperframes | split-compare | 7.9 |
| s3 | explain | Same chip, same memory speed. The pool must hold every parameter, your chat, and the system. | pool: weights + chat + system | Diagram-flow: a tall rectangle labeled "pool" fades in on "The pool". On "every parameter" a large "weights" block rises in place filling most of it; on "your chat" a "chat" block rises in place above it and slowly grows; on "the system" a thin "system" bar fades in pinned to the bottom. One amber accent, on the growing chat block. Blocks end nearly filling the pool. | manim | diagram-flow | 6.6 |
| s4 | explain | Three-bit stores each number in fewer bits. It shrinks to fifty-seven point two gigabytes of memory. It fits. Nothing left for a long chat. | 57.2 GB | it fits | nothing left for a long chat | Giant-number: "57.2 GB" fades in huge at center on "fifty-seven point two gigabytes", small "3-bit" tag above it. Below, a thin pool bar fills to near full on "It fits"; the leftover sliver stays amber. On "nothing left for a long chat" the sliver pulses once. Only the sliver carries the accent. | hyperframes | giant-number | 8.6 |
| s5 | explain | The promise, honestly read, means three-bit. Neither box is faster. Memory costs less elsewhere, unless you need CUDA. | not faster | memory costs less elsewhere | CUDA + the cluster cable | Centered-stack: three short lines rise in place one at a time on their sentences: "not faster" on "Neither box is faster", "memory costs less elsewhere" on the matching phrase, "CUDA + the cluster cable" last. Each new line fades the previous to 40 percent; only one text block animates at a time. | hyperframes | centered-stack | 7.6 |
| s6 | payoff_close | Name the biggest model you run. Its download size picks the box. | name your biggest model | its download size picks the box | 100B promise, 73 GB file | Diagram-flow: node "your biggest model" rises in place on "Name the biggest model you run", arrow draws to node "its download size", second arrow draws to node "the box" as the payoff lands. Within a second, cut to final frame: hook text "100B promise, 73 GB file" dimmed as the loop-anchor recall, wordmark settling for the last half second. | hyperframes | diagram-flow | 4.5 |

narration_full: NVIDIA promises one hundred billion parameters on the little box. Seventy-three gigabytes is the four-bit download. You waited for a Spark. The sixty-four gigabyte box, four thousand nine hundred ninety-nine dollars. The one hundred twenty-eight gigabyte box, six thousand nine hundred fifty. Same chip, same memory speed. The pool must hold every parameter, your chat, and the system. Three-bit stores each number in fewer bits. It shrinks to fifty-seven point two gigabytes of memory. It fits. Nothing left for a long chat. The promise, honestly read, means three-bit. Neither box is faster. Memory costs less elsewhere, unless you need CUDA. Name the biggest model you run. Its download size picks the box.

## Judge scores
## Scores
| # | Row | A | B | Why |
|---|-----|---|---|-----|
| 1 | Hook | 3 | 2 | A: names the Spark and the buyer's own decision inside five words; B: numbers named, but the tension waits for sentence two and the unstated 64 |
| 2 | Payoff timing | 2 | 3 | A: first rung, the price, lands by second 6 while the promised criterion waits; B: the break starts near second 3.4 and pays the hook, scored from the break per the fairness note |
| 3 | Specificity | 3 | 2 | A: one earned number per beat, GLM named, units intact; B: the seventy-three gigabyte file has no owner and one price drops "dollars" |
| 4 | Voice | 3 | 0 | A: clean second person, "crumbs" is the single wry beat and lands unexplained; B: CUDA rides with no definition, a hard constraint 3 break |
| 5 | Navigation | 3 | 2 | A: every transition names what changed and the order is load-bearing; B: the same-chip fact is spent twice and scene five stacks three moves |
| 6 | Difference | 1 | 2 | A: comparison-ladder plus decision hook repeats 2026-09-30, and the buy-rule close with the thirty-five second band echoes 09-29; B: myth-bust is five scripts back with a fresh promise-versus-file rhythm, but the landing is the shared close |
| 7 | Repeat test | 3 | 3 | A: "its four-bit download picks the box" is the repeatable line and the last thing heard; B: same construction, also final |
| 8 | Teaching | 3 | 2 | A: mechanism shown concretely on a named model, viewer can predict the next fit; B: the pool's occupants teach well but the example is faceless |

## Total
A: 21/24. B: 16/24. Winner: draft A.

## Grafts
- none. B's hook scores lower than A's, so no hook graft is on the table. B's two best sentences, the pool holding weights, chat and system, and "the promise, honestly read, means three-bit", each fail the graft test: inserting either forces a rewrite of A's surrounding beats, and the second imports a myth frame into a ladder that never states the myth.

## What the loser needed
The myth-bust needed its breaking number to belong to something: name GLM four point five Air in the same breath as the seventy-three gigabyte download, and give CUDA its appositive, since a faceless file size and a bare technical term cost it specificity and a hard voice constraint. It also needed the sixty-four gigabyte pool established inside the hook so the break lands felt rather than stated, and to stop paying the same-chip fact twice.

## Outcome
Winner: draft A (21/24 to 16/24). No grafts: the eligible sentences from B would have forced rewrites of A's surrounding beats. B's pool beat (weights, chat, system in one pool) is the line the channel should keep in the rotation for a future KV-cache video.
What B needed: the breaking number needed an owner (name GLM four point five Air beside the 73 GB download), CUDA needed its appositive, and the sixty-four gigabyte pool had to be established inside the hook.

## Decisions
- Writer A first call hit the 32000-token cap and returned empty output; the retry (same packet plus a reasoning-budget footer) returned complete files. Writer B completed first call.
- Fix pass before judging (both drafts): 3 hashtags, 20 keyword tags, referent phrasing on the gigabyte numbers, motion onset named in the hook brief, visual beats in the s1 brief; B trimmed from 132 to 112 words after the referent fixes pushed it over the band; A's close trimmed to the payoff sentence.
- Gates on both drafts after the fix pass: validate_storyboard zero blockers and zero advisories; eval_short all nine gates green, number_spend 5 of 5.
