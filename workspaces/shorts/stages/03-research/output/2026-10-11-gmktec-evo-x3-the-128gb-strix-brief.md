---
slug: 2026-10-11-gmktec-evo-x3-the-128gb-strix
stage: 03-research
topic: "GMKtec EVO-X3: the 128GB Strix Halo local AI box versus the DGX Spark"
depth: standard
generated_at: 2026-10-11T17:55:00Z
sources: 12
hub: "[[videos/2026-10-11-gmktec-evo-x3-the-128gb-strix]]"
---

# Research brief: GMKtec EVO-X3, the 128GB Strix Halo local AI box

## Summary
The video's spine is a two-number decision: GMKtec's EVO-X3 puts the same 128GB on the desk as NVIDIA's DGX Spark for $3,799.99 versus $6,950.00, and the most arresting measurement is that the two boxes generate tokens at nearly the same speed (an owner's identical llama-bench on gpt-oss-120b: tg32 47.46 vs 56.33 tokens/s). The strongest concrete case: gpt-oss-120b at 59.02 GiB fits in the EVO-X3's 96GB GPU-allocatable pool and STH measured the box's Phi-4 14B run at 24.7 tokens per second. Could not be verified: any EVO-X3-specific gpt-oss-120b number and anything quotable from the Ask HN thread (2 points, 0 comments at fetch). Conflict: community throughput figures (NVIDIA forums, medium confidence) versus STH's Windows-only MLPerf suite -- neither measures the other's workload, so both are kept and flagged.

## Thesis
The EVO-X3 turns the 128GB local-AI purchase into a memory-versus-ecosystem call: Strix Halo buys Spark-class model capacity for $3,100 less and decode speed within about a fifth, while the Spark keeps CUDA and multiplies prompt processing.

## Explanation path

Open on the decision the viewer is actually making: which single box swallows the biggest open models, and what each gigabyte costs. Establish unified memory as the scarce resource before either machine appears -- model size in gigabytes is the wall, and both machines stand at 128GB of it. Then show the real split: Windows on Strix Halo allocates up to 96GB of that pool as GPU memory, while the Spark exposes one roughly 120GB unified pool, so both swallow a 59.02 GiB gpt-oss-120b with room to spare. Next the speed question, which is really a bandwidth question: 256 GB/s on Strix Halo against 273 GB/s on the Spark, about 7 percent apart, which is why measured token generation lands within about a fifth (tg32 47.46 vs 56.33 tokens/s, community llama-bench). Then the honest catch that redeems the Spark's price: token generation is the bandwidth-bound half, but prompt processing is compute-bound, and there the Spark runs roughly 2x-5x faster with CUDA behind it. Land on the decision rule: chat and budget point at the EVO-X3; long-context RAG, agentic loops and CUDA prototyping point at the Spark. Close with the physical caveat -- the 128GB is soldered, so the buyer lives with the choice.

## Claims
1. **The GMKtec EVO-X3 is a mini-PC built on AMD's Ryzen AI Max+ 395 (Strix Halo) with 128GB of soldered LPDDR5X-8000 and Radeon 8060S graphics with 40 compute units.**
   - Source: GMKtec EVO-X3 Mini-PC Review, https://www.servethehome.com/gmktec-evo-x3-mini-pc-review/
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "AMD Ryzen AI Max+ 395, 16C/32T (5.1GHz) ... 128GB LPDDR5X-8000, Soldered ... Radeon 8060S Graphics (40 CUs)"
2. **GMKtec's US store lists the EVO-X3 (128GB RAM + 2TB SSD config) at a sale price of $3,799.99, regular price $4,100.00.**
   - Source: GMKtec EVO-X3 AI Mini PC AMD Ryzen AI Max+ 395 - GMKtec, https://www.gmktec.com/products/gmktec-evo-x3-ai-mini-pc-amd-ryzen-ai-max-395
   - Tier: primary | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "Sale price $3,799.99 Regular price $4,100.00 ... DDR + SSD: 128GB RAM + 2TB SSD"
3. **Up to 96GB of the EVO-X3's unified memory can be allocated as GPU memory for local AI workloads.**
   - Source: GMKtec EVO-X3 AMD Ryzen AI Max+ 395 AI Mini PC, https://www.gmktec.uk/products/gmktec-evo-x3-amd-ryzen%E2%84%A2-ai-max-395-ai-mini-pc
   - Tier: primary | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "Up to 96GB can be allocated as GPU memory for local AI workloads"
