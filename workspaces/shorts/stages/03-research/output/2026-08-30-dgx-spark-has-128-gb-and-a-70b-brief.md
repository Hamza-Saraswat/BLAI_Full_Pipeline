---
slug: 2026-08-30-dgx-spark-has-128-gb-and-a-70b
stage: 03-research
topic: "DGX Spark has 128 GB and a 70B still crawls at 2.7 tokens/s"
depth: standard
generated_at: 2026-08-30T03:46:37Z
sources: 10
hub: "[[videos/2026-08-30-dgx-spark-has-128-gb-and-a-70b]]"
---

# Research brief: DGX Spark has 128 GB and a 70B still crawls at 2.7 tokens/s

## Summary

LMSYS measured Llama 3.1 70B (FP8) on a DGX Spark at 803 tps prefill and 2.7 tps decode: the box reads fast and writes slow, and the reason is arithmetic, not configuration. The most arresting number is 2.7 tps decode on hardware NVIDIA advertises for models up to 200 billion parameters. The strongest concrete case is the same 70B writing at 4.423 tok/s in q4_K_M on Ollama while GPT-OSS-120B, a larger MoE model, writes at 41.14. What could not be verified: the exact context settings behind LMSYS's 2.7 figure, and our own Spark has not re-run it. No true source conflicts; the 2.7 / 4.4 / ~6 tok/s spread across reviews is three different quant-and-runtime configurations of the same model class.

## Thesis

On a DGX Spark the 128 GB decides what loads, but the 273 GB/s of memory bandwidth decides how fast it talks: a dense 70B decodes at 2.7 tokens per second because every written token re-reads the weights, so the winning move is choosing models by active bytes per token, not parameter count.

## Explanation path

Open on the pair of facts that does not add up for new owners: the spec sheet's 128 GB of unified memory, and LMSYS's measured 803 tps prefill but 2.7 tps decode for Llama 3.1 70B (FP8) on the same box. Separate the two jobs first: reading a prompt happens all at once and is compute work, the Spark's 1 PFLOP FP4 strength; writing the answer happens one token at a time, and each token re-reads the model's weights from memory once, which makes single-stream decode bandwidth work. Then the arithmetic becomes the point: 273 GB/s divided by roughly 70 GB of FP8 weights gives a ceiling near 3.9 tok/s, and 2.7 measured is that ceiling with overhead, not a misconfiguration. The turn is that decode reads the active parameters, not the total: the same 70B at q4_K_M writes at 4.423 tok/s, GPT-OSS-120B (an MoE reading only a few billion active parameters per token) writes at 41 to 55 tok/s, and speculative decoding stacks further on a bandwidth-starved box. Land on the decision rule a buyer can reuse: on unified-memory hardware you shop by active bytes read per token, not by how many parameters fit.

## Claims

1. **LMSYS benchmarked Llama 3.1 70B (FP8) on the DGX Spark at 803 tps prefill and 2.7 tps decode.**
   - Source: NVIDIA DGX Spark In-Depth Review: A New Standard for Local AI Inference, https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/
   - Tier: benchmark | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "the Spark successfully ran **Llama 3.1 70B (FP8)** at **803 tps prefill / 2.7 tps decode**"
2. **The DGX Spark's memory is 128 GB LPDDR5x unified system memory on a 256-bit interface at 4266 MHz, delivering 273 GB/s of bandwidth shared by CPU and GPU.**
   - Source: Hardware Overview, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/hardware.html
   - Tier: primary | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth"
3. **NVIDIA advertises the DGX Spark as running AI development and testing workloads with models up to 200 billion parameters at the desktop.**
   - Source: Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "Run AI development and testing workloads with AI models up to 200 billion parameters at your desktop with a large, unified system memory."
4. **At small batch sizes each generated token requires passing all of the model's parameters through memory (two bytes per parameter at 16-bit), which makes single-user decode memory-bandwidth bound rather than compute bound.**
   - Source: Transformer Inference Arithmetic, https://kipp.ly/p/transformer-inference-arithmetic
   - Tier: community | Confidence: medium | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "There is 2⋅P because we need to pass all the parameters through the memory, and each parameter is two bytes."
