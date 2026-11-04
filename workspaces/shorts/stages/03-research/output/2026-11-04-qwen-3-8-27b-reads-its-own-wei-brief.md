---
slug: 2026-11-04-qwen-3-8-27b-reads-its-own-wei
stage: 03-research
topic: "Qwen 3.8 27B reads its own weights on a laptop"
depth: standard
generated_at: 2026-11-04T12:44:24Z
sources: 14
hub: "[[videos/2026-11-04-qwen-3-8-27b-reads-its-own-wei]]"
---

# Research brief: Qwen 3.8 27B reads its own weights on a laptop

## Summary
The hook number is absurd on its face: a 17 GB model file spent 46m 12s and 43,506 reasoning tokens to name the right game from raw weights, three times out of four -- on a laptop, no cloud. The strongest concrete case is the Pac-Man transcript: roughly 104,838 input tokens of bare decimals, a 17,253-parameter toy network, an answer at 72% confidence. What could not be verified: any first-party tokens-per-second on a DGX Spark or laptop, and the paper's own headline claims (only its abstract, quoted secondhand). One conflict noted below: 17GB (Simon, Q4_K_M file) versus 18GB (Ollama's whole default tag) describe different scopes, not a disagreement. The thesis deliberately corrects the title's framing: the model read another network's weights, not its own.

## Thesis
A 27B open-weights model you can run tonight on a 17 GB download can be handed thousands of raw weight numbers and infer what the tiny network they belong to was trained to do -- not magic, not its own weights, but real weight-reading you can reproduce locally.

## Explanation path
Start with what a weight is: one number among millions that decides how strongly a signal passes; the model is nothing but these numbers, so reading them is reading the machine. Establish that a laptop-class 27B model is now a 17 GB download, not a lab cluster -- a dense vision-language model with 64 layers and a 262,144-token context that fits tonight's hardware. Then the event: Simon Willison pasted the raw floating-point weights of a tiny game-playing network into the prompt -- no tools allowed -- and the model reasoned for three quarters of an hour before naming the right game, three times out of four. Walk one identification in detail, because the mechanics are the payoff: every large weight in a row is a clue about one grid cell's job, and the model mutters through them for tens of thousands of reasoning tokens. Before the audience overclaims, land the two limits: the network read was a 17,253-parameter toy, not the model's own 27 billion; and it failed the one game too obscure to guess. Close on how to run the experiment tonight and what honest expectation looks like: hours, not seconds; partial credit, not omniscience; and the same test had a cloud frontier model only slightly faster.

## Claims
1. **Simon Willison ran the no-tools "which game is this network?" weight-reading test on Qwen 3.8 27B running locally on his laptop, and it correctly identified 3 of the 4 game networks from raw weights alone.**
   - Source: Qwen 3.8 27B on my laptop can interpret model weights, too, https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
   - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
2. **What the model read was a tiny 17,253-parameter policy network described in the prompt text, not Qwen's own weights.**
   - Source: Qwen-weights.md (Simon Willison transcript gist), https://gist.github.com/simonw/387d3a7927f165b1986bb6c2099d0f53
   - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "A policy network (multilayer perceptron) with 500 inputs, two hidden layers of 32 units with tanh activations, and 5 outputs ... 17,253 parameters in total. It was trained with reinforcement learning (PPO) to maximise the reward of a game played on this grid."
3. **The Pac-Man identification succeeded after 46m 12s and 43,506 reasoning tokens, answering "Game: A simplified Pac-Man-style gridworld" at 72% self-reported confidence.**
   - Source: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
   - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "After 46m 12s and 43,506 reasoning tokens, Qwen on my laptop returned a response that ended like this ... Confidence: 72%"
4. **Qwen 3.8 27B is officially a 27B-parameter dense vision-language model (exact count 27,781,427,952 BF16 parameters) with a native context length of 262,144 tokens, Apache-2.0, weights live since 2026-08-14.**
   - Source: Qwen/Qwen3.8-27B model card, https://huggingface.co/Qwen/Qwen3.8-27B (exact count via https://huggingface.co/api/models/Qwen/Qwen3.8-27B)
   - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "Context Length: 262,144 natively and extensible up to 1,000,000 tokens." / safetensors total: 27781427952
