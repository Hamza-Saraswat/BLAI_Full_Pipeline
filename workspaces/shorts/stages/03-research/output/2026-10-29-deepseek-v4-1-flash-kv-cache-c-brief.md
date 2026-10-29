---
slug: 2026-10-29-deepseek-v4-1-flash-kv-cache-c
stage: 03-research
topic: "DeepSeek V4.1 Flash KV cache compression explained for local runners"
depth: standard
generated_at: 2026-10-29T11:42:50Z
sources: 9
hub: "[[videos/2026-10-29-deepseek-v4-1-flash-kv-cache-c]]"
---

# Research brief: DeepSeek V4.1 Flash KV cache compression explained for local runners

## Summary
Thesis: what kills long context on local hardware is the KV cache, and DeepSeek trained that cost
down to 890 bytes per token, a 437-fold drop versus the V1 generation. The most arresting number:
a one-million-token context carries a global KV cache of about 890 MB (the paper states 890 bytes
per token and 1M context; the product is our arithmetic, not theirs). The strongest concrete case
for viewers: ISTA-DASLab already ships V4.1-Flash GGUFs at IQ1_M (1.75 bits per weight) that
"runs on a single GPU with 12 GB of VRAM" -- but only with the Strata engine, system-memory
spillover, and a 110.60 GB Engram file on disk, so total disk need is 231.32 GB. Could not be
verified: whether Ollama's library hosts the model, LM Studio KV controls (no evidence the
--kv-q* flag exists at all), and any first-party tokens-per-second on consumer hardware. Conflict:
none between sources; the two flags you already have (llama.cpp -ctk/-ctv, default f16) are a
separate runtime lever from the model's trained-in compression -- conflating them is the
misconception the video must kill.

## Thesis
DeepSeek V4.1 Flash shrinks the KV cache, the memory bill that grows with every token of context, to 890 bytes per token by building the compression into the trained model itself, not into a runtime flag.

## Explanation path
Start from what the viewer feels: a chat gets long and memory fills, and the culprit is not the
model's weights but the running notes attention keeps on every token already read -- that is the
KV cache, and by default those notes are stored in f16 precision because the llama.cpp flags that
control it (-ctk, -ctv) default to f16. Establish the two levers before naming the model: the
runtime lever everyone already has (quantize K and V to q8_0 or q4_0 in llama.cpp or Ollama) and
the risk on DeepSeek-style sparse attention, where quantized K produced confident gibberish on
every backend until the rotation fix landed (issue 25382). Then bring in the trained-in lever:
the model itself was built to share notes across layers (CSA2), store them as 4-bit FP4, and
re-derive recent ones instead of persisting them (SWA Bounded Replay), which is why 552B backbone
parameters with 8B active per token during prefill can still claim a 1M-token context. Land the
payoff in units the viewer owns: 890 bytes per token means 0.89 MB per thousand tokens, 89 MB per
hundred thousand, roughly 890 MB at the full million (our arithmetic on the paper's per-token
figure). Close on tonight's action: which GGUF quants exist today, the exact flag names, and why
the 12 GB claim carries an asterisk. The mechanism is the spine; the flags are the send-off, not
a step-by-step.

## Claims
1. **The global KV cache footprint lands at 890 bytes per token in HBM, roughly one quarter of DeepSeek-V4-Flash's.**
   - Source: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression, https://arxiv.org/abs/2609.19969
   - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "These designs reduce its global KV cache footprint (always in HBM) to 890 bytes per token, roughly 1/4 of the corresponding footprint of DeepSeek-V4-Flash."
2. **The compression is a stack of trained-in mechanisms, not one trick: cross-layer KV reuse in CSA2 plus FP4 KV caching.**
   - Source: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression, https://arxiv.org/html/2609.19969v1
   - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "To push the limits of KV cache compression, DeepSeek-V4.1-Flash combines cross-layer KV cache reuse in Compressed Sparse Attention 2 (CSA2) with FP4 KV caching."
