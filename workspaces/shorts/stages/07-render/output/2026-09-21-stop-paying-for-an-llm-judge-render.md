---
slug: 2026-09-21-stop-paying-for-an-llm-judge
duration_s: 119.53
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.924902
---

# Render: 2026-09-21-stop-paying-for-an-llm-judge

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-21T13:14:02Z.

## Gates
- lint_video --final: pass (duration 119.53 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.924902)
- Length: 119.53 s; narration 118.48 s
- Scenes: 11/11 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11)
- Captions: 385 words; sfx cues pop, type, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 8.97 | 9.00 | 1 | glm-5.3-flash |  |
| s2 | 12.64 | 12.67 | 2 | glm-5.3-flash |  |
| s3 | 8.78 | 8.76 | 3 | glm-5.3 |  |
| s4 | 13.47 | 13.47 | 3 | glm-5.3 |  |
| s5 | 9.55 | 9.57 | 1 | glm-5.3-flash |  |
| s6 | 14.03 | 14.03 | 3 | glm-5.3 |  |
| s7 | 11.60 | 11.60 | 1 | glm-5.3-flash |  |
| s8 | 12.77 | 12.80 | 5 | glm-5.3 |  |
| s9 | 7.34 | 7.37 | 3 | glm-5.3 |  |
| s10 | 10.05 | 10.07 | 2 | glm-5.3-flash |  |
| s11 | 10.20 | 10.20 | 3 | glm-5.3 |  |

## Assembly
- video total 119.53s vs narration 118.48s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-21-stop-paying-for-an-llm-judge/render/2026-09-21-stop-paying-for-an-llm-judge-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 103
