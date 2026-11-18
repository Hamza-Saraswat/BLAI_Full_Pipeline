---
slug: 2026-11-18-deepseek-v4-pro-nvfp4-which-gp
stage: 03-research
topic: "DeepSeek V4 Pro NVFP4: which GPUs can load it"
depth: standard
generated_at: 2026-11-18T12:41:34Z
sources: 12
hub: "[[videos/2026-11-18-deepseek-v4-pro-nvfp4-which-gp]]"
---

# Research brief: DeepSeek V4 Pro NVFP4: which GPUs can load it

## Summary
The video lands one piece of arithmetic: the 4-bit cut of DeepSeek V4 Pro still weighs 941139951818 bytes on disk, so "4-bit" decides nothing about fitting on a gaming card. The most arresting number is that checkpoint size, about 941.1 GB, which is roughly ten of the biggest single desktop GPU NVIDIA sells (96 GB GDDR7) and about 7.4 times a 128 GB DGX Spark; the strongest concrete case is that a 512 GB Mac Studio with M5 Ultra is the only shipping single-board machine that clears the weights alone, before any conversation memory. What could not be verified: no independent measured tokens-per-second exists for this checkpoint on any tier, and no fetched page shows llama.cpp, Ollama or LM Studio loading this exact safetensors build. One conflict to handle honestly: NVIDIA's model card validates only on 8x B200, while vLLM's own docs say NVFP4 checkpoints also load on older GPUs with slower weight-only kernels, and community threads report rejections on workstation-class Blackwell (SM120) into mid-2026.

## Thesis
DeepSeek V4 Pro in NVFP4 is still a 941 GB download that no single consumer GPU can load, because 4-bit shrinks the model, not the tier of hardware it needs.

