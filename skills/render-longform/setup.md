# Setup: render-longform

The renderer is a Remotion 4.0.484 + React 19 project in `remotion/`. It needs Node 22, a Chrome Headless Shell that Remotion downloads itself, ffmpeg with the `loudnorm` and `ebur128` filters, and Python 3.9 or newer (stdlib only; `jsonschema` is optional and gives full schema errors).

## macOS (Apple Silicon, development)

```
brew install node@22 ffmpeg
cd skills/render-longform/remotion
npm install
npx remotion browser ensure
npx tsc --noEmit
```

## Ubuntu 24.04 arm64 (DGX Spark, production)

`build/install.sh` runs these; they are listed here so a hand install matches.

```
sudo apt-get install -y ffmpeg                      # 6.x or 7.x; both carry loudnorm and ebur128
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -   # Node 22 (arm64 build)
sudo apt-get install -y nodejs
# Chrome Headless Shell dependencies on a headless server
sudo apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 \
  libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2t64 libpango-1.0-0 libcairo2 fonts-liberation
cd skills/render-longform/remotion
npm install
npx remotion browser ensure                          # downloads chrome-headless-shell for linux-arm64 into node_modules/.remotion
npx tsc --noEmit
```

The Spark has no display; Remotion runs the headless shell without one. The GPU is not used for rendering (the renderer is CPU bound at 1080p; a 10-minute episode takes roughly 6 to 12 minutes at the default concurrency set in `remotion.config.ts`).

## Verify

```
cd skills/render-longform
python3 scripts/render_longform.py --spec fixtures/example-spec.json --audio fixtures/silence.wav \
  --captions fixtures/example-captions.json --captures fixtures/captures --out /tmp/blai-longform-test --draft
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -of compact /tmp/blai-longform-test/final.mp4
ls /tmp/blai-longform-test/thumbnails
python3 scripts/lint_longform.py --help
```

Expected: `final.mp4` 640x360 h264 yuv420p 30 fps of about 30 s, three PNG thumbnails, `render.json` with `lint.skipped: true`. Drop `--draft` for a full 1920x1080 render of the fixture (about 500 s of video; the fixture audio is 20 s of silence, so the lint reports `loudness: silent`; that is expected for the fixture only).

## Fonts

Inter loads through `@remotion/google-fonts` at render time (one small fetch per render worker, cached by Chrome). On a machine without internet, set `REMOTION_OFFLINE_FONTS=1` (or pass `--offline-fonts` to the script) and the fallback stack (Helvetica Neue, Arial) renders instead. Without the variable an offline render waits for the font and fails after the Remotion timeout.

## Common failures

| Symptom | Fix |
|---------|-----|
| `spawn chrome-headless-shell ENOENT` or a missing shared library | `npx remotion browser ensure`; on Ubuntu install the libraries above |
| Render hangs at `Getting composition` | the narration audio could not be probed; check `remotion/public/<slug>/narration.wav` exists and is a wav or mp3 |
| `lint: loudness silent` on a real episode | the audio track is empty; check the `--audio` path and the loudnorm log in `render.json` |
| `color_range` warning in the lint | the render ran without `remotion.config.ts` (wrong cwd); the script always runs inside `remotion/` |
| Fonts look like Arial | fonts were offline; see Fonts above |
| A scene fell back to `est_duration_s` (`matched: false` in `layout.json`) | the scene's narration text does not match `captions.json`; regenerate captions from the same script text |
