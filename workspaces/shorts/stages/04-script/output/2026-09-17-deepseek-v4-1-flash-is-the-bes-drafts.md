---
slug: 2026-09-17-deepseek-v4-1-flash-is-the-bes
stage: 04-script
generated: 2026-09-17
---

# Drafts: 2026-09-17-deepseek-v4-1-flash-is-the-bes

Both drafts written blind on Kimi K3 from the same brief and voice law; judged blind on Kimi K3 per judge-rubric.md.

## Draft A (myth-bust, hook: number-shock) -- WITHDRAWN
- Hook: $4.65 bought 11 hacks
- Title: The $4.65 Hacking Crown Is Real. The Receipt Tells the Rest.
- Target: 106s; 309 words; 9 scenes
- Withdrawn for rotation: 2026-09-16 shipped myth-bust and the rule bars the last two structures. Two rewrite "
 "attempts toward news-react-so-what returned myth-bust-shaped boards; per the two-rounds rule the draft was "
 "withdrawn and the judge's completed run (below) kept as the record. Kept as written; the judge also found it over "
 "the three-number cap (four key numbers in narration).

| Scene | Narration | On-screen | Est s |
|-------|-----------|-----------|-------|
| s1 (hook) | Four dollars and sixty-five cents bought eleven hacks. You saw the headline. You have a gaming PC or a Mac, and you are wondering if tonight's download is the winner. | $4.65 bought 11 hacks | 10.0 |
| s2 (foreshadow) | The belief makes sense. A benchmark crowned this model, so the download must be the thing that won. That is the myth, and it is a fair one. | The download must be the winner | 9.7 |
| s3 (explain) | Now read the receipt. The benchmark kept re-sending the same source code. Two hundred sixty-six point two million of the two hundred sixty-eight point three million input tokens were cache hits. | same code, sent again | cache hit | 11.4 |
| s4 (explain) | A cache hit is input the provider already processed once, then bills cheaper when it comes back. That group rate is the four-dollar price. Your machine pays the same reuse in memory instead. | Provider: group rate | You: memory + seconds | 11.4 |
| s5 (explain) | The design underneath made that price possible. It is a mixture of experts, a model that wakes only a slice of itself for each word. Quick per word, but all of it still must fit in memory. | mixture of experts | a slice wakes per word | 12.8 |
| s6 (explain) | The reading notes get the same treatment. The KV cache, the running memory that lets it re-read earlier work, shrinks to eight hundred ninety bytes per token. Notes that small are why an agent can re-read a codebase for hours. | KV cache: 890 B / token | 13.4 |
| s7 (explain) | The brain itself does transfer. The weights carry an MIT license, the permissive kind, so nothing about the model is hidden. The same file the benchmark scored is yours tonight. | MIT license | same weights, yours tonight | 10.3 |
| s8 (explain) | What stays behind is the kitchen. The closest public proof of life is one reviewer's rig: four DGX Spark desktops sharing one model. Its extra memory tables park on disk. One gaming card cannot hold it at all. And you never pay per token here, only in memory and seconds. | 4x DGX Spark + disk | one GPU: no | 17.2 |
| s9 (payoff_close) | Where the myth still holds: the weights. Your download is the same brain the leaderboard crowned. What won, though, was that brain riding someone else's cache. Same model, different receipt. | Same model. Different receipt. | 10.3 |

## Draft B (contrarian-take, hook: wrong-diagnosis) -- WINNER
- Hook: You crowned the wrong winner
- Title: DeepSeek V4.1 Flash: the Hacking Crown Your Download Doesn't Get
- Target: 107s; 308 words; 7 scenes
- As written, before the graft and the gate-fix pass (the shipped version splits its long scenes and swaps the closer).

