---
slug: 2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th
duration_s: 40.73
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.725826
---

# Render: 2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-03T13:40:26Z.

## Gates
- lint_video --final: pass (duration 40.73 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.725826)
- Length: 40.73 s; narration 39.80 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 104 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.56 | 5.57 | 3 | glm-5.3 |  |
| s02 | 8.41 | 8.43 | 3 | glm-5.3 |  |
| s03 | 12.24 | 12.27 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s04 | 8.09 | 8.10 | 4 | glm-5.3 |  |
| s05 | 6.34 | 6.37 | 3 | glm-5.3 |  |

## Assembly
- video total 40.73s vs narration 39.80s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th/render/2026-11-03-nanbeige4-3-33b-vs-qwen-3-8-th-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 311
