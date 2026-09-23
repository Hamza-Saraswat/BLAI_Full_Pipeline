---
slug: 2026-09-23-best-coding-models-on-dgx-spar
stage: 03-research
topic: "Best coding models on DGX Spark: September 2026 (a ranked, model-by-model guide to which open coding models actually run best on an NVIDIA DGX Spark / GB10, 128 GB unified memory)"
depth: standard
generated_at: 2026-09-23T11:46:44Z
sources: 14
hub: "[[videos/2026-09-23-best-coding-models-on-dgx-spar]]"
---

# Research brief: Best coding models on DGX Spark, September 2026

## Summary
Thesis: on the 128 GB Spark the winning setup is two models, not one enormous one: a fast 3B-active coder for tight loops and a 27B thinker for hard code, while every model bigger than the box is a science project.
The most arresting number is 85 tokens per second of code generation from Qwen3-Coder-Next on a desk-sized box, immediately undercut by its 44.3 (vs 61.7) SWE-bench Pro score.
Strongest concrete case: the same 27B model on the same box went from a 22-second follow-up turn to 0.3 seconds purely from configuration, because agent turns resend a 23,000-token prompt every time.
Could not be verified: no first-party tokens-per-second figure for any model on the Spark exists anywhere, the stock driver version appears only in a community setup table, and Q2-quantization damage to GLM-5.3-Flash's coding quality is unmeasured.
Source conflict: one June forum post claims DGX OS runs 595 drivers while an August setup table lists driver 580.173.02 and the certified-595 request thread stays open; separately z.ai says GLM-5.3-Flash has 320B parameters and the Hugging Face card metadata says 321B.

## Thesis
On a DGX Spark in September 2026 the best local coding setup is not the biggest model that fits: an 80B mixture-of-experts coder flies at 85 tokens per second for tight loops, a 27B thinker scores 17 points higher when the code gets hard, and anything bigger than 128 GB of weights is a science project.

## Explanation path
Start with what the box actually is: one pool of 128 GB LPDDR5x that the CPU, the GPU and the operating system all share, feeding the GPU at 273 GB/s. That single fact drives everything else: it is why huge models fit at all, why the OS can starve when you hand the GPU too large a fraction (the survey lost zero boots at 0.80 and watched the OOM killer at 0.85), and why decode speed tracks how many bytes each token must read. Before any model is ranked, establish how a coding agent actually talks to a model, because a Claude-Code-style agent resends a 23,000-token repository prompt on every follow-up, so three numbers matter: decode speed, cold prefill, and warm turns served from a prefix cache. With that lens, the ranked list falls out as a per-task choice: Qwen3-Coder-Next (80B total, only 3B active) is the speed pick at 85 tokens per second; Qwen3.8-27B is the quality pick, scoring 61.7 vs 44.3 on SWE-bench Pro; GLM-5.3-Flash runs only as a 96.5 GB Q2 quant on the ds4 engine at 17.6 tok/s; DeepSeek V4.1 Flash does not fit at all (510 GB checkpoint vs about 121 GiB usable). Then land the platform-risk receipts as one beat: $4,999.99 street price against a $3,999 launch MSRP, a certified-driver request open since March, and an Ubuntu 26.04 path that is a hand-rolled forum recipe. Close on the equip: the box is no longer the bottleneck, configuration is.

## Claims
1. **The September 2026 survey's speed winner is Qwen3-Coder-Next on vLLM: with a GB10-calibrated NVFP4 checkpoint and a 1 GB EAGLE3 draft model it decoded at 85 tokens per second on code and prefilled a 21K-token repository context in under six seconds.**
   - Source: Coding models on DGX-Spark, state of the art of September 2026 | by Vito Rallo, https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "Holy-cow!!! 85 tokens per second on code, on a desk. A 21K-token repository context prefilled in under six seconds."
2. **The speed pick is not the quality pick: on SWE-bench Pro, the one coding benchmark both model cards report, Qwen3.8-27B scores 61.7 while Qwen3-Coder-Next scores 44.3, a 17-point gap.**
   - Source: Qwen/Qwen3.8-27B, https://huggingface.co/Qwen/Qwen3.8-27B
   - Tier: primary | Confidence: high | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "Agentic coding SWE-bench Pro 61.7 53.5 57.6 51.2 53.4" (benchmark table row, Qwen3.8-27B column first)
