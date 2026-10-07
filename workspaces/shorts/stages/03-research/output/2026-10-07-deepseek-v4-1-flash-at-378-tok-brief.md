---
slug: 2026-10-07-deepseek-v4-1-flash-at-378-tok
stage: 03-research
topic: "DeepSeek V4.1 Flash at 378 tok/s: the cache-hit catch"
depth: standard
generated_at: 2026-10-07T11:48:00Z
sources: 12
hub: "[[videos/2026-10-07-deepseek-v4-1-flash-at-378-tok]]"
---

# Research brief: DeepSeek V4.1 Flash at 378 tok/s: the cache-hit catch

## Summary
Thesis: 378 tok/s is what DeepSeek V4.1 Flash does for a warmed-up agent that already paid to read its prompt once, not what a cold first prompt sees. Most arresting number: on DeepSeek's own API, the same 128K prompt waits 13s for its first token cold and 500ms when the cache hits. Strongest concrete case: the 99.7% cache hit rate behind the headline is the single best qualifying account on RunInfra, an agent running sessions of five or more turns with at least 10 million billed input tokens. Could not verify: what a fully cold prompt measures on RunInfra's own stack (not published), and whether any community quant of this 552B model runs on 128 GB. Conflict: RunInfra's homepage said 99.3% cache hit while its model page said 99.7% for the same last-24-hours window on the same day.

## Thesis
378 tok/s is what DeepSeek V4.1 Flash does for an agent that already paid to read its prompt once; your first, cold prompt pays the prefill bill in seconds and cents, and only the repeats after it get the headline speed.

## Explanation path
The viewer must hold what a cache hit is before any speed number can be judged: a model that has read text once saves the reading work, and a request whose opening exactly matches saved work skips it, so the speed a repeat enjoys is speed the first request had to earn. With that in place the fine print becomes the story: the 99.7% figure is the cached share of the single best qualifying account on RunInfra's heaviest agent traffic, and the 378 figure is model-only, measured before the gateway, on a stack built to keep sessions warm. DeepSeek's own documents price the cold path in seconds and money, the wait for a first token on a long prompt and the split between cold and warmed input pricing, which turns the gap from jargon into a bill. The same model measured independently on DeepSeek's first-party API, and measured single-stream on a DGX Station, shows what one ordinary conversation actually gets. The viewer leaves able to ask of any tok/s headline: warmed or cold, and model-only or end to end.

## Claims
1. **RunInfra's page for DeepSeek V4.1 Flash reports an output speed of 378 output tokens per second, model only, with a cache hit rate of 99.7% last 24 hours.**
   - Source: DeepSeek V4.1 Flash API pricing and speed | RunInfra, https://runinfra.ai/inference-api/deepseek-v4-1-flash
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "378 output tokens per second, model only" ... "99.7% last 24 hours"
2. **The 378 figure carries a qualifier most readers skip: it is model-only and measured before the gateway, wording RunInfra prints on its own homepage next to the same number.**
   - Source: Open models, built for agents | RunInfra, https://runinfra.ai/
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "378 output tok/s, model only, before the gateway"
3. **The 99.7% cache hit rate is the highest qualifying account's cached-input share on paid settled traffic, agent sessions of five or more turns with at least 10 million billed input tokens per account, and RunInfra states the published figure is not a typical rate or a guarantee.**
   - Source: Measurement methodology | RunInfra, https://runinfra.ai/methodology
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "Cache hit rate is the highest qualifying account's cached-input share on paid settled traffic: agent sessions of five or more turns, at least 10 million billed input tokens per account, excluding the SDK canary." ... "the published figure is not a typical rate or a guarantee."
4. **A cache hit requires exact prefix reuse: DeepSeek's caching guide states a subsequent request can only hit the cache if it fully matches a cache prefix unit, and that the system is best-effort and does not guarantee a 100% cache hit rate.**
   - Source: Context Caching | DeepSeek API Docs, https://api-docs.deepseek.com/guides/kv_cache/
   - Tier: primary | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "A subsequent request can only hit the cache if it fully matches a cache prefix unit." ... "The cache system works on a \"best-effort\" basis and does not guarantee a 100% cache hit rate."
