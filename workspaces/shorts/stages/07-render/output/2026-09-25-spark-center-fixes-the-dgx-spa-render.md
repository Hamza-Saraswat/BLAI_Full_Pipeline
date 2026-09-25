---
slug: 2026-09-25-spark-center-fixes-the-dgx-spa
duration_s: 41.90
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.894306
---

# Render: 2026-09-25-spark-center-fixes-the-dgx-spa

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-25T12:39:05Z.

## Gates
- lint_video --final: pass (duration 41.90 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.894306)
- Length: 41.90 s; narration 40.84 s
- Scenes: 7/7 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7)
- Captions: 111 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.56 | 6.57 | 4 | glm-5.3 |  |
| s2 | 4.58 | 4.57 | 3 | glm-5.3 |  |
| s3 | 6.98 | 7.00 | 3 | glm-5.3 |  |
| s4 | 6.16 | 6.17 | 3 | glm-5.3 |  |
| s5 | 7.20 | 7.20 | 4 | glm-5.3 |  |
| s6 | 5.38 | 5.40 | 3 | glm-5.3 |  |
| s7 | 4.98 | 5.00 | 2 | glm-5.3-flash |  |

## Assembly
- video total 41.90s vs narration 40.84s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-25-spark-center-fixes-the-dgx-spa/render/2026-09-25-spark-center-fixes-the-dgx-spa-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 126
