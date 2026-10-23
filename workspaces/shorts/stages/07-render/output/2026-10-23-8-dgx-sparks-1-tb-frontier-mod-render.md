---
slug: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod
duration_s: 36.10
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.872918
---

# Render: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-23T12:31:27Z.

## Gates
- lint_video --final: pass (duration 36.10 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.872918)
- Length: 36.10 s; narration 34.96 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 107 words; sfx cues ding, pop, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.16 | 6.17 | 2 | glm-5.3-flash |  |
| s02 | 8.42 | 8.43 | 4 | glm-5.3 |  |
| s03 | 6.61 | 6.63 | 2 | glm-5.3-flash |  |
| s04 | 8.51 | 8.53 | 2 | glm-5.3-flash |  |
| s05 | 6.26 | 6.27 | 3 | glm-5.3 |  |

## Assembly
- video total 36.03s vs narration 34.96s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-23-8-dgx-sparks-1-tb-frontier-mod/render/2026-10-23-8-dgx-sparks-1-tb-frontier-mod-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 265
