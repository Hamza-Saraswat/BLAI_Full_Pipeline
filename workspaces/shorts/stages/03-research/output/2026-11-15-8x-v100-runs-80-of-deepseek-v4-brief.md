---
slug: 2026-11-15-8x-v100-runs-80-of-deepseek-v4
stage: 03-research
topic: "V100s are not dead: a cited 80%-of-model measurement from an 8-card lawyer server"
depth: standard
generated_at: 2026-11-15T12:38:36Z
sources: 8
hub: "[[videos/2026-11-15-8x-v100-runs-80-of-deepseek-v4]]"
---

# Research brief: V100s are not dead -- an 8-card lawyer server runs 80% of DeepSeek V4.1 Flash at NVFP4

## Summary

The thesis lands on one feat: a lawyer's server of eight used 2018-era Tesla V100s runs DeepSeek V4.1 Flash well enough for daily legal work by promoting only the model's most-used experts to NVFP4 while the rest stay at 2-bit. The most arresting number is that between 80% and 86% of decode routes land on those NVFP4 experts, achieved by keeping 5,949 of 15,360 experts (about 38.7%) at high precision inside 256 GiB of VRAM. The strongest concrete case is the fidelity gain measured against NVIDIA's own NVFP4 build of the same model: same next token went up to 95.1% from 92.2%, KL divergence fell to 0.079 nats from 0.196, and changed answers across 513 multiple-choice questions fell from 79 to 8. What could not be verified: the builder's identity, the true primary Reddit thread (blocked this run), and whether the two-request setup keeps the measured fidelity. Conflict: the model's size is framed differently by NVIDIA's model card (approximately 400 GiB checkpoint, 552B backbone) and Tom's Hardware (269 GiB at official precision by the builder's estimate, 248.8GB at 2-bit, 556GB package), which this brief reports side by side without averaging.

## Thesis

Eight used 2018-era V100s still run DeepSeek V4.1 Flash well enough for daily legal work, because the model only needs its most-used experts at high precision -- about 80% of the work now lands on NVFP4 experts -- while the rest stay at 2-bit and the whole thing fits in 256 GiB of VRAM.

## Explanation path

Start with the assumption the video attacks: that a GPU from 2018 with no modern quantization support is scrap. Establish what the builder actually has: eight Tesla V100-SXM2-32GB cards, 32GB of HBM2 each at 900 GB/s, 256 GiB total, bought used at about $2,400 per four-GPU board. Then establish what the model demands: DeepSeek V4.1 Flash is a Mixture-of-Experts model whose 384 routed experts per layer across 40 layers total 15,360 experts, about 269 GiB at official precision by his estimate -- more than the cards hold. The trick, understood before any speed number: MoE means only some experts work on each token, so he keeps every expert on the cards at 2-bit and swaps the most-used ones up until the cards are full -- 5,949 experts, about 38.7%, at precisely NVFP4, and between 80% and 86% of decode routes land on those NVFP4 experts. Fidelity against Nvidia's own NVFP4 build of the same model: same next token 95.1% of the time (up from 92.2%), KL divergence 0.079 nats (down from 0.196), and multiple-choice answers that change dropped from 79 to 8 across 513 questions. The cost is speed: code output fell from 160-215 tokens per second to 150-180. Close on the honest catch: the V100s are on borrowed time -- R580 is the last Nvidia driver branch to support Volta -- and NVFP4 is a Blackwell-native format the V100 does not accelerate in hardware, so this is a hand-ported labor of love that proves the memory-bandwidth floor, not a turnkey recipe.

## Claims

1. **A lawyer's server of eight used Tesla V100-SXM2-32GB GPUs (256 GiB VRAM total) runs DeepSeek V4.1 Flash with about 38.7%, or 5,949, of the model's 15,360 experts at NVFP4 precision and the rest at 2-bit, and between 80% and 86% of decode routes land on the NVFP4 experts.**
   - Source: Lawyer upgrades eight-V100 private AI server to run 80% of DeepSeek V4.1 Flash at 4-bit NVFP4 precision, https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-upgrades-eight-v100-private-ai-server-to-run-80-percent-of-deepseek-v4-1-flash-at-4-bit-nvfp4-precision-adds-1tb-of-ram-an-nvidia-rtx-3090-and-fixes-crashes-caused-by-a-bad-psu
   - Tier: docs | Confidence: high | Accessed: 2026-11-15 | Via: curl (direct fetch, HTML parsed)
   - Quote: "the workaround is to keep every expert on the cards at 2-bit and swap the most-used ones up until the cards are full, which in this case came out to about 38.7%, or 5,949 experts, at precisely NVFP4" and "between 80% and 86% of decode routes ... land on the NVFP4 experts, lowest for general text and highest for source code"
