# HyperFrames scene rules, part 1: contract and mechanics

Load only for scenes with `tool: hyperframes`. Part 2 (`rules/hyperframes-2.md`) carries the per-pack personalities. Verified commands and gotchas: `hyperframes/SETUP-NOTES.md`. The vendored upstream skills under `vendor/` teach the framework; this file constrains them to the brand. Paths are relative to `skills/render-shorts/`.

## What to load from `vendor/`

| Need | Read |
|------|------|
| Composition contract: `data-*` timing, `class="clip"`, tracks, one paused timeline, determinism bans, root sizing | `vendor/hyperframes-core/SKILL.md`, then its `references/` on demand |
| CLI loop: `lint`, `validate`, `inspect`, `render`, `doctor`, `browser` | `vendor/hyperframes-cli/SKILL.md` |
| Seek-safe keyframes, GSAP timelines, SVG draw, proxy tweens | `vendor/hyperframes-keyframes/SKILL.md` |

Skip the upstream "make me a video" workflows (product launch, faceless explainer, and so on); the storyboard already is the plan. Cross-references inside the vendored files to skills that are not vendored (animation, creative, media, registry) can be ignored.

## Composition contract

- Project: `hyperframes/` (HyperFrames 0.7.31 pinned; `npm install` once; GSAP 3.14.2 loads from the jsdelivr CDN, so the first render needs network or a vendored copy next to `packs/vendor/rough.js`).
- Author the scene as `index.html` in a working copy of `hyperframes/` (copy the folder minus `node_modules`, then symlink or reuse `node_modules`), or in place when scenes run one at a time. Pack assets resolve relative to the project root (`packs/...`).
- Root element: `data-composition-id="main" data-start="0" data-duration="<seconds>" data-width="1080" data-height="1920"`, 30 fps. `data-duration` is EXACTLY the assigned scene duration (tolerance 0.15 s).
- Every timed element: `class="clip"` plus `data-start`, `data-duration`, `data-track-index`.
- One `gsap.timeline({ paused: true })` registered as `window.__timelines["main"]`, built synchronously at load. All motion is seek-driven. Never `setTimeout`, `Date.now()`, `Math.random()`, network fetches, or autoplaying media. Videos would use `muted` with a separate `<audio>`; scenes here carry no audio at all.
- Supported GSAP props: opacity, x, y, scale, scaleX, scaleY, rotation, width, height, visibility. No `yPercent`; use px offsets inside `overflow: hidden` line wrappers for text-rise effects. No MotionPathPlugin or DrawSVG in the bundled GSAP core: use manual per-segment tweens and the `pathLength="1"` plus `strokeDashoffset` trick.
- Fonts: self-hosted woff2 declared with `@font-face` inside each pack CSS (`packs/fonts/`). Never fetch a CDN font at render. Inter is the only sans the renderer resolves without a pack; Space Grotesk fails lint.

## Commands (run inside `hyperframes/`)

```bash
npx hyperframes lint                                                  # 0 errors before any render
npm run check                                                         # lint + validate + inspect
npx hyperframes render --output <scene>.mp4 --fps 30 --quality draft  # draft check
npx hyperframes render --output <scene>.mp4 --fps 30 --quality high   # final
ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration <scene>.mp4
```

`npm run dev` (preview studio) is a long-running server; background it if you need it. `--workers N` limits Chrome processes on low-RAM hosts. `render --strict` fails on lint errors. `npx hyperframes doctor --json` diagnoses a broken environment; `npx hyperframes browser ensure` fetches the pinned Chrome.

## Brand CSS (when no pack stylesheet is linked)

```css
:root {
  --bg: #0B1020; --fg: #F5F0E8; --accent: #FFB347; --ok: #7BD88F; --bad: #FF6B6B;
  --safe-left: 90px; --safe-right: 160px; --safe-top: 240px; --safe-bottom: 660px;
}
body { background: var(--bg); color: var(--fg);
  font-family: 'Inter', 'Helvetica Neue', Arial, system-ui, sans-serif; }
.headline { font-weight: 700; font-size: 96px; line-height: 1.05; }
.body-text { font-weight: 700; font-size: 64px; }
.safe { position: absolute; left: var(--safe-left); right: var(--safe-right);
  top: var(--safe-top); bottom: var(--safe-bottom); }
```

`--safe-bottom: 660px` is the Shorts UI (450) plus the caption band (y 1260 to 1470). Content lives inside `.safe` by default. With a pack, replace this block with `<link rel="stylesheet" href="packs/<pack>.css">`; every pack ships the same `.safe` geometry (text keeps 160 px clear of the right edge, wider than the 120 px strip the checker enforces).

## Visual vocabulary (in order of preference)

1. Kinetic type: words appearing or emphasized in sync with narration beats.
2. Count-ups and big numbers with unit labels ("273 GB/s").
3. Simple diagrams: rounded rects plus arrows (gates, pipelines, routers).
4. Icon-grid metaphors (100 dots, 3 light up).

Banned: Three.js, particle systems, stock photos or video, emoji as content, more than 2 simultaneously animated elements, gradients, drop shadows.

## Motion boundaries (learned from real linter failures)

- Elements enter by fade, scale, or rise in place. Never slide in from off-screen through the UI margins; the linter samples mid-animation frames.
- Whole-scene push-ins expand content into the margins: at scale 1.04 a 96 px padded edge lands at about 78 px, inside the left strip. Skip push-ins (preferred) or pad content 140 px or more.
- First and last 8 frames: no motion. For a hook scene the hook text is already on screen at frame 1; motion may begin at frame 9. Stable is not empty.

## Self-check before handing back

1. `npx hyperframes lint` passes (0 errors).
2. `ffprobe`: 1080x1920, 30 fps, duration within 0.15 s of the assignment.
3. Three stills (start, middle, end): all text inside the safe area, at most 8 words, brand colors only, matches the `visual_brief`.
4. `python3 scripts/safe_zone_check.py <mp4> --scene` passes (`--scene` adds the caption band).
5. `python3 scripts/lint_video.py <mp4>` passes in scene mode.
6. Copy the mp4 to `<scenes-dir>/<scene_id>.mp4`. It must be 1080x1920 at 30 fps, H.264 yuv420p, silent; `scripts/assemble.py` conforms anything else with ffmpeg (letterboxed in brand navy) and logs a warning, which is a defect in the scene, not a feature.