3. **Qwen3-Coder-Next is an open-weight coder with 80B parameters in total and 3B activated, a 262,144-token native context, an Apache-2.0 license, and it supports only non-thinking mode.**
   - Source: Qwen3-Coder-Next README (raw), https://huggingface.co/Qwen/Qwen3-Coder-Next/raw/main/README.md
   - Tier: primary | Confidence: high | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "license: apache-2.0 ... Number of Parameters: 80B in total and 3B activated ... Context Length: 262,144 natively"
4. **GLM-5.3-Flash has 320B total parameters with 18B activated, a 1M-token context window, and a 128K maximum output.**
   - Source: GLM-5.3-Flash/FlashX Overview, Z.AI developer docs, https://docs.z.ai/guides/vlm/glm-5.3-flash
   - Tier: primary | Confidence: high | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "GLM-5.3-Flash has 320B total parameters with 18B activated."
5. **On the Spark, GLM-5.3-Flash ran only through ds4 (antirez's small C inference engine) from a 96.5 GB Q2 GGUF: 17.6 tok/s of plain autoregressive decode with no speculative decoding yet, after a 14.3-second repack into 86.9 GiB of CUDA artifacts.**
   - Source: Coding models on DGX-Spark, state of the art of September 2026 | by Vito Rallo, https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "So 17.6 tok/s is plain autoregressive decode on a Q2 quant that eats three quarters of the box."
6. **DeepSeek V4.1 Flash is a no-go on one Spark: around 763B stored parameters, a 510 GB official checkpoint, and a smallest quant of 246 GiB (llama.cpp Q2_K) against about 121 GiB of usable memory, with community weight-streaming runs under 10 tok/s.**
   - Source: Coding models on DGX-Spark, state of the art of September 2026 | by Vito Rallo, https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "The Spark gives you about 121 GiB of usable memory. The smallest quant I found, llama.cpp's Q2_K, is 246 GiB, still twice that."
7. **What the box gives the models: 128 GB of LPDDR5x unified system memory on a 256-bit interface at 273 GB/s, up to 1 PFLOP at FP4 precision with sparsity, and NVIDIA's own docs frame support as AI models up to 200 billion parameters (405B for a dual-Spark configuration).**
   - Source: Hardware Overview, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/hardware.html
   - Tier: primary | Confidence: high | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "Memory | 128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth"
8. **The price receipt: on Sep 20, 2026 the cheapest DGX Spark actually available was $4,999.99 on Amazon (sold by Micro Center), NVIDIA's own $4,699 listing was out of stock, and the original launch price was $3,999.**
   - Source: DGX Spark prices are already climbing before RTX Spark mini PCs launch, VideoCardz, https://videocardz.com/newz/dgx-spark-prices-are-already-climbing-before-rtx-spark-mini-pcs-launch
   - Tier: docs | Confidence: high | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "The cheapest unit we found actually available is currently $4,999.99 on Amazon, sold by Micro Center and shipped by Amazon."
9. **The driver receipt: a thread asking when the 595.58.03 certified Linux-aarch64 display driver and CUDA 13.2 will ship for DGX Spark GB10 opened on NVIDIA's developer forums on March 25, 2026 and was still drawing replies with no NVIDIA answer as of September 22, 2026.**
   - Source: 595.58.03 Certified Linux-aarch64 (ARM64) Display Driver and CUDA 13.2 - when for DGX Spark GB10, NVIDIA Developer Forums, https://forums.developer.nvidia.com/t/595-58-03-certified-linux-aarch64-arm64-display-driver-and-cuda-13-2-when-for-dgx-spark-gb10/364688
   - Tier: community | Confidence: medium | Accessed: 2026-09-23 | Via: web_extract
   - Quote: "When for DGX Spark GB10, please? Many thanks!"
10. **The Ubuntu receipt: the visible Ubuntu 26.04 path on GB10 is a user's manual backup-and-reinstall recipe (Ubuntu 26.04 desktop ARM, driver 610, cuda-toolkit-13-3 hand-installed), not an NVIDIA-supported upgrade, and no vendor page fetched names an official Ubuntu 26.04 date.**
    - Source: Ubuntu 26.04 + drivers 610 + cuda-toolkit 13.3 + ZFS on GX10, NVIDIA Developer Forums, https://forums.developer.nvidia.com/t/ubuntu-26-04-drivers-610-cuda-toolkit-13-3-zfs-on-gx10/373655
    - Tier: community | Confidence: medium | Accessed: 2026-09-23 | Via: web_extract
    - Quote: "Finally managed to get fully working setup with Ubuntu 26.04 (clean of that DGX OS's bloatware) with newest drivers/cuda and ZFS."
11. **A fully documented single-Spark run of the 27B (unsloth NVFP4, 23.4 GB download, vLLM at --gpu-memory-utilization 0.45) still had 777,645 KV tokens of cache at full 262k context, on driver 580.173.02 with 121.63 GiB of unified memory.**
    - Source: Qwen3.8-27B-NVFP4 on a single DGX Spark, NVIDIA Developer Forums, https://forums.developer.nvidia.com/t/qwen3-8-27b-nvfp4-on-a-single-dgx-spark-up-to-1m-context-vllm-mtp-measurements/380244
    - Tier: benchmark | Confidence: medium | Accessed: 2026-09-23 | Via: web_extract
    - Quote: "Hardware | DGX Spark, GB10, 121.63 GiB unified memory, driver 580.173.02" and "That gives 777,645 KV tokens, 2.97x concurrency at full 262k context."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | fastest decode measured on a Spark (Qwen3-Coder-Next, vLLM + EAGLE3, code) | 85 tokens per second | https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9 | "85 tokens per second on code, on a desk" |
| 2 | SWE-bench Pro, Qwen3.8-27B (vendor, Claude Code harness) | 61.7 | https://huggingface.co/Qwen/Qwen3.8-27B | "Agentic coding SWE-bench Pro 61.7" |
| 3 | SWE-bench Pro, Qwen3-Coder-Next (vendor) | 44.3 | https://huggingface.co/Qwen/Qwen3-Coder-Next | "SWE Bench Pro 44.3" |
| 4 | DGX Spark memory bandwidth | 273 GB/s | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "273 GB/s bandwidth" |
| 5 | DGX Spark system memory | 128 GB LPDDR5x unified system memory | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth" |
| 6 | cheapest DGX Spark actually available (Amazon listing sold by Micro Center, seen 2026-09-20) | $4,999.99 | https://videocardz.com/newz/dgx-spark-prices-are-already-climbing-before-rtx-spark-mini-pcs-launch | "currently $4,999.99 on Amazon, sold by Micro Center" |
| 7 | DGX Spark original launch MSRP | $3,999 | https://videocardz.com/newz/dgx-spark-prices-are-already-climbing-before-rtx-spark-mini-pcs-launch | "the original $3,999 price announced for DGX Spark" |
| 8 | DeepSeek V4.1 Flash official checkpoint size | 510 GB | https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9 | "The official checkpoint is 510 GB." |

## Analogy candidates
- **Vehicle: one shared pantry with a narrow serving window.** Mapping: the 128 GB unified memory is a huge pantry the chef (GPU) and kitchen staff (CPU and OS) all share, but the serving window to the chef is only 273 GB/s wide, so how fast a dish comes out depends on how much each token makes the chef carry, which is why a 3B-active coder outruns a 27B dense model. Breaks when: a real pantry never gets seized by the wait staff, but on the Spark the OS will kill your model server if you hand the GPU too much of the pool.
- **Vehicle: a firm of 512 specialists where each question goes to about ten.** Mapping: a mixture-of-experts model keeps every specialist on salary (all 80B weights resident in memory) even though each token consults only a handful, so memory fills while compute stays cheap. Breaks when: a human firm can call a freelancer in per task, but streaming expert weights in from the SSD on demand is exactly the under-10-tok/s screensaver case.
- **Vehicle: a lawyer who must re-read the whole contract before every reply.** Mapping: an agent resends the 23,000-token prompt every turn; the prefix cache is the lawyer's memory of what she already read, and the difference between caching and not is 0.3 seconds vs 22 seconds on the follow-up. Breaks when: the cache only pays if the engine keeps it between turns, and one engine in the survey cached just 16,160 of about 22,600 possible tokens on turn two.

## Misconceptions
- Myth: The biggest model that fits in 128 GB is automatically the best coder for the box. Reality: the 80B Coder-Next is the fastest thing on the box at 85 tokens per second yet scores 44.3 on SWE-bench Pro against the 27B's 61.7, so the right model is a per-task choice (claims 1, 2, 3).
- Myth: 128 GB of unified memory works like 128 GB of VRAM. Reality: it is one pool shared with the CPU and the OS, running at 273 GB/s, so decode is bandwidth-limited and the OS's out-of-memory killer starts shooting processes if the GPU takes too large a fraction; the survey lost zero boots at 0.80 and saw kills at 0.85 (claims 5, 7 and the survey's memory-fraction rule).
- Myth: If the weights fit on disk, the model will run fine. Reality: DeepSeek V4.1 Flash's smallest quant is 246 GiB against about 121 GiB of usable memory, and the only single-box workarounds stream weights from the SSD at under 10 tok/s (claim 6).