4. **AMD's official blog states the Strix Halo platform's memory bandwidth as 256 GB/s.**
   - Source: AMD Ryzen AI MAX+ 395 Processor: Breakthrough AI Performance in Thin and Light, https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "powered by the integrated Radeon(TM) 8060S and taking full advantage of the 256 GB/s bandwidth"
5. **NVIDIA's DGX Spark product page specs memory bandwidth at 273 GB/s over a 256-bit LPDDR5x interface.**
   - Source: Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "Memory Interface: 256-bit ... Memory Bandwidth: 273 GB/s"
6. **NVIDIA's own marketplace lists the DGX Spark (GB10, 128GB, 4TB) at $6,950.00 and shows it Out of Stock.**
   - Source: Personal AI Supercomputers | DGX Systems for AI | NVIDIA, https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/?superchip=GB10&page=1&limit=15
   - Tier: primary | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "$6,950.00 [Out of Stock]"
7. **ServeTheHome measured the EVO-X3 on MLPerf Client v1.6.1 (Windows, OrtGenAI/DirectML) running the Phi-4 14B reasoning model at 24.7 tokens per second with a 1.46-second time to first token.**
   - Source: GMKtec EVO-X3 Mini-PC Review - Page 3, https://www.servethehome.com/gmktec-evo-x3-mini-pc-review/3/
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "the EVO-X3 and its Ryzen AI Max+ 395 chip average a rate of 24.7 tokens per second, with a TFT of just 1.46 seconds"
8. **ServeTheHome measured the DGX Spark's out-of-the-box Ollama at over 49 tokens per second on gpt-oss 20B and 14.48 tokens per second on gpt-oss 120B.**
   - Source: NVIDIA DGX Spark Review - Page 3, https://www.servethehome.com/nvidia-dgx-spark-review-the-gb10-machine-is-so-freaking-cool/3/
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "with OpenAI gpt-oss 20B we were often over 49 tokens/ second ... we can run big models like the gpt-oss 120B model and here we got 14.48 tokens per second"
9. **An owner who ran identical llama-bench commands on a 128GB Strix Halo box (GMKtec EVO-X2, same Ryzen AI Max+ 395 SoC) and a DGX Spark found gpt-oss-120b MXFP4 decode within about a fifth (tg32 47.46 vs 56.33 tokens/s) but prefill about 2x faster on the Spark (pp2048 1000.93 vs 1939.32 tokens/s), and summarized prompt processing as 2-5x higher on the Spark.**
   - Source: DGX Spark vs AMD Strix Halo - NVIDIA Developer Forums, https://forums.developer.nvidia.com/t/dgx-spark-vs-amd-strix-halo/348751
   - Tier: community | Confidence: medium | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "the token generation is nearly identical to Strix Halo both in llama.cpp and vllm, but prompt processing is 2-5x higher than Strix Halo"
10. **ServeTheHome notes Strix Halo systems under Windows split memory roughly 32GB CPU / 96GB GPU, while the DGX Spark exposes a single roughly 120GB unified pool instead.**
   - Source: NVIDIA DGX Spark Review - Page 3, https://www.servethehome.com/nvidia-dgx-spark-review-the-gb10-machine-is-so-freaking-cool/3/
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-11 | Via: web_extract
   - Quote: "we do not have to do a 32GB CPU, 96GB GPU split. Instead, we have a big 128GB pool"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | EVO-X3 price (128GB RAM + 2TB SSD, sale) | $3,799.99 | https://www.gmktec.com/products/gmktec-evo-x3-ai-mini-pc-amd-ryzen-ai-max-395 | "Sale price $3,799.99" |
