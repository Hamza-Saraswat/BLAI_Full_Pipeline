---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
stage: 03-research
topic: "A single DGX Spark runs Qwen3.8-Flash-Next at 43 tok/s in coding: what that speed means for a local-first box"
depth: standard
generated_at: 2026-09-03T01:56:54Z
sources: 8
hub: "[[videos/2026-09-02-dgx-spark-runs-qwen3-8-flash-n]]"
---

# Research brief: DGX Spark runs Qwen3.8-Flash-Next at 43 tok/s in coding

## Summary
A community tinkerer on the NVIDIA developer forums measured roughly 43 tokens per second from Qwen3.8-Flash-Next in a coding workload on a single DGX Spark, using an NVFP4 quantization that shrinks a ~180B-parameter model (360 GB at BF16) to a 135 GB checkpoint that fits the Spark's 128 GB of unified memory with room for a 200k context. The hardware alone does not do it: FP8 heads plus multi-token prediction carry the speed, and without MTP the same setup tops out around 20 tok/s. NVIDIA's own May blog claims up to 2.6x faster inference on agentic models (Qwen3.6 35B on vLLM) from kernels, NVFP4 and MTP, so vendor direction and the field number agree. What could not be verified: any vendor-run benchmark of the 43 tok/s figure, the exact quality cost of the quantization, and the price of the Spark on a fetched pricing page. One conflict: the DGX Spark product page says "up to 1.9x inference speedups" for the DGX OS update while the GTC Taipei blog says "up to 2.6x" for a named model and framework; Notes says which one the channel can defend.

## Thesis
A single DGX Spark runs a ~180B-parameter Qwen3.8-Flash-Next at roughly 43 tok/s in coding because NVFP4 quantization and multi-token prediction, not raw memory bandwidth, decide how fast a big model feels on a desk.

## Explanation path
Start with what the viewer already owns: a gaming PC or a Mac that runs local models, and the standing doubt that anything frontier-class will ever fit or run at usable speed. Establish that the load-bearing number is tokens per second in a coding loop, because that is the number that decides whether an agent keeps up with a human. Then introduce the DGX Spark as deliberately uninteresting hardware: 128 GB of coherent unified memory, up to 273 GB/s of bandwidth, one cable, 240 W. The full model is 360 GB at BF16 and does not fit, so the first idea that does the work is quantization: the NVFP4 recipe compresses the routed experts so the checkpoint lands at 135 GB, fitting the box with headroom for a 200k context. The second idea is multi-token prediction: a small draft layer emits several tokens per step, and on this model it is the difference between roughly 20 tok/s and roughly 43 tok/s. With both ideas in place the number lands, and the close is the honest catch: one user's measurement, an experimental preview of the Qwen4 architecture, and bandwidth far below a Mac Studio Ultra's 1.2TB/s, so the claim is not fastest box, it is the frontier model fits and keeps up.

## Claims
1. **A single DGX Spark posts roughly 43 tok/s on Qwen3.8-Flash-Next in a coding workload.**
   - Source: Single DGX-Spark - Qwen 3.8-Flash-Next at ~43tok/sec in Coding, https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Single DGX-Spark - Qwen 3.8-Flash-Next at ~43tok/sec in Coding"
2. **Without multi-token prediction the same setup could not exceed 20 tok/s; MTP is described as a huge part of the performance gain.**
   - Source: Single DGX-Spark - Qwen 3.8-Flash-Next at ~43tok/sec in Coding, https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "I couldn't find a kernel that gives me more than 20tok/s before MTP (it's a huge part of the performance gain for this model)"
3. **The model run is Qwen3.8-Flash-Next at ~180B total parameters (360 GB BF16 source), quantized to NVFP4 down to a 135 GB checkpoint (~2.7x).**
   - Source: RadixArk/Qwen3.8-Flash-Next-NVFP4 model card, https://huggingface.co/RadixArk/Qwen3.8-Flash-Next-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Number of Model Parameters: ~180B in total (360 GB BF16 source)" and "Checkpoint size is reduced from 360 GB to 135 GB (~2.7x)"
4. **DGX Spark carries 128 GB of coherent unified memory and supports models of up to 200 billion parameters.**
   - Source: NVIDIA DGX Spark product page, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "128 GB of Coherent Unified System Memory" and "models up to 200 billion parameters"