3. **Versus the V1 generation the per-token global KV cache shrank approximately 437-fold.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "DeepSeek-V4.1-Flash achieves approximately 4-fold and 437-fold reductions in per-token global KV cache size relative to DeepSeek-V4-Flash and DeepSeek-V1, respectively."
4. **The model supports contexts of up to one million tokens while activating 8B parameters per token during prefill and 16B during decode, out of a 552B backbone.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash model card, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens" ... "activates 8B parameters per token during prefill and 16B during decode"
5. **KV cache memory and the bandwidth of moving it, not raw compute alone, are named the primary deployment bottleneck for long-context serving.**
   - Source: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression, https://arxiv.org/abs/2609.19969
   - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "large KV caches continue to strain HBM and SSD capacity and data-transfer bandwidth. Together, these compute, storage, and bandwidth demands constitute the primary bottleneck to further lowering deployment costs."
6. **llama.cpp exposes two flags, -ctk/--cache-type-k and -ctv/--cache-type-v, that set K and V cache precision independently, both defaulting to f16.**
   - Source: llama.cpp tools/cli README, https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/cli/README.md
   - Tier: docs | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "-ctk, --cache-type-k TYPE | KV cache data type for K ... allowed values: f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1 (default: f16)" and same for -ctv
7. **On DeepSeek-V4 architectures, a quantized K cache produced confident gibberish on every backend until the July 2026 rotation fix; the safe pattern during the bug was K at f16, V quantized.**
   - Source: DeepSeek-V4: quantized K-cache (--cache-type-k q8_0) produces garbage on all backends, https://github.com/ggml-org/llama.cpp/issues/25382
   - Tier: docs | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "with a quantized K-cache (--cache-type-k q8_0) produces confident gibberish on every backend (CPU and CUDA verified identically) while the server stays healthy" ... "With --cache-type-k f16 (V may stay q8_0)"
8. **Ollama exposes KV quantization as one env var, OLLAMA_KV_CACHE_TYPE, applied uniformly to keys and values; per-side control like llama.cpp's is only an open feature request.**
   - Source: Support differentiated quantization of the KV cache · Issue #10794, https://github.com/ollama/ollama/issues/10794
   - Tier: docs | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "Ollama only offers a way to set the same quantization method uniformly for keys and values, via OLLAMA_KV_CACHE_TYPE"
9. **Local GGUFs exist today: ISTA-DASLab ships DeepSeek-V4.1-Flash-1017 at IQ1_M (1.75 bits per weight), IQ2_XXS (2.00) and IQ2_XS (2.25), and the 12 GB GPU claim requires the Strata engine with the rest in system memory.**
   - Source: ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF model card, https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
   - Quote: "IQ1_M (1.75 bits per weight), IQ2_XXS (2.00) and IQ2_XS (2.25)" ... "every build runs on a 12 GB GPU, with the rest of the model held in system memory" (with Strata)
10. **llama.cpp has supported DeepSeek-V4.1, including images, since release b11870 (October 25, 2026).**
    - Source: ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF model card, https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF
    - Tier: primary | Confidence: high | Accessed: 2026-10-29 | Via: web_extract
    - Quote: "llama.cpp supports DeepSeek-V4.1, including images, since release b11870 (October 25, 2026), and the files here use its layout since October 27, 2026"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | global KV cache per token (HBM) | 890 bytes per token | https://arxiv.org/abs/2609.19969 | "reduce its global KV cache footprint (always in HBM) to 890 bytes per token" |
| 2 | global KV reduction vs DeepSeek-V4-Flash | roughly 1/4 | https://arxiv.org/abs/2609.19969 | "roughly 1/4 of the corresponding footprint of DeepSeek-V4-Flash" |
| 3 | global KV reduction vs DeepSeek-V4-Flash and V1 | approximately 4-fold and 437-fold | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "approximately 4-fold and 437-fold reductions in per-token global KV cache size" |
| 4 | persistent (SSD/host RAM) KV reduction vs V4-Flash | roughly 1/8 | https://arxiv.org/abs/2609.19969 | "persistent KV cache footprint (always on SSD or in host memory) to roughly 1/8 of that of DeepSeek-V4-Flash" |
| 5 | max context length | contexts of up to one million tokens | https://arxiv.org/abs/2609.19969 | "support for contexts of up to one million tokens" |
| 6 | active parameters per token | 8B parameters per token during prefill and 16B during decode | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "activates 8B parameters per token during prefill and 16B during decode" |
| 7 | smallest local quant | IQ1_M (1.75 bits per weight) | https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF | "IQ1_M (1.75 bits per weight), IQ2_XXS (2.00) and IQ2_XS (2.25)" |
| 8 | total download size, IQ1_M build | 231.32 GB | https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF | "120.72 GB / 110.60 GB / 231.32 GB" (backbone / Engram / total) |
| 9 | rotation fix decode cost | ~6.8% decode throughput (q8/q8, single card) | https://github.com/ggml-org/llama.cpp/issues/25382 | "Measured rotation cost: ~6.8% decode throughput (q8/q8, single card)" |