5. **Cold prompts pay in waiting: for a 128K prompt with high reference, DeepSeek reports first token latency cut from 13s to just 500ms when the cache hits, which makes the cold read the 13s case.**
   - Source: DeepSeek API introduces Context Caching on Disk, cutting prices by an order of magnitude, https://api-docs.deepseek.com/news/news0802/
   - Tier: primary | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "For a 128K prompt with high reference, the first token latency is cut from 13s to just 500ms."
6. **Cold prompts also pay full input price: DeepSeek's list price is $0.15 per 1M input tokens on a cache miss versus $0.003 on a cache hit, off-peak.**
   - Source: Models & Pricing | DeepSeek API Docs, https://api-docs.deepseek.com/quick_start/pricing
   - Tier: primary | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "1M INPUT TOKENS (CACHE HIT) | OFF-PEAK | $0.003 ... 1M INPUT TOKENS (CACHE MISS) | OFF-PEAK | $0.15"
7. **Independent measurement puts the same model far below the headline: Artificial Analysis measures DeepSeek V4.1 Flash (Max) at 226.6 tokens per second based on DeepSeek's API, well above a 75.0 t/s median for similar open-weight models.**
   - Source: DeepSeek V4.1 Flash (max) - Intelligence, Performance & Price Analysis | Artificial Analysis, https://artificialanalysis.ai/models/deepseek-v4-1-flash
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "DeepSeek V4.1 Flash (Max) generates output at 226.6 tokens per second (based on DeepSeek's API), which is well above average compared to other open weight models of similar size (median: 75.0 t/s)."
8. **DeepSeek V4.1 Flash is a multimodal MoE with 552B backbone parameters that activates only 8B parameters per token during prefill and 16B during decode, and compresses its global KV cache to 890 bytes per token.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash - Hugging Face, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "the model to activate only 8B parameters per token during prefill and 16B during decode" ... "reduce the global KV cache footprint to 890 bytes per token"
9. **On a DGX Station with one GB300 GPU, vLLM's verified recipe measures 90.5 aggregate tok/s for a single stream and reaches 378 only across twelve concurrent streams.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash | vLLM Recipes, https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: docs | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "aggregate tok/s, prose | 90.5 | 124 | 168 | 302 | 378 | 416–423"
10. **The number went public on Hacker News on 2026-10-07 under the title DeepSeek v4.1 Flash at 378 tok/s 99.7% Cache hit rate, two points and no comments at fetch time.**
   - Source: DeepSeek v4.1 Flash at 378 tok/s 99.7% Cache hit rate | Hacker News, https://news.ycombinator.com/item?id=49989109
   - Tier: community | Confidence: high | Accessed: 2026-10-07 | Via: web_extract
   - Quote: "DeepSeek v4.1 Flash at 378 tok/s 99.7% Cache hit rate"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | headline output speed (RunInfra, model only) | 378 output tokens per second | https://runinfra.ai/inference-api/deepseek-v4-1-flash | "378 output tokens per second, model only" |
| 2 | cache hit rate behind the headline | 99.7% last 24 hours | https://runinfra.ai/inference-api/deepseek-v4-1-flash | "99.7% last 24 hours" |
| 3 | floor to qualify for that rate, per account | at least 10 million billed input tokens | https://runinfra.ai/methodology | "agent sessions of five or more turns, at least 10 million billed input tokens per account" |
| 4 | first token on a 128K prompt, cold to warmed | from 13s to just 500ms | https://api-docs.deepseek.com/news/news0802/ | "the first token latency is cut from 13s to just 500ms" |
| 5 | input price, miss vs hit (DeepSeek list, off-peak) | $0.15 (miss) vs $0.003 (hit) per 1M input tokens | https://api-docs.deepseek.com/quick_start/pricing | "1M INPUT TOKENS (CACHE HIT) | OFF-PEAK | $0.003" |
| 6 | independent output speed (DeepSeek API) | 226.6 tokens per second | https://artificialanalysis.ai/models/deepseek-v4-1-flash | "generates output at 226.6 tokens per second (based on DeepSeek's API)" |
| 7 | one stream on DGX Station GB300 | 90.5 aggregate tok/s, prose | https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash | "aggregate tok/s, prose | 90.5 | 124 | 168 | 302 | 378 | 416–423" |
| 8 | global KV cache footprint | 890 bytes per token | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "reduce the global KV cache footprint to 890 bytes per token" |

