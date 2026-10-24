---
slug: 2026-10-24-256-tops-beats-1000-tops-readi
stage: 04-script
generated_at: 2026-10-24T13:30:00Z
hub: "[[videos/2026-10-24-256-tops-beats-1000-tops-readi]]"
---

# Drafts and judge: 2026-10-24-256-tops-beats-1000-tops-readi

Writers ran blind on kimi-k3 (separate processes, nothing shared). Board-time fixes applied
after drafting, before gating: hook A reworded to clear the frame-1 word budget and the
number-shock rotation clash; hook B trimmed; both hook visual briefs given explicit frame-1
composition; B's s03 on-screen pair cut to 6 words; B's s04 given a punch sentence.

## Draft A (myth-bust)

Working title: 256 TOPS vs 1,000 TOPS: reading the fine print

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| s01 | hook | A forty-watt box claims it beats NVIDIA's thousand-TOPS giant. | 256 TOPS vs 1000 TOPS | Two spec plaques rise-in-place at 0.3 s; small amber plaque takes a 1.12 punch fitted inside safe area, big plaque stays gray. First and last 8 frames stable. | hyperframes | giant-number | 4 |
| s02 | myth_break | NVIDIA's footnote calls its thousand theoretical, sparse math that skips zeros. You read the label's TOPS, its peak-math rating, and assumed four times meant four times faster. | 1000 TOPS: theoretical, sparse | Footnote line fades in under the big plaque on "footnote"; a magnifier scale-in highlights the sparse disclaimer on "skips zeros". One text block animates. | hyperframes | split-compare | 9 |
| s03 | teach | Prefill swallows your prompt in one pass. Decode answers word by word, re-reading the model each time. | prefill: one pass, decode: word by word | Prompt block flows into a wide amber bar on "swallows"; then single tokens drip out one at a time on "word by word". Diagram draws on, onset 0.3 s. | manim | diagram-flow | 6 |
| s04 | measure | TOPS is horsepower, bandwidth the speed limit: both boxes cruise at two hundred seventy-three gigabytes per second. Decode is city driving. | 273 GB/s on both boxes | Giant amber digits rise on "two hundred seventy-three"; two box silhouettes fade in beneath, capped by one shared ceiling bar on "both boxes". | hyperframes | giant-number | 7 |
| s05 | honest_catch | Horsepower wins drag races, and prefill is one. Sipeed's chart: vendor-run, one Qwen model, speculative decoding off, barely ahead. | 1 model, vendor-run, spec decode off | Two bar columns draw on nearly level on "barely ahead"; a small amber tag fades in listing the test conditions. Onset 0.3 s, two elements max. | manim | split-compare | 6 |
| s06 | payoff_close | Judge boxes by tokens per second on the Qwen you run, never by TOPS on the tin. | tokens per second > TOPS | Centered rule line scales in on "tokens per second"; holds static; cut within one second of the last word. | hyperframes | centered-stack | 5 |

## Value delivery
- TEACHES: "NVIDIA's footnote calls its thousand theoretical, sparse math that skips zeros."
- REFRAMES: "Judge boxes by tokens per second on the Qwen you run, never by TOPS on the tin."

## Analogy used
Engine horsepower against the speed limit (TOPS as bench horsepower, bandwidth as the limit, decode as city driving). Limit stated in one clause: "Horsepower wins drag races, and prefill is one."

## Notes
- Mandated hook screen text shows "256" but the verbatim hook narration never says two hundred fifty-six, so that digit is unspoken in s01; the user file fixed both, reviewer should confirm the exception stands.
- Vendor margins (25% / 30% from the tweet) omitted entirely; "barely ahead" follows the TechRadar and CNX reading of Sipeed's chart, since exact bar values are unverified.
- No independent MaixStation test exists; s05's "vendor-run" carries that hedge without asserting shipping performance, which is unverified.
- "Its peak-math rating" is the compact TOPS appositive; the full glossary definition would not fit the 37 s budget.
- Totals: 110 narration words, 10 sentences, average 11.0 words; 37 s estimate sits at the top of the sweet band, so s02 (27 words in 9 s) is the scene to trim first if VO runs long.

