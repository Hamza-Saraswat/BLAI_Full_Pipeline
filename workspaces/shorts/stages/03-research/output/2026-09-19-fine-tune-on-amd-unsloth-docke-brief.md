---
slug: 2026-09-19-fine-tune-on-amd-unsloth-docke
stage: 03-research
topic: "Fine-tune on AMD: Unsloth Docker in three moves"
depth: standard
generated_at: 2026-09-19T12:10:00Z
sources: 8
hub: "[[videos/2026-09-19-fine-tune-on-amd-unsloth-docke]]"
---

# Research brief: Fine-tune on AMD: Unsloth Docker in three moves

## Summary
The single idea: the part of AMD fine-tuning that hurt was never the GPU, it was assembling the software stack, and Unsloth now ships that stack as a container. The most arresting number is the floor Unsloth publishes for AMD: fine-tune Qwen3.5 in 3GB VRAM, or Gemma 4 in 8GB VRAM, cards a viewer may already own. The strongest concrete case is what the manual route demanded versus what the image bakes in: by hand you pick a PyTorch wheel matching your ROCm version from eight index tags and install a pre-release bitsandbytes wheel because versions 0.49.2 and below carry a 4-bit NaN bug on every AMD GPU; the unsloth/unsloth-rocm image ships PyTorch built against ROCm 7.2 with that fix already in. Could not be verified: any first-party run on our own AMD hardware, and how the ROCm image behaves on discrete RDNA2/RDNA4 cards (its published measurements cover a Strix Halo APU). One conflict: AMD's own July 20 article lists RDNA 2 as Limited, Linux only, gfx1030 only, while Unsloth's current docs (updated after the September 18 release) list RDNA 2 as Full across Windows + WSL + Linux; we trust the newer Unsloth page.

## Thesis
Unsloth's new Docker image turns AMD fine-tuning from a hand-pinned ROCm stack into three moves: install Docker, run unsloth/unsloth-rocm, train.

## Explanation path
Start where the viewer stands: an AMD card that every fine-tuning tutorial skips, and a history of ROCm installs that break when one version pin drifts. Establish what a Docker image actually replaces -- the matched set of a PyTorch wheel, a fixed bitsandbytes build, triton-rocm, TRL and PEFT that the manual route assembles by hand. Then the release itself: Unsloth now publishes two images, one for CUDA and one for ROCm, so the AMD path is a pull instead of a build. Before the commands, explain the one real difference from the NVIDIA habit: AMD GPUs reach Docker through kernel device nodes such as /dev/kfd rather than a container toolkit. Land on capability and honesty together -- the VRAM floors that make an aging Radeon viable, the measured MI300X numbers behind the marketing claims, and the boundaries (RDNA2 and newer inside the image, Linux for multi-GPU, no Studio in the ROCm build) so the viewer knows exactly which box they need.

