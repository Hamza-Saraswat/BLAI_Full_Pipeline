---
slug: 2026-09-06-dgx-spark-firmware-week-two-cv
duration_s: 46.70
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.899864
---

# Render: 2026-09-06-dgx-spark-firmware-week-two-cv

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-06T21:22:44Z.

## Gates
- lint_video --final: pass (duration 46.70 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.899864)
- Length: 46.70 s; narration 45.80 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 137 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.12 | 5.13 | 4 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s02 | 8.37 | 8.37 | 5 | glm-5.3 |  |
| s03 | 9.55 | 9.53 | 4 | glm-5.3 |  |
| s04 | 6.96 | 6.97 | 4 | glm-5.3 |  |
| s05 | 11.28 | 11.30 | 5 | glm-5.3 |  |
| s06 | 5.40 | 5.40 | 1 | glm-5.3-flash |  |

## Assembly
- video total 46.70s vs narration 45.80s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-06-dgx-spark-firmware-week-two-cv/render/2026-09-06-dgx-spark-firmware-week-two-cv-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 24
