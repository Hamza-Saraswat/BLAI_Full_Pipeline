---
slug: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod
format: classic
structure: number-first
style_pack: silicon
value_types: TEACHES,REFRAMES
promise: after 35 seconds the viewer can say what eight linked Sparks actually run, and the one catch: capacity, not speed.
target_duration_s: 32
brief: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod-brief.md
drafts: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod-drafts.md
---

# 8 DGX Sparks, 1 TB: frontier models on a desk

## Decisions

- Structures tried: news-react-so-what (draft A) and number-first (draft B); both clear the rotation (last two shipped: contrarian-take, worked-example). Judge tie 21/24; B won on row 6 (difference): A re-shipped the news-react skeleton from 2026-10-20 at the same ~37 s.
- Hook: candidate 2 "Eight desk boxes now hold what a datacenter rents" family; spoken hook "Eight DGX Sparks pool one terabyte of memory", frame-1 text "8 desk boxes | 1 TB pooled memory". Number-first shape; writer B drifted from its assigned named-contradiction pattern and the judge scored the result higher than a forced contradiction would read, so the board keeps hook_pattern unset and the classifier reads number-shock.
- Graft: draft A's closer "The frontier moved from their building to your desk." replaces B's final sentence (judge order: same beat, same person, no numbers, makes the repeatable line the last thing heard).
- Gates: validator 0 blockers; advisories kept: 8 hashtags / 0 keyword tags (finalized at stage 05 per playbook), FK 5.7, title 41 chars (package stage rewrites title), DGX/GLM lexicon entries exist. Eval hard gates all pass; soft entity_spend advisory kept on purpose: top2 wants ConnectX-7 present, and the script says "the cable" in s04 because the viewer does not need the marketing name to feel the 11x gap (finding: entity gates ignore glossary terms).
- est_duration_s recomputed at 2.9 wps; est sum 37.0 s against target 32 s is inside tolerance (0.8-1.25).

## Hook candidates

1. One terabyte of memory, on your desk.
2. Eight desk boxes now hold what a datacenter rents. *
3. NVIDIA just blessed an eight-Spark cluster.
4. Your desk just got a terabyte of model memory.
5. Seven hundred fifty-three billion parameters, zero datacenter.
6. A frontier model now runs on eight desk boxes.
7. Eight Sparks, one terabyte, one cable.
8. Eight DGX Sparks replaced the datacenter rental.
9. The four hundred seventy gigabyte file on a desk.
10. Eight little boxes, one frontier model, no cloud.

(* the kept family: candidates 2/8/10 scored highest -- payoff word early, product named, true per the brief, situation named; the spoken hook is the number-first variant of this family)

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Eight DGX Sparks pool one terabyte of memory. They are desk boxes. A terabyte meant a building you rent. | 8 desk boxes \| 1 TB pooled memory | Frame 1: "8 desk boxes" as giant digits-plus-words inside the silicon slab frame, fully legible. Motion onset t=0.30s: the "8" scales 1.0 to 1.08 and settles. On "desk boxes" eight tiny slab glyphs fade in beneath the number. On "used to mean a datacenter" the glyphs hold still and a faint chrome rack outline fades in behind, then dims. One text block animating at a time. | hyperframes | giant-number | 6.6 |
| s02 | explain | GLM five point three runs across all eight. Seven hundred fifty-three billion parameters. Squeezed to four bits a weight: about four hundred seventy gigabytes of model. | GLM 5.3 across 8 nodes \| 753B params -> 470 GB | Split: left "GLM 5.3" over a row of eight slab glyphs, each pulsing once in sequence on "across all eight" (staggered, never simultaneous). Mid-scene on "seven hundred fifty-three billion parameters" the left label hard-cuts from "753B params" to "4-bit weights" in amber. Right: a weight value "1.0000" collapses to "1.0" as the text hard-cuts to "470 GB", amber fill on the collapsed value; the fill completes on "gigabytes of model". Two animated elements max; hard cuts only. | hyperframes | split-compare | 9.7 |
| s03 | explain | NVIDIA measured thirty-one tokens per second for one user. That is how fast the model writes: about reading speed. | 31 tokens/sec \| 1 user, reading speed | Giant "31" digits with "tokens/sec" beneath in the slab frame. On "one user" a single amber cursor glyph blinks at a text line under the number, typing three short dashes then pausing: reading speed made visible. On "about reading speed" the cursor stops and the line dims. Number is on screen exactly while spoken. | hyperframes | giant-number | 6.6 |
| s04 | explain | The catch is the cable. A Spark's own memory outruns its ConnectX seven link, the cable between boxes, eleven times over. Eight boxes buy room, not speed. | ConnectX-7 cable: 11x slower \| room, not speed | Two panels flow: a wide amber lane inside one slab (fast) over a long thin trace running box to box (slow). On "eleven times faster" the inner lane pulses once; the trace stays dull. On "eight boxes buy room" the eight-slab grid from s01 returns small at top, pooling outline drawing around them while the trace dims. Hard cuts only. | hyperframes | diagram-flow | 9.7 |
| s05 | payoff_close | So the biggest models stopped being rentals. The frontier moved from their building to your desk. | frontier models, not rentals \| your desk | Centered: "frontier models, not rentals" types on one line, then hard-cuts to "your desk" beneath it as the slab frame from frame 1 fades back in around the words (rhyme with s01). Amber underline settles under "your desk". Wordmark settle in the final 0.5 s; stop within a second of the last spoken word. | hyperframes | centered-stack | 4.5 |

## Notes for review

Grafted closer from draft A (judge order): "The frontier moved from their building to your desk." replaces "A frontier checkpoint now runs on your desk." Reviewer: "eleven times slower" rounds the measured 196 Gb/s link vs 273 GB/s inside one Spark (claim 8); 31 TPS is NVIDIA's vendor benchmark, attributed in narration; the ~$55,600 build cost and the 816B/Q8 fit stay unspoken (Unverified). "G L M five point three" and "ConnectX seven" are pre-spoken for the voice engine.
