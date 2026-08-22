> v2 port note: paths below were rewritten for `skills/render-shorts/` (was `render/manim/`). Install steps for macOS and Ubuntu arm64 live in `../setup.md`; scene authoring rules in `../rules/manim-1.md` and `../rules/manim-2.md`.

# Manim CE vertical (9:16) pipeline -- setup notes

Verified end-to-end on 2026-07-04, macOS (Apple Silicon, Darwin 23).
Everything in this file was actually run and ffprobe-checked; nothing is aspirational.

## Versions

| Component | Version | Notes |
|---|---|---|
| uv | 0.11.6 | |
| Python (venv) | CPython 3.12.12 | uv found Homebrew `python@3.12`; system python3 is 3.9 = too old for Manim CE 0.20.x (needs >= 3.11) |
| manim (Community) | 0.20.1 | |
| manimpango | 0.6.1 | prebuilt macOS arm64 wheel (delocate -- bundles pango dylibs) |
| pycairo | 1.29.0 | **no macOS arm64 wheel on PyPI** -- built from sdist via meson; needs brew `pkg-config` + `cairo` (see below) |
| numpy / pillow / moderngl | 2.5.1 / 12.3.0 / 5.12.0 | |
| ffmpeg | 8.1.1 | system install; manim shells out to it for encoding |
| brew: pkgconf (`pkg-config`) | 2.5.1 | required to build pycairo |
| brew: cairo | 1.18.4 | required to build pycairo |
| brew: pango | 1.58.0 | installed per playbook; strictly only needed if the manimpango wheel is ever unavailable |

## One-time install (exact commands)

```bash
cd skills/render-shorts/manim
uv venv --python 3.12 .venv
brew install pkg-config pango cairo   # pycairo 1.29.0 has no macOS arm64 wheel -> sdist build needs pkg-config + cairo
uv pip install --python .venv manim
```

Observed failure mode if you skip brew: `uv pip install manim` dies building pycairo with
`Dependency lookup for cairo with method 'pkg-config' failed`. Install the brew packages and rerun.

## Render commands (verified, copy-paste ready)

