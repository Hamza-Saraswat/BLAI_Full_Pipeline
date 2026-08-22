# Experiment Plan Format

The plan is `workspaces/long-form/stages/<n>/output/<slug>-experiment.md`: a markdown note (so it reads well in Obsidian and the build journal) with one ```json block that `capture.py` executes. A bare `.json` file with the same list also works.

## The JSON block

```json
[
  {"id": "cmd1", "command": "ollama run deepseek-v4-flash:q4_k_m --verbose \"Explain what a KV cache is in three sentences.\"", "timeout_s": 600, "expect": "ok", "parse": "tok_s", "note": "the replay the viewer sees"}
]
```

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | lowercase letters, digits, `-`, `_`; unique; the spec's `capture_ref` and the reconcile notes point at it |
| `command` | yes | one shell command line; must pass `allowlist.json` (`rules/allowlist.md`); pipes to the listed filters and redirections inside the capture dir are fine |
| `timeout_s` | no (600) | wall-clock limit; the command is killed 5 s after it |
| `expect` | no (`ok`) | `ok`: a non-zero exit, a timeout, a GPU skip or a missing metric fails the run; `may_fail`: the entry is recorded and the run continues |
| `parse` | no (`none`) | which metric the entry must produce: `tok_s`, `vram_gb`, `load_s`, `ollama_ps`, `none` |
| `gpu` | no (auto) | force the free-memory check on or off |
| `note` | no | one line for the humans reading `capture.json` |

Parse types and where the number comes from:

| `parse` | Metric key | Source lines |
|---------|------------|--------------|
| `tok_s` | `tok_s` (also `prompt_tok_s` when printed) | ollama `eval rate: N tokens/s`; llama.cpp `eval time = ... (N tokens per second)`; `llama-bench` `tg` row; vllm `Output token throughput (tok/s): N`; the benchmark scripts' JSON |
| `vram_gb` | `vram_gb`, `vram_total_gb` | `nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader` |
| `load_s` | `load_s` | ollama `load duration`; llama.cpp `load time = N ms` |
| `ollama_ps` | `models[]`, `ollama_vram_gb` | the `ollama ps` table (size and `100% GPU`) |
| `none` | whatever is found | anything; nothing is required |

Every metric the parser recognizes is recorded regardless of `parse`; `parse` only says which one must be present.

## Rules for writing a plan

- Order: a baseline `nvidia-smi` first, pulls before runs, a second `nvidia-smi` after the model is loaded, benchmarks last.
- One measurement the script cites equals one entry whose `id` the spec references. The number the narration quotes is the median the benchmark script prints (`runs: 3`), not the single `ollama run` the viewer watches.
- Timeouts: pulls 3600, first runs 600 (the model loads), benchmarks 900, readings 30.
- `may_fail` for anything optional (a cross-check on a file that may not exist yet, an endpoint that may be down). Never on the entry the episode's main number comes from.
- Keep the whole plan inside the night window: a 25-minute plan plus an 85 GB pull is fine; a 4-hour fine-tune is its own plan on its own night.
- Paths are repo-relative (`python3 skills/dgx-capture/benchmarks/bench_ollama.py ...`); `capture.py` runs from the repo root.

## Complete example: DeepSeek V4 Flash on the Spark

This is `fixtures/plan-example.md`, which `--dry-run` uses.

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

Around the block the note states the question the episode answers, the window, the expected wall time, and which scene ids cite which entry ids. The spec's `terminal-replay` scene carries `"capture_ref": "cmd1"`; the reconcile step reads `bench1.metrics.tok_s` and `vram1.metrics.vram_gb`.

## Output: capture.json

One object per entry, in plan order, rewritten after every command:

```json
{"id": "cmd1", "command": "...", "status": "ok", "exit": 0, "duration_s": 3.41, "started_at": "2026-08-24T02:10:11-05:00",
 "timeout_s": 600, "expect": "ok", "parse": "tok_s", "families": ["ollama"], "gpu": true, "gpu_free_gb": 42.8,
 "cast": "cmd1.cast", "stdout_tail": "...last 60 lines...", "metrics": {"tok_s": 41.71, "prompt_tok_s": 98.08, "load_s": 0.031}, "reason": null}
```

`status` is one of `ok`, `failed`, `timeout`, `skipped` (GPU busy), `no_metric`, `refused`. `cast` is the asciinema file next to it, or `null` when asciinema was not available. `render-longform` replays the cast in `terminal-replay` scenes and shows `metrics` as chips.
