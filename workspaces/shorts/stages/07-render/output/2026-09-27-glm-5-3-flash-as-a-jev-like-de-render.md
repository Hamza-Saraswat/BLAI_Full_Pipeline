---
slug: 2026-09-27-glm-5-3-flash-as-a-jev-like-de
duration_s: 103.17
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.877471
---

# Render: 2026-09-27-glm-5-3-flash-as-a-jev-like-de

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-27T13:23:11Z.

## Gates
- lint_video --final: pass (duration 103.17 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.877471)
- Length: 103.17 s; narration 100.76 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 299 words; sfx cues tick, ding, ding, pop; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 7.86 | 7.87 | 1 | glm-5.3-flash |  |
| s02 | 9.54 | 9.57 | 3 | glm-5.3 |  |
| s03 | 11.37 | 11.40 | 2 | glm-5.3-flash |  |
| s04 | 7.73 | 7.73 | 4 | glm-5.3 |  |
| s05 | 8.63 | 8.63 | 1 | glm-5.3-flash |  |
| s06 | 11.45 | 11.47 | 5 | glm-5.3 |  |
| s07 | 9.26 | 9.27 | 3 | glm-5.3 |  |
| s08 | 12.14 | 12.17 | 1 | glm-5.3-flash |  |
| s09 | 13.36 | 13.37 | 5 | glm-5.3 |  |
| s10 | 11.71 | 11.70 | 3 | glm-5.3 |  |

## Assembly
- video total 103.17s vs narration 100.76s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-27-glm-5-3-flash-as-a-jev-like-de/render/2026-09-27-glm-5-3-flash-as-a-jev-like-de-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 138
