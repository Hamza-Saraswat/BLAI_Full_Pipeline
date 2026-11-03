---
slug: 2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th
stage: 03-research
topic: "Nanbeige4.3-33B vs Qwen 3.8: does the 10-day-old 33B really beat Qwen at coding on one consumer GPU?"
depth: standard
generated_at: 2026-11-03T12:46:09Z
sources: 13
hub: "[[videos/2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th]]"
---

# Research brief: Nanbeige4.3-33B vs Qwen 3.8: the 33B coder test

## Summary

Thesis: the new 33B's coding win is the challenger's own scoreboard, and the same table quietly hands Qwen the one benchmark both vendors publish. Most arresting number: Terminal-Bench 2.1 at 80.9 versus 73.0 -- self-reported by Nanbeige, reproduced nowhere else this run. Strongest concrete case: the 66.3 GB BF16 download already compresses to a 20.79 GB Q4_K_M GGUF that fits a 24 GB card, with 99 community quants live. Could not be verified: any independent reproduction of 80.9, any measured tok/s for the quantized 33B on consumer hardware, and Reddit hands-ons (403). Conflict: Qwen3.8-27B's SWE-bench Pro is 61.7 on its own card and on Nanbeige's table, while a 62.5 seen in research belongs to the different Flash-Next model; the brief holds 61.7.

## Thesis

Nanbeige4.3-33B's claimed coding win over Qwen 3.8 is self-reported: it leads 7 of 8 agentic benchmarks on its own card yet loses the one both vendors report, so what decides the download is which model fits your card and how much thinking you can afford.

## Explanation path

Start with the claim itself and where it comes from: a 10-day-old model card comparing itself to Qwen3.8-27B, every number on it produced by the challenger. Before any benchmark is discussed the viewer needs what each model physically is: a dense 33B Llama-family teacher model versus Qwen's 27B dense model whose thinking mode is on by default at its highest effort. Then land the honest catch: on SWE-Bench Pro, the one benchmark both vendors publish, the same table shows Qwen ahead. Only after the claim is framed does the local question open: 66.3 GB of BF16 becomes a 20.79 GB Q4_K_M file that fits a 24 GB card, while Qwen 3.8 4-bit runs in 16-19 GB, and Qwen's default thinking multiplies wall-clock time hard. Close on the only test that settles it: same task, both quants, thinking capped, your own GPU.

## Claims

1. **Nanbeige4.3-33B shipped on Hugging Face on 2026-10-24 as the flagship teacher model for the Nanbeige4.3 distillation series, Apache 2.0, 33B params BF16, with 16,976 downloads last month and 99 community quantizations already.**
   - Source: Nanbeige/Nanbeige4.3-33B model card, https://huggingface.co/Nanbeige/Nanbeige4.3-33B
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "Downloads last month16,976 ... Model size 33B params ... Tensor type BF16" and "Quantizations [99 models]"
2. **The card's own table, with all models at their highest thinking effort and Nanbeige evaluated with preserve_thinking=true, claims Terminal-Bench 2.1 at 80.9 versus Qwen3.8-27B's 73.0, and Terminal-Bench 4.0 (mini-swe-agent v2.4.6) at 23.8 versus 6.3.**
   - Source: Nanbeige/Nanbeige4.3-33B model card, https://huggingface.co/Nanbeige/Nanbeige4.3-33B
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "| Agentic Coding | Terminal-Bench 2.1 | **80.9** | 73.0 | ... |" and "1 Nanbeige4.3-33B is evaluated with `preserve_thinking=true` in the chat template."
3. **On SWE-Bench Pro the same self-reported table flips: Qwen3.8-27B is bolded the winner at 61.7 versus Nanbeige4.3-33B's 60.3, and Qwen's own card independently reports the same 61.7.**
   - Source: Nanbeige/Nanbeige4.3-33B model card, https://huggingface.co/Nanbeige/Nanbeige4.3-33B
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "| SWE-Bench Pro | 60.3 | **61.7** | 51.2 | 36.9 |"
4. **The card's official serving recipes assume four GPUs (vLLM --tensor-parallel-size 4, SGLang --tp-size 4); it publishes no single-GPU recipe.**
   - Source: Nanbeige/Nanbeige4.3-33B model card, https://huggingface.co/Nanbeige/Nanbeige4.3-33B
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "--tensor-parallel-size 4"
5. **Qwen3.8-27B is Alibaba's Apache 2.0 dense 27B vision-language model, in thinking mode by default with reasoning_effort defaulting to xhigh, self-reporting SWE-bench Pro 61.7, Terminal-Bench 2.1 73.0 and LiveCodeBench v6 90.3 on the Claude Code harness at temp=1.0, top_p=0.95, 256K context.**
   - Source: Qwen/Qwen3.8-27B model card, https://huggingface.co/Qwen/Qwen3.8-27B
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "Agentic coding SWE-bench Pro **61.7**" and "xhigh (default): for complex tasks demanding thorough analysis"
6. **Qwen 3.8 is a family, not one model: the official collection holds the 2.4T-A95B MoE and the 27B dense (each with an FP8 variant) plus a Flash-Next preview, and the Nanbeige comparison targets the 27B dense.**
   - Source: Qwen3.8 - a Qwen Collection, https://huggingface.co/collections/Qwen/qwen38
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "Text Generation • 2.4T... Qwen3.8-2.4T-A95B / Image-Text-to-Text • 28B... Qwen3.8-27B / Qwen3.8-27B-FP8"
7. **bartowski's imatrix GGUF ladder spans bf16 66.24GB, Q8_0 35.20GB, Q6_K 29.02GB, Q4_K_M 20.79GB and IQ4_XS 18.64GB, built with llama.cpp release b11845, with the fitting rule of a file 1-2GB smaller than total VRAM.**
   - Source: bartowski/Nanbeige_Nanbeige4.3-33B-GGUF, https://huggingface.co/bartowski/Nanbeige_Nanbeige4.3-33B-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM."
