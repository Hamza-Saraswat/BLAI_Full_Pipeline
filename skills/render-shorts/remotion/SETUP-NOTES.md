> v2 port note: paths below were rewritten for `skills/render-shorts/` (was `render/remotion/`). `scripts/assemble.py` now generates the props and runs the canonical render + loudnorm commands; `public/fixtures/` was dropped (Studio defaults use `public/smoke/`), and `align-captions.mjs` is a fallback only (captions come from `skills/elevenlabs-narration`).

# Assembly (EDITOR stage) - Setup Notes

Remotion project that stitches rendered scene mp4s + voiceover + music +
word-timed captions into a final 1080x1920@30 YouTube Short.

Verified working on 2026-07-04 (macOS Apple Silicon, Node v22.23.0, ffmpeg 8.1.1).

## Pinned versions (exact, no carets)

| Package                 | Version |
| ----------------------- | ------- |
| remotion                | 4.0.484 |
| @remotion/cli           | 4.0.484 |
| @remotion/captions      | 4.0.484 |
| @remotion/media         | 4.0.484 |
| @remotion/zod-types     | 4.0.484 |
| mediabunny              | 1.47.0  (matches @remotion/media's own dependency) |
| zod                     | 4.3.6   (matches @remotion/media's own dependency) |
| react / react-dom       | 19.2.3  |
| typescript              | 5.9.3   |

Scaffolded with `npx create-video@latest . --blank --yes` (blank template,
TypeScript). Remotion 5 is not released; stay on 4.x.

## Composition

- id: `Assembly`, 1080x1920, 30 fps.
- Duration is computed by `calculateMetadata` (src/Assembly.tsx): each
  segment is probed with mediabunny (`Input.computeDuration()`, the successor
  of `parseMedia({fields:{slowDurationInSeconds}})` from the retired
  @remotion/media-parser). Per-segment `durationInFrames` =
  `round(seconds * 30)`; composition duration = sum of all segments.
  The voiceover may be shorter than the video - total always follows video.
- Segments play back-to-back in a `<Series>`; each `<Series.Sequence>` is
  premounted 4s (`premountFor={4 * fps}`) and contains
  `<OffthreadVideo pauseWhenBuffering muted>` (scene mp4s are treated as
  visual-only; the voiceover carries all speech audio).
- Voiceover: `<Audio>` (@remotion/media) at full volume from frame 0.
- Music (optional): `<Audio loop>` at constant low volume
  (`musicVolumeDb`, default -22 dB -> gain 10^(dB/20) ~= 0.079). Loops if
  shorter than the video; cut off at composition end. Simple constant
  ducking for v1.
- Captions: `createTikTokStyleCaptions({captions,
  combineTokensWithinMilliseconds: 1000})`; one `<Sequence>` per page;
  currently spoken token highlighted `#FFB347`; 72px / weight 800
  sans-serif, white fill with 10px black understroke
  (`-webkit-text-stroke` + `paint-order: stroke fill`) and drop shadow.

## Props contract (Zod schema in src/schema.ts)

```jsonc
{
  "segments": [
    // 1..n scene clips, played in order. src is a path RELATIVE TO public/
    // (or an http(s) URL). durationInFrames is filled in automatically by
    // calculateMetadata - do not set it manually.
    { "src": "fixtures/scene1.mp4" },
    { "src": "fixtures/scene2.mp4" }
  ],
  "voiceoverSrc": "fixtures/voiceover.wav", // required, full volume
  "musicSrc": "fixtures/music.wav",         // optional, low-volume bed
  "captions": [
    // @remotion/captions `Caption` objects. text carries its own leading
    // space for every word after the first (whitespace-sensitive!).
    { "text": "Testing", "startMs": 0,   "endMs": 600,  "timestampMs": 300, "confidence": 1 },
    { "text": " the",    "startMs": 600, "endMs": 1150, "timestampMs": 875, "confidence": 1 }
    // ... timestampMs/confidence may be null
  ],
  "musicVolumeDb": -22,   // optional, default -22 (dBFS gain applied to music)
  "sfx": [
    // optional one-shot sound effects. name -> public/sfx/<name>.wav
    // (bundled: whoosh, pop, tick, ding, type - see skills/render-shorts/assets/sfx/README.md).
    // gainDb = TARGET PEAK in dBFS (default -16, clamped at -6 so cues
    // never rival the VO; the -20dBFS asset normalization is compensated).
    { "atMs": 6370, "name": "whoosh" },
    { "atMs": 12000, "name": "ding", "gainDb": -12 }
  ],
  "showSafeZones": false  // optional, draws safe-area debug overlay
}
```

## How segments must be delivered

The renderer runs inside headless Chrome, which cannot read arbitrary
filesystem paths. **The pipeline must copy scene mp4s, the voiceover, and
music into `skills/render-shorts/remotion/public/`** (e.g. `public/segments/job-123/...`)
and reference them in props by public/-relative path
(`"segments/job-123/scene1.mp4"`). `resolveSrc()` (src/resolve-src.ts)
turns those into `staticFile()` URLs; http(s) URLs pass through; absolute
paths (`/Users/...`) throw a descriptive error at probe time.

## Verified commands

```bash
cd skills/render-shorts/remotion
npm install

# Render (verified: ~13s wall time for the 8s test video on M-series)
npx remotion render Assembly out/test-assembly.mp4 --props=fixtures-props.json

# Safe-zone debug still (kept as safe-zone-check.png)
npx remotion still Assembly safe-zone-check.png --props=fixtures-props-safezones.json --frame=150

# List compositions / check the computed duration without rendering
npx remotion compositions --props=fixtures-props.json
```

ffprobe of the verified test render:
video h264 1080x1920 @ 30/1, audio aac 48kHz stereo, duration 8.04s
(240 frames video; the extra ~0.04s is AAC priming), size ~5.8 MB.

## Safe-zone / caption placement

Canvas 1080x1920; centered safe area 900x1160 (x 90..990, y 380..1540);
YouTube Shorts UI covers roughly the bottom 450px (y >= 1470).
The caption block is max-width 900px, centered at x 90..990, and
BOTTOM-ANCHORED at y=1380 (`bottom: 540px`), growing upward: one 72px line
occupies ~y 1297..1380 (baseline ~1360), two lines start at ~1214 - always
inside the safe area and clear of the Shorts UI. Set `"showSafeZones": true`
to draw the rects (see safe-zone-check.png).

## Test fixtures (public/fixtures/)

- `scene1.mp4` - 4.0s 1080x1920@30 ffmpeg `testsrc2`.
- `scene2.mp4` - 4.0s 1080x1920@30 solid blue + "SCENE 2" text.
- `voiceover.wav` - 7s 330Hz sine, mono 48kHz (1s shorter than video - by design).
- `music.wav` - 8s 110Hz sine, stereo 48kHz.
- `captions.json` - 10 word-timed captions spanning 0-6.4s.
- Props files at project root: `fixtures-props.json`,
  `fixtures-props-safezones.json` (same + `showSafeZones: true`).

## Gotchas

- **create-video `--no-tailwind` is broken** (minimist parses it as
  `tailwind: false`, but the CLI checks `parsed['no-tailwind']`), so the
  blank template lands WITH Tailwind even when you opt out. Tailwind was
  removed manually (package.json deps, `enableTailwind` in
  remotion.config.ts, src/index.css). Re-check if you re-scaffold.
- **`--yes` skips the "Add agent skills?" prompt** (and the git-repo
  prompt); without it the wizard hangs waiting for TTY input.
- The scaffolder ran `git init` inside the Remotion folder; that nested `.git`
  was removed (parent project manages versioning).
- **This machine's `ffmpeg` (8.1.1) has no `drawtext`** (built without
  freetype) - scene2's text frame was generated with Python/PIL instead.
- `premountFor` cannot be combined with `layout="none"` on `<Sequence>`
  (type error) - caption pages use the default absolute-fill layout.
- Remotion's eslint rule `@remotion/volume-callback` requires the media
  `volume` prop to be a callback, hence `volume={() => gain}`.
- Caption `text` is whitespace-sensitive: every word after the first must
  carry a leading space; the container uses `white-space: pre-wrap` so
  spaces are preserved but long pages still wrap within 900px.
- Caption pages: a page stays visible for
  `max(1000ms, page.durationMs)` but never past the next page's start
  (slight improvement over the skill's formula, which could cut off pages
  whose tokens span longer than the switch interval).
- Caption pre-roll: every page's DISPLAY start is shifted -150ms (clamp >=0,
  `CAPTION_PRE_ROLL_MS` in Captions.tsx) so text leads the audio; end times
  are not shifted (pages only get longer), and the next-page clamp uses the
  next page's shifted start so pages never overlap. The word highlight is
  driven from the sequence's shifted start, keeping it locked to real audio
  times.
