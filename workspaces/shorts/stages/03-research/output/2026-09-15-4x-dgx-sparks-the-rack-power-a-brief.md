---
slug: 2026-09-15-4x-dgx-sparks-the-rack-power-a
stage: 03-research
topic: "4x DGX Sparks: the rack, power and multi-node math"
depth: standard
generated_at: 2026-09-15T17:48:07Z
sources: 12
hub: "[[videos/2026-09-15-4x-dgx-sparks-the-rack-power-a]]"
---

# Research brief: 4x DGX Sparks: the rack, power and multi-node math

## Summary
The one-line idea is that four Sparks are a memory purchase, not a speed purchase: you buy the ability to hold a model no single consumer GPU can hold. The most arresting number is the physics: each unit's memory bus runs at 273 GB/s while the link between units carries 25 GB/s, so a model split across four boxes decodes at roughly one tenth of four NVLink'd H200s, and Petronella measured a 27B model dropping from 8.3 tok/s on one unit to 3.5 tok/s sharded badly over 10 Gb/s Ethernet. The strongest concrete case is Alex Ellis's write-up (5 hours old): a 753B-parameter model, GLM-5.2, that "no consumer GPU could hold", run by cabling four Sparks into a ring with no switch at all, saving a 1500 GBP MikroTik switch. What could not be verified: real electricity cost of running four units, any colo/rack rental price, and GLM-5.2's own decode speed on the four-node ring (Ellis serves GLM-5.3-Flash, the smaller model, at ~45 tok/s on agentic traffic). Sources conflict on the ceiling: NVIDIA's marketing page says up to four Sparks work with "models of up to 700 billion parameters", while Ellis's measured recipe tops out at GLM-5.3-Flash (320B total) and Exxact's table tops out at "Up to 700B to 800B".

## Thesis
Four DGX Sparks buy you memory, not speed: 512 GB of it, enough to hold a 753B-parameter model that no single consumer GPU can even load, at a decode rate a patient human can read.

