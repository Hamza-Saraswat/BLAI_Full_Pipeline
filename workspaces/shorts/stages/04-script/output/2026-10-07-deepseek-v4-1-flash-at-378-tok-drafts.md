---
slug: 2026-10-07-deepseek-v4-1-flash-at-378-tok
stage: 04-script
generated_at: 2026-10-07T12:21:52Z
winner: A (contrarian-take)
---

# Drafts and judge: DeepSeek v4.1 Flash at 378 tok/s: the cache-hit catch

## Draft A (contrarian-take, hook: named-contradiction) -- WINNER
| Scene | Role | Narration | On-screen |
|-------|------|-----------|------------|
| s01 | hook | Three hundred seventy-eight tokens a second, and that speed isn't your speed. You saw the headline for DeepSeek four point one Flash. | 378 output tokens per second | That speed isn't your speed. |
| s02 | explain | That number is RunInfra's, measuring the model alone, just the writing. Nearly every request it served was a repeat the model had already read. A cache hit is a prompt whose start matches notes already stored. | RunInfra, model only | nearly every request, a repeat |
| s03 | explain | One room, one brain, a desk for each conversation. That desk is the KV cache, the running notes of everything already read. Keeping notes for repeats is prefix caching. A hit finds your desk untouched. | room = the model | desk = the KV cache | hit: desk untouched |
| s04 | explain | But the desk takes memory, and it doesn't last. Memory pressure clears it. DeepSeek clears its disk cache nightly. Your first prompt is a cache miss. It owes full prefill, a complete read before the first word is written. | desk: not free, not forever | cleared nightly | miss = full prefill |
| s05 | explain | So what does your first prompt sit through? On DeepSeek's own API, a very long prompt took thirteen seconds to its first token. Warm, five hundred milliseconds. That gap is the cache. | first token, cold vs warm | from 13s to just 500ms |
| s06 | explain | Whose speed is it? The traffic's, not the model's. Same model, same hardware, different requests. RunInfra's best account was an agent that had already read a very long prompt. The model doesn't make the hits. Your prompts do. | hit rate = traffic, not model | your prompts make the hits |
| s07 | explain | Independent tests on DeepSeek's own API measured it slower. The number is real, and cache hits are how production agents run. Every new conversation repeats that first read. | independent check: slower | new chat = first read again |
| s08 | payoff_close | So measure the first prompt. That one is yours. | measure the first prompt | the speed is yours | Build Local AI |

## Draft B (worked-example, hook: situation)
| Scene | Role | Narration | On-screen |
|-------|------|-----------|------------|
| s01 | hook | Your first prompt arrives cold. You saw the headline: DeepSeek four point one Flash, writing faster than anything on your desk. Here is who that speed belongs to. | Your prompt arrives cold. |
| s02 | explain | Cold means the model has never seen a word of it. So it starts with prefill, reading your whole prompt once before the first word is written. A prompt this size is a long read. | cold prompt | prefill: read it all once |
| s03 | explain | On DeepSeek's API, a cold prompt this size waits thirteen seconds for its first token. That is the prefill bill, paid before anything gets written. | first token: 13s |
| s04 | explain | Prefill leaves something behind: a KV cache, the running notes the model keeps of everything it has already read. Picture one shared room, one brain, a desk for each conversation. | one room, one brain, your own desk |
| s05 | explain | The desk is not free. Those notes cost eight hundred ninety bytes per token, and they do not last. Retention is best-effort under memory pressure, and DeepSeek clears its disk cache nightly. | 890 bytes/token | cleared nightly |
| s06 | explain | Now your agent sends DeepSeek four point one Flash the same prompt again. Prefix caching keeps those notes so a repeated prompt skips re-reading. A cache hit: the beginning matches notes already stored. Your desk, exactly as you left it. | same beginning returns | notes still there |
| s07 | explain | This time the first token lands in five hundred milliseconds, down from thirteen seconds. Same model, same prompt. The only thing that changed is the notes. | 13s → 500ms |
| s08 | explain | This is where the headline lives. RunInfra measured three hundred seventy-eight tokens a second, the speed the model writes, model only. Nearly every request behind it was a repeat of one the model had already read. | 378 tok/s (model only) |
| s09 | foreshadow | The number is real, measured on real serving hardware. Agents that repeat long prompts all day live on hits like this. Your first prompt never gets one. Every new conversation pays the cold visit. | hits are real | your first prompt misses |
| s10 | payoff_close | So judge the model by the cold visit, not the repeat. The headline is not wrong. It is just not about your first prompt. | Judge the cold visit, | not the repeat. |

## Scores (judge, kimi-k3, 0-3 per row)

| Row | Draft A | Draft B |
|-----|---------|---------|
| 1 | 3 | 2 |
| 2 | 3 | 1 |
| 3 | 3 | 2 |
| 4 | 2 | 3 |
| 5 | 2 | 3 |
| 6 | 2 | 1 |
| 7 | 3 | 3 |
| 8 | 3 | 3 |
| total | 21 | 18 |

Winner: A, 21 to 18. Rows 2 and 6 decided it: A pays its hook by second 3 (378 plus 'isn't your speed' in one breath) while B teases 'cold' undefined past second 8 and holds the headline number until the final third, and A's contrarian-take is fresh against the last two shipped scripts while B re-runs the 10-01 worked-example at a near-identical duration. Row 1 widened the gap, since A's hook fuses number and felt tension where B's names only a product after an abstract tease.

Grafts: none.

What B would have needed: B needed a concrete anchor inside the first four to eight seconds, such as opening on the thirteen-second cold wait instead of an undefined 'arrives cold,' and a structure the channel had not shipped three episodes earlier. Its prefill-bill beat and airtight chronology were genuinely stronger, but a worked-example that saves the title's number for the final minute cannot beat a contrarian shape that spends the number up front and cashes it in the close.

Gate state at judging: A eval exit 0 (after cutting the fourth spoken number and the 24-hours on-screen remnant); B eval exit 0 (after tool enum fix, sfx shape fix, hook sentence to five words). Both passed variety_check.