## Draft B (comparison-ladder)

Working title: 256 TOPS vs 1,000 TOPS: the tie both boxes share

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| s01 | hook | DGX Spark or the forty-watt challenger? Bandwidth decides. | Spark vs 40W box | Two product cards rise in place, onset 0.3 s: tall Spark card left, small challenger card right with amber pulse on "forty-watt challenger"; thin amber underline sweeps in on "Bandwidth decides." First and last 8 frames stable. | hyperframes | split-compare | 3 |
| s02 | context | You compare local AI boxes by TOPS on the tin. Cost: Spark, nearly seven thousand dollars. MaixStation, under four thousand dollars, promised. | COST · $6,949.99 · <$4,000 promised | Giant "$6,949.99" scales in on "nearly seven thousand dollars"; on "promised" a smaller "<$4,000" tag fades in below with amber "promised" chip. Only the price block animates. | hyperframes | giant-number | 7 |
| s03 | teach | Speed: a thousand TOPS, peak math per second, against a dense two hundred fifty-six. NVIDIA footnotes its thousand: theoretical sparse, zeros skipped. | 1,000 TOPS* vs 256 TOPS dense · *theoretical sparse | Split columns fade in: left "1,000 TOPS" in hatched grey with amber asterisk, right shorter solid amber "256 TOPS dense"; footnote "*theoretical sparse" fades in on the word "footnotes." | manim | split-compare | 7 |
| s04 | teach | What fits is decode, your reply typing out. Both boxes share one speed limit: two hundred seventy-three gigabytes per second. Horsepower wins the drag race: reading your prompt at once. | WHAT FITS · 273 GB/s both · TOPS = hp | Diagram: one road, speed-limit sign reading 273, both box badges cruising side by side; dots (tokens) flow at one rate. Sign scales 1.12 on "speed limit"; small drag strip lights amber at the edge on "drag race." Two elements animating max. | manim | diagram-flow | 10 |
| s05 | objection | The win is Sipeed's test, one Qwen model. Its chart shows a slight edge. | vendor chart · 1 Qwen · MTP off · slight edge | Centered card: two nearly equal unlabeled bars fade in; caveat line rises beneath on "one Qwen model." Bars stay visibly close; no values printed on bars. | manim | centered-stack | 5 |
| s06 | payoff_close | Judge by tokens per second on your model, never TOPS on the tin. | Sipeed's rule: tok/s ≈ bandwidth ÷ model size | Formula scales in on "tokens per second"; on "never TOPS on the tin" a small tin label gets one amber strike. Cut within a second of the line ending. | hyperframes | giant-number | 4 |

Total: 36 s, 109 spoken words, 13 sentences (avg ~8 words).

## Value delivery
- TEACHES: "Both boxes share one speed limit: two hundred seventy-three gigabytes per second."
- REFRAMES: "Judge by tokens per second on your model, never TOPS on the tin."

## Analogy used
Engine horsepower against the speed limit (brief candidate). Limit clause: "Horsepower wins the drag race: reading your prompt at once." -- i.e., big TOPS genuinely help at prefill, just not at the decode you feel.