8. **The only fetched consumer-GPU speed number is Qwen3.8-27B at 47.7 tok/s on an RTX 4090 running unsloth's Q4_K_M GGUF at 8K context on llama.cpp 6d05498, in a review that also found Q4_K_M file sizes ranged 16.81 GB to 18.97 GB across four repos.**
   - Source: Best Qwen3.8-27B GGUF: Q2, Q3, Q4, Q5, Q6 and Q8, https://kingy.ai/blog/qwen3-8-27b-best-quantization-gguf/
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "47.7 tok/s at 8K"
9. **Artificial Analysis independently scores Nanbeige4.3-33B at Intelligence Index 20 against a small-open-weights class median of 13, but measured it generating 160M output tokens versus a 78M median, the most verbose of the 8 models in its class, with no speed data published.**
   - Source: Nanbeige4.3-33B - Artificial Analysis, https://artificialanalysis.ai/models/nanbeige4-3-33b
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
   - Quote: "it generated 160M tokens, which is very verbose in comparison to the median of 78M."
10. **An independent reviewer measured Qwen3.8-27B's xhigh default taking 21 minutes and 22,276 reasoning tokens for one SVG that took 137 seconds with reasoning off, running the 17GB Q4_K_M build on a MacBook Pro and a DGX Spark, and called the default not a good way to run the model especially on consumer hardware.**
    - Source: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things, https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults
    - Tier: community | Confidence: high | Accessed: 2026-11-03 | Via: web_extract
    - Quote: "It took **21 minutes** to generate, using 22,276 reasoning tokens to produce 3,223 tokens of output."

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Nanbeige4.3-33B downloads, last month (HF sidebar) | 16,976 | https://huggingface.co/Nanbeige/Nanbeige4.3-33B | "Downloads last month16,976" |
| 2 | Terminal-Bench 2.1, Nanbeige4.3-33B (self-reported) | 80.9 | https://huggingface.co/Nanbeige/Nanbeige4.3-33B | "Terminal-Bench 2.1 \| **80.9** \| 73.0" |
| 3 | Terminal-Bench 2.1, Qwen3.8-27B (self-reported by both cards) | 73.0 | https://huggingface.co/Qwen/Qwen3.8-27B | "Terminal Bench 2.1 (Terminus) 73.0" |
| 4 | SWE-Bench Pro, Nanbeige4.3-33B (self-reported) | 60.3 | https://huggingface.co/Nanbeige/Nanbeige4.3-33B | "SWE-Bench Pro \| 60.3 \| **61.7**" |
| 5 | SWE-Bench Pro, Qwen3.8-27B (self-reported by both cards) | 61.7 | https://huggingface.co/Qwen3.8-27B | "Agentic coding SWE-bench Pro **61.7**" |
| 6 | BF16 safetensors storage, Nanbeige4.3-33B (14 shards) | 66,259,989,086 bytes | https://huggingface.co/api/models/Nanbeige/Nanbeige4.3-33B | "usedStorage":66259989086 |
| 7 | Q4_K_M GGUF file size, Nanbeige4.3-33B (bartowski) | 20.79GB | https://huggingface.co/bartowski/Nanbeige_Nanbeige4.3-33B-GGUF | "Q4_K_M ... 20.79GB" |
| 8 | Qwen3.8-27B 4-bit total memory requirement (unsloth docs) | 16-19GB | https://unsloth.ai/docs/models/qwen3.8 | "work on 16-19GB VRAM like RTX 5080, 4090" |

