import json, glob, os
out_dir = os.path.dirname(os.path.abspath(__file__))
# map candidate -> autocomplete file (keyword chosen per fit)
kw_map = {
  "NariQ: Qwen3.8-27B at 3 bits in 10 GB": "auto_qwen_3.8.json",
  "Unsloth: Inkling 2 Mini runs 1.9x faster tonight": "auto_inkling_2_mini.json",
  "sparkDash: watch your Spark cluster in one tab": "auto_dgx_spark_monitoring.json",
  "GLM 5.3 is not MIT: read the license before you ship": "auto_glm_5.3.json",
  "Rackmount your DGX Sparks: 1.33U vs DIY": "auto_dgx_spark_rack.json",
  "MoRI: the agentic KV cache fits on NVMe": "auto_kv_cache_nvme.json",
  "Tencent Hy4 weights landed: one GGUF from local": "auto_tencent_hy4.json",
  "whisper.cpp 1.9.6: the CUDA build fix": "auto_whisper.cpp.json",
  "Kolibri 1.1: a German model for EU data desks": "auto_aleph_alpha_kolibri.json",
  "Qwen3.6 35B at 517 tok/s on a MacBook Pro": "auto_qwen_macbook.json",
}
kws = {
  "NariQ: Qwen3.8-27B at 3 bits in 10 GB": "qwen 3.8 27b",
  "Unsloth: Inkling 2 Mini runs 1.9x faster tonight": "inkling 2 mini",
  "sparkDash: watch your Spark cluster in one tab": "dgx spark monitoring",
  "GLM 5.3 is not MIT: read the license before you ship": "glm 5.3",
  "Rackmount your DGX Sparks: 1.33U vs DIY": "dgx spark rack",
  "MoRI: the agentic KV cache fits on NVMe": "kv cache nvme",
  "Tencent Hy4 weights landed: one GGUF from local": "tencent hy4",
  "whisper.cpp 1.9.6: the CUDA build fix": "whisper.cpp",
  "Kolibri 1.1: a German model for EU data desks": "aleph alpha kolibri",
  "Qwen3.6 35B at 517 tok/s on a MacBook Pro": "qwen macbook",
}
cands = json.load(open(os.path.join(out_dir, "2026-11-24-candidates.json")))
for c in cands:
    af = os.path.join(out_dir, kw_map[c["title"]])
    auto = json.load(open(af))
    c["keyword"] = kws[c["title"]]
    c["autocomplete"] = {"seed": auto.get("seed"), "depth_score": auto.get("depth_score"),
                          "suggestions": auto.get("suggestions", [])[:12]}
    c["competition"] = None
    c["competition_note"] = "YT_API_KEY not set; competition snapshot skipped this run"
    c["vidiq"] = None
    c["vidiq_note"] = "vidIQ connector not attached to this run"
    c["trend_slope"] = None
    c["named_product"] = True
json.dump(cands, open(os.path.join(out_dir, "2026-11-24-candidates.json"), "w"), indent=2)
print("wrote", len(cands), "candidates")
