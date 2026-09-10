---
slug: 2026-09-10-deepseek-v4-1-flash-open-weigh
stage: 03-research
topic: "DeepSeek V4.1 Flash open weights landed; the KV cache compression in the tech report is the real story for local hardware"
depth: standard
generated_at: 2026-09-10T11:41:55Z
sources: 12
hub: "[[videos/2026-09-10-deepseek-v4-1-flash-open-weigh]]"
---

# Research brief: DeepSeek V4.1 Flash open weights and the KV cache compression story

## Summary
Every outlet this morning is covering the weights drop; the story for this channel is Figure 1b of the tech report, where the memory a single token of context costs falls from 389,120 bytes on DeepSeek-V1 to 890 bytes on V4.1-Flash, while the model behind it got bigger, not smaller. The strongest concrete case for the viewer: by our arithmetic a full one-million-token context now needs under a gigabyte of KV cache, but the 552B-backbone-parameter weights still need hundreds of gigabytes, so on consumer hardware the cache stopped being the bottleneck and the weights became it. What could not be verified: any independent benchmark, any finished community quant (the same-day GGUF repo had no weights yet), the roughly 475 GiB checkpoint size (a community figure), and anything about tokens per second on hardware like ours. One conflict found: DeepSeek's own model card table scores NL2Repo-Bench at 64.0 while DeepSeek's own changelog says 65.4, so the brief avoids that number. And every benchmark below was run by DeepSeek on DeepSeek's own harness, which the script has to say out loud.

## Thesis
The open weights are the news, but the KV cache compression behind them -- 890 bytes per token, roughly 437 times smaller than V1 -- is what changes what one machine can hold at a million tokens of context.

## Explanation path
Open with the dated event: on the morning of September 10, 2026, DeepSeek put the V4.1-Flash weights on Hugging Face under an MIT license, and Reuters covered the launch the same day. Before any compression talk can land, the viewer needs what a KV cache is: the running notes a model keeps so it does not have to re-read the whole conversation for every word it writes, and the thing that actually grows until it fills your memory on long contexts -- the weights do not grow, the notes do. Once that is in place, give the mechanism at the level a beginner keeps: most layers stop keeping their own copy of the notes and share one (Compressed Sparse Attention 2), the notes get written in half-size shorthand (FP4), and the copy parked on disk shrinks too (SWA Bounded Replay, roughly 1/8). Then the numbers in sequence: 890 bytes per token, roughly 1/4 of the previous Flash, approximately 437-fold less than V1, and decode compute that stays nearly flat as context grows -- that last part is why people who run agents care. Then translate to the desk: about 0.9 GB of cache for a full million-token context by our arithmetic, against a 552B-parameter checkpoint in 48 shards that no 24 GB gaming GPU can hold and even a 128 GB unified-memory box cannot load at the shipped FP8/FP4 precision; the same-day community quants are only starting to appear. Close on the skeptical frame: these are the vendor's numbers on the vendor's harness; the independently checkable facts today are the MIT license, the API price, and the September 14 retirement routing of V4-Pro.

## Claims
1. **DeepSeek officially released DeepSeek-V4.1-Flash on September 10, 2026, and describes it as the smallest model in its new architecture family.**
   - Source: Change Log | DeepSeek API Docs, https://api-docs.deepseek.com/updates
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "Today, we officially release the DeepSeek-V4.1-Flash model. It is the smallest model in our new architecture family, with native multimodal visual understanding."
2. **DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts model with 552B backbone parameters and support for contexts of up to one million tokens.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "We introduce DeepSeek-V4.1-Flash, a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens."
3. **Its Causal Encoder-Decoder architecture activates 8B parameters per token during prefill and 16B during decode.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "This allows the model to activate only 8B parameters per token during prefill and 16B during decode, substantially improving cost efficiency for input-heavy agentic workloads."
4. **CSA2 cross-layer KV reuse plus FP4 main KV caching cut the global KV cache footprint to 890 bytes per token, roughly 1/4 of DeepSeek-V4-Flash and down from 389,120 bytes per token on DeepSeek-V1, approximately a 437-fold reduction.**
   - Source: DeepSeek-V4.1-Flash Technical Report, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "DeepSeek-V4.1-Flash achieves approximately 4-fold and 437-fold reductions in per-token global KV cache size relative to DeepSeek-V4-Flash and DeepSeek-V1, respectively."
