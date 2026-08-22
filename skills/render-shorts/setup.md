# render-shorts setup

Install once per host, then verify. The macOS section was executed on 2026-08-22 (Apple Silicon, Node 22.23.0, npm 10.9.8, ffmpeg 8.1.1). The Ubuntu arm64 section mirrors it for the DGX Spark; lines marked "unverified" have not been run on a Spark yet.

## macOS (Apple Silicon)

```bash
brew install node@22 ffmpeg pkg-config cairo pango uv
cd skills/render-shorts/remotion && npm install && npx remotion browser ensure
cd ../hyperframes && npm install && npx hyperframes --version && npx hyperframes doctor
cd ../manim && uv venv --python 3.12 .venv && uv pip install --python .venv manim==0.20.1
```

Notes: `pycairo` has no macOS arm64 wheel and builds from source, hence `pkg-config` and `cairo` from brew. The Remotion headless shell lands in `remotion/node_modules/.remotion/`. Remotion warns on macOS older than 15 but renders fine on 14.

## Ubuntu 24.04 arm64 (DGX Spark)

```bash
sudo apt-get install -y ffmpeg build-essential pkg-config libcairo2-dev libpango1.0-dev \
  python3.12-venv python3.12-dev fonts-dejavu-core \
  libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
  libxdamage1 libxrandr2 libgbm1 libasound2t64 libpango-1.0-0 libcairo2     # Chrome runtime libs
# Node 22: build/install.sh installs it (user-level); otherwise NodeSource or nvm.
cd skills/render-shorts/remotion && npm install && npx remotion browser ensure        # unverified on arm64
cd ../hyperframes && npm install && npx hyperframes --version && npx hyperframes doctor --json
cd ../manim && python3.12 -m venv .venv && .venv/bin/pip install manim==0.20.1        # unverified on arm64
```

Notes (unverified on the Spark): Remotion 4.0.484 resolves a Linux arm64 headless shell on its own (`remotion.media` build or the Playwright arm64 Chromium); if the download is blocked, install `chromium` from apt and pass `--browser-executable /usr/bin/chromium` to `npx remotion render` (set it in `remotion.config.ts` with `Config.setBrowserExecutable`). HyperFrames renders through Puppeteer; if `doctor` reports no Chrome, run `npx hyperframes browser ensure`, or install `chromium` and export `PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium` before rendering. `manimpango` and `pycairo` ship manylinux aarch64 wheels; the `-dev` packages above cover a source build if pip falls back to it. Fonts for Manim packs are bundled in `manim/fonts/` and registered at import, so no system font install is needed beyond DejaVu for the generic Sans fallback.

## Verify (both hosts)

```bash
cd skills/render-shorts
python3 -m py_compile scripts/*.py && python3 scripts/assemble.py --help | head -3
python3 scripts/style_rotation.py --pick --slug setup-test
cd remotion && npx remotion versions && \
  npx remotion render Assembly /tmp/blai-smoke.mp4 --props=smoke-props.json --scale 0.25 --color-space=bt709 && cd ..
python3 scripts/lint_video.py /tmp/blai-smoke.mp4      # expected: only "resolution 270x480 != 1080x1920" (the scale)
cd hyperframes && npx hyperframes lint && cd ..        # lints the bundled index.html scene template
cd manim && .venv/bin/manim render -r 540,960 --fps 15 hello_scene.py HelloVertical && cd ..
ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration manim/media/videos/hello_scene/960p15/HelloVertical.mp4
```

Expected: the smoke render takes about 15 to 20 s at scale 0.25 on an M-series Mac (398 frames), the Manim draft renders in a few seconds at 540x960 at 15 fps, `npx hyperframes --version` prints `0.7.31`.

## Maintenance

- Versions are pinned exactly (no carets) in both `package.json` files and the lockfiles; `npm install` respects them. Upgrading Remotion means re-verifying the bt709 and yuv420p behaviour with `scripts/lint_video.py`.
- `remotion/scripts/align-captions.mjs` is the v1 whisper.cpp aligner, kept as a fallback when no ElevenLabs captions exist; its first run needs `cmake` and builds whisper.cpp into `remotion/whisper.cpp/` (gitignored).
- Per-run media never enters git: `remotion/public/.gitignore` keeps only `smoke/` and `sfx/`; the repo `.gitignore` drops `node_modules/`, `out/`, `media/`.
