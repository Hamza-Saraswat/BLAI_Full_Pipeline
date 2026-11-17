---
slug: 2026-11-17-unsloth-computer-use-train-a-v
stage: 03-research
topic: "Unsloth computer use: train a vision agent on one GPU"
depth: standard
generated_at: 2026-11-17T12:38:37Z
sources: 9
hub: "[[videos/2026-11-17-unsloth-computer-use-train-a-v]]"
---

# Research brief: Unsloth computer use: train a vision agent on one GPU

## Summary
The load-bearing number is about 19 GB: the vision model Unsloth rates best at driving your screen, Qwen3.8-27B in GGUF form, fits in that much VRAM, and its 17.7 GB quant file corroborates it, so the whole trick runs on one consumer card. The strongest concrete case is Unsloth's own receipts demo: six runs of a real expense-report task on one A100, two perfect in 22 and 30 minutes, two misreads -- honest numbers the video can quote. What could not be verified: any first-party speed or memory measurement on our own hardware, the dollar cost of a full Claude computer-use task (docs give token overhead, not dollars), and community sentiment on the beta. One conflict to handle: the release notes say "local models see your screen" broadly, while the docs restrict computer use to local launches (no Docker, no WSL, no remote bind; X11 only on Linux), and OpenAI's help page simultaneously lists agent limits and says the agent "is no longer available."

## Thesis
Unsloth's v0.1.918-beta puts computer use on your own desk: a 27B vision model drives the screen from about 19 GB of VRAM, and the LoRA route to customize these open models fits one consumer GPU instead of a datacenter.

## Explanation path
Start with what computer use actually is: a vision model reads a screenshot, decides a click or a keystroke, and loops -- the same loop Anthropic and OpenAI run in the cloud, metered per request and per screenshot. Then land the event: Unsloth's v0.1.918-beta, released 2026-11-16, ships that loop as a local feature, off by default and gated by per-app approvals. Before any hardware claim, name the two shipped pieces so they never blur together: the computer-use loop runs existing local vision models (Qwen3.8-27B rated best, about 19 GB), while the new training story is MiniMax-H3-Image, MiniMax's open 33.1B image model now downloadable as GGUF, FP8 and INT8 with LoRA support. With the pieces named, do the memory math against the viewer's card: about 19 GB to drive the screen, 22 GB to QLoRA-finetune a 27B model, about 24 GB peak to train a MiniMax-H3-Image LoRA on the int8 base -- all inside one 24 GB GPU, with a 128 GB machine swimming in room. Then the honest catch, straight from Unsloth's own six-run receipts test (two perfect, two misread) and the beta's limits (local launches only, X11 on Linux, 100 to 200 actions per real task). Close on tonight's move: the 60-image, 150-step LoRA recipe that finished in about 100 seconds on a 96 GB card, and what to expect when the viewer repeats it.

## Claims
1. **Unsloth v0.1.918-beta, published 2026-11-16, ships computer use as a beta: local vision models see the screen and interact with apps across macOS, Windows and Linux, off by default with permission controls.**
   - Source: Release Computer Use, MiniMax-H3-Image + Perf fixes, unslothai/unsloth v0.1.918-beta, https://github.com/unslothai/unsloth/releases/tag/v0.1.918-beta
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "**Computer use (beta):** Local vision models and connected providers can now see your screen and interact with apps. Off by default, with permission controls." (Release assets are timestamped 2026-11-16T15:04:16Z.)
2. **The same release adds MiniMax-H3-Image support: GGUF weights for CPU, Mac and AMD, FP8 and INT8 weights for NVIDIA, and LoRA training.**
   - Source: Release Computer Use, MiniMax-H3-Image + Perf fixes, unslothai/unsloth v0.1.918-beta, https://github.com/unslothai/unsloth/releases/tag/v0.1.918-beta
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "**MiniMax-H3-Image:** GGUF support for CPU, Mac and AMD, plus FP8 and INT8 weights for NVIDIA. LoRA training is also supported."
3. **The model Unsloth rates best at computer use, Qwen3.8-27B in GGUF form, needs about 19 GB with its vision file, consistent with the 17.7 GB UD-Q4_K_XL quant file on Unsloth's repo.**
   - Source: Computer Use with Local LLMs | Unsloth Documentation, https://unsloth.ai/docs/basics/computer-use
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "Best in our tests: finished the receipts and GIMP tasks on its own. About 19 GB with its vision file" (the unsloth/Qwen3.8-27B-GGUF repo lists "UD-Q4_K_XL 17.7 GB").
4. **Unsloth's own requirements table puts QLoRA (4-bit) fine-tuning of a 27B model at 22 GB of VRAM minimum, and 16-bit LoRA of the same at 64 GB.**
   - Source: Unsloth Requirements | Unsloth Documentation, https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "Check this table for VRAM requirements sorted by model parameters and fine-tuning method. QLoRA uses 4-bit, LoRA uses 16-bit." (Table row: "27B | 22GB | 64GB"; the page calls these "the absolute minimum.")