## Analogy candidates
- **Running notes, not the notebook**: the model's weights are a printed reference book (fixed cost, paid once when it loads); the KV cache is the pad of sticky notes that grows one note per token read -- V4.1-Flash writes each note on a quarter of the paper (FP4) and lets whole floors of the building read the same pad (CSA2). Breaks when: the pad never shrinks on its own -- compression makes each note smaller, it does not throw notes away, and layers sharing one pad only works because they were trained that way.
- **Fuel tanker vs saddlebag**: weights are the engine; the KV cache is the tanker trailing the car, one barrel added per token -- this model swapped the tanker for a saddlebag of 890 bytes per token. Breaks when: fuel burns as you drive, so the tanker lightens; a KV cache only grows with context and every new token must re-read what is already there.
- **Shorthand vs longhand**: an f16 KV cache writes every note in longhand; q8_0 or q4_0 writes shorthand, half or a quarter the paper for the same conversation. Breaks when: shorthand risks a misread word -- on DeepSeek-V4 the misread was total gibberish (llama.cpp issue 25382) -- and the model's own FP4 works only because it was trained to live with it.

## Misconceptions
- Myth: "KV cache compression here just means 4-bit quantization." Reality: FP4 alone nearly halves main KV storage versus V4's FP8; the bigger factors are architectural -- cross-layer KV reuse (CSA2) and 2:1 encoder compression -- with SWA Bounded Replay cutting the persistent cache separately (claim 2).
- Myth: "I can get V4.1-Flash's 890 bytes per token by setting a flag on any model." Reality: the number is trained-in from scratch (sparse attention at 64K sequence length, FP4 via quantization-aware training); the runtime flags -ctk/-ctv are a separate, smaller lever on top (claims 1, 2, 6).
- Myth: "Quantizing the KV cache is a universally safe win on every model." Reality: on DeepSeek-V4 architectures a quantized K cache produced confident gibberish on every backend until the July 2026 fix; the model's own FP4 cache survives because it was trained into the weights (claims 2, 7).
- Myth: "The 1.75-bpw GGUF runs on any 12 GB gaming GPU in llama.cpp." Reality: the 12 GB claim requires the Strata engine with the rest of the model in system memory and a 110.60 GB Engram file on disk; the IQ1_M total is 231.32 GB (claim 9).

## Glossary
- **KV cache**: the running notes the model keeps on every token it has already read so it does not recompute them; it grows with context and is what eats your memory on long chats.
- **FP4 (E2M1)**: a 4-bit number format with one E4M3 scale per 16 channels; a quarter of the bytes of 16-bit storage.
- **CSA2**: Compressed Sparse Attention 2, V4.1-Flash's attention scheme where layers share one compressed KV store (Full, Reindex or Reuse modes) and each query attends to its top 512 chosen entries.
- **SWA Bounded Replay**: rebuilding missing sliding-window KV by re-processing only the most recent 128 tokens instead of the whole prefix, trading a little recomputation for never storing those states.
- **GGUF**: the single-file model format llama.cpp-based tools (Ollama, LM Studio) load and the format quantized weights ship in.
- **bpw (bits per weight)**: average precision across all tensors in a quantized file; lower bpw means a smaller file and more quality risk.
- **q8_0 / q4_0**: llama.cpp KV-cache quantization types (8-bit and 4-bit block quantization) accepted by -ctk and -ctv.
- **OLLAMA_KV_CACHE_TYPE**: Ollama's server-wide environment variable setting one KV quantization type applied uniformly to keys and values.

