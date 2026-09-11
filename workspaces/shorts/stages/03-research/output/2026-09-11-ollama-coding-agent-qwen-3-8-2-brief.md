---
slug: 2026-09-11-ollama-coding-agent-qwen-3-8-2
stage: 03-research
topic: "Ollama coding agent: Qwen 3.8 27B mxfp8 on one laptop"
depth: standard
generated_at: 2026-09-11T11:41:00Z
sources: 9
hub: "[[videos/2026-09-11-ollama-coding-agent-qwen-3-8-2]]"
---

# Research brief: Ollama coding agent: Qwen 3.8 27B mxfp8 on one laptop

## Summary
Thesis: the setup, not the model, is the story -- harness, context cap, sandbox. Most arresting number: the whole model is a single 32GB download that runs on a 48GB MacBook. Strongest concrete case: the HN-front-paged walkthrough (2026-09-10/11, 27 points) installs sbx, OpenCode and Ollama, pulls qwen3.8:27b-mxfp8, caps context at 65536 and launches in a sandbox. Could not be verified: tokens-per-second on this stack (community-only, 4 to 59.5 tok/s) and the llama.cpp-is-better argument. Conflict: Ollama's docs default a 48 GiB machine to 256k context while the walkthrough caps at 64K to avoid a lock-up -- that tension is the teaching beat, not an error.

## Thesis
Tonight, on one 48GB Mac, you can turn OpenCode loose on your code with Qwen 3.8 27B mxfp8 served by Ollama, because the walkthrough's real lesson is that the model is the easy part and the harness, the context cap and the sandbox are the actual setup.

## Explanation path
Start with the job, not the tools: a coding agent is a harness that lets a model read your files, run commands and edit code, so the viewer needs three pieces, the model server, the harness and the cage. Establish what OpenCode is (an open source agent that works in the terminal, IDE or desktop) and what Ollama does (serves the model with one command and defaults to MLX on Apple silicon). Then name the model: Qwen 3.8 27B, a dense vision-language model from the Qwen team that Qwen itself describes as compact and deployment-friendly, shipped in Ollama's library as qwen3.8:27b-mxfp8, a 32GB download where mxfp8 is a quantization that stores weights as 8-bit numbers with one scaling factor per block of 32 values. Before the walkthrough's numbers make sense the viewer must get two ideas: memory is the budget (a 32GB model plus context on a 48GB machine leaves little headroom), and context is the knob that spends it. Then land the walkthrough's three concrete moves: cap context to 64K so the system does not lock up when it runs out of memory, drop reasoning effort to low for agent turns, and run the agent inside Docker's sbx sandbox so a hallucinated command cannot trash the machine. Close on the payoff and the honest catch: it is slower than a cloud frontier model and the community argues about Ollama itself, but the whole stack runs on one laptop with no API key.

## Claims
1. **The HN walkthrough 'Setting up OpenCode with Ollama and sbx on Mac' is a blog post by a developer using an Apple MacBook Pro m5 48GB, who calls that machine the sweet spot for local development as it allows you to run 30B models with a decent sized context.**
   - Source: Running Opencode with Ollama on mac., https://tensorsandtokens.com/posts/opencode-ollama/
   - Tier: community | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "I'm using a Apple Macbook pro m5 48GB model. I think this is the sweet spot for local development as it allows you to run 30B models with a decent sized context."
2. **The walkthrough's install is three commands: brew install docker/tap/sbx for Docker's sandbox CLI, brew install anomalyco/tap/opencode for OpenCode, and the Ollama app downloaded from ollama.com; then ollama pull qwen3.8:27b-mxfp8 fetches the model.**
   - Source: Running Opencode with Ollama on mac., https://tensorsandtokens.com/posts/opencode-ollama/
   - Tier: community | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "brew trust docker/tap && brew install docker/tap/sbx" / "brew install anomalyco/tap/opencode" / "ollama pull qwen3.8:27b-mxfp8"
3. **The walkthrough caps the Qwen model's context at 65536 tokens in OpenCode's config, warning that limiting the context to 64k will ensure your system dose not lock up when it runs out of memory, and adds that 3GB is needed for the sandbox.**
   - Source: Running Opencode with Ollama on mac., https://tensorsandtokens.com/posts/opencode-ollama/
   - Tier: community | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "For the qwen model, we've limited the context to 64k, this will ensure your system dose not lock up when it runs out of memory. We also need 3GB for the sandbox."
