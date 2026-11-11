---
slug: 2026-11-11-minimax-h3-image-in-comfyui-lo
stage: 03-research
topic: "MiniMax H3-Image in ComfyUI: local image gen today"
depth: standard
generated_at: 2026-11-11T12:38:13Z
sources: 11
hub: "[[videos/2026-11-11-minimax-h3-image-in-comfyui-lo]]"
---

# Research brief: MiniMax H3-Image in ComfyUI: local image gen today

## Summary

Three days after the weights landed on Hugging Face (2026-11-08), the Comfy-Org repack makes MiniMax-H3-Image a four-file download, and its diffusion core merged into ComfyUI itself 14 hours before this brief was written. The grabber: the Comfy-Org repo has already pulled "351,803" downloads in its first month against "142,989" for MiniMax's own repo. The catch is disk and VRAM, not skill: 54.79 GB of files before you render a pixel, on top of a ComfyUI whose nightly merged the needed core nodes only yesterday. No tier 1-3 page states a minimum VRAM for H3-Image, and the RTX 3060 / 42.5 GB / 66%-smaller claims floating around belong to the H3 video model's August launch, not this image model. A third-party quant (PrunaAI P-H3-Image) says "21 GB of VRAM" peak at 8 MP, but that is a modified model, not the Comfy-Org path this video teaches.

## Thesis

MiniMax's H3-Image open-weight image model went from API-only to running in ComfyUI on your own GPU in three days, and tonight the whole thing is four files into three folders.

## Explanation path

Start with what the viewer already does: typing a prompt into a chatbot and getting a picture back from somebody else's server. Establish what changed on 2026-11-08: MiniMax put the H3-Image weights on Hugging Face under a community license anyone can download. Before the how, land what the model is: one checkpoint that both generates from text and edits existing pictures, at about 16 megapixels natively (4096 x 4096), in 6 steps with no negative prompt -- because the numbers are the reason anyone cares. Then the practical machine-check moment: this is a 33.1B-parameter model whose full checkpoint is "68.65 GB" and whose text encoder alone is "66.7 GB" in BF16, which is why nobody runs it raw; the Comfy-Org INT8 repack is the version that fits a gaming PC, four files totalling about 54.79 GB. Only then walk the install: update ComfyUI (the core nodes merged 2026-11-10 and the templates want 0.45.0+), pull the four files into diffusion_models / text_encoders / vae, open the built-in "MiniMax-H3-Image: Text to Image" template, start at 4 MP on purpose so smaller cards do not choke, and raise the resolution when the GPU has room. Close on the honest boundary: the license gates companies over 1 Million USD revenue, the prompt expander is an extra 7.34 GB download switched off by default, and the VRAM floor is not officially stated anywhere.

## Claims

1. **MiniMax released H3-Image as an open-weight model for download, in one checkpoint covering both text-to-image and image editing.**
   - Source: MiniMax-H3-Image model card, https://huggingface.co/MiniMaxAI/MiniMax-H3-Image
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
2. **The diffusion transformer is 33.1B parameters, distilled to a 6-step sampler with no classifier-free guidance.**
   - Source: MiniMax-H3-Image model card, https://huggingface.co/MiniMaxAI/MiniMax-H3-Image
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "The checkpoint is distilled to 6 sampling steps (6 NFEs) with no classifier-free guidance." and "**Diffusion transformer**: 33.1B parameters, a dense single-stream transformer with 50 layers"
3. **The Comfy-Org repack needs exactly four files totalling 54.79 GB (21 GB + 25.28 GB + 7.34 GB + 1.17 GB) placed in three folders under ComfyUI/models.**
   - Source: MiniMax H3 Image tutorial, https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image
   - Tier: docs | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "Pruned INT8 DiT, 21 GB", "Qwen3-VL-32B, INT8, 25.28 GB", "Qwen3.5 9B W4A8, 7.34 GB", "Image VAE, FP16, 1.17 GB"