5. **The single-stream decode ceiling on the Spark is simple arithmetic: max tokens/sec is memory bandwidth divided by bytes read per token, so a 70B model in FP8 (about 70 GB of weights) caps at 273 divided by 70, roughly 3.9 tok/s, with 2.7 to 3 tok/s in practice.**
   - Source: How fast is the DGX Spark, really? Prefill vs. decode, and the 273 GB/s wall, https://spark.enverge.ai/blog/dgx-spark-prefill-vs-decode
   - Tier: community | Confidence: medium | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "A 70B model in FP8 is about 70 GB of weights, so **273 ÷ 70 ≈ 3.9 tok/s** -- a hard ceiling, ~2.7–3 in practice."
6. **The same Llama 3.1 70B decodes at 4.423 tokens per second in q4_K_M on Ollama (firmware 580.95.05, Ollama v0.12.6), against 2.7 tps in FP8 on SGLang: harder quantization reads fewer bytes per token.**
   - Source: NVIDIA DGX Spark performance | Ollama Blog, https://ollama.com/blog/nvidia-spark-performance
   - Tier: benchmark | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "NVIDIA DGX Spark | llama3.1 | 70B | q4_K_M | 1.911k | 4.423"
7. **GPT-OSS-120B, a mixture-of-experts model in MXFP4, decodes at 41.14 tokens per second on Ollama on the same DGX Spark, faster than the dense 70B despite being the larger model, because decode reads only the active experts.**
   - Source: NVIDIA DGX Spark performance | Ollama Blog, https://ollama.com/blog/nvidia-spark-performance
   - Tier: benchmark | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "NVIDIA DGX Spark | gpt-oss | 120B | MXFP4 | 1.169k | 41.14"
8. **NVIDIA's own inference table (ISL 2048, OSL 128, batch size 1) records GPT-OSS-120B in MXFP4 on llama.cpp at 1725.47 tokens/sec prompt processing and 55.37 tokens/sec token generation on one DGX Spark.**
   - Source: How NVIDIA DGX Spark's Performance Enables Intensive AI Tasks, https://developer.nvidia.com/blog/how-nvidia-dgx-sparks-performance-enables-intensive-ai-tasks/
   - Tier: docs | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "GPT-OSS-120B | MXFP4 | llama.cpp | 1725.47 | 55.37"
9. **Prefill is the Spark's strength: LMSYS measured GPT-OSS 20B (MXFP4) at 2,053 tps prefill on the Spark against 10,108 tps on an RTX PRO 6000 Blackwell, a gap of roughly 4x that is the bandwidth limit showing up only where the workload is not already compute bound.**
   - Source: NVIDIA DGX Spark In-Depth Review: A New Standard for Local AI Inference, https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/
   - Tier: benchmark | Confidence: high | Accessed: 2026-08-30 | Via: web_extract
   - Quote: "the Spark achieved **2,053 tps prefill / 49.7 tps decode**, whereas the **RTX Pro 6000 Blackwell** reached **10,108 tps / 215 tps,** roughly **4× faster**"
10. **Exxact's engine comparison on the DGX Spark found a dense 70B drops to about 6 tok/s while a 120B-class MoE runs about 20 to 26 tok/s, concluding the box is bandwidth-bound and total size matters less than active parameter size.**
    - Source: Comparing Ollama, vLLM, DS4 on NVIDIA DGX Spark | Exxact Blog, https://www.exxactcorp.com/blog/deep-learning/comparing-inference-engines-on-dgx-spark
    - Tier: benchmark | Confidence: medium | Accessed: 2026-08-30 | Via: web_extract
    - Quote: "a 70B dense drops to ~6 tok/s, a 120B-class MoE runs ~20–26"

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | DGX Spark memory bandwidth | 273 GB/s | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "4266 MHz, 273 GB/s bandwidth" |
| 2 | DGX Spark unified system memory | 128 GB LPDDR5x | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "System Memory 128 GB LPDDR5x, coherent unified system memory" |
| 3 | Llama 3.1 70B (FP8) on SGLang, prefill / decode | 803 tps prefill / 2.7 tps decode | https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/ | "ran **Llama 3.1 70B (FP8)** at **803 tps prefill / 2.7 tps decode**" |
| 4 | Llama 3.1 70B (q4_K_M) on Ollama, decode | 4.423 tokens per second | https://ollama.com/blog/nvidia-spark-performance | "llama3.1 | 70B | q4_K_M | 1.911k | 4.423" |
| 5 | GPT-OSS-120B (MXFP4) on Ollama, decode | 41.14 tokens per second | https://ollama.com/blog/nvidia-spark-performance | "gpt-oss | 120B | MXFP4 | 1.169k | 41.14" |
| 6 | GPT-OSS-120B (MXFP4) on llama.cpp, generation (ISL 2048 / OSL 128, BS=1) | 55.37 tokens/sec | https://developer.nvidia.com/blog/how-nvidia-dgx-sparks-performance-enables-intensive-ai-tasks/ | "GPT-OSS-120B | MXFP4 | llama.cpp | 1725.47 | 55.37" |
| 7 | Single-stream decode ceiling, 70B in FP8 (about 70 GB of weights) | 273 / 70 = 3.9 tok/s | https://spark.enverge.ai/blog/dgx-spark-prefill-vs-decode | "273 ÷ 70 ≈ 3.9 tok/s" |
| 8 | DGX Spark AI compute at FP4 precision (with sparsity) | 1 PFLOP | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "Up to 1 PFLOP FP4" |

