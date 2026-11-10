---
slug: 2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre
stage: 03-research
topic: "M4 Pro vs M5 Pro MacBook for local LLM inference: MoEShift's 374 tok/s prefill with Qwen 3.8 Flash Next on a 24 GB M5 Pro"
depth: standard
generated_at: 2026-11-10T12:40:00Z
sources: 12
hub: "[[videos/2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre]]"
---

# Research brief: M4 Pro vs M5 Pro, 374 tok/s prefill with MoEShift

## Summary
The most arresting number is 374 tok/s: long-prompt prefill on a 24 GB M5 Pro versus 199 tok/s on the same-config M4 Pro, an 88% jump the runtime's author credits to SSD speed rather than the GPU. The strongest concrete case is MoEShift itself: an MIT-licensed Apple Silicon runtime that streams a 125B-parameter MoE from SSD into under 10 GB of RAM, which is the only reason a 24 GB MacBook is in this fight at all. What could not be verified: the 199/374 pair is a single self-reported run (the author's own HN post) with no independent replication, and no page measured the two machines' SSD throughput directly. Sources conflict on emphasis, not facts: Apple markets the M5 Pro's AI jump as Neural Accelerators in each GPU core, while the benchmark author says storage fed the win; the honest video holds both. Generation speed did move too, but only from 9.57 to 13.14 tok/s on the long prompt, so the upgrade story is about the first word, not the typing speed.

## Thesis
On a 24 GB MacBook Pro, the M5 Pro nearly doubles long-prompt prefill speed versus the M4 Pro for streamed MoE models, and prefill speed is what decides whether a big local model feels usable.

## Explanation path
Start with the wait the viewer already knows: paste a long prompt, stare at a blank cursor. Name the two halves of that wait: prefill, where the model reads your whole prompt before answering, and decode, where it writes the answer one token at a time. Establish that prefill is the part you wait on for long prompts, so prefill speed is time-to-first-word. Introduce the model that makes the comparison interesting: Qwen 3.8 Flash Next is 125B parameters total but only 6B active per token, because a router picks a few of 512 experts per token. That is why a 24 GB Mac can even try. Explain MoEShift as the trick that makes it possible: it keeps the experts on the SSD and streams only the ones each token needs into RAM, so the SSD becomes part of the memory system. Now the M4 Pro versus M5 Pro comparison lands as a storage-plus-silicon story rather than a spec-sheet war: memory bandwidth moved only from 273GB/s to 307GB/s, but the author's same-configuration benchmark reports long-prompt prefill jumping from 199 to 374 tok/s while decode sits at single digits. Close on the honest catches: this is the runtime author's own number, warm-run, and generation is still 13 to 15 tok/s, so the win is about the first word on long prompts, not chat speed.

## Claims
1. **MoEShift's author benchmarked Qwen 3.8 Flash Next IQ3 XXS on an M4 Pro and an M5 Pro, both with 24GB unified memory and the same configuration, and reported long-prompt prefill of 199 vs 374 tok/s (+88%) on a 6,060-input-token prompt.**
   - Source: M4 Pro vs. M5 Pro (24GB): Qwen 3.8 Flash Next at 374 Tok/S Prefill with MoEShift - Hacker News, https://news.ycombinator.com/item?id=50432586
   - Tier: community | Confidence: medium | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "Long prompt prefill (6,060 tokens): 199 vs 374 tok/s (+88%)"
2. **Decode on the same run was 9.84 vs 14.69 tok/s (+49%) on a short prompt and 9.57 vs 13.14 tok/s (+37%) on the long prompt, with peak RAM of 8.5GB on both Macs.**
   - Source: Hacker News post, https://news.ycombinator.com/item?id=50432586
   - Tier: community | Confidence: medium | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "9.84 vs 14.69 tok/s (+49%) ... 9.57 vs 13.14 tok/s (+37%) ... 8.5GB on both Macs"
3. **The author attributes the prefill gap to storage, not the GPU.**
   - Source: Hacker News post, https://news.ycombinator.com/item?id=50432586
   - Tier: community | Confidence: medium | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "The major difference is the prefill speed thanks to the higher SSD throughput of the M5 Pro, which directly impacts the expert streaming."
4. **MoEShift is an MIT-licensed local MoE inference runtime for Apple Silicon by Davide Troiani that separates execution memory from storage: routed-expert weights stay in files on the SSD and are fetched on demand, so a 125B-parameter model runs in under 10 GB of peak process memory.**
   - Source: davide-troiani/moeshift, https://github.com/davide-troiani/moeshift
   - Tier: primary | Confidence: high | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "125 billion parameters. Up to 11 tokens per second. Under 10 GB of peak process memory."
