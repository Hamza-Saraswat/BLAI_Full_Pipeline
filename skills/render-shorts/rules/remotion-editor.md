# Remotion editor rules (load only for the assembly step)

`scripts/assemble.py` is the editor. It stages the inputs into `remotion/public/<slug>/`, generates the props for the `Assembly` composition (`remotion/src/schema.ts` is the contract, `remotion/SETUP-NOTES.md` the verified mechanics), renders with `--color-space=bt709`, normalizes loudness to -14 LUFS and runs the gates. This file is the editorial policy behind the script and the rules for anyone touching the composition by hand. Paths are relative to `skills/render-shorts/`.

## Inputs

- `<scenes-dir>/<scene_id>.mp4` per storyboard scene: 1080x1920 at 30 fps, H.264 yuv420p, silent. assemble.py conforms anything else with ffmpeg (letterboxed in brand navy) and warns; the editor never "fixes" video inside React.
- `narration.wav` plus `captions.json` (`[{word, start, end}]` from elevenlabs-narration, or @remotion/captions objects). Feed real word timings; the 150 ms caption pre-roll is built into `Captions.tsx`.
- Optional music: `--music FILE`, else `assets/music/<music_mood>*.mp3|wav` (first match), else none. Silence beats a wrong vibe.
- The storyboard: scene order, `sfx` markers, `music_mood`, `script_format`.

## What the assembly does (and what you may not change)

- Segment order is storyboard scene order. Durations are probed with mediabunny; the total follows the video segments (the narration may be slightly shorter).
- Voiceover at full volume from frame 0. Music at a constant -22 dBFS (keep it between -18 and -24), looping, cut at the end of the composition. No music under the final second if it fights the loop; skip music rather than fake a mood.
- Captions: TikTok-style pages (1000 ms combine window), the spoken word in amber `#FFB347`, others warm white; 72 px, weight 800, 10 px black under-stroke; box x 90 to 955, bottom-anchored at y 1430 so one line sits at about y 1347 to 1430 and two lines start at about 1264, always inside the caption band (1260 to 1470) and clear of the bottom UI. Never move captions into scene content; if a scene headline collides, the scene is wrong, not the caption.
- SFX: sparse punctuation, not a soundtrack. Cues only at scene boundaries (whoosh) and number or stat reveals (pop, ding, tick); at most 6 per video; never two within the same second; default -16 dBFS peak, clamped at -6 so a cue never rivals the voice. assemble.py derives cues from the storyboard's `sfx` markers: `start` at the cut, `end` 350 ms before the cut, `number-reveal` on the first spoken number of that scene (scene midpoint when none is found, with a warning). The wavs live in `remotion/public/sfx/` (synthesis recipe: `assets/sfx/README.md`).
- Loop rule: first and last frame rhyme. `remotion/scripts/loop_check.mjs` scores them with SSIM (loose 0.5 threshold). If it fails, flag it in the handback; never fabricate a fix by editing frames.

## Overruns

- Judge against the format's `final_max_s` (classic 60 s, smooth-explainer 180 s) from `skills/script-gates/formats.json`; never assume 60. assemble.py passes the band to `lint_video.py` (`--max-s`, `--warn-band`).
- Over by 0.5 s or less: trim trailing stillness of the last scene. Worse: report which scenes overran their `timing.json` slot and send them back; never speed up audio, never drop scenes.

## Render mechanics that bite

- `--color-space=bt709` is required: the default output is full-range yuvj420p/bt601 and fails lint.
- Headless Chrome reads only `remotion/public/`; absolute filesystem paths throw at probe time. assemble.py stages for you and removes the staging dir afterwards (`--keep-staging` to inspect).
- Long renders: a smooth-explainer is about 3,500 frames and takes 4 to 6 minutes on an M-series Mac. Run assemble.py in the foreground with a long timeout (it defaults to 30 min) and never pipe its output through `tail` or `head`; let the progress lines stream to stderr.
- `--draft` renders at scale 0.25 with crf 32: good for timing and audio checks, never publishable; `lint_video.py` always flags its resolution, so a draft exit code ignores lint.
- Loudness: one `loudnorm` pass usually lands -14 LUFS; if lint still flags it, assemble.py runs one two-pass correction with measured values, then stops. Report the reading.
- Inside the composition: frame-driven animation only (no CSS transitions or animations); media `volume` props must be callbacks (eslint rule); `premountFor` cannot combine with `layout="none"`.

## Definition of done (all machine-checked)

1. `scripts/assemble.py` exits 0 (render plus loudnorm plus gates).
2. `scripts/lint_video.py final.mp4 --final` passes with the format band (1080x1920 at 30, yuv420p, h264, audio present, -14 LUFS plus or minus 1.5).
3. `scripts/safe_zone_check.py final.mp4 --stills 8` passes (final mode: captions may sit in the band).
4. `node remotion/scripts/loop_check.mjs final.mp4` exits 0, or the failure is flagged in the handback.
5. `<out>/qa/safe-zone.png` (the `showSafeZones` still) exists.
6. Handback: duration, loudness, caption word count, music track or "none", sfx cues used, anything trimmed or flagged, the storyboard's `notes_for_review` echoed. Never publish from here; approval is the Telegram gate.
