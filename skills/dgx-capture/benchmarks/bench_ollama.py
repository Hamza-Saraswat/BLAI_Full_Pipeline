#!/usr/bin/env python3
"""Measure an Ollama model with `ollama run MODEL --verbose` and report the median.

Usage:
  bench_ollama.py --model M [--runs 3] [--prompt "..."] [--timeout 600] [--dry-run]

Ollama prints its timing block to stderr; this parses eval rate (tokens/s), prompt eval
rate, load duration and total duration per run. Prints one JSON object on stdout
({tok_s, prompt_tok_s, load_s, runs[...]}), which capture.py parses. Exit 1 when a run
fails or prints no eval rate.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import statistics
import subprocess
import sys

DEFAULT_PROMPT = "Explain what a KV cache is in three sentences, then list three things that change its size."
UNITS = {"ms": 0.001, "s": 1.0, "m": 60.0, "µs": 1e-6, "us": 1e-6}


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def parse_verbose(text: str) -> dict:
    out: dict = {}
    m = re.search(r"eval rate:\s*([\d.]+)\s*tokens/s", text)
    if m:
        out["tok_s"] = float(m.group(1))
    m = re.search(r"prompt eval rate:\s*([\d.]+)\s*tokens/s", text)
    if m:
        out["prompt_tok_s"] = float(m.group(1))
    m = re.search(r"load duration:\s*([\d.]+)\s*(ms|s|m|µs|us)\b", text)
    if m:
        out["load_s"] = round(float(m.group(1)) * UNITS[m.group(2)], 3)
    m = re.search(r"total duration:\s*([\d.]+)\s*(ms|s|m)\b", text)
    if m:
        out["total_s"] = round(float(m.group(1)) * UNITS[m.group(2)], 3)
    m = re.search(r"eval count:\s*(\d+)\s*token", text)
    if m:
        out["eval_count"] = int(m.group(1))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    ap.add_argument("--timeout", type=float, default=600.0)
    ap.add_argument("--dry-run", action="store_true", help="print fixed fake numbers, run nothing")
    args = ap.parse_args()

    result = {"model": args.model, "prompt": args.prompt, "runs": []}
    if args.dry_run:
        result["dry_run"] = True
        result["runs"] = [{"tok_s": 41.71, "prompt_tok_s": 98.08, "load_s": 0.031, "total_s": 2.93, "eval_count": 63},
                          {"tok_s": 41.2, "prompt_tok_s": 97.5, "load_s": 0.03, "total_s": 2.96, "eval_count": 63},
                          {"tok_s": 42.0, "prompt_tok_s": 98.6, "load_s": 0.03, "total_s": 2.9, "eval_count": 63}][: max(1, args.runs)]
    else:
        if shutil.which("ollama") is None:
            log("error: ollama is not on PATH")
            return 1
        for i in range(max(1, args.runs)):
            try:
                proc = subprocess.run(["ollama", "run", args.model, "--verbose", args.prompt], capture_output=True, text=True,
                                      stdin=subprocess.DEVNULL, timeout=args.timeout)
            except subprocess.TimeoutExpired:
                log("error: run %d timed out after %.0f s" % (i + 1, args.timeout))
                return 1
            if proc.returncode != 0:
                log("error: run %d exited %d: %s" % (i + 1, proc.returncode, proc.stderr.strip()[-300:]))
                return 1
            r = parse_verbose(proc.stderr + "\n" + proc.stdout)
            if "tok_s" not in r:
                log("error: run %d printed no eval rate (is --verbose supported by this ollama?)" % (i + 1))
                return 1
            log("run %d: %.1f tok/s, load %.2f s" % (i + 1, r["tok_s"], r.get("load_s", 0.0)))
            result["runs"].append(r)
    result["tok_s"] = round(statistics.median(r["tok_s"] for r in result["runs"]), 2)
    prompts = [r["prompt_tok_s"] for r in result["runs"] if "prompt_tok_s" in r]
    loads = [r["load_s"] for r in result["runs"] if "load_s" in r]
    if prompts:
        result["prompt_tok_s"] = round(statistics.median(prompts), 2)
    if loads:
        result["load_s"] = round(statistics.median(loads), 3)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
