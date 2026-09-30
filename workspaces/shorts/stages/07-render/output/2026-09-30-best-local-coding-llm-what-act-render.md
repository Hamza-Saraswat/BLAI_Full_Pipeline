---
slug: 2026-09-30-best-local-coding-llm-what-act
duration_s: 110.90
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.707061
---

# Render: 2026-09-30-best-local-coding-llm-what-act

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-30T13:25:34Z.

## Gates
- lint_video --final: pass (duration 110.90 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.707061)
- Length: 110.90 s; narration 108.92 s
- Scenes: 11/11 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11)
- Captions: 341 words; sfx cues pop, ding, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 10.44 | 10.47 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s2 | 13.16 | 13.17 | 5 | glm-5.3 |  |
| s3 | 7.08 | 7.10 | 2 | glm-5.3-flash |  |
| s4 | 8.44 | 8.47 | 4 | glm-5.3 |  |
| s5 | 14.81 | 14.83 | 4 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s6 | 12.27 | 12.30 | 3 | glm-5.3 |  |
| s7 | 8.63 | 8.63 | 4 | glm-5.3 |  |
| s8 | 6.63 | 6.63 | 3 | glm-5.3 |  |
| s9 | 9.19 | 9.20 | 3 | glm-5.3 |  |
| s10 | 6.91 | 6.93 | 2 | glm-5.3-flash |  |
| s11 | 13.03 | 13.03 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |

## Assembly
- video total 110.77s vs narration 108.92s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-30-best-local-coding-llm-what-act/render/2026-09-30-best-local-coding-llm-what-act-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 151
