import json, subprocess, sys

KWS = ["minimax h3 image", "comfyui minimax", "llama.cpp update", "vllm cold start",
       "qwen4 max", "ollama 0.40", "llm compression", "zonos text to speech",
       "tesla k80 llm", "ai agent secrets"]

out = []
for kw in KWS:
    r = subprocess.run([sys.executable, "skills/youtube-keyword-research/scripts/autocomplete.py", kw],
                       capture_output=True, text=True, timeout=120)
    try:
        d = json.loads(r.stdout)
        out.append(f"{d['seed']} | depth {d['depth_score']} | top: " + ", ".join(d['suggestions'][:6]))
    except Exception as e:
        out.append(f"{kw} | ERROR {e}: {r.stdout[:200]} {r.stderr[:200]}")

with open("workspaces/shorts/stages/02-ideas/output/autocompletes-2026-11-11.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