## Notes
- Rounded $6,949.99 to "nearly seven thousand dollars" in narration; exact figure lives on screen. Reviewer: confirm the rounding is acceptable or I respell it in full words (+3 words, still in band).
- "Promised" hedges the under-$4,000 MaixStation price; the brief lists shipping price/performance as Unverified (Kickstarter months out, no independent hardware test). Same reason s05 prints no bar values.
- Vendor margins (25% prefill, 30% decode) omitted entirely: the brief flags the tweet-vs-chart conflict and the chart values are unverified. s05 uses "slight edge," the TechRadar/CNX reading.
- "Dense" is glossed only by contrast with "sparse, zeros skipped." If the reviewer wants an explicit dense gloss, add "every multiply counted" (+4 words, push s03 to 8 s, total 37 s).
- Key numbers spent: 40 W, $6,949.99, 1,000 TOPS (the 1 PFLOP FP4 figure), 256 TOPS, 273 GB/s = 5, at the cap. The llama.cpp pp2048/tg32 pair and the 500 TOPS dense figure were deliberately left out to stay under it.
- "What fits" rung is read as decode experience, the thing that fits your chat, since both boxes sit on the same 273 GB/s; no capacity claim (128 GB) is asserted for either box.
- No scene lacks a key number or named entity: s06 carries "Sipeed's rule" on screen (claim 10).

## Judge

## Verdict

WINNER: draft A -- 21 total (A 21, B 18).

## Score table

| # | Row | A | B | Justification |
|---|---|---|---|---|
| 1 | Hook | 3 | 3 | A: NVIDIA, 40 W and 1,000 TOPS named, "claims" carries the upset tension inside five words. B: DGX Spark named, choice tension at "or" (word 3), paid by "Bandwidth decides" in 3 s. |
| 2 | Payoff timing | 2 | 2 | A: scored from the break per fairness note -- the break's payload "theoretical, sparse" lands ~6–7 s, by second 8. B: first concrete (price) lands ~6 s; the promised bandwidth payoff waits until ~20 s. |
| 3 | Specificity without cramming | 3 | 2 | A: one new number per sentence, each load-bearing, none decorative. B: s03 spends two new numbers (1,000 and 256) in a single sentence, over the one-per-sentence budget. |
| 4 | Voice | 3 | 2 | A: "Decode is city driving" is the wry beat, lands, unexplained. B: clean second person, but "Horsepower wins the drag race: reading your prompt at once" explains its own beat. |
| 5 | Navigation | 3 | 1 | A: every transition carries content ("Horsepower wins drag races, and prefill is one" pivots on the built analogy); reordering breaks the chain. B: spoken "Cost:" / "Speed:" / "What fits" rung labels survive deletion untouched -- mechanical filler, capped at 1. |
| 6 | Difference | 1 | 3 | A: repeats 10-19's exact structure (myth-bust), hook pattern (named-contradiction), and ~37 s duration. B: comparison-ladder shape, question-answer opening rhythm, and rule-strike landing all absent from the recent five. |
| 7 | Repeat test | 3 | 3 | Both close on the repeatable line -- "never (by) TOPS on the tin" -- and it is the last thing heard. |
| 8 | Teaching | 3 | 2 | A: "re-reading the model each time" shows the why, so a viewer can predict any same-bandwidth box ties at chat and bigger models decode slower. B: the 273 GB/s cap is shown concretely, but why decode is capped is named, not shown. |

Totals: A 21, B 18.

## Grafts

None. B's hook scores level with A's on row 1 (3 vs 3), so no hook graft is available. B's strongest unique material -- the price ladder ("nearly seven thousand dollars... under four thousand dollars, promised") -- says something A omits rather than something A says worse, and inserting it would force two new numbers into A's budget and a rewrite of the already-full s02. The one real gap in A that B closes (a spoken "two hundred fifty-six") sits inside A's 27-word s02, the scene A's own notes flag for trimming; grafting it there requires rewriting surrounding beats, which the rules forbid.

## What the loser needed

B needed to stop speaking its ladder rungs -- "Cost:", "Speed:", "What fits" all delete cleanly, which is what capped navigation at 1 -- and let the content itself carry the transitions. It also needed the one mechanism beat A has and it lacks: why decode is bandwidth-bound (re-reading the model per token), without which the 273 GB/s tie is a fact to believe rather than a rule the viewer can predict from.

## Outcome

Winner: draft A (21 to 18), no grafts. Saved as 2026-10-24-256-tops-beats-1000-tops-readi-script.md and 2026-10-24-256-tops-beats-1000-tops-readi-storyboard.json.