## Claims
1. **Unsloth's v0.1.811-beta release, titled "Docker + Multi User + AMD Support", ships a new Docker image with NVIDIA and AMD support and names the AMD generations "RDNA1, RDNA2 support for AMD".**
   - Source: Release Docker + Multi User + AMD Support · unslothai/unsloth · GitHub, https://github.com/unslothai/unsloth/releases/tag/v0.1.811-beta
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "New Docker with NVIDIA & AMD support: Guide ... RDNA1, RDNA2 support for AMD ... Added an AMD ROCm image alongside CUDA for supported Linux hosts."
2. **Unsloth's Docker guide names exactly two images, unsloth/unsloth for NVIDIA and unsloth/unsloth-rocm for AMD, with the whole dependency set pre-installed.**
   - Source: Install Unsloth via Docker | Unsloth Documentation, https://unsloth.ai/docs/get-started/install/docker
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "No setup required - all dependencies are pre-installed. Just pull the image and start running and training models on your local NVIDIA or AMD GPUs."
3. **The ROCm image carries the pinned training stack -- PyTorch built against ROCm 7.2, a bitsandbytes build with the ROCm 4-bit fix, triton-rocm, TRL, PEFT and diffusers -- but omits Unsloth Studio, JupyterLab, prebuilt llama.cpp, vLLM and xformers, which stay CUDA-only for now.**
   - Source: unsloth/unsloth-rocm - Docker Image, https://hub.docker.com/r/unsloth/unsloth-rocm
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "This image carries the full training stack built against ROCm: PyTorch with ROCm 7.2, Unsloth, unsloth-zoo, a bitsandbytes build with the ROCm 4-bit fix, triton-rocm, TRL, PEFT and diffusers. ... Not included, unlike `unsloth/unsloth`: Unsloth Studio and its web UI, JupyterLab, prebuilt llama.cpp and whisper.cpp, vLLM and xformers. This is a training image; GGUF tooling and the UI are CUDA-only for now."
4. **The manual AMD route that Docker replaces meant matching a PyTorch wheel to your ROCm version by hand (index tags rocm6.0 through rocm7.2, "ROCm 6.0 or newer is required") plus a pre-release bitsandbytes wheel, because "versions ≤ 0.49.2 have a 4-bit decode NaN bug on every AMD GPU".**
   - Source: Fine-tuning LLMs on AMD GPUs with Unsloth Guide | Unsloth Documentation, https://unsloth.ai/docs/get-started/install/amd
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "All ROCm systems need a pre-release bitsandbytes build, versions ≤ 0.49.2 have a 4-bit decode NaN bug on every AMD GPU."
5. **On AMD, Unsloth publishes fine-tuning floors of 8GB VRAM for Gemma 4 and 3GB VRAM for Qwen3.5, with 70% less VRAM use claimed and no accuracy loss.**
   - Source: Train & run models on AMD GPUs with Unsloth | Unsloth Documentation, https://unsloth.ai/docs/basics/amd
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "Train Gemma 4 models in 8GB VRAM or Qwen3.5 in 3GB VRAM. Triton kernels, math algorithms and memory tricks allow 70% less VRAM use for AMD with no accuracy loss."
6. **Unsloth's own measured AMD benchmark (Llama-3.1-8B LoRA SFT on an MI300X, 16,384 tokens/step, packed) shows 2.07 s/step versus 2.87 s/step for TRL + FA2 and a peak of 18.3 GB versus 24.3 GB -- "1.39x faster and 1.33x less memory usage", short of the "up to 2x faster" headline.**
   - Source: Train & run models on AMD GPUs with Unsloth | Unsloth Documentation, https://unsloth.ai/docs/basics/amd
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "On Llama-3.1-8B LoRA SFT (batch 2 x grad-accum 4 x 2048 = 16,384 tokens/step, packed), Unsloth trains at 2.07 s/step vs 2.87 s/step for TRL + FA2, and peaks at 18.3 GB versus 24.3 GB. That is 1.39x faster and 1.33x less memory usage, with no change in accuracy."
7. **The AMD run command differs from the NVIDIA habit because AMD GPUs are passed to Docker through kernel device nodes, not a container toolkit: the guide's command passes --device /dev/kfd (and /dev/dri when present) instead of --gpus all.**
   - Source: Install Unsloth via Docker | Unsloth Documentation, https://unsloth.ai/docs/get-started/install/docker
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "For AMD GPUs, they are reached through the kernel driver's device nodes, not through a container toolkit, so the run command differs from the NVIDIA one"
8. **The ROCm Docker image trains "RDNA2 and newer, and CDNA, except gfx1033" -- so Radeon RX 6000 and up, with the Steam Deck's Van Gogh (gfx1033) refused outright because "training diverges to NaN under ROCm".**
   - Source: unsloth/unsloth-rocm - Docker Image, https://hub.docker.com/r/unsloth/unsloth-rocm
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "RDNA2 and newer, and CDNA, except `gfx1033`. ... Van Gogh (`gfx1033`, Steam Deck) is refused outright. It is RDNA2, but training diverges to NaN under ROCm while forward passes look valid"
9. **AMD multi-GPU training is Linux-only: on Linux ROCm's RCCL collectives work, but on Windows "AMD ROCm does not yet provide a GPU-collective backend".**
   - Source: Train & run models on AMD GPUs with Unsloth | Unsloth Documentation, https://unsloth.ai/docs/basics/amd
   - Tier: primary | Confidence: high | Accessed: 2026-09-19 | Via: web_extract
   - Quote: "AMD distributed training is currently Linux-only. On Linux, ROCm uses RCCL, so distributed training works. On Windows, AMD ROCm does not yet provide a GPU-collective backend"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Gemma 4 fine-tuning VRAM floor (AMD) | 8GB VRAM | https://unsloth.ai/docs/basics/amd | "Train Gemma 4 models in 8GB VRAM or Qwen3.5 in 3GB VRAM." |
