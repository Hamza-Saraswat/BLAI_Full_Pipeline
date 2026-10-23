---
slug: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod
stage: 03-research
topic: "8 DGX Sparks, 1 TB: frontier models on a desk"
depth: standard
generated_at: 2026-10-23T11:36:37Z
sources: 12
hub: "[[videos/2026-10-23-8-dgx-sparks-1-tb-frontier-mod]]"
---

# Research brief: 8 DGX Sparks, 1 TB: frontier models on a desk

## Summary
NVIDIA's technical blog (Oct 22, 2026) is the anchor: eight linked DGX Sparks pool 1 TB of unified memory, and NVIDIA itself benchmarked the full GLM 5.3 (753B) across such a cluster at about 470 GB in NVFP4, decoding at 31 TPS at one user. The most arresting number is that 470 GB checkpoint actually running on a desk, but the honest catch is arithmetic: nodes talk at about 25 GB/s while each node's own memory moves 273 GB/s, so the cluster buys capacity, not proportional speed. Unverified: the angle's 816B-class Q8 fit (Meta's Muse Spark Open exists only in community sources this run) and any street price for a full eight-unit build. Conflict: the GTC news post says NVIDIA Sync gains eight-Spark support "this month" while the technical blog says "by the end of the year."

## Thesis
NVIDIA now officially supports clustering eight desk-side DGX Sparks into 1 TB of unified memory, which turns a 753B-parameter frontier model from a datacenter rental into a 470 GB checkpoint that runs on your desk at reading speed.

## Explanation path
Start where the viewer already is: a frontier model is a file, and the whole file has to sit in memory before the model answers anything. Name the desk-side unit: one DGX Spark, a GB10 Grace Blackwell machine whose CPU and GPU share a single 128 GB unified memory pool, so no weights are copied between chips. Establish the wall: a frontier checkpoint shrunk to 4-bit is still hundreds of gigabytes, far past any one desk machine or consumer GPU. Introduce the cable before the cluster: every Spark ships with ConnectX-7 networking whose QSFP ports carry up to 200 Gb/s using RDMA, which is how separate machines hand each other pieces of one model. Then the week's news lands as the unlock: at GTC Berlin, NVIDIA raised the officially supported cluster from four nodes to eight, and eight times 128 GB is 1 TB. Make it concrete with NVIDIA's own benchmark: the full GLM 5.3, 753B parameters with 40B active per token, is about 470 GB in NVFP4 and decoded at 31 TPS for a single user across eight Sparks. Close on the two catches an engineer will raise: the inter-node link moves roughly 25 GB/s against 273 GB/s inside a single node, so this rig fits big models rather than making small ones 8x faster; and the terabyte is eight boxes plus a switch, with the cheap $4,999 SKU being the 64 GB model, not the 128 GB one the 1 TB cluster needs.

## Claims
1. **At GTC Berlin, NVIDIA announced official support for eight-node DGX Spark clusters, scaling unified memory to 1 TB.**
   - Source: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes, https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
   - Tier: docs | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "At GTC Berlin, NVIDIA announced official support for eight-node DGX Spark clusters, scaling unified memory to 1 TB and opening the door to frontier-class models, multi-agent workloads, and near-linear pre-training"
2. **Cluster memory scales per node: a single DGX Spark provides 128 GB of unified memory; four nodes reach 512 GB; eight nodes reach 1 TB.**
   - Source: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes, https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
   - Tier: docs | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "A single DGX Spark provides 128 GB of unified memory; four nodes reach 512 GB; eight nodes reach 1 TB."
3. **The full GLM 5.3 (753B) checkpoint runs across the 8x 128 GB cluster and is about 470 GB in NVFP4.**
   - Source: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes, https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
   - Tier: docs | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "The model is about 470 GB in NVFP4, measured with MTP3 at concurrency one, four, and eight." (Table 1 caption: "Full GLM 5.3 (nvidia/GLM-5.3-NVFP4) performance on an eight-node DGX Spark cluster.")
