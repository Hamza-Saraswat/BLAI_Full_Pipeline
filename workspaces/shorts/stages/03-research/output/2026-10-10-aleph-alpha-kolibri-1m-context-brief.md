---
slug: 2026-10-10-aleph-alpha-kolibri-1m-context
stage: 03-research
topic: "Aleph Alpha Kolibri: open weights with a 1M-token context window"
depth: standard
generated_at: 2026-10-10T11:42:02Z
sources: 8
hub: "[[videos/2026-10-10-aleph-alpha-kolibri-1m-context]]"
---

# Research brief: Aleph Alpha Kolibri, open weights with a 1M-token context window

## Summary
Aleph Alpha, the German enterprise and public-sector AI company, shipped Kolibri on the 3rd of October 2026: open weights under the Apache 2.0 license, 78B total parameters with only 3.46B active per token, and a context window the vendor says it validated up to 1,048,576 tokens. The most arresting number is on the same model card: for serving efficiency and complex tasks, Aleph Alpha itself recommends staying at 262,144 tokens or below on a model whose headline is one million. The strongest concrete case for our viewer is the community route: an independent Q4_K_M GGUF at 47.5 GB that a measured llama.cpp setup ran at 18.0 ± 0.3 tok/s generation with a 12 GB RTX 5070 and 128 GB of system RAM. Could not be verified: any performance inside Ollama, LM Studio or MLX beyond community posts, quantized quality versus the FP8 original, and every tokens-per-second figure on our own hardware. No material conflicts found: press numbers match the model card; the caveat is that every benchmark score is vendor-reported.

## Thesis
Kolibri proves a million-token context window now ships in an open-weight model you can run yourself, provided you respect the gap between 3.46B active parameters and the 78B that must sit in memory.

## Explanation path
Start with what actually landed: a German company whose business is sovereign AI for regulated sectors gave away the weights, Apache 2.0, no strings on the weights themselves. Then explain the two numbers everyone will quote wrong: 78B total is the memory bill because every expert must sit in memory, while 3.46B active per token is the compute bill, the reason it can be fast on modest silicon. Only once that distinction lands does the 1M-token claim make sense: the model was trained to 262,144 tokens natively, and because positional encoding lives only in the sliding-window layers, context stretches past that without position scaling or retraining, which the vendor validated to 1,048,576 tokens on RULER-style long-context evaluation. Pair that immediately with the vendor's own asterisk, that real deployments should stay at 262,144 tokens or below for complex work. Then get concrete about tonight: the official path is vLLM through the aleph-alpha-inference plugin with a ~78 GB FP8 footprint, while the community path is a 47.5 GB Q4_K_M GGUF on a patched llama.cpp build, with Ollama and LM Studio explicitly not loading it yet. Close on why a enterprise house did this: on-premise deployment for German and English work under European law, and benchmarks the vendor says match models with four times the active parameters. The payoff for the viewer: check your RAM before you trust the headline.

## Claims
1. **Aleph Alpha released Kolibri (Kolibri-1) on the 3rd of October 2026 and published the weights on Hugging Face under the Apache 2.0 license.**
   - Source: Aleph-Alpha/Kolibri-1 model card, https://huggingface.co/Aleph-Alpha/Kolibri-1
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Release Date | 3rd of October 2026 ... License | Apache 2.0 ... The model weights are published by Aleph Alpha GmbH under Apache 2.0 license."
2. **Kolibri is a Mixture-of-Experts model with 78B total parameters (`78,103,074,560`) and 3.46B active parameters per token (`3,457,573,120`).**
   - Source: Aleph-Alpha/Kolibri-1 model card, https://huggingface.co/Aleph-Alpha/Kolibri-1
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Total parameters | 78B (`78,103,074,560`) ... Active parameters / token | 3.46B (`3,457,573,120`)"
3. **The model card lists a context length of 1,048,576 tokens and recommends ≤262,144 tokens for serving efficiency and complex tasks.**
   - Source: Aleph-Alpha/Kolibri-1 model card, https://huggingface.co/Aleph-Alpha/Kolibri-1
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Context length | `1,048,576 tokens`; we recommend ≤262,144 tokens for serving efficiency and complex tasks"
4. **Kolibri was trained on 262,144 tokens in its final long-context phase (its native length), and because positional encoding is applied only in the sliding-window layers, context extends beyond that without any position scaling; Aleph Alpha validated quality and serving efficiency up to 1,048,576 tokens.**
   - Source: Aleph-Alpha/Kolibri-1 model card, https://huggingface.co/Aleph-Alpha/Kolibri-1
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Because positional encoding is applied only in the sliding-window layers, the context can be extended beyond that length without any position scaling, in principle to arbitrary lengths. We have validated quality and serving efficiency up to 1,048,576 tokens."
5. **The attention pattern is a 512-token sliding window plus full attention every 5th layer, in a 50-layer all-MoE model with 384 experts of which 6 are routed-active plus 1 shared expert.**
   - Source: Kolibri Has Landed: A Sovereign Open-Weight Model (Aleph Alpha blog), https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Layers | 50 (all MoE, 1 shared expert) ... Experts (total / active) | 384 / 6 ... Attention pattern | sliding window (512) + full attention every 5th layer"
