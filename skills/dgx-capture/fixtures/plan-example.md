# Experiment plan: 2026-08-24-deepseek-v4-flash-dgx-spark

Series: benchmarks. Question the episode answers: how fast does DeepSeek V4 Flash generate on the DGX Spark at Q4, and does it fit with a 32k context?

Window: night (01:00-06:00 America/Chicago). Expected wall time: about 25 minutes plus the pull.
Scenes that cite these ids: s05 terminal-replay (`cmd1`), s07 stat-callout (`bench1`), s09 comparison-table (`vram1`).

```json
[
  {"id": "gpu0", "command": "nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader", "timeout_s": 30, "expect": "ok", "parse": "vram_gb", "note": "baseline before anything loads"},
  {"id": "pull1", "command": "ollama pull deepseek-v4-flash:q4_k_m", "timeout_s": 3600, "expect": "ok", "parse": "none"},
  {"id": "cmd1", "command": "ollama run deepseek-v4-flash:q4_k_m --verbose \"Explain what a KV cache is in three sentences.\"", "timeout_s": 600, "expect": "ok", "parse": "tok_s", "note": "the replay the viewer sees"},
  {"id": "ps1", "command": "ollama ps", "timeout_s": 30, "expect": "ok", "parse": "ollama_ps", "note": "proves the model sits 100 % on the GPU"},
  {"id": "bench1", "command": "python3 skills/dgx-capture/benchmarks/bench_ollama.py --model deepseek-v4-flash:q4_k_m --runs 3", "timeout_s": 900, "expect": "ok", "parse": "tok_s", "note": "median of 3 is the number the script cites"},
  {"id": "vram1", "command": "nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader", "timeout_s": 30, "expect": "ok", "parse": "vram_gb", "note": "memory with the model loaded"},
  {"id": "llama1", "command": "llama-bench -m /srv/models/DeepSeek-V4-Flash-Q4_K_M.gguf -ngl 99 -p 512 -n 128", "timeout_s": 1800, "expect": "may_fail", "parse": "tok_s", "note": "optional cross-check; the GGUF may not be on disk yet"},
  {"id": "api1", "command": "curl http://localhost:11434/v1/models", "timeout_s": 30, "expect": "may_fail", "parse": "none", "note": "is the OpenAI-compatible endpoint up"}
]
```

Notes for the reconcile step: `bench1.metrics.tok_s` replaces the tokens-per-second number in s07 and s11; `vram1.metrics.vram_gb` replaces the memory number in s02 and s09. Tolerances in `rules/reconcile.md`.
