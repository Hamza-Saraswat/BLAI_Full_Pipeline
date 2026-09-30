---
slug: 2026-09-30-best-local-coding-llm-what-act
stage: 03-research
topic: "Best local coding LLM: what actually fits 128 GB"
depth: standard
generated_at: 2026-09-30T12:05:00Z
sources: 13
hub: "[[videos/2026-09-30-best-local-coding-llm-what-act]]"
---

# Research brief: Best local coding LLM: what actually fits 128 GB

## Summary
The most arresting number is a fit failure: the leaderboard's top open coder family, MiniMax M2, needs a 138.59GB file even at its own recommended Q4_K_M quant, more than the whole 128 GB machine. The strongest concrete case is on the other side: gpt-oss-120b, a 117B-total/5.1B-active MoE that ships as one 65GB MXFP4 download, was measured by the llama.cpp maintainer on this exact class of hardware at 45.34 tokens per second decode. What could not be verified: whether the SWE-bench open leaders (MiniMax M2.5, GLM 5, Kimi K2.5) fit or run at all in 128 GB, and GLM-4.5-Air's architecture figures, which no fetched page stated. Sources conflict on the crown itself: SWE-bench Verified crowns MiniMax M2.5 (75.80) while the AA Coding Index table crowns DeepSeek V4-Pro (47.5) and Kimi K2.6 (47.1), so "best open coder" depends on the harness asked.

## Thesis
On 128 GB of unified memory the right coding model is not the leaderboard's best open coder but the best one that fits and still flies: gpt-oss-120b, with GLM-4.5-Air as the quality-per-gigabyte pick.

## Explanation path
Start with the constraint itself: one shared 128 GB pool holds the model weights, the KV cache that grows with context, and the OS, so the file has to fit with room left over. Then the two numbers that decide everything and live in tension: total parameters set whether a model fits at all, active parameters set how fast it thinks, which is why a 117B-total MoE with 5.1B active can be quick while a dense model that fits can crawl. With that rule, the roundups' ordering dissolves: the SWE-bench leaders are full-size models whose local fit was never measured, while the models measured on this hardware are the mid-size MoEs. Then land the two picks that survive the rule (gpt-oss-120b for speed and one-command setup, GLM-4.5-Air at Q4_K_M for quality per gigabyte), admit the honest catch on the skill gap, and close with the single command that starts the download tonight.

## Claims
1. **gpt-oss-120b is a 117B-total, 5.1B-active MoE explicitly built to fit a single 80GB GPU, so it fits 128 GB unified memory with room for context.**
   - Source: openai/gpt-oss-120b, https://huggingface.co/openai/gpt-oss-120b
   - Tier: primary | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "(117B parameters with 5.1B active parameters)" and "for production, general purpose, high reasoning use cases that fit into a single 80GB GPU (like NVIDIA H100 or AMD MI300X)"
2. **Ollama ships gpt-oss:120b in exactly one quantization, MXFP4 at 4.25 bits per parameter, as a single 65GB download.**
   - Source: gpt-oss:120b, https://ollama.com/library/gpt-oss:120b
   - Tier: docs | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "65GB" download, "MXFP4", "4.25 bits per parameter"
3. **The llama.cpp maintainer benchmarked gpt-oss-120b MXFP4 (59.02 GiB on disk, 116.83 B params) on a GB10 with llama-bench: 45.34 t/s single-stream decode (tg128), falling to 30.43 t/s at 48k context depth, with pp4096 prefill at 2046.65 t/s.**
   - Source: Performance of llama.cpp on NVIDIA DGX Spark #16578, https://github.com/ggml-org/llama.cpp/discussions/16578
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "pp4096 | 2046.65 +/- 3.43 ... tg128 | 45.34 +/- 0.11 ... tg128 @ d48000 | 30.43 +/- 0.02"
4. **GLM-4.5-Air at Q4_K_M is 73.50GB, the repo's recommended default quant, and can rise to Q6_K at 99.18GB and still fit; Q8_0 at 117.46GB fits on paper but leaves almost nothing for the KV cache.**
   - Source: bartowski/zai-org_GLM-4.5-Air-GGUF, https://huggingface.co/bartowski/zai-org_GLM-4.5-Air-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "GLM-4.5-Air-Q4_K_M.gguf ... 73.50GB"; "GLM-4.5-Air-Q6_K.gguf ... 99.18GB"; "GLM-4.5-Air-Q8_0.gguf ... 117.46GB"
