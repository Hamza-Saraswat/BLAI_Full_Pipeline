---
slug: 2026-10-08-glm-5-3-flash-e224-runs-on-two
stage: 03-research
topic: "GLM 5.3 Flash E224 runs on two DGX Sparks"
depth: standard
generated_at: 2026-10-08T11:39:21Z
sources: 8
hub: "[[videos/2026-10-08-glm-5-3-flash-e224-runs-on-two]]"
---

# Research brief: GLM 5.3 Flash E224 runs on two DGX Sparks

## Summary
The idea the video lands: pruning plus 4-bit fitting does what quantization alone could not, and the proof is a runbook dated today. The most arresting number is 71.8 tok/s aggregate across eight streams (15.7 tok/s single-stream) on two desk-sized boxes. The strongest concrete case is the builder's deployment guide with exact usage token counts, both GPUs about 96% utilized, and a reproducible NCCL fix. What could not be verified: every accuracy score was measured on a B200, not on Spark hardware, and nothing on our own desk has measured this build yet. Conflict: the E224 card's table rules out the unpruned NVFP4 checkpoint on two Sparks, while an independent field report served it there anyway in August, capped at 24,576 tokens of context by a kernel bug.

## Thesis
A community build that prunes GLM-5.3-Flash to 224 experts per layer and quantizes the survivors to NVFP4 lands at 141 GiB, too big for one 128 GB DGX Spark and served by two ConnectX-7-linked Sparks at 15.7 tok/s single-stream.

## Explanation path
Open with the receipt, not the model: two small boxes on a desk serving GLM-5.3-Flash at conversation speed, with the numbers written down the same day. Establish what a DGX Spark is before any other fact, because every memory number in the video depends on it: 128 GB of unified LPDDR5x shared by CPU and GPU at 273 GB/s. Then show why one Spark fails: the build's 141 GiB of weights exceed 128 GB before the OS, CUDA graphs or any KV cache get a byte. Mixture of experts must be understood before the pruning story makes sense: GLM-5.3-Flash stores 288 routed experts per layer but consults only 8 per token, which is exactly why deleting rarely-routed experts is safe enough to try. The E224 build keeps 224 of 288 experts chosen by Neural Architecture Search and quantizes them to NVFP4, leaving 18 B active parameters per token unchanged, so the model stays as smart per token while its footprint drops from the unpruned NVFP4 build's roughly 190 GiB to 141 GiB. The second Spark then stops being magic: tensor parallelism over a ConnectX-7 QSFP link splits the weights about 70 GiB per node and leaves roughly 40 GiB per node for KV cache. Close on the measured trade and its honest edges: 15.7 tok/s single-stream and 71.8 tok/s eight-way, MTP speculative decoding measured slower on Spark and kept off, accuracy validated on a B200, and a single-Spark 2-bit or 3-bit GGUF path for viewers who stop at one box.

## Claims
1. **The E224 build keeps 224 of GLM-5.3-Flash's 288 routed experts per layer, selected by Neural Architecture Search, quantizes them to NVFP4, and still activates 18 B parameters per token.**
   - Source: autotrust/GLM5.3-Flash-E224-DGX-Spark, https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark
   - Tier: primary | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "It keeps 224 of the 288 routed experts in each layer by Neural Architecture Search (NAS), uses NVFP4 for the experts and still activates 18 B parameters per token."
2. **The E224 weights take 141 GiB (151.5 GB on disk), sized to fit two ConnectX-7-linked DGX Sparks with 256 GB of unified memory in total and room for long-context KV cache.**
   - Source: autotrust/GLM5.3-Flash-E224-DGX-Spark, https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark
   - Tier: primary | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "The weights take 141 GiB, which is small enough for two DGX Sparks connected by ConnectX-7 (256 GB of unified memory in total) with room left for long-context KV cache."
3. **A single DGX Spark cannot run the E224 build: its 128 GB unified memory is smaller than the 141 GiB of weights, so it needs two Sparks or a GPU with 180 GB or more.**
   - Source: autotrust/GLM5.3-Flash-E224-DGX-Spark, https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark
   - Tier: primary | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "It doesn't fit a single DGX Spark. The 128 GB unified memory is smaller than the 141 GiB of weights. You need two Sparks or a ≥180 GB GPU."
