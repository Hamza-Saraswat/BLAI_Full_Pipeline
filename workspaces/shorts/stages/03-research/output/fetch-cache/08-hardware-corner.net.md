<!-- url: https://www.hardware-corner.net/first-dgx-spark-llm-benchmarks/ -->
<!-- fetched via web_extract 2026-10-24, tier 3 (benchmark, Allan Witt, Oct 15 2025, reports llama.cpp discussion 16578 numbers). -->

Key verbatim passages (full page was fetched; file below reconstructed from the fetch):

- "The DGX Spark relies on integrated LPDDR5 memory, which tops out at approximately 275 GB/s."
- Raw numbers table: gpt-oss 120B MXFP4 pp2048 1723.07 / tg32 38.55; qwen3moe 30B.A3B Q8_0 pp2048 2916.25 / tg32 47.08 (initial Oct 2025 run).
- Comparison table: "| Nvidia DGX Spark (MXFP4) | 1723.07 | 38.55 |", "| AMD Strix Halo (MXFP4) | 339.87 | 34.13 |", "| Apple M3 Ultra 256GB (MXFP4) | 863.73 | 70.79 |", "| 3x RTX 3090 (MXFP4) | 1641.89 | 124.03 |"
- "the DGX Spark demonstrates extremely strong prompt processing speed, thanks to the Blackwell architecture and NVFP4"
- "At around 38 tokens per second on the 120B model, it is only marginally faster than the AMD Strix Halo APU."
- "A well-configured 3x 3090 system, which can be built from used parts for a comparable or even lower price, delivers over three times the token generation speed."