5. **The local run used LM Studio at a long context window because "the default 8192 context failed with errors", via the llm CLI's -f fragment option with LMSTUDIO_TIMEOUT=900.**
   - Source: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
   - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "I fired up LM Studio, ensured Qwen 3.8 27B was loaded with a long context window (the default 8192 context failed with errors)"
6. **The four prompts come from the companion repo of the Sparks of Weight-Space Programming paper, RikiyaT/lm_understand-logs, whose exp1_which_game folder holds the four game prompt.txt files.**
   - Source: RikiyaT/lm_understand-logs, https://github.com/RikiyaT/lm_understand-logs
   - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
7. **Ollama ships Qwen3.8 27B as its default tag: an 18GB download with a 256K context window, language-model blob Q4_K_M, 27.3B parameters, 17GB, plus an uncompressed BF16 CLIP vision projector (461M parameters, 931MB).**
   - Source: qwen3.8:27b - Ollama, https://ollama.com/library/qwen3.8:27b
   - Tier: docs | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "model archqwen35 · parameters27.3B · quantizationQ4_K_M · 17GB" / "projector archclip · parameters461M · quantizationBF16 · 931MB"
8. **LM Studio's catalog rates the model "laptop size" with minimum system memory of 16GB, and Unsloth's requirement table puts 4-bit quants on 16-19GB of total memory (RTX 5080, 4090, or a 24GB Mac).**
   - Source: Qwen3.8 - How to Run Locally - Unsloth Documentation, https://unsloth.ai/docs/models/qwen3.8 (LM Studio floor via https://lmstudio.ai/models/qwen/qwen3.8-27b)
   - Tier: docs | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "Qwen3.8-27B 4-bit quants work on 16-19GB VRAM like RTX 5080, 4090 or a Mac with 24GB RAM." / "Minimum system memory 16GB"
9. **After a broken DeltaNet CUDA path in older llama.cpp builds produced garbage output at full speed, an updated build (about b10450 with matching shared libraries) runs the model clean at ~42.9 tok/s on an RTX 3090 24GB under WSL CUDA with MTP speculative decoding.**
   - Source: Discussion #27164, https://github.com/ggml-org/llama.cpp/discussions/27164
   - Tier: benchmark | Confidence: medium | Accessed: 2026-11-04 | Via: web_extract
   - Quote: "The model could load successfully and run quickly while still generating completely invalid output." / "Final result on my RTX 3090: Clean Qwen3.8-27B output ~42.9 tok/s"
10. **Qwen missed Freeway (an obscure 1981 Atari game), guessing "A simplified Pac-Man-like grid game" instead; the traces are "almost incomprehensible" and a patient human "could get there with enough effort".**
    - Source: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
    - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
    - Quote: "Qwen failed at the Freeway prompt ... I expect a sufficiently experienced human being armed with a notepad and a pencil could get there with enough effort."
