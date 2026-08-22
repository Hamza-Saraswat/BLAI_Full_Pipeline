# Spec to Composition

How `<slug>-spec.json` becomes the `Episode` composition, and the line between what the spec decides and what the renderer decides.

## The path

1. `scripts/render_longform.py` validates the spec, stages media under `remotion/public/<slug>/`, inlines captures and writes `props-episode.json`: `{spec, captions, audioSrc, captures, assetsBase}`.
2. `Episode`'s `calculateMetadata` probes the narration audio, runs `computeLayout` (`remotion/src/timing.mjs`) and probes every b-roll clip. The same `timing.mjs` runs under Node through `remotion/scripts/layout.mjs` so `chapters.json` and `render.json` carry exactly the timings the video has.
3. Each scene becomes one `<Sequence from durationInFrames>` wrapping its component (`remotion/src/scenes/index.ts` maps `type` to component). The narration plays from frame 0 as one `<Audio>`.

## Timing rules

1. Without captions every scene lasts its `est_duration_s`, in order.
2. With captions a scene starts where its narration starts: the first 3 (then 2, then 1) words of `narration` are searched in `captions.json` from the previous scene's last matched word forward, lowercase, punctuation stripped, prefix-tolerant (`quantized` matches `quantized,`). The last words are matched the same way near the expected position.
3. Scenes are contiguous: a scene ends where the next one starts, so no frame is empty and nothing overlaps. A scene that did not match shares the gap up to the next matched scene with its unmatched neighbours in proportion to their `est_duration_s`.
4. The last scene runs to the end of the audio plus 0.75 s; the end card lasts at least 8 s.
5. Matched or not is recorded per scene in `layout.json` (`matched`). Fewer than half matched is a warning in `render.json`: the narration text and the captions came from different scripts.
6. Chapter times are the start of `starts_at_scene`. The first chapter must start at the first scene (YouTube wants 00:00).

## Sync points

`sync_points: [{phrase, event}]` resolve to the time the phrase is first spoken inside the scene (first 3, 2 or 1 words). Unresolved events fall back to the automatic timing, so a sync point can never break a render.

| Scene type | Events |
|------------|--------|
| `kinetic-text` | `line:<n>` starts line n (1-based); lines whose first words match the narration lock on their own |
| `code-typing` | `type` starts typing |
| `terminal-replay` | `run` starts the playback (the command is typed before it) |
| `diagram` | `node:<id>` reveals that node; its incoming arrows follow |
| `comparison-table` | `row:<n>` reveals row n |
| `chart` | `series:<n>` starts series n |
| `stat-callout` | `count` starts the count-up |
| `quote` | `reveal` shows the text |

## Lower thirds and captions

- `on_screen_text` lines cycle across the scene as the lower third: 52 px Inter, warm white on the dark background, inside the 5 % safe area (1728 x 972). At most 8 words at once; longer lines are split into 8-word chunks that share the line's time.
- `data.captions_on: true` draws word-timed captions (46 px) at the bottom of the safe area; the lower third moves up to leave the caption band free. Captions are never burned in by default; `captions.srt` is the sidecar.
- The chapter badge (number and label) sits top-left on every scene except title, chapter and end cards.

## What the spec must never contain

- Component props, frame numbers, pixel positions, font sizes, colors, easing names. The renderer owns every one of those; a spec that carries them cannot be re-rendered with a new design.
- Absolute file paths. B-roll is `data.src` relative to the spec; captures are ids.
- Digits in `narration` (voice rules, Hard Constraint 4). Digits go in `data` and `on_screen_text`.
- A scene type outside the schema enum. New scene types are added to `remotion/src/scenes/` and `rules/scene-library.md` first, then to the schema.

`render_longform.py` warns when `data` carries `props`, `frame`, `frames`, `x`, `y` or `px`.

## Outputs and how to read them

- `layout.json`: `scenes[] {id, type, startS, endS, matched, chapter, syncPoints[]}`, `chapters[]`, `totalS`.
- `render.json`: `layout` summary, `timings` (seconds per step), `warnings`, `output` (ffprobe), `thumbnails`, `lint`.
- A scene with `matched: false` in a captioned render is the first thing to check when a visual lands off-cue (`shared/pipeline-overview.md`, loop-back table).

## Studio preview

`cd remotion && npx remotion studio src/index.ts`, then load `OUT/props-episode.json` as the props of `Episode` (the defaults in `src/defaults.ts` show a six-scene sample without captions). Scenes appear as named sequences in the timeline.
