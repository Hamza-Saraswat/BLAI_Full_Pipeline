---
slug: 2026-10-30-mistral-4-beats-chinese-models
format: classic
structure: news-react-so-what
style_pack: halftone
value_types: TEACHES,REFRAMES
promise: After 38 seconds you can check any "beats the Chinese models" claim yourself: open the model card, ask which benchmark, which model, whose measurement.
target_duration_s: 38
brief: 2026-10-30-mistral-4-beats-chinese-models-brief.md
drafts: 2026-10-30-mistral-4-beats-chinese-models-drafts.md
---

# Mistral 4 beats Chinese models: run the receipt

## Decisions

- Structures tried: comparison-ladder (A) vs news-react-so-what (B). B wins 20-15 (Kimi K3 judge, rubric rows below in the drafts note). Rotation ruled out myth-bust and contrarian-take (last two shipped) and the number-shock hook (yesterday); first attempt at number-first + myth-bust was re-assigned before drafting for exactly that reason.
- Hook: "The Mistral headline isn't the receipt. The card is." (named-contradiction, candidate 2 of 10; frame-1 text "The Mistral headline isn't the receipt"). Judge scored both hooks 3; B won on payoff timing (first score at ~3 s) and voice.
- Graft: A's coding line into B's s04, replacing "the open-weight leader" with the brief's named model: "The card, the page beside the weights, prints forty-eight percent on coding: tied with GLM five point three."
- Gates: validator 0 blockers / 0 advisories; eval gate1_ready true (number_spend 4/4 heard, 2-5 band; hook_concrete via Mistral; scene_specificity 7/7 after fixes; skeleton 0.0; positional labels 0; sameness clean vs last 5); normalizer 1 scene changed; variety recorded; style pack halftone (topic fit; previous signal).

## Hook candidates

1. Mistral or the Chinese models? The card decides. (decision, 6) -- draft A's pick
2. The headline isn't the receipt. The card is. (named-contradiction, 5) * PICK
3. Two hundred thirty-three gigabytes. Smallest file they ship. (number-shock, 6) -- banned today (10-29)
4. Mistral claims the win. The card prints a tie. (named-contradiction, 5)
5. Beats the Chinese models. Which benchmark? (decision, 5)
6. Mistral Large 4 landed open. Your PC is out. (situation, 5)
7. Forty-eight percent coding. Tied with China's best. (number-shock, 5) -- banned today
8. A French model "beats" China. Read the receipt. (named-contradiction, 4)
9. You saw the headline. The card disagrees. (situation, 5)
10. One claim, three scores, zero benchmarks named. (number-shock, 4)

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | The Mistral headline isn't the receipt. The card is. | headline ≠ receipt · the card is | Frame 1: finished composition, glossy headline strip; on "The Mistral headline isn't the receipt" it fades to half brightness; on "The card is" a plain paper model card rises-in-place beside it. Onset after 0.30s, two elements max. | hyperframes | centered-stack | 3.1 |
| s02 | explain | Twenty-six on the index, one blended score of benchmarks; your gaming PC or Mac saw the headline. Chinese leaders score higher. | 26 on the index · Chinese leaders higher | On "Twenty-six" a giant "26" scales in; on "your gaming PC or Mac saw the headline" the small headline strip fades behind the digit; on "Chinese leaders score higher" a second row rises-in-place above it. Digit upper-center, out of right 120 px. | hyperframes | giant-number | 7.2 |
| s03 | explain | Mistral Large four landed yesterday: open weights, the downloadable numbers a model is made of. The claim named no models or benchmarks. | Mistral Large 4 · no models named · no benchmarks | On "landed yesterday" a date node rises-in-place on a short line; on "open weights" a file sheet fades in at the node; on "named no models or benchmarks" two empty outline chips fade in, unfilled. Never more than two moving. | hyperframes | timeline | 7.6 |
| s04 | explain | The card, the page beside the weights, prints forty-eight percent on coding: tied with GLM five point three. Cyber index: fifty-one percent, ahead. | coding 48% tied \| cyber 51% ahead | Split panel: on "forty-eight percent" the coding bar draws to its mark, "tied" tag fades in; on "fifty-one percent" the cyber bar draws past a faint rival line, "ahead" tag fades in. Bars above bottom 450 px. | hyperframes | split-compare | 7.9 |
| s05 | explain | The catch: the Artificial Analysis index is somebody's chosen bucket; trading it for one win cherry-picks back. | one index = somebody's chosen bucket | On "somebody's chosen bucket" benchmark chips fade down into a bucket outline; on "cherry-picks back" a single chip rises-in-place out of the bucket and holds. Two motions max. | hyperframes | diagram-flow | 5.9 |
| s06 | explain | Smallest quant, the tightest squeeze, two hundred thirty-three gigabytes of weights; your gaming PC can't hold it. | smallest file: 233 GB | On "two hundred thirty-three gigabytes" huge digits scale in, centered high, clear of safe zones; on "can't hold it" a small PC tower outline fades in beneath and dims, dwarfed. | hyperframes | giant-number | 5.9 |
| s07 | payoff_close | Tonight, open the card before the headline: which benchmark, which model, whose measurement? | which benchmark · which model · whose measurement | Rhyme with frame 1: on "open the card" the same paper card rises-in-place at center; on the triplet three short check lines rise one by one beneath it. Ends on the card. | hyperframes | centered-stack | 4.5 |

## Notes for review

- Numbers are the model card's own (vendor-cited Artificial Analysis harnesses; the independent AA page confirms the 26). No local tokens/s exists yet: any speed line must stay hedged.
- 233 GB is the unsloth 1-bit quant size; "can't hold it" covers 24 GB GPUs and 128 GB Macs, not 256 GB boxes.
- The spoken "Mistral Large four" is the product name; "four" inside it is not a stat (normalizer keeps it).
- Value lines: TEACHES = "Tonight, open the card before the headline: which benchmark, which model, whose measurement?" REFRAMES = "The Mistral headline isn't the receipt. The card is."
- Wry beat: "trading it for one win cherry-picks back" (s05), on the benchmark game, not the viewer.