4. **The builder's deployment guide, measured 2026-10-08 on two ConnectX-7-linked Sparks running vLLM 0.31.0 with tensor parallelism 2 and fp8 KV cache, records single-stream decode of 15.7 tok/s and 8-way aggregate throughput of 71.8 tok/s with both GPUs about 96% utilized.**
   - Source: GLM-5.3-Flash-E224 on 2x NVIDIA DGX Spark -- Deployment & Operations Guide, https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark/raw/main/DEPLOY-2X-DGX-SPARK.md
   - Tier: primary | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "Measured (2026-10-08): single-stream 15.7 tok/s, 8-way aggregate 71.8 tok/s (exact usage token counts), both GPUs ≈96% utilized. Methodology in §8.2."
5. **NVIDIA's user guide specifies the Spark's memory as 128 GB LPDDR5x unified at 273 GB/s bandwidth and positions the machine for AI models up to 200 billion parameters, or 405B in a dual-Spark configuration.**
   - Source: Hardware Overview -- DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/hardware.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "Support for AI models up to 200 billion parameters (or 405B for dual-Spark configuration)"
6. **The smallest full-model path that fits one 128 GB machine is a low-bit GGUF: Unsloth's 3-bit UD-IQ3_XXS dynamic quant of GLM-5.3-Flash is 120.37 GB and fits 128 GB devices like a Mac or NVIDIA DGX Spark, while 1-bit runs on 100 GB.**
   - Source: GLM-5.3-Flash: How to Run Locally | Unsloth Documentation, https://unsloth.ai/docs/models/glm-5.3-flash
   - Tier: docs | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "The smallest 1-bit quant works on 100GB RAM while 3-bit works on 128GB devices like a Mac or NVIDIA DGX Spark." (quant table: "UD-IQ3_XXS ... 120.37")
7. **An independent two-Spark DeepSWE field report found the unpruned GLM-5.3-Flash NVFP4 decoded at 10 to 15 tokens per second and could only be served stably at 24,576 tokens of context because of a kernel bug in its serving stack, while DeepSeek V4 Flash served its full 1,048,576-token window at 41 to 66 tok/s on the same cluster.**
   - Source: GLM-5.3-Flash vs DeepSeek V4 Flash on 2x DGX Spark: Real-World DeepSWE Benchmark Results, https://flowtivity.ai/blog/glm-5-3-flash-vs-deepseek-v4-flash-dgx-spark-benchmark/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "GLM-5.3-Flash NVFP4 solved 0 of 5 tasks, never submitted a patch, decoded at 10 to 15 tokens per second, and could only be served stably at 24,576 tokens of context because of a kernel bug in its serving stack."
8. **GLM-5.3-Flash is Z.ai's first natively multimodal model in the GLM-5 series, with 320B total parameters and 18B active, built on a hybrid sparse and linear attention architecture.**
   - Source: zai-org/GLM-5.3-Flash, https://huggingface.co/zai-org/GLM-5.3-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-08 | Via: web_extract
   - Quote: "We introduce GLM-5.3-Flash, the first natively multimodal model in the GLM-5 series. With 320B total parameters and just 18B active parameters"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | single-stream decode, 2x Spark, vLLM 0.31.0 TP=2, fp8 KV cache | 15.7 tok/s | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark/raw/main/DEPLOY-2X-DGX-SPARK.md | "single-stream 15.7 tok/s" |
| 2 | 8-way aggregate decode, 2x Spark, same harness | 71.8 tok/s | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark/raw/main/DEPLOY-2X-DGX-SPARK.md | "8-way aggregate 71.8 tok/s (exact usage token counts)" |
| 3 | E224 weight footprint (NVFP4 experts) | 141 GiB | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark | "The weights take 141 GiB" |
| 4 | routed experts kept per layer, of 288 in the base model | 224 | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark | "It keeps 224 of the 288 routed experts in each layer" |
| 5 | active parameters per token (top-8 of 224) | 18 B | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark | "still activates 18 B parameters per token" |
| 6 | DGX Spark unified memory (GB10, LPDDR5x) | 128 GB | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "128 GB unified system memory" |
| 7 | DGX Spark memory bandwidth | 273 GB/s | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "273 GB/s bandwidth" |
| 8 | Unsloth UD-IQ3_XXS dynamic GGUF size, single-Spark path | 120.37 GB | https://unsloth.ai/docs/models/glm-5.3-flash | "UD-IQ3_XXS ... 120.37" |