The hook pair is 1 plus 2; the payoff number is 4, the same prompt's first token at 13s cold and 500ms warmed.

## Analogy candidates
- **Vehicle**: a kitchen where the prep cook has already chopped everything. Mapping: the cache hit is cooking from mise en place, the cache miss is chopping every vegetable from scratch, and the tok/s figure is plates per minute once the pan is hot. Breaks when: the cache speeds up the reading of your prompt and cuts the input bill, not the writing itself; the writing hand is the same either way.
- **Vehicle**: rereading a long document with your highlights in hand. Mapping: the prefix is the part you already highlighted, the hit is skimming those highlights instead of rereading, the miss is the full first read. Breaks when: nothing carries over between two different conversations; only an identical opening counts, and the highlights get thrown out after hours to days.

## Misconceptions
- Myth: 378 tok/s is the speed you get when you call DeepSeek V4.1 Flash. Reality: it is RunInfra's model-only figure behind a 99.7% cache hit rate, and independent measurement on DeepSeek's own API is 226.6 tokens per second (claims 1, 2, 7).
- Myth: a high cache hit rate is a property of the model. Reality: it is a property of the traffic; only requests that fully match a stored prefix hit, and DeepSeek says the system does not guarantee a 100% cache hit rate (claim 4).
- Myth: once the cache is warm it stays warm. Reality: RunInfra holds prefixes on the serving GPU with best-effort retention under memory pressure, and DeepSeek clears unused entries, usually within a few hours to a few days (claim 4's sources).

## Glossary
- **token**: the smallest chunk of text a model reads or writes, roughly a word or a piece of one.
- **tokens per second (tok/s)**: how fast a model produces new tokens once it has started writing.
- **prefill**: the phase where the model reads your whole prompt before it can write the first token.
- **time to first token (TTFT)**: how long you wait between sending a prompt and seeing the first word.
- **KV cache**: the saved intermediate results of a model reading text, kept so the same text never has to be fully re-read.
- **cache hit / cache miss**: a request whose opening exactly matches something already stored is a hit, cheap and fast; anything else is a miss and pays full price.
- **prefix**: the start of your prompt, matched from the very first token; partial matches in the middle do not count.
- **model-only vs end-to-end**: speed measured at the model itself versus speed measured at your client, gateway and network included.
- **aggregate tok/s**: the combined speed of all concurrent conversations on one server, not the speed of one conversation.
- **mixture of experts (MoE)**: a model architecture that keeps many specialist blocks and activates only a few per token.

## Unverified
- What a fully cold prompt measures in tok/s on RunInfra's own stack is not published anywhere fetched this run; the page reports one output speed and a hit rate, never a cold-path speed.
- Whether any community quantization of the 552B DeepSeek V4.1 Flash fits and runs on a 128 GB DGX Spark was not verified; the native checkpoint is roughly 511 GB on disk per vLLM's recipe.
- The radar's second lead, a fast single-box DeepSeek v4.1 Flash runtime at tangled.org, could not be located in this run's searches; nothing about it is cited.
- RunInfra's homepage showed 99.3% cache hit for the same last-24-hours window its model page reported as 99.7%; hourly revalidation per its methodology likely explains the drift, but that is our reading, not a confirmed explanation.

## Suggested outline
1. Hook: the headline says DeepSeek v4.1 Flash at 378 tok/s, and the fine print under it says 99.7% cache hit rate.
2. What a cache hit is: the model saves the work of reading text, and only a request whose opening exactly matches saved work skips it; a first, cold prompt can never hit.
3. The receipt: 99.7% is the best qualifying account on RunInfra, sessions of five or more turns and at least 10 million billed input tokens, a figure the site itself says is not a typical rate or a guarantee.
4. What cold costs: on DeepSeek's own API a 128K prompt's first token takes 13s cold versus 500ms warmed, and cold input lists at $0.15 per 1M tokens versus $0.003 warmed; measured independently, the model does 226.6 tok/s.
5. The local mirror and the landing: one stream on a DGX Station GB300 is 90.5 tok/s, with 378 only across twelve streams at once; cache speed is earned by repetition, and the first prompt always pays full price.

## Viewer situation
You saw a Hacker News headline saying DeepSeek v4.1 Flash runs at 378 tok/s and you want to know whether the model you would call or run is actually that fast.

## Has process
false

## Objection
The number is still real: a measured 378 on real serving hardware, and cache hits are simply how production agents run, so the headline is not wrong, it is just not about your first prompt.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://runinfra.ai/inference-api/deepseek-v4-1-flash | DeepSeek V4.1 Flash API pricing and speed \| RunInfra | benchmark | web_extract | 2026-10-07 |
| 2 | https://runinfra.ai/ | Open models, built for agents \| RunInfra | benchmark | web_extract | 2026-10-07 |
| 3 | https://runinfra.ai/methodology | Measurement methodology \| RunInfra | benchmark | web_extract | 2026-10-07 |
| 4 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash \| Hugging Face | primary | web_extract | 2026-10-07 |
| 5 | https://api-docs.deepseek.com/guides/kv_cache/ | Context Caching \| DeepSeek API Docs | primary | web_extract | 2026-10-07 |
| 6 | https://api-docs.deepseek.com/news/news0802/ | DeepSeek API introduces Context Caching on Disk \| DeepSeek API Docs | primary | web_extract | 2026-10-07 |
| 7 | https://api-docs.deepseek.com/quick_start/pricing | Models & Pricing \| DeepSeek API Docs | primary | web_extract | 2026-10-07 |
| 8 | https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash \| vLLM Recipes | docs | web_extract | 2026-10-07 |
| 9 | https://artificialanalysis.ai/models/deepseek-v4-1-flash | DeepSeek V4.1 Flash (max) \| Artificial Analysis | benchmark | web_extract | 2026-10-07 |
| 10 | https://news.ycombinator.com/item?id=49989109 | DeepSeek v4.1 Flash at 378 tok/s 99.7% Cache hit rate \| Hacker News | community | web_extract | 2026-10-07 |
| 11 | https://hn.algolia.com/api/v1/search?query=runinfra%20deepseek&tags=story | HN Algolia search: runinfra deepseek | community | web_extract | 2026-10-07 |
| 12 | https://www.mindstudio.ai/blog/deepseek-v4-1-flash-local | How to Run DeepSeek V4.1 Flash Locally \| MindStudio | docs | web_extract | 2026-10-07 |

## Notes
Source conflict: RunInfra's homepage said "99.3% cache hit, last 24 hours" while its model page said "99.7% last 24 hours", both fetched on 2026-10-07; quote the model page and HN title (99.7%) since that is the headline being busted, and expect the live figure to move.
The vLLM DGX Station table's 378 aggregate tok/s at twelve streams is numerically identical to RunInfra's 378 by coincidence; if the writer uses it, say plainly it is a different measurement, twelve conversations on one box rather than one conversation in one cloud.
Tiering: RunInfra measures its own serving with a published method, so its pages are tier 3 benchmark here even though they are vendor pages; DeepSeek docs and the model card are tier 1.
Artificial Analysis measures 226.6 tok/s on DeepSeek's first-party API, not on RunInfra; it bounds the model's publicly measured single-conversation speed, not RunInfra's stack.
