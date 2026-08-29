# Scene agent rules (every scene worker and the editor reads this first)

Scope: one Shorts scene (HyperFrames or Manim) or the final assembly. The storyboard is the spec. The tool rule file for your scene (`rules/hyperframes-1.md` or `rules/manim-1.md`) and the pack file (`styles/<pack>.md`) constrain the look. Paths are relative to `skills/render-shorts/`.

## Inputs a scene worker receives

- The storyboard JSON (`shared/schemas/storyboard.schema.json`), your scene id, the video's `style_pack`.
- Your exact duration in seconds from the narration timing (`scripts/scene_timing.py`), tolerance plus or minus 0.15 s, and the scene-relative word timings for your narration.
- The output path: `<scenes-dir>/<scene_id>.mp4`.

Read, in this order: this file, the tool rule file, `styles/<pack>.md`, your scene object (`narration`, `on_screen_text`, `visual_brief`, `render_notes`). The brief is the spec; do not add ideas beyond it. `render_notes` are producer hints: honor them, but they never override brand rules or linters.

## Format hard tokens (machine-checked, not negotiable)

- Canvas 1080 x 1920 at 30 fps, H.264 / yuv420p. Loudness of the final cut about -14 LUFS (assembly owns audio; scene clips are silent).
- Hook scene: the hook text is fully legible at frame 1 and a motion onset happens within 0.5 s. Frame 1 passes the thumbnail test on mute. Never open on a blank frame.
- The payoff starts by about second 4. By second 8 the viewer has learned one concrete thing, not just been promised it.
- Visual change at least every 3 s; no static stretch over 5 s; a new information beat every 5 to 8 s.
- No spoken CTA. The final 0.5 s is the wordmark settle; the last frame rhymes with frame 1 (loop anchor).
- Captions are always on, word-timed, composited at assembly. They own the caption band y 1260 to 1470; scene content never enters it (`scripts/safe_zone_check.py --scene` enforces this).
- Safe area: the RENDERER'S OWN CONSTANTS are the authority, never a number retyped from a document (finding 51). Manim: import `blai_layout` (870 x 950 px; `SAFE_X` -3.3333..+3.1111, `SAFE_Y` -2.2222..+4.8148, `SAFE_CENTER` (-0.1111, +1.2963) -- noticeably above frame center; content that looks high in a still is correct). HyperFrames: lay out inside the `.safe` container (830 x 1020 px -- stricter than any doc). Nothing that matters in the bottom 450 px (YouTube UI) or the right 120 px (like/comment rail). Debug helpers: `showSafeZones` in Remotion, `safe_zone_debug()` in Manim, `.safe` in HyperFrames.
- On-screen text: at most 8 words visible at once; minimum text height about 64 px at 1080 wide.
- Per-format bands (classic 32 to 38 s, smooth-explainer 75 to 150 s) live in `skills/script-gates/formats.json`. A scene worker never changes the script or its timing.

## Brand tokens

- Background `#0B1020`, text `#F5F0E8`, accent `#FFB347`, success `#7BD88F`, error `#FF6B6B`. A pack may swap the dark background family and the fonts; amber stays the one accent in every pack.
- Dark background always; big type; one focal idea per frame; generous margins.
- Fonts: HyperFrames and Remotion use Inter (bold weights), fallback Helvetica Neue, Arial; packs self-host their own woff2 in `hyperframes/packs/fonts/`. Manim uses `brand_text()` (generic Sans, BOLD) unless the pack helper says otherwise.
- Charts and diagrams: flat fills, no gradients, no drop shadows, 4 px strokes.
- When a number appears on screen it is also spoken, and every load-bearing spoken number appears on screen. Digits belong on screen; the narration carries the spoken form.

## Working rules

