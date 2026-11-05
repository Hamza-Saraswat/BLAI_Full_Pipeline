---
slug: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh
stage: 03-research
topic: "Kimi K3.1 Pro open-weights drop: 1.56 TB of MXFP4 and what actually runs on your hardware"
depth: standard
generated_at: 2026-11-05T12:42:16Z
sources: 12
hub: "[[videos/2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh]]"
---

# Research brief: Kimi K3.1 Pro open-weights drop -- 1.56 TB of MXFP4 and what actually runs on your hardware

## Summary
Moonshot put the full weights of a frontier-class model on Hugging Face three days ago, and the drop fits no single consumer machine on earth: the repo stores 1561355732732 bytes (1.56 TB) against the 128 GB of a DGX Spark or the 24 GB of a consumer RTX card. The concrete case for the video is the precedent, not the promise: Unsloth already crushed the same-size Kimi K3 base from 1.56 TB to a 594 GB 1-bit build that still demands 610 GB of memory and keeps only 78.875% top-1 agreement. What could not be verified: every K3.1-Pro-specific quant size (an 816.9 GB MLX build, a 928 GB storage-offload build) comes from community repos, and no tokens-per-second number on any named machine exists yet. One conflict: Terminal-Bench 4.0 is 65.7 in Moonshot's own table but 67% in Artificial Analysis's write-up, run under different harness settings.

## Thesis
Kimi K3.1 Pro is the first frontier-class open-weights drop that no viewer can run as shipped -- 1.56 TB of weights against a 128 GB Spark or a 24 GB card -- so the real local-AI story is the sizing math and the community-quant path that decides what, if anything, you will ever run of it.