11. **The same Breakout prompt was answered correctly by the cloud frontier model Kimi K3.1 Pro after 9m 41s and 19,493 reasoning tokens -- the local 27B needed 52m 25s for its 88%-confidence answer.**
    - Source: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
    - Tier: primary | Confidence: high | Accessed: 2026-11-04 | Via: web_extract
    - Quote: "which successfully guessed Breakout after 9m 41s and 19,493 reasoning tokens"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | parameters in the toy network that was read (not Qwen's own) | 17,253 parameters in total | https://gist.github.com/simonw/387d3a7927f165b1986bb6c2099d0f53 | "17,253 parameters in total" |
| 2 | games identified correctly | 3 of 4 | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | "Qwen failed at the Freeway prompt" (the other three succeeded) |
| 3 | Simon's local model file size (Q4_K_M GGUF) | 17GB | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | "it's just 17GB (I use this version... Qwen3.8-27B-Q4_K_M.gguf)" |
| 4 | Pac-Man run duration | 46m 12s | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | "After 46m 12s and 43,506 reasoning tokens" |
| 5 | Pac-Man reasoning tokens | 43,506 reasoning tokens | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | "After 46m 12s and 43,506 reasoning tokens" |
| 6 | input tokens per weight prompt | 104,838 input tokens | https://gist.github.com/simonw/387d3a7927f165b1986bb6c2099d0f53 | "104,838 input" |
| 7 | Breakout confidence | 88% | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | "Confidence: 88%" |
| 8 | exact Qwen3.8-27B parameter count (BF16) | 27,781,427,952 | https://huggingface.co/api/models/Qwen/Qwen3.8-27B | safetensors total: 27781427952 |
| 9 | native context window | 262,144 tokens | https://huggingface.co/Qwen/Qwen3.8-27B | "Context Length: 262,144 natively and extensible up to 1,000,000 tokens." |
| 10 | Ollama default 27B tag download size | 18GB | https://ollama.com/library/qwen3.8:27b | "18GB · 256K context window" |
| 11 | minimum system memory (LM Studio catalog) | 16GB | https://lmstudio.ai/models/qwen/qwen3.8-27b | "Minimum system memory 16GB" |
| 12 | 4-bit quant total-memory band (Unsloth) | 16-19GB VRAM | https://unsloth.ai/docs/models/qwen3.8 | "4-bit quants work on 16-19GB VRAM" |
| 13 | measured decode speed, RTX 3090 24GB, WSL CUDA, MTP on (benchmark tier) | ~42.9 tok/s | https://github.com/ggml-org/llama.cpp/discussions/27164 | "Clean Qwen3.8-27B output ~42.9 tok/s" |
| 14 | cloud comparison: Kimi K3.1 Pro Breakout run | 9m 41s and 19,493 reasoning tokens | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | "successfully guessed Breakout after 9m 41s and 19,493 reasoning tokens" |
| 15 | HN traction for the source post (why-now) | 649 points, 189 comments | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | radar item hn-6857dc224a (simonwillison.net, score 80) |

## Analogy candidates
- **Song from raw WAV samples**: identify a song by reading its raw sample values instead of listening; the model reads thousands of bare decimals like -2.107, 1.169, 0.513 and infers "paddle on the bottom row, ball above". Breaks when: Qwen only recognizes games it already knows -- the obscure Freeway "waveform" got identified as Pac-Man.
- **Detective reading a diary written in pure arithmetic**: each weight row is a clue about one grid cell's job (agent / ghost / pellet / wall), and 43,506 reasoning tokens is the detective muttering line by line. Breaks when: cost -- one hunch takes 46 minutes to over an hour, and the pages are "almost incomprehensible" even to skim.
- **Reading assembly to guess the program**: weights are the machine code of a neural net, the model the reverse engineer with no disassembler. Breaks when: the target was a 17,253-parameter toy, not a real model; doing this to a 27B model is not what happened and is not plausible at this speed.

## Misconceptions
- Myth: Qwen read its own weights. Reality: it read a tiny 17,253-parameter game-playing policy network pasted into the prompt; it never touched its own 27 billion parameters (claim 2).
- Myth: Local AI is now superhuman at reading neural nets. Reality: 3-for-4 on famous games, and Simon expects "a sufficiently experienced human being armed with a notepad and a pencil could get there with enough effort" (claim 10).
- Myth: It answers instantly like a magic trick. Reality: 46 minutes to 1h 16m per run on roughly 104,838 input tokens, needing a long context window because the default 8192 failed (claims 3, 5).
- Myth: If it loads and streams at full speed, the model is working. Reality: older llama.cpp CUDA builds ran it at full speed and "roughly 19 GB" VRAM while emitting pure garbage through a broken DeltaNet path; one DGX Spark user's identical symptoms came from a corrupted GGUF (claim 9).
- Myth: A 27B model needs a lab or 27GB-plus of pro hardware. Reality: the default Ollama tag is an 18GB download (17GB Q4_K_M blob), LM Studio's floor is 16GB, Unsloth puts 4-bit at 16-19GB (claims 7, 8).

## Glossary
- **weight**: one number among millions that decides how strongly a signal passes through the network; the model is nothing but these numbers.
- **policy network**: the small network that was read -- 500 grid inputs, two hidden layers of 32 units, 5 action outputs, trained with PPO to play a grid game.
- **reasoning tokens**: tokens the model generates internally while thinking before its final answer; 43,506 to 69,787 per run here.
- **Weight-Space Programming**: the paper's term for LLMs analyzing and modifying raw neural network weights directly, using reasoning instead of training loops.
- **GGUF / Q4_K_M**: the single-file quantized weight format runtimes load, and the 4-bit scheme that makes a 27B model a 17GB download.
- **context window**: how much text the model can hold at once; the weight prompts need about 104,838 tokens, and the default 8192 failed with errors.
- **thinking mode**: Qwen 3.8's default behavior of generating visible reasoning before answering, tunable via reasoning_effort.

## Unverified
- The paper's own headline numbers (GPT-6 Astra raising MATH-500 from 7.9% to 48.1% and IFEval by 3x by editing 0.016% of Qwen3.5-0.8B's weights) are quoted from Simon's post quoting the abstract; the paper itself was not fetched this run.
- Real tokens-per-second on our own DGX Spark or a laptop for this model is not publicly measured; willitrunai's 13.8 tok/s (range 10.4-16.2) for a DGX Spark is a bandwidth-formula estimate flagged EST. with no public result, and no first-party Spark number exists yet.
- How much of the weight-reading ability survives 4-bit quantization is unmeasured; no fetched page benchmarks introspection quality per quant.
- Simon's laptop hardware (which Mac or chip, RAM) is not stated in the post or the gists.
- The exact context length Simon set in LM Studio is not stated; only that the default 8192 failed with errors.
- The first llama.cpp build that shipped the fixed DeltaNet CUDA path is not pinned; the thread only names broken commit 221f0f6 and working approximately-b10450 (ece963f41).

