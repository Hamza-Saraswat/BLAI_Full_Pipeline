---
slug: 2026-10-14-lfm2-5-24b-a2b-a-24b-moe
stage: 03-research
topic: "LFM2.5-24B-A2B: a 24B MoE that runs like a 2B"
depth: standard
generated_at: 2026-10-14T11:40:31Z
sources: 10
hub: "[[videos/2026-10-14-lfm2-5-24b-a2b-a-24b-moe]]"
---

# Research brief: LFM2.5-24B-A2B, a 24B MoE that runs like a 2B

## Summary
Liquid AI shipped LFM2.5-24B-A2B on October 13, 2026: a reasoning model that stores 24.0B parameters but computes each token through only 2.45B of them, which is why it can decode at 184 tokens/s on a laptop-class Apple M5 Max. The strongest concrete case is the vendor's own table: it beats Qwen3.6-35B-A3B, a MoE with about 50% more total and active parameters, on 5 of 8 agentic and tool-use benchmarks (LiveClaw 48.09 vs 38.19). What could not be verified: community reception (Reddit returned 403), the Hugging Face trending rank, and any independent benchmark of this exact model -- Artificial Analysis has only the predecessor, which it rates below average. One conflict to handle on camera: Liquid claims day-one ecosystem support, but Ollama's `lfm2.5` library page still lists only the 8B variant, so the honest day-one command is llama.cpp's one-liner.

## Thesis
LiquidAI's LFM2.5-24B-A2B keeps 24B parameters in memory but computes each token with only 2.45B of them, so a laptop runs a 24B model at small-model speed -- 184 tokens/s on an Apple M5 Max.

## Explanation path
Start from the one distinction the whole video hangs on: a model's total parameter count is what memory pays for, while its active parameter count is what speed pays for; establish that before any product name appears. Then walk one token through the model: 24.0B parameters stored, a router inside each mixture-of-experts block paging 4 of 64 experts, 2.45B parameters actually computing. Only then land the measured payoff -- 184 tokens per second decode on an Apple M5 Max using 15 GB of memory at Q4_K_M -- and immediately follow with the honest catch: all 24B still sit in memory, knowledge-heavy benchmarks go to the bigger Qwen (the vendor's own table says so), and Ollama's `lfm2.5` tag today pulls the 8B model, so the real day-one command is the llama.cpp one-liner.

## Claims
1. **Liquid AI released LFM2.5-24B-A2B, a 24B-parameter reasoning model with just 2B active parameters, built for fast, private agents on-device; it is the largest and final model in the LFM2.5 family.**
   - Source: LFM2.5-24B-A2B: Built for Fast On-Device Agents, https://www.liquid.ai/blog/lfm2-5-24b-a2b
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "Today, we release **LFM2.5-24B-A2B**, a 24B-parameter reasoning model with just 2B active parameters, built for fast, private agents on-device. It is the largest and final model in the LFM2.5 family"
2. **The announcement is dated October 13, 2026, and both the base and post-trained models are open-weight on Hugging Face.**
   - Source: Run fast, private agents on-device with LFM2.5-24B-A2B, https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b
   - Tier: docs | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "Published October 13, 2026"