| 2 | DGX Spark price (128GB, 4TB, NVIDIA marketplace) | $6,950.00 | https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/?superchip=GB10&page=1&limit=15 | "$6,950.00 [Out of Stock]" |
| 3 | Strix Halo memory bandwidth (AMD official) | 256 GB/s | https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html | "taking full advantage of the 256 GB/s bandwidth" |
| 4 | DGX Spark memory bandwidth (NVIDIA official) | 273 GB/s | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "Memory Bandwidth: 273 GB/s" |
| 5 | EVO-X3 GPU-allocatable memory | Up to 96GB | https://www.gmktec.uk/products/gmktec-evo-x3-amd-ryzen%E2%84%A2-ai-max-395-ai-mini-pc | "Up to 96GB can be allocated as GPU memory for local AI workloads" |
| 6 | EVO-X3 MLPerf Client Phi-4 14B reasoning | 24.7 tokens per second | https://www.servethehome.com/gmktec-evo-x3-mini-pc-review/3/ | "average a rate of 24.7 tokens per second, with a TFT of just 1.46 seconds" |

## Analogy candidates
- **Two delivery trucks on the same highway**: token generation is cruising speed, set by the highway (memory bandwidth, 256 vs 273 GB/s), so both trucks cruise within about a fifth of each other hauling the same 59GB trailer; the Spark's ~1 PFLOP engine only shortens the loading dock (prefill). Breaks when: a truck's bigger engine also raises top speed, while here the compute edge barely moves decode -- say "same speed limit" explicitly or the analogy misleads.
- **Soldered memory is an engine with a welded hood**: the 128GB pool is fixed at the factory like a sealed engine, so the RAM decision is permanent; the two M.2 bays are the only bays that open. Breaks when: extended to storage, which is upgradeable, not welded.

## Misconceptions
- Myth: 128GB of unified memory means 128GB of VRAM. Reality: the EVO-X3 allocates up to 96GB as GPU memory, and the Spark exposes a single roughly 120GB pool (claims 3 and 10).
- Myth: the Spark's up-to-1-PFLOP-FP4 compute makes chat much faster than Strix Halo. Reality: token generation is memory-bandwidth-bound (256 vs 273 GB/s, about 7 percent apart), and measured gpt-oss-120b decode sits within about a fifth; the compute pays out in prompt processing, 2-5x faster on the Spark (claims 4, 5, 9).

## Glossary
- **Strix Halo**: AMD's Ryzen AI Max+ 300-series halo chip pairing Zen 5 CPU cores with a Radeon 8060S iGPU and up to 128GB of unified LPDDR5X memory.
- **Unified memory**: one pool of RAM shared by CPU and GPU, so a model loads once instead of being copied into separate VRAM.
- **Memory bandwidth (GB/s)**: how fast weights can stream from memory each second; it caps tokens per second when the model is generating.
- **Tokens per second**: how many words-or-pieces the model emits each second while answering; the speed a viewer actually feels.
- **Prefill (prompt processing)**: the phase where the model reads your whole prompt at once; it is compute-bound, which is where the Spark pulls ahead.
- **Decode (token generation)**: the phase where the model writes the answer one token at a time; it is memory-bandwidth-bound, which is why the two boxes tie.
- **gpt-oss-120b**: an open mixture-of-experts model shipped in MXFP4 quantization at 59.02 GiB, small enough for both 128GB boxes.
- **OCuLink**: a cabled PCIe port on the EVO-X3 for attaching an external GPU, rarer than Thunderbolt on mini-PCs.

## Unverified
- No EVO-X3-specific gpt-oss-120b tokens-per-second measurement exists in the fetched pages; the tg32 47.46 figure is an EVO-X2 (same SoC) in an owner's forum post, and the EVO-X3's own number is STH's MLPerf Phi-4 14B on Windows.
- The Strix Halo tg32 47.46 row was partially reconstructed from a truncated forum table (community tier, medium confidence).
- The DGX Spark's street availability and price at non-NVIDIA retailers was not checked; only NVIDIA's marketplace listing ($6,950.00, Out of Stock) was fetched.
- The Ask HN thread "Best Local LLM Box?" (id 50039529) had 2 points and 0 comments when fetched, so it contributes no quotable recommendations.
- Historical DGX Spark launch prices ($3,999 or $4,999) could not be grounded in any fetched page.
- What the EVO-X3 does on Linux with ROCm rather than Windows DirectML was not measured in any fetched page.