## Analogy candidates
- **Vehicle**: laying off specialists, not cutting their pay. Mapping: GLM-5.3-Flash is a 288-person consultancy where every question goes to only 8 specialists; the E224 build lays off the 64 least-called specialists per department (chosen by NAS) and puts the rest on a 4-bit salary (NVFP4), so the firm moves into two small offices (two Sparks) while every question still reaches 8 specialists and costs the same 18 B parameters per token. Breaks when: a real layoff changes who answers; here quality stayed within noise only on the measured benchmarks, and GPQA-Diamond at low thinking effort did drop (about 78% versus low-80s for larger builds).
- **Vehicle**: furniture versus truck bed. Mapping: 141 GiB of weights is furniture, one Spark's 128 GB is a truck bed that also carries the OS and luggage (KV cache); no repacking (quantization alone) fit the unpruned build, so the builder threw out furniture (64 experts per layer) until two truck beds held it with room left. Breaks when: furniture is not re-read every second, but weights are; decode speed on Spark is set by the 273 GB/s bandwidth, not by whether the truck has space.

## Misconceptions
- Myth: Quantization alone put GLM-5.3-Flash on two DGX Sparks. Reality: The unpruned NVFP4 checkpoint at roughly 190 GiB leaves almost no KV room per node; the E224 build also prunes 64 of 288 experts per layer to buy back about 40 GiB of KV cache per node (claims 1, 2).
- Myth: Two linked Sparks behave like one 256 GB GPU, so any model under 256 GB fits. Reality: Each 128 GB node must hold its own share of weights, KV cache, CUDA graphs, the OS and the desktop; the field runbook had to drop the context target to 65536 tokens and gpu-memory-utilization to 0.72 because the model card's 163840 and 0.85 settings OOM-killed the worker during profiling (claims 2, 4).
- Myth: You need two Sparks to run GLM-5.3-Flash at all. Reality: Unsloth's 3-bit UD-IQ3_XXS GGUF at 120.37 GB runs on one 128 GB Spark (claim 6); the second Spark buys near-full-quality NVFP4 weights plus long-context KV headroom (claims 1, 2).

## Glossary
- **Quantization**: Storing model weights at lower numeric precision (4-bit, 3-bit, 2-bit) so they take less memory, at some cost in quality.
- **NVFP4**: NVIDIA's 4-bit floating-point weight format with 16-element groups and two levels of scaling, executed natively by Blackwell tensor cores like the Spark's.
- **Mixture of experts (MoE)**: A model design that stores many specialist sub-networks ("experts") but routes each token through only a few of them, so total size and per-token cost are different numbers.
- **Expert pruning**: Permanently deleting the experts the router rarely uses, shrinking memory footprint without changing per-token compute.
- **KV cache**: The memory that stores a conversation's keys and values so past tokens are not recomputed; it grows with context length and competes with weights for room.
- **Tensor parallelism**: Splitting one model's layers across multiple GPUs so each device holds part of the weights and the group acts as a single engine.
- **ConnectX-7**: The high-speed Smart NIC in each DGX Spark whose QSFP ports link two units into one cluster for tensor-parallel serving.
- **tok/s (tokens per second)**: How fast a model generates text; single-stream is one user's chat speed, aggregate is all concurrent users combined.

## Unverified
- No independent page confirms the build's Neural Architecture Search pruning method; it rests on the builder's own model card.
- Every accuracy number for the E224 build (GPQA-Diamond 90.9%, AIME 2025 88.3%, HumanEval 98.2%) was measured on a single B200, not on DGX Spark hardware.
- The roughly 40 GiB of free memory per node is calculated from the measured weight footprint, not measured on Spark hardware.
- Community reports of about 65 t/s decode for GLM-5.3-Flash on two Sparks were seen only in a search snippet and never fetched.
- Build Local AI has not measured this build on its own Sparks; every throughput figure here is the builder's or a third party's.

## Suggested outline
1. Cold open on the receipt: two desk-sized boxes serving GLM-5.3-Flash at 15.7 tok/s single-stream, 71.8 tok/s across eight streams.
2. Name the hardware: DGX Spark, 128 GB unified memory, 273 GB/s, and why unified memory is the whole game.
3. The wall: 141 GiB of weights versus 128 GB of memory, and the OS already lives there.
4. The fix in two moves: NVFP4 on the experts, then NAS pruning from 288 to 224 experts per layer with 18 B active parameters per token unchanged.
5. The second Spark and the cable: ConnectX-7 QSFP link, tensor parallelism, about 70 GiB of weights and 40 GiB of KV cache per node.
6. The honest catch: accuracy measured on a B200, MTP measured slower on Spark and left off, and the model card's own context settings had to be lowered in the field.
7. The viewer's decision: link a second Spark for near-full quality and long context, or stay on one box with the 120.37 GB 3-bit GGUF.

