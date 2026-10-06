---
slug: 2026-10-06-amd-quark-on-strix-halo-offici
stage: 03-research
topic: "AMD Quark on Strix Halo: official local quantization"
depth: standard
generated_at: 2026-10-06T11:43:02Z
sources: 11
hub: "[[videos/2026-10-06-amd-quark-on-strix-halo-offici]]"
---

# Research brief: AMD Quark on Strix Halo: official local quantization

## Summary
AMD's ROCm blog shipped an official recipe for quantizing models on the Strix Halo APU itself, closing the loop on a machine that previously only ran quants other people made. The arresting number: a 35B MoE checkpoint shrinks from roughly 70 GB to about 21 GB on the device, inside the same 128 GB pool it runs from. The concrete case is a single ASUS ROG Flow Z13 (Ryzen AI Max+ 395, 128 GB, ROCm 7.2.0, amd-quark 0.12.post1) that quantizes with Quark, exports to GGUF or safetensors, then runs in llama.cpp, vLLM and Lemonade. Not verified anywhere fetched: how fast the Quark-exported artifacts actually generate (the blog reports no tokens-per-second), and the HP Z2 Mini G1a as a 395 machine. No source conflicts; the one date wrinkle is that the post is bylined September 25, 2026, not "hours ago" as the idea pitch assumed.

## Thesis
AMD's Quark recipe turns a Strix Halo box from a machine that only runs other people's Q4 quants into one that makes its own: a 35B MoE checkpoint shrinks from roughly 70 GB to about 21 GB on the device, then drops straight into llama.cpp or vLLM.

## Explanation path
Start with the half of local AI the viewer never sees: before any model runs, someone compressed it. Quantization is that step, turning 16-bit weights into 4-bit ones so the model streams through a third of the memory. Establish why size is the whole game on an APU: the Radeon 8060S integrated GPU shares one LPDDR5X pool with the CPU at 256 GB/s, so smaller weights mean faster tokens, and up to 96GB of that pool can be handed to the GPU through Variable Graphics Memory. Then place the viewer's status quo: they run Q4 GGUFs other people made, through Ollama or LM Studio, because making a quant yourself meant a conversion pipeline, imatrix tuning, and usually a bigger machine than the one the model runs on. Then the news: AMD's ROCm blog walks the entire workflow on one 128 GB Strix Halo machine -- Quark quantizes the 35B MoE checkpoint on-device (peaking at 95 GB of the unified pool), exports GGUF Q4_0/Q4_1 for llama.cpp or safetensors for vLLM with no extra conversion step, and Lemonade serves the same GGUF interactively. Close on the honest catch: AMD's own numbers show the quality cost of 4-bit is task dependent and no configuration is uniformly best, so the value is not a magic file but the quantization decision moving in-house.

## Claims
1. **AMD's ROCm blog quantizes Qwen3.6-35B-A3B, a 35B-parameter Mixture-of-Experts model, from BF16 to W4A16 directly on a Strix Halo system with 128 GB of unified memory, reducing the model weights from roughly 70 GB to about 21 GB.**
   - Source: Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo, https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "In this post, we quantize Qwen3.6-35B-A3B, a 35B-parameter Mixture-of-Experts model, from BF16 to W4A16 directly on a Strix Halo system with 128 GB of unified memory. Quantization reduces the model weights from roughly 70 GB to about 21 GB."
2. **The official workflow is quantize with Quark (W4A16, RTN), export, then run: GGUF for llama.cpp (Q4_0 from symmetric INT4, Q4_1 from asymmetric UInt4, both at group size 32) and safetensors for vLLM (group size 128), with both export paths generated directly from Quark and no additional model-conversion step in the target runtime.**
   - Source: Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo, https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "Both export paths are generated directly from Quark without requiring an additional model-conversion step in the target inference runtime."
3. **Quantizing the 35B checkpoint on-device peaks at 95 GB of GPU-visible unified memory (GTT) on the GGUF path and stays within the system's 128 GB, with a quant time of 1.5 min and an export time of 22 min for INT4-GS32.**
   - Source: Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo, https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "Peak memory stays within the system's 128 GB of unified memory in all cases, so quantizing a 35B model that starts at roughly 70 GB in BF16 fits on a single Strix Halo machine."
4. **On wikitext-2 perplexity measured with llama.cpp, the Quark Q4_0 GGUF scores 6.79 ±0.24 versus 6.61 ±0.23 for the F16 baseline, a +2.7% change, while the artifact compresses to about 30% of the float model.**
   - Source: amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF model card, https://huggingface.co/amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "Quantization is nearly lossless: Q4_1 is only +1.8% over F16 and Q4_0 only +2.7%, while the size is compressed to about 30% of the float model."
