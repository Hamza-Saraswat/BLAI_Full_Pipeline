---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
duration_s: 41.23
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.838226
---

# Render: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-05T22:44:58Z.

## Gates
- lint_video --final: pass (duration 41.23 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.838226)
- Length: 41.23 s; narration 40.24 s
- Scenes: 5/6 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 112 words; sfx cues pop, ding, tick; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 7.51 | 7.53 | 2 | glm-5.3-flash |  |
| s02 | 7.35 | 7.37 | 2 | glm-5.3-flash |  |
| s03 | 7.00 | 7.00 | 2 | glm-5.3-flash |  |
| s04 | 5.85 | 5.87 | 2 | glm-5.3-flash |  |
| s05 | 9.11 | 9.13 | 1 | glm-5.3-flash |  |
| s06 | 4.20 | 0.00 |  |  |  |

## Assembly
- video total 41.23s vs narration 40.24s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-02-dgx-spark-runs-qwen3-8-flash-n/render/2026-09-02-dgx-spark-runs-qwen3-8-flash-n-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 13
