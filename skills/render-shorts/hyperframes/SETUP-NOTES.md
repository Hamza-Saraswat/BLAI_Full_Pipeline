> v2 port note: paths below were rewritten for `skills/render-shorts/` (was `render/hyperframes/`). The upstream skills are vendored under `../vendor/` (core, cli, keyframes only); the `npx skills add` install step is not needed in v2. `packs/hello-*.mp4` reference renders were not ported; re-render a snippet to regenerate one.

# HyperFrames Setup Notes

Date: 2026-07-04 · macOS (darwin), Node v22.23.0, ffmpeg 8.1.1, system Chrome present.

## Versions

| Component | Version | Notes |
|---|---|---|
| hyperframes (CLI + local devDependency) | **0.7.31** (exact pin, no `^`) | `devDependencies` in `package.json`; scaffold scripts also pin `npx --yes hyperframes@0.7.31` |
| gsap | 3.14.2 | Loaded from jsdelivr CDN in `index.html` (scaffold default) |
| skills CLI (`npx skills`) | 1.5.14 | Used for repo-root skill installs |
| heygen-com/hyperframes skills | 21 skills | Installed to repo `skills/` via `.claude/skills` symlink |
| remotion-dev/skills | 1 skill (`remotion-best-practices`) | Same install path |

## How this project was created

```bash
cd skills/render-shorts/hyperframes
HYPERFRAMES_SKIP_SKILLS=1 npx -y hyperframes@0.7.31 init . --non-interactive --example blank --resolution portrait
npm install   # installs the exact-pinned hyperframes devDependency
```

- `--resolution portrait` = 1080x1920 (9:16). Other useful presets: `landscape`, `portrait-4k`, `square`.
- `HYPERFRAMES_SKIP_SKILLS=1` stops `init` from installing AI skills itself; we install them
  separately from the repo root with `npx skills add heygen-com/hyperframes` (see below).

## Working commands (verified)

```bash
# Lint (0 errors, 0 warnings on hello-world)
./node_modules/.bin/hyperframes lint

# Render -- THE verified command
./node_modules/.bin/hyperframes render --output hello.mp4 --fps 30
# (fps default is already 30; flag kept for explicitness. Add --quality high for finals.)

# Verify
ffprobe -v error -show_entries stream=width,height,r_frame_rate,duration hello.mp4
# -> width=1080, height=1920, r_frame_rate=30/1, duration=5.000000
```

`npm run render` / `npm run check` (lint + validate + inspect) / `npm run dev` (preview studio,
long-running -- background it) are the script-level equivalents.

## Render wall-time (5 s hello-world, 150 frames @ 1080x1920)

- **17.4 s** pipeline time (17.9 s real incl. CLI startup) on first render.
- Breakdown from render trace: frame capture ~13.4 s (5 parallel Chrome workers, screenshot mode),
  encode ~1.0 s, assemble ~0.04 s. Output: 1.1 MB H.264 MP4.

## Composition rules that matter (from scaffold CLAUDE.md + `hyperframes docs`)

1. Root wrapper needs `data-composition-id`, `data-start`, `data-duration`, `data-width="1080"`, `data-height="1920"`.
2. Every timed element needs `class="clip"` + `data-start` + `data-duration` + `data-track-index`.
3. GSAP timelines must be `{ paused: true }` and registered: `window.__timelines["<composition-id>"] = tl;`.
4. Supported GSAP props: opacity, x, y, scale, scaleX, scaleY, rotation, width, height, visibility
   (no `yPercent` -- use px offsets inside `overflow: hidden` line wrappers for text-rise effects).
5. Deterministic only: no `Date.now()`, `Math.random()`, or runtime fetches.
6. Quick terminal reference: `npx hyperframes docs <data-attributes|gsap|compositions|rendering|examples|troubleshooting>`.

## Skills install (repo root)

```bash
cd /path/to/BLAI_Animator
npx -y skills@1.5.14 add heygen-com/hyperframes --agent claude-code --skill '*' -y
npx -y skills@1.5.14 add remotion-dev/skills    --agent claude-code --skill '*' -y
```

- Writes `skills-lock.json` at repo root (22 entries, per-skill content hashes).
- `.claude/skills -> ../skills` symlink was handled fine by the CLI (files "copied" through it
  into `skills/`); no workaround needed.
- `--agent claude-code` deliberately avoids creating other agent dirs (`.cursor/`, etc.).

## Gotchas hit / to know

- **No real gotchas -- everything worked first try.** Lint passed clean, render succeeded, symlink survived.
- `init` prints a deprecation warning for transitive `node-domexception` -- harmless.
- `init` scaffolds its own `AGENTS.md`/`CLAUDE.md` **inside** `skills/render-shorts/hyperframes/` (project-local
  agent guidance; distinct from the repo-root AGENTS.md).
- Render log line `[HyperFrames] render runtime fps [object Object]` is cosmetic log noise; actual
  fps verified correct via ffprobe.
- Renderer auto-picked 5 workers (each worker is a Chrome process, ~256 MB); `--workers N` to limit
  on low-RAM machines, `--low-memory-mode` exists.
- For CI-grade runs: `render --strict` fails on lint errors; `validate` runtime-checks JS errors,
  missing assets, contrast in headless Chrome.
- GSAP is vendored at `packs/vendor/gsap.min.js` (3.14.2); the snippets load it locally, no network needed at render (finding 54).
- Cloud alternative exists (`hyperframes cloud`) if local Chrome/ffmpeg ever become a problem.

## Reference artifacts in this directory

- `index.html` is a FINISHED AXON-PACK SCENE (s2 of the DGX Spark video), NOT a hello-world, and
  `hello.mp4` does not exist here (finding 52). **The reference for a new scene is
  `packs/<pack>-snippet.html`** -- copying `index.html` silently gives you the wrong style pack,
  and nothing lints the pack choice.