| 2 | Qwen3.5 fine-tuning VRAM floor (AMD) | 3GB VRAM | https://unsloth.ai/docs/basics/amd | "Train Gemma 4 models in 8GB VRAM or Qwen3.5 in 3GB VRAM." |
| 3 | Claimed VRAM reduction on AMD | 70% less VRAM | https://unsloth.ai/docs/basics/amd | "memory tricks allow 70% less VRAM use for AMD with no accuracy loss" |
| 4 | Unsloth step time (Llama-3.1-8B LoRA SFT, MI300X) | 2.07 s/step | https://unsloth.ai/docs/basics/amd | "Unsloth trains at 2.07 s/step vs 2.87 s/step for TRL + FA2" |
| 5 | TRL + FA2 comparison step time (same benchmark) | 2.87 s/step | https://unsloth.ai/docs/basics/amd | "Unsloth trains at 2.07 s/step vs 2.87 s/step for TRL + FA2" |
| 6 | Unsloth peak VRAM (same benchmark) | 18.3 GB | https://unsloth.ai/docs/basics/amd | "peaks at 18.3 GB versus 24.3 GB" |
| 7 | TRL + FA2 peak VRAM (same benchmark) | 24.3 GB | https://unsloth.ai/docs/basics/amd | "peaks at 18.3 GB versus 24.3 GB" |
| 8 | ROCm version the Docker image is built against | ROCm 7.2 | https://hub.docker.com/r/unsloth/unsloth-rocm | "PyTorch with ROCm 7.2" |

## Analogy candidates
- **Frozen meal kit vs grocery shopping**: The Docker image is the pre-portioned kit -- PyTorch matched to ROCm 7.2, the fixed bitsandbytes, triton-rocm, TRL, PEFT all in one box -- while the manual route is shopping for each ingredient and hoping the versions combine into dinner (the rocm6.0-through-rocm7.2 wheel index, the pre-release bitsandbytes wheel). Breaks when: you want an ingredient the kit does not carry -- a newer ROCm, Unsloth Studio's web UI, or GGUF tooling all need something beyond this image, so the kit is a starting point, not a pantry.

## Misconceptions
- Myth: The release says RDNA1 support, so my old Radeon RX 5000 card can now fine-tune through this Docker image. Reality: The unsloth/unsloth-rocm image trains RDNA2 and newer, and CDNA except gfx1033; Unsloth's hardware table gives RDNA 1 (Radeon RX 5000, gfx1010/gfx1012) "Vulkan inference" only (claims 1, 8).
- Myth: The AMD container is the same experience as the NVIDIA one, just with ROCm inside. Reality: The ROCm image is a training image -- Unsloth Studio, JupyterLab, prebuilt llama.cpp, vLLM and xformers are not included and remain CUDA-only for now (claim 3).
- Myth: You still need the NVIDIA-style container toolkit wiring for AMD. Reality: AMD GPUs are reached through kernel device nodes such as /dev/kfd, so the run command uses --device flags, not --gpus all (claim 7).
- Myth: Fine-tuning needs a big NVIDIA card. Reality: Unsloth publishes 8GB VRAM for Gemma 4 and 3GB VRAM for Qwen3.5 on AMD (claim 5).

## Glossary
- **Docker image**: A ready-to-run package holding an application plus every dependency it needs, so the same stack runs on any machine with Docker installed.
- **ROCm**: AMD's open software platform for GPU compute, the AMD counterpart to NVIDIA's CUDA.
- **RDNA2**: The GPU architecture inside AMD Radeon RX 6000 series cards, the oldest generation the Unsloth ROCm Docker image trains.
- **/dev/kfd**: The Linux kernel device node that exposes an AMD GPU's compute driver, the pipe Docker passes into the container in place of NVIDIA's toolkit.
- **QLoRA**: A fine-tuning method that loads a quantized 4-bit model and trains small adapter weights on top, which is what cuts VRAM to the 8GB and 3GB floors.
- **bitsandbytes**: The library doing the 4-bit quantization in QLoRA, and the package whose AMD bug forced manual installs onto pre-release wheels.
- **VRAM**: The memory on the graphics card that holds the model during training.
- **PyTorch wheel**: A prebuilt, installable package of PyTorch for one specific platform, such as the ROCm 7.2 build inside the Docker image.

## Unverified
- Community lore says hand-built ROCm stacks routinely broke on system updates; no fetched page states this as a measured fact, so treat it as the audience's lived experience, not a citation.
- No first-party measurement exists yet of training speed or VRAM on our own AMD hardware; Unsloth's numbers are the vendor's, measured on an MI300X.
- How the unsloth/unsloth-rocm image performs on discrete RDNA2, RDNA4 or CDNA cards is unverified: the image's published measurements were taken on a Strix Halo APU (Radeon 8060S, gfx1151).
- Docker Hub reported roughly 306 pulls for unsloth/unsloth-rocm versus 100K+ for unsloth/unsloth at fetch time; page-reported counters, not a claim the video should cite.

