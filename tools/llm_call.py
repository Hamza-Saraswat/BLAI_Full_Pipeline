#!/usr/bin/env python3
"""One chat completion, no agent loop: packet in, text out.

    python3 tools/llm_call.py --provider moonshot-k3 --model kimi-k3 \
        --system-file packet/system.md --user-file packet/user.md --out draft.md

Exists because a blind writer or a judge does not need tools, a scratch shell or an
agent's system prompt: it needs its packet and one answer. Running those three
calls per Short as full subagents cost ~2.6M metered tokens on the 2026-08-30 walk;
as direct calls they cost ~30K. Blindness is structural here (three separate
processes, nothing shared).

Providers: a named entry in ~/.hermes/config.yaml (`providers.<name>.base_url` +
`key_env`), or --base-url/--key-env given explicitly. `zai` is built in and pinned to
the coding-plan endpoint (never the pay-as-you-go one). Keys come from the
environment; when the named env var is empty the script reads ~/.hermes/.env itself so
it also works from a plain ssh shell.

stdout: the completion (or nothing when --out is given). stderr: one JSON line
{"model", "prompt_tokens", "completion_tokens", "seconds"}. Exit 0/1. Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

HERMES_DIR = pathlib.Path(os.environ.get("HERMES_HOME", "~/.hermes")).expanduser()
BUILTIN = {
    # coding-plan endpoint; GLM_BASE_URL overrides (the same pin Hermes uses)
    "zai": {"base_url": os.environ.get("GLM_BASE_URL") or "https://api.z.ai/api/coding/paas/v4",
            "key_env": "GLM_API_KEY"},
}


def hermes_env(name: str) -> str:
    """Env var, else the value from ~/.hermes/.env (first non-empty KEY=VALUE line)."""
    val = os.environ.get(name, "").strip()
    if val:
        return val
    env_file = HERMES_DIR / ".env"
    if not env_file.exists():
        return ""
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() == name and v.strip().strip('"').strip("'"):
            return v.strip().strip('"').strip("'")
    return ""


def provider_config(name: str) -> dict:
    if name in BUILTIN:
        return dict(BUILTIN[name])
    cfg_path = HERMES_DIR / "config.yaml"
    if cfg_path.exists():
        # Minimal YAML walk: find `providers:` then `  <name>:` then its base_url/key_env.
        # Avoids a PyYAML dependency for a two-key lookup.
        lines = cfg_path.read_text(encoding="utf-8").splitlines()
        in_providers = in_name = False
        found: dict = {}
        for raw in lines:
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            indent = len(raw) - len(raw.lstrip())
            if indent == 0:
                in_providers = raw.strip() == "providers:"
                in_name = False
                continue
            if in_providers and indent == 2 and raw.strip().rstrip(":") == name:
                in_name = True
                continue
            if in_providers and indent == 2:
                in_name = False
                continue
            if in_name and indent >= 4 and ":" in raw:
                k, v = raw.strip().split(":", 1)
                found[k.strip()] = v.strip().strip('"').strip("'")
        if found.get("base_url"):
            return found
    raise SystemExit("llm_call: unknown provider %r (not built in, not in %s)" % (name, cfg_path))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--system-file", required=True)
    ap.add_argument("--user-file", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--max-tokens", type=int, default=4000)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--base-url", default="", help="override the provider's base_url")
    ap.add_argument("--key-env", default="", help="override the env var holding the API key")
    a = ap.parse_args()

    cfg = provider_config(a.provider)
    base_url = (a.base_url or cfg.get("base_url", "")).rstrip("/")
    key_env = a.key_env or cfg.get("key_env", "")
    api_key = hermes_env(key_env) if key_env else ""
    if key_env and not api_key:
        raise SystemExit("llm_call: %s is empty (env and ~/.hermes/.env)" % key_env)

    body = {
        "model": a.model,
        "temperature": a.temperature,
        "max_tokens": a.max_tokens,
        "messages": [
            {"role": "system", "content": pathlib.Path(a.system_file).read_text(encoding="utf-8")},
            {"role": "user", "content": pathlib.Path(a.user_file).read_text(encoding="utf-8")},
        ],
    }
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = "Bearer " + api_key
    req = urllib.request.Request(base_url + "/chat/completions", data=json.dumps(body).encode("utf-8"),
                                 headers=headers, method="POST")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=a.timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit("llm_call: HTTP %d from %s: %s" % (e.code, base_url, e.read()[:400].decode("utf-8", "replace")))
    except (urllib.error.URLError, TimeoutError) as e:
        raise SystemExit("llm_call: %s unreachable: %s" % (base_url, e))

    try:
        text = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise SystemExit("llm_call: unexpected response shape: %s" % json.dumps(data)[:400])
    usage = data.get("usage") or {}
    print(json.dumps({"model": data.get("model", a.model),
                      "prompt_tokens": usage.get("prompt_tokens"),
                      "completion_tokens": usage.get("completion_tokens"),
                      "seconds": round(time.time() - t0, 1)}), file=sys.stderr)
    if a.out:
        out = pathlib.Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
