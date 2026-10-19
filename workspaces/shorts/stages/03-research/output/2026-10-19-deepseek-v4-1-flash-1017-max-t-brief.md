---
slug: 2026-10-19-deepseek-v4-1-flash-1017-max-t
stage: 03-research
topic: "DeepSeek V4.1 Flash 1017 (Max): what the index result really is, and which machine runs the weights"
depth: standard
generated_at: 2026-10-19T11:50:00Z
sources: 12
hub: "[[videos/2026-10-19-deepseek-v4-1-flash-1017-max-t]]"
---

# Research brief: DeepSeek V4.1 Flash 1017 (Max) -- the index result, the weights, the machine

## Summary
The drop is real but the headline needs a correction: 1017 (Max) scores 45 on the Artificial Analysis Intelligence Index, #2 of 121 in its open-weight class (the September predecessor scored 39), while closed models led by Claude Opus 5.5 still sit above it overall. The concrete case: MIT weights shipped on Hugging Face the same day (2026-10-17), and a community quant converter already published a roughly 106 GiB build explicitly sized for one 128 GB DGX Spark. Could not verify: first-party speed on our own Spark, the exact official checkpoint size (a community page says 510 GB), and any stock-llama.cpp GGUF. Conflict: The Decoder relays vendor benchmarks ("beats larger models", DeepSWE 77.0 percent at under $0.20 per task) while AA measures output speed slightly down (227.1 vs 231.2 tokens per second) and the independent Terminal-Bench 4.0 board is still led by Claude Sonnet 5.5 at 63.6%.

## Thesis
DeepSeek's Flash 1017 is the first front-page drop that is both a top-of-class open-weight reasoning model and a same-day local download, but at 552B backbone parameters plus an Engram memory the machine that runs it is a 128 GB unified-memory box, not a gaming card.

## Explanation path
Establish what the name is before any scoreboard: 1017 is an upgrade of the existing V4.1 Flash, shipped 2026-10-17, same weights family, and "Max" is the top of a reasoning-effort dial on one set of weights, not a second model. With that anchor, the index result lands honestly: 45 on the Artificial Analysis Intelligence Index, second of 121 among open-weight large reasoning models, six points over its predecessor, with closed models still above it overall. Then the size reality, because "Flash" misleads: the architecture is a 552B-parameter backbone with a 196B-parameter Engram lookup memory, activating only 16B parameters per token during decode, which is why it is cheap on the API (about $0.26 per index task) yet heavy on disk. The payoff is the local question already answered: weights are MIT and downloadable today, a community quant is sized for exactly one 128 GB DGX Spark, the llama.cpp route still needs two 96 GB cards plus host RAM and an unmerged PR, and a single 24 GB GeForce is not in this model's future at any quant. What a gaming-card viewer takes away is the API price and the knowledge of which machine class to watch.

## Claims
1. **DeepSeek shipped V4.1-Flash-1017 on 2026-10-17 as an upgrade of V4.1 Flash, live on web, app and API the same day.**
   - Source: DeepSeek-V4.1-Flash-1017: Wish-Driven Programming Made Real, https://api-docs.deepseek.com/news/news261017/
   - Tier: primary | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "DeepSeek V4.1 Flash has been upgraded to DeepSeek-V4.1-Flash-1017."
2. **The 1017 weights are open on Hugging Face under the MIT License (Safetensors, 48 shards), with the card listing a model size of 763B params.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash-1017, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
   - Tier: primary | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "Model size 763B params"
3. **The architecture is a mixture-of-expans model with a 552B backbone plus a 196B Engram conditional memory, activating 8B parameters per token in prefill and 16B during decode, with a 1M-token context.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters" and "activate only 8B parameters per token during prefill and 16B during decode"
4. **"Max" is not a separate model: the official card exposes a continuously controllable reasoning-effort setting from 1 to 100, and Artificial Analysis lists "(Max)" as that effort level on the same weights.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash-1017, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
   - Tier: primary | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "a continuously controllable reasoning effort setting (integer 1-100)"
5. **DeepSeek V4.1 Flash 1017 (Max) scores 45 on the Artificial Analysis Intelligence Index, ranking #2 of 121 in its open-weight class.**
   - Source: DeepSeek V4.1 Flash 1017 model page, https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "DeepSeek V4.1 Flash 1017 (Max) scores 45 on the Artificial Analysis Intelligence Index"