## Explanation path
Start with the event, because it is concrete: 1.56 TB of weights, in 96 shards, free to download, posted three days ago. Before any machine appears, make the number honest: it is a storage figure, and it is mixed precision -- the routed experts are 4-bit MXFP4 while attention, shared experts, router, embeddings and the vision tower stay BF16 or FP32, which is why 2.8T parameters land at 1.56 TB instead of roughly half that. Mixture-of-experts comes next because it is the crux and the most misunderstood part: each token touches only 104B of the 2.8T parameters, so the model is cheap per token, but every one of the 896 experts must still be reachable in memory because any token can route to any expert. Only once that is established do the machines arrive, from the 24 GB consumer card to the 128 GB DGX Spark (with NVIDIA's own 200-billion-parameter inference ceiling) to the 512GB Mac Studio, so the viewer feels the gap compound instead of hearing three disconnected specs. After the dead end, open the two escape hatches: quantization, with the Kimi K3 594 GB precedent and its measured accuracy cost, and streaming experts from storage, with its speed cost. Land on what the viewer does tonight: the API at $2.00 / MTok input, a model that actually fits, and the quantization repos worth watching.

## Claims
1. **Kimi K3.1 Pro is a Mixture-of-Experts model with 2.8T total parameters and 104B activated parameters per token, published open-weight on Hugging Face.**
   - Source: moonshotai/Kimi-K3.1-Pro · Hugging Face, https://huggingface.co/moonshotai/Kimi-K3.1-Pro
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "| **Architecture** | Mixture-of-Experts (MoE) | ... | **Total Parameters** | 2.8T | ... | **Activated Parameters** | 104B | ... | **Number of Experts** | 896 | ... | **Selected Experts per Token** | 16 |"
2. **The published repo occupies 1561355732732 bytes (about 1.56 TB) across 96 safetensors shards and was created on 2026-11-02, three days before this brief.**
   - Source: moonshotai/Kimi-K3.1-Pro model API (repo file listing), https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro?blobs=true
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "\"createdAt\":\"2026-11-02T04:13:51.000Z\" ... \"usedStorage\":1561355732732"
3. **Only the MoE expert weights ship quantized to 4-bit: the repo's parameter census lists 2722740830208 U8 parameters alongside 57358410752 BF16 and 11122432 F32, totaling 2780110363392 -- the mixed precision that puts 2.8T parameters at 1.56 TB rather than less.**
   - Source: moonshotai/Kimi-K3.1-Pro model API (repo file listing), https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro?blobs=true
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "\"safetensors\":{\"parameters\":{\"F32\":11122432,\"BF16\":57358410752,\"U8\":2722740830208},\"total\":2780110363392}"
4. **Moonshot announced K3.1 Pro on October 23, 2026 and committed to publishing the full weights by Nov 4.**
   - Source: Introducing Kimi K3.1 Pro (Kimi blog), https://www.kimi.ai/blog/kimi-k3-1-pro
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "The full model weights will be released by Nov 4."
5. **NVIDIA's DGX Spark carries 128 GB of coherent unified memory and NVIDIA itself rates a single unit for inference with models up to 200 billion parameters; even four Sparks pooled reach 512 GB, rated up to 700B parameters.**
   - Source: NVIDIA DGX Spark product page, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "Test, validate, and inference with AI models up to 200 billion parameters. ... 4x DGX Spark 512 GB Up to 700B parameters"
6. **Apple's Mac Studio maxes out at 512GB of unified memory on the M5 Ultra -- the largest memory pool in a consumer Mac, and still about a third of K3.1 Pro's 1.56 TB.**
   - Source: Mac Studio - Technical Specifications, https://www.apple.com/mac-studio/specs/
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "512GB unified memory (M5 Ultra with 36-core CPU and 80-core GPU)"
7. **A flagship consumer card, the GeForce RTX 4090, carries 24 GB of G6X memory -- roughly 1.5% of the download.**
   - Source: GeForce RTX 4090 Graphics Cards | NVIDIA, https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/
   - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "It's powered by the NVIDIA Ada Lovelace architecture and comes with 24 GB of G6X memory to deliver the ultimate experience for gamers and creators."
8. **Unsloth's quantization ladder for Kimi K3, the same 2.8T base model, runs from 1.56 TB at full precision down to a 594 GB dynamic 1-bit GGUF that still requires at least 610 GB of RAM plus VRAM and keeps 78.875% top-1 agreement.**
   - Source: Kimi K3 - How to Run Locally | Unsloth Documentation, https://unsloth.ai/docs/models/kimi-k3
   - Tier: docs | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "Full-precision inference requires 1.56 TB of storage and 1-bit Kimi K3 [Unsloth] Dynamic GGUF requires 594 GB (62% less)."
9. **Artificial Analysis scores K3.1 Pro at 55 on its Intelligence Index, 4th overall, and projects it as the highest-scoring open-weights model once weights ship, narrowing the open-versus-closed gap from 12 points to 3.**
   - Source: Kimi K3.1 Pro launches at 4th on the Intelligence Index | Artificial Analysis, https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks
   - Tier: benchmark | Confidence: medium | Accessed: 2026-11-05 | Via: web_extract
   - Quote: "Once the weights for K3.1 Pro are released it will be the highest-scoring open weights model and the gap between the leading open weights and proprietary models on the Intelligence Index will narrow from 12 points to 3."
10. **Moonshot's API prices kimi-k3.1-pro at $2.00 / MTok input and $10.00 / MTok output, with cached input at $0.20 / MTok.**
    - Source: Model Inference Pricing - Kimi API Platform, https://platform.kimi.ai/docs/pricing/chat
    - Tier: primary | Confidence: high | Accessed: 2026-11-05 | Via: web_extract
    - Quote: "| kimi-k3.1-pro | $2.00 / MTok | $10.00 / MTok | $0.20 / MTok | $2.00 / MTok | $4.00 / MTok |"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total weight storage on Hugging Face (the hook) | 1561355732732 bytes (about 1.56 TB) | https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro?blobs=true | "\"usedStorage\":1561355732732" |
| 2 | total parameters (all experts in memory) | 2.8T | https://huggingface.co/moonshotai/Kimi-K3.1-Pro | "| **Total Parameters** | 2.8T |" |
| 3 | activated parameters per token | 104B | https://huggingface.co/moonshotai/Kimi-K3.1-Pro | "| **Activated Parameters** | 104B |" |
| 4 | DGX Spark unified memory | 128 GB | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "Up to 128 GB Unified Memory" |
| 5 | Mac Studio maximum unified memory (M5 Ultra) | 512GB | https://www.apple.com/mac-studio/specs/ | "512GB unified memory (M5 Ultra with 36-core CPU and 80-core GPU)" |
| 6 | RTX 4090 memory (G6X) | 24 GB | https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/ | "comes with 24 GB of G6X memory" |
| 7 | Unsloth dynamic 1-bit GGUF of Kimi K3 (same 2.8T base) | 594 GB | https://unsloth.ai/docs/models/kimi-k3 | "Dynamic GGUF requires 594 GB (62% less)" |
| 8 | Kimi K3.1 Pro API input price | $2.00 / MTok | https://platform.kimi.ai/docs/pricing/chat | "| kimi-k3.1-pro | $2.00 / MTok | $10.00 / MTok | $0.20 / MTok |" |

## Analogy candidates
- **A hospital with 896 specialist doctors**: any one patient (token) only needs 16 specialists plus 2 on staff (104B active parameters), but the hospital building must house all 896 (2.8T parameters, 1.56 TB) because you cannot predict who the next patient needs. Breaks when: a hospital can page an off-site specialist and still answer within the hour -- that is disk offload, possible but painfully slow -- and the analogy hides that "how fast the specialist walks" (memory bandwidth) matters as much as building size.
- **A freight shipment of 96 crates**: the model arrives as 96 shards totalling 1.56 TB, and your loading dock (a 24 GB card) fits about 1.5% of one crate. Breaks when: crates are not interchangeable -- you cannot keep just your favorite crates, because routing decides per token which crate is needed, with no notice.

## Misconceptions
- Myth: "1.56 TB means you need 1.56 TB of RAM or nobody can run it." Reality: 1.56 TB is the storage size; a machine can technically run it with less memory by streaming experts from fast storage at a heavy speed cost, which is exactly what the community offload builds do -- Unsloth's rule of thumb is RAM+VRAM roughly equal to the quant size, "otherwise it'll still work, just much slower due to disk offloading" (claim 8).
- Myth: "It's a 4-bit model, so 2.8T parameters should weigh about half of the BF16 size." Reality: only the routed experts are MXFP4; attention, shared experts, router, embeddings and the vision tower ship BF16 or FP32, which is why the census shows 57358410752 BF16 parameters next to the packed experts (claim 3).
- Myth: "2.8T parameters means 2.8T parameters of math per token." Reality: each token activates 104B parameters -- 16 of 896 experts plus 2 shared -- so per-token compute is 104B-class while memory must still hold every expert (claim 1).

## Glossary
- **Mixture-of-Experts (MoE)**: an architecture that keeps hundreds of specialist sub-networks ("experts") and routes each token through only a few of them, so total parameters are huge but per-token compute is small.
- **Activated parameters**: the subset of an MoE model's weights that actually touches any single token (here 104B of 2.8T).
- **MXFP4**: a 4-bit floating-point weight format with 8-bit block scales, applied here during quantization-aware training so the model was trained to expect it.
- **Unified memory**: one memory pool shared by CPU and GPU (DGX Spark, Apple silicon), so a model is not split across separate VRAM and system RAM.
- **Disk offload**: keeping expert weights on NVMe storage and streaming them into memory only when a token routes to them, trading speed for capacity.
- **Community quant**: a re-encoding of a model's published weights at fewer bits per parameter (GGUF, MLX) by a third party, trading accuracy or speed for a smaller footprint.

## Unverified
- A community MLX repack of K3.1 Pro itself (AinsleyMarkov/Kimi-K3.1-Pro-2bit-UVMAX) claims the full 2.78T parameters in 816.9 GB at 2.35 bits per parameter, with no public loader in mlx-lm yet.
- inferencerlabs/Kimi-K3.1-Pro-MLXse lists a 928 GB 4-bit MLX build that offloads experts to storage for memory-constrained devices; its M3 Ultra tokens-per-second field was blank at fetch time.
- No Unsloth GGUF of K3.1 Pro existed at fetch time; the 594 GB ladder is for Kimi K3, which shares the 2.8T architecture, so treat any K3.1 Pro equivalent as expected, not available.
- Tokens per second for any K3.1 Pro build on a DGX Spark 128 GB: no first-party or benchmark number exists yet, and this channel's own measurement would be the first.
- Hacker News commenters guess the full-precision weights need "something like an 8x B300 node"; no primary source states Moonshot's own serving configuration.
- A community repo summarizes the Kimi K3.1 Pro license as MIT-style with a separate-agreement clause above US$20M revenue for model-as-a-service and a branding clause above 100M monthly active users; the LICENSE text itself was not fetched this session.

## Suggested outline
1. The drop: 1.56 TB of weights, 96 shards, free on Hugging Face three days ago.
2. What the number actually is: storage, not VRAM, and mixed precision -- experts at 4-bit, the rest at BF16.
3. Mixture-of-experts in one move: 896 experts, 16 picked per token, 104B active of 2.8T total.
4. The arithmetic against real machines: a 24 GB card holds about 1.5%, the 128 GB Spark is NVIDIA-rated to 200B parameters, the 512GB Mac Studio tops every consumer Mac and still sees a third.
5. The escape hatches: the 594 GB 1-bit precedent with its 78.875% top-1 agreement, and streaming experts from storage at a speed cost.
6. Tonight's move: the $2.00 / MTok API if you want this model, a model that fits if you want local, and the quant repos to watch.

## Viewer situation
You run local models on a 24 GB gaming card, a Mac, or the 128 GB DGX Spark, and today every feed says a frontier model just went open-weight -- so you are doing the one math that matters: does any of it fit on your machine.

## Has process
false

## Objection
"Open" here means a 1.56 TB download aimed at racks, not bedrooms: the community 594 GB crush of the previous model keeps only 78.875% top-1 agreement by its own makers' table, disk offload turns tokens per second into a slideshow, and at $2.00 / MTok input and $10.00 / MTok output the API is cheaper than the drive you would need to store the thing.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/moonshotai/Kimi-K3.1-Pro | moonshotai/Kimi-K3.1-Pro · Hugging Face | primary | web_extract | 2026-11-05 |
| 2 | https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro?blobs=true | moonshotai/Kimi-K3.1-Pro model API (repo file listing) | primary | web_extract | 2026-11-05 |
| 3 | https://www.kimi.ai/blog/kimi-k3-1-pro | Introducing Kimi K3.1 Pro (Kimi blog) | primary | web_extract | 2026-11-05 |
| 4 | https://platform.kimi.ai/docs/pricing/chat | Model Inference Pricing - Kimi API Platform | primary | web_extract | 2026-11-05 |
| 5 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | NVIDIA DGX Spark product page | primary | web_extract | 2026-11-05 |
| 6 | https://www.apple.com/mac-studio/specs/ | Mac Studio - Technical Specifications | primary | web_extract | 2026-11-05 |
| 7 | https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/ | GeForce RTX 4090 Graphics Cards (NVIDIA) | primary | web_extract | 2026-11-05 |
| 8 | https://unsloth.ai/docs/models/kimi-k3 | Kimi K3 - How to Run Locally (Unsloth Documentation) | docs | web_extract | 2026-11-05 |
| 9 | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | Kimi K3.1 Pro launches at 4th on the Intelligence Index (Artificial Analysis) | benchmark | web_extract | 2026-11-05 |
| 10 | https://news.ycombinator.com/item?id=50366999 | Kimi K3.1 Pro model weights are out (Hacker News) | community | web_extract | 2026-11-05 |
| 11 | https://huggingface.co/inferencerlabs/Kimi-K3.1-Pro-MLXse | inferencerlabs/Kimi-K3.1-Pro-MLXse · Hugging Face | community | web_extract | 2026-11-05 |
| 12 | https://huggingface.co/AinsleyMarkov/Kimi-K3.1-Pro-2bit-UVMAX | AinsleyMarkov/Kimi-K3.1-Pro-2bit-UVMAX · Hugging Face | community | web_extract | 2026-11-05 |

## Notes
Terminal-Bench 4.0 conflict: Moonshot's model card reports 65.7 (Claude Code harness) while Artificial Analysis reports 67% as the highest score of any model; different harness settings, both kept, not averaged -- name the harness on screen. The Unsloth ladder is for Kimi K3, the same 2.8T/104B base with the same 1.56 TB storage; the Hugging Face model tree listed only 3 quantizations of K3.1 Pro at fetch time, two of them MLX, so the GGUF path is precedent, not product. Units: 1561355732732 bytes is 1.56 TB decimal (about 1.42 TiB) -- keep the decimal form on screen. Apple's specs page fetched today still lists the 512GB M5 Ultra configuration. The Hacker News thread (510 points, 142 comments) spends its energy on license enforceability and who the drop is for, not on viewer-hardware sizing -- that sizing-math angle is this video's gap. A roughly 9-hours-old MXFP4 explainer was mentioned in the pick but was not located or fetched this session, so nothing here relies on it.
