# Source: https://huggingface.co/PrunaAI/P-H3-Image-Comfy
# Fetched: 2026-11-11 via hermes web_extract

![](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/resolve/main/assets/p-h3-image-comfy.jpg)

[![GitHub](https://img.shields.io/badge/GitHub-PrunaAI-9334E9?style=plastic&logo=github&logoColor=white)](https://github.com/PrunaAI/pruna)[![Twitter/X](https://img.shields.io/badge/Twitter%2FX-@PrunaAI-9334E9?style=plastic&logo=x&logoColor=white)](https://twitter.com/PrunaAI)[![LinkedIn](https://img.shields.io/badge/LinkedIn-PrunaAI-9334E9?style=plastic&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/pruna-ai)[![Discord](https://img.shields.io/badge/Discord-Join%20us-9334E9?style=plastic&logo=discord&logoColor=white)](https://discord.com/invite/JFQmtFKCjd)[![Performance Models](https://img.shields.io/badge/Performance%20Models-Try%20them%20now-9334E9?style=plastic&logo=[IMAGE])](https://dashboard.pruna.ai/login?utm_source=huggingface&utm_medium=org_card&utm_campaign=hf_traffic)

# P-H3-Image

## ComfyUI files for P-H3-Image, based on MiniMax-H3

### bf16, int8 and w4a8   ·   From 21 GB of VRAM   ·   8 steps   ·   Text-to-image and editing with up to 8 images

This repository holds the ComfyUI files for **P-H3-Image**, an image model for text-to-image generation and image
editing based on [MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3). It renders 8-megapixel images in 8 steps
without CFG and edits with up to 8 input images. Every component comes in bf16 and in ComfyUI's native int8 and 4-bit
formats. The smallest set is a 20 GB download that peaks at 21 GB of VRAM at 8 MP, against 143 GB of weights for
MiniMax-H3.

ComfyUI supports P-H3-Image natively, no custom nodes needed. The diffusers pipeline is
in [PrunaAI/P-H3-Image](https://huggingface.co/PrunaAI/P-H3-Image). Try it in the [Hugging Face Spaces](https://huggingface.co/spaces/PrunaAI/P-H3-Image). Read the full blog post [here](https://pruna.ai/blog/oss-p-h3-image-launch).

## Quickstart

1. **Update ComfyUI.** P-H3-Image support is on ComfyUI's master branch and ships with the next release. Until then,
update to the latest ComfyUI from GitHub (nightly). The desktop app and Comfy Cloud follow stable releases and get it
with the next one.



```bash
cd ComfyUI && git pull
```

2. **Download one file per component** into `ComfyUI/models`. The bf16 set, a 55 GB download plus the prompt upsampler,
peaks at about 56 GB of VRAM:



```bash
hf download PrunaAI/P-H3-Image-comfy --include "diffusion_models/p-h3-image_bf16.safetensors" "text_encoders/p-h3-image_text_encoder_bf16.safetensors" "text_encoders/p-h3-image_prompt_upsampler_bf16.safetensors" "vae/p-h3-image_vae_bf16.safetensors" --local-dir ComfyUI/models
```



The smallest set, a 20 GB download plus the prompt upsampler, peaks at about 21 GB of VRAM:



```bash
hf download PrunaAI/P-H3-Image-Comfy --include "diffusion_models/p-h3-image_w4a8.safetensors" "text_encoders/p-h3-image_text_encoder_w4a8.safetensors" "text_encoders/p-h3-image_prompt_upsampler_bf16.safetensors" "vae/p-h3-image_vae_int8_convrot.safetensors" --local-dir ComfyUI/models
```

3. **Open a workflow** from `workflows/`, type a short request and run. The
workflows render at 8 MP in 8 steps through the prompt upsampler.


## Pick your files

Pick one file per component. Files of different precisions can be mixed freely.

| Component | Folder | bf16 | int8 (`int8_convrot`) | w4a8 |
| --- | --- | :-: | :-: | :-: |
| Diffusion model | `diffusion_models/` | 40.5 GB | 21.2 GB | 13.4 GB |
| Text encoder | `text_encoders/` | 9.1 GB | 5.1 GB | 3.6 GB |
| Prompt upsampler | `text_encoders/` | 19.3 GB | 9.7 GB | 6.7 GB |
| VAE | `vae/` | 5.6 GB | 3.1 GB | – |
| LoRA for MiniMax-H3 | `loras/` | 2.0 GB | – | – |

| Set (model, text encoder, VAE) | Download | Peak VRAM at 8 MP |
| --- | :-: | :-: |
| bf16 | 55 GB | 56 GB |
| int8 | 30 GB | 31 GB |
| w4a8, int8 VAE | **20 GB** | **21 GB** |

![](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/resolve/main/assets/weights.png)

_Weights on disk. MiniMax-H3 counts its transformer, text encoder and video VAE._

The int8 set stays very close to bf16, often almost pixel for pixel. The w4a8 set keeps the quality but changes more
of the details and sometimes the composition. On a 48 GB L40S, where the bf16 set has to offload, the w4a8 set renders a
2048 × 2048 image in 6.3 s instead of 19 s.

![](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/resolve/main/assets/quantization.jpg)

_The same prompts and seed in bf16, int8 and w4a8, at 8 MP. The headers give the download size and the peak VRAM at_
_8 MP._

The quantized files use ComfyUI's native formats, need no calibration data and run on comfy-kitchen's INT8 kernels, for
NVIDIA Ampere or newer and AMD RDNA3/4.

- **int8 (`int8_convrot`).** Weights are rotated with grouped Hadamard transforms to spread outliers, then stored as
INT8 with per-row scales. Activations are quantized to INT8 on the fly.
- **w4a8.** The same rotation, then 4-bit weights on a 16-level codebook with an FP8 scale for every 16 inputs, and
INT8 activations. The layers most sensitive to 4-bit weights stay in int8.

## Workflows

| Workflow | What it does |
| --- | --- |
| `p-h3-image_text_to_image.json` | Text-to-image at 8 MP from a short request |
| `p-h3-image_edit.json` | Edits an image, with optional reference images |
| `p-h3-image_lora_text_to_image.json` | Text-to-image with the LoRA on your own MiniMax-H3 |
| `p-h3-image_lora_edit.json` | Editing with the LoRA on your own MiniMax-H3 |

The workflows use only ComfyUI's own nodes. Load Diffusion Model loads the model, followed by ModelSamplingMiniMaxH3 at
1.0 for both shifts. Load CLIP (type `minimax`) loads the text encoder, Load VAE the VAE, and p-h3-image Conditioning
turns the prompt and the images into the conditioning and the latent. The prompt upsampler runs on Generate Text, and
sampling on ManualSigmas with the 8-step grid, Basic Guider, `euler` and Sampler Custom Advanced, with no CFG or
negative prompt. The LoRA loads with ComfyUI's Load LoRA (Bypass, Model Only).

## Recommended resolutions

![](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/resolve/main/assets/resolutions.png)

| Aspect ratio | 8 MP (width × height) | 4 MP, for edits |
| :-: | :-: | :-: |
| 1:1 | **2912 × 2912** | 2048 × 2048 |
| 4:3 | **3360 × 2496** | 2368 × 1760 |
| 3:4 | **2496 × 3360** | 1760 × 2368 |
| 3:2 | **3552 × 2368** | 2496 × 1664 |
| 2:3 | **2368 × 3552** | 1664 × 2496 |
| 16:9 | **3872 × 2176** | 2720 × 1536 |
| 9:16 | **2176 × 3872** | 1536 × 2720 |

Text-to-image works best at 8 MP. In the workflows, Resolution Selector at 8 megapixels and a multiple of 32 gives
these sizes. Edits work best at 4 or 8 MP. In the edit workflows, Scale Image to Total Pixels brings `image_1`, the
image being edited, to 4 MP, and p-h3-image Conditioning generates the edit at its size unless `width` and `height` are
set. Reference images above about 8 MP are scaled down.

## Prompt upsampler

P-H3-Image is sensitive to prompting and renders full, specific prompts much better than short requests. The prompt
upsampler, based on Qwen3.5-9B, turns a one-line request into that prompt, and all example workflows use it. It thinks
about the request first and then writes the prompt.

It runs on ComfyUI's own nodes, the way FLUX.3 Klein's templates run theirs: Load CLIP (type `minimax`) and Generate
Text, with greedy decoding, so a request always gives the same prompt.

- **Text-to-image.** Format Text turns the request into the upsampler's input, `Aspect ratio: 1:1` and `Request: ...`
on two lines, and Generate Text runs with `thinking` on. Keep the aspect ratio the same as in Resolution Selector.
- **Edits.** Format Text writes the upsampler's input with a `<Picture N>` block for every image, and the images reach
Generate Text through Batch Images: `image_1` at 1 MP, the references padded to its size. The result is the edit
prompt for p-h3-image Conditioning.
- **Use prompt upsampler**, an If/Else switch, set to false sends the request to the model as it is.

The upsampler runs before P-H3-Image, and ComfyUI moves it out of VRAM when P-H3-Image needs the memory. Its output is
cached, so it only runs again when the request or the images change.

| Upsampler file | Size | Peak VRAM | Time per prompt, L40S |
| --- | :-: | :-: | :-: |
| `p-h3-image_prompt_upsampler_bf16` (recommended) | 19.3 GB | about 21 GB | about 7 s |
| `p-h3-image_prompt_upsampler_int8_convrot` | 9.7 GB | about 12 GB | about 13 s |
| `p-h3-image_prompt_upsampler_w4a8` | 6.7 GB | about 9 GB | about 11 s |

The w4a8 prompts differ most from bf16. Use the smaller files only when 21 GB does not fit.

## Editing

Connect the image to edit as `image_1` and up to 7 references after it, in the same order in Batch Images and on
p-h3-image Conditioning, with a `<Picture N>` block in Upsampler input for every image. The request can name the images
however you like, such as "the hat from the second photo".

![](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/resolve/main/assets/multi_image.jpg)

_Top, eight public-domain portraits and the dinner party P-H3-Image composed from them, from a one-sentence request._
_Bottom, eight scientists at a poker table, seven presidents wading through the swamp with an astronaut, and characters_
_from our own renders in the same swamp._

## Already have MiniMax-H3?

If you run MiniMax-H3 in ComfyUI, the 2 GB LoRA `loras/p-h3-image_lora_bf16.safetensors` runs P-H3-Image on its FL2VA
transformer without a second large download. Load `minimax_h3_fl2va_bf16.safetensors` from
[Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) (the pruned and quantized FL2VA files work too),
apply the LoRA with Load LoRA (Bypass, Model Only) at strength 1.0, and start from the `lora` workflows.

## Limitations

- **It is sensitive to prompting.** Keep the prompt upsampler in the graph. Hype words and very long prompts make
images worse, and very short prompts give weak results without it.
- **Hands can break, and small people in the background can come out distorted.** Rendering at 8 MP helps.
- **Text is not fully reliable.** Small or dense text turns into pseudo-text, and longer passages sometimes get single
letters wrong. Short quoted strings render well.
- **Quantized files are not identical to bf16.** int8 stays very close, w4a8 changes more of the details.

## License

The P-H3-Image weights are based on MiniMax-H3 and released under the [MiniMax H3 Community License](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/tree/main/LICENSE). Please
read it before use. Among other terms, it excludes the European Union, the United Kingdom, the Republic of Korea and
the United States unless you have a separate license from MiniMax, and products built on it must show "Powered by
MiniMax H3". The text encoder's Qwen3-VL-4B parts and the prompt upsampler, based on Qwen3.5-9B, are under the
[Apache License 2.0](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/tree/main/LICENSE-APACHE). See [NOTICE](https://huggingface.co/PrunaAI/P-H3-Image-Comfy/tree/main/NOTICE) for details.

## What's next?

- Compress your own models with [Pruna](https://github.com/PrunaAI/pruna) and give us a ⭐️ for more efficiency!
- Want to use our optimized image models right away? Check [P-Image-Ideogram](https://www.pruna.ai/p-image-ideogram) and [P-Image-Edit](https://www.pruna.ai/p-image-edit).

[Try our models](https://dashboard.pruna.ai/login?utm_source=huggingface&utm_medium=model_card&utm_campaign=hf_traffic)

Downloads last month782,946

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)

[Text-to-Image](https://huggingface.co/tasks/text-to-image "Learn more about text-to-image")

This model isn't deployed by any Inference Provider. [🙋1Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/13482)

## Model tree for PrunaAI/P-H3-Image-Comfy

Base model

[MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)

Finetuned

[PrunaAI/P-H3-Image](https://huggingface.co/PrunaAI/P-H3-Image)

Quantized

( [8](https://huggingface.co/models?other=base_model:quantized:PrunaAI/P-H3-Image))

this model

Quantizations

[3 models](https://huggingface.co/models?other=base_model:quantized:PrunaAI/P-H3-Image-Comfy)

## Spaces using PrunaAI/P-H3-Image-Comfy3

## Collection including PrunaAI/P-H3-Image-Comfy

[The latest Pruna model updates are listed for easy reference.•6 items•Updated 8 days ago• 2](https://huggingface.co/collections/PrunaAI/pruna-model-watch)

Inference providers allow you to run inference using different serverless providers.

StripeM-Inner
