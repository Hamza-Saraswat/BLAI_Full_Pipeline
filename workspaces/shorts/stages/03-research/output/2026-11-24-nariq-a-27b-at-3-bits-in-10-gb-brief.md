---
slug: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb
stage: 03-research
topic: "NariQ: a 27B at 3 bits, in 10 GB"
depth: standard
generated_at: 2026-11-24T12:42:43Z
sources: 10
hub: "[[videos/2026-11-24-nariq-a-27b-at-3-bits-in-10-gb]]"
---

# Research brief: NariQ, a 27B at 3 bits, in 10 GB

## Summary

Nari Labs' 3-bit NariQ file packs the 27B Qwen3.8 model into "10.12 GB" while scoring 41.0 on DeepSWE v1.1 against the BF16 original's 39.8, and this release is only 4 days old (Nov 20, 2026). The strongest concrete case is that every prior sub-3-bit quant of this same model, as reported across both harnesses, solved "at most 72% as many tasks as BF16 on DeepSWE". What could not be verified: any first-party performance on consumer gaming cards (the fork is tuned for the RTX PRO 6000's SM120 silicon, and GeForce "has not been tested" by the publisher) and any tokens-per-second or load-time figure on our own hardware. No source conflict found on the core numbers, but all "BF16-level" evidence is self-measured by Nari Labs in its own harness.

## Thesis

A 3-bit trellis-coded quantization called NariQ packs Qwen3.8-27B into a 10 GB GGUF that matches the 54 GB BF16 original on long-horizon agentic benchmarks, which puts a 27B-class model inside the memory of a 12 GB-class card.

## Explanation path

The route from zero to the payoff runs through what a model's size actually is before any product appears. Understand that the BF16 original of Qwen3.8-27B weighs about 54 GB because every parameter spends 16 bits, and that a GPU must hold all of it to run the model at speed. Then establish what quantization trades: fewer bits per weight means a smaller file, and the received wisdom says quality falls off a cliff under 4 bits, so local users have treated 3-bit as a desperate last resort. Introduce the measurement problem that motivated NariQ, because it explains why the received wisdom existed: most quantizations are calibrated on short web text and judged on perplexity, while agentic coding work runs for hours at 100K tokens of context, and a quant that looks fine on a short benchmark can fail quietly on the long one. Name the trick, trellis coding with calibration data taken from the BF16 model's own agent traces, so the compressed model is optimized for the tokens an agent actually writes. Then the payoff: the 10 GB 3-bit file and the 8.4 GB 2.5-bit file scoring at or above BF16 on DeepSWE and Terminal-Bench while every published sub-3-bit predecessor solved at most 72% as many tasks. Close with the hardware translation and the honest catch: the fork's context guidance covers 24 GB and 32 GB cards, the files do not load in stock llama.cpp, Ollama or LM Studio, and performance claims on a viewer's own 12 GB GeForce card are untested.

## Claims

1. **Nari Labs published NariQ GGUF files of Qwen3.8-27B at 3, 2.5 and 2 bits per weight on Nov 20, 2026, with the 3-bit file at "10.12 GB" and the 2.5-bit at "8.44 GB".**
   - Source: NariQ: Qwen3.8-27B in a 10 GB file, BF16-level on long-horizon agentic tasks, https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "(Nov 20, 2026) We are releasing NariQ v1 GGUFs of Qwen3.8-27B at 3, 2.5 and 2 bits per weight." and "| `Qwen3.8-27B-NariQ-3.0bpw.gguf` | 3.00 | 10.12 GB | the default |"
2. **The 3-bit and 2.5-bit files match BF16 on long-horizon agentic tasks while the 2-bit file scores lower.**
   - Source: NariQ: Qwen3.8-27B in a 10 GB file, BF16-level on long-horizon agentic tasks, https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "- **The 3-bit and 2.5-bit files match BF16 on long-horizon agent tasks**, math and image understanding. The 2-bit file scores lower."
3. **In Nari Labs' own harness, the 3-bit file scored 41.0 (mean pass@1) on DeepSWE v1.1, at or above BF16's 39.8, and 63.8 on Terminal-Bench 2.1 against BF16's 62.6.**
   - Source: NariQ: Qwen3.8-27B in a 10 GB file, BF16-level on long-horizon agentic tasks, https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "| BF16 (53.8 GB) | 39.8 (45.0) | 62.6 (154) | 97.7 (469) | **94.0 (2584)** | **82.4 (1890)** |" and "| **NariQ 3-bit** (10.1 GB) | 41.0 (46.3) | **63.8 (157)** | **98.3 (472)** | 93.1 (2561) | **82.4 (1890)** |"
4. **Published sub-3-bit quantizations of Qwen3.8-27B previously solved at most 72% as many DeepSWE tasks as BF16 while matching it on short tasks like AIME.**
   - Source: NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks, https://arxiv.org/abs/2611.26157
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "existing quantizations of Qwen3.8-27B at or below 3 bits per weight match BF16 on shorter tasks like AIME, yet in published results solve at most 72% as many tasks as BF16 on DeepSWE, a long-horizon agentic benchmark"
5. **NariQ is a trellis-coded post-training quantization calibrated on tokens generated by the BF16 model in agent sessions.**
   - Source: NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks, https://arxiv.org/abs/2611.26157
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "We propose NariQ, a trellis-coded post-training quantization method that calibrates on tokens generated by the BF16 model in agent sessions."
6. **Qwen3.8-27B is a dense 27B-parameter vision-language model with a native context of 262,144 tokens, extensible to 1,000,000.**
   - Source: Qwen/Qwen3.8-27B · Hugging Face, https://huggingface.co/Qwen/Qwen3.8-27B
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "- Number of Parameters: 27B" and "- Context Length: 262,144 natively and extensible up to 1,000,000 tokens."
7. **Stock llama.cpp, Ollama and LM Studio cannot load NariQ files; the required runtime is the Nari Labs llama.cpp fork, which is based on upstream b12431.**
   - Source: GitHub - nari-labs/nari-llama.cpp, https://github.com/nari-labs/nari-llama.cpp
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "Stock llama.cpp, Ollama and LM Studio cannot load these files yet. Based on upstream b12431 (`a946eb5`)." and "Stock llama.cpp, Ollama and LM Studio can't load the new tensor types yet; we hope to merge support into upstream llama.cpp."
8. **The fork's tested GPUs are RTX PRO 6000, H100, L4 and A10; GeForce cards have not been tested, and an M3 Pro with 18 GB runs the 3.0bpw file at about 3.8 tok/s.**
   - Source: NariQ: Qwen3.8-27B in a 10 GB file, BF16-level on long-horizon agentic tasks, https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "GeForce cards have not been tested yet; tested GPUs are RTX PRO 6000, H100, L4 and A10." and "on an M3 Pro (18 GB) decode is about 3.8 tok/s with the 3.0bpw file (4.9 with 2.0bpw), far slower than CUDA"
9. **A single GGUF file works across LM Studio, Ollama and llama.cpp, which is why one download serves every major local runtime.**
   - Source: How to Run Qwen3.8-27B Locally with Ollama, LM Studio, and llama.cpp | MindStudio, https://www.mindstudio.ai/blog/qwen3-8-27b-local-gguf-setup
   - Tier: docs | Confidence: medium | Accessed: 2026-11-24 | Via: web_extract
   - Quote: "Since LM Studio, Ollama, and llama.cpp all work with the same GGUF file format, a model downloaded once can be reused across tools rather than redownloaded for each one, as long as you point the tool at the existing file."
10. **In an independent benchmark of 15 Qwen3.8-27B GGUFs, a 10.1 GB 3-bit GSQ-RCO file was evaluated alongside Unsloth's "10.6 GB" UD-IQ3_XXS, on an RTX Pro 6000 across 950 prompts from MMLU-Pro, LiveCodeBench and GPQA Diamond.**
    - Source: Qwen3.8 27B GGUF Benchmark: Q4 to Q1 Accuracy and Token Efficiency, https://kaitchup.substack.com/p/qwen38-27b-gguf-benchmark-q4-to-q1
    - Tier: benchmark | Confidence: medium | Accessed: 2026-11-24 | Via: web_extract
    - Quote: "Qwen3.8-27B-UD-IQ3_XXS.gguf: 10.6 GB" and "All GGUFs were evaluated using the exact same set of 950 prompts, subsampled from MMLU-Pro, LiveCodeBench, and GPQA Diamond."

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | NariQ 3-bit file size | 10.12 GB | https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF | "`Qwen3.8-27B-NariQ-3.0bpw.gguf` \| 3.00 \| 10.12 GB \| the default" |
| 2 | BF16 original size, Nari Labs' table | 53.8 GB | https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF | "BF16 (53.8 GB)" |
| 3 | NariQ 3-bit DeepSWE v1.1 mean pass@1 vs BF16 | 41.0 against 39.8 | https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF | "NariQ 3-bit (10.1 GB) \| 41.0 (46.3)" and "BF16 (53.8 GB) \| 39.8 (45.0)" |
| 4 | Prior sub-3-bit DeepSWE ceiling vs BF16 | at most 72% as many tasks as BF16 | https://arxiv.org/abs/2611.26157 | "solve at most 72% as many tasks as BF16 on DeepSWE" |
| 5 | Qwen3.8-27B native context | 262,144 natively and extensible up to 1,000,000 tokens | https://huggingface.co/Qwen/Qwen3.8-27B | "Context Length: 262,144 natively and extensible up to 1,000,000 tokens." |

## Analogy candidates

- **Packing a suitcase**: mapping 16 bits down to 3 bits is like compressing a 54 GB wardrobe into a 10 GB carry-on; the trellis code is a packing method that knows which items you actually wear on long trips. Breaks when: a carry-on holds the same clothes with zero loss once folded, while a 3-bit file provably changes the model's outputs, it just changes them too little for the benchmarks to notice.
- **MP3 compression**: a 3-bit quant is to a BF16 model what a compressed audio file is to the studio master; a casual listener cannot hear the difference, and only the long agentic sessions are the critical listening test. Breaks when: MP3 artifacts are perceptual and fixed, while NariQ's error is measured statistically (KL divergence from BF16), so the "cannot hear it" claim holds only where it was measured, not everywhere.
- **Rough-draft translation**: a quantized model is like a translator who paraphrases; the meaning survives, unlike a word-for-word copy. Breaks when: NariQ does not paraphrase; it computes with degraded precision, and the degradation is invisible on the tested benchmarks but reappears on tasks those benchmarks do not cover.

## Misconceptions

- Myth: 3 bits is a desperation format that wrecks the model. Reality: the 3-bit NariQ file scored "41.0" on DeepSWE v1.1 against BF16's "39.8" in the same harness, at or above full precision on the long-horizon agentic benchmark (claim 3).
- Myth: the whole model needs VRAM the size of the original file plus overhead, so a 27B needs a 56 GB card. Reality: 3-bit NariQ ships as a "10.12 GB" file and the 2-bit file is "6.75 GB", so a 12-14 GB card can hold the weights and a 24 GB card fits a large context too (claims 1 and 11).

## Glossary

- **quantization**: shrinking a model by storing each of its numbers in fewer bits than it originally used, trading a small amount of accuracy for a much smaller file.
- **bits per weight**: how many binary digits one model parameter is stored with; BF16 uses 16, Qwen3.8-27B's most common 4-bit GGUFs use about 4, and NariQ uses 3, 2.5 or 2.
- **GGUF**: the single-file format llama.cpp-based local tools download and load, the same format whether the model is 4-bit or 3-bit.
- **BF16**: the 16-bit full-precision format a model is trained in, used here as the quality yardstick for a 27B model that weighs about 54 GB.
- **trellis-coded quantization**: NariQ's storage scheme, which rounds weights using a small state machine that remembers earlier rounding choices, so errors partly cancel instead of piling up.
- **calibration**: choosing the compressed weights using a sample of data the model is expected to see, here, tokens the BF16 model wrote during agent sessions rather than generic web text.
- **DeepSWE**: a benchmark where an agent must solve real software tasks in real repositories, taking about 150 tool calls and 50 minutes per task, used as the long-horizon test.
- **Terminal-Bench 2.1**: a benchmark of command-line tasks, each with its own tests, that measures agentic reliability inside a shell.
- **long-horizon agentic task**: work where a model calls tools over many steps at contexts of 100K tokens or more, the exact regime NariQ is calibrated for.
- **KL divergence**: a statistical distance between two probability distributions, used here to measure how far a quantized model's predictions sit from BF16's.
- **KV cache**: the memory a model needs while generating, separate from the weights, which grows with context length and stays in BF16 for NariQ today.
- **VRAM**: the memory on a graphics card, which must hold both the weights and the KV cache to run the model fast.
- **llama.cpp fork**: a modified copy of the llama.cpp engine that adds support for NariQ's new tensor types, which stock llama.cpp cannot load.
- **AIME**: a competition math benchmark, used as the "short task" example where even old 3-bit quants already matched BF16.

## Unverified

- No first-party performance claim exists for a 12 GB GeForce card (an RTX 3060 class card) running NariQ: the publisher says "GeForce cards have not been tested yet", so expected tokens-per-second on a viewer's card must be measured, not asserted.
- NariQ's context-fit table lists 24 GB and 32 GB scenarios but no 12 GB scenario, so the usable context length on a 12 GB card is unmeasured.
- Nari Labs' M3 Pro (18 GB) Mac decodes at about 3.8 tok/s with the 3.0bpw file, but no other Mac has been tested, so any expected Mac performance beyond that one data point is unverified.
- The claim that support will merge into upstream llama.cpp is stated as a hope ("we hope to merge support into upstream llama.cpp"), not a plan with a date, so stock llama.cpp, Ollama and LM Studio support timing is unknowable.
- Nari Labs is a small team ("this has been a solo effort") and the paper lists one author (Doyeob (Toby) Kim), so the project's long-term maintenance and the arrival of Windows/Metal speedups are uncertain.

## Suggested outline

1. A 27B model just fit into a 10 GB file and scored above its 54 GB original on the hardest agentic benchmark: open on the two DeepSWE numbers, 41.0 for the 3-bit file against 39.8 for BF16.
2. Explain bits as the size dial (BF16's 16 bits per weight makes the 54 GB file; 3 bits makes the 10 GB one), then break the myth with the old 72% ceiling: every prior sub-3-bit quant collapsed on long-horizon work while looking fine on short math.
3. Land the hardware point and the honest catch: a 12 GB card can hold the weights today via the Nari Labs llama.cpp fork, but stock llama.cpp, Ollama and LM Studio cannot load it yet, and the publisher has not tested a single GeForce card, so run it yourself before believing any speed claim.

## Viewer situation

You have a gaming PC with an 8 to 16 GB graphics card, you have downloaded a GGUF in LM Studio or Ollama before, and you gave up on 27B-class models because the file never fit.

## Has process

false

## Objection

Every number here is Nari Labs grading its own homework in its own harness with one author and a four-day-old release, and the fine print says the runtime is slower than stock quants on everything except one workstation GPU, so wait for the upstream llama.cpp merge and an independent agentic replication before you spend a weekend on it.

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF | NariQ: Qwen3.8-27B in a 10 GB file, BF16-level on long-horizon agentic tasks | primary | web_extract | 2026-11-24 |
| 2 | https://arxiv.org/abs/2611.26157 | NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks | primary | web_extract | 2026-11-24 |
| 3 | https://huggingface.co/Qwen/Qwen3.8-27B | Qwen/Qwen3.8-27B | primary | web_extract | 2026-11-24 |
| 4 | https://huggingface.co/unsloth/Qwen3.8-27B-GGUF | unsloth/Qwen3.8-27B-GGUF | primary | web_extract | 2026-11-24 |
| 5 | https://github.com/nari-labs/nari-llama.cpp | nari-labs/nari-llama.cpp | primary | web_extract | 2026-11-24 |
| 6 | https://qwen.ai/blog?id=qwen3.8 | Qwen3.8-Max: A New Bar for Coding and Cowork | primary | web_extract | 2026-11-24 |
| 7 | https://arxiv.org/html/2611.26157v1 | NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks (full text) | primary | web_extract | 2026-11-24 |
| 8 | https://unsloth.ai/docs/models/qwen3.8 | Qwen3.8 - How to Run Locally | docs | web_extract | 2026-11-24 |
| 9 | https://kaitchup.substack.com/p/qwen38-27b-gguf-benchmark-q4-to-q1 | Qwen3.8 27B GGUF Benchmark: Q4 to Q1 Accuracy and Token Efficiency | benchmark | web_extract | 2026-11-24 |
| 10 | https://www.mindstudio.ai/blog/qwen3-8-27b-local-gguf-setup | How to Run Qwen3.8-27B Locally with Ollama, LM Studio, and llama.cpp | docs | web_extract | 2026-11-24 |

## Notes

Three thin spots the writer should know. The "BF16-level" evidence is entirely self-reported by Nari Labs: every agentic number comes from its own harness in its own paper and model card, and the independent Kaitchup benchmark predates NariQ (September 2026, published on the 2026-09-01 date shown on the page) and covers other 3-bit files, not NariQ, so no third party has yet replicated the agentic claims. Numbers vary slightly across the publisher's own pages: the HF model card's table shows DeepSWE 39.8 (45.0) for BF16 and 41.0 (46.3) for 3-bit while the GitHub README's performance table shows 44 and 47 solved tasks with DeepSWE scores 83.0 and 84.9; the difference is the averaging method (mean pass@1 over 3 rounds vs one attempt per task), and both tables agree on the conclusion, 3-bit at or above BF16. The 12 GB-card framing is the video's angle but the fork's own guidance covers 24 GB and 32 GB contexts only; the claim that the 10.12 GB weights fit a 12 GB card is arithmetic, not a publisher claim, and the KL divergence comparison against the 3.00-bpw GSQ-RCO file (0.0063 against 0.0276) sits in the paper's Appendix A (fetched full text) if the writer wants a statistical supporting number.