## Suggested outline
1. Same desk, same 128GB, $3,100 apart: the EVO-X3 at $3,799.99 and the Spark at $6,950.00 both exist to swallow models no gaming GPU can hold.
2. What fits and how fast: up to 96GB of GPU memory versus a roughly 120GB unified pool (both hold the 59.02 GiB gpt-oss-120b), then the bandwidth tie -- 256 versus 273 GB/s -- and the measurements showing token generation within about a fifth.
3. The honest catch and the rule: prefill and CUDA are what the extra dollars buy (2-5x prompt processing), so chat-on-a-budget points at the EVO-X3 and long-context or CUDA work points at the Spark -- and the memory is soldered, so choose once.

## Viewer situation
You want one box on the desk that runs the biggest open models at home, you keep seeing 128GB machines, and the DGX Spark's $6,950 price tag makes you ask whether the mini-PC does the same job.

## Has process
false

## Objection
One forum owner's llama-bench table and a Windows-only MLPerf run are not review-grade cross-platform evidence, and none of it tells me what the EVO-X3 does on Linux with ROCm or how it holds up as context fills.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.servethehome.com/gmktec-evo-x3-mini-pc-review/ | GMKtec EVO-X3 Mini-PC Review Looking at a 128GB AMD Local AI Box | benchmark | web_extract | 2026-10-11 |
| 2 | https://www.servethehome.com/gmktec-evo-x3-mini-pc-review/3/ | GMKtec EVO-X3 Mini-PC Review - Page 3 | benchmark | web_extract | 2026-10-11 |
| 3 | https://www.gmktec.com/products/gmktec-evo-x3-ai-mini-pc-amd-ryzen-ai-max-395 | GMKtec EVO-X3 AI Mini PC AMD Ryzen AI Max+ 395 - GMKtec | primary | web_extract | 2026-10-11 |
| 4 | https://www.gmktec.uk/products/gmktec-evo-x3-amd-ryzen%E2%84%A2-ai-max-395-ai-mini-pc | GMKtec EVO-X3 AMD Ryzen AI Max+ 395 AI Mini PC | primary | web_extract | 2026-10-11 |
| 5 | https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html | AMD Ryzen AI Max+ 395 Processors | primary | web_extract | 2026-10-11 |
| 6 | https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html | AMD Ryzen AI MAX+ 395 Processor: Breakthrough AI Performance | primary | web_extract | 2026-10-11 |
| 7 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | Personal AI Supercomputer Powered by Blackwell - NVIDIA DGX Spark | primary | web_extract | 2026-10-11 |
| 8 | https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/?superchip=GB10&page=1&limit=15 | Personal AI Supercomputers - DGX Systems for AI - NVIDIA | primary | web_extract | 2026-10-11 |
| 9 | https://www.servethehome.com/nvidia-dgx-spark-review-the-gb10-machine-is-so-freaking-cool/3/ | NVIDIA DGX Spark Review - Page 3 | benchmark | web_extract | 2026-10-11 |
| 10 | https://www.servethehome.com/nvidia-dgx-spark-review-the-gb10-machine-is-so-freaking-cool/4/ | NVIDIA DGX Spark Review - Page 4 | benchmark | web_extract | 2026-10-11 |
| 11 | https://forums.developer.nvidia.com/t/dgx-spark-vs-amd-strix-halo/348751 | DGX Spark vs AMD Strix Halo - NVIDIA Developer Forums | community | web_extract | 2026-10-11 |
| 12 | https://news.ycombinator.com/item?id=50039529 | Ask HN: Best Local LLM Box ? | community | web_extract + hn.algolia.com items API | 2026-10-11 |

## Notes
Price grounding: the first research pass reported a $3,600-$3,800 band without a quote; the follow-up pass grounded the exact string ($3,799.99 sale, $4,100.00 regular, 128GB RAM + 2TB SSD) on GMKtec's US store, and the band was discarded. Bandwidth grounding: ServeTheHome's EVO-X3 review does not print a GB/s figure; the verbatim 256 GB/s comes from AMD's official blog, and the runaihome comparison page fetched in the same session corroborates 128GB @ 256 GB/s for Strix Halo-class boxes. Conflict kept: the llama-bench cross-machine numbers (claim 9) are community-tier and the EVO-X2 shares the EVO-X3's SoC but not its chassis or cooling; STH's EVO-X3 numbers are Windows MLPerf, not llama.cpp. The two measurements are kept separate and neither is averaged into the other.
