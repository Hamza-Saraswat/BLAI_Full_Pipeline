---
slug: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4
stage: 03-research
topic: "Nemotron 3.5 Super VL is NVFP4 only: what that means for local"
depth: standard
generated_at: 2026-10-18T11:38:24Z
sources: 9
hub: "[[videos/2026-10-18-nemotron-3-5-super-vl-is-nvfp4]]"
---

# Research brief: Nemotron 3.5 Super VL is NVFP4 only: what that means for local

## Summary
Thesis: the deploy-ready Nemotron 3.5 Super VL checkpoint is encoded in NVFP4, so the intended path is Blackwell hardware and everyone else re-routes through a GGUF re-quant. The most arresting number is the hardware gate itself: vLLM's docs require compute capability 10.0, Blackwell only, for NVFP4, while the weight-only W4A16 fallback path reaches back to Turing at 7.5. The strongest concrete case: NVIDIA's own card points local users on DGX Spark, RTX Spark, and RTX Pro 6000 to llama.cpp and Unsloth, whose GGUF ladder runs this model from 46.1 GB to 132 GB. Unverified: local tokens-per-second on any hardware, and any head-to-head quality claim between NVFP4 and GGUF Q4_K_M. Conflict: none material; the community conversion story (issue 15415, later fixed by PR 23629) refines but does not contradict the primary pages.

## Thesis
NVIDIA shipped Nemotron 3.5 Super VL with NVFP4 as the deploy-ready checkpoint, so the intended fast path runs on Blackwell machines like the DGX Spark and everyone else runs a GGUF re-quant built from the separate BF16 release instead.

## Explanation path
Open on the fact that carries the whole story: NVIDIA posted a 120B-parameter vision-language model whose ready-to-run checkpoint is encoded in NVFP4, a weight format only some NVIDIA GPUs can accelerate. Before any hardware talk, make NVFP4 concrete: every weight is stored in 4 bits, in blocks of 16 values that share one 8-bit scale factor, which is why the whole model fits in a 75 GB download. Then explain the catch: multiplying those 4-bit values at speed needs FP4 tensor cores, which exist only in NVIDIA's Blackwell generation (compute capability 10.0), the silicon inside a DGX Spark, an RTX PRO 6000, or a datacenter GB200. The model card itself names that hardware and the runtimes that serve the file, vLLM, SGLang, and TensorRT-LLM, and states the model runs W4A4 math on Blackwell but W4A16 elsewhere. Land the fork for the viewer: a Blackwell box serves the NVFP4 file as designed, while anything older, including a 24 GB gaming card, cannot use the format natively and needs a GGUF re-quant built from the separate BF16 release, which is what Unsloth publishes from 46.1 GB to 132 GB. Close on the honest catch: the quality delta between BF16 and NVFP4 is benchmark-specific, and a re-quant is different weights, not the same weights decompressed.

## Claims
1. **NVIDIA released Nemotron 3.5 Super VL on 10/15/2026 as a vision-language model with 120B total parameters and 12B active parameters, context lengths up to 1M tokens, under the OpenMDW-1.1 license, and the NVFP4 checkpoint is the deploy-ready release.**
   - Source: nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 model card, https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "It has **120B total parameters** and **12B active parameters** and supports context lengths up to **1M tokens**."
2. **NVFP4 stores each weight as 4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared FP8 scale per 16 value block, with a second-level FP32 scale per tensor, which NVIDIA says cuts the model memory footprint by approximately 3.5x relative to FP16 and approximately 1.8x compared to FP8.**
   - Source: Introducing NVFP4 for Efficient and Accurate Low-Precision Inference, https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/
   - Tier: docs | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "NVFP4 stores one 4-bit value plus minor overhead of one FP8 scale per 16 values (4.5 bits per value) and one FP32 per tensor second-level scaling factor. This reduces the model memory footprint by approximately 3.5x relative to FP16, and approximately 1.8x compared to FP8."
