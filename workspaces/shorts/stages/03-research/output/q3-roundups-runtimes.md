# Q3 — Roundups & runtimes: what the 'best local coding LLM' lists skip about 128 GB unified memory

Question: What do the popular 'best local coding LLM' roundups get wrong or skip about the 128 GB unified-memory constraint, and what does the user actually have to do to run one of these models tonight (download size, quant choice, runtime)?
Topic: Best local coding LLM for a 128 GB unified-memory machine (NVIDIA DGX Spark GB10 class). Date: 2026-09-30.
Budget used: 2 searches, 3 page fetches succeeded (5 attempted; Reddit blocked twice, no browser available).

## Pages fetched this session

- https://www.datacamp.com/blog/best-llm-for-coding — "Best LLM for Coding in 2026: 9 Models Ranked | DataCamp" (tier: secondary roundup press) — web_extract
- https://ollama.com/library/gpt-oss:120b — "gpt-oss:120b" Ollama library page (tier: docs, primary runtime doc) — web_extract
- https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569 — NVIDIA DGX Spark forum (tier: community, tier 4) — web_extract

## FINDINGS: claim | verbatim quote | url | page title | tier | confidence | fetched via | 2026-09-30

1. The DataCamp 9-model coding ranking from the ideas note is real and current: it self-identifies as the September 2026 edition and reviews releases dated September 22, 2026, consistent with 'published this week'; it ranks cloud models first and states the ordering principle explicitly. | "The best cloud frontier models for coding in September 2026 are Claude Opus 5.5, Claude Fable 5.1, GPT-6 Astra, and Gemini 3.8 Flash, and all 4 ship a context window of roughly 1M tokens. ... I list them in the order I would recommend them to a team that can afford any of them." | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary (roundup press) | high | web_extract | 2026-09-30

2. The claim that the DataCamp roundup 'says nothing about local memory fit' is FALSE: it carries a dedicated 128 GB workstation pick with parameter and quant-size context. The real gap for a 128 GB viewer is different — the roundup's top-scoring open models are explicitly un-runnable at home, and the memory guidance that exists is scattered across model blurbs rather than a fit guide. | "Best local model for a 128 GB workstation: Laguna S 2.1 (Poolside), 118B parameters with only 8B active, 1M context." | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary | high | web_extract | 2026-09-30

3. The roundup's strongest open-weight coder is flagged as impossible to run at home, and the cheapest top-tier open model has a checkpoint that dwarfs any 128 GB machine — a reader who stops at rank 5-6 buys hardware advice that does not apply to their box. | "Best open weights you cannot run at home: Kimi K3 (Moonshot AI), 2.8 trillion parameters, 88.3% Terminal-Bench 2.1. ... The checkpoint is also about 510 GB, so \"open weights\" here means a multi-GPU server." | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary | high | web_extract | 2026-09-30

4. The 128 GB memory math the roundups bury in a trade-off paragraph: a 118B MoE at 4-bit needs roughly 60-70 GB for weights alone BEFORE the KV cache — that is the number that decides what fits on a DGX Spark tonight. | "118B parameters at 4-bit is roughly 60 to 70 GB of weights before you allocate a KV cache, so a 24 GB GPU is out." | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary | high | web_extract | 2026-09-30

5. What 'tonight' actually looks like per the roundup's own run-locally recipe: 3 steps — download a quantized GGUF, serve it with llama.cpp/LM Studio/Ollama, point a client at the OpenAI-compatible endpoint. | "Running an open-weight coding model locally takes 3 steps: download a quantized checkpoint, serve it behind an OpenAI-compatible endpoint, and point your client or coding assistant at that endpoint. ... llama-server -m Qwen3.8-27B-UD-Q4_K_M.gguf -c 32768 -ngl 99 --port 8080" | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary | high | web_extract | 2026-09-30

6. Runtime reality (Ollama docs, 100B+ class): gpt-oss:120b is a 117B-parameter MoE shipped in exactly ONE quantization — MXFP4 — as a single 65GB download; you do NOT pick Q4_K_M vs Q8 on this model in Ollama, and the stated guidance is it "fits on a single 80GB GPU". | "parameters117B · quantizationMXFP4 · 65GB ... Ollama is supporting the MXFP4 format natively without additional quantizations or conversions. ... quantizing these to MXFP4 enables the smaller model to run on systems with as little as 16GB memory, and the larger model to fit on a single 80GB GPU." | https://ollama.com/library/gpt-oss:120b | gpt-oss:120b (Ollama library page) | docs (primary runtime doc) | high | web_extract | 2026-09-30

7. The one-command tonight path in Ollama for a 100B+ model, with its download size and adoption stated on the page. | "ollama run gpt-oss:120b ... a951a23b46a1 · 65GB ... 13.3M Downloads" | https://ollama.com/library/gpt-oss:120b | gpt-oss:120b (Ollama library page) | docs | high | web_extract | 2026-09-30