5. **DGX Spark memory bandwidth is up to 273GB/s, and its power draw is 240W.**
   - Source: NVIDIA DGX Spark datasheet, https://dam-cdn.nvd.orangelogic.com/AssetLink/3lhuar5pc56pn7se4c7ahsskw20xw8h5.pdf
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Memory Bandwidth Up to273GB/s" and "Power Consumption 240W"
6. **A Mac Studio with M5 Ultra offers 1.2TB/s memory bandwidth and up to 512GB unified memory.**
   - Source: Mac Studio - Apple, https://www.apple.com/mac-studio/
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "1.2TB/s memory bandwidth" and "Up to 512GB unified memory"
7. **NVIDIA's own update brings up to 2.6x faster inference on top agentic models like Qwen3.6 35B on vLLM, via kernel optimizations, NVFP4 quantization and multi-token prediction.**
   - Source: NVIDIA GTC Taipei at COMPUTEX live blog, https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/
   - Tier: docs | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Developers can experience up to 2.6x faster inference on top agentic models like Qwen3.6 35B on vLLM, driven by a combination of kernel optimizations, NVFP4 quantization and multi-token prediction."
8. **Qwen3.8-Flash-Next is an experimental preview of the Qwen4 architecture: 125B parameters with 6B activated, plus 51B n-gram embedding and 4B MTP, context 262,144 tokens natively.**
   - Source: Qwen/Qwen3.8-Flash-Next model card, https://huggingface.co/Qwen/Qwen3.8-Flash-Next
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Number of Parameters: 125B with 6B activated, plus 51B n-gram embedding and 4B MTP" and "Context Length: 262,144 natively"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | DGX Spark throughput, Qwen3.8-Flash-Next coding, single box, community measurement | ~43tok/sec | https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859 | "~43tok/sec in Coding" |
| 2 | Throughput ceiling before MTP, same setup | 20tok/s | https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859 | "more than 20tok/s before MTP" |
| 3 | Model size, BF16 source | ~180B in total (360 GB BF16 source) | https://huggingface.co/RadixArk/Qwen3.8-Flash-Next-NVFP4 | "~180B in total (360 GB BF16 source)" |
| 4 | NVFP4 checkpoint size | 135 GB (~2.7x) | https://huggingface.co/RadixArk/Qwen3.8-Flash-Next-NVFP4 | "Checkpoint size is reduced from 360 GB to 135 GB (~2.7x)" |
| 5 | DGX Spark unified memory | 128 GB | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "128 GB of Coherent Unified System Memory" |
| 6 | DGX Spark memory bandwidth | Up to273GB/s | https://dam-cdn.nvd.orangelogic.com/AssetLink/3lhuar5pc56pn7se4c7ahsskw20xw8h5.pdf | "Memory Bandwidth Up to273GB/s" |
| 7 | Mac Studio M5 Ultra memory bandwidth | 1.2TB/s | https://www.apple.com/mac-studio/ | "1.2TB/s memory bandwidth" |
| 8 | NVIDIA-claimed inference speedup on agentic models | up to 2.6x | https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/ | "up to 2.6x faster inference on top agentic models like Qwen3.6 35B on vLLM" |
| 9 | Native context length of Qwen3.8-Flash-Next | 262,144 tokens | https://huggingface.co/Qwen/Qwen3.8-Flash-Next | "Context Length: 262,144 natively and extensible up to 1,000,000 tokens" |
| 10 | Context fitted on the Spark in the forum run | 200k context | https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859 | "fitting a 200k context into this beautiful machine" |
| 11 | Time to get running with the installer, poster's estimate | ~ 30 mins | https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859 | "You'll be up and running in ~ 30 mins" |

## Analogy candidates
- **Vehicle**: a freight loading dock. **Mapping**: 128 GB is the dock; NVFP4 shrink-wraps the 360 GB shipment into 135 GB so it fits; MTP is the forklift that moves several boxes per trip instead of one, which is why throughput more than doubles. **Breaks when**: shrink-wrap implies nothing is lost; quantization trades precision for space, and the dock still cannot take a shipment bigger than itself.
- **Vehicle**: a kitchen with one burner. **Mapping**: the Spark's 273 GB/s is a single burner next to a restaurant range (1.2TB/s); MTP is batch cooking, preparing several portions per pass so the single burner feeds the table anyway. **Breaks when**: cooking batches changes the food little, while MTP can change output quality, and the range still wins when the pot itself is too big for one burner.

## Misconceptions
- Myth: 43 tok/s is a vendor benchmark you can put on a comparison chart. Reality: it is one forum user's field measurement on an experimental quantization of an experimental model; the number is real but its provenance is a thread, not a lab. (claims 1, 3, 8)
- Myth: the box with the biggest memory bandwidth always generates fastest. Reality: the Spark's up to 273GB/s is a fraction of a Mac Studio Ultra's 1.2TB/s, yet the Spark posts 43 tok/s on a ~180B model because quantization and MTP, not bandwidth alone, set the speed at this size. (claims 5, 6)

