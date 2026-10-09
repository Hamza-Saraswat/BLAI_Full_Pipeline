---
slug: 2026-10-09-ecosia-ditched-mistral-for-chi
duration_s: 37.97
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.786231
---

# Render: 2026-10-09-ecosia-ditched-mistral-for-chi

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-09T12:54:49Z.

## Gates
- lint_video --final: pass (duration 37.97 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.786231)
- Length: 37.97 s; narration 37.12 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 101 words; sfx cues type, ding, pop; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.44 | 5.47 | 4 | glm-5.3 |  |
| s02 | 6.08 | 6.10 | 3 | glm-5.3 |  |
| s03 | 12.33 | 12.33 | 4 | glm-5.3 |  |
| s04 | 6.81 | 6.83 | 4 | glm-5.3 |  |
| s05 | 7.22 | 7.23 | 5 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |

## Assembly
- video total 37.97s vs narration 37.12s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-09-ecosia-ditched-mistral-for-chi/render/2026-10-09-ecosia-ditched-mistral-for-chi-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 193