5. **The MiniMax-H3-Image LoRA recipe is real and timed: 150 steps on 60 tarot cards took about 100 seconds on an RTX PRO 6000, and training needs 32 GB+ of GPU memory (an estimate; tested on 96 GB) or the int8 base at about 24 GB peak.**
   - Source: MiniMax-H3-Image | Unsloth Documentation, https://unsloth.ai/docs/models/minimax-h3-image
   - Tier: primary | Confidence: medium | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "Train a style or subject LoRA in Unsloth: 150 steps on 60 tarot cards took about 100 seconds on an RTX PRO 6000." ... "**GPU memory:** 32 GB+ (estimate; tested on 96 GB). bf16 base with 56 GB+ free (45.5 GB peak), else int8 (about 24 GB peak)."
6. **Unsloth's own reliability test is mixed: across six runs of a receipts task, Qwen3.8-27B on one A100 at about 130 tokens a second got everything right twice (22 and 30 minutes), while two runs misread one amount, one stopped before the deck, and one charted the wrong column.**
   - Source: Computer Use with Local LLMs | Unsloth Documentation, https://unsloth.ai/docs/basics/computer-use
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "We ran this task six times with Qwen3.8-27B on one A100, at about 130 tokens a second. Two runs got everything right, in 22 and 30 minutes ... Two misread one amount, one stopped before making the deck, and one charted the Date column."
7. **MiniMax-H3-Image itself is a 33.1B-parameter dense diffusion transformer released under the MiniMax-H3-Image Community License Agreement, with the BF16 checkpoint at 68.65 GB.**
   - Source: MiniMaxAI/MiniMax-H3-Image - Hugging Face, https://huggingface.co/MiniMaxAI/MiniMax-H3-Image
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "**Diffusion transformer**: 33.1B parameters, a dense single-stream transformer with 50 layers" ... "| **MiniMax-H3-Image** | Text-to-image and image editing | BF16 (DiT) | 68.65 GB |"
8. **MiniMax-H3-Image-PE, the optional prompt expander, is a separate model fine-tuned from Qwen3.8-27B, shipped as NVFP4 at 17.9 GB, under the MiniMax-H3-Image Community License Agreement on top of Qwen's Apache 2.0 base.**
   - Source: MiniMaxAI/MiniMax-H3-Image-PE - Hugging Face, https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "MiniMax-H3-Image-PE weights (fine-tuned from Qwen3.8-27B, FP4), task and system prompts, and a client example" (the MiniMax-H3-Image model zoo lists "MiniMax-H3-Image-PE (optional) | Prompt expander for text-to-image | NVFP4 | 17.9 GB").
9. **On the cloud side, Anthropic's computer-use toolset adds about 4,500 input tokens to a request before any work happens, and every screenshot comes back billed as image input.**
   - Source: Computer use tool - Claude Platform Docs, https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
   - Tier: primary | Confidence: high | Accessed: 2026-11-17 | Via: web_extract
   - Quote: "Declaring `computer_toolset_20260801` with its default members adds about 4,500 input tokens to a request: about 4,590 on Claude Sonnet 5 and about 4,520 on the other supported models." ... "Screenshot and zoom images returned in tool results, billed as image input"
