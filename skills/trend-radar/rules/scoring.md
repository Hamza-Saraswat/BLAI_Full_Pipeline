# Scoring

`scripts/scoring.py` implements this file; change both together. Every item ends with a
`score` from 0 to 100:

```
score = 100 * min(1, 0.85 * source_weight * signal * decay + product_bonus)
        + 5 per extra source that carried the same item (capped at 100)
```

## Signal: per-source engagement normalized to 0-1

Counts are log-scaled (`log10(1 + x) / log10(1 + full)`) and capped at 1.0 once `x` reaches
`full`, so a 10,000-upvote post does not flatten everything else.

| Source | Parts (`full` value) | Signal |
|--------|----------------------|--------|
| reddit | upvotes (1,000), comments (300) | 0.7 upvotes + 0.3 comments |
| hn | points (300), comments (150) | 0.7 points + 0.3 comments |
| hf | trendingScore (2,000), likes (1,000), downloads (1,000,000) | 0.5 trending + 0.5 max(likes, downloads) |
| github | release 0.6 (pre-release 0.4), notes +0.1 when the body runs 300+ chars | sum |
| youtube | views per hour (2,000), views (500,000) | 0.6 views/h + 0.4 views |
| firecrawl | flat prior 0.5 (no engagement data) | 0.5 |

The 0.85 factor leaves room for the bonus: an item without a named product tops out at 85,
only a named product can reach 100.

Source weights: reddit 1.0, hn 1.0, github 1.0, hf 0.9, youtube 0.9, firecrawl 0.8. The
weights say how often the source's top item has turned into a Short; revisit them at the weekly
retro, not per run.

## Recency decay

`decay = max(0.05, 0.5 ** (age_hours / 48))`: half the value after 48 h, a quarter after 96 h,
floor 0.05. Items with no date (FireCrawl results) are scored as if they were `hours / 2` old.
GitHub uses a one-week and Hugging Face a two-week fetch window, so a five-day-old release still
shows up, but at a tenth of its fresh value.

## Product extraction

A regex list of known products and vendors (case-insensitive, word-bounded) runs over
`title + summary`. Names are returned in order of first appearance. Each entry has a kind:

| Kind | Entries |
|------|---------|
| hardware | DGX Spark, DGX Station, GB10, Grace Blackwell, Blackwell, RTX 5090/5080/5070/4090/4080/3090/3060, RTX PRO 6000, H100, H200, B200, B300, Jetson, Apple M4, Apple M5, Mac Studio, Mac mini, MacBook, Strix Halo, Ryzen AI, Radeon, Intel Arc, Raspberry Pi |
| model | Qwen, DeepSeek, Llama (not llama.cpp), Mistral, Mixtral, Gemma, GLM, Nemotron, Phi, Kimi, MiniMax, gpt-oss, Grok, Whisper, Kokoro, FLUX, Stable Diffusion, Wan, Hunyuan, SmolLM, Granite, OLMo |
| cloud | ChatGPT, GPT-5, Claude, Gemini, Copilot |
| runtime | llama.cpp, vLLM, Ollama, LM Studio, SGLang, Unsloth, TensorRT, CUDA, MLX, MLC, exo, Open WebUI, ComfyUI, whisper.cpp, ExLlama, LocalAI, Docker Model Runner |
| format | GGUF, NVFP4, MXFP4, FP8, FP4, AWQ, GPTQ |
| vendor | NVIDIA, AMD, Intel, Apple, Meta, Google, Microsoft, OpenAI, Anthropic, Hugging Face, Alibaba, Moonshot, Zhipu, xAI |

`product_bonus` is +0.15 (15 points) when at least one hardware, model, cloud, runtime or format
name is present. A vendor alone earns nothing: "NVIDIA" is not a title, "DGX Spark" is. Titles
that name the product are what the channel's search traffic is made of
(`shared/playbook/titles-descriptions.md`).