5. **MiniMax-M2 at its recommended Q4_K_M quant is 138.59GB and does not fit 128 GB unified memory; only 3-bit-class quants such as Q3_K_XL at 108.74GB fit.**
   - Source: bartowski/MiniMaxAI_MiniMax-M2-GGUF, https://huggingface.co/bartowski/MiniMaxAI_MiniMax-M2-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "MiniMax-M2-Q4_K_M.gguf ... 138.59GB"; "MiniMax-M2-Q3_K_XL.gguf ... 108.74GB"
6. **Full-size GLM-4.5 overshoots 128 GB at every quant at or above 3-bit (Q3_K_M 164.95GB) and even its Q2_K_L file alone is 128.51GB, over budget before any KV cache.**
   - Source: bartowski/zai-org_GLM-4.5-GGUF, https://huggingface.co/bartowski/zai-org_GLM-4.5-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "GLM-4.5-Q3_K_M.gguf ... 164.95GB"; "GLM-4.5-Q2_K_L.gguf ... 128.51GB"
7. **On the official SWE-bench Verified default board (bash-only, mini-SWE-agent, human-filtered 500-instance subset) the open-family leaders are MiniMax M2.5 (high) 75.80, GLM 5 (high) 72.80%, Kimi K2.5 (high) 70.80%, while gpt-oss-120b posts 26.00 via mini-SWE-agent.**
   - Source: SWE-bench, https://www.swebench.com/
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "MiniMax M2.5 (high) 75.80"; "GLM 5 (high) 72.80%"; "Kimi K2.5 (high) 70.80%"; "gpt-oss-120b ... 26.00"
8. **DataCamp's September 2026 nine-model ranking lists cloud models first, names Kimi K3 ("2.8 trillion parameters") the best open weights you cannot run locally, and carries a 128 GB workstation pick whose 4-bit weights run "roughly 60 to 70 GB".**
   - Source: Best LLMs for Coding, https://www.datacamp.com/blog/best-llm-for-coding
   - Tier: docs | Confidence: high | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "2.8 trillion parameters"; "roughly 60 to 70 GB of weights"; "118B parameters with only 8B active"
9. **The crowns flip with the harness: a Fireworks table of the AA Coding Index (updated 4.27.26) crowns DeepSeek V4-Pro (47.5) and Kimi K2.6 (47.1) the top open-source coders, not SWE-bench's leaders.**
   - Source: Best LLMs for Coding, https://fireworks.ai/blog/best-llms-for-coding
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-30 | Via: hermes web_extract
   - Quote: "The top open-source spot on the AA Coding Index is now a near-tie between DeepSeek V4-Pro (47.5) and Kimi K2.6 (47.1)"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | MiniMax-M2 recommended Q4_K_M file size (does not fit) | 138.59GB | https://huggingface.co/bartowski/MiniMaxAI_MiniMax-M2-GGUF | "MiniMax-M2-Q4_K_M.gguf ... 138.59GB" |
| 2 | gpt-oss-120b total parameters | 117B parameters | https://huggingface.co/openai/gpt-oss-120b | "(117B parameters with 5.1B active parameters)" |
| 3 | gpt-oss-120b active parameters | 5.1B active parameters | https://huggingface.co/openai/gpt-oss-120b | "(117B parameters with 5.1B active parameters)" |
| 4 | Ollama gpt-oss:120b single download size (MXFP4 only) | 65GB | https://ollama.com/library/gpt-oss:120b | "65GB" |
| 5 | gpt-oss-120b decode on GB10, single-stream (tg128) | 45.34 t/s | https://github.com/ggml-org/llama.cpp/discussions/16578 | "tg128 | 45.34 +/- 0.11" |
| 6 | GLM-4.5-Air Q4_K_M file size (fits) | 73.50GB | https://huggingface.co/bartowski/zai-org_GLM-4.5-Air-GGUF | "GLM-4.5-Air-Q4_K_M.gguf ... 73.50GB" |
| 7 | GLM-4.5 Q2_K_L file alone (over budget before KV cache) | 128.51GB | https://huggingface.co/bartowski/zai-org_GLM-4.5-GGUF | "GLM-4.5-Q2_K_L.gguf ... 128.51GB" |
| 8 | Kimi K3 total parameters (best open weights you cannot run locally) | 2.8 trillion parameters | https://www.datacamp.com/blog/best-llm-for-coding | "2.8 trillion parameters" |

