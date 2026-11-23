# 05 -- Unsloth docs, Inkling 2 Mini run-locally guide

URL: https://unsloth.ai/docs/models/inkling-2-mini
Accessed: 2026-11-23 | Via: web_extract | Tier: docs (maintained documentation; full-page cached at ~/.hermes/cache/web/unsloth.ai-eee4b675d7.md)

## Verbatim
- "Inkling 2 Mini is Thinking Machines Lab's 26.4B MoE (5.4B active) model for coding, agentic, and vision workloads. Released under Apache 2.0 and built on a Looped Transformers variant, it has 1M context and scores 48.2% on DeepSWE v1.1 and 77.9% on SWEBench Pro v2 (Hard), making it the strongest for its size, ahead of Qwen3.8-27B."
- "Run on 16GB RAM or 24GB RAM for full precision."
- "UD-Q8_K_XL is full precision. The recommended quant is UD-Q4_K_XL (17.6 GB)."
- Hardware requirements table (RAM + VRAM, or unified memory): 1-bit 9 GB; 2-bit 10-11 GB; 3-bit 13-15 GB; 4-bit 17-18 GB; 8-bit (lossless) 24 GB.
- "Use these ranges as a starting point. Longer contexts, image inputs and other apps can use more memory."
- "Mini scores 6.0 percentage points higher than Qwen3.8-27B on DeepSWE v1.1 and 4.1 points higher on SWEBench Pro v2 (Hard)."
- Quant table: UD-Q2_K_XL 9.14 GB, mean KLD 0.0595, same top token 91.6%; UD-Q3_K_XL 13.63 GB, 96.3%; UD-Q4_K_XL 17.63 GB, 98.0%; UD-Q8_K_XL 22.87 GB (reference).
- Benchmark table (same numbers as the model card): SWE-bench Verified Inkling 2 Mini 79.2%, Qwen3.8-27B 77.8%, Muse Glimmer 76.0%, Gemma 4 31B 46.1%; DeepSWE v1.1 48.2% vs 42.2%; Terminal Bench v2.1 71.6% vs 73.0%; params row "5 / 26" for Inkling vs "27 / 27" Qwen.
- Setup path: Unsloth Desktop (macOS, Windows, Linux), search "Inkling 2 Mini", download quant that fits; llama.cpp path needs "an Unsloth or llama.cpp build with looped-layer support and per-expert NVFP4 scales".

## Use in brief
- The quantization-for-beginners numbers: 4-bit file 17.6 GB on a 24 GB card, 2-bit at 10-11 GB, and the quality-vs-size ladder (91.6% -> 98.0% same top token).
- Named tools: Unsloth Desktop, llama.cpp, GGUF.