2. **The near-NVFP4 build raised fidelity against Nvidia's own NVFP4 reference build of the same model: same next token went up to 95.1% from 92.2%, KL divergence fell to 0.079 nats from 0.196, and across 513 multiple-choice questions the changed answers fell from 79 to 8, with accuracy about the same.**
   - Source: same Tom's Hardware article as claim 1.
   - Tier: docs | Confidence: high | Accessed: 2026-11-15 | Via: curl (direct fetch, HTML parsed)
   - Quote: "Same next token, or how often a build picks the same next token as the reference, went up to 95.1% from 92.2%. For KL divergence ... it went down to 0.079 nats from 0.196. In measuring multiple-choice answers that change, across 513 questions ... it went from 79 different to just 8."
3. **The precision upgrade cost speed: code output fell to 150-180 tokens per second, from 160-215, and the new build's Hugging Face package is about 556GB while the 2-bit weights were 248.8GB.**
   - Source: same Tom's Hardware article as claim 1.
   - Tier: docs | Confidence: high | Accessed: 2026-11-15 | Via: curl (direct fetch, HTML parsed)
   - Quote: "The upgrade costs speed: code output falls to 150-180 tokens per second, from 160-215" and "With the 2-bit build, the weights were 248.8GB; the new build's Hugging Face package is about 556GB."
4. **The eight Tesla V100-SXM2-32GB cards each have 32GB of HBM2 at 900 GB/s and connect over SXM2 boards with NVLink inside each four-card board for 128GB per board, while the two boards only communicate over PCIe; the four-GPU boards cost about $2,400 apiece when bought.**
   - Source: Lawyer builds private AI server with eight used Nvidia V100 GPUs, https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board
   - Tier: docs | Confidence: high | Accessed: 2026-11-15 | Via: curl (direct fetch, HTML parsed)
   - Quote: "The eight Tesla V100-SXM2-32GB cards, each with 32GB of HBM2 at 900 GB/s ... all four cards are NVLinked ... for 128GB per board, but the two boards only communicate over PCIe" and "The four-GPU boards cost about $2,400 apiece when the builder bought them."
5. **NVIDIA's official NVFP4 quantization of DeepSeek V4.1 Flash is a 552B-backbone Mixture-of-Experts model (16B active during decode) whose checkpoint is approximately 400 GiB and whose converted routed experts span 384 experts across 40 layers, matching the layout the lawyer's build exploits.**
   - Source: nvidia/DeepSeek-V4.1-Flash-1017-NVFP4 model card, https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4
   - Tier: primary | Confidence: high | Accessed: 2026-11-15 | Via: web_extract
   - Quote: "Number of Model Parameters: 552B backbone in total, 8B activated during prefill and 16B during decode, plus 196B Engram conditional memory" and "The converted projections are w1, w2, and w3 for 384 experts across 40 layers" and "The checkpoint is approximately 400 GiB (source: approximately 475 GiB) in 48 safetensors shards."
6. **NVFP4 is Nvidia's 4-bit floating point format introduced with the Blackwell architecture, using an E2M1 value with a shared FP8 scale per 16-value block plus a second-level FP32 scale per tensor, and it cuts model memory roughly 3.5x relative to FP16.**
   - Source: Introducing NVFP4 for Efficient and Accurate Low-Precision Inference, https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/
   - Tier: primary | Confidence: high | Accessed: 2026-11-15 | Via: web_extract
   - Quote: "NVFP4 is an innovative 4-bit floating point format introduced with the NVIDIA Blackwell GPU architecture" and "This strategy applies a fine-grained E4M3 scaling factor to each 16-value micro-block" and "The format cuts model memory footprint by approximately 3.5x relative to FP16."
