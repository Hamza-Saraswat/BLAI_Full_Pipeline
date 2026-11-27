---
slug: 2026-11-27-amd-forked-llama-cpp-for-its-o
duration_s: 42.40
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.880856
---

# Render: 2026-11-27-amd-forked-llama-cpp-for-its-o

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-27T14:02:15Z.

## Gates
- lint_video --final: pass (duration 42.40 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.880856)
- Length: 42.40 s; narration 41.32 s
- Scenes: 7/7 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07)
- Captions: 112 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 2.19 | 2.20 | 1 | glm-5.3-flash |  |
| s02 | 11.24 | 11.27 | 4 | glm-5.3 |  |
| s03 | 5.79 | 5.80 | 3 | glm-5.3 |  |
| s04 | 6.50 | 6.50 | 3 | glm-5.3 |  |
| s05 | 9.14 | 9.17 | 3 | glm-5.3 |  |
| s06 | 3.66 | 3.67 | 1 | glm-5.3-flash |  |
| s07 | 3.80 | 3.80 | 2 | glm-5.3-flash |  |

## Assembly
- video total 42.40s vs narration 41.32s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-27-amd-forked-llama-cpp-for-its-o/render/2026-11-27-amd-forked-llama-cpp-for-its-o-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 406