## Analogy candidates

- **Music file formats**: BF16 weights are the studio master (66.24GB), Q8_0 is FLAC (35.20GB), Q4_K_M is a high-bitrate MP3 (20.79GB); a 24GB card forces the MP3, a 96GB card plays the master. Breaks when: quantization loss is uneven across models and can change what the model can do, not just its fidelity; the card publishes nothing about how much coding skill survives each rung.
- **A stove that ships set to high**: Qwen 3.8 leaves the factory in thinking mode at xhigh, its maximum effort, so every prompt pays maximum reasoning tokens before the answer. Breaks when: effort levels multiply tokens rather than smoothly scaling heat, and the setting must be turned down per request; the model cannot be permanently re-set from the weights.

## Misconceptions

- Myth: The 80.9 versus 73.0 Terminal-Bench win is independently confirmed. Reality: every head-to-head number sits on the challenger's own card, self-reported with preserve_thinking=true; no independent page fetched this run reproduces 80.9.
- Myth: The new 33B beats Qwen 3.8 everywhere. Reality: on SWE-Bench Pro the card's own table has Qwen ahead 61.7 to 60.3, and Qwen's card reports the same 61.7 (claim 3).
- Myth: Qwen 3.8 is one model. Reality: it is a family: a 2.4T-A95B MoE, a 27B dense (each with FP8), and a Flash-Next preview; the Nanbeige comparison is against the 27B dense (claim 6).
- Myth: A 33B model cannot be the target of a one-GPU setup. Reality: the 20.79GB Q4_K_M GGUF fits the 1-2GB-under-VRAM rule for a 24GB card, and the model already has 99 community quantizations.

## Glossary

- **quantization**: storing model weights in fewer bits per number so the file shrinks enough to fit in memory, at some cost in precision.
- **GGUF**: the single-file weight format llama.cpp and its apps load for local inference.
- **Q4_K_M**: a mid-tier 4-bit quantization that keeps the most sensitive tensors at higher precision; the usual quality-per-gigabyte choice.
- **KV cache**: memory holding attention keys and values for earlier tokens; it grows with context length and sits on top of the weight file.
- **thinking mode**: the model generating hidden reasoning tokens before its visible answer, trading time for quality.
- **reasoning_effort**: Qwen 3.8's knob for how much thinking to do, with levels xhigh, medium and low; xhigh is the shipped default.
- **self-reported benchmark**: a score published by the model's own developer rather than an independent evaluator, so harness and settings may favor it.
- **Terminal-Bench**: a benchmark scoring models on finishing real terminal tasks end to end.
- **SWE-Bench Pro**: a benchmark scoring models on resolving real GitHub issues in real repositories.
- **dense model**: a model that reads every parameter for every token, so speed tracks memory bandwidth and the whole file must fit.
- **teacher model**: a large model whose behavior is distilled into smaller, cheaper student models.
- **tok/s**: output tokens per second, the standard measure of local generation speed.

## Unverified

- No independent page fetched this run reproduces the 80.9 Terminal-Bench 2.1 score; its only fetched appearance is Nanbeige's own card.
- Reddit r/LocalLLaMA hands-on threads returned 403; community reception of the model stays unread.
- An estimator site claims 24.5 GB VRAM at Q4_K_M and 58.8 tokens per second on an RTX 5090 for Nanbeige4.3-33B; the page was never fetched.
- A blog claims Nanbeige's KV cache is 3.25 times Qwen3.8-27B's; the page was never fetched.
- First-party tokens-per-second and pass-at-1 for both models on the Spark are expected but not measured; a build-stage measurement can replace this line.
- unsloth's roughly 20 tokens per second generation figure is a vendor claim about B200 GPUs with unclear scope.
- Artificial Analysis per-eval coding scores for Nanbeige4.3-33B render as charts; no number was extractable.
- Qwen3.8's exact release day (August 13 versus 14, 2026) is inferred; only the month is solid.

## Suggested outline