## Glossary
- **quantization**: shrinking model weights to fewer bits each (4-bit NVFP4, 2-bit Q2) so they take less memory, at some cost in fidelity.
- **mixture of experts (MoE)**: a model design that stores many specialist weight blocks but activates only a few per token.
- **active parameters**: the subset of a model's weights actually used to produce one token, the number that drives speed.
- **tokens per second (tok/s)**: how fast a model generates text, measured in word-pieces; decode speed is the number everyone quotes.
- **prefill**: the work a model does reading your prompt before it writes the first word of the answer.
- **prefix cache**: a saved copy of work the engine already did on earlier turns, so a coding agent does not pay full prefill every follow-up.
- **KV cache**: the per-conversation memory of tokens already processed that the model reuses as context grows.
- **unified memory**: one pool of RAM shared by the CPU, the GPU and the operating system, instead of separate system RAM and VRAM.
- **speculative decoding**: a small draft model guesses several tokens and the big model checks them all in one pass, trading compute for speed.

## Unverified
- No first-party tokens-per-second measurement for any of these models on DGX Spark exists; every speed number in this brief is one survey author or one forum author on nightly builds the author himself says expires in days.
- The exact stock DGX OS driver version could not be grounded in an NVIDIA page; a community setup table lists driver 580.173.02 on GB10 as of Aug 14, 2026.
- What 2-bit (Q2) quantization does to GLM-5.3-Flash's coding quality is unmeasured; the survey measured speed only and explicitly ran no quality evals.
- Whether the $4,999.99 street price holds after RTX Spark systems launch in October 2026 is unknown.
- NVIDIA's own listed $4,699 price could not be checked against NVIDIA's marketplace directly because the marketplace listing was out of stock at fetch time.