10. **OpenAI's documented agent limits were 40 messages per month on Plus and 400 on Pro -- and the same page now says ChatGPT agent is no longer available, folded into ChatGPT Work.**
    - Source: ChatGPT agent | OpenAI Help Center, https://help.openai.com/en/articles/11752874-chatgpt-agent
    - Tier: primary | Confidence: medium | Accessed: 2026-11-17 | Via: web_extract
    - Quote: "Agent mode includes the following monthly message limits: - **Plus:** 40 messages/month - **Pro:** 400 messages/month" ... "ChatGPT agent is no longer available. Use ChatGPT Work for longer, multi-step tasks and finished deliverables."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | VRAM for the best-tested computer-use model (Qwen3.8-27B GGUF with vision file) | about 19 GB | https://unsloth.ai/docs/basics/computer-use | "About 19 GB with its vision file" |
| 2 | Minimum VRAM to QLoRA (4-bit) fine-tune a 27B model | 22 GB | https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements | "27B \| 22GB \| 64GB" (QLoRA 4-bit vs LoRA 16-bit) |
| 3 | Peak GPU memory training a MiniMax-H3-Image LoRA on the int8 base | about 24 GB peak | https://unsloth.ai/docs/models/minimax-h3-image | "bf16 base with 56 GB+ free (45.5 GB peak), else int8 (about 24 GB peak)" |
| 4 | Unsloth's timed LoRA run (150 steps, 60 images) | about 100 seconds on an RTX PRO 6000 | https://unsloth.ai/docs/models/minimax-h3-image | "150 steps on 60 tarot cards took about 100 seconds on an RTX PRO 6000" |
| 5 | Anthropic computer-use toolset overhead per request | about 4,500 input tokens | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool | "adds about 4,500 input tokens to a request" |
| 6 | ChatGPT agent monthly limit, Plus plan | 40 messages/month | https://help.openai.com/en/articles/11752874-chatgpt-agent | "**Plus:** 40 messages/month" |
| 7 | MiniMax-H3-Image-PE download size (NVFP4) | 17.9 GB | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | "Prompt expander for text-to-image \| NVFP4 \| 17.9 GB" |

## Analogy candidates
- **A new hire driving your desktop over your shoulder**: the model sees only what is on the screen and moves the same mouse and keyboard you use, asking approval the way Unsloth asks before the first action and each new app. Breaks when: a human intern remembers your apps after day one; the model re-reads a fresh screenshot at every step, so long tasks drift -- a real task takes 100 to 200 actions, and two of Unsloth's six receipt runs misread or quit.

## Misconceptions
- Myth: Teaching an AI to use your computer is a cloud-company, datacenter-scale project. Reality: Unsloth's own numbers put the screen-driving model at about 19 GB and QLoRA fine-tuning of a 27B model at 22 GB of VRAM -- one consumer GPU, not a rack (claims 3 and 4).
- Myth: Computer use means handing an AI unrestricted control of your machine. Reality: Unsloth's beta is off by default, asks before the first action in each chat and before each new app, keeps blocked apps inaccessible, and never types into OS security prompts (claim 1).

## Glossary
- **computer use**: an AI feature where a model looks at screenshots of your screen and drives your mouse and keyboard to do tasks inside your apps.
- **vision-language model**: a model that understands images as well as text.
- **LoRA**: a small set of adapter weights trained on top of a frozen base model, teaching it a style or skill without rewriting the whole model.
- **QLoRA**: LoRA training with the base model compressed to 4-bit precision, cutting the memory it needs to a fraction.
- **quantization (GGUF, FP8, INT8, 4-bit)**: storing model weights in fewer bits so the model fits in less memory, at a small cost in quality.
- **GGUF**: a single-file model format that runs on CPUs, Macs and AMD GPUs as well as NVIDIA cards.
- **VRAM**: the memory on your graphics card that the model and its context have to fit inside.
- **prompt expander**: a helper model that rewrites your short request into a long, detailed prompt before image generation.
- **token**: the word-sized chunk of text that models read and write, and the unit APIs bill by.

## Unverified
- No first-party measurement exists yet for how fast these models run on the channel's own DGX Spark; any tokens-per-second claim for our hardware is untested.
- The dollar cost of a complete Claude computer-use task could not be computed from the docs, which give token overhead but no per-task dollar figure.
- Community sentiment on the computer-use beta (Reddit, X, forums) was not fetched this session, so any "people say it is stable or buggy" line is unsupported.
- Whether MiniMax-H3-Image LoRA training actually fits a 24 GB card at int8 in practice is an estimate from the docs (the 32 GB+ figure is labeled an estimate, tested on 96 GB) and has not been verified on real 24 GB hardware.