Adding a product: one line in `PRODUCTS` in `scoring.py` plus the table above. Patterns need a
word boundary or a digit so that "phi" inside "philosophy" or "wan" inside "want" cannot match.

## Why-now rubric

Every item gets one kind, the first match in this order, so a release note that admits a break
is "Broke", not "Shipped":

| Kind | Evidence in the window |
|------|------------------------|
| Broke | broke, breaks (not "break-even"), bug, regression, crash, fails, not working, security, CVE, revert, pin to, workaround, OOM |
| Shipped | released, launched, announced, out, now available, open weights, "weights on", drops, new model, day-0, Show HN; every GitHub release and every new Hugging Face model (a release whose notes mention a break is "Shipped with a known break") |
| Measured | benchmark, tok/s, throughput, latency, faster, slower, Nx, N%, tested, compared, vs, side by side, results |
| Changed | updated, upgraded, deprecated, price, cheaper, "now supports/runs/works/fine-tunes/fits", adds, enables, firmware, driver, default, policy, regulation, shortage |
| Discussed | none of the above: a thread or article with engagement but no event |

`why_now` is one sentence: the kind, the evidence from the source (counts, release tag, views
per hour, channel) and the age, for example
`Broke: r/LocalLLaMA thread, 640 upvotes, 118 comments, 8 h ago`.

## Lane assignment (workspace shorts)

Keyword rules, checked in this order; the first hit wins. The comparison cue must sit in the
title (a release note that mentions a "side-by-side view" is not a comparison); the other lanes
read `title + summary`:

1. `comparison` when the title carries a versus phrase (vs, versus, compared to, head-to-head,
   side by side, "killer?", "worth it over", instead of, ahead of, beats, outperforms) and at
   least two non-vendor products are named
2. `enterprise-privacy`: privacy, GDPR, HIPAA, compliance, on-prem, air-gapped, enterprise,
   law firm, clinic, hospital, sovereign, EU AI Act, data leak, self-hosted, regulation
3. `how-to`: how to, guide, tutorial, install, set up, getting started, "in N minutes", "the stack"
4. `myth-bust`: myth, actually, "don't need", overrated, "is not free", "not as fast", the truth,
   "still run", wrong, debunk, surprising, "the math", "finally cheaper"
5. `explainer`: an explanatory cue such as explained, what is, why does, "why X matters",
   how does, understanding, deep dive, plain English, "in N seconds". Topic words alone
   (quantization, KV cache, MoE) do not make an explainer; a release that mentions them is news
6. a versus phrase in the title with fewer than two products still lands in `comparison`
7. everything else is `news-react`, the lane for things that shipped, changed or broke

## Series assignment (workspace long-form)

1. `beyond-llms` for any Hugging Face pipeline other than text-generation, or speech, voice,
   transcription, image or video generation keywords
2. `dgx-spark-specific` when DGX Spark is named together with firmware, driver, ConnectX,
   two Sparks, GB10, Spark OS, playbook, NCCL, 200 GbE, CUDA graphs on GB10, sm_121
3. `my-dgx-spark-projects`: fine-tune, LoRA, Unsloth, agent, RAG, "I built", project, home lab
4. `benchmarks`: benchmark, tok/s, throughput, latency, vs, faster, Nx, measured, side by side
5. `inference-engineering-at-home`: quantization, GGUF, AWQ, FP8, FP4, NVFP4, KV cache, batch,
   context window, speculative decoding, flash attention, kernels, CUDA graphs, offload, serving,
   or any runtime name
6. `local-ai-for-dummies`: explained, what is, beginner, basics, intro, why does, how does,
   "cheaper than", "the math"
7. no rule: a named model goes to `benchmarks`, a named runtime or format to
   `inference-engineering-at-home`, the rest to `local-ai-for-dummies`

The group is stored in `signals.group`; the top-level item keys stay exactly
`id, title, url, source, published_at, signals, products, summary, why_now, score`.
