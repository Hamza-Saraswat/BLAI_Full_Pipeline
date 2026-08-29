# Manim scene rules, part 2: style packs

Load after `rules/manim-1.md` for scenes with `tool: manim`. One brand, seven looks. `styles/README.md` is locked (shared anchors); per-pack token specs live in `styles/<pack>.md`. The storyboard's `style_pack` picks ONE pack per video; a scene worker never chooses and never mixes. Tokens and pack helpers live in `manim/blai_packs.py` (companion to `blai_layout.py`; the layout and safe-area API is unchanged). Paths are relative to `skills/render-shorts/`.

```python
from manim import *
from blai_layout import *   # SAFE_*, place_in_safe, fit_safe_width, brand_text
from blai_packs import *    # PACKS, use_pack, pack helpers

class SceneS3(Scene):
    def construct(self):
        T = use_pack(self, "terminal")   # sets camera bg, returns the token dict
        line = terminal_text("> vllm serve", t2c={">": T["secondary"]})
```

`use_pack(scene, pack)` sets `camera.background_color` and returns the token dict: `bg / fg / accent / secondary / muted / font / stroke_width` (blueprint adds `grid`, `construction_opacity`; axon adds `face_top`, `face_left`, `face_right`, `floor`, `mono`; halftone adds `ink`, `dot_field`, `mono`; silicon adds `mono`, `copper_unlit`, `board_grid`, `silkscreen`). `accent` is `#FFB347` in EVERY pack, still the one highlight color. Semantic ok and error stay `BRAND_OK` / `BRAND_ERROR` from `blai_layout`. Never hardcode pack hex in a scene; read the dict.

## Helper table (all core API, whitelist-conforming)