3. **The vLLM compression docs list NVFP4 as requiring Blackwell (SM100) GPUs with a minimum compute capability of 10.0, while the weight-only W4A16 scheme runs on Turing GPUs at compute capability 7.5 and up.**
   - Source: Choosing the right compression scheme (LLM Compressor Docs, vLLM), https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-scheme/
   - Tier: docs | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "NVFP4 | 4-bit NVIDIA floating point | Weights and activations | Blackwell (SM100) | 10.0" and "W4A16/W8A16 | 4 or 8 bit weights, 16-bit activations | Weights | Turing | 7.5"
4. **The model card's own deployment guidance for the NVFP4 checkpoint tops out at 1x DGX Spark, 1x H200, 2x H100, or 1x GB200, names vLLM, SGLang, and TensorRT-LLM as runtime engines, states inference uses W4A4 on Blackwell and W4A16 on non-Blackwell platforms, and points local users on DGX Spark, RTX Spark, and RTX Pro 6000 to llama.cpp and Unsloth.**
   - Source: nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 model card, https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "**Deployment** | 1× DGX Spark, 1× H200, 2× H100, or 1× GB200" ; "Inference uses W4A4 on Blackwell and W4A16 on non-Blackwell platforms, according to the serving configuration." ; "For Local inference on DGX Spark, RTX Spark, and RTX Pro 6000 you can find details on running the model through the following libraries: llama.cpp ... Unsloth"
5. **NVIDIA also publishes the BF16 reference weights of the same model, and their card lists deployment at 4x H100 or 2x GB200, hardware far beyond a consumer box, which makes BF16 the source for community re-quants rather than a local option.**
   - Source: nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 model card, https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
   - Tier: primary | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "**Deployment** | 4× H100 or 2× GB200"
6. **Unsloth publishes GGUF re-quants of this Nemotron spanning 46.1 GB (UD-IQ1_M) to 132 GB (Q8_0), with an NVFP4-flavored GGUF at 79 GB and UD-Q4_K_XL at 86.9 GB, sizes that fit a 128 GB unified-memory box and let llama.cpp-based tools run the model on non-Blackwell hardware.**
   - Source: unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF model card, https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "UD-IQ1_M 46.1 GB ... NVFP4 79 GB UD-Q4_K_XL 86.9 GB ... Q8_0 132 GB"
7. **As of 2026-10-18 the NVFP4 repository shows 7,599 downloads last month and 141 likes on Hugging Face, with repo storage of 75,049,013,059 bytes (about 75 GB) for the checkpoint a downloader actually pulls.**
   - Source: Hugging Face API record for the model, https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-10-18 | Via: curl
   - Quote: "downloads: 7599 ... likes: 141 ... usedStorage: 75049013059"
8. **NVIDIA's own benchmark table shows the NVFP4 checkpoint within a point of BF16 on most benchmarks (GPQA-Diamond 89.52 BF16 vs 89.90 NVFP4; SWE-bench Verified 71.10 vs 71.07) but down from 76.91 to 73.76 on MMLU-ProX, so the quantization cost is benchmark-specific, not uniform.**
   - Source: nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 model card, https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "GPQA-Diamond | 89.52 | 89.90" ; "MMLU-ProX | 76.91 | 73.76" ; "SWE-bench Verified | 71.10 | 71.07"
9. **llama.cpp contributors state you cannot just repackage NVFP4 quants into GGUF, because GGUF would need native NVFP4 support rather than a file conversion, so the everywhere-runnable quants are re-quantized from the BF16 weights instead.**
   - Source: llama.cpp issue 15415, https://github.com/ggml-org/llama.cpp/issues/15415
   - Tier: community | Confidence: medium | Accessed: 2026-10-18 | Via: web_extract
   - Quote: "You can't just \"repackage\" NVFP4 quants into GGUF. What you're asking here is basically \"support NVFP4 quantization natively for GGUF, similar to MXFP4\"."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total vs active parameters (Nemotron 3.5 Super VL) | 120B total parameters and 12B active parameters | https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 | "It has 120B total parameters and 12B active parameters" |
