---
slug: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r
stage: 03-research
topic: "Hy-Memory-30B-A3B: a 30B that remembers"
depth: standard
generated_at: 2026-10-17T11:38:41Z
sources: 10
hub: "[[videos/2026-10-17-hy-memory-30b-a3b-a-30b-that-r]]"
---

# Research brief: Hy-Memory-30B-A3B: a 30B that remembers

## Summary
The news is not a chat model that remembers you; it is a model whose only job is deciding what your assistant remembers; every memory framework has been paying a frontier model to do that bookkeeping after every turn. The most arresting number is 55.49% vs 54.62%: a ~3B-active open writer edged Claude Opus 5 across four memory harnesses on Tencent's matrix. The strongest concrete case is the day-one local story: Apache-2.0 weights, a community Q4_K_M GGUF at 18.237 GB running in llama.cpp, and a 30 GB MLX build decoding at ~51 tok/s on an M3 Max. What could not be verified: community reception (the r/LocalLLaMA thread failed to fetch twice) and any third-party benchmark; none was found. Conflict: Hugging Face's own pages disagree on the community-quant count (7 in the filtered listing, 8 on the model card's tree), and no advertised maximum context length appears anywhere -- 32768 is one quantizer's tested allocation, not a vendor limit.

## Thesis
Tencent's Hy-Memory-30B-A3B is not a bigger brain for your chat model but a 30B-total, ~3B-active specialist that writes the external memory bank for frameworks like Mem0 and MemOS, matching Claude Opus 5 on the write task at a fraction of the serving cost.

## Explanation path
Establish the nightly frustration first: close the window and the local model forgets you, and the instinctive fix, a bigger context window, costs more memory per chat and still wipes on reset. Before any model appears, establish the idea that actually persists: a memory bank that lives outside the model, which frameworks like Mem0 and MemOS already provide -- and whose hidden cost is that a big general-purpose model does the write-path bookkeeping after every turn. With that cost in view, introduce what Tencent trained: a 30B-total, ~3B-active mixture-of-experts whose whole skill is deciding what to keep, how to phrase it, and what to overwrite. Deliver the surprise as a score: 55.49% macro average against 54.62% for Claude Opus 5, and 44.37 for the same-size Qwen3-30B-A3B. Then make it tangible on the viewer's own hardware: Apache-2.0 weights, a Q4_K_M GGUF at 18.237 GB for llama.cpp, a 30 GB MLX build for Macs, and an official vLLM serving path. Land on the reframe: memory is becoming a small local service sitting next to your chat model rather than a bigger model -- and close on the honest catch that every number so far comes from Tencent's own subsampled benchmark.

## Claims
1. **Hy-Memory-30B-A3B is a memory writer, not a chat model: a compact long-term-memory writer with ~3B active parameters, built by Tencent Hunyuan to execute the write path inside external memory frameworks.**
   - Source: tencent/Hy-Memory-30B-A3B model card, https://huggingface.co/tencent/Hy-Memory-30B-A3B
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "Hy-Memory-30B-A3B is a compact long-term-memory writer model (~3B active parameters) developed by Tencent Hunyuan to execute the write path inside external memory frameworks."
2. **It drops into Mem0, MemOS and Hy-Memory in place of the general-purpose LLM those frameworks normally call, and transfers with no further training to EverMemOS, a memory framework it never saw in training.**
   - Source: tencent/Hy-Memory-30B-A3B model card, https://huggingface.co/tencent/Hy-Memory-30B-A3B
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "It directly replaces the general-purpose LLM inside Mem0, MemOS, and Hy-Memory (covering Chat, Working, and Coding scenarios) ... and transfers directly to unseen memory frameworks such as EverMemOS."
3. **On fixed 20% benchmark subsamples across four memory harnesses, it posts a 55.49% macro average versus 54.62% for Claude Opus 5, ranking first on all four harnesses including the held-out EverMemOS.**
   - Source: arXiv 2610.22196 abstract, https://arxiv.org/abs/2610.22196
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "Hy-Memory-30B-A3B ranks first on all four evaluated harnesses, including held-out EverMemOS, with a 55.49% macro average versus 54.62% for Claude Opus 5."
4. **It outscores the same-size open MoE Qwen3-30B-A3B on the same matrix by a wide margin: 55.49 vs 44.37 macro average.**
   - Source: tencent/Hy-Memory-30B-A3B model card (Table 1), https://huggingface.co/tencent/Hy-Memory-30B-A3B
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "Qwen3-30B-A3B | 39.81 | 45.67 | 45.44 | 46.57 | 44.37"
5. **Config confirms a mixture-of-experts architecture (HYV3ForCausalLM, model type hy_v3) with 128 experts and 8 routed per token, 30064725888 total parameters in BF16, an apache-2.0 license tag, and weights on Hugging Face since 2026-10-15.**
   - Source: Hugging Face API record for tencent/Hy-Memory-30B-A3B, https://huggingface.co/api/models/tencent/Hy-Memory-30B-A3B
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "num_experts: 128, num_experts_per_tok: 8 ... license:apache-2.0 ... createdAt: 2026-10-15T09:52:00.000Z"
6. **Community GGUF quantizations appeared within about a day; Q4_K_M lands at 18.237 GB (decimal) and runs in llama.cpp builds with hy_v3 architecture support (tested revision f3363593f457169cdfbdfe22ea399b1cc139ba18), after the converter corrected an expert-width mismatch in the publisher config, validated on an M4 Max with 64 GB unified memory.**
   - Source: rapatsky/Hy-Memory-30B-A3B-GGUF model card, https://huggingface.co/rapatsky/Hy-Memory-30B-A3B-GGUF
   - Tier: benchmark | Confidence: medium | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "Tested with llama.cpp revision f3363593f457169cdfbdfe22ea399b1cc139ba18. Use a build with HY V3 (hy_v3) architecture support."
7. **On Apple silicon, an 8-bit MLX build measures 30 GB with a 7.0 s load and ~51 tok/s decode on an M3 Max (64 GB), scoring 100% extraction recall on a 15-case / 70-fact eval; a 17 GB mixed 4/6-bit variant scored identically on that eval.**
   - Source: hermitdave/Hy-Memory-30B-A3B-MLX-8bit model card, https://huggingface.co/hermitdave/Hy-Memory-30B-A3B-MLX-8bit
   - Tier: benchmark | Confidence: medium | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "8.0 bits per weight · 30 GB · effectively lossless ... Decode ~51 tok/s / ~65 tok/s"
8. **The vendor serving path is vLLM (tested with v0.31.0) behind an OpenAI-compatible API, with a no-think mode for extraction calls.**
   - Source: tencent/Hy-Memory-30B-A3B model card, https://huggingface.co/tencent/Hy-Memory-30B-A3B
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "Deploy the model with vLLM (tested with v0.31.0) using --served-model-name hy-memory, then call the OpenAI-compatible API."
9. **The model ships inside a full open-source stack: the Hy-Memory framework (Apache-2.0, pip install hy-memory==2.0.2) and MemHub, a local-first desktop and CLI app that unifies memory across tools like Claude Code, Cursor, Codex, OpenCode and Qwen Code.**
   - Source: Tencent-Hunyuan/Hy-Memory repository README, https://github.com/Tencent-Hunyuan/Hy-Memory
   - Tier: primary | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
   - Quote: "unifies conversation history and coding traces from user-authorized AI applications (such as Claude Code, Cursor, Codex, OpenCode, and Qwen Code) into a single managed runtime and local data directory, enabling governed cross-application memory recall."
10. **Early independent coverage flags the caveats: every score is Tencent's own matrix on 20% subsamples, and two of the four harnesses are statistical ties with Claude Opus 5 (60.55 vs 60.53 on Hy-Memory; 50.51 vs 50.50 on MemOS).**
    - Source: explainx.ai analysis, https://explainx.ai/blog/tencent-hy-memory-30b-a3b-open-memory-writer-model-mem0-memos-2026
    - Tier: docs | Confidence: high | Accessed: 2026-10-17 | Via: web_extract
    - Quote: "Those are Tencent's numbers, not an independent test ... On the Hy-Memory harness the two are 60.55 versus 60.53, and on MemOS 50.51 versus 50.50. Those are ties."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total parameters (all experts resident, BF16) | 30064725888 parameters | https://huggingface.co/api/models/tencent/Hy-Memory-30B-A3B | "total: 30064725888" |
| 2 | active parameters per token | ~3B active parameters | https://huggingface.co/tencent/Hy-Memory-30B-A3B | "a compact long-term-memory writer model (~3B active parameters)" |
| 3 | four-harness macro average (Tencent matrix, 20% subsamples) | 55.49% | https://arxiv.org/abs/2610.22196 | "with a 55.49% macro average versus 54.62% for Claude Opus 5" |
| 4 | Claude Opus 5 macro average, same matrix | 54.62% | https://arxiv.org/abs/2610.22196 | "with a 55.49% macro average versus 54.62% for Claude Opus 5" |
| 5 | Qwen3-30B-A3B macro average, same matrix | 44.37 | https://huggingface.co/tencent/Hy-Memory-30B-A3B | "Qwen3-30B-A3B \| 39.81 \| 45.67 \| 45.44 \| 46.57 \| 44.37" |
| 6 | Q4_K_M GGUF file size | 18.237 GB (decimal) | https://huggingface.co/rapatsky/Hy-Memory-30B-A3B-GGUF | "Q4_K_M \| 18.237 \| 16.984 \| 4.85" |
| 7 | MLX 8-bit build size | 30 GB | https://huggingface.co/hermitdave/Hy-Memory-30B-A3B-MLX-8bit | "8.0 bits per weight · 30 GB · effectively lossless" |
| 8 | MLX 8-bit decode speed on M3 Max (64 GB) | ~51 tok/s | https://huggingface.co/hermitdave/Hy-Memory-30B-A3B-MLX-8bit | "Decode \| ~51 tok/s \| ~65 tok/s" |

## Analogy candidates
- **Night porter at a law firm**: The lawyers (your chat model) argue cases by day; the porter (Hy-Memory-30B-A3B) reads everything that crossed the desk overnight and files, merges and corrects the cabinet (the memory bank) so any lawyer can find the precedent without rereading every document. Breaks when: a porter only files papers, while the writer must also strike and rewrite old entries when new evidence contradicts them, and each firm (Mem0, MemOS, Hy-Memory) keeps different filing rules -- this porter was trained to follow all of them.
- **Sports statistician keeping the season ledger**: After every game the statistician updates the record book (new streaks, corrected errors) so the commentator (your chat model) can call tonight's game with the whole season in hand without replaying every match. Breaks when: a ledger mostly appends, while the writer must reconcile conflicts and drop what no longer matters, and the statistician works for one league whereas this model transfers to frameworks it never saw.

## Misconceptions
- Myth: This is a chat model with a giant context window you talk to directly. Reality: it is a specialist writer that a memory framework calls after each conversation chunk; your chat model stays whatever it already is and this model never answers you (claims 1, 2).
- Myth: ~3B active means it fits in the memory of a 3B dense model. Reality: all 128 experts stay resident -- 30064725888 parameters total, still 18.237 GB at Q4_K_M -- the ~3B active cuts compute per token, not the weights you load (claims 5, 6).
- Myth: "Remembers" means the memory is inside the model's weights. Reality: memories live in an external bank the framework owns; the model only writes and edits that bank, which is exactly why the same model drops into Mem0, MemOS, Hy-Memory and even the unseen EverMemOS (claims 1, 2).

## Glossary
- **memory writer**: a model whose only job is deciding what an agent should store, how to phrase it, and when to update or overwrite what is already stored.
- **write path**: the half of a memory system that runs after each conversation chunk and edits the stored memories, as opposed to the read path that fetches them when a new question arrives.
- **memory bank**: the external store a memory framework maintains (vectors, graphs, database rows); it survives restarts and holds the memories, not the model.
- **active parameters**: in a mixture-of-experts model, the share of weights actually used for a given token; ~3B active means cheap compute per token while the full 30B of weights sit in memory.
- **GGUF**: the single-file format that llama.cpp-based tools load; a quantized GGUF shrinks a model to one downloadable file.
- **Q4_K_M**: a popular llama.cpp quantization preset that keeps most weights at around 4 bits with some tensors higher, trading a little quality for a much smaller file.
- **MLX**: Apple's machine-learning framework for Apple silicon; the usual way to run models locally on a Mac.
- **Mem0 / MemOS**: open-source agent-memory frameworks; Hy-Memory-30B-A3B plugs into either as the model that writes the memories.

## Unverified
- A r/LocalLLaMA thread on the release exists (seen in search results) and reportedly discusses about 12 GB of RAM at 131k context versus a comparable Qwen MoE, but the page failed to fetch twice, so the figure and the sentiment are unconfirmed.
- No third-party (non-Tencent) benchmark of the memory-writing scores was found; every number in the matrix is the vendor's own.
- Official Ollama or LM Studio library support is unconfirmed; the documented runtimes are vLLM v0.31.0, llama.cpp builds with hy_v3 support, and MLX-LM or oMLX on Apple silicon.
- The model's advertised maximum context length is not stated on the model card; the 32768 in the llama.cpp example is one quantizer's tested allocation, not a vendor limit.
- Tokens per second on the DGX Spark has not been measured yet.

## Suggested outline
1. Open on the reset: your local model forgets everything between chats, and the fix is not a bigger context window -- it is memory that lives outside the model.
2. What Tencent shipped: a 30B-total, ~3B-active specialist that does the bookkeeping Mem0 and MemOS used to pay a frontier model for, edging Claude Opus 5 (55.49% vs 54.62%) and crushing same-size Qwen3-30B-A3B (44.37).
3. Tonight's angle and the honest catch: Apache-2.0 weights with day-one GGUF (18.237 GB at Q4_K_M) and MLX (30 GB) builds, but every score is Tencent's own 20% subsample -- run it, do not crown it.

## Viewer situation
You chat with a local model in Ollama or LM Studio, and every new conversation starts from zero -- it has no idea what you told it yesterday.

## Has process
false

## Objection
Every number is Tencent's own benchmark on 20% subsamples, two of the four harnesses are statistical ties with Opus 5, and the writer only matters if you already run a memory framework -- nothing here improves a bare chat server on its own.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/tencent/Hy-Memory-30B-A3B | tencent/Hy-Memory-30B-A3B · Hugging Face | primary | web_extract | 2026-10-17 |
| 2 | https://arxiv.org/abs/2610.22196 | [2610.22196] Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing | primary | web_extract | 2026-10-17 |
| 3 | https://huggingface.co/api/models/tencent/Hy-Memory-30B-A3B | Hugging Face API record for tencent/Hy-Memory-30B-A3B | primary | web_extract | 2026-10-17 |
| 4 | https://huggingface.co/rapatsky/Hy-Memory-30B-A3B-GGUF | rapatsky/Hy-Memory-30B-A3B-GGUF · Hugging Face | benchmark | web_extract | 2026-10-17 |
| 5 | https://huggingface.co/hermitdave/Hy-Memory-30B-A3B-MLX-8bit | hermitdave/Hy-Memory-30B-A3B-MLX-8bit · Hugging Face | benchmark | web_extract | 2026-10-17 |
| 6 | https://github.com/Tencent-Hunyuan/Hy-Memory | GitHub - Tencent-Hunyuan/Hy-Memory | primary | web_extract | 2026-10-17 |
| 7 | https://explainx.ai/blog/tencent-hy-memory-30b-a3b-open-memory-writer-model-mem0-memos-2026 | Hy-Memory-30B-A3B: Tencent Open Memory Model Beats Opus 5 (explainx.ai) | docs | web_extract | 2026-10-17 |
| 8 | https://huggingface.co/models?other=base_model:quantized:tencent/Hy-Memory-30B-A3B | Quantized Models for tencent/Hy-Memory-30B-A3B -- Hugging Face | docs | web_extract | 2026-10-17 |
| 9 | https://hn.algolia.com/api/v1/search?query=Hy-Memory-30B | HN Search API results for Hy-Memory-30B (0 hits) | community | web_extract | 2026-10-17 |
| 10 | https://memory.hunyuan.tencent.com/ | Hy-Memory 2.0 official site, Tencent Hunyuan | primary | web_extract | 2026-10-17 |

## Notes
Tool family: web_search for discovery and web_extract for every cited page; Firecrawl is dead (402 payment required on every call this month, including both Reddit attempts). Spent 3 searches and 12 fetch attempts, of which 10 pages returned content. NOT FOUND (do not cite): https://www.reddit.com/r/LocalLLaMA/comments/1x7cc2z/tencenthymemory30ba3b_hugging_face/ and its old.reddit mirror, both 402 after two tries each; HN search shows zero stories for the model name as of 2026-10-17. Conflict: the model card's quantization badge says 8 models while the filtered HF quantization listing fetched the same day enumerates 7; trust the enumeration (it lists the repos) and treat the count as moving hourly. The official site (source 10) corroborates 55.49 vs 54.62 vs 44.37 and adds framework-level numbers (LoCoMo 72.6%, memory storage occupancy 6.06%) not used in claims. The GGUF and MLX converters each had to correct an expert-width mismatch in the publisher config (moe_intermediate_size 1536 vs actual 768-wide expert weights) -- an early-days rough edge worth one honest beat.
