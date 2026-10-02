---
slug: 2026-10-02-llama-cpp-shipped-three-builds
duration_s: 45.40
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.774217
---

# Render: 2026-10-02-llama-cpp-shipped-three-builds

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-02T12:47:25Z.

## Gates
- lint_video --final: pass (duration 45.40 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.774217)
- Length: 45.40 s; narration 44.32 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 125 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 2.60 | 2.60 | 1 | glm-5.3-flash |  |
| s02 | 9.18 | 9.20 | 3 | glm-5.3 |  |
| s03 | 8.15 | 8.17 | 3 | glm-5.3 |  |
| s04 | 9.38 | 9.40 | 4 | glm-5.3 |  |
| s05 | 5.80 | 5.80 | 2 | glm-5.3-flash |  |
| s06 | 10.21 | 10.23 | 2 | glm-5.3-flash |  |

## Assembly
- video total 45.40s vs narration 44.32s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-02-llama-cpp-shipped-three-builds/render/2026-10-02-llama-cpp-shipped-three-builds-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 166
