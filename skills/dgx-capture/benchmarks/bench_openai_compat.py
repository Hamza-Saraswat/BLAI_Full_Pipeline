#!/usr/bin/env python3
"""Measure generation speed and time-to-first-token against any OpenAI-compatible local
server (vLLM, llama-server, Ollama's /v1 endpoint). Stdlib only.

Usage:
  bench_openai_compat.py --url http://localhost:8000/v1 --model M [--prompt-tokens 256]
                         [--max-tokens 256] [--runs 3] [--warmup 1] [--timeout 300] [--dry-run]

Streams /chat/completions; TTFT is the first content chunk, tokens/s is completion
tokens divided by the time from the first to the last chunk. Prints one JSON object on
stdout ({tok_s, ttft_ms, runs[...]}), which capture.py parses. API key from
OPENAI_API_KEY if set (local servers rarely need one). Exit 1 on any failed request.
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
import urllib.error
import urllib.request

FILLER = ("The DGX Spark is a small desktop computer with a GB10 chip and one hundred twenty-eight gigabytes "
          "of unified memory shared between the CPU and the GPU. It runs open models at home. ")


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def build_prompt(tokens: int) -> str:
    words = max(20, int(tokens * 0.75))
    text = ""
    while len(text.split()) < words:
        text += FILLER
    text = " ".join(text.split()[:words])
    return text + "\n\nContinue this text for as long as you can, in the same style. Do not stop early."


def stream_once(url: str, model: str, prompt: str, max_tokens: int, timeout: float, api_key: str | None) -> dict:
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0,
        "stream": True,
        "stream_options": {"include_usage": True},
    }
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions", data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "Accept": "text/event-stream"}, method="POST")
    if api_key:
        req.add_header("Authorization", "Bearer " + api_key)
    t_start = time.perf_counter()
    t_first = None
    t_last = t_start
    chunks = 0
    usage = None
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        for raw in resp:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            payload = line[5:].strip()
            if payload == "[DONE]":
                break
            try:
                obj = json.loads(payload)
            except ValueError:
                continue
            if obj.get("usage"):
                usage = obj["usage"]
            choices = obj.get("choices") or []
            delta = (choices[0].get("delta") or {}) if choices else {}
            content = delta.get("content") or delta.get("reasoning_content") or ""
            if content:
                now = time.perf_counter()
                if t_first is None:
                    t_first = now
                t_last = now
                chunks += 1
    if t_first is None:
        raise RuntimeError("no content received from %s" % url)
    completion = (usage or {}).get("completion_tokens") or chunks
    gen_s = max(1e-6, t_last - t_first)
    return {
        "ttft_ms": round((t_first - t_start) * 1000.0, 1),
        "gen_tok_s": round((completion - 1) / gen_s, 2) if completion > 1 else 0.0,
        "completion_tokens": completion,
        "prompt_tokens": (usage or {}).get("prompt_tokens"),
        "total_s": round(t_last - t_start, 3),
        "token_count_source": "usage" if usage and usage.get("completion_tokens") else "chunks",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", default="http://localhost:8000/v1")
    ap.add_argument("--model", required=True)
    ap.add_argument("--prompt-tokens", type=int, default=256)
    ap.add_argument("--max-tokens", type=int, default=256)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--warmup", type=int, default=1, help="untimed runs before measuring (default 1)")
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--dry-run", action="store_true", help="print fixed fake numbers, no network")
    args = ap.parse_args()

    result = {"url": args.url, "model": args.model, "prompt_tokens_requested": args.prompt_tokens,
              "max_tokens": args.max_tokens, "runs": []}
    if args.dry_run:
        result["dry_run"] = True
        result["runs"] = [{"ttft_ms": 231.4, "gen_tok_s": 41.2, "completion_tokens": args.max_tokens, "total_s": 6.44},
                          {"ttft_ms": 228.9, "gen_tok_s": 41.8, "completion_tokens": args.max_tokens, "total_s": 6.35},
                          {"ttft_ms": 233.0, "gen_tok_s": 41.5, "completion_tokens": args.max_tokens, "total_s": 6.40}][: max(1, args.runs)]
    else:
        prompt = build_prompt(args.prompt_tokens)
        api_key = os.environ.get("OPENAI_API_KEY")
        try:
            for _ in range(max(0, args.warmup)):
                log("warmup run")
                stream_once(args.url, args.model, prompt, min(32, args.max_tokens), args.timeout, api_key)
            for i in range(max(1, args.runs)):
                r = stream_once(args.url, args.model, prompt, args.max_tokens, args.timeout, api_key)
                log("run %d: ttft %.0f ms, %.1f tok/s (%d tokens)" % (i + 1, r["ttft_ms"], r["gen_tok_s"], r["completion_tokens"]))
                result["runs"].append(r)
        except (urllib.error.URLError, RuntimeError, OSError, TimeoutError) as exc:
            log("error: %s" % exc)
            return 1
    result["tok_s"] = round(statistics.median(r["gen_tok_s"] for r in result["runs"]), 2)
    result["ttft_ms"] = round(statistics.median(r["ttft_ms"] for r in result["runs"]), 1)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