5. **SWA Bounded Replay reduces the persistent KV cache footprint, the copy kept on SSD or in host memory, to roughly 1/8 of DeepSeek-V4-Flash.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "This allows the model ... avoiding the need to persist SWA KV to SSD and reducing the persistent KV cache footprint to roughly 1/8 of that of DeepSeek-V4-Flash."
6. **The repository and the model weights are MIT licensed, so the weights can be downloaded, run and redistributed freely.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "This repository and the model weights are licensed under the MIT License."
7. **Extending the context 256-fold, from 4K to 1M tokens, increases the model's single-token Decode FLOPs by only 1/4.**
   - Source: DeepSeek-V4.1-Flash Technical Report, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "Figure 2 shows that extending the context length 256-fold, from 4K to 1M, increases its Decode FLOPs by only 1/4, significantly less than the growth observed for DeepSeek-V4-Flash."
8. **On DeepSeek's own harness (reasoning_effort=100, Minimal mode of DeepSeek Harness, 1M-token context window, temperature=1.0, top_p=0.95), V4.1-Flash scores DeepSWE v1.1 (Resolved) 74.2 against DeepSeek-V4-Pro's 62.7, and Terminal-Bench 2.1 (Pass@1) 90.6 against V4-Pro's 87.9.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "| DeepSWE v1.1 (Resolved) | 74.0 | 73.0 | 67.5 | 66.9 | 62.7 | 54.4 | 74.2 |" ... "For code agent benchmarks (Terminal-Bench 2.1/3.0/4.0, DeepSWE v1.1, NL2Repo-Bench, ProgramBench), the model is evaluated with the Minimal mode of DeepSeek Harness and a 1M-token context window."
9. **The API undercuts V4-Pro at $0.15 per million input tokens (cache miss, off-peak) and $0.6 per million output tokens (off-peak) against V4-Pro's $0.66 and $1.98, and from 12:00 Beijing Time on September 14, 2026 all deepseek-v4-pro requests route to V4.1-Flash at Flash pricing.**
   - Source: Models & Pricing | DeepSeek API Docs, https://api-docs.deepseek.com/quick_start/pricing
   - Tier: primary | Confidence: high | Accessed: 2026-09-10 | Via: web_extract
   - Quote: "| PRICING(3) | 1M INPUT TOKENS (CACHE MISS) | OFF-PEAK | $0.15 | $0.66 |" ... "After 12:00 Beijing Time on September 14, 2026, and until V4.1 Pro is released in the future, requests to `deepseek-v4-pro` will all be routed to V4.1 Flash and billed at the V4.1 Flash price."
10. **Community quantized builds appeared on Hugging Face the same morning: the model's quantization listing showed 3 entries at fetch time, including a GGUF repo and two NVFP4 builds.**
    - Source: Quantized Models for deepseek-ai/DeepSeek-V4.1-Flash, https://huggingface.co/models?other=base_model:quantized:deepseek-ai/DeepSeek-V4.1-Flash
    - Tier: primary | Confidence: medium | Accessed: 2026-09-10 | Via: web_extract
    - Quote: "Models 3" ... "vcruz305/DeepSeek-V4.1-Flash-GGUF ... s-zaizen/DeepSeek-V4.1-Flash-NVFP4 ... LibertAIDAI/DeepSeek-V4.1-Flash-NVFP4"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | global KV cache per token, V4.1-Flash | 890 bytes per token | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf | "reduce its global KV cache footprint (always in HBM) to 890 bytes per token" |
