---
slug: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac
duration_s: 40.33
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.859259
---

# Render: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-09T13:49:41Z.

## Gates
- lint_video --final: pass (duration 40.33 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.859259)
- Length: 40.33 s; narration 39.44 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 114 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.18 | 6.20 | 1 | glm-5.3-flash |  |
| s02 | 8.76 | 8.77 | 2 | glm-5.3-flash |  |
| s03 | 4.01 | 4.03 | 1 | glm-5.3-flash |  |
| s04 | 7.11 | 7.13 | 1 | glm-5.3-flash |  |
| s05 | 7.68 | 7.70 | 1 | glm-5.3-flash |  |
| s06 | 6.50 | 6.50 | 3 | glm-5.3 |  |

## Assembly
- video total 40.33s vs narration 39.44s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-09-vllm-0-29-sizes-its-own-kv-cac/render/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 43
