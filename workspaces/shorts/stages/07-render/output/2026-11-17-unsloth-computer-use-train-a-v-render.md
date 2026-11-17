---
slug: 2026-11-17-unsloth-computer-use-train-a-v
duration_s: 100.50
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.711387
---

# Render: 2026-11-17-unsloth-computer-use-train-a-v

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-17T14:07:25Z.

## Gates
- lint_video --final: pass (duration 100.50 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.711387)
- Length: 100.50 s; narration 99.68 s
- Scenes: 11/11 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11)
- Captions: 320 words; sfx cues whoosh, tick, ding, ding, ding, pop; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 9.92 | 9.93 | 2 | glm-5.3-flash |  |
| s02 | 9.68 | 9.70 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s03 | 9.50 | 9.50 | 4 | glm-5.3 |  |
| s04 | 9.06 | 9.07 | 4 | glm-5.3 |  |
| s05 | 12.20 | 12.20 | 5 | glm-5.3 |  |
| s06 | 11.74 | 11.73 | 4 | glm-5.3 |  |
| s07 | 7.17 | 7.16 | 4 | glm-5.3 |  |
| s08 | 5.83 | 5.83 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s09 | 6.33 | 6.33 | 5 | glm-5.3 | motion inside the last 0.5s (rule 10 stillness) |
| s10 | 10.66 | 10.67 | 2 | glm-5.3-flash |  |
| s11 | 8.35 | 8.37 | 2 | glm-5.3-flash |  |

## Assembly
- video total 100.50s vs narration 99.68s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-17-unsloth-computer-use-train-a-v/render/2026-11-17-unsloth-computer-use-train-a-v-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 363
