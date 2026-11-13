---
slug: 2026-11-13-llama-cpp-1-0-pin-it-before-b1
duration_s: 34.70
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.842768
---

# Render: 2026-11-13-llama-cpp-1-0-pin-it-before-b1

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-13T13:55:05Z.

## Gates
- lint_video --final: pass (duration 34.70 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.842768)
- Length: 34.70 s; narration 33.64 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 109 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.28 | 5.30 | 1 | glm-5.3-flash |  |
| s02 | 8.00 | 8.00 | 2 | glm-5.3-flash |  |
| s03 | 7.90 | 7.90 | 2 | glm-5.3-flash |  |
| s04 | 7.39 | 7.40 | 2 | glm-5.3-flash |  |
| s05 | 6.07 | 6.10 | 1 | glm-5.3-flash |  |

## Assembly
- video total 34.70s vs narration 33.64s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-13-llama-cpp-1-0-pin-it-before-b1/render/2026-11-13-llama-cpp-1-0-pin-it-before-b1-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 350