## Suggested outline
1. Hook: your laptop model can read another network's mind -- thousands of raw weight numbers in, the right game out, three times out of four.
2. What a weight is: one number among millions that decides how strongly a signal passes; the model is nothing but these numbers.
3. Tonight's hardware reality: a 27B vision-language model is an 18GB download, 16GB floor, 17GB Q4_K_M file -- no lab cluster.
4. The event: Simon Willison pasted the raw weights of a tiny game network into the prompt, no tools allowed, and asked which game it plays.
5. The mechanics, walked slow: every large weight row is a clue about one grid cell's job; the model mutters through them for 43,506 reasoning tokens.
6. The score: Pac-Man right in 46m 12s at 72%, Breakout right at 88%, Pong right, Freeway wrong -- obscure games beat it.
7. The honest limit: it read a 17,253-parameter toy, not its own 27 billion; a cloud frontier model did the same job in 9m 41s; a patient human with a notepad could too.
8. Run it tonight: ollama run qwen3.8:27b or LM Studio, long context (default 8192 fails), grab the prompt from RikiyaT/lm_understand-logs, expect hours and partial credit.
9. Close: weights are readable -- slowly, partially, on your own machine; that is the door this opens.

## Viewer situation
You have a gaming PC or a Mac with 16GB-plus of memory and you have run a local model before, but you treat its weights as an opaque file you download and never look inside.

## Has process
`true`
- Install a runtime (Ollama or LM Studio) and download the model: ollama run qwen3.8:27b (18GB download) or load the Q4_K_M GGUF in LM Studio.
- Raise the context window well past the default 8192 tokens -- the weight prompt is about 104,838 input tokens.
- Grab a raw-weights prompt file from the RikiyaT/lm_understand-logs repo (exp1_which_game folder).
- Paste the prompt as one single-shot message with no tools enabled.
- Leave it alone for about an hour while it reasons, then read the answer and its confidence.