## Unverified
- No fetched page states Ollama's library hosts DeepSeek V4.1 Flash or an official Ollama model page for it.
- No evidence from any fetched page or search result that an LM Studio --kv-q* flag exists; the flag name appears not to exist.
- The NVIDIA NVFP4 quantization card for this model was seen only as a search snippet, not a fetched page.
- Any tokens-per-second, load time or memory figure for V4.1 Flash on consumer hardware: needs a first-party measurement on the Spark before it can be stated.
- The third-party paper alleging periodic long-context retrieval failures in V4/V4.1 (Reddit r/DeepSeek thread): the fetch failed, so it is a lead, not a fact.

## Suggested outline
1. Cold open on the feeling: the chat grows, memory fills, the model slows -- name the culprit as the notes the model keeps per token, not the model.
2. The bill today: what a KV cache is, that llama.cpp stores it f16 by default, and the runtime lever (-ctk/-ctv q8_0) with its DeepSeek-shaped scar tissue (gibberish bug, K-stays-f16 workaround).
3. The trained-in answer: V4.1-Flash shares notes across layers (CSA2), writes them FP4, skips persisting recent ones; 890 bytes per token, 437-fold under V1, 1M-token context, 552B backbone with 8B active in prefill.
4. The catch: weights are still huge -- smallest GGUF today is IQ1_M at 1.75 bpw, 231.32 GB on disk; the 12 GB GPU line needs Strata plus system memory.
5. Send-off: two separate levers -- pick your runtime cache type knowingly, and know the model you pull already has the big compression built in.

## Viewer situation
You run open models at home through Ollama or LM Studio on a gaming PC or a Mac, you have watched a long chat eat your memory, and you have seen the cache-type flags mentioned without anyone explaining what they actually touch.

## Has process
false

## Objection
"890 bytes per token is a lab number from DeepSeek's own paper on their own serving setup, and the 12 GB claim needs a specific engine plus 231 GB on disk -- so nothing here changes what runs on my 24 GB card tonight."

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://arxiv.org/abs/2609.19969 | DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression | primary | web_extract | 2026-10-29 |
| 2 | https://arxiv.org/html/2609.19969v1 | DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression (full text) | primary | web_extract | 2026-10-29 |
| 3 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash model card | primary | web_extract | 2026-10-29 |
| 4 | https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF | ISTA-DASLab DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF model card | primary | web_extract | 2026-10-29 |
| 5 | https://github.com/ggml-org/llama.cpp/issues/25382 | DeepSeek-V4: quantized K-cache produces garbage on all backends | docs | web_extract | 2026-10-29 |
| 6 | https://github.com/ollama/ollama/issues/10794 | Support differentiated quantization of the KV cache | docs | web_extract | 2026-10-29 |
| 7 | https://docs.vllm.ai/en/stable/configuration/optimization/ | vLLM Optimization and Tuning docs | docs | web_extract | 2026-10-29 |
| 8 | https://github.com/ggml-org/llama.cpp/blob/master/README.md | llama.cpp README | docs | web_extract | 2026-10-29 |
| 9 | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/cli/README.md | llama.cpp tools/cli README (parameter reference) | docs | web_extract | 2026-10-29 |

## Notes
Sources do not conflict. One framing caution for the writer: the 890 MB-at-1M-context figure is
arithmetic (890 bytes x 1M), not a number the paper states; if spoken, attribute it as our
multiplication. The paper also says FP4 retention is "only marginal performance degradation" with
no numeric ablation in the fetched text -- keep it qualitative or leave it out. vLLM docs were
fetched to confirm KV cache is the resource that runs out first (preemption behavior) but carry no
claim here; they are spillover for the writer, not a load-bearing source. No source fetched this
run quantifies consumer-GPU or Mac memory limits, so the script must not name a specific card's
VRAM as a sourced number.

## Decisions
- 2026-10-29T11:47:00Z - 2026-10-29 research checkpoint (unattended): angle and slug confirmed as picked (KV-cache mechanism angle, not GPU-fit angle; the published 2026-10-19 Short covered fit). 9 sources fetched (4 primary, 5 docs); validator exit 0; 10 claims, 9 key numbers. FireCrawl 402 (no credits) so all fetches ran via web search/extract fallback. No source conflicts; LM Studio KV flags do not exist (kept under unverified) and Ollama library availability unconfirmed, so the script stays on llama.cpp -ctk/-ctv as the only grounded runtime lever.
