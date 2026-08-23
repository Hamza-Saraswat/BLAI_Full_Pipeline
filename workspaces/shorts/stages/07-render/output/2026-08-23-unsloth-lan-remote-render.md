---
slug: 2026-08-23-unsloth-lan-remote
workspace: shorts
stage: 07-render
lint_pass: true
---

# Render: Unsloth ships LAN access (myth-bust, smooth-explainer)

**LOCAL TEST RENDER.** Voiced by Kokoro `am_eric`, not the ElevenLabs clone. Not publishable as-is.

## Output

| | |
|---|---|
| File | `.local-builds/2026-08-23-unsloth-lan-remote/out/final.mp4` |
| Duration | **74.50 s** (smooth-explainer warn band 70-155 s, max 180 s) |
| Video | 1080x1920, h264, yuv420p, 30 fps |
| Audio | aac 48 kHz, **-14.1 LUFS** measured |
| Size | 5.2 MB |
| Captions | 279 words, word-timed, burned in |
| Music | none (deliberate manual step) |
| SFX | none requested by the storyboard |

## Gates -- all pass

| Gate | Result |
|---|---|
| `lint_video.py --final` | **PASS** -- 0 violations, 0 warnings |
| `safe_zone_check.py` | **PASS** -- 0 violations |
| `loop_check.mjs` | **PASS** -- SSIM **0.7912** against a 0.5 threshold |

## Scenes

| Scene | Tool | Assigned | Rendered | Delta | Attempts |
|---|---|---|---|---|---|
| s1 | hyperframes | 6.64 s | 6.633 s | -0.007 | 3 |
| s2 | manim | 8.68 s | 8.667 s | -0.013 | 2 |
| s3 | hyperframes | 7.26 s | 7.267 s | +0.007 | 3 |
| s4 | hyperframes | 8.46 s | 8.467 s | +0.007 | 3 |
| s5 | manim | 9.92 s | 9.933 s | +0.013 | 3 |
| s6 | hyperframes | 5.32 s | 5.333 s | +0.013 | 4 |
| s7 | manim | 11.92 s | 11.933 s | +0.013 | 1 |
| s8 | manim | 7.36 s | 7.367 s | +0.007 | 2 |
| s9 | hyperframes | 8.88 s | 8.900 s | +0.020 | 3 |

Nine scenes, 24 render attempts, none hit the 5-attempt limit. Every scene inside +/-0.15 s; worst is s9 at +0.020 s. s7 -- the longest scene in either Short at 11.93 s -- landed first try.

## Audit

| Check | Result |
|---|---|
| Linters | PASS (both) |
| Length | PASS -- 74.50 s, inside the 70-155 s warn band |
| Scenes | PASS -- all 9 rendered, present and in order |
| Frame 1 | PASS -- the amber hook is fully legible at frame 1 inside the terminal window; motion onset at frame 9 (t = 0.300 s) |
| Numbers | PASS -- `3 SETTINGS` and `1 PASSWORD` are spoken in the same beat ("three settings, one password"); digits on screen, spoken form in narration, per the brand rule |

## Verify

Scene narration heard in the cut matches the storyboard exactly; no scene added or dropped.

## Assembly warning (expected)

```
video total 74.50s vs narration 73.53s (segments win; check scene durations)
```

The documented 1 s hold on the last scene, same as the Ornith cut.

## This Short exercised the `terminal` pack for the first time

The two pilot scenes ran on `signal`. Nine scenes on `terminal` surfaced findings 58, 59 and 60 -- the pack's `.term-text` and `.label` classes ship below the brand's minimum text height, `.cursor` silently beats `.accent` on cascade order, `data-layout-allow-occlusion` has to sit on the occluded text rather than the coverer, and `styles/terminal.md` names a scramble-decode technique the pack ships no implementation of.

The pack itself is sound: `terminal-snippet.html` copies across unmodified, the self-hosted JetBrains Mono resolves with no CDN and no tofu on box-drawing or check glyphs, and the pack's mechanical personality (hard cuts, typewriters, no soft fades) sidesteps the masked-text audit trap entirely. The governing constraint is width, not style: at the 64 px type floor a monospace line holds about 19 characters across the 830 px safe box, which is what forced two-line wrapping in five of the nine scenes.

## Loop anchor

s9's worker measured s1's rendered frame 1 rather than working from the brief, and put its closing headline on the same y-centre (704 px) the hook occupied. It deliberately did **not** copy s1's terminal window frame -- the storyboard never specified one, the s1 worker added it, and reproducing it would have pushed the payoff lines into the caption band. Scene-level SSIM 0.8736; the assembled cut scores 0.7912.
