---
slug: 2026-09-08-mistral-raises-3b-euro-for-ope
format: classic
structure: comparison-ladder
style_pack: halftone
value_types: TEACHES,REFRAMES
promise: after ~35 s you can repeat one rule for which Mistral model runs on your own hardware and which one needs a datacenter
target_duration_s: 37
brief: 2026-09-08-mistral-raises-3b-euro-for-ope-brief.md
drafts: 2026-09-08-mistral-raises-3b-euro-for-ope-drafts.md
---

# Mistral tonight: Small 4 runs, Large 3 waits

## Decisions
- Structures tried: contrarian-take (A) vs comparison-ladder (B); both cleared rotation (last two scripts were number-first and news-react-so-what). B won 21-18 on the blind kimi-k3 rubric; no grafts. A's close ("Your half downloads tonight") rhymed with yesterday's "so tonight pull" landing and its difference row paid for it.
- Hook: "You can already run Mistral tonight. Just not the six hundred seventy-five billion one." (named-contradiction, pick 2 of 10); A got "Three billion euros, and the open-weight pledge is already half true" (number-shock). Two patterns forced apart per finding 12.
- Fixes applied inside drafts before gates: A's "fits your gaming GPU" (not traceable to any brief claim) became "downloadable tonight"; A's dropped "on some benchmarks" qualifier restored; B's sixth spoken number (41B active) cut for the five-number classic cap.
- Gates: validator 0 blockers, 0 advisories both drafts; eval all hard gates pass both; soft advisories entity_spend (0.086/0.114 vs 0.5) and top2 (extractor wants "Large" and "Europe") kept on purpose: the scripts name the models viewers search (Small 4, Large 3, Ministral, Mistral) and "Europe"/"Large" as bare tokens are extractor artifacts, not entities a Short should spend. sameness clean vs last 5.

## Hook candidates
1. Three billion euros, and the open-weight pledge is already half true. (A, number-shock)
2. You can already run Mistral tonight. Just not the six hundred seventy-five billion one. * (B, named-contradiction)
3. Six hundred seventy-five billion parameters, and it still wants eight GPUs.
4. Europe's biggest round ever just bet on downloadable weights.
5. Mistral raised three billion euros. Your GPU cares about one number.
6. The pledge says open weights. Your gaming PC already has proof.
7. You run open models at home. Mistral just made that a business model.
8. One hundred nineteen billion parameters, and it runs tonight.
9. Samsung just led three billion euros into open weights.
10. Frontier AI was supposed to leave your desk behind. It didn't.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You can already run Mistral tonight. Just not the six hundred seventy-five billion one. | Run Mistral tonight. Not 675B. | Frame 1: two model cards side by side; on "run Mistral tonight" the Small 4 card scales in bright from 0.30 s; on "six hundred seventy-five billion" the Large 3 card fades in greyed out. | hyperframes | split-compare | 4.4 |
| s02 | foreshadow | You run open models on a gaming PC or Mac. Mistral just raised three billion euros promising open weights, published files you run yourself. | EUR 3B for open weights | On "gaming PC or Mac" a desktop tower and laptop fade in; on "three billion euros" the EUR 3B figure rises in place above them; on "published files" a download arrow lands on the machines. | hyperframes | giant-number | 7.5 |
| s03 | explain | Both are Apache two point oh, a license allowing free commercial use. | Apache 2.0, both models | Both model cards return; on "Apache two point oh" a license tag scales in, bridging the two cards to show one shared license. | hyperframes | split-compare | 3.8 |
| s04 | explain | Both are mixtures of experts, an office lighting only the rooms in use, though you own the building. Small four lights six and a half billion parameters per word. | MoE: lit rooms, owned building / Small 4: 6.5B per word | On "office lighting only the rooms in use" a floor-plan grid fades in with a few rooms lit; on "six and a half billion" the Small 4 label rises with 6.5B beside a mostly-dark Large 3 floor. | manim | diagram-flow | 8.1 |
| s05 | explain | Now the totals. Small four, one hundred nineteen billion parameters, runs on your box. The six hundred seventy-five billion one wants eight datacenter GPUs. | 119B: your box / 675B: 8 datacenter GPUs | On "one hundred nineteen billion" the Small 4 card settles onto the desktop tower and fits; on "eight datacenter GPUs" a server rack fades in beside Large 3, which stays off the desk. | hyperframes | split-compare | 7.5 |
| s06 | payoff_close | So the rule: fits your GPU, Small four. Needs a datacenter, Large three. | Fits your GPU: Small 4 | On "fits your GPU" the Small 4 card settles onto the desktop; the two-card frame rhymes with frame 1; final half second wordmark settle, no further motion. | hyperframes | centered-stack | 3.4 |

Value delivery: TEACHES -- s04's lit-rooms mechanism plus s05's totals let the viewer place any future Mistral model on their own box (judge row 8 gave this a 3). REFRAMES -- s02 reframes the EUR 3B raise from "funding news" into "a bet on the files you download"; the decision rule in s06 is the repeatable line.

## Notes for review
- "eight datacenter GPUs" is the breath-friendly form of the brief's verbatim "a single 8xA100 or 8xH100 node"; the storyboard's on-screen text keeps the verbatim node line in s04's screen field of draft A's table but B's s05 screen says "8 datacenter GPUs". If you want the verbatim hardware names on screen, s05's second beat is the place.
- The office analogy's limit ("though you own the building") compresses the brief's limit that disk and VRAM must hold every expert; it is spoken once, in s04.
- The 256k context length and the EUR 21B valuation were cut from B for time and the five-number cap; both live in the brief if a rescript wants them.
- No tokens-per-second claim anywhere: we have not measured Mistral models on our hardware.