The arresting number for the hook is #1: 138.59GB against a 128 GB machine.

## Analogy candidates
- **Vehicle**: a big-block engine that fires only a few cylinders per revolution. Mapping: total parameters are the whole engine that must fit the garage (memory); active parameters are the cylinders actually fired each token, which set the speed. Breaks when: the analogy hides that the whole engine still has to be parked in the garage before any cylinder fires, and that a bigger engine costs nothing per revolution once parked.
- **Vehicle**: parking a car in a garage by removing seats. Mapping: quantization strips the model down (Q4_K_M is "removing seats") so it fits the 128 GB garage. Breaks when: below roughly 3-bit you are cutting structural parts, which the quant tables themselves flag as "Very low quality".

## Misconceptions
- Myth: 128 GB of unified memory can run any ~120B-scale open model. Reality: MiniMax-M2 needs 138.59GB even at its recommended Q4_K_M quant, so it misses the budget; only 3-bit-class quants such as Q3_K_XL at 108.74GB fit (claims 5).
- Myth: the best open coder on the leaderboard is therefore the best local coder. Reality: the SWE-bench Verified open leaders (MiniMax M2.5 75.80, GLM 5 72.80%, Kimi K2.5 70.80%) are full-size models whose 128 GB fit and speed were measured on no page fetched this run, while gpt-oss-120b, measured at 45.34 t/s on this hardware, posts 26.00 on the same board (claims 3, 7).
- Myth: bigger total parameter count is always the smarter local pick. Reality: total parameters only decide fit; active parameters decide speed, which is why the 117B-total/5.1B-active gpt-oss-120b decodes fluently while denser models that fit can crawl (claims 1, 3).
- Myth: "open weights" means you can run it on your box tonight. Reality: DataCamp's own roundup names Kimi K3, at "2.8 trillion parameters", the best open weights you cannot run locally, and DeepSeek V4.1 Flash's checkpoint is about 510 GB (claim 8).
- Myth: if it fits, it is fast. Reality: decode is bandwidth-bound, not capacity-bound: the same thread measured gpt-oss-20b at 84.67 tokens/sec on a Spark versus 117.32 tokens/sec on a MacBook Pro M4 Max.

## Glossary
- **unified memory**: a single pool of RAM shared by CPU and GPU (as on DGX Spark GB10), so one big model file needs no splitting between VRAM and system RAM.
- **quantization (quant)**: storing model weights at fewer bits per weight (for example 4-bit Q4_K_M) to shrink the file and memory footprint at some quality cost.
- **total vs active parameters**: total parameters are all stored weights and set memory size; active parameters are the weights computed per token and set generation speed.
- **MoE (Mixture of Experts)**: an architecture that stores many expert weight blocks but routes each token through only a few, allowing huge total size with small per-token compute.
- **GGUF**: the llama.cpp ecosystem's single-file model format in which each file is one specific quant of a model, with its size listed in GB on the repo page.
- **KV cache**: per-conversation memory that grows with context length and must fit in memory alongside the model weights.
- **MXFP4**: a 4.25-bit micro-scaling weight format used natively by the gpt-oss models; Ollama ships gpt-oss:120b in this one quant only.
- **SWE-bench Verified**: a human-filtered 500-instance subset of real GitHub issues whose official leaderboard currently defaults to a bash-only mini-SWE-agent setting.
- **tokens per second (decode)**: how fast a loaded model generates text; llama-bench reports it as tg (text generation) at a given context depth.

## Unverified
- GLM-4.5-Air is widely described as a 106B-total / 12B-active MoE with 128K context and MIT license, but those figures were not stated on any page fetched this session (only its GGUF quant sizes were).
- Whether quantized variants of the SWE-bench open leaders (MiniMax M2.5, GLM 5, Kimi K2.5) fit and run acceptably in 128 GB was not measured on any fetched page.
- Spark Arena values quoted inside the llama.cpp thread (gpt-oss-120b 58.82 tok/s single node) quote a leaderboard site that was not fetched this session.
- A July 2026 roundup attributes 273 GB/s memory bandwidth to the GB10 and community decode speeds near 50 tok/s for gpt-oss-120b and 2.5 to 5 tok/s for dense 70B models, with no per-number method shown.
- Qwen3-Coder-480B-A35B, DeepSeek-V3.x and Kimi K2 are commonly reported as far too large for 128 GB at usable quants, but no fetched page stated their quant file sizes.
- GLM-4.6 exists as a newer GLM coding release, but no page fetched this session states its parameter count or quant sizes.
- Usable memory on DGX Spark is often reported around 119-120 GB after system overhead, which would tighten the fits above; not verified on a fetched page this session.