| 2 | maximum context length | Up to 1M tokens | https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 | "supports context lengths up to 1M tokens" |
| 3 | NVFP4 block structure | 4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared FP8 scale per 16 value block | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ | "4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared FP8 scale per 16 value block" |
| 4 | memory savings claimed by NVIDIA | approximately 3.5x relative to FP16, and approximately 1.8x compared to FP8 | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ | "reduces the model memory footprint by approximately 3.5x relative to FP16, and approximately 1.8x compared to FP8" |
| 5 | minimum vLLM compute capability for NVFP4 | 10.0 (Blackwell SM100) | https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-scheme/ | "NVFP4 ... Blackwell (SM100) ... 10.0" |
| 6 | NVFP4 checkpoint repo storage | 75,049,013,059 bytes (about 75 GB) | https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 | "usedStorage: 75049013059" |
| 7 | NVFP4-flavored GGUF size (Unsloth) | 79 GB | https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF | "NVFP4 79 GB" |
| 8 | Unsloth UD-Q4_K_XL GGUF size | 86.9 GB | https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF | "UD-Q4_K_XL 86.9 GB" |

## Analogy candidates
- **An appliance built for one country's power outlet**: the NVFP4 checkpoint is a device wired for a 240V outlet; in a house built for it (a Blackwell machine like the DGX Spark) it performs exactly as designed, anywhere else you need an adapter (a GGUF re-quant from the BF16 release) that lets it run but was never what the manufacturer benchmarked. Breaks when: a power adapter is cheap and changes nothing about the appliance, while a re-quant rebuilds the weights themselves and trades some quality for compatibility.
- **A native app versus an emulated port**: NVFP4 weights are a native build for Blackwell tensor cores; on older GPUs you run the port (GGUF), which works everywhere but none of the native build's speed optimizations transfer. Breaks when: emulation reproduces the exact same program, whereas re-quantization produces numerically different weights, not the same model slowed down.

## Misconceptions
- Myth: NVFP4 is just marketing shorthand for any 4-bit quant. Reality: NVFP4 is one specific encoding, 4-bit values in blocks of 16 sharing one FP8 (E4M3) scale plus a second-level FP32 scale per tensor, distinct from GGUF's Q4_K_M or generic INT4 (claim 2).
- Myth: You can convert the NVFP4 checkpoint to GGUF and run the same weights anywhere. Reality: llama.cpp contributors say you cannot just repackage NVFP4 quants into GGUF; the quants that run everywhere are re-quantized from the BF16 release, and that ladder spans 46.1 GB to 132 GB versus the about 75 GB NVFP4 repo (claims 6 and 9).
- Myth: 4-bit is 4-bit, so the quality cost is the same no matter which format or benchmark. Reality: NVIDIA's own table shows the cost is benchmark-specific: NVFP4 scores 89.90 vs BF16's 89.52 on GPQA-Diamond and 71.07 vs 71.10 on SWE-bench Verified, but drops MMLU-ProX from 76.91 to 73.76 (claim 8).

## Glossary
- **quantization**: Storing a model's weights in fewer bits so it takes less memory, at some cost in numerical precision.
- **NVFP4**: NVIDIA's 4-bit weight format that stores values in blocks of 16, each block sharing one 8-bit scale factor.
- **BF16**: The 16-bit format models are trained in; the full-precision reference weights a re-quant is built from.
- **GGUF**: The file format llama.cpp-based tools like LM Studio and Ollama load, with its own quantization levels such as Q4_K_M.
- **vision-language model**: A model that takes images and video as input alongside text and answers questions about them.
- **mixture of experts (MoE)**: A model design that keeps many specialist weights in memory but activates only a few of them for each token.
- **active parameters**: The subset of a mixture-of-experts model's weights actually used to produce each token, here 12B of 120B.
- **compute capability**: NVIDIA's version number for a GPU's feature set; NVFP4 acceleration needs 10.0, the Blackwell generation.
- **Blackwell**: NVIDIA's current GPU generation, including the DGX Spark's GB10 chip, RTX PRO 6000, and datacenter B200/GB200, whose tensor cores natively do 4-bit math.
- **KV cache**: The working memory a model builds up as it reads your prompt, which grows with context length and competes with weights for VRAM.