1. Hook: a 10-day-old 33B posts 80.9 against Qwen 3.8's 73.0 on Terminal-Bench, from the maker's own table.
2. Name the source of the numbers: self-reported, preserve_thinking on, all rivals at highest thinking effort.
3. The catch: the same table's SWE-Bench Pro row reads 60.3 to 61.7, Qwen ahead, and Qwen's card agrees.
4. Local reality: 66.3 GB of BF16 becomes a 20.79 GB Q4_K_M that fits a 24 GB card; Qwen 3.8 4-bit runs in 16-19 GB; a 4090 was measured at 47.7 tok/s.
5. The thinking tax: Qwen's xhigh default burned 22,276 reasoning tokens and 21 minutes on one SVG; cap it or it caps you.
6. Do tonight: pull both quants, thinking off, one real repo task each, and let your own terminal settle the table.

## Viewer situation

You've got a 24 GB card (or 16-19 GB free) and you write code with a local model every day; a 10-day-old 33B just claimed the coding crown from the Qwen 3.8 you already run, and you want to know whether to re-download.

## Has process

true
- Pull the Nanbeige4.3-33B Q4_K_M GGUF (20.79GB, bartowski) and the Qwen3.8-27B Q4_K_M you already have.
- Give both the same repo task with thinking capped or off.
- Compare pass or fail and wall-clock time on your own terminal.
- Decide with your result, not the card's table.

## Objection

Both rows of that table are the challenger's own runs; until someone independent reproduces 80.9, the only honest verdict is that nobody has tested the claim.

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/Nanbeige/Nanbeige4.3-33B | Nanbeige/Nanbeige4.3-33B model card | primary | web_extract | 2026-11-03 |
| 2 | https://huggingface.co/api/models/Nanbeige/Nanbeige4.3-33B | HF model API JSON | primary | web_extract | 2026-11-03 |
| 3 | https://huggingface.co/Nanbeige/Nanbeige4.3-33B/raw/main/config.json | config.json | primary | web_extract | 2026-11-03 |
| 4 | https://huggingface.co/Qwen/Qwen3.8-27B | Qwen/Qwen3.8-27B model card | primary | web_extract | 2026-11-03 |
| 5 | https://huggingface.co/Qwen/Qwen3.8-27B/raw/main/README.md | Qwen3.8-27B README (raw) | primary | web_extract | 2026-11-03 |
| 6 | https://huggingface.co/collections/Qwen/qwen38 | Qwen3.8 - a Qwen Collection | primary | web_extract | 2026-11-03 |
| 7 | https://huggingface.co/bartowski/Nanbeige_Nanbeige4.3-33B-GGUF | bartowski/Nanbeige_Nanbeige4.3-33B-GGUF | primary | web_extract | 2026-11-03 |
| 8 | https://huggingface.co/models?other=base_model:quantized:Nanbeige/Nanbeige4.3-33B | Quantized Models for Nanbeige/Nanbeige4.3-33B | primary | web_extract | 2026-11-03 |
| 9 | https://huggingface.co/unsloth/Nanbeige4.3-33B-GGUF | 404 - Hugging Face (negative check) | primary | web_extract | 2026-11-03 |
| 10 | https://unsloth.ai/docs/models/qwen3.8 | Qwen3.8 - How to Run Locally | docs | web_extract | 2026-11-03 |
| 11 | https://kingy.ai/blog/qwen3-8-27b-best-quantization-gguf/ | Best Qwen3.8-27B GGUF | benchmark | web_extract | 2026-11-03 |
| 12 | https://artificialanalysis.ai/models/nanbeige4-3-33b | Nanbeige4.3-33B - Artificial Analysis | benchmark | web_extract | 2026-11-03 |
| 13 | https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults | Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things | community | web_extract | 2026-11-03 |

## Notes

Conflicts: the SWE-bench Pro value 62.5 seen during research belongs to Qwen3.8-Flash-Next's own card (different model); Qwen3.8-27B's number is 61.7 on both the 27B card and Nanbeige's table, so 61.7 is the defensible figure. Terminal-Bench 4.0: Nanbeige's 23.8 versus 6.3 was run with mini-swe-agent v2.4.6; Qwen's own card reports no TB 4.0 at all (the 5.6 on its page is an Artificial Analysis community eval), so the 6.3 has no Qwen-reported counterpart. Negative check: unsloth/Nanbeige4.3-33B-GGUF returns Hugging Face's 404 page as of 2026-11-03; bartowski, AtomicChat and mradermacher fill the gap. Willison's post is community tier and is used for mechanism and measured timing, not for any benchmark score.

## Decisions

- Checkpoint (step 2): confirmed angle "a 10-day-old 33B claims to beat Qwen 3.8 at coding; we test what that means for a local pull" with slug 2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th; no redirect.
- Depth standard, 12 sources fetched across 3 research questions (fan-out via isolated subagents); live downloads counter corrected from the ideas note's 17.8k estimate to 16,976 (HF sidebar, accessed 2026-11-03).