| 2 | global KV cache per token, DeepSeek-V1 | 389,120 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf | "\| DeepSeek-V1 \| 2023.11 \| 389,120 \| -- \|", listed under "Global KV Cache Per Token (Bytes)" |
| 3 | persistent KV cache vs DeepSeek-V4-Flash | roughly 1/8 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "reducing the persistent KV cache footprint to roughly 1/8 of that of DeepSeek-V4-Flash" |
| 4 | activated parameters | 8B per token during prefill and 16B during decode | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "activate only 8B parameters per token during prefill and 16B during decode" |
| 5 | API price, cache-miss input | $0.15 per 1M input tokens (off-peak) | https://api-docs.deepseek.com/quick_start/pricing | "\| 1M INPUT TOKENS (CACHE MISS) \| OFF-PEAK \| $0.15 \| $0.66 \|", priced per 1M tokens as of 2026-09-10 |

## Analogy candidates
- **A kitchen's shared clipboard**: The KV cache is the running prep notes a cook keeps so each new plate does not mean re-chopping every onion from scratch; the notes grow with the order, not the recipe book. CSA2 is the sous chefs agreeing to share one clipboard instead of each keeping a copy, and FP4 is writing the shorthand smaller. Breaks when: a photocopy loses nothing, but FP4 really does write the notes with less precision, and sharing only works because the model was trained to share -- you cannot hand this clipboard trick to a normal model.
- **The streaming-service rewatch**: Persistent KV on SSD is keeping every tape of every episode so a returning viewer skips nothing; SWA Bounded Replay is re-watching just the last minute to catch up, at 1/8 the shelf space. Breaks when: the rewatch is not free -- it spends compute re-prefilling the recent tokens, so the trade is shelf space for a little replay work, not storage for nothing.

## Misconceptions
- Myth: "890 bytes per token means the download shrank 437 times." Reality: the compression applies to the per-conversation memory the context uses at run time; the model itself is a 552B-backbone-parameter MoE that must still be loaded whole (claim 2, claim 4).
- Myth: "It beat DeepSeek-V4-Pro, so it beats everything." Reality: DeepSeek's own table shows Opus-5.0 ahead of V4.1-Flash on Terminal-Bench 3.0 (43.3 vs 30.0) and HLE (56.3 vs 36.8); the "surpassed" claim is DeepSeek's, about its own V4-Pro, on its own harness (claim 8).

## Glossary
- **KV cache**: the notes a model keeps about everything it has read so far, so it does not have to recompute them for every new word it writes.
- **Mixture of Experts (MoE)**: a model design where only a small subset of specialist sub-networks is activated for each token, so total stored parameters far exceed active ones.
- **open weights**: the trained model files are published for anyone to download, run and inspect locally, under a license (here MIT) that permits it.
- **quantization**: storing model numbers in fewer bits than they were trained with, shrinking memory and download size at some cost in fidelity.
- **prefill**: the phase where the model reads your input and builds its notes.
- **decode**: the phase where the model writes the answer one token at a time.
- **FP4**: a 4-bit number format; KV notes stored in FP4 take half the space of 8-bit notes.
- **HBM**: high-bandwidth memory, the fast memory on AI accelerators and top-end GPUs that the runtime KV cache lives in.
- **token**: the smallest chunk of text a model reads or writes, roughly a word or part of one.

## Unverified
- By our own arithmetic from the tech report's numbers, 890 bytes per token works out to about 0.9 GB of KV cache for a full one-million-token context; DeepSeek does not state the per-context total anywhere we fetched.
- The same-day community GGUF repo describes the official checkpoint as about 475 GiB across 48 shards; the 48-shard count is confirmed by the Hugging Face file tree, but the size figure is community-reported and no official page states it.
- The most-watched same-day GGUF repo had not uploaded any weights at fetch time, so no complete community quantization is confirmed to exist yet.
- No llama.cpp, vLLM, Ollama, LM Studio or SGLang release supporting V4.1-Flash could be verified at fetch time; the model card's inference folder is the only official local path we could ground.
- Community posters on Hacker News and the NVIDIA DGX Spark forum expect quantized builds to run on 192 GB-class machines, but no tier 1-3 page we fetched confirms any actual local run of V4.1-Flash.
- Tokens per second, load time and memory use on our own DGX Spark and consumer GPUs must be measured by us before the channel states any performance figure.

