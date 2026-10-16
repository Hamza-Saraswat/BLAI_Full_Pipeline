---
slug: 2026-10-16-mlx-distributed-inference-two
stage: 03-research
topic: "MLX distributed inference: two Mac Studios as one"
depth: standard
generated_at: 2026-10-16T11:40:58Z
sources: 10
hub: "[[videos/2026-10-16-mlx-distributed-inference-two]]"
---

# Research brief: MLX distributed inference: two Mac Studios as one

## Summary
Apple's machine-learning research post of 2026-10-15 is the recipe this video rides: wire two (or four) Mac Studios together with Thunderbolt 5, switch on the RDMA driver macOS 26.2 added, and MLX's JACCL backend shards one model across all of them. Most arresting number: Muse Spark Open, 816B total parameters, decodes at 24.99 tokens per second on two M5 Ultras and 36.73 on four, at 8,192-token context. Strongest concrete case: a model needing about 493GB even after 4-bit quantization runs on a desk at roughly 300W per box, not in a data center. Could not verify: achieved RDMA cable throughput (only the port spec of up to 120Gb/s) and the price of the two-Studio setup. Conflict to handle: Apple's WWDC session enables RDMA with a Settings toggle while the current MLX docs require macOS recovery, and the docs are newer and win.

## Thesis
Two Mac Studios wired together with Thunderbolt cables now act as one inference machine: macOS 26.2's RDMA and MLX's JACCL let a single model's memory span both, running the 816B-parameter Muse Spark Open at up to 24.99 tokens per second where no single Mac can hold it.

## Explanation path
Start with the wall every local runner already knows: a model's weights have to sit in memory before it can think, and the biggest open model of the moment, Muse Spark Open, holds 816B parameters, about 493GB even after 4-bit quantization, and one Mac Studio tops out at 512GB of unified memory, so once working memory is added the model cannot fit. Establish the memory ceiling before the second machine appears, so the problem is clearly capacity, not speed. Then split the model two ways: by depth, where each Mac holds consecutive layers and hands activations to its neighbor (pipeline parallelism, minimal code changes, decode speed essentially unchanged), and by width, where each Mac holds a slice of every layer and they compute in lockstep (tensor parallelism, faster, but communication-hungry). That hunger motivates the plumbing: macOS 26.2 added RDMA over Thunderbolt 5 so one Mac writes into another's memory with little overhead, and MLX v0.30.1 and later added the JACCL collectives that coordinate the group. With the plumbing named, the recipe collapses to one command, mlx.launch with a JSON hostfile, and the model is sharded across all devices automatically. Land the honest catch before the payoff: pipelined decode runs at single-machine speed, so two Studios buy capacity, not speed; speed comes from tensor parallelism, and only because the cable is fast. Close on the reframe: the unit of local AI is no longer the machine, it is the desk.

## Claims
1. **Apple published the distributed-inference recipe on 2026-10-15, showing how to run Muse Spark Open, "nearly a trillion parameters", on Mac Studios with "the latest version of MLX, released today".**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "In this post, we show how to run the latest frontier-class model -- Muse Spark Open, with nearly a trillion parameters -- right from your desk, using the latest version of MLX, released today."
2. **The model cannot fit on any single machine: Muse Spark Open would require more than 1.6TB of RAM in BF16 for the parameters alone, and about 493GB in 4-bit NVFP4, while a single Mac Studio tops out at 512GB of unified memory.**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "In a 4-bit quantized (NVFP4) format, the model memory footprint is lowered to about 493GB. Add the memory needed for intermediate computations during inference, and the model cannot fit on a single machine."
3. **MLX splits a model two ways: pipeline parallelization splits it across depth and is "extremely simple to implement, requiring only minimal code changes", while tensor parallelization splits it across width and needs a very low-latency link to pay off.**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "As a result, a very low-latency communication technology like Thunderbolt RDMA, supported by MLX `jaccl`, is critical for this approach to yield any speedup."
4. **Muse Spark Open decodes at 15.74 tokens per second on two M5 Ultras with pipeline parallelization, 24.99 with tensor parallelization, and 36.73 on four with tensor parallelization, at a context size of 8,192 tokens.**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "On a cluster of four Mac Studios, Muse Spark Open generates over 36 tokens per second (see Figure 1), well above average human reading speed."
5. **Pipeline parallelization does not speed up generation: Mistral Medium 3.5 decodes at 7.70 tokens per second on one M5 Ultra and 7.70 on two in pipeline, and Qwen 3.8 goes 19.69 to 19.44, because the layers still run sequentially.**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "In general, decode inference speed with pipeline parallelization (see Figure 7) is very similar to that of a single machine, since the layers are still evaluated sequentially."
6. **Tensor parallelization speeds up models that already fit: Qwen 3.8 goes from 19.69 tokens per second on one M5 Ultra to 33.27 on two and 50.89 on four.**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "Decode speed in tokens per second for Qwen 3.8, Mistral Medium 3.5, and Muse Spark Open, at context sizes of 8,192 and 65,536 tokens. Higher is better."
7. **macOS 26.2 shipped the interconnect this needs: its release notes say RDMA over Thunderbolt "enables low-latency communication between Thunderbolt 5 hosts for use cases including distributed AI inference using MLX".**
   - Source: macOS Tahoe 26.2 Release Notes, https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "Enables low-latency communication between Thunderbolt 5 hosts for use cases including distributed AI inference using MLX. (164123391)"