## Objection
This is one anecdote on a 17,253-parameter toy network with self-reported confidence and zero tool use; it does not scale to real models and proves nothing about the model understanding its own weights.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/ | Qwen 3.8 27B on my laptop can interpret model weights, too | primary | web_extract | 2026-11-04 |
| 2 | https://gist.github.com/simonw/387d3a7927f165b1986bb6c2099d0f53 | Qwen-weights.md (transcripts: Pac-Man, Pong, Breakout) | primary | web_extract | 2026-11-04 |
| 3 | https://gist.github.com/simonw/6ed68f659e26a32e7d9096391d92f326 | Freeway failure transcript | primary | web_extract | 2026-11-04 |
| 4 | https://github.com/RikiyaT/lm_understand-logs | RikiyaT/lm_understand-logs (paper's prompt repo) | primary | web_extract | 2026-11-04 |
| 5 | https://huggingface.co/Qwen/Qwen3.8-27B | Qwen/Qwen3.8-27B model card | primary | web_extract | 2026-11-04 |
| 6 | https://huggingface.co/api/models/Qwen/Qwen3.8-27B | HF model repo API (JSON) | primary | web_extract | 2026-11-04 |
| 7 | https://qwen.ai/blog?id=qwen3.8 | Qwen3.8-Max announcement blog | primary | web_extract | 2026-11-04 |
| 8 | https://github.com/QwenLM/Qwen3.8 | QwenLM/Qwen3.8 GitHub README | primary | web_extract | 2026-11-04 |
| 9 | https://ollama.com/library/qwen3.8:27b | qwen3.8:27b - Ollama | docs | web_extract | 2026-11-04 |
| 10 | https://ollama.com/library/qwen3.8 | qwen3.8 - Ollama (family page) | docs | web_extract | 2026-11-04 |
| 11 | https://lmstudio.ai/models/qwen/qwen3.8-27b | qwen/qwen3.8-27b - LM Studio | docs | web_extract | 2026-11-04 |
| 12 | https://unsloth.ai/docs/models/qwen3.8 | Qwen3.8 - How to Run Locally - Unsloth | docs | web_extract | 2026-11-04 |
| 13 | https://github.com/ggml-org/llama.cpp/discussions/27164 | llama.cpp discussion #27164 (DeltaNet CUDA fix, 3090 speeds) | benchmark | web_extract | 2026-11-04 |
| 14 | https://willitrunai.com/models/qwen-3.8-27b | willitrunai VRAM/speed estimates (EST.) | benchmark | web_extract | 2026-11-04 |

## Notes
The angle's "reads its own weights" framing is technically false and the brief corrects it deliberately (misconception 1): the model read a 17,253-parameter toy network described in the prompt, never its own parameters. The script should keep the hook and pay off the correction honestly. Cross-check: willitrunai's 38.5 tok/s RTX 3090 estimate is consistent with the discussion's measured ~42.9 tok/s with MTP on. Conflict note: Ollama's page says 18GB download / 17GB model blob while Simon says "just 17GB" for his Q4_K_M file; both are kept verbatim, they describe the same quant at different scopes (with/without projector).

## Decisions
- Checkpoint (step 2): confirmed angle "A 27B model you can run tonight can be prompted to explain and locate its own weights -- no API, no lab cluster" with slug 2026-11-04-qwen-3-8-27b-reads-its-own-wei; no redirect. Kept despite the "its own weights" imprecision because the demo's reality (it reads another network's weights) is recorded as misconception 1 and the correction is part of the story the script must land.
- Depth standard, 14 sources fetched across 3 research questions via one 3-worker fan-out (page contents cached under output/sources/, never entering the orchestrator context); FireCrawl unavailable (402, 0 credits until 2026-11-22), workers fell back to web search + fetch per rules/firecrawl-usage.md.