4. **Docker documents sbx as a CLI whose sandboxes run AI coding agents in isolated microVM sandboxes where each sandbox gets its own Docker daemon, filesystem, and network, and states the sbx CLI is free to use, including for commercial work.**
   - Source: Docker Sandboxes -- Docker Docs, https://docs.docker.com/ai/sandboxes/
   - Tier: docs | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "Docker Sandboxes run AI coding agents in isolated microVM sandboxes. Each sandbox gets its own Docker daemon, filesystem, and network" / "The `sbx` CLI is free to use, including for commercial work."
5. **Ollama's library ships Qwen 3.8 27B in mxfp8 form as qwen3.8:27b-mxfp8, a 32GB download with 1.8M Downloads, runnable with the single command ollama run qwen3.8:27b-mxfp8.**
   - Source: qwen3.8:27b-mxfp8 -- Ollama, https://ollama.com/library/qwen3.8:27b-mxfp8
   - Tier: primary | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "1.8M DownloadsUpdated 3 weeks ago" / "464021588235 · 32GB ·" / "ollama run qwen3.8:27b-mxfp8"
6. **Qwen's model card describes Qwen3.8-27B as a compact, deployment-friendly dense model with 27B parameters, a context length of 262,144 natively and extensible up to 1,000,000 tokens, and reports SWE-bench Pro 61.7 for agentic coding.**
   - Source: Qwen/Qwen3.8-27B -- Hugging Face, https://huggingface.co/Qwen/Qwen3.8-27B
   - Tier: primary | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "Qwen3.8-27B brings these advances to a compact, deployment-friendly dense model" / "Context Length: 262,144 natively and extensible up to 1,000,000 tokens." / "SWE-bench Pro | **61.7**"
7. **OpenCode describes itself as an open source agent that helps you write code in your terminal, IDE, or desktop, supports any model from any provider including local models through 75+ LLM providers, and installs with curl -fsSL https://opencode.ai/install | bash.**
   - Source: OpenCode | The open source AI coding agent, https://opencode.ai/
   - Tier: docs | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "OpenCode is an open source agent that helps you write code in your terminal, IDE, or desktop." / "75+ LLM providers through Models.dev, including local models" / "curl -fsSL https://opencode.ai/install | bash"
8. **Ollama's context-length documentation defaults to 4k context below 24 GiB VRAM, 32k for 24-48 GiB, and 256k at 48 GiB or more, and says tasks which require large context like web search, agents, and coding tools should be set to at least 64000 tokens.**
   - Source: Context length -- Ollama, https://docs.ollama.com/context-length
   - Tier: docs | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "< 24 GiB VRAM: 4k context" / ">= 48 GiB VRAM: 256k context" / "Tasks which require large context like web search, agents, and coding tools should be set to at least 64000 tokens."
9. **NVIDIA's technical blog defines the quantization: the MXFP8 variant employs block-wise scaling, where a separate scaling factor represented in an 8-bit exponent-only format (E8M0) is assigned to each block of 32 consecutive values, further optimizing memory usage.**
   - Source: Floating-Point 8 -- NVIDIA Technical Blog, https://developer.nvidia.com/blog/floating-point-8-an-introduction-to-efficient-lower-precision-ai-training/
   - Tier: docs | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
   - Quote: "the MXFP8 variant employs block-wise scaling, where a separate scaling factor represented in an 8-bit exponent-only format (E8M0) is assigned to each block of 32 consecutive values, further optimizing memory usage"
10. **The Ollama library page for qwen3.8 lists an OpenCode application shortcut, ollama launch opencode --model qwen3.8, showing the model is pre-wired for the harness.**
    - Source: qwen3.8 -- Ollama, https://ollama.com/library/qwen3.8
    - Tier: primary | Confidence: high | Accessed: 2026-09-11 | Via: web_extract
    - Quote: "OpenCode`ollama launch opencode --model qwen3.8`"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | model download size on Ollama (mxfp8 tag) | 32GB | https://ollama.com/library/qwen3.8:27b-mxfp8 | "464021588235 · 32GB ·" |
| 2 | laptop used in the walkthrough | Apple MacBook Pro m5 48GB | https://tensorsandtokens.com/posts/opencode-ollama/ | "I'm using a Apple Macbook pro m5 48GB model." |
| 3 | context cap the walkthrough sets in OpenCode config | 65536 | https://tensorsandtokens.com/posts/opencode-ollama/ | "we've limited the context to 64k" |
| 4 | memory the walkthrough budgets for the sandbox | 3GB | https://tensorsandtokens.com/posts/opencode-ollama/ | "We also need 3GB for the sandbox." |
| 5 | native context length of Qwen3.8-27B per the model card | 262,144 natively and extensible up to 1,000,000 tokens | https://huggingface.co/Qwen/Qwen3.8-27B | "Context Length: 262,144 natively and extensible up to 1,000,000 tokens." |
| 6 | agentic coding benchmark, Claude Code harness (Qwen model card) | SWE-bench Pro 61.7 | https://huggingface.co/Qwen/Qwen3.8-27B | "SWE-bench Pro | **61.7**" |
| 7 | Ollama context default below 24 GiB VRAM | 4k context | https://docs.ollama.com/context-length | "< 24 GiB VRAM: 4k context" |
| 8 | Ollama minimum recommended context for agents and coding tools | at least 64000 tokens | https://docs.ollama.com/context-length | "should be set to at least 64000 tokens." |