## Suggested outline
1. Hook on the dated event and the buried number: free MIT-licensed weights for a 552B-parameter, million-token-context model landed on Hugging Face this morning, and the tech report's own table says a token of context now costs 890 bytes of cache, down from 389,120 on V1.
2. Define the KV cache as the model's running notes, then walk the two compression tricks through one analogy (layers share one clipboard; notes written in half-size shorthand; the disk copy shrinks to roughly 1/8), keeping the 24 GB gaming GPU versus 128 GB unified-memory frame at the center.
3. Honest catch and payoff: a full million-token context costs under a gigabyte of cache by our arithmetic, but the weights still do not fit a 24 GB card and every benchmark is DeepSeek's own harness; the checkable facts are the MIT license, the $0.15 per million input tokens off-peak price and the September 14 V4-Pro retirement, so end on what to watch next -- the first quant that actually fits the viewer's machine.

## Viewer situation
You've got a gaming PC with a 24 GB GPU or a 128 GB Mac, you saw this morning that DeepSeek dropped free model weights again, and you want to know whether this one finally fits your machine.

## Has process
false

## Objection
Every number here is DeepSeek's own, measured on DeepSeek's own harness, and 890 bytes per token shrinks the conversation's memory, not the 552-billion-parameter weight download that still is not coming close to fitting on your card.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash model card | primary | web_extract | 2026-09-10 |
| 2 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf | DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression (Technical Report) | primary | web_extract | 2026-09-10 |
| 3 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/tree/main | deepseek-ai/DeepSeek-V4.1-Flash file tree | primary | web_extract | 2026-09-10 |
| 4 | https://huggingface.co/models?other=base_model:quantized:deepseek-ai/DeepSeek-V4.1-Flash | Quantized Models for deepseek-ai/DeepSeek-V4.1-Flash | primary | web_extract | 2026-09-10 |
| 5 | https://api-docs.deepseek.com/news/news260910 | DeepSeek-V4.1-Flash: Smarter, Faster, More Efficient | primary | web_extract | 2026-09-10 |
| 6 | https://api-docs.deepseek.com/updates | Change Log | DeepSeek API Docs | primary | web_extract | 2026-09-10 |
| 7 | https://api-docs.deepseek.com/quick_start/pricing | Models & Pricing | DeepSeek API Docs | primary | web_extract | 2026-09-10 |
| 8 | https://www.deepseek.com/en/news/deepseek-v4-1-flash/ | Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient. | primary | web_extract | 2026-09-10 |
| 9 | https://www.reuters.com/world/asia-pacific/chinas-deepseek-launches-v41-flash-model-2026-09-10/ | China's DeepSeek launches V4.1-Flash model | Reuters | docs | web_extract | 2026-09-10 |
| 10 | https://huggingface.co/vcruz305/DeepSeek-V4.1-Flash-GGUF | vcruz305/DeepSeek-V4.1-Flash-GGUF | community | web_extract | 2026-09-10 |
| 11 | https://forums.developer.nvidia.com/t/deepseek-v4-1-flash/382725 | DeepSeek v4.1 Flash - DGX Spark / GB10 - NVIDIA Developer Forums | community | web_extract | 2026-09-10 |
| 12 | https://news.ycombinator.com/item?id=49624603 | DeepSeek launching v4.1 flash cheaper and more capable than v4 pro | Hacker News | community | web_extract | 2026-09-10 |

## Notes
Conflict: DeepSeek's model card table scores NL2Repo-Bench (Score) at 64.0 for V4.1-Flash while DeepSeek's own API changelog lists "NL2Repo-Bench: 65.4"; both pages were fetched, both are tier 1, and the brief avoids the number entirely. All benchmark figures are vendor-run (DeepSeek Harness, reasoning_effort=100); no independent harness page (Artificial Analysis, LMArena) for V4.1-Flash could be fetched at this hour, so nothing here is third-party verified. The HLE and Terminal-Bench 3.0/4.0 gaps behind Opus-5.0 are the strongest engineer-credible counterweight to the "beats everything" reading. Reuters confirms the launch date and adds IPO-preparation context (STAR Market), background color only. The strongest keyword-gap beat is the KV-per-token generational table (389,120 to 890): no Shorts-form summary of it existed at fetch time.