8. **MLX v0.30.1 and later builds on that driver and provides the communication collectives named jaccl, pronounced "jackal".**
   - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "macOS 26.2 introduced a low-latency RDMA driver over Thunderbolt 5, and MLX (v0.30.1 and later) builds on top of this driver and provides new communication collectives (`jaccl`, pronounced \"jackal\") for different parallelization schemes."
9. **Running it is one command: launch mlx_lm.server through mlx.launch with a hostfile, and "the model is automatically sharded across all available devices", with speed-ups "up to three times with four nodes".**
   - Source: Run local agentic AI on the Mac using MLX (WWDC26 session 232), https://developer.apple.com/videos/play/wwdc2026/232/
   - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
   - Quote: "The model is automatically sharded across all available devices and everything else just works."
10. **Apple's two-Mac setup uses two Thunderbolt cables between the pair "to double the link bandwidth", and on four M5 Ultras at a 65,536-token context two cables per link cut time to first token from about 50.5s to 40.6s.**
    - Source: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio, https://machinelearning.apple.com/research/mlx-distributed-inference
    - Tier: primary | Confidence: high | Accessed: 2026-10-16 | Via: web_extract
    - Quote: "In our setup, the two Mac Studios are connected with two Thunderbolt cables (to double the link bandwidth), providing the RDMA-over-Thunderbolt link that `jaccl` uses."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Muse Spark Open size | 816B total parameters (42B active) | https://machinelearning.apple.com/research/mlx-distributed-inference | "Muse Spark Open \| 816B \| 42B \| BF16 \| NVFP4" |
| 2 | Memory footprint, 4-bit NVFP4 | about 493GB | https://machinelearning.apple.com/research/mlx-distributed-inference | "the model memory footprint is lowered to about 493GB" |
| 3 | Memory needed in native BF16 | more than 1.6TB of RAM | https://machinelearning.apple.com/research/mlx-distributed-inference | "would require more than 1.6TB of RAM in its native precision (BF16) for the model parameters alone" |
| 4 | Decode, two M5 Ultras, pipeline | 15.74 tokens per second | https://machinelearning.apple.com/research/mlx-distributed-inference | "2 M5 Pipeline: 8,192-Token Context 15.74" |
| 5 | Decode, two M5 Ultras, tensor | 24.99 tokens per second | https://machinelearning.apple.com/research/mlx-distributed-inference | "2 M5 Tensor: 8,192-Token Context 24.99" |
| 6 | Decode, four M5 Ultras, tensor | 36.73 tokens per second | https://machinelearning.apple.com/research/mlx-distributed-inference | "4 M5 Tensor: 8,192-Token Context 36.73" |
| 7 | Qwen 3.8 decode, one vs two tensor | 19.69 vs 33.27 tokens per second | https://machinelearning.apple.com/research/mlx-distributed-inference | "Qwen 3.8 \| 12.46 \| 19.69 \| 19.44 \| 33.27 \| 50.89" |
| 8 | Thunderbolt 5 port bandwidth | up to 120Gb/s | https://www.apple.com/mac-studio/specs/ | "Thunderbolt 5 (up to 120Gb/s)" |