## Analogy candidates
- **A food truck with a fixed parking spot**: the 32GB mxfp8 model is the truck, needing its spot (48GB of unified memory) rented up front; the context window is the counter space, and every order sitting on it takes room. Breaks when: the viewer asks about speed -- a food truck does not get slower as the counter fills, but a model's memory pressure does lock the machine up, which is exactly why the 64K cap exists.
- **A workshop with a rollaway toolbox**: Ollama is the workshop's power strip, OpenCode is the apprentice who walks to the shelves and picks tools, and sbx is the workshop being a rented bay where the apprentice cannot burn down your house. Breaks when: tools are deterministic while model output is probabilistic -- the apprentice can hallucinate a step that was never taught, which is the sandbox's actual reason to exist.

## Misconceptions
- Myth: A 27B model needs a datacenter GPU or a $30,000 rig. Reality: It is a single 32GB download that runs on a 48GB MacBook: Ollama's page lists qwen3.8:27b-mxfp8 at 32GB, and the walkthrough runs it on an Apple MacBook Pro m5 48GB (claims 1 and 5).
- Myth: Coding agents are cloud products; running one locally means self-hosting a server stack. Reality: OpenCode is an open source agent that runs in the terminal, and the Ollama library page ships an ollama launch opencode --model qwen3.8 shortcut, so the local stack is two installs and a pull command (claims 7 and 10).
- Myth: Bigger context is always better, so you should let the model use all 262,144 tokens it supports. Reality: The walkthrough caps context at 64K precisely because uncapped context spends memory the laptop does not have: limiting the context ensures your system does not lock up when it runs out of memory (claim 3).

## Glossary
- **coding agent**: A harness that lets a model read your files, run commands and edit code to finish a task, not just chat about it.
- **Ollama**: A free tool that downloads and serves local models behind one command, ollama run, so other software can talk to them like an API.
- **OpenCode**: An open source coding agent that works in your terminal, IDE or desktop and can use local models instead of cloud ones.
- **Qwen 3.8 27B**: A dense 27-billion-parameter model from the Qwen team built for coding and long-horizon agentic tasks, small enough for one laptop.
- **mxfp8**: A quantization that stores model weights as 8-bit numbers and gives each block of 32 values its own scaling factor, shrinking the model's memory footprint while keeping accuracy close.
- **context window**: The model's working memory: the maximum number of tokens it can hold, and every token of conversation and file contents sits inside it.
- **KV cache**: The memory the model allocates to remember the conversation so far; it grows as context fills, which is why uncapped context can lock up a laptop.
- **sbx**: Docker's sandbox CLI that runs an AI coding agent inside an isolated microVM with its own filesystem and network so it cannot touch host resources beyond what you share.
- **quantization**: Storing a model's numbers in fewer bits, trading a little accuracy for a much smaller memory footprint.
- **reasoning effort**: A dial on Qwen 3.8 that sets how much hidden thinking the model does before answering, from xhigh down to low.

## Unverified
- Community threads report the Qwen 3.8 27B mlx variant downloads as roughly an 18GB file and runs at speeds between 4 and 59.5 tok/s depending on the Mac chip.
- One HN commenter running the model on an M1 Max reports GPU temperatures around 95C with the stock fan curve, suggesting thermals are worth mentioning on sustained agent runs.
- The walkthrough's author says in the HN thread that he tried OMLX, MLX and LM Studio (now Bionic) and returned to Ollama because of stability issues, but this is one user's anecdote, not a benchmark.
- Commenters on the walkthrough's HN thread argue that llama.cpp is a more resource-frugal alternative to Ollama and link a community critique page, but no fetched primary page grounds that claim.
- The second HN lead about mining Qwen 3.8 reasoning traces resolved to a discussion of prefilling reasoning traces from GPT-5.5 Pro into Qwen 3.8, which is off the how-to angle and was not fetched into claims.
- No first-party tokens-per-second measurement exists for this exact stack on our own hardware; any speed claim in the script must be attributed to community reports or dropped.