## Suggested outline
1. Hook on the concrete: an AMD Radeon card fine-tunes Qwen3.5 in 3GB VRAM (Gemma 4 in 8GB), and the stack that used to mean a weekend of ROCm version-pinning is now one docker run away.
2. What shipped: two images (unsloth/unsloth for CUDA, unsloth/unsloth-rocm built against ROCm 7.2 with the 4-bit-fixed bitsandbytes), and the one AMD difference -- GPUs pass through device nodes like /dev/kfd, not a container toolkit.
3. Honest catch into payoff: the image trains RDNA2 and newer (RDNA1 is Vulkan inference, gfx1033 refused, multi-GPU is Linux-only) and the measured gain is 1.39x, not the up-to-2x headline -- then the payoff: the image's smoke test runs a real 5-step LoRA on a 1B model, so the box proves it trains before you spend an evening on it.

## Viewer situation
You've got an AMD box -- maybe a Radeon RX 6000 or 7000 card -- that every fine-tuning tutorial skips, and your last attempt died somewhere in ROCm version mismatches.

## Has process
true
Install Docker Engine on the Linux host with the command the docs print: `curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh`
Run the unsloth/unsloth-rocm container passing the AMD device nodes (--device /dev/kfd, --device /dev/dri when present, plus the video and render group ids) and mounting your Hugging Face cache so downloads survive `docker rm`
Check the GPU actually trains using the image's built-in smoke test (`python /workspace/smoke_test_rocm.py`, a real 5-step LoRA on a 1B model that fails loudly if the GPU is unusable)
Train your model inside the container: load it with FastModel, wrap it in LoRA adapters with get_peft_model, then fit it with SFTTrainer and call trainer.train()

## Objection
A Docker image does not fix ROCm itself -- per-architecture wheel gaps still force rebuilds on some Strix Halo and RDNA4 chips, multi-GPU is Linux-only, and the vendor's own measured gain is 1.39x, not the marketed 2x.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/unslothai/unsloth/releases/tag/v0.1.811-beta | Release Docker + Multi User + AMD Support · unslothai/unsloth · GitHub | primary | web_extract | 2026-09-19 |
| 2 | https://unsloth.ai/docs/get-started/install/docker | Install Unsloth via Docker \| Unsloth Documentation | primary | web_extract | 2026-09-19 |
| 3 | https://unsloth.ai/docs/basics/amd | Train & run models on AMD GPUs with Unsloth \| Unsloth Documentation | primary | web_extract | 2026-09-19 |
| 4 | https://unsloth.ai/docs/new/changelog | Unsloth Updates \| Unsloth Documentation | primary | web_extract | 2026-09-19 |
| 5 | https://hub.docker.com/r/unsloth/unsloth | unsloth/unsloth - Docker Image | primary | web_extract | 2026-09-19 |
| 6 | https://hub.docker.com/r/unsloth/unsloth-rocm | unsloth/unsloth-rocm - Docker Image | primary | web_extract | 2026-09-19 |
| 7 | https://unsloth.ai/docs/get-started/install/amd | Fine-tuning LLMs on AMD GPUs with Unsloth Guide \| Unsloth Documentation | primary | web_extract | 2026-09-19 |
| 8 | https://www.amd.com/en/developer/resources/technical-articles/2026/train-and-run-models-on-amd-gpus-with-unsloth.html | Train & run models on AMD GPUs with Unsloth (AMD technical article, Jul 20, 2026) | docs | web_extract | 2026-09-19 |

## Notes
Source conflict on RDNA 2: AMD's July 20, 2026 article lists "RDNA 2 | Radeon RX 6000 Series | gfx1030 only | Limited | Linux only", while Unsloth's current basics/amd page (carrying a Sept 18 update line and last-updated 2 hours before fetch) lists RDNA 2 as Full on Windows + WSL + Linux across gfx1030, gfx1031, gfx1032, gfx1034. Trust the newer Unsloth page; the AMD article predates the September RDNA1/2 expansion. Second, smaller discrepancy: the changelog page headlines the same Docker + AMD announcement under September 17, 2026 (the v0.1.810-beta cut) while the GitHub tag v0.1.811-beta is dated September 18 (assets stamped 2026-09-18T16:49:57Z); cite the GitHub release for the tag date. Thin spot: the ROCm image's published measurements cover a Strix Halo APU only, so discrete-card behavior is unverified. Source 4 (changelog) and source 5 (CUDA Docker Hub page) corroborate but carry no unique claims; source 8 grounds the July baseline that makes the conflict visible.
