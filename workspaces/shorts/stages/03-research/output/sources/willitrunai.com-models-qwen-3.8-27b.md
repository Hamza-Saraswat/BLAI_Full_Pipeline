# URL: https://willitrunai.com/models/qwen-3.8-27b
![Alibaba](https://willitrunai.com/logos/providers/qwen.svg)Alibaba

# Qwen3.8 27B

Frontier

[![huggingface](https://willitrunai.com/logos/providers/huggingface.avif)HuggingFace](https://huggingface.co/Qwen/Qwen3.8-27B)

7.5MDownloads18.7KLikesAug 2026Released262K tokensContextapache-2.0License81 StrongQuality

Qwen3.8 27B (27.8B parameters) needs about 21.9 GB of VRAM at Q4\_K\_M with a 16K-token context on an RTX 4090 24GB: 17.7 GB of weights, 1.0 GB of KV cache, 0.9 GB of runtime overhead and a 2.4 GB safety reserve. Verdict on that card: Tight fit (reserve intact).

Get started

— copy & paste to run locally

Copy-paste commands to run Qwen3.8 27B on your machine.

LM Studiollama.cpp

▶First time? Show install step

Run

`lms load Qwen3.8-27B && lms server start`Copy

Quick specs

Parameters27.8B

Architecturedense

Context262K tokens

Modalitytext+vision

Weights, smallest10.1 GB (Q2\_K)

Weights, rec.17.7 GB (Q4\_K\_M)

Licenseapache-2.0

FamilyQwen

✓Vision✓Code✓Chat✓Reasoning

About this model

Qwen3.8-27B brings the Qwen3.8 generation to a compact dense model that is natively vision-language, understanding images and video alongside text. It interleaves Gated DeltaNet and Gated Attention over 64 layers, supports 262,144 tokens natively, and lets thinking mode be toggled and tuned per request.

Related models

57 models in Qwen family

Your hardware

UnknownUAMD RDNA GPU

32 GB VRAM

A

Runs great on your hardware

4.9 tok/s decode · 168K context

This model fits, but memory bandwidth is the part holding decode speed back.

Prioritize bandwidth, not only capacity

Change

Inference speed

## Qwen3.8 27B inference speed — tokens per second by GPU & Mac

Estimated decode speed (tokens/sec) for Qwen3.8 27B at Q4\_K\_M across popular GPUs and Apple Silicon, using the fastest local runtime per device.Fastest is **RTX 5090 32GB at ~74 tok/s**. Speed is memory-bandwidth bound, so cards that fit the whole model in VRAM run far faster than ones that offload to system RAM.

| GPU / Mac | Memory | Quant | Speed (tok/s) | Fits? |
| --- | --- | --- | --- | --- |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 5090 32GB | 32 GB | Q4\_K\_M | 74.0 | Fits |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 4090 24GB | 24 GB | Q4\_K\_M | 42.0 | Tight (reserve intact) |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 3090 24GB | 24 GB | Q4\_K\_M | 38.5 | Tight (reserve intact) |
| AMDRX 7900 XTX 24GB | 24 GB | Q4\_K\_M | 33.5 | Tight (reserve intact) |
| AppleMacBook Pro M4 Max 128GB | 128 GB | Q4\_K\_M | 24.4 | Fits |
| AppleMacBook Pro M4 Max 64GB | 64 GB | Q4\_K\_M | 24.4 | Fits |
| AppleMac Studio M3 Ultra 256GB | 256 GB | Q4\_K\_M | 24.1 | Fits |
| AppleMac Studio M2 Ultra 128GB | 128 GB | Q4\_K\_M | 20.1 | Fits |
| AppleMac Studio M1 Ultra 128GB | 128 GB | Q4\_K\_M | 19.0 | Fits |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)NVIDIA DGX Spark 128GB | 128 GB | Q4\_K\_M | 13.810.4–16.2 · 32k ctx 10.1prefill ~270 tok/sEST. | Fits |
| AppleMacBook Pro M4 Pro 48GB | 48 GB | Q4\_K\_M | 12.2 | Fits |
| AppleMacBook Pro M3 Max 64GB | 64 GB | Q4\_K\_M | 10.4 | Fits |
| AMDAMD Ryzen AI Max+ 395 (Radeon 8060S) 128GB | 128 GB | Q4\_K\_M | 10.46.5–12.5 · 32k ctx 7.6prefill ~180 tok/sEST. | Fits |
| AppleMacBook Pro M1 Max 64GB | 64 GB | Q4\_K\_M | 9.5 | Fits |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 4080 Super 16GB | 16 GB | Q4\_K\_M | — | Too big |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 4070 12GB | 12 GB | Q4\_K\_M | — | Too big |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 3060 12GB | 12 GB | Q4\_K\_M | — | Too big |
| ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)RTX 4060 8GB | 8 GB | Q4\_K\_M | — | Too big |

DGX Spark, Strix Halo and clusters: how the ranges are built (0 public results)

Unified-memory boxes show typical decode (large), the min–max range across engines builds and settings, the typical speed with 32k tokens already in context, and prefill. With three or more public results from the last 9 months the typical value is their median; with one or two it is the newest result inside the formula range; with none it is the bandwidth formula (EST.). Older results are listed as legacy and do not move the number. Speculative decoding is never folded in. Cluster rows multiply the one-node range by a cited cluster factor (llama.cpp RPC never above 1×: it lets bigger models fit, it does not make a model that already fits any faster).

NVIDIA DGX Spark 128GB · Ollama

No public result for this model yet. The range is the bandwidth formula with the published efficiency band for this engine.

Up to ~2x with speculative decoding (EAGLE3 / MTP / drafter), workload-dependent. Never folded into the range.

AMD Ryzen AI Max+ 395 (Radeon 8060S) 128GB · llama.cpp (Vulkan RADV)

No public result for this model yet. The range is the bandwidth formula with the published efficiency band for this engine.

Estimates for single-stream decoding at Q4\_K\_M; real tokens/sec varies with prompt length, context, batch size, and runtime build. Prompt processing (prefill) is faster than the decode figures shown here.“—” means the model does not fit on that device, not even with RAM offload, so there is no speed to quote; “< 2” means it only runs from offload and is too slow to estimate.

Alternative engines

## Engines with self-reported speedups for Qwen3.8 27B

These engines publish their own speed claims. We list them only where the project says it runs, and we have not verified the numbers: they never change our estimates, ranges or rankings. [How we treat engine claims](https://willitrunai.com/why-it-works#engine-claims).

[TensorFold](https://github.com/ashhart/TensorFold) v1.0.11 · Apache-2.0 · MTP heads (Nemotron, Flash Next, GLM) and the DFlash2 drafter (Qwen3.8-27B) · exact (lossless) drafting

- TensorFold 1.0.11 (native Zig engine): Mac Studio M3 Ultra 96GB, Mac Studio M3 Ultra 256GB (mlx-4bit;qualified by the project, one node). [source](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/README.md#qualified-models)
- TensorFold 0.6.6 (Python engine, frozen): NVIDIA DGX Spark 128GB (mlx-4bit;supported, one node, or two in tensor parallel). [source](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/cuda.md#checkpoints)
- TensorFold 0.6.6 (Python engine, frozen): NVIDIA DGX Spark 128GB (nvfp4, exl3;supported, one node). [source](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/cuda.md#checkpoints)
- TensorFold 0.6.6 (Python engine, frozen): RTX PRO 6000 Blackwell Workstation Edition 96GB (nvfp4;supported, one node). [source](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/cuda.md#nvfp4-precision)

- [Self-reported](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/qwen3.8-27b.md#nvfp4-checkpoints "The engine project's own number, not verified by WillItRunAI. Opens the source.") TensorFold 0.6.6 claims 38.2–47.2 tok/s decode for Qwen3.8 27B at NVFP4 (nvidia/Qwen3.8-27B-NVFP4) on NVIDIA DGX Spark 128GB: 1.50–2.01x vLLM (MTP=3) at 23.4–25.8 tok/s.Not verified by WillItRunAI.

Drafting: DFlash2 drafter (z-lab/Qwen3.8-27B-DFlash2). One DGX Spark, tensorfold serve, 64 tokens, five seeds, medians; one stream. The table predates a later FP8 lane-matmul fix. Baseline: vLLM (version not stated; NVFP4 (same checkpoint)).Source read at commit c7137bb on 2026-10-14.

- [Self-reported](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/qwen3.8-27b.md#nvfp4-checkpoints "The engine project's own number, not verified by WillItRunAI. Opens the source.") TensorFold 0.6.6 claims 50–57.8 tok/s decode for Qwen3.8 27B at MLX 4-bit (TensorFold/Qwen3.8-27B-MLX-4bit) on NVIDIA DGX Spark 128GB: 1.97–2.47x vLLM (MTP=3) at 23.4–25.8 tok/s.Not verified by WillItRunAI.

Drafting: DFlash2 drafter (z-lab/Qwen3.8-27B-DFlash2). Same session as the NVFP4 row: one DGX Spark, 64 tokens, five seeds, medians, one stream. Baseline: vLLM (version not stated; NVFP4 (nvidia/Qwen3.8-27B-NVFP4)). The engine and the baseline did not run the same checkpoint (or the baseline's is not stated).Source read at commit c7137bb on 2026-10-14.

- [Self-reported](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/qwen3.8-27b.md#exl3-checkpoints-experimental "The engine project's own number, not verified by WillItRunAI. Opens the source.") TensorFold 0.6.6 claims 39.9–83.4 tok/s decode for Qwen3.8 27B at EXL3 3.00 bpw (turboderp/Qwen3.8-27B-exl3) on NVIDIA DGX Spark 128GB: 1.62–3.56x vLLM (MTP=3) at 23.4–25.8 tok/s.Not verified by WillItRunAI.

Drafting: DFlash2 drafter (z-lab/Qwen3.8-27B-DFlash2). One DGX Spark, the project's public benchmark command, medians of 15 runs a cell, one stream. Baseline: vLLM (version not stated; NVFP4 (the same vLLM figures as the NVFP4 table)). The engine and the baseline did not run the same checkpoint (or the baseline's is not stated).Source read at commit c7137bb on 2026-10-14.

- [Self-reported](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/cuda.md#nvfp4-precision "The engine project's own number, not verified by WillItRunAI. Opens the source.") TensorFold 0.6.6 claims 162–274 tok/s decode for Qwen3.8 27B at NVFP4 (nvidia/Qwen3.8-27B-NVFP4), checkpoint math on RTX PRO 6000 Blackwell Workstation Edition 96GB: 1.40–2.04x vLLM (MTP=3, --gpu-memory-utilization 0.29) at 116–151 tok/s.Not verified by WillItRunAI.

Drafting: DFlash2 drafter. One stream, 256-token replies, median of two passes, same weights and window (34,816 tokens) on both engines. At 8 concurrent streams TensorFold measured 0.72-0.93x vLLM; cold prompts 0.95-0.97x. Measured on the RTX PRO 6000 Blackwell Max-Q at a 250 W power limit, not the 600 W workstation card. Baseline: vLLM (version not stated; NVFP4 (same checkpoint)).Source read at commit c7137bb on 2026-10-14.

- [Self-reported](https://github.com/ashhart/TensorFold/blob/c7137bb31a7dad924fb541a7068422127b9a94b2/docs/recipes/qwen3.8-27b.md#historical-public-fixture-results "The engine project's own number, not verified by WillItRunAI. Opens the source.") TensorFold (historical build, version not stated) claims 58.9–82.4 tok/s decode for Qwen3.8 27B at MLX 4-bit (TensorFold/Qwen3.8-27B-MLX-4bit) on NVIDIA DGX Spark 128GB x2 (tensor parallel): 1.29–1.66x TensorFold (one rank, one Spark) at 45.8–49.6 tok/s.Not verified by WillItRunAI.

Drafting: DFlash2 drafter. Two DGX Sparks, tensor parallel (two ranks), NVIDIA pytorch:26.07-py3 container. The project labels these 'historical public-fixture results, not measurements of the merged 0.3.5 release'. Baseline is TensorFold itself on one Spark, not another engine. Baseline: TensorFold (same historical build; MLX 4-bit (same checkpoint)).Source read at commit c7137bb on 2026-10-14.


Planned: we will measure TensorFold on our ownRTX PRO 6000 Blackwell Workstation Edition 96GB (Qwen3.8 27B)against the baseline engine with the same prompts. No result yet.

Speed preview

Q2\_KQ3\_K\_SQ4\_K\_MQ5\_K\_MQ6\_KQ8\_0F16

Q4\_K\_M (Medium quality) — 22.7 GB VRAM needed, 4.9 tok/s estimated

See how fast it feelsQwen3.8 27B on AMD RDNA GPU

Two prompts — see the difference between cold start and warm inference

▶Play

Estimated: 4.9 tok/s decode · 1.7s TTFT (warm) · 288 tok/s prefill

Quick picks

[![Intel](https://willitrunai.com/logos/providers/intel.avif)\\
\\
Best budgetA\\
\\
Intel Arc Pro B60 24GB~$599 — 14 tok/s](https://willitrunai.com/can-run/qwen-3.8-27b-on-arc-pro-b60-24gb) [![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)\\
\\
Best overallS\\
\\
RTX 5090 32GB~$1,999 — 74 tok/s](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-5090-32gb)

Best hardware

## Top picks for Qwen3.8 27B

[![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)\\
\\
RTX 5090 32GBS\\
\\
32 GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-5090-32gb) [AMD\\
\\
AMD Instinct MI100 32GBS\\
\\
32 GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-instinct-mi100-32gb) [![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)\\
\\
RTX PRO 4500 Blackwell 32GBS\\
\\
32 GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-pro-4500-blackwell-32gb) [![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)\\
\\
NVIDIA A100 40GBS\\
\\
40 GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-a100-40gb) [![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)\\
\\
NVIDIA V100 32GBS\\
\\
32 GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-v100-32gb)

Run this model

[Qwen3.8 27B on RTX 5090 32GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-5090-32gb) [Qwen3.8 27B on AMD Instinct MI100 32GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-instinct-mi100-32gb) [Qwen3.8 27B on RTX PRO 4500 Blackwell 32GB](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-pro-4500-blackwell-32gb)

Quantization

## Qwen3.8 27B quantization — VRAM & quality by quant level

How much VRAM Qwen3.8 27B (27.8B) needs at each GGUF quant, and whether it fits a 24 GB card (RTX 4090 / 3090).The recommended **Q4\_K\_M** uses ~17.7 GB of VRAM for its weights — about **33% less** VRAM than Q8\_0, at a small quality cost.

| Quant | Bits | Weights in VRAM | Quality | Fits 24 GB? |
| --- | --- | --- | --- | --- |
| PTQ1\_0 | 1.75 | 5.6 GB | Low | No runtime |
| PQ2\_0 | 2.13 | 6.8 GB | Low | No runtime |
| Q1\_0\_G128 | 1.125 | 3.7 GB | Very Low | No runtime |
| Q2\_0\_G128 | 1.71 | 6.9 GB | Low | No runtime |
| Q2\_K | 2 | 10.1 GB | Low | Fits |
| Q3\_K\_S | 3 | 12.7 GB | Low | Fits |
| MXFP4 | 4 | 12.9 GB | Medium | No runtime |
| NVFP4 | 4 | 14.5 GB | Medium | No runtime |
| Q4\_K\_Mrecommended | 4 | 17.7 GB | Medium | Tight (reserve intact) |
| Q5\_K\_M | 5 | 19.5 GB | High | Tight (reserve intact) |
| Q6\_K | 6 | 22.2 GB | High | Offloads |
| Q8\_0 | 8 | 26.6 GB | Very High | Heavy offload |
| F16 | 16 | 53.0 GB | Maximum | Too big |

Weights only, counted the way the fit check and the memory breakdown count VRAM (binary GB, as cards report capacity), so a download looks bigger (the Q4\_K\_M file is 19.0 GB on disk). The total adds KV cache for your context, runtime overhead and a safety reserve: Q4\_K\_M at 16K context on anRTX 4090 24GB needs 21.9 GB in all.Lower quants trade quality for memory — Q4\_K\_M is the usual sweet spot; Q2/Q3 only when you must fit a bigger model.

Quality benchmarks

## Qwen3.8 27B benchmark scores

Benchmark verified

Reasoning

MMLU-Pro—

GPQA Diamond89.2%

MATH-500—

ARC Challenge—

Hardware compatibility

## Fit estimates across all hardware

[Open calculator](https://willitrunai.com/calculator)

| Grade | Hardware | Memory | Decode | Safe ctx |  |
| --- | --- | --- | --- | --- | --- |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 2060 6GB](https://willitrunai.com/gpus/rtx-2060-6gb) | 20/6 GB | 2 tok/soffload ~12.2 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-2060-6gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3050 8GB](https://willitrunai.com/gpus/rtx-3050-8gb) | 20/8 GB | 3.8 tok/soffload ~10.4 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3050-8gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3060 12GB](https://willitrunai.com/gpus/rtx-3060-12gb) | 21/12 GB | 5.4 tok/soffload ~6.8 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3060-12gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3060 Ti 8GB](https://willitrunai.com/gpus/rtx-3060-ti-8gb) | 20/8 GB | 4.3 tok/soffload ~10.4 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3060-ti-8gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3070 8GB](https://willitrunai.com/gpus/rtx-3070-8gb) | 20/8 GB | 4.4 tok/soffload ~10.4 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3070-8gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3080 10GB](https://willitrunai.com/gpus/rtx-3080-10gb) | 21/10 GB | 5.8 tok/soffload ~8.6 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3080-10gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3080 Ti 12GB](https://willitrunai.com/gpus/rtx-3080-ti-12gb) | 21/12 GB | 7 tok/soffload ~6.8 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3080-ti-12gb) |
| STight | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3090 24GB](https://willitrunai.com/gpus/rtx-3090-24gb) | 22/24 GB | 38.5 tok/s | 50K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3090-24gb) |
| STight | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 3090 Ti 24GB](https://willitrunai.com/gpus/rtx-3090-ti-24gb) | 22/24 GB | 42.1 tok/s | 50K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-3090-ti-24gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 4060 8GB](https://willitrunai.com/gpus/rtx-4060-8gb) | 20/8 GB | 4 tok/soffload ~10.4 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-4060-8gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 4060 Ti 16GB](https://willitrunai.com/gpus/rtx-4060-ti-16gb) | 21/16 GB | 7.4 tok/soffload ~3.2 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-4060-ti-16gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 4070 12GB](https://willitrunai.com/gpus/rtx-4070-12gb) | 21/12 GB | 6.1 tok/soffload ~6.8 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-4070-12gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 4070 Super 12GB](https://willitrunai.com/gpus/rtx-4070-super-12gb) | 21/12 GB | 6.3 tok/soffload ~6.8 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-4070-super-12gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 4070 Ti Super 16GB](https://willitrunai.com/gpus/rtx-4070-ti-super-16gb) | 21/16 GB | 11.5 tok/soffload ~3.2 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-4070-ti-super-16gb) |
| FNo fit | ![NVIDIA](https://willitrunai.com/logos/providers/nvidia.avif)[RTX 4080 Super 16GB](https://willitrunai.com/gpus/rtx-4080-super-16gb) | 21/16 GB | 12.1 tok/soffload ~3.2 GB RAM | 0K | [Details](https://willitrunai.com/can-run/qwen-3.8-27b-on-rtx-4080-super-16gb) |

Show all 199 hardware

Memory breakdown

## Reference: RTX 4090 24GB

Q4\_K\_M, 16K-token context, llama.cpp:21.9 GB of 24.0 GB. KV cache grows with context and the safety reserve scales with the card.

Weights17.7 GB

KV Cache1.0 GB

Runtime0.9 GB

Headroom2.4 GB

Frequently asked questions

## FAQ — Qwen3.8 27B

How much VRAM does Qwen3.8 27B need?

Qwen3.8 27B (27.8B parameters) needs about 21.9 GB of VRAM at Q4\_K\_M with a 16K-token context on an RTX 4090 24GB: 17.7 GB of weights, 1.0 GB of KV cache, 0.9 GB of runtime overhead and a 2.4 GB safety reserve. Verdict on that card: Tight fit (reserve intact). Longer contexts need more KV cache; lower quantizations use less memory but may reduce quality.

Can I run Qwen3.8 27B on a Intel Arc Pro B60 24GB?

Yes, Intel Arc Pro B60 24GB can run Qwen3.8 27B with a compatibility score of 82/100. It provides 24 GB of memory and achieves approximately 14.1 tokens per second.

What is the best quantization for Qwen3.8 27B?

The recommended quantization for Qwen3.8 27B is Q4\_K\_M, which offers the best balance between model quality and memory efficiency. Higher quantizations preserve more quality but require more VRAM.

What hardware is recommended for Qwen3.8 27B?

The top recommended hardware for Qwen3.8 27B: RTX 5090 32GB (score: 91/100), AMD Instinct MI100 32GB (score: 89/100), RTX PRO 4500 Blackwell 32GB (score: 89/100). These provide the best combination of memory, bandwidth, and compute for running this model locally.

Is Qwen3.8 27B good for reasoning?

Yes, Qwen3.8 27B is well-suited for reasoning as well as coding, agentic, vision, chat. It was designed with these use cases in mind.

See also

[Quantization Guide](https://willitrunai.com/docs#quantization) [Scoring Methodology](https://willitrunai.com/why-it-works) [VRAM Calculator](https://willitrunai.com/calculator)

Qwen3.8 27B

[Check your GPU](https://willitrunai.com/calculator)