3. **The model card's spec list gives 24.0B total parameters and 2.45B active parameters per token.**
   - Source: LiquidAI/LFM2.5-24B-A2B model card, https://huggingface.co/LiquidAI/LFM2.5-24B-A2B
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "**Total parameters**: 24.0B ... **Active parameters**: 2.45B"
4. **The architecture has 40 layers (30 double-gated short convolution blocks plus 10 GQA), 64 experts per MoE block with top-4 routing, and a 131,072-token context window, extended from the predecessor's 32,768.**
   - Source: LiquidAI/LFM2.5-24B-A2B model card, https://huggingface.co/LiquidAI/LFM2.5-24B-A2B
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "**Number of layers**: 40 (30 double-gated short convolution blocks + 10 GQA) ... **Experts**: 64 per MoE block, top-4 routing ... **Context length**: 131,072 tokens ... the context window extension from 32,768 to 131,072 tokens"
5. **Day-one runtimes are Transformers, llama.cpp, vLLM, SGLang, MLX and LM Studio (plus ONNX and FP8 checkpoints); on MLX you must install mlx-lm>=0.32.0 because earlier versions route the experts incorrectly.**
   - Source: LFM2.5-24B-A2B -- Liquid Docs, https://docs.liquid.ai/lfm/models/lfm25-24b-a2b
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "**Install** (requires `mlx-lm>=0.32.0`, earlier versions route the experts incorrectly):"
6. **At Q4_K_M with llama.cpp it decodes 184 tokens/s on an Apple M5 Max and 114 tokens/s on an AMD Ryzen AI Max+ 395, up to 1.7x faster than the next comparable MoE, while using the least memory of the compared models (15 GB on the M5 Max, 4K-token input context).**
   - Source: LFM2.5-24B-A2B: Built for Fast On-Device Agents, https://www.liquid.ai/blog/lfm2-5-24b-a2b
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "It decodes 184 tokens/s on an Apple M5 Max and 114 tokens/s on an AMD Ryzen AI Max+ 395, up to 1.7x faster than the next-best model, while using the least memory." (table row: "Apple M5 Max | Memory (GB) | LFM2.5-24B-A2B | 15"; settings: "Q4\_K\_M quantization, measured with llama.cpp, and 4K-token input context.")
7. **On Liquid's own 16-benchmark table it is competitive with Qwen3.6-35B-A3B, a model with ~50% more total and active parameters, leading on five of eight agentic and tool-use benchmarks: LiveClaw 48.09 versus 38.19 and AutomationBench 27.69 versus 8.72 (all evals run with vLLM by Liquid AI).**
   - Source: LFM2.5-24B-A2B: Built for Fast On-Device Agents, https://www.liquid.ai/blog/lfm2-5-24b-a2b
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "LFM2.5-24B-A2B is competitive with Qwen3.6-35B-A3B, a model with ~50% more total and active parameters, on five of eight agentic and tool-use benchmarks, scoring 48.09 on LiveClaw versus 38.19 and 27.69 on AutomationBench versus 8.72."
8. **The same table shows where it loses: GPQA Diamond 74.42 versus Qwen3.6-35B-A3B's 83.69, and SWE-Bench Verified (OpenCode) 51.00 versus 66.20; Liquid itself recommends pairing it with retrieval or web search for knowledge-heavy work.**
   - Source: LFM2.5-24B-A2B: Built for Fast On-Device Agents, https://www.liquid.ai/blog/lfm2-5-24b-a2b
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "Larger models keep an edge on knowledge-heavy benchmarks like GPQA Diamond, HLE, and AA-Omniscience, and on coding benchmarks like SWE-Bench Verified (OpenCode) and SciCode."
9. **The official GGUF repo lists a 14.5 GB Q4_K_M build and a 13.6 GB Q4_0 build that is a Quantization-Aware Distillation checkpoint trained to recover accuracy lost to quantization; the repo showed 17,807 downloads in its first day, and runs with one llama.cpp line.**
   - Source: LiquidAI/LFM2.5-24B-A2B-GGUF model card, https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
   - Quote: "The Q4\_0 build in this repository is the Quantization-Aware Distillation (QAD) checkpoint ... It was trained to recover the accuracy lost to Q4\_0 quantization." (size list: "Q4\_K\_M 14.5 GB"; sidebar: "Downloads last month 17,807")