4. **On that eight-node cluster, GLM 5.3 decoded at 31 TPS total at concurrency 1 and 67 TPS at concurrency 8, with prefill of 1,600 TPS.**
   - Source: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes, https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
   - Tier: docs | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "Full GLM 5.3 (nvidia/GLM-5.3-NVFP4) performance on an eight-node DGX Spark cluster." (Table 1 rows: concurrency 1 decodes 31 total TPS; concurrency 8 decodes 67 total TPS; prefill is 1,600 TPS at all concurrencies.)
5. **GLM 5.3 is a Mixture-of-Experts model with 753B parameters in total and 40B activated, and context length up to 1M.**
   - Source: nvidia/GLM-5.3-NVFP4 model card, https://huggingface.co/nvidia/GLM-5.3-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "Number of Model Parameters: 753B in total and 40B activated" and "Context length up to 1M"
6. **Each DGX Spark has two QSFP ConnectX-7 ports, and each port provides up to 200 Gigabits per second (Gb/s).**
   - Source: ConnectX-7 Networking, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "Each DGX Spark has two QSFP ports (sometimes called "ConnectX-7 ports") on the back of the device. Each port provides up to 200 Gigabits per second (Gb/s)"
7. **Decode throughput scales from about 12 TPS on one node to 52 TPS on eight nodes on Qwen3.8-27B (NVFP4), with the ROCEnante backend delivering a 4.43x speedup vs. 3.05x without it at eight nodes.**
   - Source: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes, https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
   - Tier: docs | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "decode throughput scales strongly with node count, from about 12 TPS on one node to 52 TPS on eight nodes." and "At eight Spark nodes, ROCEnante delivers a 4.43x speedup vs. 3.05x without it"
8. **The cluster link is far slower than a node's own memory: a measured 196 Gb/s (about 24.5 GB/s) between two Sparks versus 273 GB/s of memory bandwidth inside one Spark, roughly eleven times slower.**
   - Source: DGX Spark Memory Bandwidth: 273 GB/s vs the 25 GB/s Link, https://petronellatech.com/blog/dgx-spark-cluster-bandwidth-what-400g-really-means/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "we measured 196 Gb/s over a single 0.5 m DAC with two RDMA streams running" and "The link between nodes is roughly eleven times slower than the memory inside a single node"
9. **ServeTheHome ran an 8-node GB10 cluster with 1TB of memory in February 2026, before NVIDIA supported it, to run Kimi K2.5 locally.**
   - Source: BIG AI Cluster Little Power the 8x NVIDIA GB10 Cluster, https://www.servethehome.com/big-cluster-little-power-the-8x-nvidia-gb10-cluster-marvell-cisco-ubiquiti-qnap-arm/
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
   - Quote: "In February, we amassed eight NVIDIA GB10 units so we could build something that was nowhere near supported." and "we had an 8-node NVIDIA GB10 cluster up and running with 1TB of memory, 160 Arm cores"