5. **AMD's lm-evaluation-harness results show the impact of 4-bit quantization is task dependent with no uniformly best configuration: on GPQA the BF16 baseline scores 0.4337 acc_norm versus 0.4086 for the INT4-GS32 GGUF, and the GS128 vLLM accuracy run was executed on a separate data-center GPU system.**
   - Source: Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo, https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "The results do not indicate a single quantization configuration that is uniformly best across all tasks."
6. **The Ryzen AI Max+ 395 (former codename Strix Halo) pairs 16 Zen 5 CPU cores with an integrated GPU of 40 RDNA 3.5 compute units, ships in systems with 32GB up to 128GB of unified memory, and up to 96GB of that can be converted to VRAM through AMD Variable Graphics Memory.**
   - Source: AMD Ryzen AI MAX+ 395 Processor: Breakthrough AI Performance in Thin and Light, https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "Powered by 16 "Zen 5" CPU cores, 50+ peak AI TOPS XDNA™ 2 NPU and a truly massive integrated GPU driven by 40 AMD RDNA™ 3.5 CUs, the Ryzen™ AI MAX+ 395 is available today with system memory options ranging from 32GB all the way up to 128GB of unified memory – out of which up to 96GB can be converted to VRAM through AMD Variable Graphics Memory."
7. **The platform's LPDDR5X gives the integrated Radeon 8060S 256 GB/s of memory bandwidth, which AMD credits for up to 2.2x the token throughput of the Intel Arc 140V.**
   - Source: AMD Ryzen AI MAX+ 395 Processor: Breakthrough AI Performance in Thin and Light, https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "From the results, we can see that the ASUS ROG Flow Z13 - powered by the integrated Radeon™ 8060S and taking full advantage of the 256 GB/s bandwidth - effortlessly achieves up to 2.2x the performance of the Intel Arc 140V in token throughput."
8. **Before this post, AMD's own local-inference guidance centered on running pre-quantized Q4_K_M models through Ollama on Strix Halo: Qwen3.5 35B-A3B at Q4_K_M (20.5 GB) generated at 42.04 tok/s with 100% GPU offloading.**
   - Source: AI Inference on AMD Ryzen AI Max Processor, https://rocm.blogs.amd.com/artificial-intelligence/ryzen-uma-llm/README.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "The 35B MoE model achieves 42.04 tok/s generation throughput and 154.52 tok/s prompt processing with 100% GPU offloading."
9. **Framework sells the Framework Desktop, a 4.5L workstation built on Strix Halo, in Ryzen AI Max+ 395 SKUs at 64GB and 128GB, and its September 2026 table recommends running DeepSeek V4 Flash 0731 at UD-IQ2_XXS using 90.9GB on the 128GB SKU.**
   - Source: Framework Desktop product page, https://frame.work/desktop
   - Tier: primary | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
   - Quote: "| AMD Ryzen™ AI Max+ 395 - 128GB | DeepSeek V4 Flash 0731 | UD-IQ2_XXS | 90.9GB |"
10. **The GMKtec EVO-X2 is a reviewed mini-PC pairing the Ryzen AI Max+ 395's 16 CPU cores and 40-core RDNA 3.5 GPU with 128GB of LPDDR5X memory.**
    - Source: GMKtec EVO-X2 Review an AMD Ryzen AI Max 395 Powerhouse, https://www.servethehome.com/gmktec-evo-x2-review-an-amd-ryzen-ai-max-395-powerhouse/
    - Tier: docs | Confidence: high | Accessed: 2026-10-06 | Via: web_extract
    - Quote: "That processor is a big deal because we get 16 CPU cores and the massive 40-core RDNA 3.5 GPU integrated with 128GB of LPDDR5X memory."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Qwen3.6-35B-A3B weights, BF16 to W4A16 | roughly 70 GB to about 21 GB | https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html | "Quantization reduces the model weights from roughly 70 GB to about 21 GB." |
| 2 | Peak GPU-visible unified memory (GTT) during on-device quantization, INT4-GS32 GGUF path | 95 GB | https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html | "Peak memory stays within the system's 128 GB of unified memory in all cases" |
| 3 | Status-quo generation speed, Qwen3.5 35B-A3B at Q4_K_M via Ollama, 100% GPU offload | 42.04 tok/s | https://rocm.blogs.amd.com/artificial-intelligence/ryzen-uma-llm/README.html | "The 35B MoE model achieves 42.04 tok/s generation throughput and 154.52 tok/s prompt processing with 100% GPU offloading." |
| 4 | Strix Halo LPDDR5X memory bandwidth | 256 GB/s | https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html | "taking full advantage of the 256 GB/s bandwidth" |
| 5 | Unified memory convertible to VRAM via AMD Variable Graphics Memory | up to 96GB | https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html | "out of which up to 96GB can be converted to VRAM through AMD Variable Graphics Memory" |
| 6 | Wikitext-2 perplexity of the Quark Q4_0 GGUF (F16 baseline 6.61 ±0.23) | 6.79 ±0.24 | https://huggingface.co/amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF | "Q4_0 (INT4 symmetric) | 6.79 ±0.24 | +2.7% | ~21 GB" |