8. Community reality on the exact target machine (tier 4): a DGX Spark owner runs Qwen3-Next-80B-A3B on vLLM at about 45 tok/s with 115-120 GB of the 128 GB unified memory in use — a real 128 GB coding stack consumes nearly all of it once KV cache and helper models are loaded. | "Right now I'm running Qwen3‑Next‑80B‑A3B at around 45 tok/s, with 115–120 GB of unified memory in use and roughly 95 % GPU utilization; Qwen3‑Embedding‑0.6B and Qwen3‑Reranker‑0.6B add under 1.5 GB VRAM overhead." | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569 | Building Local + Hybrid LLMs on DGX Spark That Outperform Top Cloud Models — NVIDIA Developer Forums | community (tier 4) | medium | web_extract | 2026-09-30

9. Community-sourced simpler alternative for coding on the Spark (tier 4): when the owner does not want the full RAG stack, the recommended pure fast chat/code stack is Ollama with a 32B-class model. | "Pure fast chat / code | Ollama + DeepSeek‑R1 or Qwen2.5‑32B | Lower latency, simpler, no reranker overhead." | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569 | Building Local + Hybrid LLMs on DGX Spark — NVIDIA Developer Forums | community (tier 4) | medium | web_extract | 2026-09-30

10. The honest capability gap the roundups do print, and the 128 GB buyer should hear: the best 24 GB-class local model is still ~18 Terminal-Bench points behind the cloud leader. | "73.0% versus 91.4% on Terminal-Bench 2.1 is still an 18-point gap, and it shows up as more retries on long agentic tasks." | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary | high | web_extract | 2026-09-30

11. Quant-choice and download-size reality per model class, from the roundup's own entries: the 27B dense pick is a 16.5 GB single GGUF at UD-Q4_K_M; the 80B MoE pick is about 48 GB at Q4_K_M; the 118B pick needs 60-70 GB at Q4 — all three fit a 128 GB machine with room for context. | "The community UD-Q4_K_M GGUF from Unsloth is a single 16.5 GB file, which leaves room for a 32K context on a 24 GB card. ... The official Q4_K_M GGUF is about 48 GB, which suits a 64 GB Mac or a CPU-offload setup better than a single consumer GPU." | https://www.datacamp.com/blog/best-llm-for-coding | Best LLM for Coding in 2026: 9 Models Ranked | DataCamp | secondary | high | web_extract | 2026-09-30

## NUMBERS: label | verbatim value with unit | url

- Ollama gpt-oss:120b download size | "65GB" | https://ollama.com/library/gpt-oss:120b
- Ollama gpt-oss:120b total parameters | "117B" | https://ollama.com/library/gpt-oss:120b
- MXFP4 precision | "4.25 bits per parameter" | https://ollama.com/library/gpt-oss:120b
- Stated minimum memory for the 20B sibling | "as little as 16GB memory" | https://ollama.com/library/gpt-oss:120b
- Stated fit target for the 120B model | "a single 80GB GPU" | https://ollama.com/library/gpt-oss:120b
- Ollama gpt-oss:120b downloads to date | "13.3M Downloads" | https://ollama.com/library/gpt-oss:120b
- Laguna S 2.1 weights at 4-bit (128 GB workstation pick) | "roughly 60 to 70 GB of weights" | https://www.datacamp.com/blog/best-llm-for-coding
- Laguna S 2.1 size / active params | "118B parameters with only 8B active" | https://www.datacamp.com/blog/best-llm-for-coding
- Laguna S 2.1 memory listed in comparison table | "60 to 70 GB at Q4" | https://www.datacamp.com/blog/best-llm-for-coding
- Qwen3.8-27B UD-Q4_K_M GGUF size | "16.5 GB at UD-Q4_K_M" | https://www.datacamp.com/blog/best-llm-for-coding
- Qwen3.8-27B UD-Q4_K_XL size | "UD-Q4_K_XL is 17.6 GB" | https://www.datacamp.com/blog/best-llm-for-coding
- Qwen3-Coder-Next official Q4_K_M GGUF size | "about 48 GB" | https://www.datacamp.com/blog/best-llm-for-coding
- DeepSeek V4.1 Flash checkpoint size | "about 510 GB" | https://www.datacamp.com/blog/best-llm-for-coding
- Kimi K3 total parameters | "2.8 trillion parameters" | https://www.datacamp.com/blog/best-llm-for-coding
- Local-vs-cloud Terminal-Bench 2.1 gap | "73.0% versus 91.4% ... still an 18-point gap" | https://www.datacamp.com/blog/best-llm-for-coding
- DGX Spark Qwen3-Next-80B-A3B generation speed (community) | "around 45 tok/s" | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569
- DGX Spark unified memory in use with 80B stack (community) | "115–120 GB of unified memory" | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569
- Embedding+reranker VRAM overhead on Spark (community) | "under 1.5 GB VRAM overhead" | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569
- llama.cpp context flag in the roundup's run command | "-c 32768" | https://www.datacamp.com/blog/best-llm-for-coding

## MISCONCEPTIONS: myth | reality | url