## Suggested outline
1. Open on the arrest: 85 tokens per second of code generation from a box the size of a hardcover, then the catch that the model doing it scores 44.3, not 61.7, on SWE-bench Pro, and set the hardware in one line (128 GB shared pool, 273 GB/s).
2. The ranked list carried by one worked example, the agent turn that resends a 23,000-token repository prompt every follow-up: Qwen3-Coder-Next for speed (80B total, 3B active, Apache 2.0), Qwen3.8-27B for hard code (61.7 SWE-bench Pro, sub-second warm turns when configured right, 22 s vs 0.3 s on the same box), GLM-5.3-Flash only as a 96.5 GB Q2 science project on ds4 at 17.6 tok/s, and DeepSeek V4.1 Flash not at all (510 GB checkpoint vs about 121 GiB usable).
3. The receipts beat, all three in one breath: $4,999.99 street price against a $3,999 launch MSRP, the certified-595-driver ask open since March 25 with no answer, and Ubuntu 26.04 as a hand-rolled forum recipe, closing on the equip: the box is no longer the bottleneck, your configuration is.

## Viewer situation
You run coding agents against a chat API every day, you have been eyeing a DGX Spark to bring that work home, and this month's model drops have you wondering whether one $5,000 box can replace the tab.

## Has process
false