## Viewer situation
You have a DGX Spark on your desk and you keep hearing GLM-5.3-Flash is the model to run, but every recipe you find either needs two boxes or crushes it to 2 bits.

## Has process
true
- Connect the two Sparks with QSFP cables on the ConnectX-7 ports and follow NVIDIA's "Connect two Sparks" playbook for networking and passwordless SSH.
- Download autotrust/GLM5.3-Flash-E224-DGX-Spark to the same path on both nodes (about 158 GB).
- Create a Python venv on each node and install vllm==0.31.0 with transformers and ninja.
- Add a 64 GB swap file on each node and cap FlashInfer JIT parallelism with MAX_JOBS=2 to survive weight loading.
- Point NCCL's socket bootstrap at the management NIC and RDMA at the ConnectX-7 cards using NCCL_SOCKET_IFNAME and NCCL_IB_HCA.
- Launch vllm serve on the head node with --tensor-parallel-size 2 --nnodes 2, then the worker with --headless.
- Wait for the worker rendezvous line in the head log, then hit the health endpoint and send a test chat.

## Objection
Every number here comes from the builder's own runbook, the accuracy runs happened on a B200 rather than a Spark, and a 2-bit single-Spark GGUF already serves this model on one box -- so why should I buy and cable a second Spark for 15.7 tok/s?

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark | autotrust/GLM5.3-Flash-E224-DGX-Spark (Hugging Face) | primary | web_extract | 2026-10-08 |
| 2 | https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark/raw/main/DEPLOY-2X-DGX-SPARK.md | GLM-5.3-Flash-E224 on 2x NVIDIA DGX Spark -- Deployment & Operations Guide | primary | web_extract | 2026-10-08 |
| 3 | https://huggingface.co/zai-org/GLM-5.3-Flash | zai-org/GLM-5.3-Flash (Hugging Face) | primary | web_extract | 2026-10-08 |
| 4 | https://huggingface.co/autotrust/GLM-5.3-Flash-GGUF-DGX-Spark | autotrust/GLM-5.3-Flash-GGUF-DGX-Spark (Hugging Face) | primary | web_extract | 2026-10-08 |
| 5 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview -- DGX Spark User Guide | primary | web_extract | 2026-10-08 |
| 6 | https://build.nvidia.com/spark | Start Building AI Agents on DGX Spark (NVIDIA) | primary | web_extract | 2026-10-08 |
| 7 | https://unsloth.ai/docs/models/glm-5.3-flash | GLM-5.3-Flash: How to Run Locally (Unsloth Documentation) | docs | web_extract | 2026-10-08 |
| 8 | https://flowtivity.ai/blog/glm-5-3-flash-vs-deepseek-v4-flash-dgx-spark-benchmark/ | GLM-5.3-Flash vs DeepSeek V4 Flash on 2x DGX Spark: Real-World DeepSWE Benchmark Results (Flowtivity) | benchmark | web_extract | 2026-10-08 |

## Notes
Two conflicts the writer must not blend. (1) Internal to the build's own pages: the model card's quick start says --max-model-len 163840 with --gpu-memory-utilization 0.85, but the field-tested runbook says 163840 OOM-kills the worker during profiling on unified memory and runs 65536 at 0.72 with about 9.2 GiB of KV cache per node; the runbook is the receipt, the card is the aspiration, and the video should not quote the card's context settings as the achieved ones. (2) Across sources: the E224 card's table rules out the unpruned NVFP4 checkpoint on two Sparks (about 95 GiB per node, little KV room), while Flowtivity did serve that unpruned build there in August, capped at 24,576 tokens of context by a kernel bug; both are true at different times and serving stacks. Thin spot: all Spark-side throughput figures trace to the builder's pages (single runs, methodology in the runbook), and the only independent Spark measurement found (Flowtivity) covers the unpruned build, not E224. The companion GGUF card (source 4) gives the single-Spark contrast: 79.1 GiB at 2-bit with 256 experts, expected but not measured by its author at roughly 15-20 t/s single-stream.

## Decisions
- Checkpoint (angle + slug): angle confirmed as restated -- NAS-pruned E224, 141 GiB, two-Spark serving receipt, one Spark cannot hold it; slug 2026-10-08-glm-5-3-flash-e224-runs-on-two unchanged.
- Why: matches the ideas pick's angle and the keyword gap (nobody indexes the two-Spark deployment); no redirect signal in the hub note.
