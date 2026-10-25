---
slug: 2026-10-25-ollama-v0-40-11-is-it-worth-re
duration_s: 40.20
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.884403
---

# Render: 2026-10-25-ollama-v0-40-11-is-it-worth-re

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-25T12:50:53Z.

## Gates
- lint_video --final: pass (duration 40.20 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.884403)
- Length: 40.20 s; narration 39.12 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 121 words; sfx cues type, ding, pop, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.68 | 5.70 | 4 | glm-5.3 |  |
| s02 | 5.65 | 5.67 | 2 | glm-5.3-flash |  |
| s03 | 7.59 | 7.60 | 2 | glm-5.3-flash |  |
| s04 | 7.29 | 7.30 | 1 | glm-5.3-flash |  |
| s05 | 7.64 | 7.67 | 3 | glm-5.3 |  |
| s06 | 6.19 | 6.20 | 1 | glm-5.3-flash |  |

## Assembly
- video total 40.13s vs narration 39.12s (segments win; check scene durations)
- sfx tick at 26267 ms dropped: within 1000 ms of the previous cue
- props: /home/buildlocalai/blai/builds/2026-10-25-ollama-v0-40-11-is-it-worth-re/render/2026-10-25-ollama-v0-40-11-is-it-worth-re-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 272
