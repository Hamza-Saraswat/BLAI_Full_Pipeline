---
name: render-longform
description: Render a BLAI long-form episode (1920x1080, 30 fps, H.264) from a long-form spec JSON with a Remotion 4 scene library; also renders the three thumbnails, the captions.srt sidecar, chapter times and a lint report.
metadata:
  tags: "remotion, long-form, render, thumbnails, lint, captions, dgx-spark"
---

# render-longform

Compiles `<slug>-spec.json` (shared/schemas/longform-spec.schema.json) into a 1920x1080 episode with the Remotion project in `remotion/`. The spec says what each scene shows and says; this skill decides how it moves.

## When to Use

- The render stage of `workspaces/long-form` (Spark side): the spec, `narration.wav` and `captions.json` exist and the hub note is `building`.
- A re-render after the reconcile step rewrote a narration line, or after a Telegram `rerender:` tap.
- A quick timing check before a full render: `--draft` gives a 640x360 preview of the first 30 seconds in well under a minute.

## What You Need Before Calling

- `<slug>-spec.json` that validates against the schema: at least 8 scenes, 3 chapters, exactly 3 thumbnail concepts, scene types from `rules/scene-library.md`.
- `narration.wav` (44.1 or 48 kHz) and `captions.json` (`[{word, start, end}]`, seconds) from `skills/elevenlabs-narration`. A `captions.srt` next to it is copied through when present, else generated.
- Optional: the capture directory from `skills/dgx-capture` (`capture.json` plus `<id>.cast`) for `terminal-replay` scenes; b-roll clips next to the spec at the path in `data.src` (or pass `--assets DIR`).
- `remotion/node_modules` installed and the headless browser present (`setup.md`); `ffmpeg`, `ffprobe`, Node 22 and Python 3.9+ on PATH.

## How It Works

1. `scripts/render_longform.py --spec S.json --audio narration.wav --captions captions.json [--captures DIR] --out OUT [--draft]` validates the spec (jsonschema when installed, the minimal checks always), copies the audio and every b-roll clip into `remotion/public/<slug>/`, inlines the captures and writes `OUT/props-episode.json`.
2. `node remotion/scripts/layout.mjs` computes the scene timeline from the captions with the rules in `rules/spec-to-composition.md` and writes `OUT/layout.json`, `OUT/chapters.json` and `OUT/chapters.txt` (the `00:00 Label` lines for the description).
3. `npx remotion render src/index.ts Episode` renders the episode. Full renders go through a two-pass `loudnorm` to -14 LUFS and land in `OUT/final.mp4`. `--draft` renders 640x360, crf 35, the first 900 frames, and skips the lint.
4. `npx remotion still src/index.ts Thumbnail` renders `OUT/thumbnails/1.png`, `2.png`, `3.png` from `thumbnail_concepts` (`rules/thumbnails.md`); a `.jpg` is added next to any PNG over 2 MB.
5. `OUT/captions.srt` is copied or generated; `scripts/lint_longform.py OUT/final.mp4 --target-s N --chapters OUT/chapters.json` checks resolution, fps, codec, pixel format, loudness, duration and chapters and prints a JSON report.
6. `OUT/render.json` records inputs, per-scene timings, warnings, output probe and the lint result. Exit 1 on a validation error, a failed render or a failed lint. `--dry-run` validates, writes props and layout, prints the commands and renders nothing.

```
python3 skills/render-longform/scripts/render_longform.py --spec S.json --audio narration.wav \
  --captions captions.json --captures CAPTURE_DIR --out OUT --draft
python3 skills/render-longform/scripts/lint_longform.py OUT/final.mp4 --target-s 600 --chapters OUT/chapters.json
```

## Rules

- `rules/scene-library.md`: the 13 scene types, when to use each, what `data` must carry, what a muted viewer understands, duration guidance.
- `rules/spec-to-composition.md`: how the spec becomes a composition, the timing rules, sync points, lower thirds and captions, what the spec must never contain.
- `rules/thumbnails.md`: how a concept becomes three variants, the 4-word limit, export and size rules.

## After the Call

- Deliverables in `OUT/`: `final.mp4`, `thumbnails/1.png 2.png 3.png`, `captions.srt`, `chapters.txt`, `render.json`.
- Write `stages/<render-stage>/output/<slug>-render.md` from `render.json` (timings, warnings, lint), then send the review card with `skills/telegram-gate`.
- A failed lint, a missing capture or a scene that fell back to `est_duration_s` is fixed upstream (spec, audio, capture), not by editing the renderer. Regenerating audio recomputes every scene duration (`shared/pipeline-overview.md`).
- `remotion/public/<slug>/` keeps the copied media for re-renders and Studio previews (`npx remotion studio src/index.ts` in `remotion/`, then load `OUT/props-episode.json`); pass `--clean-public` to delete it after a successful render.