6. **Official deployment is vLLM through the aleph-alpha-inference package (the Kolibri vLLM plugin), and the model card lists a memory footprint of ~78 GB (FP8 weights) with a minimum of 2× A100 80 GB, 2× H100 SXM5, 1× H200, 1× B200 or 1× B300.**
   - Source: Aleph-Alpha/Kolibri-1 model card, https://huggingface.co/Aleph-Alpha/Kolibri-1
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Kolibri requires the **aleph-alpha-inference** package that provides the Kolibri vLLM plugin ... Hardware requirements | Model memory footprint: ~78 GB (FP8 weights). Minimum: 2× A100 80 GB, 2× H100 SXM5, 1× H200, 1× B200 or 1× B300."
7. **Stock llama.cpp does not support the kolibri1 architecture yet: the independent Q4_K_M GGUF (47.5 GB) requires applying a patch to llama.cpp at upstream commit 836d571, and Ollama, LM Studio and other llama.cpp-based apps will not load the file until they include support.**
   - Source: Hob-forge/Kolibri-1-GGUF model card, https://huggingface.co/Hob-forge/Kolibri-1-GGUF
   - Tier: primary | Confidence: medium | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Stock llama.cpp does not support the `kolibri1` architecture yet. Apply `kolibri1-llama.cpp.patch` (included in this repo) to llama.cpp at upstream commit `836d571` ... Ollama, LM Studio and other llama.cpp-based apps will not load this file until they include support for the architecture."
8. **A measured llama-bench run (2026-10-07, AMD Ryzen 7 7800X3D, 128 GB DDR5-6400, RTX 5070 12 GB) generated at 18.0 ± 0.3 tok/s with attention and the shared expert on the GPU and all routed experts in RAM, with Q4_K_M using 46.6 GB of system RAM.**
   - Source: Hob-forge/Kolibri-1-GGUF model card, https://huggingface.co/Hob-forge/Kolibri-1-GGUF
   - Tier: benchmark | Confidence: medium | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "GPU for attention + shared expert, all routed experts in RAM (`-ngl 99 --cpu-moe`, KV q8_0) | 723 ± 18 tok/s | 18.0 ± 0.3 tok/s ... Machine: AMD Ryzen 7 7800X3D, 128 GB DDR5-6400 (2 × 64 GB), RTX 5070 12 GB ... Memory (CPU, weights loaded without mmap): Q4_K_M uses 46.6 GB RAM"
9. **Aleph Alpha reports AIME 2025 at 96.9 (versus 84.6 for Qwen3.6 35B-A3B and 91.7 for Nemotron 3 Super 120B-A12B in its comparison table) and says Kolibri matches models with up to four times its active parameter count.**
   - Source: Kolibri Has Landed: A Sovereign Open-Weight Model (Aleph Alpha blog), https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/
   - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
   - Quote: "Across math, coding, grounding, and long-context tasks, Kolibri matches models with up to four times its active parameter count, such as Nemotron 3 Super. ... | AIME 2025 | 96.9 | 81.9 | 84.6 | 91.7 | 79.8 |"
10. **Aleph Alpha positions Kolibri as sovereign AI: built in Germany, trained on infrastructure in Germany and Finland, under European and German law, with no foreign control, for on-premise deployment without sending internal data to third-party inference services.**
    - Source: Kolibri Has Landed: A Sovereign Open-Weight Model (Aleph Alpha blog), https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/
    - Tier: primary | Confidence: high | Accessed: 2026-10-10 | Via: web_extract
    - Quote: "Our teams built the model in Germany, trained it on infrastructure in Germany and Finland, under European and German law, with no foreign **control**."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total parameters | 78B (`78,103,074,560`) | https://huggingface.co/Aleph-Alpha/Kolibri-1 | "Total parameters | 78B (`78,103,074,560`)" |