## Analogy candidates
- **Assembly line**: pipeline parallelism is an assembly line where each Mac is one station holding a consecutive block of layers and passes the half-finished work down the line. Breaks when: a real line works on many items at once and so speeds output, but pipelined decode pushes each token through both stations in sequence, so it fits bigger models without making generation faster.
- **Two cooks chopping one recipe**: tensor parallelism gives each cook half of every ingredient (a slice of every layer), and they hand pieces back and forth constantly; the wide pass-through counter is Thunderbolt RDMA. Breaks when: if the counter is narrow (plain Ethernet), the handing costs more than the parallel chopping saves, which is why only the low-latency link makes it worth it.

## Misconceptions
- Myth: two Mac Studios behave like one Mac with double the memory and double the speed. Reality: pipeline parallelism fits bigger models but leaves decode speed "very similar to that of a single machine" -- Mistral Medium 3.5 decodes at 7.70 tokens per second on one M5 Ultra and 7.70 on two in pipeline (claim 5).
- Myth: you need data-center networking to spread one model across machines. Reality: macOS 26.2 added RDMA over Thunderbolt 5, plain cables between machines on a desk, and MLX's docs say JACCL reaches "communication latency an order of magnitude lower than the ring backend" (claims 3, 7, 8).
- Myth: this is a new Apple invention. Reality: tensor and pipeline parallelism are how NVIDIA clusters already split models; MLX's own docs call JACCL "an obvious pun to Nvidia's NCCL" -- the Mac is getting its own NCCL, not a new law of physics.

## Glossary
- **MLX**: Apple's open-source array framework for Apple silicon that runs and trains models using the chip's unified memory.
- **unified memory**: memory on an Apple silicon Mac shared by the CPU and GPU, so a model's weights sit in one pool the GPU can read directly.
- **RDMA (Remote Direct Memory Access)**: a way for one machine to read and write another machine's memory directly, skipping most CPU and operating-system overhead.
- **Thunderbolt 5**: the latest Thunderbolt port (up to 120Gb/s) that since macOS 26.2 also carries RDMA traffic between Macs.
- **JACCL**: Apple's open-source collective communication library, pronounced "jackal", that coordinates Macs over RDMA for MLX.
- **pipeline parallelism**: splitting a model by depth so each machine holds a consecutive slice of the layers and passes activations to the next machine.
- **tensor parallelism**: splitting a model by width so every machine holds a fraction of every layer and they compute in lockstep.
- **tokens per second (decode speed)**: how fast a model generates new text after it has read your prompt.
- **time to first token (TTFT)**: how long you wait for the model's first word, dominated by reading the prompt.
- **quantization (4-bit, NVFP4)**: storing model weights in fewer bits so they take less memory, at some cost in precision.
- **mixture of experts (MoE)**: a model design where only a fraction of the experts, and thus parameters, is active for any given token.
- **hostfile**: a small JSON file listing each Mac's SSH name and RDMA connections that tells mlx.launch how to reach every machine.

## Unverified
- The achieved sustained throughput of RDMA over Thunderbolt 5 was not measured in any page fetched this session; a community-reported 3.5-3.8 GB/s file-transfer figure appeared only in unfetched search snippets, so the script should not quote a cable speed beyond the port spec of up to 120Gb/s.
- Whether the recipe works on non-Studio Macs (MacBook Pro, Mac mini) is not stated in any fetched page; every fetched demo uses Mac Studio with M3 Ultra or M5 Ultra.
- The price of a two-512GB-Mac-Studio setup was not verified from a fetched Apple page this session.
- Hacker News reception of the Apple post was minimal when fetched (6 points, 1 comment), too thin to characterize community reaction.
- No first-party measurement on our own hardware exists yet; any "what it is like to run" line must wait for one.

## Suggested outline
1. Hook: a nearly-trillion-parameter model running on a desk, Muse Spark Open generating over 36 tokens per second spread across four Mac Studios, and 24.99 on just two.
2. The wall and the split: 816B parameters need about 493GB even quantized and one Studio tops out at 512GB of unified memory, so split the model by depth (each Mac holds half the layers) or by width (each Mac holds a slice of every layer) and the pair becomes one memory pool.
3. The recipe and the catch: macOS 26.2 RDMA over Thunderbolt plus MLX's JACCL make it a one-command launch that shards automatically, but pipelining buys capacity, not speed -- Qwen 3.8 sits at 19.44 tokens per second pipelined versus 19.69 on one machine, while tensor parallelism takes it to 33.27.