## Analogy candidates
- **Compressing raw photos into JPEGs for your phone**: the BF16 checkpoint is the roughly 70 GB of raw originals; W4A16 quantization is the about 21 GB of compressed copies (about 30% of the original) that look the same at normal viewing distance; group size is how many pixels share one compression setting. Breaks when: a JPEG opens in any viewer, but a quantized model only loads in a runtime that speaks its format -- which is exactly why Quark exports GGUF for llama.cpp and safetensors for vLLM rather than one file.
- **Repackaging bulk groceries into jars for one shared pantry**: unified memory is the single 128 GB pantry CPU and GPU both eat from; quantization repacks the 70 GB bulk purchase into 21 GB jars that fit the shelf the GPU can reach (up to 96GB of it via Variable Graphics Memory). Breaks when: the pantry's door is the 256 GB/s bandwidth -- smaller jars help everything fit, but the door still sets how fast you can cook, so quantization buys capacity before it buys speed.

## Misconceptions
- Myth: Quantizing a model yourself needs a data-center GPU or at least a big discrete card. Reality: AMD ran the whole quantization on the 128 GB Strix Halo laptop itself, peaking at 95 GB of unified memory (claim 3).
- Myth: A quant made outside llama.cpp's own tooling won't load without conversion scripts. Reality: Quark writes GGUF that llama.cpp loads directly and safetensors that vLLM loads through its Quark integration, with no additional model-conversion step (claim 2).
- Myth: 4-bit is 4-bit, so any Q4 file is as good as any other. Reality: AMD's own harness runs show the quality impact is task dependent, with no single configuration uniformly best across tasks (claim 5).

## Glossary
- **quantization**: Compressing a model's stored weights from high precision such as 16-bit floats to lower precision such as 4-bit integers so it uses less memory.
- **W4A16**: A quantization scheme with 4-bit weights and 16-bit activations, so only the weights shrink.
- **AMD Quark**: AMD's open-source quantization toolkit that turns model checkpoints into deployable formats for AMD hardware.
- **GGUF**: The model file format loaded by llama.cpp and the apps built on it, including Ollama and LM Studio.
- **safetensors**: The checkpoint format vLLM loads; Quark stores its quantization metadata in config.json alongside it.
- **unified memory**: One LPDDR5X memory pool shared by CPU, integrated GPU and NPU, so the integrated GPU can see up to 128 GB on Strix Halo.
- **Mixture-of-Experts (MoE)**: A model architecture where only a fraction of the parameters is active per token, here 3B of 35B.
- **group size**: How many weights share a single quantization scale; group size 32 gives finer scaling on the GGUF path, 128 on the vLLM path.
- **RTN (Round-To-Nearest)**: The simplest quantization method, snapping each weight to the nearest representable 4-bit value without calibration data.
- **Q4_0**: The llama.cpp symmetric 4-bit quant format that Quark's INT4 group-size-32 export maps to; Q4_K_M is the community's everyday format made with llama.cpp's own tools.
- **llama.cpp**: The open-source C/C++ inference engine underneath Ollama and LM Studio.
- **vLLM**: A serving-focused inference engine that loads Quark safetensors through its Quark integration.
- **Lemonade**: An AMD-supported local LLM application layer that serves the same Quark GGUF through its llama.cpp backend.
- **tokens per second (tok/s)**: How fast a model generates text; on an APU it is bounded by memory bandwidth.

## Unverified
- How fast the Quark-exported GGUF or safetensors artifacts actually generate on Strix Halo: the blog reports quantization cost and accuracy but no inference speed for its own artifacts.
- That the HP Z2 Mini G1a ships the Ryzen AI Max+ 395: no page fetched this session states it.
- That Vulkan llama.cpp builds often beat ROCm builds for decode on Strix Halo: seen only in search snippets, never read in a fetched page.
- That the blog post was published hours ago: the byline reads September 25, 2026, about eleven days before today.
- Community llama-bench figures for the same model class on a Framework Strix Halo (44.58 to 53.48 tok/s tg128 at Q8_0) come from a forum post and await a named reviewer or first-party run.