## Explanation path
Start with what one Spark is: a 150 x 150 mm Mac-Mini-sized box with 128 GB of unified memory that the CPU and GPU share, sold for $4,699.00 on NVIDIA's own marketplace. Establish the wall a single unit hits -- the biggest open models simply do not fit in 128 GB -- before any second box appears. Then show what the network cable actually does: two units pool memory to 256 GB, four pool to 512 GB, and NVIDIA's clustering tooling supports up to three units on direct cables, up to four through a switch. With the memory math in place, deliver the reality check: inside each unit the memory bus moves 273 GB/s but the cable between units moves 25 GB/s, so clustering is a capacity play that buys model size, not linear speed -- Petronella's four GB10 nodes decode GLM-5.3-Flash at 26.5 tok/s on prose while four H200s decode at 233 to 339 tok/s. Then the buy story lands: Alex Ellis's write-up explains why a business bought four, cabled them into a switchless ring (avoiding a 1500 GBP switch), and what it actually cost -- about 10000 GBP for two units in the UK. Close on the honest caveat: the multi-node software is community-patched and fragile (vLLM's stock image "died five different ways before producing a token"), the whole rack still draws less than a space heater (under 1200W), and one bigger box may be the smarter buy if raw speed is the goal.

## Claims
1. **NVIDIA's own marketplace lists the DGX Spark at $4,699.00 (4 TB), currently out of stock.**
   - Source: NVIDIA DGX Spark US - A Grace Blackwell AI supercomputer on your desk, https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "$4,699.00 [Out of Stock]"
2. **Alex Ellis (OpenFaaS Ltd) published the buy write-up on 2026-09-15, explaining how and why the team bought 4x DGX Sparks; two units with 4TB drives cost "almost 10000 GBP" in the UK, and an NVIDIA Inception startup discount clawed back "about 600 GBP".**
   - Source: How and Why We Bought 4x DGX Sparks, https://blog.alexellis.io/how-and-why-we-bought-4-dgx-sparks/
   - Tier: docs | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "Two DGX Sparks in the UK with 4TB drives were going to cost us almost 10000 GBP to purchase, and the prices had increased the previous month."
3. **The four-unit cluster needs no switch at all: Ellis cabled the four Sparks into a closed ring and skipped the 1500 GBP MikroTik CRS804 DDQ switch by patching NCCL so non-adjacent units relay through a neighbour.**
   - Source: How and Why We Bought 4x DGX Sparks, https://blog.alexellis.io/how-and-why-we-bought-4-dgx-sparks/
   - Tier: docs | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "I also thought we'd need to purchase a noisy MikroTik CRS804 DDQ switch (1500 GBP) in order to cluster the 4x units, but we managed to get away without it by patching the NCCL library and giving units that were not directly connected a way to route through each other."
4. **Four nodes buy memory, not linear speed: GLM-5.3-Flash NVFP4 at tensor-parallel 4 across four GB10 nodes decoded at 26.5 tok/s on prose, 38.1 on code and 46.7 on math, with 91.2 tok/s aggregate over six concurrent streams -- while the same model in FP8 on four H200 GPUs with NVLink decoded at 233 to 339 tok/s single stream.**
   - Source: DGX Spark Cluster: From Two Sparks to a Switched Fabric, https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "Single-stream decode at temperature 0 on 256-token outputs measured 26.5 tok/s on prose, 38.1 on code and 46.7 on math."
5. **The speed ceiling is physics: each unit's unified LPDDR5x memory runs at 273 GB/s while the 200 Gb/s link between units is 25 GB/s, and Petronella conclude "Clustering GB10 units is a capacity play, not a raw speed boost".**
   - Source: DGX Spark Cluster: From Two Sparks to a Switched Fabric, https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "Clustering GB10 units is a capacity play, not a raw speed boost; the 273 GB/s memory bus inside each unit against the 25 GB/s link between them is the reason."
6. **The recipe actually works and has receipts: Ellis's GLM-5.3-Flash NVFP4 TP4 ring serves one OpenAI-compatible endpoint with a 262K context window at ~45 tok/s on real agentic traffic, and its controlled 5 September 2026 baseline measured 75.2 tok/s completed code decode, 29.8 tok/s prose decode and 2,276 tok/s cold 64K prefill, all 15/15 output gates passed.**
   - Source: GitHub - alexellis/glm-5.3-flash-4x-dgx-spark-switchless, https://github.com/alexellis/glm-5.3-flash-4x-dgx-spark-switchless
   - Tier: docs | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "One OpenAI-compatible endpoint, a 262K context window, ~45 tok/s on real agentic traffic -- on hardware you own."
7. **Four-to-eight nodes on a big MoE is the sweet spot: Qwen3.8-Flash-Next NVFP4 needed tensor parallel plus expert parallel to load on four nodes at all and delivered 39.6 / 57.0 / 76.9 tok/s single stream and 167.4 tok/s across six concurrent streams -- 21 to 54 percent faster per stream than the same model on two nodes.**
   - Source: DGX Spark Cluster: From Two Sparks to a Switched Fabric, https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "Against the same model on two nodes (35.3 / 36.0 / 53.2 tok/s) that is 21 to 54 percent faster per stream, the one case where clustering buys per-stream speed: a mixture of experts whose per-rank working set shrinks."
8. **The multi-node software is still fragile: as of August 2026 the vendor vLLM image for GLM-5.3-Flash "died five different ways before producing a token" on GB10 and needed community patch chains (tonyd2wild's GLM recipes, x00byte's Qwen recipe) to run.**
   - Source: DGX Spark Cluster: From Two Sparks to a Switched Fabric, https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "The stock image for GLM-5.3-Flash died five different ways before producing a token: a wrong attention backend gate, a NaN in the attention kernel at specific batch sizes, a silent NCCL downgrade from 2.30.7 to 2.29.7 that fails on the RoCE fabric, a CUTLASS DSL mismatch, and a Programmatic Dependent Launch race."
9. **Power is a non-story at four units: each Spark ships with a 240W external supply and the whole four-node build plus a CRS804 switch stays under 1200W, below a standard 1800W outlet circuit.**
   - Source: Build a 4x NVIDIA DGX Spark Cluster | Exxact Blog, https://www.exxactcorp.com/blog/deep-learning/what-you-need-to-build-a-4x-nvidia-dgx-spark-cluster-switch-cabling-power
   - Tier: docs | Confidence: high | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "each DGX Spark ships with a 240W external supply; the CRS804 draws roughly 92W typical and about 123W under load. You may need a PDU, but max power draw shouldn't exceed 1200W, well below the standard outlet circuit 1800W peak."
10. **What four units unlock is the model class: NVIDIA's ConnectX networking page says four Spark systems work with "AI models of up to 700 billion parameters", and the model Ellis targets, GLM-5.2, is 753B parameters on its own model card -- "no consumer GPU" can hold it.**
   - Source: Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: medium | Accessed: 2026-09-15 | Via: web_extract
   - Quote: "High-performance NVIDIA ConnectX networking enables the connection of up to four NVIDIA DGX Spark systems to work with AI models of up to 700 billion parameters."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | single-unit price, 4 TB, NVIDIA marketplace | $4,699.00 | https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/ | "$4,699.00" |
| 2 | cost of first two units in the UK (4TB drives) | almost 10000 GBP | https://blog.alexellis.io/how-and-why-we-bought-4-dgx-sparks/ | "Two DGX Sparks in the UK with 4TB drives were going to cost us almost 10000 GBP to purchase" |
| 3 | four-node combined unified memory | 512 GB | https://developer.nvidia.com/blog/run-local-ai-agents-with-faster-models-and-multi-node-clustering-on-nvidia-dgx-spark/ | "a cluster assistant that automates connecting two to four DGX Spark units into a high-bandwidth cluster with up to 512 GB of unified memory" |
| 4 | GLM-5.2 total parameters | 753B params | https://huggingface.co/zai-org/GLM-5.2 | "Safetensors Model size 753B params Tensor type BF16" |
| 5 | four-node real decode, GLM-5.3-Flash NVFP4, prose | 26.5 tok/s | https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/ | "Single-stream decode at temperature 0 on 256-token outputs measured 26.5 tok/s on prose, 38.1 on code and 46.7 on math." |
| 6 | same model, four H200 with NVLink | 233 to 339 tok/s | https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/ | "the same GLM-5.3-Flash model in FP8 on four H200 GPUs with NVLink, on the same harness, decodes at 233 to 339 tok/s single stream" |
| 7 | switch saved by ring topology | 1500 GBP | https://blog.alexellis.io/how-and-why-we-bought-4-dgx-sparks/ | "a noisy MikroTik CRS804 DDQ switch (1500 GBP)" |
| 8 | whole four-node rack, max draw | 1200W | https://www.exxactcorp.com/blog/deep-learning/what-you-need-to-build-a-4x-nvidia-dgx-spark-cluster-switch-cabling-power | "max power draw shouldn't exceed 1200W, well below the standard outlet circuit 1800W peak" |

## Analogy candidates
- **Vehicle**: four people moving a piano versus one strongman. Mapping: one consumer GPU is the strongman -- very fast (273 GB/s memory bus) but cannot lift the piano (a 753B model does not fit in 128 GB or 32 GB of VRAM); four Sparks are four ordinary movers who together can lift it, but they keep pausing to coordinate (25 GB/s between units), so the move is slower per step than the strongman's would be if he could lift it at all. Limit: breaks when the viewer concludes four movers are always slower -- for sparse mixture-of-experts models the per-rank working set shrinks and Petronella measured 21 to 54 percent faster per stream than two nodes.
- **Vehicle**: a bucket brigade. Mapping: each Spark is a bucket-holder with a big bucket (128 GB); tensor parallelism passes the water bucket to bucket over the 25 GB/s link, so total throughput is set by the passing speed, not bucket size. Limit: breaks because water is not split -- in reality each node holds a different quarter of the model and they exchange activations, which is why aggregate bandwidth matters more than per-link latency for prefill.

## Misconceptions
- Myth: four DGX Sparks are four times faster than one at generating tokens. Reality: clustering buys capacity, not linear speed -- the memory bus inside each unit runs at 273 GB/s while the link between units runs at 25 GB/s, so four GB10 nodes deliver roughly one tenth of four H200s on per-stream decode (claims 4 and 5).
- Myth: you need an expensive network switch before you can cluster four Sparks. Reality: NVIDIA's own guidance supports up to three units on direct cables and up to four through a switch, but Ellis's switchless ring runs four units with patched NCCL and no switch at all, with speed "on par with a switched setup" (claims 3 and 10).

## Glossary
- **DGX Spark**: NVIDIA's desk-side AI computer -- a 150 x 150 mm box built on the GB10 Grace Blackwell superchip with 128 GB of memory shared by CPU and GPU.
- **unified memory**: one pool of RAM that the CPU and GPU share, instead of separate VRAM; it is why the Spark can hold models a gaming GPU cannot.
- **tensor parallelism**: splitting one model's layers across several machines so each holds a slice and they exchange intermediate results every step.
- **MoE (Mixture of Experts)**: a model architecture that stores many small expert sub-networks and activates only a few per token, so it can be huge on disk but cheap per token.
- **tok/s (tokens per second)**: the decode speed of a language model -- how many tokens of answer come out each second; tens is human-reading pace.
- **prefill**: the step that digests your whole prompt before the first answer token appears; big context means slow first response.
- **speculative decoding**: a small drafter model guesses several tokens ahead and the big model verifies them in one pass; Ellis's recipe uses a drafter called DFlash2.
- **NCCL**: NVIDIA's collective communication library that moves data between GPUs; patching it is what made the switchless four-node ring possible.
- **RoCE**: RDMA over Converged Ethernet -- a way to move memory directly between machines over ordinary Ethernet at near line rate.
- **NVFP4 / quantization**: shrinking model weights to a 4-bit format so a huge model fits in far less memory, at some quality cost.
- **KV cache**: the memory where a model stores the conversation so far so it does not recompute it every token; long context eats it fast.
- **tok/s aggregate**: total throughput summed over concurrent users or agents, as opposed to the speed one single stream sees.

## Unverified
- What GLM-5.2 (the 753B model that motivated buying units three and four) actually decodes at on the four-node ring: Ellis's published numbers are for GLM-5.3-Flash, the smaller model; expect the bigger model to be slower, but no fetched page states a figure.
- Electricity cost of running four Sparks plus a switch for a year: the hardware ceiling is 1200W per the Exxact build sheet, but no fetched page computes a real energy bill at a named tariff.
- Colocation or rack rental pricing for a four-Spark build: no fetched page quotes a monthly colo cost; the story that matters here is that four units fit under a desk and a standard outlet.
- Tokens per second on our own DGX Spark hardware: NVIDIA's marketing shows up to 2.6x throughput improvements for Qwen3.6-35B on a single Spark, and Petronella's four-node GLM-5.3-Flash numbers are 26.5 tok/s prose / 38.1 code single stream; until we run our own RigMark measurement, treat these as other people's numbers on other people's configurations.
- Community throughput claims of "65-85 tokens per second" for two-Spark DeepSeek recipes: Ellis reports these were "counting to 200" benchmaxxing and real speeds were "often around 30-40 tokens per second"; do not cite the higher figure.
- Whether NVIDIA halting first-edition DGX Spark production (per a macnica.co.jp link in Ellis's post) affects unit availability: the claim's source page was not fetched this run.

## Suggested outline
1. A 753-billion-parameter model came out and literally no GPU you can buy can hold it -- but four desk-side boxes, cabled in a ring, can.
2. What one DGX Spark is ($4,699.00, 128 GB of shared memory, a 240W power brick) and the wall it hits alone: the biggest open models do not fit.
3. The cable is the story: two units pool to 256 GB, four to 512 GB; NVIDIA says up to four units and ~700B parameters, Ellis's ring skips the 1500 GBP switch entirely -- and the catch: 273 GB/s inside a unit versus 25 GB/s between them means 26.5 tok/s prose instead of H200 speed, which is exactly human reading pace.

## Viewer situation
You own or are eyeing one DGX Spark, you have watched models like GLM-5.2 land at sizes your 128 GB simply cannot hold, and you are wondering whether three more boxes and a network switch is a smart buy or an expensive toy.

## Has process
false

## Objection
A skeptical engineer says: the multi-node stack is community-patched vLLM that "died five different ways" before working, four 240W boxes with 512 GB of slow-interconnected RAM will never match one proper GPU server on speed, and roughly 20000 GBP of hardware to decode at 26.5 tok/s is a hobby, not infrastructure.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://blog.alexellis.io/how-and-why-we-bought-4-dgx-sparks/ | How and Why We Bought 4x DGX Sparks | docs | web_extract | 2026-09-15 |
| 2 | https://github.com/alexellis/glm-5.3-flash-4x-dgx-spark-switchless | GLM-5.3-Flash NVFP4 -- 4x DGX Spark, switchless-ring TP4 + DFlash2 | docs | web_extract | 2026-09-15 |
| 3 | https://petronellatech.com/blog/dgx-spark-cluster-from-two-sparks-to-a-switched-fabric/ | DGX Spark Cluster: From Two Sparks to a Switched Fabric | benchmark | web_extract | 2026-09-15 |
| 4 | https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/ | NVIDIA DGX Spark US - A Grace Blackwell AI supercomputer on your desk | primary | web_extract | 2026-09-15 |
| 5 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark | primary | web_extract | 2026-09-15 |
| 6 | https://www.exxactcorp.com/blog/deep-learning/what-you-need-to-build-a-4x-nvidia-dgx-spark-cluster-switch-cabling-power | Build a 4x NVIDIA DGX Spark Cluster | Exxact Blog | docs | web_extract | 2026-09-15 |
| 7 | https://developer.nvidia.com/blog/run-local-ai-agents-with-faster-models-and-multi-node-clustering-on-nvidia-dgx-spark/ | Run Local AI Agents with Faster Models and Multi-Node Clustering on NVIDIA DGX Spark | docs | web_extract | 2026-09-15 |
| 8 | https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html | ConnectX-7 Networking -- DGX Spark User Guide | docs | web_extract | 2026-09-15 |
| 9 | https://huggingface.co/zai-org/GLM-5.2 | zai-org/GLM-5.2 - Hugging Face | primary | web_extract | 2026-09-15 |
| 10 | https://forums.developer.nvidia.com/t/llama-cpp-rpc-on-dgx-spark/361862 | Llama.cpp rpc on dgx spark - NVIDIA Developer Forums | community | web_extract | 2026-09-15 |
| 11 | https://github.com/ggml-org/llama.cpp/discussions/16578 | Performance of llama.cpp on NVIDIA DGX Spark | docs | web_extract | 2026-09-15 |
| 12 | https://www.storagereview.com/review/nvidia-dgx-spark-cluster-review-distributed-inference-on-dell-gigabyte-and-hp | NVIDIA DGX Spark Cluster Review: Distributed Inference on Dell, GIGABYTE, and HP | benchmark | web_extract | 2026-09-15 |

## Notes
Source conflict on the four-node ceiling: NVIDIA's product page says ConnectX networking links up to four Sparks for "AI models of up to 700 billion parameters", Exxact's scaling table says "Up to 700B to 800B" for 4x at NVFP4, but the two measured write-ups cap at GLM-5.2 (753B params, fits but not measured for speed) and GLM-5.3-Flash (320B total, measured). Trust the measured pages for what four nodes actually deliver day to day; treat the 700B figure as the marketing ceiling. The llama.cpp RPC forum thread and the StorageReview cluster review were fetched but returned thin content (a closed thread stub and a cookie wall respectively), so neither contributes a number. Thinnest spot: power and colo economics -- we have the 1200W ceiling and per-unit 240W supply, but no fetched source computes a running cost, so the video should stay at watts, not dollars per year.
