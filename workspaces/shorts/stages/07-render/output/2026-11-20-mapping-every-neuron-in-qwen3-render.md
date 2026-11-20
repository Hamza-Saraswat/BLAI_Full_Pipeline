---
slug: 2026-11-20-mapping-every-neuron-in-qwen3
duration_s: 105.93
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.881256
---

# Render: 2026-11-20-mapping-every-neuron-in-qwen3

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-20T13:52:17Z.

## Gates
- lint_video --final: pass (duration 105.93 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.881256)
- Length: 105.93 s; narration 105.00 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 339 words; sfx cues whoosh, tick, pop, tick, tick; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 9.36 | 9.37 | 2 | glm-5.3-flash |  |
| s02 | 12.62 | 12.63 | 2 | glm-5.3-flash |  |
| s03 | 9.14 | 9.17 | 2 | glm-5.3-flash |  |
| s04 | 13.05 | 13.07 | 2 | glm-5.3-flash |  |
| s05 | 14.11 | 14.13 | 3 | glm-5.3 |  |
| s06 | 10.40 | 10.40 | 2 | glm-5.3-flash |  |
| s07 | 6.94 | 6.97 | 1 | glm-5.3-flash |  |
| s08 | 11.12 | 11.13 | 3 | glm-5.3 |  |
| s09 | 11.26 | 11.27 | 2 | glm-5.3-flash |  |
| s10 | 7.80 | 7.80 | 2 | glm-5.3-flash |  |

## Assembly
- video total 105.93s vs narration 105.00s (segments win; check scene durations)
- sfx pop at 68417 ms dropped: within 1000 ms of the previous cue
- props: /home/buildlocalai/blai/builds/2026-11-20-mapping-every-neuron-in-qwen3/render/2026-11-20-mapping-every-neuron-in-qwen3-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 374