10. **Ollama's lfm2.5 tag list, fetched on 2026-10-14, contains only the 8B family -- five tags, all of them 8b-a1b variants at 5.2 GB to 17 GB -- so `ollama run lfm2.5` does not get you this 24B model yet.**
    - Source: Tags -- lfm2.5, https://ollama.com/library/lfm2.5/tags
    - Tier: docs | Confidence: high | Accessed: 2026-10-14 | Via: web_extract
    - Quote: "lfm2.5:8b-a1b-q8\_0 ... 9.0GB · 125K context window · Text · 4 months ago" (the page's complete five-tag list: latest, 8b, 8b-a1b-q4\_K\_M, 8b-a1b-q8\_0, 8b-a1b-bf16)

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total parameters (all stored in memory) | 24.0B | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B | "**Total parameters**: 24.0B" |
| 2 | active parameters per token | 2.45B | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B | "**Active parameters**: 2.45B" |
| 3 | experts per MoE block / routing | 64 per MoE block, top-4 routing | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B | "**Experts**: 64 per MoE block, top-4 routing" |
| 4 | decode speed on Apple M5 Max (llama.cpp, Q4_K_M, 4K-token input) | 184 tokens/s | https://www.liquid.ai/blog/lfm2-5-24b-a2b | "It decodes 184 tokens/s on an Apple M5 Max" |
| 5 | memory in use on Apple M5 Max (llama.cpp, Q4_K_M, 4K-token input) | 15 GB | https://www.liquid.ai/blog/lfm2-5-24b-a2b | "Apple M5 Max \| Memory (GB) \| LFM2.5-24B-A2B \| 15" |
| 6 | download size of the Q4_K_M GGUF | 14.5 GB | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF | "Q4\_K\_M 14.5 GB" |
| 7 | LiveClaw score vs Qwen3.6-35B-A3B (vendor-run, vLLM) | 48.09 | https://www.liquid.ai/blog/lfm2-5-24b-a2b | "scoring 48.09 on LiveClaw versus 38.19" |
| 8 | context length | 131,072 tokens | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B | "**Context length**: 131,072 tokens" |

## Analogy candidates
- **A specialist clinic with 64 doctors where a triage nurse pages exactly 4 per patient visit**: the full roster (24B parameters) is on staff and paid for in memory, but each visit (each token) is handled by just the 4 specialists paged (2.45B active parameters), so visits are fast while the expertise on call is huge. Breaks when: the clinic pays all 64 salaries whether or not they are paged -- RAM cost never shrinks with activity -- and it hides that the nurse (the router) takes a small cut of every single visit.
- **A tradesperson's van carrying the full tool inventory, where each job touches only a few tools**: the van is the 14.5 GB Q4_K_M download holding all 24B parameters; you haul the whole kit so any specialty is on hand, but a given job moves at small-kit speed. Breaks when: a van does not choose its own tools -- the model's router scores and picks experts fresh for every token, and different tokens pick different tools, which the van image flattens out.

## Misconceptions
- Myth: A 24B model is out of reach for a laptop; big model always means big, slow inference. Reality: memory does hold all 24B (a 14.5 GB Q4_K_M download, 15 GB in use on an M5 Max), but each token computes through only 2.45B parameters, so decode speed tracks a small model -- 184 tokens/s measured with llama.cpp (claims 3 and 6).
- Myth: If only about 2B parameters are active, it must think like a 2B model; the 24B is marketing. Reality: capacity is stored across 64 experts per MoE block and selected per token (claim 4); it beats the bigger Qwen3.6-35B-A3B on 5 of 8 agentic benchmarks (claim 7) while losing GPQA Diamond and SWE-Bench (claim 8) -- the win is agent skill and speed, not encyclopedic knowledge.

## Glossary
- **parameter**: a learned number inside a model; more parameters usually means more capability, and always means more memory.
- **mixture of experts (MoE)**: a model design that stores many specialist sub-networks and, for each token, activates only the few a gatekeeper picks.
- **expert**: one specialist sub-network inside the model; LFM2.5-24B-A2B has 64 to choose from in each MoE block.
- **active parameters**: the subset of the model's parameters that actually compute on a given token -- here 2.45B out of 24.0B.
- **router (top-4 routing)**: the small network that scores all experts and picks which 4 handle each token.
- **token**: a chunk of text roughly a word long; models read and write one token at a time.
- **tokens per second (tok/s)**: how fast a model generates text; higher means snappier replies.
- **quantization (Q4_K_M)**: storing model weights in fewer bits to shrink memory; here it turns 24B parameters into a 14.5 GB file.
- **GGUF**: the single-file format that llama.cpp-based tools load; one download is the whole model.
- **reasoning model**: a model that writes an explicit chain of thought before its final answer; this one always does.

## Unverified
- Community reception threads on r/LocalLLaMA and r/LocalLLM returned 403 this session, so any community-reported tokens-per-second figures or quality impressions are unverified.
- The Hugging Face trending rank of 234 and the like counts come from the stage-02 idea note, not from a page fetched this session.
- Tokens per second on our own DGX Spark and consumer GPUs is not yet measured; the only fetched numbers are Liquid's (Apple M5 Max 184 tok/s, AMD Ryzen AI Max+ 395 114 tok/s, both llama.cpp at Q4_K_M).
- Artificial Analysis has not evaluated LFM2.5-24B-A2B itself; whether independent testers rate its intelligence above the predecessor's is unknown.
- An Ollama tag for LFM2.5-24B-A2B may appear after this brief is written; the gap was verified only on 2026-10-14.

## Suggested outline
1. Open on the impossible-sounding number: a 24B-parameter model decoded at 184 tokens per second on a laptop, because 21.55B of those parameters never touched that token.
2. One scenario carries the explanation: follow a single token through the clinic -- the router pages 4 of 64 specialists per block, 2.45B parameters fire, the other 21.55B wait their turn; total parameters are what memory pays for, active parameters are what speed pays for.
3. The honest catch, said plainly: all 24B still sit in memory (15 GB at Q4_K_M), it loses GPQA Diamond and SWE-Bench to the bigger Qwen, and Ollama's lfm2.5 tag is still the 8B -- so the real day-one move is the llama.cpp one-liner on a 14.5 GB download.

## Viewer situation
You run models at home in Ollama or LM Studio on a 16-to-32 GB Mac or gaming PC, you have watched small models fly and 24B-class models crawl, and you just saw "a 24B MoE that runs like a 2B" start trending on Hugging Face.

## Has process
false

## Objection
All 24B parameters still have to sit in memory (15 GB even at 4-bit), and 2.45B active genuinely caps depth -- it lost GPQA Diamond 74.42 to 83.69 and SWE-Bench 51.00 to 66.20 against the bigger Qwen3.6-35B-A3B -- so you are trading some of what it knows for how fast it moves.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.liquid.ai/blog/lfm2-5-24b-a2b | LFM2.5-24B-A2B: Built for Fast On-Device Agents (Liquid AI blog) | primary | web_extract | 2026-10-14 |
| 2 | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B | LiquidAI/LFM2.5-24B-A2B model card | primary | web_extract | 2026-10-14 |
| 3 | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF | LiquidAI/LFM2.5-24B-A2B-GGUF model card | primary | web_extract | 2026-10-14 |
| 4 | https://docs.liquid.ai/lfm/models/lfm25-24b-a2b | LFM2.5-24B-A2B -- Liquid Docs | primary | web_extract | 2026-10-14 |
| 5 | https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b | Run fast, private agents on-device with LFM2.5-24B-A2B (HF blog) | docs | web_extract | 2026-10-14 |
| 6 | https://ollama.com/library/lfm2.5/tags | Tags -- lfm2.5 (Ollama) | docs | web_extract | 2026-10-14 |
| 7 | https://ollama.com/library/lfm2.5 | lfm2.5 (Ollama) | docs | web_extract | 2026-10-14 |
| 8 | https://ollama.com/library/lfm2:24b-a2b | lfm2:24b-a2b (Ollama) | docs | web_extract | 2026-10-14 |
| 9 | https://artificialanalysis.ai/models/lfm2-24b-a2b | LFM2 24B A2B -- Artificial Analysis | benchmark | web_extract | 2026-10-14 |
| 10 | https://www.liquid.ai/blog/lfm2-24b-a2b | LFM2-24B-A2B: Scaling Up the LFM2 Architecture (Liquid AI blog) | primary | web_extract | 2026-10-14 |

## Notes
All benchmark, speed and memory numbers are vendor-run (Liquid AI, evaluated with vLLM; edge metrics via llama.cpp Q4_K_M on Pipette) and should be attributed to Liquid on camera. Artificial Analysis has only the predecessor LFM2-24B-A2B: 23.8B total and 2.3B active parameters, rated 6 (estimated) on the AA Intelligence Index and described as "below average in intelligence" among similar open-weight non-reasoning models -- a reason to hedge quality claims for the new model until independent numbers exist. Ollama's lfm2:24b-a2b tag (23.8B params, Q4_K_M 14 GB, 1.1M downloads, updated 7 months ago) is the older LFM2-24B-A2B, not this release; do not show it as the way to run LFM2.5. The model card sidebar showed 4,067 downloads within the first day. API price on Liquid Console: "$.10/1M input tokens (at $.05 for cached input) and $1.00/1M output tokens". MLX users need mlx-lm>=0.32.0; earlier versions route the experts incorrectly.