## Unverified
- Tokens per second and model load time for this model on a DGX Spark or any 24 GB card are unmeasured by us, and the model card publishes no first-party local throughput number.
- Reports that consumer RTX 50-series GPUs fall back to slower non-native kernels for NVFP4 mixture-of-experts checkpoints could not be grounded in a page fetched this session.
- No fetched page compares NVFP4 quality head-to-head against GGUF Q4_K_M on the same tasks, so the video must not claim one beats the other.
- Whether Ollama or LM Studio already list this model in their built-in catalogs was not checked this session.

## Suggested outline
1. Hook: NVIDIA's new 120B vision-language model landed this week in a format most GPUs cannot accelerate, 7,599 downloads already, and your card probably cannot run it as shipped.
2. What NVFP4 is and the hardware gate: 4 bits per weight in blocks of 16 sharing one 8-bit scale is how 120B shrinks to about 75 GB, and doing that math at speed needs FP4 tensor cores, Blackwell only (compute capability 10.0), exactly the machines the model card's deployment table names.
3. Your move plus the honest catch: a Blackwell box serves the NVFP4 file in vLLM, everyone else grabs a GGUF re-quant from the BF16 release (46.1 GB to 132 GB), knowing a re-quant is different weights and the BF16-to-NVFP4 deltas are benchmark-specific (MMLU-ProX 76.91 to 73.76).

## Viewer situation
You have a 24 GB gaming GPU or a 128 GB unified-memory box, you saw the Nemotron 3.5 Super VL release this week, and you are wondering whether the NVFP4 weights everyone is downloading will actually run on your machine.

## Has process
true
- Check your GPU's compute capability before downloading anything: 10.0 or newer (Blackwell) can accelerate NVFP4, older cards cannot.
- On a Blackwell box such as a DGX Spark or RTX PRO 6000, download the NVFP4 checkpoint and serve it with vLLM v0.32.0 or newer following the model card's recipe.
- On anything else, skip the NVFP4 repo and download a GGUF re-quant built from the BF16 release, picking the size your memory allows from 46.1 GB up to 132 GB.
- Load that GGUF in llama.cpp, LM Studio, or Ollama, and trim the context length until the model plus cache fits your memory.

## Objection
The GGUF ladder is not the model NVIDIA benchmarked: every re-quant from BF16 is a different set of weights, and without FP4 tensor cores you also lose the W4A4 fast path, so it running and it running as designed are two different claims.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 | nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 model card | primary | web_extract | 2026-10-18 |
| 2 | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ | Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | docs | web_extract | 2026-10-18 |
| 3 | https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-scheme/ | Choosing the right compression scheme (LLM Compressor Docs, vLLM) | docs | web_extract | 2026-10-18 |
| 4 | https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 | nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 model card | primary | web_extract | 2026-10-18 |
| 5 | https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF | unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF model card | primary | web_extract | 2026-10-18 |
| 6 | https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 | Hugging Face API record for the NVFP4 model | primary | curl | 2026-10-18 |
| 7 | https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/ | NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning | docs | web_extract | 2026-10-18 |
| 8 | https://github.com/ggml-org/llama.cpp/issues/15415 | Feature Request: convert_hf_to_gguf.py supports conversion of NVFP4 models | community | web_extract | 2026-10-18 |
| 9 | https://github.com/ggml-org/llama.cpp/discussions/23627 | Unsuccessful attempt at obtaining a working NVFP4 GGUF from a working NVFP4 model | community | web_extract | 2026-10-18 |

## Notes
Two fetched community pages (llama.cpp issue 15415 and discussion 23627) explain the conversion story: maintainers rejected mere repackaging, and a May 2026 PR (#23629) later fixed direct NVFP4 GGUF handling, which is why Unsloth can ship an NVFP4-flavored 79 GB GGUF today. The model card links a ggml-org llama.cpp collection for local runs, but that collection URL returned 404 when fetched, so llama.cpp support is grounded in the issue, the discussion, and the Unsloth card instead. The launch blog's over 600 tokens per second figure is a Baseten datacenter endpoint number, not local hardware, and should not be spoken as a local expectation. Downloads (7,599) are Hugging Face's last-month window as of 2026-10-18, not all-time.
