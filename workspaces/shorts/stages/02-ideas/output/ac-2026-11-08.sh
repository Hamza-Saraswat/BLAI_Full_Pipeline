#!/bin/env bash
# Autocomplete fan-out for 2026-11-08 ideas candidates (stage 02 step 2)
set -u
cd /home/buildlocalai/blai/repo
S=skills/youtube-keyword-research/scripts
OUT=workspaces/shorts/stages/02-ideas/output/2026-11-08-autocomplete.json
echo '{}' > "$OUT"
kw() {
  local key="$1"; shift
  local res
  res=$(python3 "$S/autocomplete.py" "$1" 2>&1)
  python3 - "$OUT" "$key" "$res" << 'PYEOF'
import json, sys
path, key, raw = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    obj = json.loads(raw)
except Exception:
    obj = {"error": raw[:300]}
with open(path) as f: data = json.load(f)
data[key] = obj
with open(path, "w") as f: json.dump(data, f, indent=1)
print(key, "->", obj.get("depth_score", obj.get("error")))
PYEOF
}
kw owui_agents "open webui coding agent"
kw owui_http "open webui plain http"
kw modchip "run deepseek without gpu"
kw tokirecur "llama.cpp kv cache"
kw wsp "weight space programming"
kw mtp "llama.cpp speculative decoding"
kw fp4 "qwen3.8 flash fp4"
kw vindex "vulkan gguf inference"
kw aivim "aivim ollama"
kw maxxbench "maxxbench deepswe"
kw jacq "write cuda kernels"
echo "ALL DONE"