## Suggested outline
1. Open cold on the promise: tonight your laptop becomes the coding agent's whole datacenter, no API key, no subscription.
2. Name the three pieces in one breath: the model server (Ollama), the agent (OpenCode), the cage (Docker's sbx).
3. Anchor the hardware early: a 48GB MacBook Pro is the walkthrough's machine, and 32GB of that is the model alone.
4. Pull the model on screen: ollama pull qwen3.8:27b-mxfp8, and unpack mxfp8 as 8-bit weights with a scaling factor per 32-value block, the reason 27B fits at all.
5. Explain the memory budget before the config: model plus context plus sandbox must fit in 48GB, which is why the next knob exists.
6. Cap the context: 65536 tokens in OpenCode's config, the walkthrough's explicit guard against the system locking up when it runs out of memory.
7. Drop reasoning effort to low for agent turns via /models, and note Ollama's own docs back the idea that coding agents need at least 64000 tokens of context.
8. Build the cage: an sbx kit whose spec.yaml points the agent at the host's Ollama on localhost:11434, then sbx run opencode --kit ./sbx-kit/.
9. Land the honest catch: this is slower than a cloud frontier model, thermals matter, and the community itself argues over whether Ollama is the right server.
10. Close on the state change: same laptop, now a self-contained coding agent; the viewer leaves with three installs and one config file between them and local agentic coding.

## Viewer situation
You have one laptop, a gaming PC or a Mac, you have downloaded a model in something like Ollama to try it, and you have watched cloud coding agents work but never pointed one at your own code.

## Has process
`true`
- Install the three tools: Docker's sbx CLI, OpenCode, and the Ollama app.
- Pull the model with ollama pull qwen3.8:27b-mxfp8.
- Create the sbx kit folder with spec.yaml and the OpenCode config file.
- Cap the Qwen model's context at 65536 tokens in the OpenCode config.
- Launch the agent with sbx run opencode --kit ./sbx-kit/.
- Drop reasoning effort to low via the /models command inside OpenCode.

## Objection
A 27B model at 64K context on a laptop will be too slow to be a productive agent compared with just paying for a frontier API, and a sandboxed agent is still one misconfigured network rule away from your host.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://tensorsandtokens.com/posts/opencode-ollama/ | Running Opencode with Ollama on mac. -- Tensors & Tokens | community | web_extract | 2026-09-11 |
| 2 | https://news.ycombinator.com/item?id=49652122 | Setting up OpenCode with Ollama and sbx on Mac -- Hacker News | community | web_extract | 2026-09-11 |
| 3 | https://ollama.com/library/qwen3.8:27b-mxfp8 | qwen3.8:27b-mxfp8 -- Ollama | primary | web_extract | 2026-09-11 |
| 4 | https://huggingface.co/Qwen/Qwen3.8-27B | Qwen/Qwen3.8-27B -- Hugging Face | primary | web_extract | 2026-09-11 |
| 5 | https://opencode.ai/ | OpenCode -- The open source AI coding agent | docs | web_extract | 2026-09-11 |
| 6 | https://ollama.com/library/qwen3.8 | qwen3.8 -- Ollama | primary | web_extract | 2026-09-11 |
| 7 | https://docs.docker.com/ai/sandboxes/ | Docker Sandboxes -- Docker Docs | docs | web_extract | 2026-09-11 |
| 8 | https://docs.ollama.com/context-length | Context length -- Ollama | docs | web_extract | 2026-09-11 |
| 9 | https://developer.nvidia.com/blog/floating-point-8-an-introduction-to-efficient-lower-precision-ai-training/ | Floating-Point 8 -- NVIDIA Technical Blog | docs | web_extract | 2026-09-11 |

## Notes
Nine pages fetched and cited, within the 8-12 standard band. The thinnest load-bearing fact is the blog walkthrough itself: it is a personal blog (tier 4) and is the sole source for the 64K context cap being the difference between usable and locked-up on a 48GB Mac, though Ollama's own docs independently recommend at least 64000 tokens for coding agents, which corroborates the direction. The walkthrough's blog typo 'dose not' is preserved verbatim inside the claim quote. HN thread gives the objection beat ('Friends don't let friends use Ollama') and the author's stability answer as honest-catch color. Conflict recorded: Ollama's docs default a 48GB+ machine to 256k context while the walkthrough manually caps at 64K; both stated, the tension is the teaching moment, not an error to average away. The 'Mining Qwen 3.8 reasoning trace' lead resolved to a distillation-controversy thread (reasoning prefill from GPT-5.5 Pro), off-angle for a how-to, so it stays under unverified.
