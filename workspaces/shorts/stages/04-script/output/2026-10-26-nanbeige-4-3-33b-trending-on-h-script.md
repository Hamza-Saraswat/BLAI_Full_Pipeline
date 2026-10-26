---
slug: 2026-10-26-nanbeige-4-3-33b-trending-on-h
format: classic
structure: worked-example
style_pack: signal
value_types: TEACHES,EQUIPS
promise: after thirty-five seconds you can say whether your box holds Nanbeige 4.3 at 4-bit and what context to cap
target_duration_s: 36
brief: 2026-10-26-nanbeige-4-3-33b-trending-on-h-brief.md
drafts: 2026-10-26-nanbeige-4-3-33b-trending-on-h-drafts.md
---

# Nanbeige 4.3 33B on a 24 GB card: the memory math

## Decisions
- Structures tried: number-first (draft A) vs worked-example (draft B). B won the judge tie 22-22 on the row-6 tiebreak: fresh situation opening and landing vs A's number-shock replaying the 10-23 script's rhythm. No grafts.
- Hook: "24 GB card vs 19 GB model" (candidate 7, situation pattern) -- the viewer's own card is the first frame; A's number-shock was candidate 1.
- Blind writers: two kimi-k3 calls per the seat map, private scratch dirs, pattern-forced divergence.

## Hook candidates
1. Nanbeige 4.3: 19 GB on disk
2. Nanbeige 4.3 woke up today
3. A 33B model, 19 GB on disk
4. Half a million tokens. One file.
5. Trending #2. Fits a 24 GB card.
6. One RAM bank decides this
7. 24 GB card vs 19 GB model *
8. You downloaded it. Now count.
9. Nanbeige 4.3, day two: 19 GB
10. The file is the story, not the bench

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | You've got a twenty-four gigabyte card. Nanbeige four point three is a nineteen-gigabyte file. | 24 GB card vs 19 GB model | Frame 1: dark background, giant text '24 GB card vs 19 GB model' top center, two empty vertical amber-outlined bars below, left labeled 'your card', right labeled 'the model'. Moti | manim | split-compare | 4.8 |
| s2 | explain | Step one: load the file onto your card. It downloads as a G G U F, the one file local models ship in. | Step 1: fit the file | GGUF: one file, whole model | Centered stack on dark: the line 'Step 1: fit the file' fades in on 'Step one'. A single amber document icon labeled 'GGUF' scales in center-frame on 'G G U F'. On 'the one file lo | hyperframes | centered-stack | 7.9 |
| s3 | foreshadow | The model also promises half a million tokens of context. Each token rents working memory, a cache that piles beside the weights. | context: 524,288 tokens | cache grows per token | A horizontal amber timeline labeled 'context' stretches rightward on 'half a million tokens of context', tick marks multiplying toward an end label reading '524,288'. On 'rents wor | manim | timeline | 7.6 |
| s4 | explain | Step two: cap the context window before loading. Your leftovers hold roughly eight to sixteen thousand tokens. Bartowski's build loads in LM Studio tonight. | Step 2: cap the context | room left: 8K-16K tokens | On 'cap the context window' an amber slider fades in and its handle pins near the low end of a track. Giant amber text '8K-16K' scales in center on 'eight to sixteen thousand token | hyperframes | giant-number | 8.3 |
| s5 | payoff_close | A hundred and twenty-eight gigabytes buys the long conversations. Your card still runs it, and trending never got a vote. | 128 GB: long conversations | your card still runs it | Rhymes with frame 1: the same two-bar split-compare composition from the hook returns, card bar left, model bar nested inside it. On 'hundred and twenty-eight gigabytes' a much tal | manim | split-compare | 6.9 |

## Notes for review
- Rounded for the ear: 19.36 GiB to "nineteen-gigabyte file"; 524,288 tokens to "half a million tokens" (screen shows 524,288 in the same scene); 8K-16K to "roughly eight to sixteen thousand tokens".
- The 24 GB fit and the 8K-16K window come from webdiga's config math (medium confidence): hedged as "roughly", no speed or quality claims anywhere.
- "Wants nineteen of them" rewritten to "is a nineteen-gigabyte file" so the number_spend gate hears the unit with its referent.
- Single wry beat: "Each token rents working memory" (scene 3), aimed at the cache, not the viewer.