## Suggested outline
1. Open on the metered world: Anthropic's computer-use toolset adds about 4,500 input tokens before the first screenshot, and OpenAI capped its agent at 40 messages a month on Plus -- then the turn: yesterday Unsloth shipped the same loop for your own GPU.
2. Show the goods: the computer-use beta driving a real desktop with Qwen3.8-27B in about 19 GB, plus MiniMax-H3-Image (33.1B, now GGUF, FP8 and INT8) with LoRA training -- and the memory math that keeps it all on one consumer card.
3. Land the recipe and the honest catch: 60 captioned images, 150 steps, about 100 seconds on a 96 GB card and about 24 GB peak at int8, against the beta's own numbers -- two of six receipt runs perfect, local launches only -- so the viewer leaves knowing exactly what one GPU buys and what it does not.

## Viewer situation
You've got a gaming PC with a 24 GB graphics card, you've watched Claude and ChatGPT agents drive screens for a metered fee, and you've assumed teaching one to do that yourself would take a datacenter.

## Has process
true
- Install Unsloth newer than 2026.11.4 (clone the repo and run the local installer until the next release ships it).
- Open Images, then Train, and set Model family to MiniMax-H3-Image.
- Upload about 60 captioned images of one style or subject, with a trigger word such as trtcrd in every caption.
- Check the defaults: 150 steps, rank 32, resolution 1024, base precision Auto.
- Click Start training and watch the loss line and the sample previews (about 8 minutes end to end in Unsloth's run).
- Click Deploy to Create and prompt with your trigger word at weight 1.0.

## Objection
It's a beta: two of Unsloth's own six receipt runs misread an amount or quit early, a 27B local model is not Claude, and the training floor is an estimate tested on a 96 GB card, so "one GPU" buys you privacy and flat cost, not cloud-grade reliability.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/unslothai/unsloth/releases/tag/v0.1.918-beta | Release Computer Use, MiniMax-H3-Image + Perf fixes (unslothai/unsloth) | primary | web_extract | 2026-11-17 |
| 2 | https://unsloth.ai/docs/basics/computer-use | Computer Use with Local LLMs - Unsloth Documentation | primary | web_extract | 2026-11-17 |
| 3 | https://unsloth.ai/docs/models/minimax-h3-image | MiniMax-H3-Image - Unsloth Documentation | primary | web_extract | 2026-11-17 |
| 4 | https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements | Unsloth Requirements - Unsloth Documentation | primary | web_extract | 2026-11-17 |
| 5 | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | MiniMaxAI/MiniMax-H3-Image - Hugging Face | primary | web_extract | 2026-11-17 |
| 6 | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE | MiniMaxAI/MiniMax-H3-Image-PE - Hugging Face | primary | web_extract | 2026-11-17 |
| 7 | https://huggingface.co/unsloth/Qwen3.8-27B-GGUF | unsloth/Qwen3.8-27B-GGUF - Hugging Face | primary | web_extract | 2026-11-17 |
| 8 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool | Computer use tool - Claude Platform Docs | primary | web_extract | 2026-11-17 |
| 9 | https://help.openai.com/en/articles/11752874-chatgpt-agent | ChatGPT agent - OpenAI Help Center | primary | web_extract | 2026-11-17 |

## Notes
Do not conflate the two MiniMax models: MiniMax-H3-Image is the 33.1B image diffusion transformer, while MiniMax-H3-Image-PE is a separate 27B prompt-expander LLM fine-tuned from Qwen3.8-27B; Unsloth's LoRA training section covers the image model. The release notes' "letting local models see your screen" is narrower in the docs: local launches only (no Docker, no WSL, no network bind, not via API key), Linux needs an X11 session, and the training VRAM floor of 32 GB+ is an estimate tested on 96 GB. OpenAI's page both lists the 40/400 limits and says the agent is no longer available; quote the limits as documented on 2026-11-17 and expect them to move. The release also reports a 2048px image decoding "in 0.28s instead of 2.82s on an A100 80GB," held back from key numbers as peripheral to the thesis.