10. **The DGX Spark 64GB partner configuration rolls out on Friday, Oct. 23, starting at $4,999, while the 128 GB model lists at about $6,950 as of October 2026.**
    - Source: NVIDIA DGX Spark 64GB Gives Developers More Ways to Build and Scale Local AI, https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/
    - Tier: docs | Confidence: high | Accessed: 2026-10-23 | Via: web_extract
    - Quote: "DGX Spark 64GB is available from Acer, ASUS, Dell, Gigabyte, HP and MSI on Friday, Oct. 23, starting at $4,999." (The $6,950 figure for the 128 GB model is from https://www.spheron.network/gpu-price/gb10/, accessed 2026-10-23: "the 128GB model lists at about $6,950 as of October 2026".)

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | eight-node cluster unified memory | 1 TB | https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/ | "eight nodes reach 1 TB" |
| 2 | GLM 5.3 checkpoint size, quantized | about 470 GB | https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/ | "The model is about 470 GB in NVFP4" |
| 3 | GLM 5.3 parameters | 753B in total and 40B activated | https://huggingface.co/nvidia/GLM-5.3-NVFP4 | "Number of Model Parameters: 753B in total and 40B activated" |
| 4 | GLM 5.3 decode on 8-node cluster, one user | 31 TPS | https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/ | Table 1: "Decode, total (TPS)" = 31 at concurrency 1 |
| 5 | per-port cluster interconnect speed | up to 200 Gigabits per second (Gb/s) | https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html | "Each port provides up to 200 Gigabits per second (Gb/s)" |
| 6 | memory bandwidth inside one Spark | 273 GB/s | https://petronellatech.com/blog/dgx-spark-cluster-bandwidth-what-400g-really-means/ | "delivering 273 GB/s of memory bandwidth" |
| 7 | DGX Spark 64GB partner price, Oct 23 | starting at $4,999 | https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/ | "starting at $4,999" |
| 8 | DGX Spark 128 GB list price, Oct 2026 | about $6,950 | https://www.spheron.network/gpu-price/gb10/ | "the 128GB model lists at about $6,950 as of October 2026" |

## Analogy candidates
- **Eight branch libraries with one courier**: each Spark is a branch that holds 128 GB of shelves and serves readers at its own counter speed (273 GB/s); the 200 Gb/s cable is the inter-library courier (about 25 GB/s); pooling eight branches fits a collection too big for any one (a 470 GB model in a 1 TB system), but every book that has to change branches waits on the courier. Breaks when: the model's layers must sync every single token (tensor-parallel all-reduce), because then the courier, not the shelves, sets the pace -- which is exactly why eight nodes decode at 4.43x, not 8x.

## Misconceptions
- Myth: NVIDIA shipped a single desk machine with 1 TB of memory. Reality: the 1 TB is the aggregate of eight 128 GB systems linked over ConnectX-7; no single DGX Spark contains 1 TB (claim 2).
- Myth: eight Sparks make inference eight times faster. Reality: nodes exchange tensors over a link measured at 196 Gb/s (about 24.5 GB/s) while each node's own memory moves 273 GB/s, so decode scaled to 4.43x at eight nodes in NVIDIA's own benchmark (claims 7, 8).
- Myth: the terabyte cluster costs eight times the $4,999 headline price. Reality: $4,999 is the 64 GB partner configuration rolling out Oct 23; the terabyte needs 128 GB units listing at about $6,950 each, which is about $55,600 at list before the switch and cables (claim 10).

## Glossary
- **DGX Spark**: NVIDIA's desk-side AI computer built on the GB10 chip, with 128 GB of unified memory.
- **GB10 Grace Blackwell Superchip**: the chip inside DGX Spark that pairs a 20-core Arm CPU with a Blackwell GPU over one shared memory pool.
- **Unified memory**: one pool of memory the CPU and GPU both address directly, so model weights are never copied between them.
- **Quantization (NVFP4, Q8)**: storing each model weight in fewer bits, shrinking the checkpoint at some quality cost; NVFP4 is 4-bit, Q8 is 8-bit.
- **ConnectX-7**: the network card built into every DGX Spark, whose QSFP ports link Sparks into a cluster.
- **QSFP port**: the dense connector on the back of a Spark that carries the clustering cable at up to 200 Gb/s.
- **RDMA over Converged Ethernet (RoCE)**: a way for one machine to write directly into another's memory over Ethernet, the transport Spark clusters use to exchange tensors.
- **Tensor parallelism**: splitting one model's layers across several machines so each holds a slice and they synchronize every token.
- **Mixture of experts (MoE)**: a model architecture in which only a fraction of the total parameters activates for any given token.
- **Tokens per second (TPS)**: how fast a model generates text; the number a local user actually feels.

## Unverified
- Meta's Muse Spark Open is an 816B-parameter open model, and at 8-bit quantization its weights alone would need about 816 GB, which arithmetic says fits the 1 TB pool with limited headroom for the KV cache; no tier 1-3 page fetched this run states that model's size or that fit.
- A full eight-unit 128 GB cluster at today's prices computes to about $55,600 at list (8 x $6,950), but no fetched page prices a complete eight-Spark build, and OEM street pricing varies.
- Any tokens-per-second figure measured on our own hardware: NVIDIA's 31 TPS for GLM 5.3 and the roughly 80 TPS it reports for GLM 5.3 Flash are vendor measurements, not independently reproduced.
- Whether NVIDIA Sync's one-click eight-node Cluster Assistant arrives this month or by the end of the year: NVIDIA's own posts say both (see Notes).

## Suggested outline
1. Hook on the concrete fact: NVIDIA this week officially blessed eight desk boxes linked into 1 TB of memory, enough to hold a frontier model's weights without a datacenter.
2. The mechanism: one Spark is 128 GB of unified memory; a 470 GB GLM 5.3 cannot start on one; eight Sparks hold it and decoded at 31 tokens per second in NVIDIA's own test.
3. The honest catch: the cable moves about 25 GB/s against 273 GB/s inside a box, so the cluster buys capacity, not 8x speed; hobbyists at ServeTheHome ran this exact rig months before NVIDIA supported it, and the terabyte costs eight 128 GB units at about $6,950 each, not the $4,999 headline SKU.

## Viewer situation
You've got a gaming PC or a Mac, you watch frontier models go by, and you assume anything with hundreds of billions of parameters needs a cloud account and someone else's datacenter.

## Has process
false

## Objection
A cluster of LPDDR5x boxes talking over a roughly 25 GB/s link is not a frontier rig: a single rented H200 moves 4.8 TB/s, and 31 tokens per second on a 753B model is a vendor demo, not a product.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/ | Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes | docs | web_extract | 2026-10-23 |
| 2 | https://blogs.nvidia.com/blog/local-ai-gtc-rtx-dgx-spark-station-sync/ | Bringing the Spark to Europe: Local Intelligence Powers Next Wave of Agents | docs | web_extract | 2026-10-23 |
| 3 | https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/ | NVIDIA DGX Spark 64GB Gives Developers More Ways to Build and Scale Local AI | docs | web_extract | 2026-10-23 |
| 4 | https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html | ConnectX-7 Networking, DGX Spark User Guide | primary | web_extract | 2026-10-23 |
| 5 | https://docs.nvidia.com/dgx/dgx-spark/release-notes.html | DGX Spark Release Notes | primary | web_extract | 2026-10-23 |
| 6 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | Personal AI Supercomputer Powered by Blackwell, NVIDIA DGX Spark | primary | web_extract | 2026-10-23 |
| 7 | https://huggingface.co/nvidia/GLM-5.3-NVFP4 | nvidia/GLM-5.3-NVFP4 model card | primary | web_extract | 2026-10-23 |
| 8 | https://www.guru3d.com/story/nvidia-dgx-spark-clusters-can-now-scale-to-eight-systems-and-1tb-of-unified-memory/ | NVIDIA DGX Spark Clusters Can Now Scale to Eight Systems and 1TB of Unified Memory | docs | web_extract | 2026-10-23 |
| 9 | https://www.servethehome.com/big-cluster-little-power-the-8x-nvidia-gb10-cluster-marvell-cisco-ubiquiti-qnap-arm/ | BIG AI Cluster Little Power the 8x NVIDIA GB10 Cluster | benchmark | web_extract | 2026-10-23 |
| 10 | https://petronellatech.com/blog/dgx-spark-cluster-bandwidth-what-400g-really-means/ | DGX Spark Memory Bandwidth: 273 GB/s vs the 25 GB/s Link | benchmark | web_extract | 2026-10-23 |
| 11 | https://www.spheron.network/gpu-price/gb10/ | NVIDIA GB10 (DGX Spark) Price: $6,950, Specs and Buy vs Rent | benchmark | web_extract | 2026-10-23 |
| 12 | https://www.techpowerup.com/forums/threads/nvidia-launches-dgx-spark-64-gb-desktop-ai-systems.353347/ | NVIDIA Launches DGX Spark 64 GB Desktop AI Systems | docs | web_extract | 2026-10-23 |

## Notes
Conflict on NVIDIA Sync timing: the GTC news post (source 2) says "NVIDIA Sync to support eight DGX Sparks and add Model Launcher this month," while the technical blog (source 1) says "Support for eight-node clusters in NVIDIA Sync is coming by the end of the year"; today the eight-unit path is manual configuration, and the Cluster Assistant in current docs handles up to three systems direct or four through a switch (sources 4, 5). Trust the technical blog for engineering state and the news post for intent; the video should say "manual configuration today, assistant coming." The NVIDIA product page (source 6) still markets "up to four DGX Spark systems," lagging the announcement. NVIDIA's performance numbers are vendor benchmarks; the only independent corroboration fetched is Petronella's link measurement and ServeTheHome's build. Guru3D (source 8) usefully flags that the 1 TB is aggregate, not single-device. The angle's "three outlets covered it" was not verified as a count.