6. **It does not top the overall index: AA's comparison list shows Claude Opus 5.5 (max with fallback), Claude Sonnet 5.5, Muse Wonder Full, GPT-6 Astra and others ranked above it.**
   - Source: DeepSeek V4.1 Flash model comparison, https://artificialanalysis.ai/models/deepseek-v4-1-flash
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "Claude Opus 5.5 (max with fallback), Claude Sonnet 5.5 (max with fallback), Muse Wonder Full (max), Claude Fable 5.1, GPT-6 Astra (max)"
7. **The API lists at $0.30 per 1M input tokens and $1.20 per 1M output tokens ($0.18 blended at AA's 7:2:1 mix, 98% cache discount), and AA measures cost per Intelligence Index task at $0.26, down from the predecessor's $0.49.**
   - Source: DeepSeek V4.1 Flash 1017 model page, https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "$0.30 per 1M input tokens", "$1.20 per 1M output tokens", "$0.26"
8. **In DeepSeek's own benchmarks relayed by The Decoder, 1017 beats larger models including Claude Opus 5, GPT 5.6-Sol, Kimi K3 and GLM 5.3 in several coding and agent categories, hitting DeepSWE v1.1 77.0 percent at just under $0.20 per task versus the predecessor's 74.2 percent at around $0.50.**
   - Source: The Decoder (Matthias Bastian, 2026-10-17), https://the-decoder.com/deepseek-v4-1-flash-1017-beats-larger-rivals-in-agentic-tasks-while-once-again-massively-cutting-per-task-costs/
   - Tier: docs | Confidence: medium | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "V4.1-Flash-1017 hits a top score of 77.0 percent at an average cost of just under $0.20 per task." / "The predecessor scored 74.2 percent but cost around $0.50 per run."
9. **A community VQ GGUF conversion finished and uploaded the same day (2026-10-17): a 113,556,639,424-byte base GGUF (about 106 GiB resident, --mem-budget-mb 110000) explicitly sized for one 128 GB DGX Spark, loadable only by the ds4-dfm-rs runtime.**
   - Source: Baekpica/DeepSeek-V4.1-Flash-1017-VQ-GGUF, https://huggingface.co/Baekpica/DeepSeek-V4.1-Flash-1017-VQ-GGUF
   - Tier: community | Confidence: medium | Accessed: 2026-10-19 | Via: web_extract
   - Quote: "about 106 GiB loaded for this recipe on V4.1 Flash" / "Status, 2026-10-17: the conversion is finished and uploaded" / "Standard llama.cpp, Ollama and Transformers loaders do not read this format."
10. **The llama.cpp route is a 261.4 GiB IQ2_XS build targeting two 96 GB GPUs (roughly 79 GiB per card) plus about 115 GiB of host RAM for the Engram tables, and it requires an unmerged llama.cpp branch (PR #28696), marked experimental.**
    - Source: cliecy/DeepSeek-V4.1-Flash-1017-UD-IQ2XS-GGUF, https://huggingface.co/cliecy/DeepSeek-V4.1-Flash-1017-UD-IQ2XS-GGUF
    - Tier: community | Confidence: medium | Accessed: 2026-10-19 | Via: web_extract
    - Quote: "all weights except the engram tables to fit on two 96 GB GPUs" / "RAM: about 115 GiB free"
11. **On the independent Terminal-Bench 4.0 leaderboard, Claude Sonnet 5.5 (Max, Default Fallback) holds the highest score at 63.6%.**
    - Source: Terminal-Bench 4.0 evaluation page, https://artificialanalysis.ai/evaluations/terminalbench-4-0
    - Tier: benchmark | Confidence: high | Accessed: 2026-10-19 | Via: web_extract
    - Quote: "Claude Sonnet 5.5 (Max, Default Fallback) scores the highest on Terminal-Bench 4.0 with a score of 63.6%"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Artificial Analysis Intelligence Index score, 1017 (Max) | 45 | https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017 | "scores 45 on the Artificial Analysis Intelligence Index" |
| 2 | Same index, September predecessor V4.1 Flash (Max) | 39 | https://artificialanalysis.ai/models/deepseek-v4-1-flash | "DeepSeek V4.1 Flash (Max) scores 39" |
| 3 | Backbone parameters | 552B | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "552B backbone parameters" |
| 4 | Parameters activated per token during decode | 16B | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "16B during decode" |
| 5 | Model size on the 1017 card | 763B params | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 | "Model size 763B params" |
| 6 | Cost per Intelligence Index task (1017 vs predecessor) | $0.26 vs $0.49 | https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017 | "$0.26" |
| 7 | Context length | 1M | https://api-docs.deepseek.com/quick_start/pricing/ | "CONTEXT LENGTH \| 1M" |

## Analogy candidates
- **Vehicle**: a library where every question wakes only six of 384 shelves. **Mapping**: the 552B backbone is the shelves of books, the 196B Engram tables are the card catalog consulted before any shelf opens, and the 16B active parameters are the few shelves actually read per token -- which is why it thinks like a giant but bills like a small model. **Breaks when**: the catalog is nearly half the weight of the books and must ride in RAM or on disk no matter which shelves you open, so the building cannot shrink below the catalog.
- **Vehicle**: an oven dial. **Mapping**: "Max" is the temperature dial on the same 1017 oven -- one set of weights, a reasoning-effort setting from 1 to 100 that sets how long it thinks before answering. **Breaks when**: a hotter oven costs real time and tokens -- AA still ranks the model among the most verbose (210M output tokens on the index run).

## Misconceptions
- Myth: DeepSeek 1017 (Max) is now the top AI model overall. Reality: 45 is #2 of 121 among open-weight large reasoning models on AA v4.3.2; Claude Opus 5.5, Sonnet 5.5 and GPT-6 Astra sit above it overall (claims 5, 6).
- Myth: No local weights yet, Flash 1017 is API-only. Reality: MIT weights shipped on Hugging Face the same day, and a community quant is already sized for a 128 GB DGX Spark (claims 2, 9).
- Myth: It is called Flash, so it fits a gaming card. Reality: 552B backbone plus ~196B Engram tables means even 2-bit builds target 128 GB unified memory or two 96 GB cards (claims 3, 9, 10).

## Glossary
- **Mixture of Experts (MoE)**: a model architecture that stores many specialist sub-networks ("experts") and activates only a few per token.
- **Active parameters**: the subset of a model's weights actually used to process one token, the number that drives speed and cost.
- **Engram conditional memory**: DeepSeek's lookup-table memory (196B parameters in this architecture) consulted via token-based lookup before the main network runs.
- **GGUF**: the single-file weight format used by llama.cpp and friends for running models locally.
- **Quantization**: shrinking weight precision (for example 4-bit) to cut file size and memory at some accuracy cost.
- **Reasoning effort**: a dial for how long a model thinks before answering; on 1017 it is an integer from 1 to 100, and "Max" is its top.
- **Artificial Analysis Intelligence Index**: an independent aggregate score (v4.3.2, ten evaluations) comparing models across reasoning and agent tasks.
- **Unified memory**: a machine design where CPU and GPU share one memory pool, such as the DGX Spark's 128 GB.

## Unverified
- "1017 (Max)" as a distinct DeepSeek product: no fetched official page names one; officially, Max is the top of a 1-100 reasoning-effort dial.
- The exact total size of the official safetensors checkpoint: a community page reports "The 510 GB official checkpoint", but no fetched official page states a total.
- Performance on the channel's own DGX Spark (tokens per second, load time): not measured; a first-party number should replace this line.
- A Hacker News discussion title suggesting 24 GB of VRAM plus disk streaming is enough for 1017: the discussion page was not fetched.
- Stock-llama.cpp GGUFs of 1017 (for example mrfakename or unsloth repos): seen only as search snippets; llama.cpp support rides the unmerged PR #28696.
- The radar's "152 points / 54 comments" thread was not found; the fetched HN thread (item 50129045) shows 941 points and 706 comments.

## Suggested outline
1. Hook on the correction: 1017 (Max) just scored 45 on the Artificial Analysis index, number two of 121 open-weight models -- and the weights are already downloadable, not "when GGUFs".
2. What actually shipped on 2026-10-17: MIT weights, a 552B-parameter backbone with an Engram lookup memory, only 16B active per token, 1M context; "Max" is the effort dial, not a bigger model.
3. The local fit answered: a community quant already sized for one 128 GB DGX Spark (about 106 GiB resident); the llama.cpp route still wants two 96 GB cards plus host RAM and an unmerged PR; a 24 GB gaming card is out -- the cheap API ($0.26 per index task) is the gaming-card viewer's takeaway.

## Viewer situation
You have watched every DeepSeek open drop run on local hardware, and you have one 24 GB gaming card waiting for the next one.

## Has process
false

## Objection
It is 763B parameters on the card -- "Flash" is marketing, nothing consumer-sized runs it without a 128 GB unified-memory box or two workstation cards, and the index crown is only within open weights.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://api-docs.deepseek.com/news/news261017/ | DeepSeek-V4.1-Flash-1017: Wish-Driven Programming Made Real | primary | web_extract | 2026-10-19 |
| 2 | https://api-docs.deepseek.com/quick_start/pricing/ | Models and Pricing, DeepSeek API Docs | primary | web_extract | 2026-10-19 |
| 3 | https://api-docs.deepseek.com/updates/ | Change Log, DeepSeek API Docs | primary | web_extract | 2026-10-19 |
| 4 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 | deepseek-ai/DeepSeek-V4.1-Flash-1017 model card | primary | web_extract | 2026-10-19 |
| 5 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash model card | primary | web_extract | 2026-10-19 |
| 6 | https://huggingface.co/Baekpica/DeepSeek-V4.1-Flash-1017-VQ-GGUF | Baekpica/DeepSeek-V4.1-Flash-1017-VQ-GGUF | community | web_extract | 2026-10-19 |
| 7 | https://huggingface.co/cliecy/DeepSeek-V4.1-Flash-1017-UD-IQ2XS-GGUF | cliecy/DeepSeek-V4.1-Flash-1017-UD-IQ2XS-GGUF | community | web_extract | 2026-10-19 |
| 8 | https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017 | DeepSeek V4.1 Flash 1017 model page | benchmark | web_extract | 2026-10-19 |
| 9 | https://artificialanalysis.ai/models/deepseek-v4-1-flash | DeepSeek V4.1 Flash model page and comparison list | benchmark | web_extract | 2026-10-19 |
| 10 | https://artificialanalysis.ai/evaluations/terminalbench-4-0 | Terminal-Bench 4.0 evaluation leaderboard | benchmark | web_extract | 2026-10-19 |
| 11 | https://the-decoder.com/deepseek-v4-1-flash-1017-beats-larger-rivals-in-agentic-tasks-while-once-again-massively-cutting-per-task-costs/ | The Decoder: DeepSeek's smaller model beats larger rivals in agentic tasks | docs | web_extract | 2026-10-19 |
| 12 | https://news.ycombinator.com/item?id=50129045 | Hacker News: DeepSeek-v4.1-Flash-1017 | community | web_extract | 2026-10-19 |

## Notes
Conflict: The Decoder's "beats larger models" line relays DeepSeek's own benchmark charts (per-benchmark margins live in images), and it noted "Independent benchmarks haven't come out yet" at publish; AA's measured speed is slightly down (227.1 vs 231.2 output tokens per second) even as cost per task halved, and independent Terminal-Bench 4.0 is led by Claude Sonnet 5.5 (Max) at 63.6%. The Decoder names "GPT 5.6-Sol" where AA now lists "GPT-6.1 Sol", likely a rename between article and leaderboard. Tier note: the community quant sizes (claims 9, 10) are community-tier, so the narration should attribute them ("the converter reports about 106 GiB"); key numbers above are all primary- or benchmark-backed. The radar's "tops the index" premise is corrected by claims 5 and 6; keep the reframe, drop the global crown.

## Decisions
- Checkpoint (angle confirm, unattended): kept the pick's angle (index result + local-weights question) but corrected the premise -- 45 is #2 of 121 in AA's open-weight class, not the overall #1, and weights already shipped day one, so "GGUFs when?" becomes "GGUFs exist, what fits". Chosen because every fetched source contradicts the stronger reading; the reframe is the honest version and still the hook.
- Sources: 12 fetched (5 primary, 3 benchmark, 2 community HF repos, 1 press, 1 HN); FireCrawl 402 so fetches ran via the research workers' web tools.
