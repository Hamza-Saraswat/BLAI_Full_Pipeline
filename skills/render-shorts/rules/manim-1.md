# Manim scene rules, part 1: API, layout, commands

Load only for scenes with `tool: manim`. Part 2 (`rules/manim-2.md`) carries the style-pack helpers and personalities. Verified setup, gotchas and the px-to-unit math: `manim/SETUP-NOTES.md`. Paths are relative to `skills/render-shorts/`.

## Environment and commands

- Project: `manim/` with Manim Community 0.20.1 in `manim/.venv` (Python 3.12; see `setup.md`). Never use the system `python3` for Manim.
- Always run from `manim/`: `manim.cfg` is only read from the invocation cwd and it pins the portrait frame (1080x1920 at 30 fps, logical frame 8.0 x 14.2222 units, 1 unit = 135 px on both axes). Never override resolution in code.
- Never pass quality flags (`-ql`, `-qm`, `-qh`, `-qp`, `-qk`): they replace the pixel size with landscape presets and squish the frame. Draft is `-r 540,960 --fps 15`, nothing else. `-r` is `W,H`.
- Write the scene file where the stage keeps per-run work (for example `<out>/work/<scene_id>.py`) and start it with the path shim used by `manim/pack_hellos/*.py` so `blai_layout` and `blai_packs` import from `manim/`:

```python
import sys
from pathlib import Path
sys.path.insert(0, "/abs/path/to/skills/render-shorts/manim")
```

```bash
cd skills/render-shorts/manim
.venv/bin/manim render -r 540,960 --fps 15 /abs/path/work/s3.py SceneS3   # draft
.venv/bin/manim render /abs/path/work/s3.py SceneS3                       # final, cfg-driven
ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration media/videos/s3/1920p30/SceneS3.mp4
```

Output lands at `manim/media/videos/<module>/<height>p<fps>/<SceneName>.mp4` (gitignored; `partial_movie_files/` is a cache, safe to delete). Copy the final to `<scenes-dir>/<scene_id>.mp4`.

## Allowed API surface (whitelist, nothing else)

- Mobjects: `Text` (never `Tex` or `MathTex`; LaTeX is banned and no TeX is installed), `Rectangle`, `RoundedRectangle`, `Circle`, `Dot`, `Line`, `Arrow`, `SurroundingRectangle`, `VGroup`, `DecimalNumber` / `Integer` for count-ups only with `mob_class=Text` (their default renders through LaTeX).
- Positioning: `.arrange()`, `.next_to()`, `.to_edge()`, `.move_to()` with helpers from `blai_layout.py` ONLY. No hand-tuned raw coordinates like `np.array([1.3, -2.7, 0])`; derive every position from another mobject or a `blai_layout` constant.
- Animations: `FadeIn`, `FadeOut`, `Write`, `Transform` / `ReplacementTransform`, `Create`, `Indicate`, `ChangeDecimalToValue`, `.animate` moves, `LaggedStart`.
- Colors and fonts: import from `blai_layout.py` and use `brand_text("...")` instead of raw `Text()` (Pango's default face is serif, off-brand); `self.camera.background_color = BRAND_BG` (or `use_pack`, part 2).
- No 3D, no `updater` functions unless a count-up demands it, no external images or SVGs, no plugins.

## Scene skeleton

```python
from manim import *
from blai_layout import *   # SAFE_* constants, safe_zone_debug, place_in_safe, fit_safe_width, brand_text

class SceneS2(Scene):       # class name = Scene + scene id, e.g. SceneS2 for s2
    def construct(self):
        self.camera.background_color = BRAND_BG
        # build inside the safe area; pace to the narration beats;
        # end with 8 frames of stillness (self.wait(0.27))
```

## Layout discipline (the number one failure mode is overlap or off-screen)

- Max 3 visual groups alive at once; `FadeOut` the old before the new.
- Text: `fit_safe_width(brand_text(s))`; never let text exceed the safe width; break lines at 4 words or fewer. The portrait frame is narrow: `scale_to_fit_width` every Text whose length you do not control.
- Never place text flush against a safe-area edge: descenders bleed past the bounding box (a real linter catch). `place_in_safe` insets 0.15 u by default; keep it at 0.15 or more for text.
- The caption band (canvas y 1260 to 1470) belongs to captions at assembly; `blai_layout`'s bottom margin (660 px) already excludes it. Never work around that margin. Verify with `scripts/safe_zone_check.py <mp4> --scene`.
- `role: hook` scenes: the hook text is already on screen at frame 1 (`self.add(...)` before the first `self.play`); never open on a blank frame; motion may start after 8 frames.
- Before the final render, add `self.add(safe_zone_debug())` once, render one draft, verify nothing escapes, then REMOVE the debug rect.
- The safe center is not the frame center (it sits left of and above (0,0)); `place_in_safe(m, "center")` targets the safe center, which is what you want on Shorts.

## Retry procedure (bounded)

1. Write the scene, draft render.
2. On a Python or Manim error: read the full traceback, fix that exact error (usually a hallucinated kwarg or a misused method; check the whitelist), retry. Max 5 attempts in total, then mark the scene blocked with the final traceback and what you tried.
3. On a clean draft: extract 2 or 3 stills; check overlap, safe area, 8 words or fewer, brief followed. Layout fixes count toward the same budget.
4. Final render at 1080x1920 at 30 fps, verify with `ffprobe`; match the assigned duration within 0.15 s using `self.wait()` padding (pad if short, trim waits if long).
5. `python3 scripts/lint_video.py <mp4>` (scene mode) and `python3 scripts/safe_zone_check.py <mp4> --scene` on the final; then copy it to `<scenes-dir>/<scene_id>.mp4`.

## Style reminders (the failure modes that actually happen)

- Overlap: `FadeOut` the previous group BEFORE `FadeIn` the next.
- Off-screen: the frame is narrow; fit every Text.
- Pacing: motion should land on the narration phrase it illustrates; when in doubt, slower and simpler.
- Fonts are registered by `blai_packs` at import (`manim/fonts/*.ttf`, all OFL). A missing font never breaks a render; helpers fall back to Menlo or Sans BOLD and warn on stderr.