## Viewer situation
You run big models on one Mac with MLX and you have hit the ceiling where the model you want needs more memory than your machine has.

## Has process
true
- Connect the two Macs directly with Thunderbolt 5 cables, two cables between the pair to double the link bandwidth.
- Enable RDMA on each machine (in macOS recovery run `rdma_ctl enable` per the MLX docs; Apple's WWDC session shows a Settings toggle).
- Generate the cluster's hostfile with `mlx.distributed_config --hosts <names> --over thunderbolt --backend jaccl --auto-setup`.
- Launch one command: `mlx.launch --hostfile hostfile.json --backend jaccl --env MLX_METAL_FAST_SYNCH=1 -- mlx_lm.server --model meta-models/Muse-Spark-Open-816B-A42B-NVFP4 --port 8080`.
- Point any OpenAI-compatible client at `http://127.0.0.1:8080/v1`.

## Objection
Tensor and pipeline parallelism are exactly how NVIDIA clusters already split models, and a 120Gb/s Thunderbolt link is no NVLink, so two Studios is an expensive way to buy memory one bigger machine would hold -- and pipeline mode does not even generate faster.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://machinelearning.apple.com/research/mlx-distributed-inference | Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio | primary | web_extract | 2026-10-16 |
| 2 | https://developer.apple.com/videos/play/wwdc2026/233/ | Explore distributed inference and training with MLX (WWDC26 session 233) | primary | web_extract | 2026-10-16 |
| 3 | https://developer.apple.com/videos/play/wwdc2026/232/ | Run local agentic AI on the Mac using MLX (WWDC26 session 232) | primary | web_extract | 2026-10-16 |
| 4 | https://ml-explore.github.io/mlx/build/html/usage/distributed.html | Distributed Communication (MLX 0.32.4 documentation) | docs | web_extract | 2026-10-16 |
| 5 | https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes | macOS Tahoe 26.2 Release Notes | primary | web_extract | 2026-10-16 |
| 6 | https://www.apple.com/mac-studio/specs/ | Mac Studio - Technical Specifications | primary | web_extract | 2026-10-16 |
| 7 | https://github.com/ml-explore/mlx/releases | Releases | ml-explore/mlx | primary | web_extract | 2026-10-16 |
| 8 | https://github.com/ml-explore/mlx-lm | ml-explore/mlx-lm: Run LLMs with MLX | primary | web_extract | 2026-10-16 |
| 9 | https://localai.io/docs/features/mlx-distributed/ | (experimental) MLX Distributed Inference :: LocalAI | docs | web_extract | 2026-10-16 |
| 10 | https://news.ycombinator.com/item?id=50113743 | Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio - Hacker News | community | web_extract | 2026-10-16 |

## Notes
- Conflict, RDMA enablement: WWDC26 session 233 says to enable RDMA from Settings ("Open settings on the machine, search for 'RDMA'"), while the MLX 0.32.4 docs say it "has to be done in macOS recovery" by running `rdma_ctl enable`. Trust the MLX docs: they are the maintained, more specific instruction, and the session is a general walkthrough. The process steps follow the docs and note the toggle.
- Conflict, MLX_METAL_FAST_SYNCH=1: Apple's post sets it in every launch command, but the MLX docs warn it "is not reliable that can lead to deadlock and leave the GPU wedged (see #3142), so it is off by default and best left unset". Keep the flag in the quoted command as Apple publishes it; the script should not claim it is risk-free.
- Referents: all decode numbers are from the 8,192-token context column of Table 3 / Figure 1 (batch 1, measured over 128 generated tokens); the 50.5s to 40.6s TTFT comparison is at a 65,536-token context on four M5 Ultras. Qwen 3.8 and Mistral Medium 3.5 are dense models (BF16 and FP8); Muse Spark Open is MoE in NVFP4, so its speeds are not comparable to theirs.
- Freshness chain: the Apple post is dated 2026-10-15 and says "the latest version of MLX, released today"; MLX v0.32.4 was released 14 Oct 2026 and includes "[jaccl] second cable for the mesh"; mlx-lm v0.32.2 was released 2026-10-16. The Hacker News thread on the post appeared about 8 hours before this brief was written.
- Quotes copy source text with em dashes rendered as "--" per repo style; no other character was altered.