## Objection
Every speed number here is one reviewer on nightly builds that he says expire in days, the quality scores are vendor-reported rather than independently reproduced, and the box itself just jumped to $4,999.99 street price with its driver stack stuck waiting on NVIDIA.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9 | Coding models on DGX-Spark, state of the art of September 2026 (Vito Rallo, Medium) | benchmark | web_extract | 2026-09-23 |
| 2 | https://huggingface.co/Qwen/Qwen3.8-27B | Qwen/Qwen3.8-27B model card | primary | web_extract | 2026-09-23 |
| 3 | https://huggingface.co/Qwen/Qwen3-Coder-Next | Qwen/Qwen3-Coder-Next model card | primary | web_extract | 2026-09-23 |
| 4 | https://huggingface.co/Qwen/Qwen3-Coder-Next/raw/main/README.md | Qwen3-Coder-Next README (raw) | primary | web_extract | 2026-09-23 |
| 5 | https://huggingface.co/zai-org/GLM-5.3-Flash | zai-org/GLM-5.3-Flash model card | primary | web_extract | 2026-09-23 |
| 6 | https://docs.z.ai/guides/vlm/glm-5.3-flash | GLM-5.3-Flash/FlashX Overview (Z.AI docs) | primary | web_extract | 2026-09-23 |
| 7 | https://z.ai/blog/glm-5.3-flash | GLM-5.3-Flash: Frontier Intelligence, Flash Cost (Z.ai blog) | primary | web_extract | 2026-09-23 |
| 8 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview, DGX Spark User Guide | primary | web_extract | 2026-09-23 |
| 9 | https://videocardz.com/newz/dgx-spark-prices-are-already-climbing-before-rtx-spark-mini-pcs-launch | DGX Spark prices are already climbing before RTX Spark mini PCs launch (VideoCardz, Sep 20, 2026, byline WhyCry) | docs | web_extract | 2026-09-23 |
| 10 | https://forums.developer.nvidia.com/t/595-58-03-certified-linux-aarch64-arm64-display-driver-and-cuda-13-2-when-for-dgx-spark-gb10/364688 | 595.58.03 Certified Linux-aarch64 Display Driver and CUDA 13.2 - when for DGX Spark GB10 (NVIDIA Developer Forums) | community | web_extract | 2026-09-23 |
| 11 | https://forums.developer.nvidia.com/t/ubuntu-26-04-drivers-610-cuda-toolkit-13-3-zfs-on-gx10/373655 | Ubuntu 26.04 + drivers 610 + cuda-toolkit 13.3 + ZFS on GX10 (NVIDIA Developer Forums) | community | web_extract | 2026-09-23 |
| 12 | https://forums.developer.nvidia.com/t/qwen3-8-27b-nvfp4-on-a-single-dgx-spark-up-to-1m-context-vllm-mtp-measurements/380244 | Qwen3.8-27B-NVFP4 on a single DGX Spark, up to 1M context, vLLM+MTP measurements (NVIDIA Developer Forums) | benchmark | web_extract | 2026-09-23 |
| 13 | https://qwen.ai/blog?id=qwen3-coder-next | Qwen3-Coder-Next: Pushing Small Hybrid Models on Agentic Coding (Qwen blog) | primary | web_extract | 2026-09-23 |
| 14 | https://github.com/QwenLM/Qwen3-Coder | QwenLM/Qwen3-Coder repository README | primary | web_extract | 2026-09-23 |

## Notes
- Driver-state conflict: a June 17 forum post says llama.cpp speed "is about same as DGX OS+595 drivers+13.3 cuda", while the later and more specific Aug 14 setup table lists driver 580.173.02 and the certified-595 request thread was still open on Sep 22; I trust the later table plus the open thread, and the exact stock driver version stays under Unverified.
- Parameter rounding conflict: z.ai and the Z.AI docs state GLM-5.3-Flash has 320B total parameters; the Hugging Face card metadata says "321B params". The brief uses the vendor docs figure (320B) and flags the discrepancy here rather than averaging.
- All Spark speed numbers come from two independent authors (the survey and the forum measurements) on nightly builds; the survey itself warns "these numbers have a shelf life measured in days", so the script should date-stamp any speed claim.
- 14 pages were fetched against the standard band of 8-12 because the Apache-2.0 license fact, the raw model card, and both halves of the driver story each needed their own primary fetch; four of the fourteen (Qwen blog, GitHub README, Z.ai blog, HF GLM card) serve only as corroboration and are cited by no claim.
