---
slug: 2026-08-23-ornith-1-5-9b
workspace: shorts
stage: 07-render
lint_pass: true
---

# Render: Ornith 1.5 9B: 5.63 GB, real bugs

**LOCAL TEST RENDER.** Voiced by Kokoro `am_eric`, not the ElevenLabs clone. Not publishable as-is.

## Output

| | |
|---|---|
| File | `.local-builds/2026-08-23-ornith-1-5-9b/out/final.mp4` |
| Duration | **30.13 s** (classic band 28-60 s, warn band 28-47 s) |
| Video | 1080x1920, h264, yuv420p, 30 fps |
| Audio | aac 48 kHz, **-14.0 LUFS** measured (target -14) |
| Size | 3.2 MB |
| Captions | 101 words, word-timed, burned in |
| Music | none -- `assets/music/` is a deliberate manual step; the pipeline renders silent rather than pick a wrong mood |
| SFX | 2 cues fired: `pop` @ 510 ms, `tick` @ 13,040 ms |

## Gates -- all pass

| Gate | Result |
|---|---|
| `lint_video.py --final` | **PASS** -- 0 violations, 0 warnings |
| `safe_zone_check.py` (8 stills) | **PASS** -- 0 violations |
| `loop_check.mjs` | **PASS** -- SSIM **0.9558** against a 0.5 threshold |

## Scenes

| Scene | Tool | Assigned | Rendered | Delta | Attempts |
|---|---|---|---|---|---|
| s1 | hyperframes | 3.16 s | 3.167 s | +0.007 | 2 |
| s2 | hyperframes | 3.41 s | 3.400 s | -0.010 | 2 |
| s3 | hyperframes | 4.47 s | 4.500 s | +0.030 | 3 |
| s4 | manim | 6.96 s | 6.966 s | +0.006 | 2 |
| s5 | manim | 5.89 s | 5.900 s | +0.010 | 2 |
| s6 | hyperframes | 6.20 s | 6.200 s | +0.000 | 4 |

Six scenes, 15 render attempts total, no scene hit the 5-attempt limit. Every scene inside the +/-0.15 s tolerance; worst is s3 at +0.030 s. Total compute across all six scenes was **under two minutes**; the wall-clock cost was reading rule files and working around findings 51-55.

## Audit

| Check | Result |
|---|---|
| Linters | PASS (both, above) |
| Length | PASS -- 30.13 s, inside the 28-47 s warn band |
| Scenes | PASS -- all 6 storyboard scenes rendered and present in the cut, in order |
| Frame 1 | PASS -- the amber `5.63 GB` and the file glyph are fully legible at frame 1, first motion at frame 10 (t = 0.333 s), inside the 0.5 s requirement |
| Numbers | PASS with one flagged exception, below |

## Verify

Scene narration heard in the cut matches the storyboard exactly; no scene added or dropped.

## One assembly warning, and it is honest

```
video total 30.13s vs narration 29.09s (segments win; check scene durations)
```

The scenes sum to 30.13 s against 29.09 s of narration, a 1.04 s overhang. That is `scene_timing.py` giving the last scene its documented 1 s hold, so it is expected rather than drift -- but the warning is worth keeping, because a real overrun would look identical.

## A rule conflict worth deciding (new)

**The loop-anchor rule and the numbers rule contradict each other on the final scene of every Short.**

`scene-agent.md` requires the last frame to rhyme with frame 1 (the loop anchor, checked by `loop_check.mjs`). It separately requires that every number on screen is spoken in the same beat. Frame 1 of a Short is usually a giant number -- here `5.63 GB` -- so honouring the loop anchor necessarily puts an unspoken number on the last frame.

s6's worker flagged exactly this: its final frame carries `5.63 GB` (spoken in s1) and its opening carries `70.6` (spoken in s4). Both are deliberate recalls, both are correct choices, and both technically breach the numbers rule. The storyboard's own `notes_for_review` warns about unspoken on-screen numbers, so the tension is already half-noticed.

Recommended resolution: exempt the loop anchor and deliberate recalls from the numbers rule explicitly, rather than leaving each scene worker to decide. It is a one-line change to `scene-agent.md`.

## Defects found

None in the assembled cut. The three defects this render surfaced were all in the rule files rather than the output -- findings 51 to 55, now corrected in the worker briefing.

## Loop anchor, measured

s6's worker did not eyeball the rhyme. It measured s1's frame-1 bounding boxes pixel-wise (cream glyph x 113-248 / y 564-739, amber figure x 306-896 / y 578-726) and rebuilt the composition to land within 1-2 px on every edge. `loop_check.mjs` scored its scene 0.9826; the assembled cut scores 0.9558 with the wordmark added.
