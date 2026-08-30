---
slug: 2026-08-30-dgx-spark-has-128-gb-and-a-70b
duration_s: 110.23
lint_ok: true
safe_zone_ok: true
loop_ok: true
loop_ssim: 0.948906
scenes: 9
attempts: 16
---

# Render: 2026-08-30-dgx-spark-has-128-gb-and-a-70b

## Gates

| Gate | Result |
|------|--------|
| lint_video.py --final (band smooth-explainer, warn 70-155 s) | PASS, 0 violations, 0 warnings |
| safe_zone_check.py (8 stills) | PASS, 0 violations |
| loop_check.mjs | PASS, SSIM 0.948906 (threshold 0.5) |
| Length | 110.23 s, inside the 70-155 s warn band |
| Scenes in cut | 9 of 9 storyboard scenes rendered and assembled in order |
| Loudness | normalized to about -14 LUFS by assemble.py |
| Captions | 373 words, 97 cues, whisper timing |

Warning carried: video total 110.23 s vs narration 109.16 s (1.07 s of segment slack; assemble.py: "segments win"). Music: none. SFX cues: none (the storyboard carried none).

## Scene timings and attempts

| Scene | Tool | Target s | Final s | Attempts | Notes |
|-------|------|----------|---------|----------|-------|
| s1 hook | hyperframes | 8.02 | 8.02 | 2 | attempt 1: ARM64 browser discovery (HYPERFRAMES_BROWSER_PATH not propagated); attempt 2 green |
| s2 | hyperframes | 10.46 | 10.50 | 1 | clean first pass |
| s3 | hyperframes | 7.59 | 7.60 | 2 | content_overlap on the 803/tok-s stack, separated |
| s4 | manim | 14.13 | 14.127 | 2 | draft+final, both clean |
| s5 | hyperframes | 11.83 | 11.83 | 2 | same ARM64 browser discovery, inline path fix |
| s6 | manim | 14.58 | 14.58 | 3 | fraction width and 64 px floor fixes |
| s7 | hyperframes | 17.84 | 17.833 | 4 | duration trims to delta 0.007 s |
| s8 | hyperframes | 15.63 | 15.63 | 2 | content_overlap tag-vs-SVG-layer fix |
| s9 payoff_close | hyperframes | 10.08 | 10.10 | 1 | loop anchor measured from s1 frame 1, SSIM 0.949 |

16 attempts across 9 scenes (cap 5 each). Every scene passed safe_zone_check --scene --stills 9 and lint_video scene mode; hyperframes scenes also passed lint, validate and inspect --samples 40 --at-transitions --strict.

## notes_for_review (from the storyboard)

Working values for title/description/hashtags; stage 05 overwrites. Draft B (myth-bust, wrong-diagnosis hook). Scene 6 derives "about seventy gigabytes" and "under four tokens a second" from claim 5 without quoting the 3.9 row verbatim; scene 8's two-hundred-billion is claim 3 (NVIDIA advertising), not a key-number row. hook_text trimmed to six words for the schema.

## Gate card

- send_card.py --kind gate: attempted; result recorded in the hub note Build journal and this run's final report.