7. **NVIDIA's R580 release notes list the NVIDIA V100 (Volta) among the supported GPUs for the Release 580 family of data center drivers for Linux, the branch NVIDIA and press describe as the last to support Maxwell, Pascal, and Volta.**
   - Source: Version 580.126.09(Linux) release notes, https://docs.nvidia.com/datacenter/tesla-release-notes-580-126-09/index.html
   - Tier: primary | Confidence: high | Accessed: 2026-11-15 | Via: web_extract
   - Quote: the supported-GPUs table lists "NVIDIA Volta | NVIDIA V100" (version 580.126.09, Linux driver release date 01/13/2026).
8. **Phoronix reported that NVIDIA's deprecation schedule states "The release 580 series will be the last to support GPUs based on the Maxwell, Pascal, and Volta architectures.", confirming the V100 is on a legacy driver branch with no successor.**
   - Source: NVIDIA Confirms 580 Linux Driver Is The Last For Maxwell / Pascal / Volta, https://www.phoronix.com/news/NVIDIA-580-Linux-Driver-Last-HW
   - Tier: docs | Confidence: high | Accessed: 2026-11-15 | Via: web_extract
   - Quote: "The release 580 series will be the last to support GPUs based on the Maxwell, Pascal, and Volta architectures."
9. **The Tesla V100 specification page lists 32/16 GB HBM2 capacity at 900 GB/s bandwidth, NVLink at 300 GB/s bi-directional, PCIe at 32 GB/s, and 300 WATTS max consumption for the NVLink version.**
   - Source: NVIDIA Tesla V100 specifications, https://www.nvidia.com/en-gb/data-center/tesla-v100/
   - Tier: primary | Confidence: high | Accessed: 2026-11-15 | Via: web_extract
   - Quote: "CAPACITY 32/16 GB HBM2, BANDWIDTH 900 GB/s" and "NVLink 300 GB/s, PCIe 32 GB/s" and "POWER Max Consumption 300 WATTS."
