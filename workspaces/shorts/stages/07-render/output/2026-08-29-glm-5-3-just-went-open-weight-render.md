---
slug: 2026-08-29-glm-5-3-just-went-open-weight
workspace: shorts
stage: 07-render
lint_pass: true
---

# Render: GLM-5.3-Flash: the 93 GB "small" build

**LOCAL TEST RENDER** (proof run of the shorts-only rebuild). Kokoro voice; not publishable as-is.

## Output

| | |
|---|---|
| File | `.local-builds/2026-08-29-glm-5-3-just-went-open-weight/out/final.mp4` |
| Duration | **39.13 s** (classic warn band 28-47) |
| Video | 1080x1920, h264, yuv420p, 30 fps |
| Audio | aac 48 kHz, **-14.1 LUFS** |
| Size | 4.2 MB |
| Captions | 133 words burned in |
| Music | none (manual step by design) |
| SFX | tick @0.03s, pop @8.86s, tick @22.17s |

## Gates -- all pass

| Gate | Result |
|---|---|
| `lint_video.py --final` | PASS, 0/0 |
| `safe_zone_check.py` | PASS, 0 violations |
| `loop_check.mjs` | PASS, SSIM **0.9551** (scene-level anchor measured 0.9878, pixel-identical amber boxes) |

## Scenes

| Scene | Tool | Assigned | Rendered | Delta | Attempts |
|---|---|---|---|---|---|
| s1 | hyperframes | 2.38 | 2.400 | +0.020 | 1 |
| s2 | hyperframes | 3.38 | 3.400 | +0.020 | 2 |
| s3 | manim | 4.85 | 4.866 | +0.016 | 1 |
| s4 | manim | 6.35 | 6.366 | +0.016 | 2 |
| s5 | manim | 7.48 | 7.467 | -0.013 | 2 |
| s6 | hyperframes | 9.36 | 9.367 | +0.007 | 1 (after a wedged first worker was stopped and respawned) |
| s7 | hyperframes | 5.26 | 5.267 | +0.007 | 2 |

First live use of the **silicon** pack: sound overall; defect list (chip() label sizing, pin-stub
overhang, the 1.15-scale drop vs the safe box, snippet root/selector traps) folded into the pack
files and recorded for the findings log. One worker wedged before writing anything and was stopped
and respawned; the respawn published in 1 attempt.

## Verify

Scene narration heard in the cut matches the storyboard; 7 scenes present in order; the assembly
warning (39.13 s video vs 38.06 s narration) is the documented last-scene hold.