## Explanation path
Start from what the viewer already does: download a model and watch it fill video memory, so "will it fit" is a byte count, not a vibe. Define quantization in one move: every weight stored in 4 bits instead of 16 or 8, so the file shrinks roughly fourfold, at some risk to quality. Then the detail most viewers miss: DeepSeek V4 Pro is a mixture-of-experts model, and although only 49B of its 1.65T parameters fire per token, every expert must sit in memory before the first token moves, so the memory ticket is the full parameter count times the storage format, not the active count. With that habit installed, read the actual number off the repo page: 941139951818 bytes across 66 safetensors shards, plus KV cache (the model's running memory of the conversation, which grows with context up to a 1 million token maximum) on top. Now the tier ladder writes itself: 24 GB and 32 GB gaming cards are not in the conversation; 96 GB (one RTX PRO 6000 Blackwell) holds about a tenth of the weights; 128 GB unified (DGX Spark) about a seventh; 512 GB unified (Mac Studio M5 Ultra) is the first single board that clears the weights alone. Only then deliver the catch the title promises: NVFP4 is not a plain Q4 GGUF. It reuses the same 4-bit weight grid the base model already ships in, but stores finer correction scales (one FP8 scale per 16 values), which is why the file is slightly larger than its MXFP4 source; its fast path wants Blackwell datacenter tensor cores (vLLM lists minimum compute capability 10.0), with slower weight-only kernels as the fallback on older GPUs; and the quality story is nearly flat, GPQA Diamond moving 88.51 to 88.42 on NVIDIA's own table. Land on the decision: know your memory tier and your runtime before committing to a terabyte-scale download, because the format name tells you nothing about fit.

## Claims
1. **DeepSeek-V4-Pro-0813-NVFP4 is NVIDIA's NVFP4 re-quantization of a Mixture-of-Experts model with 1.65T parameters in total and 49B activated per token.**
   - Source: nvidia/DeepSeek-V4-Pro-0813-NVFP4 model card, https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "**Number of Model Parameters:** 1.65T in total and **49B** activated"
2. **The checkpoint's files occupy 941139951818 bytes (about 941.1 GB, or 876.5 GiB) across 66 safetensors shards, 65 of them 14.7 GB each.**
   - Source: Hugging Face model API, nvidia/DeepSeek-V4-Pro-0813-NVFP4, https://huggingface.co/api/models/nvidia/DeepSeek-V4-Pro-0813-NVFP4?blobs=true
   - Tier: primary | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "\"usedStorage\":941139951818" (siblings list runs through "model-00066-of-00066.safetensors"; the tree page lists 65 shards at "14.7 GB")
3. **NVIDIA's model card lists SGLang and vLLM as the only supported runtime engines and NVIDIA Blackwell B200 as the supported hardware, with the vLLM configuration validated on 8x B200 with tensor parallel size 8.**
   - Source: nvidia/DeepSeek-V4-Pro-0813-NVFP4 model card, https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "This configuration was validated on 8xB200 (TP=8) against this checkpoint with both `vllm/vllm-openai:v0.27.1` and `v0.28.0`"
4. **NVFP4 is a 4-bit floating-point format introduced with the NVIDIA Blackwell architecture, storing 4-bit values with a fine-grained E4M3 FP8 scaling factor per 16-value micro-block.**
   - Source: Introducing NVFP4 for Efficient and Accurate Low-Precision Inference, NVIDIA Technical Blog, https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/
   - Tier: docs | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "This strategy applies a fine-grained E4M3 scaling factor to each 16-value _micro-block_, a compact subset of the larger tensor, while also leveraging a second-level FP32 scalar applied per tensor."
5. **vLLM's compression docs put NVFP4's hardware-accelerated tier at Blackwell (SM100) with minimum compute capability 10.0, and state that NVFP4 checkpoints also load on older GPUs (Ampere and newer) using weight-only Marlin kernels with 16-bit activations, giving the memory savings without the activation speedup.**
   - Source: Choosing the right compression scheme, LLM Compressor Docs (vLLM project), https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-scheme/
   - Tier: docs | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "NVFP4, MXFP4 and MXFP8 checkpoints also load on older GPUs (Ampere and newer). There vLLM uses weight-only Marlin kernels and keeps activations in 16-bit, so you get the memory savings without the activation speedup."
6. **On NVIDIA's own evaluation table the NVFP4 build scores within a fraction of a point of its MXFP4 source, GPQA Diamond 88.51 versus 88.42, while one agentic benchmark moves up (96.49 to 98.25 on Tau-squared Bench Telecom).**
   - Source: nvidia/DeepSeek-V4-Pro-0813-NVFP4 model card, https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "| MXFP4 (source) | **88.51** | **68.67** | **96.49** | **53.45** | **76.53** | **51.39** |" and "| NVFP4 | **88.42** | **69.33** | **98.25** | **53.75** | **75.68** | **50.69** |"
7. **The biggest single desktop GPU NVIDIA sells, the RTX PRO 6000 Blackwell Workstation Edition, carries 96 GB of GDDR7 memory.**
   - Source: RTX PRO 6000 Blackwell Workstation Edition, NVIDIA, https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/
   - Tier: primary | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "| Memory Configuration | 96 GB GDDR7 with error-correcting code (ECC) |"
8. **A Mac Studio with M5 Ultra configures up to 512GB of unified memory, the only shipping single-board machine in this brief whose memory clears the checkpoint's 941139951818 bytes on its own.**
   - Source: Mac Studio Technical Specifications, Apple, https://www.apple.com/mac-studio/specs/
   - Tier: primary | Confidence: high | Accessed: 2026-11-18 | Via: web_extract
   - Quote: "Configurable to:\n\n256GB or 512GB (M5 Ultra with 36-core CPU and 80-core GPU)"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total parameters (all experts resident in memory) | 1.65T in total and 49B activated | https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4 | "Number of Model Parameters: 1.65T in total and 49B activated" |
| 2 | checkpoint size on disk (weights, scales, tokenizer) | 941139951818 bytes (876.5 GiB) | https://huggingface.co/api/models/nvidia/DeepSeek-V4-Pro-0813-NVFP4?blobs=true | "usedStorage":941139951818" |
| 3 | GPQA Diamond, MXFP4 source model | 88.51 | https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4 | "MXFP4 (source) 88.51" |
| 4 | GPQA Diamond, NVFP4 build | 88.42 | https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4 | "NVFP4 88.42" |
| 5 | RTX PRO 6000 Blackwell GPU memory | 96 GB GDDR7 with error-correcting code (ECC) | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/ | "Memory Configuration: 96 GB GDDR7 with error-correcting code (ECC)" |
| 6 | Mac Studio M5 Ultra maximum unified memory | 512GB | https://www.apple.com/mac-studio/specs/ | "256GB or 512GB (M5 Ultra with 36-core CPU and 80-core GPU)" |
| 7 | DGX Spark memory | 128 GB Unified Memory | https://build.nvidia.com/spark/nvfp4-quantization | "DGX Spark \| DGX OS (Linux) \| 128 GB Unified Memory" |
| 8 | maximum context length (sets KV cache growth ceiling) | 1 million tokens | https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4 | "Maximum context length of 1 million tokens." |

## Analogy candidates
- **Restaurant with 384 specialist chefs**: A mixture-of-experts model is a kitchen that must have every specialist on staff before service (all 1.65T parameters in memory), even though each order only pulls in a few (49B activated per token); hiring cheaper chefs (4-bit storage) shrinks the payroll, not the seating capacity needed to house them all. Breaks when: it suggests you could send chefs home to save space, and you cannot subset experts without rebuilding and retraining the model.

## Misconceptions
- Myth: "It's 4-bit, so it should fit on my 24 GB card like other 4-bit quants." Reality: 4-bit shrinks each weight, but 1.65T parameters still fill 941139951818 bytes on disk, roughly ten 96 GB flagship GPUs, so the format name tells you nothing about fit (claims 1 and 2).
- Myth: "NVFP4 is just another Q4 GGUF with a brand sticker." Reality: it reuses the same 4-bit weight grid as the base model's MXFP4 but stores finer E4M3 scales per 16 values, it is aimed at Blackwell tensor cores with minimum compute capability 10.0, and the supported runtimes NVIDIA lists are SGLang and vLLM, not the GGUF toolchain (claims 3, 4 and 5).
- Myth: "Cutting weights to 4 bits always costs real quality." Reality: on NVIDIA's own table GPQA Diamond moved only from 88.51 to 88.42 and one agentic benchmark rose from 96.49 to 98.25 (claim 6).

## Glossary
- **quantization**: storing each model weight in fewer bits so the file and memory footprint shrink, at some risk to answer quality.
- **NVFP4**: NVIDIA's 4-bit floating-point storage format that keeps a small high-precision correction (an FP8 scale) for every group of 16 weights.
- **mixture of experts**: a model design that stores many specialist sub-networks and consults only a few per token, so all weights must sit in memory even though only some are read.
- **active parameters**: the subset of weights actually used to produce one token, 49B of the 1.65T total here.
- **KV cache**: the memory a model keeps of the conversation so far, which grows with context length and stacks on top of the weights.
- **compute capability**: NVIDIA's version number for a GPU generation; NVFP4's fast kernels need 10.0, the Blackwell generation.
- **safetensors**: the file format Hugging Face ships model weights in, 66 shards in this repo.
- **tensor parallel**: splitting one model's layers across several GPUs so a checkpoint larger than any single card can be served.

## Unverified
- No page fetched this session reports measured tokens per second for this checkpoint on any single machine, and our expectation is that a 128 GB DGX Spark cannot come close to holding it, so any Spark number would come from a multi-node or offloading setup a first-party measurement would have to replace.
- A community thread on the sibling Flash NVFP4 repo reports vLLM rejecting NVFP4 Mixture-of-Experts configs on workstation Blackwell (SM120, RTX PRO 6000 and DGX Spark) into mid-2026 with a fix pull request still open, which matches no statement in NVIDIA's model card; treat it as a lead to retest on current vLLM, not a fact.
- No fetched page demonstrates llama.cpp, Ollama or LM Studio loading this exact safetensors checkpoint, and community GGUF ports of DeepSeek V4 Pro exist only as unread forum and repo mentions, so the plain-Q4 comparison path on consumer tools is unconfirmed.
- The disk-space cost of the download plus any conversion output landing alongside it plausibly needs on the order of 2 TB free, but no fetched page states a requirement, so hedge or drop.

## Suggested outline
1. Cold open on the number: the 4-bit cut of DeepSeek V4 Pro is 941139951818 bytes, about 941 GB, and the biggest desktop GPU NVIDIA sells holds 96 GB, so do the load math before you touch the download button.
2. The math itself: what 4-bit storage does, why a mixture-of-experts model must keep all 1.65T parameters resident even though only 49B fire per token, and the tier ladder (24 and 32 GB out, 96 GB holds a tenth, 128 GB unified a seventh, 512 GB Mac Studio the first single board that clears it).
3. The catch and the verdict: NVFP4 is not a plain Q4 (finer scales per 16 values, a slightly larger file than its MXFP4 source, Blackwell-first acceleration with slower weight-only fallbacks elsewhere, quality flat at 88.51 to 88.42 on GPQA Diamond), the honest objection that this is datacenter hardware talk, and the one decision to walk away with: check your memory tier first.

## Viewer situation
You've got a gaming PC or a 96 GB workstation card, you keep seeing NVFP4 builds of DeepSeek V4 Pro advertised as the 4-bit cut, and you want to know whether your machine can load one before you commit to a roughly one-terabyte download.

## Has process
false

## Objection
A skeptical engineer says this was never a consumer model: NVFP4 is a format NVIDIA built for B200-class fleets, a 1.65T-parameter checkpoint needs around a terabyte of memory no matter how you slice the bits, and a video about which GPUs load it is really a video about hardware almost nobody owns.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4 | nvidia/DeepSeek-V4-Pro-0813-NVFP4 model card | primary | web_extract | 2026-11-18 |
| 2 | https://huggingface.co/nvidia/DeepSeek-V4-Pro-0813-NVFP4/tree/main | nvidia/DeepSeek-V4-Pro-0813-NVFP4 file tree (66 shards) | primary | web_extract | 2026-11-18 |
| 3 | https://huggingface.co/api/models/nvidia/DeepSeek-V4-Pro-0813-NVFP4?blobs=true | Hugging Face model API: nvidia/DeepSeek-V4-Pro-0813-NVFP4 | primary | web_extract | 2026-11-18 |
| 4 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 | deepseek-ai/DeepSeek-V4-Pro-0813 base model card | primary | web_extract | 2026-11-18 |
| 5 | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ | Introducing NVFP4 for Efficient and Accurate Low-Precision Inference (NVIDIA Technical Blog) | docs | web_extract | 2026-11-18 |
| 6 | https://build.nvidia.com/spark/nvfp4-quantization | Quantize Models to NVFP4 with NVIDIA Model Optimizer (DGX Spark playbook) | primary | web_extract | 2026-11-18 |
| 7 | https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-scheme/ | Choosing the right compression scheme (LLM Compressor Docs, vLLM project) | docs | web_extract | 2026-11-18 |
| 8 | https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro | deepseek-ai/DeepSeek-V4-Pro (vLLM Recipes) | docs | web_extract | 2026-11-18 |
| 9 | https://github.com/NVIDIA/TensorRT-LLM/releases | Releases, NVIDIA/TensorRT-LLM | primary | web_extract | 2026-11-18 |
| 10 | https://huggingface.co/nvidia/DeepSeek-V4-Flash-NVFP4/discussions/3 | Not working on dgx spark with vllm (community discussion) | community | web_extract | 2026-11-18 |
| 11 | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/ | RTX PRO 6000 Blackwell Workstation Edition (NVIDIA) | primary | web_extract | 2026-11-18 |
| 12 | https://www.apple.com/mac-studio/specs/ | Mac Studio Technical Specifications (Apple) | primary | web_extract | 2026-11-18 |

## Notes
Three things the writer should carry. First, a framing conflict to state honestly rather than average: NVIDIA's card validates the vLLM path on 8x B200 only, while vLLM's compression docs say NVFP4 checkpoints also load on Ampere-and-newer GPUs via weight-only Marlin kernels and TensorRT-LLM's release notes enable Marlin NVFP4 on Ada Lovelace and W4A16 NVFP4 on SM120, so "Blackwell-only" is about the fast kernels, not about the file refusing to load; we trust the docs' distinction because it is the runtime's own maintained page. Second, a naming trap: the Hugging Face sidebar rounds the parameter count to "1.7T params" while the card itself says 1.65T in total and the API totals 1650497936906 parameters, so use 1.65T, and note that vLLM's recipes page lists a separate NVFP4 variant repo id (nvidia/DeepSeek-V4-Pro-NVFP4, MTP draft, built from the preview weights) that is not the 0813 checkpoint this brief cites; do not conflate them. Third, thin spots: no independent benchmark harness has published throughput or quality for this exact checkpoint (the 88.51 versus 88.42 table is NVIDIA's own, measured on SGLang at temperature 1.0), and the KV cache cost at a typical context is not published as one number anywhere fetched, which is why the brief carries context ceiling (1 million tokens) rather than a fabricated cache figure.