- Myth: The big 'best coding LLM' roundups ignore local memory fit entirely. | Reality: This week's DataCamp 9-model ranking does rank cloud models first ("I list them in the order I would recommend them to a team that can afford any of them") but does NOT skip memory: it names a "Best local model for a 128 GB workstation" (Laguna S 2.1) and gives quant sizes (16.5 GB / ~48 GB / 60-70 GB at Q4). What it skips is a fit guide — sizes are scattered across model blurbs, and ranks 5-6 (the top open models) are un-runnable on 128 GB. | https://www.datacamp.com/blog/best-llm-for-coding
- Myth: 'Open weights' means you can run it on your 128 GB box tonight. | Reality: The two highest-scoring open models are explicitly out of reach: Kimi K3 is "2.8 trillion parameters" ("Best open weights you cannot run at home") and DeepSeek V4.1 Flash's checkpoint is "about 510 GB". The practical ceiling from this list on 128 GB is the 118B Laguna S 2.1 at 60-70 GB of weights. | https://www.datacamp.com/blog/best-llm-for-coding
- Myth: Running a 100B+ model means shopping Q4_K_M vs Q8 quant ladders in your runtime. | Reality: Ollama's gpt-oss:120b ships in exactly one quantization, MXFP4 (4.25 bits per parameter), a single 65GB download — "without additional quantizations or conversions". Quant ladders (Q4_K_M, UD-Q4_K_XL...) apply to GGUF-family models like Qwen3.8-27B, not this one. | https://ollama.com/library/gpt-oss:120b
- Myth: 128 GB unified memory means 128 GB of model weights. | Reality: A real DGX Spark coding stack runs an 80B MoE at "115–120 GB of unified memory in use" out of 128 GB once KV cache, embedding and reranker services are counted; 4-bit weights are only the first "60 to 70 GB" slice on a 118B model. | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569
- Myth: If it fits in memory, it is the best coder for the machine. | Reality: The roundup states the fit-for-speed trade explicitly: Laguna's "8B active parameters make it far faster once the weights fit, which is the point of an overnight agent", while smaller dense Qwen3.8-27B "edges it" on raw scores; and local still trails cloud by "an 18-point gap" on Terminal-Bench 2.1. | https://www.datacamp.com/blog/best-llm-for-coding

## GLOSSARY: term | definition

- Unified memory | Single pool of LPDDR5X shared by CPU and GPU on the DGX Spark GB10 class (128 GB on that machine), so model weights + KV cache + services all draw from one budget.
- Quantization / quant | Storing model weights at fewer bits per parameter to shrink download and memory footprint, at some accuracy cost (4-bit roughly quarters weight size vs FP16).
- Q4_K_M | A llama.cpp GGUF k-quant mix averaging about 4-bit, the common quality/size default; "UD-Q4_K_M" is Unsloth's dynamic variant that keeps sensitive layers at higher precision.
- MXFP4 | OpenAI's 4.25-bit-per-parameter block format used by gpt-oss; Ollama supports it natively with no alternative quant ladder for that model.
- MoE (active parameters) | Mixture-of-experts model with a large total parameter count but few parameters computed per token (e.g. 118B total / 8B active); total size sets memory, active count sets speed.
- KV cache | Per-context memory the runtime allocates on top of weights; grows with context length, which is why weights + context must fit the memory budget together.
- Terminal-Bench 2.1 | Agentic eval (89 curated tasks) where a model works in a live shell; the roundup's headline coding-agency metric for 2026.

## UNVERIFIED

- An r/LocalLLaMA thread titled "Best LLM model for 128GB of VRAM?" exists (reddit.com/r/LocalLLaMA/comments/1qbmtuw), and a search snippet quotes a commenter saying "128GB os vRAM is the sweet spot tho! If you can do vllm or sglang then go for those!" — snippet only; Reddit blocked both fetch attempts this session, so treat as sentiment, not citation.
- Search results also surfaced related Reddit threads ("What's the best Local LLM to fully use 128 GB of unified memory in a DGX...", "New to local LLMs, DGX Spark owner looking for best coding model") that were not fetched and are unverified.
- The DataCamp article's exact publication date is not stated in the fetched text; it self-identifies as the September 2026 edition ("In a Nutshell: The Best Coding LLMs in September 2026") and cites September 22, 2026 releases, consistent with the ideas note's "published this week" but not a dated stamp.
- Sentiment (not grounded): community consensus reportedly favors vLLM/SGLang over Ollama for fully using ~128 GB — only the NVIDIA forum post (fetched, tier 4) actually supports a vLLM-on-Spark data point.

## NOT FOUND

- A fetchable r/LocalLLaMA page: old.reddit.com and www.reddit.com both rejected by the extractor, and no local browser was available to route around it.
- An explicit memory-guidance table in the Ollama gpt-oss:120b doc beyond the two fit statements quoted (16GB minimum for 20B; single 80GB GPU for 120B); Ollama publishes no per-host RAM requirement list on that page.
- NVIDIA's own DGX Spark memory-sizing documentation (not fetched within the 2-search/4-fetch budget).
- An exact publication date for the DataCamp ranking.