| Helper | Pack | What you get |
|---|---|---|
| `brand_text(s)` | signal (and labels everywhere) | Sans BOLD Text in brand fg |
| `terminal_text(s)` | terminal | monospace Text, JetBrains Mono (bundled OFL, auto-registered), fallback Menlo |
| `terminal_frame(w, h)` | terminal | RoundedRectangle window (the pack's ONE rounded corner) plus 3 header dots |
| `typewriter(text, time_per_char=0.05)` | terminal | `AddTextLetterByLetter` wrapper; pass `run_time=` for exact scene timing |
| `cursor_blink()` | terminal | use the returned `cursor_rect` ONLY; drive visibility with hard `add`/`remove` between exact-frame waits. The `Blink` half cannot be frame-accounted (float-summed child run_times; see manim-1 timing traps) |
| `sketch_text(s)` | sketch | Caveat handwriting Text (bundled OFL); falls back to Sans BOLD with a stderr warning |
| `sketch_jitter(m, seed, amplitude=0.02)` | sketch | THE one sanctioned raw-point manipulation: deterministic smooth wobble (seeded RandomState sinusoid field). Seed from the scene id; amplitude 0.03 u or less |
| `chalk_underline(m)` | sketch | jittered underline with hand overshoot past both ends; reveal with `Create` |
| `blueprint_grid()` | blueprint | full-frame faint NumberPlane (50 px major / 10 px minor). The ONE element allowed outside the safe area; it stays far under the linter's luma threshold. `self.add` it first; it is paper, not content |
| `construction_line(a, b)` | blueprint | DashedLine `#5FB4FF` at 55 %; derive `a` and `b` from mobject corners or centers, never raw coords |
| `ref_marker(n)` | blueprint | small circled amber number. The digit is brand-font `Text`, NOT `Integer` (the LaTeX route) |
| `iso_project(x, y, z)` | axon | THE iso projection (`x' = (x - y) * cos30`, y' sign-flipped for Manim's y-up); every axon point goes through it, defined once |
| `iso_prism(x, y, z, w, d, h, tokens)` | axon | VGroup(left, right, top) flat-fill Polygons with bg-colored strokes; no z-buffer, so add whole prisms back-to-front (smaller x + y is farther) |
| `iso_explode(group, spacing)` | axon | per-slab shift vectors along the iso up-axis for exploded views; fade `DashedLine` leaders in AFTER the separation lands |
| `iso_path(points)` | axon | sharp-corner conveyor VMobject (`set_points_as_corners`) for `MoveAlongPath`; give packets z = half their height so they ride ON the floor; never add the path itself |
| `axon_floor(cells, cell)` | axon | floor-grid diamonds sorted by distance from center; `LaggedStart(..., lag_ratio=0.08)` IS the ripple |
| `benday_grid(rows, cols, radius_fn=None)` | halftone | VGroup of Circles on a regular 45 degree lattice, zero randomness; `radius_fn(row, col)` is the size-ramp convention (`r = r0 + k*row`, the shading substitute). Raises if `rows*cols` exceeds the 600-dot budget |
| `punch_card(text, face_color=None)` | halftone | Bangers CAPS Text on a RoundedRectangle face plus a twin ink-shadow copy offset about 7x9 px (never a blur); cream face default, `T["accent"]` is the POW card. Falls back to Sans BOLD with a warning |
| `starburst(n=12)` | halftone | jagged amber `Star` polygon, fill-only; pop it with `SpinInFromNothing` / `GrowFromCenter` BEHIND the card it announces |
| `comic_panel(w, h)` | halftone | thick cream-stroked Rectangle, ink `#0E0B16` fill, square corners; the stage every bright element must sit inside |
| `pcb_trace(points, lit=False)` | silicon | copper polyline (`set_points_as_corners`), 45/90 degree law validated (raises on an illegal segment). `lit=False` is the unlit `#7A5A2E` VMobject; `lit=True` is the glow-law VGroup of 3 stacked stroke copies; reveal with `Create(..., lag_ratio=0.0)` |
| `signal_pulse(trace)` | silicon | `(pulse, anim)`: glow-dot stack plus `MoveAlongPath`, rate_func LINEAR (a signal never eases) |
| `chip(w, h, pins, label)` | silicon | FILLED rounded-rect body (epoxy = board-grid tone, tin outline) plus pin-stub Lines and an IBM Plex Mono die label; drop with `FadeIn(..., scale=1.15)` and `ease_out_cubic` |
| `via()` | silicon | concentric rings at a trace endpoint (`Annulus` plus bg `Dot` drill hole and a low-opacity glow annulus); pop with `GrowFromCenter` and `ease_out_back`, the pack's ONE overshoot |
| `silkscreen_label(s)` | silicon | `VGroup(box, text)`: `DashedVMobject` frame (`Create` / `FadeIn`) plus a mono designator typed with `AddTextLetterByLetter(lbl[1])` |

Fonts: `manim/fonts/*.ttf` (JetBrains Mono, Caveat, Sora SemiBold/Bold, Sometype Mono Regular/Bold, Bangers, Space Mono Regular/Bold, Chakra Petch Regular/SemiBold/Bold, IBM Plex Mono Regular/SemiBold; all OFL, license files alongside) are registered with Pango when `blai_packs` is imported (`manimpango.register_font`, process-local, idempotent). Missing files never break a render; helpers fall back (Menlo or Sans BOLD) and warn on stderr.

## Per-pack personality (dos and don'ts)

**signal, professional-snappy.** Big bold `brand_text`, flat shapes, hard cuts. Punch beats with `Indicate` (scale about 1.12, accent color; size punched text to `SAFE_W / 1.12` or the peak leaves the safe area); default smooth easing everywhere else. DON'T add texture, gradients, or more than one element moving at once; cleanliness IS the texture. A whole-screen change is a STAGED swap (drop the largest block on its own beat, bring the replacement into a non-overlapping band) -- a naive cross-dissolve renders one headline through another and no linter sees it.

**terminal, mechanical.** Reveals are `typewriter(...)` (steps, linear); new lines appear via hard `self.add`, no fades, no drift. `>` prompt prefix on beat lines, `$` for commands, `exit 0` as a success beat (sparingly). The cursor blinks between beats. DON'T use `Write`, soft fades, rounded rects (except the window frame), or flicker. Width budget: JetBrains Mono advances ~0.6 em, so the 64 px legibility floor caps a line at ~19 monospace characters across the safe box -- long commands take a `\` continuation, never a smaller font, and a continuation indent aligns to the first inked glyph (leading spaces in `Text()` produce no submobjects). On wide archetypes (grid) the window frame costs ~120 px of width and collides with the floor: drop the frame and carry pack identity with `terminal_text`, prompts, typewriters and hard cuts. `Indicate` on a `terminal_frame` recolors the FILL too (a solid flash); target something unfilled for a stroke-only pulse. `T["stroke_width"]` (2) is a CSS number: diagram strokes here use 4 px per scene-agent, so double it.

**sketch, human.** Draw-on everything: `Write` for chalk text, `Create` for jittered shapes; gentle overshoot via `rate_func=rate_functions.ease_out_back` on small moves and fades; nothing perfectly linear. Circle the key word, underline with overshoot, cross out wrong answers. Jitter every shape (`sketch_jitter`, seeded). DON'T leave straight machine-perfect lines, and DON'T animate the jitter itself (static wobble, deterministic renders). Circles and underlines overshoot a text bbox; re-check the composed group against `SAFE_X_MIN` / `SAFE_X_MAX` (see `pack_hellos/hello_sketch.py` for the clamp pattern).

**blueprint, drafting-machine.** Near-linear `Create` (`rate_func=rate_functions.linear`), strict ordering: grid first (frame 1), construction guides BEFORE the shape they define, the shape, then annotations (`ref_marker`, labels) fade in last. Stroke-only shapes (`fill_opacity=0`), sharp corners, `SECTION A-A` style labels used straight. DON'T fill shapes, bounce, or let anything but the grid touch the margins.

**axon, weighty-premium.** Builds use `rate_func=rate_functions.ease_in_out_cubic`, landings `ease_out_back`, conveyors `ease_in_out_sine`; `LaggedStart` lag_ratio 0.08. The extrusion build is a `ReplacementTransform` from an h of about 0 `iso_prism` to the full one (identical 3-polygon topology, a pure vertex tween; the same trick does the face-fold cutaway). Amber (`T["accent"]`) fills packets, tokens, and weight cubes ONLY; structure keeps the `face_top` / `face_left` / `face_right` triplet with bg-colored strokes. Headlines are `Text(font=AXON_FONT)` (Sora), diagram labels `AXON_MONO` (Sometype Mono, via `T["mono"]`). DON'T outline blocks (blueprint's turf), jitter anything (sketch's), or lead with type (signal's); DON'T fight the painter, hand-sort every add back-to-front; no gradients, no `Integer` / `DecimalNumber` for packet counts (LaTeX route), Text digits instead.

