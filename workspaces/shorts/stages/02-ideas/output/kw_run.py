#!/usr/bin/env python3
"""Stage 02 helper: run autocomplete for each seed, assemble candidates.json."""
import json, subprocess, pathlib

out = pathlib.Path(__file__).parent
seeds = [
    # (title, lane, keyword, why_now, named_product)
    ("Ripple-65B: the 65B open weights that beat the cloud coders", "news-react", "ripple 65b", "Ricursive shipped the Ripple-65B preview, 305 pts / 109 comments on HN, 17 h ago", True),
    ("Asus Ascent GX10 vs DGX Spark: same GB10, different box", "comparison", "dgx spark", "Spheron published the GB10 box comparison (Asus/Dell/HP/Lenovo vs Spark), 23 h ago", True),
    ("Asus Ascent GX10 vs DGX Spark: same GB10, different box", "comparison", "asus ascent gx10", "same item", True),
    ("Unsloth v0.1.915: lower idle VRAM means bigger fine-tunes", "how-to", "unsloth fine tuning", "unsloth v0.1.915-beta released 18 h ago", True),
    ("llama.cpp overnight: 3 builds, and your pin matters", "news-react", "llama.cpp update", "b12123/b12124/b12125 all released within hours, 5 h ago", True),
    ("OpenCL llama.cpp: Adreno phones just got faster", "how-to", "llama.cpp android", "b12125 enables f32/q5_k multi-column GEMV by default on Adreno X2", True),
    ("GPUWorks: a GPU cluster in a 40 MB binary", "how-to", "vllm cluster", "Show HN 25 pts, 20 h ago", True),
    ("Kimi K3.1 Pro's 1.56 TB drop and what you can actually run", "news-react", "kimi k3", "weights on HF 3 d ago; 1.56 TB MXFP4 explainer 9 h ago", True),
    ("Qwen 27B at 256K context on a 24 GB Mac: just fit?", "myth-bust", "qwen 256k context", "JustFit repo posted 6 h ago on HN", True),
    ("Qwen3.5-4B GLB 3D Coder: a coder that fits any GPU", "how-to", "qwen 3.5 4b", "new on HF, 12.2k downloads in 4 d", True),
    ("DeepSeek is 53% of OpenRouter: what that says about open weights", "news-react", "deepseek openrouter", "dirac.run market-share measurement, 16 h ago", True),
    ("Best local LLM right now: what the benchmarks miss", "explainer", "best local llm", "evergreen pillar fallback; radar window thin on explainer items", True),
]

cands = []
for title, lane, kw, why, named in seeds:
    p = subprocess.run(
        ["python3", "skills/youtube-keyword-research/scripts/autocomplete.py", kw],
        capture_output=True, text=True, cwd="/home/buildlocalai/blai/repo", timeout=120)
    try:
        ac = json.loads(p.stdout)
    except Exception:
        ac = {"seed": kw, "error": p.stdout[:200] + p.stderr[:200], "depth_score": None, "suggestions": []}
    cands.append({
        "title": title, "lane": lane, "keyword": kw, "why_now": why,
        "named_product": named,
        "autocomplete": {"depth_score": ac.get("depth_score"), "n_suggestions": len(ac.get("suggestions") or [])},
        "competition": None, "vidiq": None, "trend_slope": None,
        "null_reasons": {
            "competition": "YT_API_KEY not set in this environment",
            "vidiq": "no vidIQ MCP connector attached",
        },
    })
    print(kw, "->", ac.get("depth_score"))

with open(out / "2026-11-05-candidates.json", "w") as f:
    json.dump(cands, f, indent=1)
print("wrote", len(cands), "candidates")
