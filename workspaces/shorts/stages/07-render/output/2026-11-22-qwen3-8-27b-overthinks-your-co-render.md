---
slug: 2026-11-22-qwen3-8-27b-overthinks-your-co
duration_s: 42.37
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.904418
---

# Render: 2026-11-22-qwen3-8-27b-overthinks-your-co

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-22T13:36:53Z.

## Gates
- lint_video --final: pass (duration 42.37 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.904418)
- Length: 42.37 s; narration 41.48 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 117 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.52 | 5.53 | 2 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s02 | 4.74 | 4.77 | 4 | glm-5.3 |  |
| s03 | 9.22 | 9.23 | 3 | glm-5.3 |  |
| s04 | 9.34 | 9.33 | 3 | glm-5.3 |  |
| s05 | 4.74 | 4.77 | 2 | glm-5.3-flash |  |
| s06 | 8.72 | 8.73 | 3 | glm-5.3 |  |

## Assembly
- video total 42.37s vs narration 41.48s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-22-qwen3-8-27b-overthinks-your-co/render/2026-11-22-qwen3-8-27b-overthinks-your-co-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 380
