# Pack: halftone -- midnight comic press (pop-art punch panels)

Identity: loud midnight comic press; every stat lands like a punch panel.
Spider-Verse Ben-Day dot texture, Lichtenstein pop-art, gig-poster motion.
Mechanically perfect print process -- the OPPOSITE of sketch's hand wobble:
no jitter, no rough.js, hard panel geometry, everything on a regular grid.

**THE STYLE LAW (linter survival): a full-perimeter gutter of pure
`#16121F` ink, WIDER than the linter margin strips (left ≥90px, right
≥160px, top ≥240px, bottom ≥660px), on EVERY frame.** Panels and all
bright content (cream/amber/dots) always inset within it. Cream at Y≈230
in a margin is an instant fail. Panels slide between inset positions only
(or behind an SVG clip/`overflow: hidden` stage) so bright pixels never
enter the gutter -- even mid-transition.

## Tokens

| Token | Hex | Role |
|---|---|---|
| bg | `#16121F` | ink violet-black -- page, gutter, margins |
| ink | `#0E0B16` | panel-interior fill, card shadows, text on cream/amber |
| fg (cream) | `#F2E8D5` | type + dots -- bright, **PANEL-INTERIOR ONLY, never margins** |
| accent | `#FFB347` | LOCKED brand anchor -- **the "POW" ink**: burst cards, starburst rays, second ink in duotone dot screens |
| mauve | `#8B7A9E` | muted labels, kickers |
| dot field | `#5E2A4D` | deep red-violet -- the default dot-screen ink |
| ok / bad | `#7BD88F` / `#FF6B6B` | LOCKED semantics |
| muted | cream at 55% | de-emphasized mono text |

- Fonts -- HF: **'Bangers'** (display, single Regular weight, **caps-only
  role** -- always uppercase, never body copy) + **'Space Mono'**
  (captions/labels/body, 400+700); self-hosted static woff2 (both Google
  Fonts OFL, static weights, no instancing). Manim: registered
  'Bangers' via `punch_card()` / 'Space Mono' via the pack's `mono` token
  (fallbacks: Sans BOLD / Monospace -- report, don't break).
- Dot screens: SVG `<pattern>` of EQUAL circles on a 45° lattice (two
  dots per square tile), revealed by animating a mask rect -- regular
  grids, deterministic, zero randomness. **DOT BUDGET ≤600 dots per
  frame.** Size-ramp convention: dot radius is a deterministic function
  of row, `r = r0 + k·row` (build-time-generated SVG circles; Manim:
  `benday_grid(rows, cols, radius_fn=...)`) -- dot-size ramps ARE the
  shading substitute (gradients are banned).
- Line: hard panel geometry -- 10px straight cream borders on `#0E0B16`
  panels; punch cards get an **offset ink shadow as a twin element
  (~6px behind, NEVER css box-shadow blur)**.
- Easing personality: **percussive, beat-mapped** -- `back.in(2)` impacts,
  `power4.out` snaps, `steps(2)` plate-flicks, at most ONE
  `elastic.out(1,0.4)` mega-punch per video.
- Motion vocabulary: punch cards slam in at scale 1.6→1.0 with
  `back.in(2)` + 3° rotation snap; starburst rays (jagged Star polygon,
  scale+rotate pop -- Manim: `Star(n=12,...)` + `SpinInFromNothing` /
  `GrowFromCenter`); misregistration flick -- amber and cream twin text
  layers offset ±3px for 2–3 frames at exact keyframed timeline marks
  (never random); panel-gutter transitions -- new panels slide across the
  gutter with `power4.inOut`, clipped by the stage.

## Topic fit

Hot takes, benchmark face-offs ("Llama vs Mistral"), myth-busting ("no,
you don't need an H100"). Anything that wants a verdict stamped on it.

## Don'ts (distinctiveness laws)

- NO hand wobble of any kind -- no rough.js, no jitter, no feTurbulence
  displacement (that's sketch's turf; this press is machine-perfect).
- NO CRT/scanline anything (terminal's turf).
- NO gradients, NO blur/shadow filters (shadows are offset twin
  elements; shading is a dot-size ramp), no emoji, no stock assets.
- NO randomness anywhere: dot patterns are regular grids, misregistration
  offsets are keyframed, starburst points come from a formula.
- Bangers never lowercase, never body copy; Space Mono never a headline.
- Never break THE STYLE LAW: no bright pixel outside the perimeter
  gutter, on any frame, including mid-slide.

## Implementation

- HF: `skills/render-shorts/hyperframes/packs/halftone.css` + snippet
  (`.gutter-stage` clip box, `.panel`, punch-card structure, Ben-Day
  pattern + mask-reveal recipe, misreg twins, starburst host).
- Manim: `blai_packs.py` → `HALFTONE` token set (`ink`, `dot_field`,
  `mono` pack keys) + `benday_grid()`, `punch_card()`, `starburst()`,
  `comic_panel()` helpers (core API only: Circle, RoundedRectangle,
  Rectangle, Star, Text).
