---
slug: 2026-10-24-256-tops-beats-1000-tops-readi
format: classic
structure: myth-bust
style_pack: halftone
value_types: TEACHES, REFRAMES
promise: after forty seconds you can read an AI box's spec sheet and know which number actually sets the speed you feel
target_duration_s: 36
brief: 2026-10-24-256-tops-beats-1000-tops-readi-brief.md
drafts: 2026-10-24-256-tops-beats-1000-tops-readi-drafts.md
---

# 256 TOPS vs 1,000 TOPS: reading the fine print

## Decisions
- Structures tried: myth-bust (draft A) and comparison-ladder (draft B); A won 21 to 18 on the judge rubric, no grafts.
- Hook: candidate 'DGX Spark's label isn't its speed.', reworded at board time from 'A forty-watt box claims it beats NVIDIA's thousand-TOPS giant.'; reason: the variety classifier reads 'thousand' as number-shock, which 2026-10-23 already used (hard sameness rule), and ten words broke the seven-word frame-1 budget. The 256-vs-1000 pair stays on screen in s01 as the loop anchor.
- Style pack: halftone (topic-fit row 'myth-busting'; the hintless rotation script suggested signal, overruled by the pack table's specialist row; previous pack silicon, rotation respected).
- entity_spend soft advisory 0.238 kept: the brief's entity pool is source-heavy (TechRadar, Wccftech, CNX, NVIDIA docs); the script names the products the viewer meets (DGX Spark, NVIDIA, Sipeed, Qwen) and the top-2 entities are present.
- Validator: zero blockers, zero advisories on the final board. Eval: gate1_ready, failures none; sameness clean against the last five.

## Hook candidates
1. DGX Spark's label isn't its speed. *
2. A forty-watt box claims it beats NVIDIA's thousand-TOPS giant.
3. DGX Spark or the forty-watt challenger? Bandwidth decides.
4. One number ties these boxes: two hundred seventy-three gigabytes a second.
5. The thousand-TOPS machine is not the fast one.
6. Two hundred fifty-six TOPS just picked a fight with a thousand.
7. NVIDIA's biggest number is a footnote.
8. You are comparing AI boxes by the wrong number.
9. A forty-dollar-a-year-to-run box says it beats NVIDIA's desk giant.
10. Reading the label, not the benchmark, settles this box fight.
11. The spec sheet says four times faster. Your chat says otherwise.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | DGX Spark's label isn't its speed. | 256 TOPS vs 1000 TOPS | Frame 1: two spec plaques centered and fully legible, small amber 256 plaque left, large gray 1000 plaque right; motion onset at 0.30 s as both plaques rise-in-place, small plaque takes a 1.12 punch fitted inside the safe area; first and last 8 frames stable. | hyperframes | giant-number | 3 |
| s02 | explain | NVIDIA's footnote calls its thousand theoretical, sparse math that skips zeros. You read the label's TOPS, its peak-math rating, and assumed four times meant four times faster. | 1000 TOPS: theoretical, sparse | Footnote line fades in under the big plaque on "footnote"; a magnifier scale-in highlights the sparse disclaimer on "skips zeros". One text block animates. | hyperframes | split-compare | 9 |
| s03 | explain | Prefill reads your prompt once. Decode answers word by word, re-reading the model each time. | prefill: one pass, decode: word by word | Prompt block flows into a wide amber bar on "reads your prompt once"; then single tokens drip out one at a time on "word by word". Diagram draws on, onset 0.3 s. | manim | diagram-flow | 6 |
| s04 | explain | TOPS is horsepower, bandwidth the speed limit: both boxes cruise at two hundred seventy-three gigabytes per second. Decode is city driving. | 273 GB/s on both boxes | Giant amber digits rise on "two hundred seventy-three"; two box silhouettes fade in beneath, capped by one shared ceiling bar on "both boxes". | hyperframes | giant-number | 7 |
| s05 | explain | Horsepower wins drag races, and prefill is one. Sipeed's chart: vendor-run, one Qwen model, speculative decoding off, barely ahead. | 1 model, vendor-run, spec decode off | Two bar columns draw on nearly level on "barely ahead"; a small amber tag fades in listing the test conditions. Onset 0.3 s, two elements max. | manim | split-compare | 6 |
| s06 | payoff_close | Judge boxes by tokens per second on the Qwen you run, never by TOPS on the tin. | tokens per second > TOPS | Centered rule line scales in on "tokens per second"; holds static; cut within one second of the last word. | hyperframes | centered-stack | 5 |

## Notes for review
- The s01 on-screen pair (256 vs 1000) is not spoken in s01: the loop-anchor exception; the digits return as spoken words nowhere, by design, and the close rhymes the label motif.
- Vendor margins (25% prefill, 30% decode from Sipeed's tweet) are omitted: the chart values are unverified and TechRadar/CNX read the chart as only slightly ahead; s05 says 'barely ahead'.
- 'Nearly four times faster' paraphrase dropped at board time; the myth beat says 'assumed four times meant four times faster' (viewer's words from the brief's viewer_situation).
- The llama.cpp prefill/decode pair (2986.97 vs 61.06 t/s) was cut for the number budget; if the reviewer wants the measurement spoken, it belongs in s05 in place of the chart hedge.
