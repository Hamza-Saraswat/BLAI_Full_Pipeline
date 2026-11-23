# 09 -- Software Architecture Weekly, "Can Local LLMs replace Claude Code?" (tier 3, independent experiment)

URL: https://softwarearchitectureweekly.substack.com/p/can-local-llms-replace-claude-code
Accessed: 2026-11-23 | Via: web_extract | Tier: benchmark (named author Vladimir Ivanov, method shown; PAYWALL: first half read, tuning half behind trial)

Dated Jul 23, 2026. Subtitle: "€4,250 of hardware, four models, one autonomous pipeline - and whether any of it can replace a €200/month subscription."

## Verbatim
- "The whole setup ended up with a cost of €4250."
- Machine: "an AMD Ryzen 9 9950X3D, an AMD Radeon AI PRO R9700 with 32GB of VRAM, running Arch Linux (Omicky)" [sic: Omarchy]. "The 32GB card is the whole story here - it's the single number that constrains almost every decision in this post."
- "For a 35-billion-parameter model, it takes roughly 70GB just to store the numbers. My card has 32GB total. The model simply does not fit into VRAM."
- Quantization explainer: "you round those 16-bit numbers down to something smaller - 8 bits, 6 bits, 4 bits - and store that instead. You lose a little precision. In exchange, the model shrinks dramatically and runs faster ... The whole game is figuring out how much precision you can throw away before the model gets noticeably dumber."
- Model rotation: "Qwen3-8B, Q4_K_M (~5GB)"; "Qwen3.6-35B-A3B, Q4_K_M (~22GB). This is a Mixture-of-Experts model - 35B parameters total, but only about 3B 'active' per token"; "Ornith-1.0-35B, Q5_K_M (~25GB)"; back to Qwen3.6-35B-A3B at "Q6_K (~29GB)".
- "at Q6_K the model weights alone occupy 29.3GB out of 32GB. That leaves a sliver of the card for everything else inference needs (the KV cache, i.e. the model's working memory for the current conversation)"
- KV cache defined: "the model's working memory for the current conversation"
- Break point: "Ornith simply didn't show up. Despite the leaderboard scores, one triggered run against Ornith produced a clean, zero-error exit and a grand total of one line in the log: 'I'm ready to help! What would you like to work on?' No ticket read, no tool call, nothing. ... Rolling back to Qwen3.6-35B-A3B and re-running the identical trigger worked correctly on the first try."
- "Benchmark leaderboards, it turns out, tell you almost nothing about whether a model will actually follow a long, detailed operating manual."
- Bridge pain: "Claude Code speaks Anthropic's Messages API. llama-server speaks an OpenAI-compatible chat-completions API. These are not the same shape of JSON, and nothing translates between them for free."

## Use in brief
- The break-points beat: benchmarks vs real harness behavior; VRAM ceiling math (70GB -> 32GB card); KV cache squeeze.
- Caveat: paywalled second half; only first-half facts used.