| Scene | Narration | On-screen | Est s |
|-------|-----------|-----------|-------|
| s1 (hook) | You're crowning the wrong winner. You've got a gaming PC, and you saw the headline. An open-weights model swept a hacking benchmark. | You crowned the wrong winner | 7.9 |
| s2 (explain) | The win is real. The benchmark hands an agent a low-privilege account and one shell. A run only counts when the target executes a command and returns fresh proof. DeepSeek's V four point one Flash hacked every vulnerable target. Every patched one held. The whole sweep cost four dollars and sixty-five cents. The leaderboard itself warns it is not a general model ranking. | DeepSeek V4.1 Flash | every target hacked | $4.65 total | 21.7 |
| s3 (explain) | Now read the receipt. Two hundred sixty-six million of the two hundred sixty-eight million input tokens were cache hits. A cache hit is input the provider already processed once, re-billed cheaper. That discount is a serving-stack trick. The weights play no part in it. | 266.2M of 268.3M tokens cached | re-billed cheaper | 15.2 |
| s4 (explain) | The model is a mixture of experts, a company of specialists with a receptionist who wakes only the few each word needs. Speed comes from the few that wake. Memory comes from the whole company, because any specialist could be next. The receptionist re-picks for every word, so picture hundreds of small wake-ups per sentence. | many experts on staff | a few wake per word | 19.3 |
| s5 (explain) | The closest public local run is four DGX Spark boxes wired as one, the model split across them. Peak speed: seventy-seven point two tokens per second. One consumer GPU cannot shelve the full weight set at all. The extra memory tables sit on disk, exiled, just to make room. Locally the currencies are memory and tokens per second. | 4x DGX Spark, wired as one | 1 GPU cannot shelve it | 20.0 |
| s6 (explain) | The weights are yours under an M I T license, free to download tonight, free to use commercially. The brain in that benchmark is the same brain you would get. The building around it stays behind: the caching, the serving stack, the discount. | MIT license, same brain | the stack stays home | 14.8 |
| s7 (payoff_close) | The honest claim is smaller than the headline. The benchmark crowned a model plus its serving stack. Your download comes with the model. | model + serving stack | your download: the model | 7.9 |

## Score table (completed blind judge run)
| Row | A (myth-bust) | B (contrarian-take) |
|-----|----|----|
| Hook | 3 | 1 |
| Payoff timing | 3 | 1 |
| Specificity | 1 | 3 |
| Voice | 3 | 3 |
| Navigation | 3 | 3 |
| Difference | 0 | 0 |
| Repeat test | 2 | 2 |
| Teaching | 2 | 3 |
| **Total** | **17** | **16** |

Winner: B by 1 (19-17).
Graft: Insert B's sentence 'The leaderboard itself warns it is not a general model ranking.' at the end of A's s2 narration, just before 'Now read the receipt.' Why: The brief's honesty caveat is only folded into A's myth framing, while B speaks it outright; the line adds no numbers, stays in person, slots in at a scene boundary without rewriting any surrounding beat, and it narrows the crown's scope without pre-empting the receipt break that s3 delivers. No hook graft (B's hook scored lower) and no second sentence: B's 77.2 tok/s line would break A's number budget, and B's receptionist sentences would force a rewrite of A's library-based MoE beat.
Hook graft declined (A's hook scored 3 vs B's 1, eligible): it would have added a fourth key number to B and forced rewrites of B's opening beats.

## Numbers check (judge)
- A: $4.65 - spoken ('four dollars and sixty-five cents') and on screen in s1; 11 targets - spoken ('eleven hacks') and on screen in s1; rides in on the fixed hook outside the desk's three-number spend; 268.3M input tokens - spoken only ('two hundred sixty-eight point three million'), kept off every screen per s3 render notes; 266.2M cache hits - spoken only ('two hundred sixty-six point two million'), kept off every screen; this pair is the draft's one spoken-only number; 890 bytes per token - spoken ('eight hundred ninety bytes') and on screen in s6; four DGX Spark boxes - spoken ('four') and shown as '4x' in s7; treated by the desk as the rig's name, but strictly a sixth key number, so A runs well past the <=3 budget
- B: $4.65 - spoken and on screen in s2; 266.2M of 268.3M cache hits - on screen in s3; spoken rounded as 'two hundred sixty-six million of the two hundred sixty-eight million'; 77.2 tok/s - spoken only ('seventy-seven point two'), absent from all on_screen_text; the draft's one spoken-only number; four DGX Spark boxes - spoken ('four') and shown as '4x' in s5; strictly a fourth key number, so B is also past the <=3 budget, though lighter than A

## Drift check (judge)
A: none found. B: none.

## What the loser needed
The contrarian-take needed to pay its take inside the first eight seconds: open on the receipt (nearly every input token a cache hit) and compress the win to one concession line, instead of spending a twenty-two-second second scene re-telling a headline its own hook says the viewer already saw. It also needed a hook that names a number or a product with the tension built in (its own candidate list had 'Four dollars and sixty-five cents bought eleven hacks'), because 'You're crowning the wrong winner' names neither and repeats the previous shipped script's hook head, structure, closing move and runtime almost exactly.

## Run log (provider incidents, for the retro)
- Writer A first pass completed cleanly; judge run one hit a moonshot read timeout (900s) and its retry completed.
- Writer A rewrites hit HTTP 520 twice; one retry completed but kept the myth-bust shape; the seat was retired after
  two rounds rather than spent again.