| 2 | active parameters per token | 3.46B (`3,457,573,120`) | https://huggingface.co/Aleph-Alpha/Kolibri-1 | "Active parameters / token | 3.46B (`3,457,573,120`)" |
| 3 | maximum validated context length | 1,048,576 tokens | https://huggingface.co/Aleph-Alpha/Kolibri-1 | "Context length | `1,048,576 tokens`" |
| 4 | vendor-recommended context for serving efficiency and complex tasks | ≤262,144 tokens | https://huggingface.co/Aleph-Alpha/Kolibri-1 | "we recommend ≤262,144 tokens for serving efficiency and complex tasks" |
| 5 | model memory footprint (FP8 weights) | ~78 GB | https://huggingface.co/Aleph-Alpha/Kolibri-1 | "Model memory footprint: ~78 GB (FP8 weights)" |
| 6 | Q4_K_M community GGUF file size | 47.5 GB | https://huggingface.co/Hob-forge/Kolibri-1-GGUF | "`Kolibri-1-Q4_K_M.gguf` | Q4_K_M | 47.5 GB" |
| 7 | measured generation speed, Q4_K_M, 12 GB GPU + experts in RAM | 18.0 ± 0.3 tok/s | https://huggingface.co/Hob-forge/Kolibri-1-GGUF | "GPU for attention + shared expert, all routed experts in RAM ... 18.0 ± 0.3 tok/s" |

## Analogy candidates
- **Vehicle**: a hospital with 384 specialist doctors on staff where every case is routed to 6 specialists plus 1 generalist. Mapping: the payroll (78B parameters) must all be in the building and paid for (memory), even though only 7 touch your case (3.46B active, speed). Breaks when: doctors can be sent home between cases, but expert weights sit in memory for every single token, so the memory bill never takes a shift off.
- **Vehicle**: reading a 800-page contract with a magnifying glass that only shows the last page, plus a notary who has read the whole file and is summoned every fifth chapter. Mapping: sliding-window layers (512 tokens) carry local flow cheaply while the full-attention layers every 5th layer carry the long-range story, which is why context can stretch past the trained length. Breaks when: the notary layers still pay full cost as the document grows, so a million tokens is cheap, not free.

## Misconceptions
- Myth: A 1M-token context window means full quality across one million tokens. Reality: the model card itself recommends ≤262,144 tokens for serving efficiency and complex tasks; 262,144 is the trained native length and 1,048,576 is the validated maximum (claim 3, claim 4).
- Myth: Open weights under Apache 2.0 mean you can run it anywhere tonight, in Ollama or LM Studio. Reality: the official path is vLLM via the aleph-alpha-inference plugin, stock llama.cpp does not support the kolibri1 architecture yet, and Ollama, LM Studio and other llama.cpp-based apps will not load the community GGUFs until they ship support (claim 6, claim 7).

