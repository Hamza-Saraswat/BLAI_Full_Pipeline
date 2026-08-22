---
name: render-shorts
description: Render a Build Local AI YouTube Short from an approved storyboard and its ElevenLabs narration. Scene workers render each storyboard scene as a HyperFrames (HTML/GSAP) or Manim clip in the video's style pack; assemble.py stitches the clips, narration, word-timed captions and sfx through the Remotion Assembly composition, normalizes loudness and runs the release linters. Use on the DGX Spark render stage, or on any host with Node 22, ffmpeg and Python.
metadata: {tags: "render, shorts, remotion, hyperframes, manim, style-packs, captions, safe-zone, lint"}
---

# render-shorts

Port of the v1 BLAI Animator render stack (Remotion assembly, HyperFrames and Manim scene tooling, seven style packs, release linters) as one bundled skill. Paths below are relative to `skills/render-shorts/`.

## When to Use

- The Shorts render stage: the storyboard passed `script-gates`, `narration.wav` and `captions.json` exist from `elevenlabs-narration`, and the hub note is `building`.
- Re-rendering one scene after a reject with feedback, or re-assembling after scene fixes.
- Picking or recording the style pack for a new storyboard (`scripts/style_rotation.py`).
- Running the release gates on any Short (`scripts/lint_video.py`, `scripts/safe_zone_check.py`).
- Not for long-form episodes (`skills/render-longform`) and not for writing or changing scripts.

## What You Need Before Calling

- Node 22 and ffmpeg/ffprobe on PATH (ffmpeg 8.x verified; any build with `loudnorm`, `signalstats` and `ssim` works).
- `npm install` once in `remotion/` (Remotion 4.0.484, React 19, lockfile pinned) and once in `hyperframes/` (HyperFrames 0.7.31, lockfile pinned).
- Chrome Headless Shell for Remotion: `cd remotion && npx remotion browser ensure` (downloads into `remotion/node_modules/.remotion/`; Linux arm64 is supported). HyperFrames: `cd hyperframes && npx hyperframes doctor` and, if it asks, `npx hyperframes browser ensure`.
- Python 3.12 venv with Manim Community 0.20.1 at `manim/.venv` for Manim scenes (`setup.md`). The scripts in `scripts/` are stdlib-only and run with the system `python3` (3.9 or newer).
- Inputs per video: the storyboard JSON (`shared/schemas/storyboard.schema.json`), `narration.wav` (44.1 or 48 kHz), `captions.json` (`[{word, start, end}]`, seconds), the slug, an output directory.
- No secrets and no paid calls. Network is only needed for the one-time installs and for the GSAP CDN script that HyperFrames scenes load (vendor it if the Spark is offline).

## How It Works

1. Style pack. At storyboard time: `python3 scripts/style_rotation.py --pick --slug <slug> --storyboard <sb.json>` prints the next pack (never the previous one, topic-fit scored); on approval `--record <pack> --slug <slug>` appends to `styles/history.json`, the rotation ledger.
2. Timing. `python3 scripts/scene_timing.py --storyboard sb.json --captions captions.json --out timing.json` maps the narration's word timings onto scenes: `[{scene_id, start_ms, end_ms, duration_s, words}]` (scene 1 starts at 0, the last scene holds 1 s). Each scene worker gets its `duration_s` (tolerance 0.15 s) and its window.
3. Scene fan-out. One worker per scene; `tool` selects HyperFrames (`rules/hyperframes-1.md`, `rules/hyperframes-2.md`) or Manim (`rules/manim-1.md`, `rules/manim-2.md`). Every worker reads `rules/scene-agent.md` and `styles/<pack>.md` first, renders a draft, verifies (ffprobe, three stills, `scripts/safe_zone_check.py <mp4> --scene`, `scripts/lint_video.py <mp4>`), renders final, and copies the clip to `<scenes-dir>/<scene_id>.mp4`. Five attempts, then blocked with the last error.
4. Assembly. `python3 scripts/assemble.py --slug S --storyboard sb.json --audio narration.wav --captions captions.json --scenes-dir DIR --out OUT [--draft]` generates the Remotion props (`OUT/<slug>-props.json`), stages media under `remotion/public/<slug>/`, renders `Assembly` with `--color-space=bt709`, runs `loudnorm` to -14 LUFS, writes `OUT/final.mp4`, then runs `lint_video.py --final` with the format band from `skills/script-gates/formats.json`, `safe_zone_check.py` (8 stills into `OUT/qa/`), `loop_check.mjs`, and saves `OUT/qa/safe-zone.png`. Stdout is one JSON line: `{final, duration_s, lint_ok, safe_zone_ok, loop_ok, loop_ssim, props, music, sfx_cues, caption_words, warnings}`. `--draft` renders at scale 0.25 to `final-draft.mp4` for a fast timing check; `--dry-run` writes the props and prints the plan without rendering.
5. Gates on their own: `python3 scripts/lint_video.py final.mp4 --final [--max-s N --warn-band LO:HI]` (exit 0/1, JSON), `python3 scripts/safe_zone_check.py final.mp4 [--scene] [--stills N] [--debug-dir DIR]` (exit 0/1, JSON), `node remotion/scripts/loop_check.mjs final.mp4` (exit 0 similar, 1 not, 2 error).

## Rules

- `rules/scene-agent.md`: what every scene worker and the editor obeys: inputs, format hard tokens, brand tokens, working rules, hard don'ts, handback.
- `rules/hyperframes-1.md`: HyperFrames composition contract, which vendored skills to load, commands, brand CSS, visual vocabulary, motion boundaries, self-check.
- `rules/hyperframes-2.md`: the seven packs in HyperFrames: what each pack ships and its easing personality, dos and don'ts.
- `rules/manim-1.md`: Manim environment and commands, the API whitelist, scene skeleton, layout discipline, bounded retry.
- `rules/manim-2.md`: `blai_packs` helpers per pack, fonts, per-pack personality, reference scenes.
- `rules/remotion-editor.md`: editorial policy for assembly (order, music, captions, sfx, loop rule, overruns), render mechanics that bite, definition of done.
- `rules/style-packs.md`: pack selection table, the never-twice-in-a-row rule, the rotation script, anti-sameness beyond packs.

## After the Call

- Outputs: `OUT/final.mp4` (binary, gitignored), `OUT/<slug>-props.json` and `timing.json` (text, committed as the audit trail), `OUT/qa/safe-zone.png` and `OUT/qa/safezone_t*.png` (gitignored), scene clips in `<scenes-dir>` (gitignored). `remotion/public/<slug>/` staging is removed after the render unless `--keep-staging`.
- The render stage writes `-render.md` from the summary JSON: duration, loudness, gate results, attempts per scene, sfx and music used, anything flagged, `notes_for_review` echoed; the hub note goes to `review` once `telegram-gate` sends the card. Approval and publishing never happen here.
- Record the pack with `style_rotation.py --record` if the storyboard stage has not.
- Loop-backs (`shared/pipeline-overview.md`): a scene off-cue or a number on screen that is not spoken goes back to the storyboard; a scene that overran its slot goes back to that scene worker; loudness out of band re-runs assembly (two-pass correction is built in); a failed loop check is flagged, not patched.
- Gotchas worth remembering: never pass Manim quality flags; run Manim from `manim/`; `--color-space=bt709` is required in Remotion; `lint_video.py` is deliberately dumb about formats, pass the band; draft renders always fail lint on resolution.