5. **The MoEShift benchmark runner's long-prompt measurements are warm-run, not cold-storage.**
   - Source: moeshift/benchmarks/README.md, https://github.com/davide-troiani/moeshift/blob/main/benchmarks/README.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "Prompt caching is disabled, but expert caches and macOS file caches remain active. These are warm-run measurements under your stated conditions, not cold-storage benchmarks."
6. **Qwen3.8-Flash-Next is a MoE model with 125B total parameters, 6B activated per token, 512 experts of which 10 routed plus 1 shared activate per token, and a native context of 262,144 tokens extensible to 1,000,000.**
   - Source: Qwen/Qwen3.8-Flash-Next model card, https://huggingface.co/Qwen/Qwen3.8-Flash-Next
   - Tier: primary | Confidence: high | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "Number of Parameters: 125B with 6B activated, plus 51B n-gram embedding and 4B MTP ... Number of Experts: 512 ... 10 Routed + 1 Shared ... Context Length: 262,144 natively and extensible up to 1,000,000 tokens."
7. **Apple lists the M5 Pro MacBook Pro's memory bandwidth at 307GB/s and the M4 Pro MacBook Pro's at 273GB/s, both with 24GB unified memory standard and 16-core or 20-core GPU options.**
   - Source: MacBook Pro (14-inch, M5 Pro or M5 Max) - Tech Specs, https://support.apple.com/en-us/126318
   - Tier: primary | Confidence: high | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "307GB/s memory bandwidth" / "273GB/s memory bandwidth" (M4 Pro page, https://support.apple.com/en-us/121553)
8. **Prefill is compute-bound and decode is memory-bandwidth-bound.**
   - Source: Prefill vs Decode: LLM Inference Phases Explained, https://redis.io/blog/prefill-vs-decode/
   - Tier: docs | Confidence: high | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "prefill is usually compute-bound, meaning it's limited by how fast the GPU can do math. Decode is usually memory-bandwidth-bound, meaning it's limited by how fast the GPU can move data around."
9. **Apple claims the M5 Pro GPU has a Neural Accelerator in each core and delivers over 4x the peak GPU compute compared to M4 Pro for AI workloads.**
   - Source: Apple debuts M5 Pro and M5 Max - Apple Newsroom, https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/
   - Tier: primary | Confidence: high | Accessed: 2026-11-10 | Via: web_extract
   - Quote: "a next-generation up-to-20-core GPU featuring a Neural Accelerator in each core" ... "M5 Pro delivers over 4x the peak GPU compute compared to M4 Pro"
10. **Community aggregation across 464 runs each on Apple Silicon found GGUF (llama.cpp) averaged 95.5 tok/s versus MLX's 73.7 tok/s, a 30% gap contradicting the assumption that MLX is always faster on Mac.**
    - Source: Benchmark Analysis - Anubis OSS, https://uncsoft.github.io/anubis-oss/analysis.html
    - Tier: benchmark | Confidence: medium | Accessed: 2026-11-10 | Via: web_extract
    - Quote: "GGUF averages 95.5 tok/s versus MLX's 73.7 tok/s, a 30% gap that contradicts the common assumption that native MLX is always the faster path on Apple Silicon."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | M5 Pro long-prompt prefill (6,060 input tokens, Qwen 3.8 Flash Next IQ3 XXS, 24GB) | 374 tok/s | https://news.ycombinator.com/item?id=50432586 | "199 vs 374 tok/s (+88%)" |
| 2 | M4 Pro long-prompt prefill (same setup) | 199 tok/s | https://news.ycombinator.com/item?id=50432586 | "199 vs 374 tok/s (+88%)" |
| 3 | Prefill gap M4 Pro to M5 Pro (author-stated) | +88% | https://news.ycombinator.com/item?id=50432586 | "199 vs 374 tok/s (+88%)" |
| 4 | Long-prompt total inference time (M4 Pro vs M5 Pro) | 83.9 vs 55.1 seconds | https://news.ycombinator.com/item?id=50432586 | "83.9 vs 55.1 seconds" |
| 5 | Decode, long prompt (M4 Pro vs M5 Pro) | 9.57 vs 13.14 tok/s | https://news.ycombinator.com/item?id=50432586 | "9.57 vs 13.14 tok/s (+37%)" |
| 6 | Qwen3.8-Flash-Next parameters | 125B with 6B activated | https://huggingface.co/Qwen/Qwen3.8-Flash-Next | "125B with 6B activated" |
| 7 | Qwen3.8-Flash-Next context window | 262,144 natively and extensible up to 1,000,000 tokens | https://huggingface.co/Qwen/Qwen3.8-Flash-Next | "262,144 natively and extensible up to 1,000,000 tokens" |
| 8 | M5 Pro memory bandwidth | 307GB/s | https://support.apple.com/en-us/126318 | "307GB/s memory bandwidth" |
| 9 | M4 Pro memory bandwidth | 273GB/s | https://support.apple.com/en-us/121553 | "273GB/s memory bandwidth" |

## Analogy candidates
- **Chef with a tiny countertop and a walk-in fridge**: RAM is the countertop holding only the ingredients (experts) in active use; the SSD is the fridge holding the whole 125B pantry; the recipe (router) calls items and the sous-chef (lookahead scheduling) fetches them just before they are needed so the chef (GPU) never idles. Breaks when: fridge trips still cost time, the docs warn overlap "does not eliminate SSD latency or guarantee that every missing-expert read is hidden," and a wrong prediction wastes I/O.
- **Read the whole brief vs write the answer**: prefill is speed-reading the entire document you were handed before you may speak; decode is dictating your answer one word at a time while re-checking every note before each word. Breaks when: a human does not literally re-scan all notes before every word, but every decode step does re-read all weights and the KV cache, which is why decode speed tracks memory bandwidth.

## Misconceptions
- Myth: 374 tok/s means the M5 Pro writes text at 374 tokens per second. Reality: It is prefill only, ingesting a 6,060-token prompt; generation on that run was 13.14 tok/s on the long prompt and 14.69 tok/s on the short one (claims 1 and 2).
- Myth: The M5 Pro wins because its GPU is 88% faster. Reality: The author attributes the prefill delta to higher SSD throughput feeding expert streaming, not compute; Apple's bandwidth spec itself only moved from 273GB/s to 307GB/s (claims 3 and 7).
- Myth: MoEShift is a new model or a re-quantised Qwen. Reality: It is an inference runtime that runs existing GGUFs: "Preparation copies bytes; it does not strip, rewrite or requantize the GGUFs."
- Myth: The 125B model fits in 8.5 GB because of clever compression. Reality: Execution memory and storage are separated: peak process memory was 8.5GB on both Macs, but the setup wants at least 120 GB of fast SSD, with experts streamed on demand (claim 4).
- Myth: MLX is always the fastest runtime on a Mac. Reality: Across 464 community runs each, GGUF averaged 95.5 tok/s versus MLX's 73.7 tok/s; runtime and quant choice matter as much as chip generation (claim 10).

## Glossary
- **prefill (prompt processing)**: The phase that reads your entire input prompt in parallel before the first output token can be produced; it is compute-bound and sets the blank-cursor wait.
- **decode (token generation)**: The phase that generates output tokens one at a time, each step re-reading all weights and the KV cache from memory; it is memory-bandwidth-bound.
- **tok/s**: Tokens per second; meaningless without the phase (prefill or decode), the model, the quantisation and the hardware.
- **MoE (Mixture-of-Experts)**: A model architecture where a router activates only a few specialist weight blocks (experts) per token, so most parameters sit idle for any given token.
- **expert streaming**: Keeping routed-expert weights in files on the SSD and reading only the selected experts into RAM on demand instead of loading the whole model.
- **unified memory**: Apple Silicon design where CPU and GPU share one RAM pool, quoted here as the 24GB configuration on both Macs.
- **IQ3_XXS**: An aggressive low-bit (about 3-bit) quantisation; the tested GGUF is ISTA-DASLab's GSQ-RCO IQ3_XXS release of Qwen 3.8 Flash Next.

## Unverified
- Whether the two test machines were MacBook Pros or Mac minis is not stated; the post says only M5 Pro and M4 Pro, both Macs, both 24GB unified memory.
- The actual SSD throughput of the M4 Pro and M5 Pro in GB/s was not measured in any fetched page; the SSD attribution for the prefill gap is the author's stated explanation.
- The MoEShift version and context size used for the 199 vs 374 run were not stated (the runner recommends a context of at least 8192).
- Independent third-party replication of the 374 tok/s prefill number was not found in this session; the number is the runtime author's self-report on Hacker News.
- An r/LocalLLaMA post with the same benchmark exists but could not be fetched, so its contents beyond the title are unverified.
- US starting prices for the M4 Pro and M5 Pro MacBook Pro configurations appeared only in search snippets and were not fetched, so no price claim is made.

## Suggested outline
1. Open on the blank cursor: you paste a long document into your local model and wait; name the wait as prefill, the step nobody benchmarks.
2. Show the number: same model, same quant, same 24GB config, M4 Pro 199 tok/s prefill versus M5 Pro 374 tok/s on a 6,060-token prompt, an 88% jump the author credits to SSD speed, not the GPU.
3. Explain why a 125B model is even in the room: 6B active parameters per token, a router picking experts, and MoEShift streaming those experts from SSD so peak RAM stays at 8.5GB.
4. Land the honest catch: decode is still 13 to 15 tok/s, so this is a first-word-on-long-prompts upgrade, not a chat-speed upgrade; and the number is the author's own warm-run benchmark.

## Viewer situation
You have a Mac with Apple Silicon and somewhere around 24 GB of RAM, you run open models on it with llama.cpp or LM Studio, and you keep hearing you need the newest chip to do AI locally.

## Has process
false

## Objection
The 374 tok/s figure is one developer's self-reported benchmark of his own alpha-stage runtime, warm-run, on an unfetched-protocol prompt, and prefill speed does nothing for the decode rate that dominates how long the answer takes to finish.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/davide-troiani/moeshift | davide-troiani/moeshift: Memory efficient and high performance MoE inference for Apple Silicon | primary | web_extract | 2026-11-10 |
| 2 | https://github.com/davide-troiani/moeshift/blob/main/docs/architecture.md | moeshift/docs/architecture.md | primary | web_extract | 2026-11-10 |
| 3 | https://github.com/davide-troiani/moeshift/blob/main/benchmarks/README.md | moeshift/benchmarks/README.md | primary | web_extract | 2026-11-10 |
| 4 | https://news.ycombinator.com/item?id=50432586 | M4 Pro vs. M5 Pro (24GB): Qwen 3.8 Flash Next at 374 Tok/S Prefill with MoEShift | community | web_extract | 2026-11-10 |
| 5 | https://huggingface.co/Qwen/Qwen3.8-Flash-Next | Qwen/Qwen3.8-Flash-Next model card | primary | web_extract | 2026-11-10 |
| 6 | https://support.apple.com/en-us/126318 | MacBook Pro (14-inch, M5 Pro or M5 Max) - Tech Specs | primary | web_extract | 2026-11-10 |
| 7 | https://support.apple.com/en-us/121553 | MacBook Pro (14-inch, M4 Pro or M4 Max, 2024) - Tech Specs | primary | web_extract | 2026-11-10 |
| 8 | https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/ | Apple debuts M5 Pro and M5 Max | primary | web_extract | 2026-11-10 |
| 9 | https://redis.io/blog/prefill-vs-decode/ | Prefill vs Decode: LLM Inference Phases Explained | docs | web_extract | 2026-11-10 |
| 10 | https://uncsoft.github.io/anubis-oss/analysis.html | Benchmark Analysis - Anubis OSS | benchmark | web_extract | 2026-11-10 |
| 11 | https://xhinker.medium.com/qwen3-8-flash-next-40-tokens-second-on-an-m4-max-macbook-4-27-bpw-quant-168k-context-a8e594e0bb87 | Qwen3.8-Flash-Next: 40 tokens/second on an M4 Max MacBook | community | web_extract | 2026-11-10 |
| 12 | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | Mastering LLM Techniques: Inference Optimization | primary | web_extract | 2026-11-10 |

## Notes
The headline 199 vs 374 tok/s pair and its decode siblings come from one source: the MoEShift author's own HN post (tier 4). Every framing fact around it (mechanism, warm-run protocol, model card, Apple specs) is tier 1-2 and was fetched this session. The video should attribute the number to the author by name and keep the phase labels (prefill versus decode) attached to every tok/s it speaks; a bare 374 invites the generation misconception. The repo README's own M4 Pro numbers use different protocols (256-output legacy run at 160.8 tok/s prefill; a 417.24 tok/s prefill on Qwen3.6-35B-A3B), so do not mix them into the comparison. Prefill-on-Mac context if needed: Anubis community logs show 36,219 tok/s prefill peaks on M5 Pro with small MoE models, proof that prefill numbers are only comparable within one setup.