## Glossary
- **tokens per second (tok/s)**: how many word-pieces the model emits each second; the number that decides whether a coding agent keeps up with you.
- **quantization**: storing model weights in fewer bits, such as FP8 or NVFP4, so a big model fits in less memory at some cost in precision.
- **NVFP4**: NVIDIA's 4-bit floating-point weight format, coarser but smaller and faster than FP8 or BF16.
- **multi-token prediction (MTP)**: a small extra draft layer trained to predict several tokens per generation step, multiplying output speed.
- **mixture-of-experts (MoE)**: an architecture where only a subset of expert layers activates per token, so a huge parameter count costs less compute per token.
- **DGX Spark**: NVIDIA's desktop AI computer built on the GB10 Grace Blackwell Superchip with 128 GB of coherent unified memory.
- **Qwen3.8-Flash-Next**: Alibaba's experimental preview of the Qwen4 architecture, a ~180B-parameter multimodal MoE with sparse attention and n-gram embeddings.
- **unified memory**: one pool of memory shared by CPU and GPU, so a model loads once and both sides read it.

## Unverified
- No vendor or independent lab has repeated the ~43tok/sec figure; it rests on the single forum thread and its screenshots.
- The quality cost of the NVFP4 quantization on coding output is documented only as "lowers the quality JUST A BIT" in the poster's words, with no benchmark attached.
- The DGX Spark's current street price was not verified on a fetched pricing page this run.
- The exact serving configuration (batch size, KV cache settings) behind the 43 tok/s run is not documented in the thread.
- Our own hardware should measure tokens per second on the same workload before the channel states it as fact; until then attribute it as one owner's number.

## Suggested outline
1. Hook: a desk box the size of a hardcover book just ran a ~180B-parameter model at ~43tok/sec in coding, and the poster says he was not done tuning.
2. The fit: BF16 needs 360 GB and does not fit, so NVFP4 compresses the checkpoint to 135 GB, and 128 GB of unified memory takes it with room for a 200k context.
3. The speed: MTP is the multiplier, roughly 20tok/s without it versus ~43tok/sec with it, NVIDIA's own stack update leans on the same trick, and the honest catch is provenance plus the Mac Studio Ultra's 1.2TB/s bandwidth, so the claim is the frontier fits, not that the box is fastest.

## Viewer situation
You run local models on a gaming PC or a Mac today, and you keep hearing that anything frontier-class will never fit on your desk.

## Has process
false

## Objection
A skeptical engineer says: one forum post about an experimental quant of an experimental architecture is not evidence, the Spark's up to 273GB/s bandwidth is a fraction of a Mac Studio Ultra's 1.2TB/s, and nobody has reproduced the number.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://forums.developer.nvidia.com/t/single-dgx-spark-qwen-3-8-flash-next-at-43tok-sec-in-coding/381859 | Single DGX-Spark - Qwen 3.8-Flash-Next at ~43tok/sec in Coding | benchmark | web_fetch | 2026-09-03 |
| 2 | https://forums.developer.nvidia.com/t/qwen3-8-flash-next-180b-single-solo-dgx-spark-with-hashk-ple-nvfp4/381519 | Qwen3.8-Flash-Next 180B, Single Solo DGX Spark With HashK-PLE NVFP4 | benchmark | web_fetch | 2026-09-03 |
| 3 | https://huggingface.co/Qwen/Qwen3.8-Flash-Next | Qwen/Qwen3.8-Flash-Next model card | primary | web_fetch | 2026-09-03 |
| 4 | https://huggingface.co/RadixArk/Qwen3.8-Flash-Next-NVFP4 | RadixArk/Qwen3.8-Flash-Next-NVFP4 model card | primary | web_fetch | 2026-09-03 |
| 5 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | NVIDIA DGX Spark product page | primary | web_fetch | 2026-09-03 |
| 6 | https://dam-cdn.nvd.orangelogic.com/AssetLink/3lhuar5pc56pn7se4c7ahsskw20xw8h5.pdf | NVIDIA DGX Spark datasheet | primary | web_fetch | 2026-09-03 |
| 7 | https://www.apple.com/mac-studio/ | Mac Studio - Apple | primary | web_fetch | 2026-09-03 |
| 8 | https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/ | NVIDIA GTC Taipei at COMPUTEX: Live Updates | docs | web_fetch | 2026-09-03 |

## Notes
- Conflict: the DGX Spark product page says "up to 1.9x inference speedups" for the DGX OS update while the GTC Taipei blog says "up to 2.6x faster inference" naming Qwen3.6 35B on vLLM and the techniques behind it. The channel should cite the 2.6x line because it names model, framework and mechanism; the 1.9x page line names none.
- Thin spot: the 43 tok/s number's serving configuration lives in a screenshot the thread links but does not spell out; the script should attribute the number to the forum owner, not state it as settled fact.
- The companion thread (source 2) shows a second owner running the same ~180B model solo on one Spark via a different quantization path (HashK-PLE NVFP4), which corroborates the fit claim even though it posts no tok/s number in the fetched portion.
