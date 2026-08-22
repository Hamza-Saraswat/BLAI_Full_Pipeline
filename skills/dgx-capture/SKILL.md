---
name: dgx-capture
description: Run an episode's experiment plan on the NVIDIA DGX Spark under a strict command allowlist, inside the night window, recording every command as an asciinema cast and parsing the measured numbers (tokens/s, memory, load time) into capture.json for the render and reconcile steps.
metadata:
  tags: "dgx-spark, benchmark, capture, asciinema, allowlist, ollama, llama.cpp, vllm"
---

# dgx-capture

The Spark runs real models so the episode can show real numbers. This skill is the only way a plan gets to run commands on the box: every command passes `allowlist.json`, runs under a timeout, is recorded, and its numbers are parsed into one JSON file the later stages trust more than the script.

## When to Use

- The capture stage of `workspaces/long-form` (Spark side) when the hub note is `building` and `<slug>-experiment.md` exists.
- Re-running one experiment after a reconcile block (edit the plan, keep the ids).
- Measuring an endpoint by hand with the benchmark scripts (`benchmarks/`), for example while writing a plan.

## What You Need Before Calling

- The plan: `<slug>-experiment.md` in the format of `rules/experiment-plan-format.md` (a ```json block of `{id, command, timeout_s, expect, parse}`), or a plain `.json`.
- The Spark with the runtimes the plan names on PATH (`ollama`, `llama-server`, `llama-cli`, `llama-bench`, `vllm`, `docker`, `nvidia-smi`); `asciinema` and `timeout` (coreutils) installed by `build/install.sh`.
- The clock: the default window is 01:00-06:00 America/Chicago (`--window night`). Outside it the script exits 1 at once and runs nothing; `--window any` overrides for hand runs.
- The working directory: run from the repo root, because plans call `python3 skills/dgx-capture/benchmarks/...` with repo-relative paths.

## How It Works

1. `scripts/capture.py --plan FILE --out DIR [--window any|night] [--dry-run]` parses the plan and checks every command against `allowlist.json`: command family by first token, allowed subcommands, argument patterns (benchmark script paths, localhost URLs, docker images), deny patterns (`sudo`, `rm`, pipes to a shell, `wget`, `ssh`, `dd`, `mkfs`, backticks, `$(`), and redirections, which may only point at `/dev/null` or inside `DIR`. One refusal refuses the whole plan (exit 1, nothing runs, the message names the rule).
2. The window check, then the commands in order. Before a GPU command (ollama, llama.cpp, vllm, docker, the benchmark scripts) it reads `nvidia-smi --query-gpu=memory.used,memory.total` and skips the command when less than `gpu_min_free_gb` (8) is free.
3. Each command runs as `timeout -k 5 N bash -c '...'`, recorded with `asciinema rec -c ... DIR/<id>.cast` when asciinema is installed, else captured by subprocess. The exit code travels in the transcript so both paths agree.
4. Metrics are parsed from the transcript with regexes: ollama `--verbose` (`eval rate`, `load duration`), llama.cpp timings (`eval time ... tokens per second`, `load time`), `llama-bench` tables (`tg` and `pp` rows), `vllm bench` (`Output token throughput`, `TTFT`), `nvidia-smi` memory, `ollama ps`, and the JSON the benchmark scripts print. `parse` names the metric the entry must produce; a missing metric is a failure.
5. `DIR/capture.json` is rewritten after every command: `[{id, command, status, exit, duration_s, started_at, stdout_tail, metrics, cast, reason}]`. Exit 1 if any command was refused, failed, timed out, was skipped for GPU memory or produced no metric, unless that entry says `"expect": "may_fail"`.
6. `--dry-run` executes nothing: it checks the plan, fakes `nvidia-smi`, fills `capture.json` from `fixtures/fake-outputs/` and exits 0 (or 1 on a refusal). Without `--plan` it uses `fixtures/plan-example.md`.

```
python3 skills/dgx-capture/scripts/capture.py --plan workspaces/long-form/stages/<n>/output/<slug>-experiment.md --out BUILD/<slug>/capture
python3 skills/dgx-capture/benchmarks/bench_openai_compat.py --url http://localhost:8000/v1 --model M --runs 3
python3 skills/dgx-capture/benchmarks/bench_ollama.py --model M --runs 3
```

## Rules

- `rules/allowlist.md`: the command families, why each is there, the deny list, how to add a family.
- `rules/experiment-plan-format.md`: the plan format, every field, parse types, a complete example plan.
- `rules/reconcile.md`: tolerances, how a measured number rewrites a narration line, when to block for a re-script.

## After the Call

- `DIR/capture.json` and `DIR/<id>.cast` feed `skills/render-longform` (`--captures DIR`; `terminal-replay` scenes reference ids) and the reconcile step (`rules/reconcile.md`).
- Write `stages/<capture-stage>/output/<slug>-capture.md` from `capture.json`: one table row per id (status, duration, metrics) plus the reconcile decisions. Casts are binaries for git purposes and stay out of the repo (`.gitignore`).
- On exit 1 read the `reason` of every non-`ok` entry. A refusal is a plan bug (fix the command or extend the allowlist through its rule file); a `gpu_busy` skip means another process holds the GPU; a `no_metric` means the tool's output format changed and the regex in `capture.py` needs a look.