4. **The Comfy-Org repository published the repackage on 2026-11-08 and logged "351,803" downloads in its first month, versus "142,989" on MiniMax's own repo.**
   - Source: MiniMax H3 Image (Comfy-Org README), https://huggingface.co/Comfy-Org/MiniMax-H3-Image
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "Downloads last month351,803" (page's compressed form)
5. **Native support merged into ComfyUI core on 2026-11-10 as "feat: Support MiniMax-H3-image (CORE-708)", and the docs templates require ComfyUI 0.45.0+ and template pack 0.11.104+.**
   - Source: Comfy-Org/ComfyUI GitHub repository, https://github.com/Comfy-Org/ComfyUI
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "feat: Support MiniMax-H3-image (CORE-708) (#17655) ... 14 hours agoNov 10, 2026"; docs: "Both need ComfyUI **0.45.0+** and template pack **0.11.104+**."
6. **The text-to-image template deliberately opens at 4 MP, below the model's native 16 MP, so low-VRAM machines do not run out of memory.**
   - Source: MiniMax H3 Image tutorial, https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image
   - Tier: docs | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "The template opens at 4 MP on a square canvas, deliberately below the model's native resolution so low-VRAM machines do not run out of memory."
7. **The BF16 checkpoint is 68.65 GB and its required text encoder another 66.7 GB, which is why the INT8 repack exists.**
   - Source: MiniMax-H3-Image model card, https://huggingface.co/MiniMaxAI/MiniMax-H3-Image
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "**MiniMax-H3-Image** | Text-to-image and image editing | BF16 (DiT) | 68.65 GB"; "Text encoder | Not in this repository. ... 66.7 GB"
8. **The license requires separate written authorization from MiniMax if your annualized revenue exceeds 1 Million USD or you provide hosted services to third parties.**
   - Source: MiniMax H3 Image (Comfy-Org README), https://huggingface.co/Comfy-Org/MiniMax-H3-Image
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "You shall obtain a separate, prior written authorization from MiniMax ... if the Annualized Revenue of you and/or your affiliates exceeds 1 Million USD, or, you provide Hosted Service(s) to any Third Parties."
9. **MiniMax's announcement claims a 4K (4096 x 4096) image "in under 10 seconds, at up to 5x the speed of mainstream alternatives".**
   - Source: Bringing 4K Image Generation into the 10-Second Era, https://www.minimax.io/blog/minimax-h3-image
   - Tier: primary | Confidence: high | Accessed: 2026-11-11 | Via: hermes web_extract
   - Quote: "H3-Image can generate a 4K (4096 x 4096) image in under 10 seconds, with rich, realistic details, strong prompt adherence, the ability to understand and work with up to 16 reference image." / "at up to 5x the speed of mainstream alternatives"
10. **A third-party quantized variant (PrunaAI P-H3-Image) lists "From 21 GB of VRAM" peaking at 8 MP, against "143 GB of weights for MiniMax-H3".**
    - Source: PrunaAI/P-H3-Image-Comfy model card, https://huggingface.co/PrunaAI/P-H3-Image-Comfy
    - Tier: primary | Confidence: medium | Accessed: 2026-11-11 | Via: hermes web_extract
    - Quote: "From 21 GB of VRAM   -   8 steps   -   Text-to-image and editing with up to 8 images"; "The smallest set is a 20 GB download that peaks at 21 GB of VRAM at 8 MP, against 143 GB of weights for MiniMax-H3."

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Comfy-Org repo downloads, first month | 351,803 | https://huggingface.co/Comfy-Org/MiniMax-H3-Image | "Downloads last month351,803" |
| 2 | DiT size, INT8 Comfy-Org repack | 21 GB | https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image | "Pruned INT8 DiT, 21 GB" |
| 3 | Full four-file download total | 54.79 GB (21 GB + 25.28 GB + 7.34 GB + 1.17 GB) | https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image | "Four files go under ComfyUI/models" |
| 4 | Diffusion transformer parameters | 33.1B parameters | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | "**Diffusion transformer**: 33.1B parameters, a dense single-stream transformer with 50 layers" |
| 5 | Native output resolution | 4096 x 4096 (about 16 MP) | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | "It generates images of about 16 megapixels at every aspect ratio, from 4096x4096 (1:1) to 6272x2688 (21:9)" |
| 6 | Sampling steps (fixed) | 6 steps | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | "The checkpoint is distilled to 6 sampling steps (6 NFEs) with no classifier-free guidance." |
| 7 | BF16 checkpoint size | 68.65 GB | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | "BF16 (DiT) | 68.65 GB" |
| 8 | MiniMax-claimed 4K generation time | under 10 seconds | https://www.minimax.io/blog/minimax-h3-image | "H3-Image can generate a 4K (4096 x 4096) image in under 10 seconds" |

## Analogy candidates

- **Vehicle**:Downloading a game and its HD texture pack, not installing a mod. **Mapping**: The model is a AAA game engine; Comfy-Org's INT8 files are the official compressed download; the four files land in named folders exactly like a game's /models directories; ComfyUI itself is the launcher that must be updated first. **Breaks when**: the viewer starts imagining paid DLC or always-online checks -- everything here is free and offline once downloaded; the only gate is a license clause for million-dollar companies.
- **Vehicle**: A studio camera that shoots 16 MP in one shot versus a phone app that upscales a 1 MP snapshot. **Mapping**: H3-Image renders native 16 MP in a single pass, where most local models output 1-4 MP and get upscaled afterwards. **Breaks when**: the viewer expects photography physics like lenses and exposure -- generation has no optics, and the honest catch is that 16 MP costs real compute per image, not just a bigger sensor.

## Misconceptions

- Myth: You need to install a custom node pack from some third party to run MiniMax H3-Image in ComfyUI. Reality: Support merged into ComfyUI core on 2026-11-10 ("feat: Support MiniMax-H3-image (CORE-708)"), and the Comfy-Org docs point at built-in template workflows; update ComfyUI instead of hunting custom nodes. (claim 5)
- Myth: The download is one model file. Reality: Four files go into three different folders (diffusion model 21 GB, text encoder 25.28 GB, optional prompt expander 7.34 GB, VAE 1.17 GB), and the expander is optional. (claim 3)
- Myth: The famous "runs on an RTX 3060" / 42.5 GB claims apply to H3-Image. Reality: Those numbers come from Comfy-Org's August day-0 blog about the MiniMax H3 video model's memory optimization ("from 123.6 GB in full precision to 42.5 GB"), not the image model; no official H3-Image VRAM floor exists. (claim 10, Unverified)

## Glossary

- **open weights**: The numbered files that make a model work are published for anyone to download and run on their own machine, not just through the company's website.
- **Hugging Face**: The website where AI models are hosted for download, like an app store for model files.
- **checkpoint**: The model file itself; the trained weights that turn text into images.
- **diffusion model / DiT**: The image-generating core of the system; it refines a field of static noise into a picture step by step.
- **text encoder**: The model part that reads your prompt first and turns it into numbers the image generator understands.
- **VAE**: The decoder that translates the model's internal compressed image into the actual PNG you can open.
- **ComfyUI**: A free, node-based app for running image and video models locally, where you wire boxes together instead of typing into a single box.
- **INT8 quantization**: A shrink-wrapped version of the model that stores numbers more roughly (8-bit instead of 16-bit) so it fits in less memory, at a small quality cost.
- **VRAM**: The memory sitting on your graphics card; models must fit inside it to run fast.
- **steps**: How many denoising passes the model takes; H3-Image is fixed at 6, which is few.
- **classifier-free guidance (CFG)**: A common second pass that checks the image against your prompt; H3-Image skips it (guidance fixed at 1), so there is no negative prompt.
- **megapixel (MP)**: A measure of image size; 16 MP is roughly a 4096 x 4096 canvas, several times the pixel count of a typical 1080p wallpaper.
- **prompt expander**: An optional small language model that rewrites your short prompt into the detailed paragraph the image model reads best.
- **template workflow**: A ready-made wiring diagram that ships inside ComfyUI; you open it and press run instead of building the graph yourself.
- **community license**: A free-to-use license with conditions; here, companies above 1 Million USD a year must ask MiniMax for written permission.

## Unverified

- No official minimum VRAM or system-RAM requirement for MiniMax-H3-Image has been published by MiniMax or Comfy-Org; any specific GB floor for running it locally is community folklore until measured or stated.
- Community posts report H3-family models running on cards as small as 8-12 GB with heavy quantization, but none of those numbers are confirmed by a tier 1-3 page for H3-Image specifically.
- The "under 10 seconds" 4K generation time is MiniMax's own API-side claim with no published hardware or method; local speed on a viewer's GPU is unknown and will differ.
- Whether the just-merged core support (2026-11-10) has shipped in a stable ComfyUI release, or only in nightly builds, is not stated on any fetched page; the docs warn template nodes may lag stable releases.
- Reddit and X reception threads (r/LocalLLaMA, r/comfyui) could not be fetched this run (403 blocks), so community sentiment is ungrounded.
- The Hacker News item page given as a radar seed (news.ycombinator.com/item?id=1f1dbabb56) returned an empty body this run and could not be read; only the Algolia API confirmed the story exists (4 points, 0 comments, posted 2026-11-10).

## Suggested outline

1. Hook: three days ago this model did not exist outside MiniMax's servers; last night ComfyUI itself learned to run it -- and the Comfy-Org download page already shows 351,803 pulls.
2. Name what the viewer has: a gaming PC with a decent GPU and ComfyUI curiosity; this is the first open-weight image model that natively shoots about 16 MP in 6 steps.
3. Explain the three cooperating parts with the game-install analogy: ComfyUI is the launcher (update it first, core support merged 2026-11-10), the four files are the game (21 GB DiT + 25.28 GB text encoder + 7.34 GB expander + 1.17 GB VAE into three named folders), the template is the saved game (open and run).
4. The payoff run: open the built-in Text to Image template, notice it starts at 4 MP on purpose, write a prompt, raise resolution when the GPU has room.
5. Honest catch: no official VRAM floor exists, the RTX 3060 stories are about the H3 video model, and the license gates million-dollar companies -- measure on your own card before promising viewers a number.

## Viewer situation

You have a gaming PC or Mac with a decent GPU, you have used ChatGPT to make pictures, and you have heard people run image models themselves in ComfyUI but never tried a brand-new one this early.

## Has process

true

## Process steps

- Update ComfyUI to the latest version (0.45.0+; core MiniMax-H3-Image support merged 2026-11-10).
- Download the four files from the Comfy-Org Hugging Face repos: the 21 GB INT8 diffusion model, the 25.28 GB INT8 text encoder, the 7.34 GB prompt expander, and the 1.17 GB VAE.
- Place them in ComfyUI/models/diffusion_models, ComfyUI/models/text_encoders (two files), and ComfyUI/models/vae.
- Open the built-in "MiniMax-H3-Image: Text to Image" template from the workflow template library.
- Run once at the template's default 4 MP canvas, then raise resolution with the selector when the GPU has headroom.

## Objection

A skeptical engineer says the four-file package is still 54.79 GB, no official VRAM floor is published, the merged core support is hours old, and a 12 GB card may simply choke on a 33.1B-parameter DiT no matter how good the INT8 repack is.

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/Comfy-Org/MiniMax-H3-Image | MiniMax H3 Image (Comfy-Org README) | primary | web_extract | 2026-11-11 |
| 2 | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | MiniMax-H3-Image model card | primary | web_extract | 2026-11-11 |
| 3 | https://huggingface.co/Comfy-Org/MiniMax-H3-Image/tree/main | Comfy-Org repo Files tab | primary | web_extract | 2026-11-11 |
| 4 | https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image | MiniMax H3 Image tutorial (ComfyUI docs) | docs | web_extract | 2026-11-11 |
| 5 | https://www.minimax.io/blog/minimax-h3 | MiniMax H3 blog post | primary | web_extract | 2026-11-11 |
| 6 | https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui | MiniMax H3 Day-0 Support in ComfyUI | docs | web_extract | 2026-11-11 |
| 7 | https://www.minimax.io/blog/minimax-h3-image | Bringing 4K Image Generation into the 10-Second Era | primary | web_extract | 2026-11-11 |
| 8 | https://github.com/Comfy-Org/ComfyUI | Comfy-Org/ComfyUI GitHub repository | primary | web_extract | 2026-11-11 |
| 9 | https://hn.algolia.com/api/v1/search?query=MiniMax%20H3-Image | HN Algolia search API (H3-Image story: 4 points, 0 comments) | community | web_extract | 2026-11-11 |
| 10 | https://kingy.ai/ai/ai-guides/minimax-h3-comfyui-local-guide/ | MiniMax H3 ComfyUI Guide (Kingy.ai) | docs | web_extract | 2026-11-11 |
| 11 | https://huggingface.co/PrunaAI/P-H3-Image-Comfy | PrunaAI/P-H3-Image-Comfy model card | primary | web_extract | 2026-11-11 |

## Notes

Conflicts and thin spots. The RTX 3060 / 42.5 GB / 66% memory-reduction claims in the Comfy day-0 blog (blog.comfy.org) describe the MiniMax H3 video model launched in August, not H3-Image; do not attribute them to the image model on screen. The 21 GB VRAM peak figure belongs to PrunaAI's modified P-H3-Image quant (8 steps, 8 MP, up to 8 references), not the Comfy-Org INT8 path this video teaches; kept as claim 10 with that framing. Downloads on the two HF repos will keep moving after this run; the quoted 351,803 and 142,989 are the values printed on the pages fetched 2026-11-11 and MiniMax's own blog says weights were released with the announcement. Kingy.ai's file sizes cover the H3 video files, not H3-Image; its value here is the explicit statement that no minimum-VRAM matrix has been published. The HN item URL given as a seed returned an empty body this run; the Algolia API search confirms an H3-Image story posted 2026-11-10 at 4 points with 0 comments, which matches the radar seed. Reddit and X reception threads were blocked (403) and are ungrounded.