**halftone, percussive.** Frame 1 is a finished panel: `comic_panel` sized to the safe area plus the hook `punch_card` already on screen. Beats land as impacts: wind a card up (`.scale(1.6).rotate(6*DEGREES)`) and slam it home with `rate_func=rate_functions.ease_in_back`; pop a `starburst` behind it first; print dot screens on with `FadeIn(benday_grid(...), lag_ratio=0.002)`. Radius ramps (`radius_fn=lambda r, c: r0 + k*r`) are the ONLY shading, no gradients. Space Mono (`T["mono"]`) sets captions and labels; Bangers is caps-only display and never body copy. DON'T jitter or wobble anything (this press is machine-perfect, the opposite of sketch), do not exceed 600 dots per frame, and never let cream, amber, or dots leave the panel: THE STYLE LAW keeps a full-perimeter gutter of pure `#16121F` (left 90 px or more, right 160 or more, top 240 or more, bottom 660 or more) on every frame; content that slides stays inside the panel bounds.

**silicon, machine-placement.** The board is a physical object: filled metal, weighted strokes (copper over tin over silkscreen), light travelling copper. Strict ordering: board grid first (frame 1, the ONE full-frame element besides blueprint's, luma about 31, margin-legal), copper routes UNLIT (`Create(pcb_trace(...))`, `ease_in_out_quad`, 45 and 90 degree bends only), then a LINEAR `signal_pulse` energizes it while the `lit=True` stack draws behind, via pops (`ease_out_back`, slight), chips drop 1.15 to 1 (`ease_out_cubic`), silkscreen designators type in last. All glow is stacked stroke copies, never blur; type never glows. DON'T draw dashed construction guides or dimension choreography (blueprint's), DON'T let anything bright go green, scanline, CRT, or cursor (terminal's), DON'T wobble (the via overshoot is the only bounce), and DON'T let amber, tin, or silkscreen (luma over 140) or any routed copper leave the safe area (unlit `#7A5A2E` is luma about 95 and margin-legal by the math, but any trace is a candidate to be energized; keep it inside).
  Silicon traps (confirmed twice in first live use): `chip()`'s die label is hard-coded at font_size 40 with no kwargs (long labels overflow small chips -- replace it or build the chip from core API), its pin stubs add ~0.16 u per side (a near-safe-width chip overflows the box), and the canonical 1.15-scale drop breaches the safe area at mid-animation for wide elements: size dropped chips to `SAFE_W / 1.15`, or use a shift-drop (`FadeIn(shift=DOWN*0.18)`). There is no `silicon_board_grid()` helper yet; copy the NumberPlane block from `pack_hellos/hello_silicon.py`. <!-- chip() traps -->

## Reference scenes

`manim/pack_hellos/hello_{signal,terminal,sketch,blueprint,axon,halftone,silicon}.py`: one 5 s hello per pack (hook plus signature motif), each verified in v1 (draft and final render, ffprobe 1080x1920 at 30, `safe_zone_check.py --scene` and `lint_video.py` clean). Copy their structure (the `sys.path` shim included; they live one directory below `blai_layout.py`). Render from `manim/` as always: `.venv/bin/manim render pack_hellos/hello_terminal.py HelloTerminal`.