10. **DeepSeek's own model card describes DeepSeek-V4.1-Flash-1017 as a natively multimodal Mixture-of-Experts model with support for contexts of up to one million tokens and a recommended context window of 1M tokens.**
    - Source: deepseek-ai/DeepSeek-V4.1-Flash-1017 model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
    - Tier: primary | Confidence: high | Accessed: 2026-11-15 | Via: web_extract
    - Quote: "a natively multimodal Mixture-of-Experts (MoE) model with a Causal Encoder-Decoder (CED) architecture, Compressed Sparse Attention 2 (CSA2), and support for contexts of up to one million tokens" and "context_window 1M tokens."

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | share of decode routes landing on NVFP4 experts (one request at a time) | 80% to 86% | (Tom's Hardware update article, claim 1) | "between 80% and 86% of decode routes ... land on the NVFP4 experts" |
| 2 | experts kept at NVFP4 in the 8x V100 build | 5,949 experts (about 38.7%) | (Tom's Hardware update article, claim 1) | "about 38.7%, or 5,949 experts, at precisely NVFP4" |
| 3 | total VRAM across eight 32GB V100s | 256 GiB | (Tom's Hardware update article, claim 1) | "eight 32GB V100s have 256 GiB in total before anything else is loaded" |
| 4 | code output before / after the precision upgrade | 160-215 tokens per second to 150-180 tokens per second | (Tom's Hardware update article, claim 3) | "code output falls to 150-180 tokens per second, from 160-215" |
| 5 | same-next-token fidelity vs NVIDIA's NVFP4 reference | 95.1% (up from 92.2%) | (Tom's Hardware update article, claim 2) | "went up to 95.1% from 92.2%" |
| 6 | changed multiple-choice answers across 513 questions | 79 to 8 | (Tom's Hardware update article, claim 2) | "it went from 79 different to just 8" |
| 7 | cost per four-GPU SXM2 board when bought | about $2,400 | (Tom's Hardware first article, claim 4) | "The four-GPU boards cost about $2,400 apiece when the builder bought them" |
| 8 | per-card memory bandwidth of the V100 (32GB HBM2) | 900 GB/s | (NVIDIA Tesla V100 specifications, claim 9) | "BANDWIDTH 900 GB/s" |

## Analogy candidates

- **Vehicle**: A workshop where every tool hangs on the wall at 2-bit, but the handful of tools you actually reach for all day get the full-quality version on the bench.
  - Mapping: All 15,360 experts stay resident at 2-bit; the 5,949 most-used ones get promoted to NVFP4 so that 80-86% of actual work runs at high precision.
  - Breaks when: the viewer assumes the choice is permanent: which experts are "most-used" was counted from a mix of four kinds of text, and adding a second concurrent request shrinks the NVFP4 set (6,215 / 5,949 / 5,663 experts for one / two / three slots), pushing one to two points of calls back to 2-bit.

## Misconceptions

- Myth: V100s are dead for AI in 2026; nothing modern runs on them. Reality: A production legal server runs DeepSeek V4.1 Flash daily on eight of them at 150-180 tokens per second for code and 93.5-105.5 tokens per second for legal writing (claim 1), though the R580 driver branch is the last to support Volta (claims 7 and 8).
- Myth: You need to fit the whole model at high precision or the quality collapses. Reality: The build keeps every expert at 2-bit and promotes only the most-used 38.7% to NVFP4; fidelity to NVIDIA's full NVFP4 reference actually improved, with same next token at 95.1% and changed multiple-choice answers down from 79 to 8 (claim 2).

## Glossary

- **expert**: one of the specialized sub-networks inside a Mixture-of-Experts model that gets routed only some of the work; DeepSeek V4.1 Flash has 384 per layer across 40 layers, 15,360 in all.
- **Mixture-of-Experts (MoE)**: a model design where a router picks a few experts per token instead of using every parameter, so memory cost is huge but per-token compute is small.
- **NVFP4**: NVIDIA's 4-bit floating point format from the Blackwell era: an E2M1 value with a shared FP8 scale per 16-value block plus an FP32 scale per tensor, cutting memory roughly 3.5x versus FP16.
- **2-bit quantization**: compressing model weights to two bits each, which slashes memory about 8x versus 16-bit at the cost of precision; the fallback tier for this build's less-used experts.
- **decode route**: one call to an expert while the model writes output tokens; the share of routes landing on NVFP4 experts is the build's headline 80-86% figure.
- **same next token**: a fidelity check: how often a build picks the identical next token as a reference build of the same model; higher means closer behavior, not higher accuracy.
- **KL divergence**: a distance measure between two probability distributions, here how far the build's next-token probabilities sit from the reference's, measured in nats; lower is closer.
- **R580**: NVIDIA's Release 580 driver family for Linux, the last branch to support Maxwell, Pascal, and Volta GPUs including the V100.
- **tokens per second**: how fast a model emits output tokens, the everyday speed number for local inference.
- **SXM2**: NVIDIA's mezzanine socket for data center GPUs; the builder's V100s plug into SXM2 boards with NVLink inside each four-card board instead of PCIe slots.
- **Engram tables**: DeepSeek V4.1's conditional-memory lookup tables, about 110GB of which stay in system RAM in the lawyer's build rather than on the GPUs.

## Unverified

- The builder's identity as Nick Mermiges, founder of PLI Labs and proprietarylegal.ai, is reported by Tom's Hardware from Reddit comments and was not independently confirmed.
- The builder's claim that the V100s are on "borrowed time" after R580 suggests a specific end-of-support date for Volta that no fetched page states.
- That the V100's Tensor Cores lack any hardware support for FP4 formats, leaving the NVFP4 math to custom kernels, is plausible from the format's Blackwell introduction but was not stated on a fetched page.
- Used V100 SXM2 32GB cards now selling on eBay for about $900, more than double the roughly $400 apiece from the post, is a market observation from the first article not re-checked this run.
- The builder's estimate that 50% to 60% of his LLM workflows can run on the box instead of frontier models is his own figure and no independent page corroborates it.
- Whether the two-request setup he now runs preserves the fidelity numbers measured on the single-request build is untested; the tests ran on the build's first release.
- That current-generation consumer hardware (for example a 2-card RTX 5090 setup or a DGX Spark) could match the 8x V100 throughput at lower power is an expectation, not a fetched measurement.

## Suggested outline

1. The 80% number on screen first: eight V100s from 2018 and the share of work now running at high precision.
2. Name the machine: a lawyer's private server, eight used Tesla V100s, 256 GiB of VRAM, built so case files never leave the office.
3. The myth being busted: everyone counts V100s out -- no modern quantization support, last driver branch coming -- yet daily legal work runs on them today.
4. The mechanism in one idea: Mixture-of-Experts means only some experts work per token, so promote the most-used 5,949 of 15,360 to NVFP4 and leave the rest at 2-bit.
5. The payoff numbers: 80-86% of decode routes on NVFP4 experts, same next token 95.1%, changed answers on 513 questions down from 79 to 8.
6. The honest catch: speed dropped (code 160-215 down to 150-180 tokens per second), R580 is the last Volta driver branch, and NVFP4 is a Blackwell format ported by hand to Volta.
7. What the viewer takes home: old data center cards are priced by their memory bandwidth, not their age -- 900 GB/s per card still moves a modern MoE if you quantize where it counts.

## Viewer situation

You've been told your old GPUs are useless for modern AI, but you keep seeing used data center cards go for the price of a gaming GPU.

## Has process

false

## Objection

A single new GPU with native FP4 support would beat eight power-hungry 2018 cards on performance per watt, and the R580 driver branch is the end of the line anyway.

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-upgrades-eight-v100-private-ai-server-to-run-80-percent-of-deepseek-v4-1-flash-at-4-bit-nvfp4-precision-adds-1tb-of-ram-an-nvidia-rtx-3090-and-fixes-crashes-caused-by-a-bad-psu | Lawyer upgrades eight-V100 private AI server to run 80% of DeepSeek V4.1 Flash at 4-bit NVFP4 precision (Tom's Hardware) | docs | curl | 2026-11-15 |
| 2 | https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board | Lawyer builds private AI server with eight used Nvidia V100 GPUs (Tom's Hardware) | docs | curl | 2026-11-15 |
| 3 | https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4 | nvidia/DeepSeek-V4.1-Flash-1017-NVFP4 model card | primary | web_extract | 2026-11-15 |
| 4 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 | deepseek-ai/DeepSeek-V4.1-Flash-1017 model card | primary | web_extract | 2026-11-15 |
| 5 | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ | Introducing NVFP4 for Efficient and Accurate Low-Precision Inference (NVIDIA Technical Blog) | primary | web_extract | 2026-11-15 |
| 6 | https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-126-09/index.html | Version 580.126.09(Linux) release notes (NVIDIA) | primary | web_extract | 2026-11-15 |
| 7 | https://www.phoronix.com/news/NVIDIA-580-Linux-Driver-Last-HW | NVIDIA Confirms 580 Linux Driver Is The Last For Maxwell / Pascal / Volta (Phoronix) | docs | web_extract | 2026-11-15 |
| 8 | https://www.nvidia.com/en-gb/data-center/tesla-v100/ | NVIDIA Tesla V100 specifications | primary | web_extract | 2026-11-15 |

## Notes

Numbers come from Tom's Hardware' reporting on the builder's own measurements (Nov. 5 for 2-bit, Nov. 12 for near-NVFP4; greedy decoding, thinking off, one request at a time), so they are self-reported bench numbers relayed by tech press (tier 2) rather than an independent lab run; treat the 80% figure as a builder measurement, not a vendor spec. Two conflict notes. First, parameter framing differs: NVIDIA's model card says 552B total backbone with 16B active during decode plus 196B Engram conditional memory, while Tom's Hardware' first article says the model is compressed to mostly 2 bits with weights totaling 248.8GB and the second article estimates about 269 GiB at official precision; the card's approximately 400 GiB NVFP4 checkpoint is the authoritative size for the reference build the builder measures against. Second, the V100 spec page lists 900 GB/s per card for the NVLink version (1134 GB/s for V100S PCIe), matching the article's per-card figure. The Reddit thread (r/homelab, u/TumbleweedNew6515) is the true primary source but was not fetchable this run (403 from reddit.com and old.reddit.com); every number above is grounded in the two Tom's Hardware articles instead. FireCrawl unavailable (402 payment required), so discovery used web_search and acquisition used web_extract plus direct curl; the browser tool was down (chrome-not-running).