**Always run from `skills/render-shorts/manim/`** -- manim only reads `manim.cfg` from the invocation cwd,
and the portrait frame geometry lives in that file (gotcha #4).

No venv activation needed (the console script pins its own interpreter):

```bash
# DRAFT -- 540x960 @ 15 fps  (~1.5 s wall for the 5 s scene)
.venv/bin/manim render -r 540,960 --fps 15 hello_scene.py HelloVertical

# FINAL -- 1080x1920 @ 30 fps, fully cfg-driven  (~2.3 s wall for the 5 s scene)
.venv/bin/manim render hello_scene.py HelloVertical
```

Equivalent with activation:

```bash
source .venv/bin/activate
manim render -r 540,960 --fps 15 hello_scene.py HelloVertical   # draft
manim render hello_scene.py HelloVertical                        # final
```

### ffprobe verification (actual outputs, 2026-07-04)

```text
# FINAL  media/videos/hello_scene/1920p30/HelloVertical.mp4
codec_name=h264  width=1080  height=1920  avg_frame_rate=30/1  duration=5.000000  nb_frames=150

# DRAFT  media/videos/hello_scene/960p15/HelloVertical.mp4
codec_name=h264  width=540   height=960   avg_frame_rate=15/1  duration=4.933008
```

(Draft duration is 4.93 s because 5 s quantizes to 74 whole frames at 15 fps -- expected.)

## Where output lands

Pattern: `media/videos/<module_stem>/<pixel_height>p<fps>/<SceneName>.mp4`, relative to cwd.

- Final: `skills/render-shorts/manim/media/videos/hello_scene/1920p30/HelloVertical.mp4` (184 KB)
- Draft: `skills/render-shorts/manim/media/videos/hello_scene/960p15/HelloVertical.mp4` (80 KB)
- `media/videos/.../partial_movie_files/` is manim's per-animation cache -- safe to delete anytime.

If this directory becomes a git repo, ignore: `.venv/`, `media/`, `__pycache__/`.

## Gotchas (each one verified the hard way)

1. **Never use quality flags (`-ql -qm -qh -qp -qk`).** They overwrite the cfg pixel dims
   with LANDSCAPE presets while the logical frame stays portrait. Verified: `-ql` produced
   `854x480` (ffprobe). Squished garbage. Draft = `-r 540,960 --fps 15`, nothing else.
2. **Portrait frame geometry: manim only derives `frame_width` FROM `frame_height`, never the
   reverse** (`manim/_config/utils.py:669-674` in 0.20.1). The original plan assumed setting
   `frame_width=8.0` would derive `frame_height≈14.22` -- empirically FALSE: `frame_height`
   stayed at its 8.0 default, giving anisotropic units (135 px/u horizontal vs 240 px/u
   vertical = distorted geometry). Fix in `manim.cfg`: pin **both**
   `frame_height = 14.222222222222222` and `frame_width = 8.0`. (Also verified: setting only
   `frame_height=14.222222222222222` derives `frame_width` to exactly `8.0`.)
3. **`-r` is `W,H`**, not H,W: `-r 540,960` → 540 wide x 960 tall (ffprobe-verified).
   `-r`/`--fps` are digested after `-q`, so they beat presets -- but see gotcha 1: just don't pass `-q`.
4. **cwd matters.** `manim.cfg` is only picked up from the invocation cwd. Run from another
   directory and the logical frame silently falls back to 8.0 x 4.5 (landscape default) --
   text sizes and safe-area pixel mapping all shift. Always `cd skills/render-shorts/manim` first.
5. **No LaTeX, ever.** This pipeline is `Text()`/Pango only; `Tex`/`MathTex` are banned
   (and would fail anyway -- no TeX distribution installed).
6. **System python3 is 3.9** -- never use it. The venv (CPython 3.12.12) is the only interpreter.
7. **Stay inside the safe area.** Shorts UI covers roughly the bottom 450 px (title/channel/
   description) and right 120 px (like/share rail). Use `blai_layout.place_in_safe()` /
   `safe_zone_debug()`; brand colors also come from `blai_layout` only.

## Safe area: px → scene-unit math

At 1080x1920 with frame 8.0 x 14.2222 u: **1 scene unit = 135 px on both axes**
(px/u horizontal = 1080/8.0 = 135.0; vertical = 1920/14.2222 = 135.0 -- probe-verified).
`blai_layout` stores margins as *fractions* of the live frame dims, so the same constants
are correct at draft resolution too.

Safe box: 900 x 1160 px = left 60 / right 120 / top 310 / bottom 450 px reserved.

| Constant | px | scene units (= px x 8/1080) |
|---|---|---|
| `SAFE_LEFT` | 60 | 0.444444 |
| `SAFE_RIGHT` | 120 | 0.888889 |
| `SAFE_TOP` | 310 | 2.296296 |
| `SAFE_BOTTOM` | 450 | 3.333333 |
| `SAFE_W` x `SAFE_H` | 900 x 1160 | 6.666667 x 8.592593 |
| safe x-range | 60..960 | -3.555556 .. +3.111111 |
| safe y-range (y up) | -- | -3.777778 .. +4.814815 |
| `SAFE_CENTER` | (510, 730 from top-left) | (-0.222222, +0.518519, 0) |

Note the safe center is **not** the frame center -- it sits left of and above (0,0).
`place_in_safe(mobj, "center")` targets the safe center, which is what you want on Shorts.

## Files

- `manim.cfg` -- 1080x1920 @ 30, frame 8.0 x 14.2222 (both pinned; see gotcha 2)
- `blai_layout.py` -- SAFE_* constants, `safe_zone_debug()`, `place_in_safe()`,
  `fit_safe_width()`, `BRAND_BG` `#0B1020` / `BRAND_FG` `#F5F0E8` / `BRAND_ACCENT` `#FFB347` (placeholders)
- `hello_scene.py` -- `HelloVertical`, 5.0 s / 150 frames smoke test, Text()-only