- `scripts/loop_check.mjs <mp4>` - first/last-frame SSIM "visual rhyme"
  check (threshold 0.5, `--threshold` to override; exit 0 similar / 1 not /
  2 error; prints one JSON line).
- zod v4 (4.3.6) is what @remotion/media itself depends on at 4.0.484, so
  zod v4 is the correct pin for this Remotion version (older docs said
  3.22.3).
- `out/` is gitignored (template default); `safe-zone-check.png` at the
  project root is kept on purpose as the visual reference.

## Caption alignment (added post-setup)

- `scripts/align-captions.mjs <vo.wav> <storyboard.json> <captions-out.json>`
  → writes captions.json (@remotion/captions Caption[] words) + timing.json
  (per-scene {scene_id, start_ms, end_ms, duration_s incl. +0.35s breath,
  +1.0s extra on the last scene}) next to it. Exit 3 = >10% word drift.
- Dep: `@remotion/install-whisper-cpp@4.0.484` (pinned). First run clones +
  builds whisper.cpp v1.7.4 into `skills/render-shorts/remotion/whisper.cpp/` and downloads
  the base.en model (~148MB).
- **Gotcha: whisper.cpp build requires `cmake`** (installed via brew, 4.3.4).
  If a build fails partway, DELETE `skills/render-shorts/remotion/whisper.cpp/` before
  retrying -- the installer refuses half-built folders.
- Input is resampled to 16kHz mono automatically (whisper.cpp requirement;
  Kokoro emits 24kHz).

## Canonical final-render command (smoke-test verified)

```bash
npx remotion render Assembly <raw.mp4> --props=<props.json> --color-space=bt709
ffmpeg -i <raw.mp4> -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 192k <final.mp4>
```

- Without `--color-space=bt709` Remotion 4.0.484 emits full-range
  yuvj420p/bt601 (`color_range=pc`) which fails `lint_video.py`.
- The loudnorm pass brings integrated loudness to -14 LUFS (video stream
  copied, audio re-encoded AAC 192k). Verified end-to-end 2026-07-04:
  13.4s smoke Short, both final gates green.