1. Render draft quality first, verify, then render final quality.
2. Bounded retries: at most 5 attempts per scene. Lint failures, render errors and layout fixes all count. Feed the exact error back each time. After 5, mark the scene blocked with the last error and what you tried. Do not thrash.
3. Match the assigned duration within plus or minus 0.15 s (`ffprobe`). Pad with stillness, never by slowing the motion.
4. Leave the first and last 8 frames visually stable so cuts read cleanly. Stable is not empty: for a hook scene the hook text is already on screen.
5. Prefer the simplest mechanism that reads well: opacity, position and scale moves, count-ups, bar and arrow diagrams. No 3D, no particles, no physics.
6. Sync motion beats to the narration phrase timings you were given. Motion lands on the phrase it illustrates; when in doubt, slower and simpler.
7. Elements enter by fade, scale or rise in place, never by sliding through the UI margins (the safe-zone linter samples mid-animation frames).
8. Verify before handing back: `ffprobe` (1080x1920, 30 fps, duration), three stills (start, middle, end: text inside the safe area, at most 8 words, brand colors only, matches the brief), `python3 scripts/safe_zone_check.py <mp4> --scene --stills 9` (the default 5 misses mid-animation frames), `python3 scripts/lint_video.py <mp4>` (scene mode: 2 to 25 s, no audio needed). HyperFrames scenes additionally run all three of `lint`, `validate` and `inspect --samples 40 --at-transitions --strict` -- `lint` alone passes masked-text and occlusion defects that only `inspect` catches (finding 53).
9. Before designing, diff your brief's clock against the assigned duration from `timing.json`: briefs are written against `est_duration_s` and the narration routinely lands 9-38% shorter, so "at 4s" beats can point past the end of your scene (finding 56). Re-anchor every beat to the narration word timings; drop or merge what no longer fits. Do not scale the clock.
10. Verifying head/tail stillness: H.264 makes identical frames byte-different, so use YAVG on a difference chain AND require `YMAX > ~100` before calling a spike motion -- x264's GOP keyframe at frame 250 re-quantizes the whole frame (diffuse YAVG spike, YMAX ~33), so any scene over 8.33 s false-positives on YAVG alone: `ffprobe -v error -f lavfi "movie=<mp4>,tblend=all_mode=difference,signalstats" -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.YMAX -of csv=p=0`.
11. The final scene's loop anchor is MEASURED, not eyeballed: extract frame 1 of s1, measure its bounding boxes, and rebuild the composition to land within a few px (`loop_check.mjs` scores SSIM against a 0.5 threshold; the measured approach scored 0.87-0.98). The loop anchor and deliberate recalls are the documented exception to "a number on screen is spoken in the same beat".
12. Write only your own scene file and its render, inside your own private work directory (`.local-builds/<slug>/scenes-work/<scene_id>/`). Never touch the storyboard, the narration audio, captions, timing or other scenes -- and never a shared scratch path (finding 11 lost work to one).

## Hard don'ts (any agent may reject work that violates these)

- No unexplained jargon on screen.
- No walls of text; no more than one text block animating at a time; at most 2 simultaneously animated elements.
- No stock-footage vibes: everything is typographic or diagrammatic in brand colors. No emoji as content, no gradients, no drop shadows.
- No claims the storyboard does not make.
- No LaTeX in Manim (`Text()` only; `Tex` and `MathTex` are banned).
- No CSS transitions or animations in Remotion (frame-driven only). No wall-clock timing in HyperFrames (seek-driven `data-*` and paused GSAP timelines only).
- No whole-scene push-ins or zooms that creep content into the margins.

## Editor (assembly) essentials

- `scripts/assemble.py` is the editor: it stages inputs, generates the Remotion props, renders with `--color-space=bt709`, normalizes loudness to -14 LUFS and runs the linters. Editorial policy lives in `rules/remotion-editor.md`.
- Segment order is storyboard scene order. No reordering, no trimming except trailing stillness of the last scene when the overrun is 0.5 s or less; anything worse goes back to the offending scene.
- Overrun is judged against the format's `final_max_s` (60 s classic, 180 s smooth-explainer), never a hard-coded 60.

## Handback (one paragraph, no code dumps)

Scene id, attempts used, final duration, linter results (both), output path, anything flagged. For the editor: final path, duration, loudness, caption word count, music track or "none", sfx cues used, loop-check result, anything trimmed or flagged, and the storyboard's `notes_for_review` echoed.