## Glossary
- **open weights**: the downloadable model files are yours to use under the stated license, here Apache 2.0; the training data and pipeline stay closed.
- **Mixture-of Experts (MoE)**: a model built from many specialist sub-networks (experts) where a router picks a few per token instead of running everything.
- **active parameters**: the fraction of the model that actually computes for each token (3.46B of Kolibri's 78B); it sets speed, not memory.
- **context window**: how much text the model can consider at once, measured in tokens, roughly three-quarters of a word in English.
- **sliding-window attention**: attention layers that only look at a fixed stretch of recent tokens (512 here) instead of the whole context, keeping their memory cost flat.
- **FP8**: an 8-bit number format for weights; Kolibri's official checkpoint ships in FP8, about ~78 GB.
- **quantization (Q4_K_M)**: squeezing weights into fewer bits to shrink the download; Q4_K_M is a 4-bit llama.cpp format, here 47.5 GB.
- **KV cache**: the memory the model fills with what it has already read; it grows with context length and is the hidden cost of long inputs.

## Unverified
- Tokens per second, load time and memory use on the DGX Spark or any of our own hardware; nothing has been measured by us yet.
- Whether and when stock llama.cpp, Ollama or LM Studio merge support for the kolibri1 architecture; only an independent patch exists as of 2026-10-10.
- MLX performance figures for Apple Silicon, including the community-reported 84 tok/s across 4 sessions on an M2 Max, which appears only in community discussion.
- Quality of the quantized GGUF and MLX builds versus the original FP8 checkpoint; the converter states no benchmark suite was run.
- All benchmark scores are Aleph Alpha's own reported evaluations; no independent leaderboard confirmation was fetched.

## Suggested outline
1. German enterprise AI shop Aleph Alpha drops Kolibri on October 3: open weights, Apache 2.0, 78B total but 3.46B active per token, and a headline 1,048,576-token context.
2. The trick that makes it work and the asterisk that comes with it: positional encoding only in the sliding-window layers lets context stretch past the trained 262,144 without retraining, but the vendor itself says stay at ≤262,144 tokens for real work.
3. What fits tonight: ~78 GB FP8 on official vLLM for datacenter GPUs, or the 47.5 GB Q4_K_M GGUF on patched llama.cpp at a measured 18.0 ± 0.3 tok/s with a 12 GB GPU and 128 GB of RAM, while Ollama and LM Studio cannot load it yet.

## Viewer situation
You've got a gaming PC or a Mac with 32 to 128 GB of memory, a week of headlines telling you million-token context is here, and no idea whether this German model actually fits on your machine tonight.

## Has process
true
- Download the FP8 weights from the Aleph-Alpha/Kolibri-1 repository on Hugging Face.
- Install the official runtime with pip install 'aleph-alpha-inference>=1', which brings the supported vLLM version and the Kolibri plugin.
- Serve the model with vllm serve Aleph-Alpha/Kolibri-1 --kv-cache-dtype fp8 --reasoning-parser kolibri1 --tool-call-parser kolibri1 --enable-auto-tool-choice.
- Add --max-model-len 1048576 --hf-overrides '{"max_position_embeddings": 1048576}' only when you need contexts beyond 262,144 tokens.
- Skip the datacenter route on one PC: download the Q4_K_M GGUF (47.5 GB) from the Hob-forge/Kolibri-1-GGUF repository on Hugging Face.
- Build llama.cpp at commit 836d571 with the kolibri1 patch applied (or download the prebuilt hob-b11434 release), then run llama-server -m Kolibri-1-Q4_K_M.gguf -c 32768 --jinja.
- Expect Ollama and LM Studio to fail until they ship kolibri1 support, so check before you download.

## Objection
A 78B-parameter model that needs ~78 GB of FP8 weights, a vLLM plugin or a patched llama.cpp, and carries the vendor's own advice to stay at 262,144 tokens is a datacenter release with an asterisk, not a tonight project for a 24 GB gaming PC.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/Aleph-Alpha/Kolibri-1 | Aleph-Alpha/Kolibri-1 model card (Hugging Face) | primary | web_extract | 2026-10-10 |
| 2 | https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/ | Kolibri Has Landed: A Sovereign Open-Weight Model (Aleph Alpha blog) | primary | web_extract | 2026-10-10 |
| 3 | https://aleph-alpha.com/downloads/tech-report.pdf | Kolibri: A Sovereign European Model on the Pareto Frontier (tech report) | primary | web_extract | 2026-10-10 |
| 4 | https://huggingface.co/Hob-forge/Kolibri-1-GGUF | Hob-forge/Kolibri-1-GGUF model card (Hugging Face) | primary | web_extract | 2026-10-10 |
| 5 | https://huggingface.co/Aleph-Alpha/Kolibri-1/discussions/1 | Request: Quantized versions (MLX / GGUF) for Apple Silicon (HF discussion) | community | web_extract | 2026-10-10 |
| 6 | https://news.ycombinator.com/item?id=49942706 | Kolibri: A Sovereign Open-Weight Model (Hacker News thread) | community | web_extract | 2026-10-10 |
| 7 | https://www.testingcatalog.com/aleph-alpha-releases-open-weight-kolibri-with-1m-context/ | Aleph Alpha releases open-weight Kolibri with 1M context (TestingCatalog) | docs | web_extract | 2026-10-10 |
| 8 | https://www.marktechpost.com/2026/10/04/aleph-alpha-releases-kolibri-a-78-1b-open-weight-english-german-moe-model-with-only-3-46b-active-parameters/ | Aleph Alpha Releases Kolibri: A 78.1B Open-Weight English-German MoE Model (MarkTechPost) | docs | web_extract | 2026-10-10 |

## Notes
Hob-forge/Kolibri-1-GGUF is an independent community conversion, explicitly "not made or endorsed by Aleph Alpha or the llama.cpp project"; its speed figures come with methodology (llama-bench, dated, hardware listed) so they are cited as benchmark tier, but its file sizes and runtime-support statements are the converter's own. Aleph Alpha answered the quant request in the HF discussion by pointing to community quants, confirming no official quants exist yet. The tech report corroborates the model card (78.1B total, 3.46B active, Apache 2.0, 24T training tokens) and describes the hybrid-attention ablations; it is listed in Sources as supporting reading. MarkTechPost's "only 10 layers grow with context" is consistent with the blog's "full attention every 5th layer" across 50 layers. Reddit threads were unreachable (403), so reception leans on the HN thread, where team members confirmed FP8 is the default checkpoint and a BF16 repo exists (Kolibri-1-BF16). FireCrawl was unavailable (402) all session; all fetches went through web_search plus web_extract.
