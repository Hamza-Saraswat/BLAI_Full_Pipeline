---
slug: 2026-09-29-the-dgx-spark-handbook-every-s
duration_s: 39.17
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.899434
---

# Render: 2026-09-29-the-dgx-spark-handbook-every-s

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-29T12:40:25Z.

## Gates
- lint_video --final: pass (duration 39.17 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.899434)
- Length: 39.17 s; narration 38.44 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 113 words; sfx cues whoosh, pop; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.34 | 6.37 | 2 | glm-5.3-flash |  |
| s02 | 6.32 | 6.33 | 1 | glm-5.3-flash |  |
| s03 | 5.55 | 5.53 | 5 | glm-5.3 |  |
| s04 | 6.87 | 6.90 | 1 | glm-5.3-flash |  |
| s05 | 8.18 | 8.20 | 5 | glm-5.3 |  |
| s06 | 5.82 | 5.83 | 3 | glm-5.3 |  |

## Assembly
- video total 39.17s vs narration 38.44s (segments win; check scene durations)
- sfx ding at 160 ms dropped: within 1000 ms of the previous cue
- props: /home/buildlocalai/blai/builds/2026-09-29-the-dgx-spark-handbook-every-s/render/2026-09-29-the-dgx-spark-handbook-every-s-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 144