## Analogy candidates

- **A library with an enormous reading room and one narrow door**: the 128 GB is how many books fit in the room (what loads); the 273 GB/s is the width of the door (how fast volumes move); writing each token means carrying the whole active collection through the door once, so a dense 70B crawls while an MoE carrying a few shelves per token walks fast. Breaks when: serving is batched or the work is prefill-heavy, because many readers share one carry and the door stops being the constraint.
- **A pickup truck's payload bed versus its top highway speed**: capacity (128 GB) is what the bed holds, bandwidth (273 GB/s) is how fast the truck moves with that load; a 70B fits in the bed but the truck cannot cruise at chat speed with it. Breaks when: quantization shrinks the load itself, which no truck analogy covers; Q4 makes the same model lighter per token.

## Misconceptions

- Myth: 128 GB of unified memory means any model that fits will run well. Reality: capacity decides what loads; bandwidth decides how fast it talks, and a dense 70B that fits perfectly still decodes at 2.7 tps (claim 1).
- Myth: a 120B model must be slower than a 70B on the same box. Reality: GPT-OSS-120B (MoE, MXFP4) writes at 41.14 to 55.37 tok/s, ten to fifteen times the dense 70B, because decode reads only the active parameters per token (claims 7 and 8).
- Myth: 2.7 tok/s on a 70B means the Spark is misconfigured. Reality: it is the arithmetic ceiling of 273 GB/s divided by about 70 GB of FP8 weights, reproduced across SGLang benchmarks and owner forum reports (claim 5).

## Glossary

