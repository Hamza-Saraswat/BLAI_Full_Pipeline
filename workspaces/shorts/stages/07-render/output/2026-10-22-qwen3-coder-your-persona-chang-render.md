---
slug: 2026-10-22-qwen3-coder-your-persona-chang
duration_s: 42.00
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.74902
---

# Render: 2026-10-22-qwen3-coder-your-persona-chang

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-22T12:54:06Z.

## Gates
- lint_video --final: pass (duration 42.00 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.74902)
- Length: 42.00 s; narration 40.92 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 125 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.21 | 6.23 | 2 | glm-5.3-flash |  |
| s02 | 7.28 | 7.30 | 3 | glm-5.3 |  |
| s03 | 7.47 | 7.50 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s04 | 8.80 | 8.80 | 3 | glm-5.3 |  |
| s05 | 7.20 | 7.20 | 1 | glm-5.3-flash |  |
| s06 | 4.96 | 4.97 | 3 | glm-5.3 |  |

## Assembly
- video total 42.00s vs narration 40.92s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-22-qwen3-coder-your-persona-chang/render/2026-10-22-qwen3-coder-your-persona-chang-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 258
