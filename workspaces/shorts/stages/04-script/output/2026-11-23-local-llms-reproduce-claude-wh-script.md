---
slug: 2026-11-23-local-llms-reproduce-claude-wh
format: smooth-explainer
structure: worked-example
style_pack: halftone
value_types: REFRAMES,TEACHES
promise: After forty seconds you can decide whether running Claude at home replaces your subscription, and name the exact trade: which Claude, what speed, what door.
target_duration_s: 104
brief: 2026-11-23-local-llms-reproduce-claude-wh-brief.md
drafts: 2026-11-23-local-llms-reproduce-claude-wh-drafts.md
---

# Local LLMs reproduce Claude: what the experiments show

## Decisions
- Structures: worked-example (draft A, 22/24) vs contrarian-take (draft B, 20/24). A won: factually clean against the brief, number budget spent on the viewer's tension, most repeatable payoff line. Judge noted B's honest beat drifted ("Not anywhere" asserts a universal absence the brief does not establish).
- Hook: pattern situation (candidate 2 family; final wording by writer A: "CLAUDE AT HOME, FREE?"). Picks were candidate 1 for A (situation) and candidate 10 for B (wrong-diagnosis), two different patterns per the divergence rule.
- Graft from B into A's verdict beat: "In another engineer's test, a leaderboard favorite did nothing while a plainer model finished." (row 8 + the honest beat; adds the independent-engineer evidence with no new numbers).
- Value delivery: REFRAMES lands on "So Claude at home is real, and it's a trade, not a replacement." TEACHES lands on the quantization beat ("storing the model's numbers with fewer bits") and the mixture-of-experts beat.

## Hook candidates
1. Claude at home, free? The receipts say slower
2. You want Claude at home. One man tested it.
3. Everyone says local AI matches Claude now
4. Local LLMs reproduced Claude. Almost.
5. Your subscription isn't the target. The claim is.
6. Sixty to eighty tokens a second. His box does thirty.
7. A secondhand graphics card reproduced Claude. Half of it.
8. He reproduced last year's Claude in his bedroom
9. The keyword in his verdict is almost
10. What got reproduced isn't what you think

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You pay for Claude every month. Then a post says you could run it at home for free. | CLAUDE AT HOME, FREE? | Frame 1: finished halftone composition, dark background, the headline CLAUDE AT HOME, FREE? set in large amber dotted letters with a dotted speech-bubble halo, all text 64px or tal | hyperframes | centered-stack | 6.2 |
| s02 | foreshadow | One developer actually tried it. His box is a home P C, two generations old, with a secondhand graphics card. It runs local models, A I stored as files on his own machine. | ONE DEVELOPER | HOME PC, SECONDHAND CARD | Hard cut to a dotted diagram. On 'One developer' a dotted avatar silhouette fades in at left. On 'home P C' a dotted PC tower scales in at center, joined to the avatar by a faint d | hyperframes | diagram-flow | 11.4 |
| s03 | explain | His test was one hard job he built himself: rebuild a research simulation as working code. On that job, the local models landed very close to Claude Sonnet. | ONE HARD JOB, HIS OWN | CLAUDE SONNET VS LOCAL | VERY SIMILAR OUTPUTS | On 'one hard job' two dotted panels rise side by side: left labeled CLAUDE SONNET, right labeled LOCAL, each filled with dotted code lines. On 'rebuild a research simulation' a sma | hyperframes | split-compare | 9.7 |
| s04 | explain | So what did he measure? Claude's app usually streams sixty to eighty tokens a second, tokens being the little chunks of words it writes. | CLAUDE'S APP | 60-80 TOKENS/SEC | Hard cut to a giant amber dotted number 60-80 with TOKENS/SEC beneath, fading in on 'sixty to eighty tokens a second', with a ding on the reveal. Static label CLAUDE'S APP above it | hyperframes | giant-number | 8.3 |
| s05 | explain | His big local models? Thirty tokens a second. He says he's happy to get it. That's just under half the speed of a subscription. | LOCAL BIG MODELS: 30 TOK/SEC | HALF THE SPEED | Two vertical dotted bars grow by scale from a shared baseline: a tall left bar labeled CLAUDE APP, no digits, and a short right bar labeled LOCAL with 30 at its top, popping in on  | hyperframes | split-compare | 8.3 |
| s06 | explain | So how does a giant model fit on a gaming card? Quantization, storing the model's numbers with fewer bits, shrinks the file until it fits in your card's memory. | QUANTIZATION | FEWER BITS, SMALLER FILE | On 'giant model' a big dotted file box labeled MODEL fades in above a dotted GPU outline it clearly cannot fit. On 'Quantization' the word scales in as a label at top. On 'fewer bi | hyperframes | diagram-flow | 10.0 |
| s07 | explain | The other trick is mixture of experts, waking only a few specialist parts per token. A huge model ends up running at small-model speed. | MIXTURE OF EXPERTS | FEW SPECIALISTS WAKE | A dotted grid of many small expert tiles fades in on 'mixture of experts', label static at top. On 'only a few specialist parts' a scattered few tiles light amber while the rest st | hyperframes | grid | 8.3 |
| s08 | explain | Now the verdict he wrote. His best local models edge past last year's Claude and almost tie today's Sonnet. The keyword, he writes, is almost. No blind test, no head-to-head benchmark, and no drop-in replacement for the top Claude. In another engineer's test, a leaderboard favorite did nothing while a plainer model finished. | EDGES LAST YEAR'S CLAUDE | ALMOST TIES SONNET | NO BLIND TEST | The hook's dotted headline returns, now punctured with holes, tick sound as the scene opens. On 'edge past last year's Claude' a stamp reading EDGES LAST YEAR'S CLAUDE fades in top | hyperframes | centered-stack | 18.3 |
| s09 | explain | Think of a local model as a cover band that has rehearsed your setlist. On the songs it knows, it sounds like the record. His simulation job was one of those songs. Shout a request it never learned, and it fumbles. | COVER BAND | KNOWS YOUR SETLIST | NEW REQUEST? FUMBLES | A dotted setlist grid of song cards fades in on 'cover band'. On 'rehearsed your setlist' amber checkmarks scale onto most cards. On 'sounds like the record' a dotted waveform puls | hyperframes | grid | 14.1 |
| s10 | payoff_close | So Claude at home is real, and it's a trade, not a replacement. Even the man who ran it still pays ten dollars a month for the original. | CLAUDE AT HOME: REAL | A TRADE, NOT A REPLACEMENT | HE STILL PAYS $10/MO | The frame-1 composition reassembles: same dotted headline style now reading CLAUDE AT HOME: REAL, fading in on 'Claude at home is real'. On 'a trade, not a replacement' that sublin | hyperframes | centered-stack | 9.7 |

## Notes for review
- The experimenter's hedge "almost" is kept verbatim where his verdict is spoken; do not sharpen it.
- Speed numbers rounded for the ear only inside the pair "sixty to eighty" vs "thirty"; the brief's verbatim strings are in the key-numbers table.
- The cover-band analogy states its limit on screen in its scene; check the clause survived the worker.
- The graft sentence carries the only second-experiment claim; it is tier-3 sourced (benchmark, medium confidence) and hedged ("another engineer's test").