- **tokens per second (tok/s)**: how many chunks of text the model reads or writes per second; below roughly 10 tok/s a chat feels like watching someone type.
- **unified memory**: one pool of memory the CPU and GPU share, so huge models load without copying into a separate, smaller VRAM.
- **memory bandwidth**: how many gigabytes per second the chip can move between memory and compute; on the Spark it is 273 GB/s.
- **quantization**: storing each weight in fewer bytes (FP8 is 1 byte, Q4 about half a byte) so each token read moves fewer bytes, trading a little quality for speed.
- **mixture of experts (MoE)**: a model split into many expert subnetworks where only a few activate per token, so a 120B MoE may read only a few billion parameters' worth of weights per token.
- **prefill versus decode**: prefill reads your whole prompt at once (compute-bound, fast on the Spark); decode writes the answer one token at a time (bandwidth-bound, the Spark's weak spot).
- **speculative decoding**: a small draft model proposes several tokens that the big model verifies in one read, so accepted tokens cost almost no bandwidth.

## Unverified

- The exact context length and batch settings behind LMSYS's 2.7 tps decode figure for Llama 3.1 70B (FP8) are not stated in the passages read; the review lists models and backends but not per-run context.
- Owner reports on the NVIDIA developer forums of about 3 tok/s on dense 70B FP8 models are community posts; they corroborate but are not independent measurements.
- Our own DGX Spark has not re-run the 70B FP8 benchmark this week; a first-party measurement would replace the cited figures.
- Enverge's prefill claim of about 4x a Mac Studio M3 Ultra comes from a companion post not fetched this run.

## Suggested outline

1. LMSYS ran Llama 3.1 70B (FP8) on a DGX Spark: 803 tps reading your prompt, 2.7 tps writing the answer. Same box, same model, two speeds.
2. The 128 GB decides what loads; the 273 GB/s decides how fast it talks. Every written token re-reads the weights, and 273 divided by about 70 GB of FP8 weights is a ceiling near 3.9 tok/s.
3. What a token actually reads is the active parameters, not the total: the same 70B at Q4 writes at 4.4 tok/s, GPT-OSS-120B (an MoE) writes at 41 to 55. On this box you shop by active bytes per token, not parameter count.

## Viewer situation

You just unboxed a DGX Spark (or you are about to order one) and the first thing you want to run is the biggest model the 128 GB can hold, expecting cloud-chat speed.

## Has process

false

## Objection

Sure, FP8 on SGLang is slow, but Ollama already gets 4.4 tok/s on the same 70B and NVIDIA's table shows 55 on GPT-OSS-120B, so is the "wall" really a hardware limit or just a bad model choice?

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/ | NVIDIA DGX Spark In-Depth Review: A New Standard for Local AI Inference | benchmark | web_extract | 2026-08-30 |
| 2 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview, DGX Spark User Guide | primary | web_extract | 2026-08-30 |
| 3 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | Personal AI Supercomputer Powered by Blackwell | primary | web_extract | 2026-08-30 |
| 4 | https://developer.nvidia.com/blog/how-nvidia-dgx-sparks-performance-enables-intensive-ai-tasks/ | How NVIDIA DGX Spark's Performance Enables Intensive AI Tasks | docs | web_extract | 2026-08-30 |
| 5 | https://ollama.com/blog/nvidia-spark-performance | NVIDIA DGX Spark performance | benchmark | web_extract | 2026-08-30 |
| 6 | https://kipp.ly/p/transformer-inference-arithmetic | Transformer Inference Arithmetic | community | web_extract | 2026-08-30 |
| 7 | https://spark.enverge.ai/blog/dgx-spark-prefill-vs-decode | How fast is the DGX Spark, really? Prefill vs. decode, and the 273 GB/s wall | community | web_extract | 2026-08-30 |
| 8 | https://www.exxactcorp.com/blog/deep-learning/comparing-inference-engines-on-dgx-spark | Comparing Ollama, vLLM, DS4 on NVIDIA DGX Spark | benchmark | web_extract | 2026-08-30 |
| 9 | https://levelup.gitconnected.com/nvidia-dgx-spark-has-128gb-why-does-a-70b-llm-still-crawl-at-2-7-tokens-s-f06ce0ec169e | NVIDIA DGX Spark 70B LLM Performance Explained | community | web_extract | 2026-08-30 |
| 10 | https://nvidianews.nvidia.com/news/nvidia-puts-grace-blackwell-on-every-desk-and-at-every-ai-developers-fingertips | NVIDIA Puts Grace Blackwell on Every Desk and at Every AI Developer's Fingertips | primary | web_extract | 2026-08-30 |

## Notes

Cross-source consistency: 2.7 tps (LMSYS, SGLang FP8), 4.423 tok/s (Ollama, q4_K_M) and about 6 tok/s (Exxact, dense 70B, engine unspecified) are three different quantization and runtime configurations of the same model class, not disagreements; the video should name the config when it names a number. The Ollama blog calls the GB10's unified memory "120GB of VRAM", loose wording for the shared LPDDR5x pool; cite the NVIDIA docs for memory facts instead. NVIDIA's developer-blog table is batch-1 generation, matching the single-user scenario of this video. Source 9 is the Medium piece circulating the 2.7 figure this week; it attributes the measurement to LMSYS, so claims cite LMSYS directly.

## Decisions

- Checkpoint call (unattended): angle confirmed as picked, "bandwidth and quantization, not the 128 GB, decide Spark speed", slug confirmed 2026-08-30-dgx-spark-has-128-gb-and-a-70b; no picks.md swap exists for 2026-08-30, so the ideas-note order governs.
- Fan-out ran as 3 parallel research subagents per the blai-research skill; the three final reports were lost to provider API timeouts (90 s threshold) after their fetches completed, so the merge step read every fetched page from the session web cache and verified each quote above directly. All 10 sources were fetched this run via web_extract.