## Suggested outline
1. Open on the fit failure: the leaderboard's top open coder family needs a 138.59GB file at its own recommended quant, and your whole machine is 128 GB.
2. Give the rule the roundups bury: total parameters decide fit, active parameters decide speed, so the 117B-total / 5.1B-active gpt-oss-120b ships as one 65GB download and was measured at 45.34 tokens per second on this exact class of hardware, while GLM-4.5-Air at 73.50GB is the quality-per-gigabyte pick.
3. Honest catch and payoff: the same leaderboard gives gpt-oss-120b 26.00 against the leaders' 75.80, so local means choosing fit and speed over the crown; tonight it is one Ollama command and a 65GB download.

## Viewer situation
You've got a 128 GB unified-memory machine (or you're eyeing one) and you want the best coding model that actually runs on it tonight, not another cloud-first top-ten list.

## Has process
false

## Objection
"You're telling me to run the model that scores 26.00 on SWE-bench because it's fast; the leaderboard's best open coder is 75.80, so the honest answer is that local still means second-rate at coding."

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/openai/gpt-oss-120b | openai/gpt-oss-120b | primary | hermes web_extract | 2026-09-30 |
| 2 | https://ollama.com/library/gpt-oss:120b | gpt-oss:120b | docs | hermes web_extract | 2026-09-30 |
| 3 | https://github.com/ggml-org/llama.cpp/discussions/16578 | Performance of llama.cpp on NVIDIA DGX Spark #16578 | benchmark | hermes web_extract | 2026-09-30 |
| 4 | https://huggingface.co/bartowski/zai-org_GLM-4.5-Air-GGUF | bartowski/zai-org_GLM-4.5-Air-GGUF | primary | hermes web_extract | 2026-09-30 |
| 5 | https://huggingface.co/bartowski/MiniMaxAI_MiniMax-M2-GGUF | bartowski/MiniMaxAI_MiniMax-M2-GGUF | primary | hermes web_extract | 2026-09-30 |
| 6 | https://huggingface.co/bartowski/zai-org_GLM-4.5-GGUF | bartowski/zai-org_GLM-4.5-GGUF | primary | hermes web_extract | 2026-09-30 |
| 7 | https://www.swebench.com/ | SWE-bench | benchmark | hermes web_extract | 2026-09-30 |
| 8 | https://fireworks.ai/blog/best-llms-for-coding | Best LLMs for Coding (Fireworks) | benchmark | hermes web_extract | 2026-09-30 |
| 9 | https://artificialanalysis.ai/models/comparisons/glm-4-6-reasoning-vs-gpt-oss-120b-low | GLM-4.6 (Reasoning) vs gpt-oss-120b (low) | benchmark | hermes web_extract | 2026-09-30 |
| 10 | https://www.datacamp.com/blog/best-llm-for-coding | Best LLMs for Coding (DataCamp, September 2026 edition) | docs | hermes web_extract | 2026-09-30 |
| 11 | https://forums.developer.nvidia.com/t/building-local-hybrid-llms-on-dgx-spark-that-outperform-top-cloud-models/359569 | Building local hybrid LLMs on DGX Spark | community | hermes web_extract | 2026-09-30 |
| 12 | https://forums.developer.nvidia.com/t/dgx-spark-the-sovereign-ai-stack-dual-model-architecture-for-local-inference/ | DGX Spark: the sovereign AI stack | community | hermes web_extract | 2026-09-30 |
| 13 | https://sayob.com/blog/which-llms-run-on-dgx-spark/ | Which LLMs run on DGX Spark | community | hermes web_extract | 2026-09-30 |

## Notes
Tool family: hermes web_search + web_extract (no FireCrawl MCP connector in this session); 3 parallel research subagents, roughly 8 searches and 13 page fetches spent. Crowns conflict by harness (SWE-bench Verified vs AA Coding Index); the brief reports both and the script should say "depends which harness you ask" rather than crowning one. The sayob.com bandwidth figure (273 GB/s) is tier-4 and stays out of Key numbers. Reddit JSON returned 403 and was not fetched. The official llama.cpp dgx-spark.md results table was linked but not fetched; decode numbers come from replies inside discussion 16578.
