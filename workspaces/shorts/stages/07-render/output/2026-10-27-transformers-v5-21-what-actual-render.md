---
slug: 2026-10-27-transformers-v5-21-what-actual
duration_s: 42.13
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.865528
---

# Render: 2026-10-27-transformers-v5-21-what-actual

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-27T13:00:47Z.

## Gates
- lint_video --final: pass (duration 42.13 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.865528)
- Length: 42.13 s; narration 41.28 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 123 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.38 | 6.40 | 3 | glm-5.3 |  |
| s02 | 8.18 | 8.20 | 2 | glm-5.3-flash |  |
| s03 | 8.56 | 8.57 | 3 | glm-5.3 |  |
| s04 | 7.11 | 7.13 | 1 | glm-5.3-flash |  |
| s05 | 6.11 | 6.13 | 1 | glm-5.3-flash |  |
| s06 | 5.70 | 5.70 | 1 | glm-5.3-flash |  |

## Assembly
- video total 42.13s vs narration 41.28s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-27-transformers-v5-21-what-actual/render/2026-10-27-transformers-v5-21-what-actual-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 282