## Suggested outline
1. Open on the box under the viewer's desk: it runs Q4 quants other people made, and the making half of the hobby was never theirs -- until AMD shipped an official recipe for their exact chip.
2. Walk the recipe on one machine: Quark squashes Qwen3.6-35B-A3B from roughly 70 GB to about 21 GB inside the same 128 GB pool it runs from (95 GB peak), then exports GGUF for llama.cpp or safetensors for vLLM with no conversion step.
3. Land the catch and the payoff: perplexity only moves +2.7% but AMD's own table shows task-dependent dips and reports no speed for its artifacts -- the real win is that the quantization decision moves in-house.

## Viewer situation
You own or you are eyeing a Strix Halo machine -- a Framework Desktop, a GMKtec EVO-X2, an HP Z2 Mini G1a -- with 64 or 128 GB of unified memory, and today you run Q4 GGUFs that other people quantized, pulled through Ollama or LM Studio with VRAM-allocation and GPU-offload settings you tweaked by hand.

## Has process
`true`
- Install amd-quark with pip inside a ROCm-enabled Python environment on the Strix Halo machine.
- Load the BF16 checkpoint you want (for example Qwen/Qwen3.6-35B-A3B) with transformers, or run the model card's quantize_q4_0.py script.
- Pick the configuration: symmetric INT4 or asymmetric UInt4, group size 32 for the GGUF/llama.cpp path or 128 for the safetensors/vLLM path.
- Run the Quark quantizer to produce the W4A16 checkpoint (1.5 min for INT4-GS32, peaking at 95 GB of unified memory).
- Export to GGUF Q4_0 or Q4_1 for llama.cpp, or to safetensors with quantization metadata in config.json for vLLM (22 min for the GGUF path).
- Load and run the artifact: a ROCm HIP build of llama.cpp, vLLM with VLLM_USE_TRITON_AWQ=1 for the MoE expert shapes, or Lemonade's llama.cpp backend for interactive chat.

## Objection
"Why would I burn my APU for an hour to RTN-quantize on-device when Unsloth and half of Hugging Face already ship Q4 GGUFs for every model, and Round-To-Nearest without calibration data is the bluntest quantization method there is?"

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html | Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo | primary | web_extract | 2026-10-06 |
| 2 | https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html | AMD Ryzen AI Max+ 395 processor product page | primary | web_extract | 2026-10-06 |
| 3 | https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html | AMD Ryzen AI MAX+ 395 Processor: Breakthrough AI Performance in Thin and Light | primary | web_extract | 2026-10-06 |
| 4 | https://github.com/AMD/Quark | AMD Quark Model Optimizer, GitHub repository README | primary | web_extract | 2026-10-06 |
| 5 | https://docs.vllm.ai/en/stable/features/quantization/quark/ | AMD Quark, vLLM documentation | docs | web_extract | 2026-10-06 |
| 6 | https://frame.work/desktop | Framework Desktop product page | primary | web_extract | 2026-10-06 |
| 7 | https://rocm.blogs.amd.com/artificial-intelligence/ryzen-uma-llm/README.html | AI Inference on AMD Ryzen AI Max Processor | primary | web_extract | 2026-10-06 |
| 8 | https://huggingface.co/amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF | amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF model card, Hugging Face | primary | web_extract | 2026-10-06 |
| 9 | https://forum.level1techs.com/t/strix-halo-llm-inference-notes/249466 | Strix Halo LLM inference notes, Level1Techs Forums | benchmark | web_extract | 2026-10-06 |
| 10 | https://www.servethehome.com/gmktec-evo-x2-review-an-amd-ryzen-ai-max-395-powerhouse/ | GMKtec EVO-X2 Review an AMD Ryzen AI Max 395 Powerhouse, ServeTheHome | docs | web_extract | 2026-10-06 |
| 11 | https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md | llama.cpp tools/quantize README, GitHub | docs | web_extract | 2026-10-06 |

## Notes
FireCrawl REST returned 402 (insufficient credits) on the first call, so the run used the built-in web_search/web_extract fallback per rules/firecrawl-usage.md: 8 searches, 11 page fetches, every fetched page cached under output/fetch-cache/ before citing. No material conflicts between sources. Two things the writer must know: the idea pitch said the blog was published hours ago, but the byline reads September 25, 2026 (a related-posts listing on AMD's own site shows September 24, 2026), so age the reference honestly; and AMD's own caveats are the catch beat -- the GS128 vLLM accuracy run executed on a separate data-center GPU system, and the GGUF loglikelihood evaluations needed a patched llama-server (branch hongweimeng/gguf-prompt-logprobs), both stated in the post. The Level1Techs forum thread corroborates that owners already run this model class at 44-53 tok/s, but it stays out of Claims because it is community-sourced. Sources 2, 4, 5 and 11 are in the Sources table for grounding (spec sheet, Quark's feature matrix, the pip-install and 5-step quantization process, llama.cpp's two-phase quantize tool) without carrying claims of their own.
