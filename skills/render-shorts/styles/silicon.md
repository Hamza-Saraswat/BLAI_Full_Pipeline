# Pack: silicon -- matte-black circuit board (hardware mode)

Identity: a premium matte-black PCB where information travels as light down
copper. Black-soldermask board art, GPU marketing renders, MKBHD matte black
with a single accent. The board is a physical OBJECT -- filled metal, weighted
stroke hierarchy, luminous signal traffic. The locked brand amber is literally
the conductive material: ENIG gold / energized copper.

## Tokens

Palette (Y = 0.299R + 0.587G + 0.114B, the safe-zone linter's luma):

| Role | Hex | Y | Where it may appear |
|---|---|---|---|
| bg -- solder-mask charcoal (faint green CAST, never saturated) | `#0E1211` | ~17 | full bleed |
| board grid | `#1A211E` | ~31 | full bleed, margins included |
| copper, UNLIT (deep copper shadow) | `#7A5A2E` | ~95 | traces/pads/footprints -- see linter playbook |
| ENIG gold / energized copper -- brand accent | `#FFB347` | ~189 | center-frame (safe area) ONLY |
| tin/nickel (secondary traces, pads, chip outlines) | `#8FA0A8` | ~156 | center-frame ONLY |
| silkscreen (labels, designators, fg) | `#C9D2CC` | ~207 | center-frame ONLY |
| ok `#7BD88F` / bad `#FF6B6B` | -- | -- | LOCKED semantic, center-frame |

- muted: silkscreen at 50% over bg. Chip bodies reuse the board-grid tone
  `#1A211E` (dark epoxy) -- no extra hex.
- Fonts -- HF: 'Chakra Petch' (headlines/labels -- squared techno; static
  400/600/700 woff2 in `packs/fonts/`) + 'IBM Plex Mono' (reference
  designators/values, static 400/600). Both Google Fonts OFL. Manim:
  `SILICON_FONT` ('Chakra Petch') and `SILICON_MONO` ('IBM Plex Mono'),
  registered from `skills/render-shorts/manim/fonts/`. IBM Plex Mono is a DIFFERENT face
  from the terminal pack's JetBrains Mono -- never substitute one for the
  other.
- Line: weighted stroke hierarchy (this pack has WEIGHT, blueprint doesn't):
  copper traces 5px > tin secondary 3px > silkscreen 2px (dashed callouts).
  Rounded caps/joins on traces (etched copper, not drafted ink). Chips are
  FILLED rounded rects with pin stubs; pads are filled.

## Trace-routing grammar (the 45°/90° law)

Traces are polylines with ONLY 90° and 45° bends -- every segment is
horizontal, vertical, or exactly |dx| == |dy|. No curves, no arbitrary
angles, ever. HF: SVG polyline/path with `pathLength="1"`,
`stroke-dasharray: 1`, tween `stroke-dashoffset` 1 → 0 (no DrawSVG -- bundled
GSAP is core only). Manim: `pcb_trace(points)` -- `VMobject`
`.set_points_as_corners`, revealed with `Create`; the helper validates the
45° discipline and raises on an illegal segment. Copper routes first at the
unlit `#7A5A2E` level; light only ever travels along already-routed copper.

## Glow law

ALL glow = 2–3 stacked stroke copies of the same geometry: wide stroke at
low opacity → mid → thin at full opacity (e.g. 22px @ .12, 12px @ .30, 5px
@ 1.0). NEVER `filter: blur()` / `text-shadow` -- stacked strokes reproduce
identically in Manim (concentric stroke_width copies); blur does not. Type
never glows in this pack: light lives in the copper, not the letters.

## Green law

The solder-mask green cast may only exist at luminance < 40 -- i.e. the bg
(`#0E1211`, Y≈17) and board grid (`#1A211E`, Y≈31). Every bright element is
amber, silver (tin/silkscreen), or white. If anything saturates toward
phosphor green it rhymes with the terminal pack -- that is a defect. Hard
ban: no scanlines, no CRT artifacts, no typewriter-as-identity.

## Easing personality: machine-placement

Pick-and-place precision. No wobble, ever.
- Trace routing: `power2.inOut` (Manim: `rate_functions.ease_in_out_quad`).
- Signal pulses: strictly LINEAR (`ease: "none"` / `rate_functions.linear`).
- Component drops: `power3.out`, scale 1.15 → 1 (`ease_out_cubic`).
- Via pops: `back.out(1.3)` -- the ONE sanctioned overshoot
  (`rate_functions.ease_out_back`, kept small).
- Pin/pad sequences: `steps(n)` / instant `.set()` toggles / stepped
  staggers -- machine indexing, not organic stagger.

## Motion vocabulary (signature techniques)

1. **Trace routing draw-on** -- 45°/90° polyline draws via
   dasharray/dashoffset (HF) / `Create(pcb_trace(...))` (Manim),
   `power2.inOut`.
2. **Signal pulse** -- a short bright amber dash travels an already-drawn
   trace. HF: a path copy with tiny dasharray (`0.08 1.92`, `pathLength=1`),
   tween dashoffset `0.08 → -1.0`, linear; an energized amber copy (glow
   stack) draws behind it at the same rate. Manim: `signal_pulse(trace)` --
   glow-dot stack + `MoveAlongPath`, linear.
3. **Component placement** -- chip (rounded rect + pin stubs + mono die
   label) drops onto its footprint: opacity 0→1, scale 1.15→1 `power3.out`;
   pads flash amber on contact, settle to tin.
4. **Via pops** -- concentric rings (`Annulus` + `Dot`) punctuate trace
   endpoints, slight `back.out(1.3)` overshoot.
5. **Copper-pour flood fill** -- a zone highlights by sliding a bg-colored
   cover rect away (or clip-path inset). Manim: filled Polygon behind a
   bg-colored masking Rectangle that slides off. Never animate fill opacity
   over the margins.
6. **Silkscreen annotation** -- dashed outline callout (fade in -- dashes
   never draw, the dash pattern clashes with dashoffset) + reference
   designator (`U1`, `VRAM0`, `KV$`) typed via incremental textContent
   keyframes (HF, seek-safe proxy slice) / `DashedVMobject` +
   `AddTextLetterByLetter` (Manim).

## Topic fit

Hardware anatomy: GPU/VRAM, quantization ("fewer bits per cell"), token
throughput, PCIe bandwidth, unified memory -- anything where the natural
visual IS the board.

## Don'ts

- **vs blueprint**: silicon is a physical object -- filled metal, weighted
  strokes, luminous signal traffic. Blueprint is a flat stroke-only DRAWING
  with drafting conventions. NO dashed construction-guide sequences, NO
  dimension-line/label choreography, no stroke-only "schematic" shapes as
  hero elements.
- **vs terminal**: no phosphor-green brights (green law), no scanlines, no
  CRT, no cursor, no typewriter-as-identity -- the designator type-in is an
  annotation beat, never the scene's organizing conceit.
- No gradients, no CSS `filter: blur()`, no text glow, no emoji, no stock
  assets, no randomness (seek-driven/deterministic only).
- No wobble/organic easing; nothing bounces except the small via overshoot.
- Never light a trace that hasn't routed first; never route a curve.

## Linter playbook

Margin strips (left 90 / right 120 / top 240 / bottom 450 px) and the
caption band (y 1260–1470) must stay dark (Y ≤ 140) every frame.
- bg (Y≈17) and board grid (Y≈31) are legal everywhere -- the full-bleed
  board texture is safe by a wide margin.
- Unlit copper `#7A5A2E` is Y≈95 -- under the 140 threshold, so by the math
  an unlit trace MAY touch the margins. Pack rule anyway: **keep all routed
  copper inside the safe area.** Any trace is a candidate to be energized
  (amber Y≈189 = instant fail), pulses overshoot geometry, and glow stacks
  widen strokes -- a margin-touching trace is a trap for later edits. Only
  bg + board grid live in the margins.
- Amber (Y≈189), tin (Y≈156), silkscreen (Y≈207): center-frame only, always.
- The safe box (`--safe-*` / `place_in_safe`) already clears the caption
  band; chips, pads, callouts and via glows must stay inside it.

## Implementation

- HF: `skills/render-shorts/hyperframes/packs/silicon.css` + `silicon-snippet.html`
  (board grid bg, trace draw + pulse, chip drop + pad flash, via pop,
  silkscreen designator type-in).
- Manim: `blai_packs.py` → `PACKS["silicon"]` (+ `mono`, `copper_unlit`,
  `board_grid`, `silkscreen` keys) and helpers `pcb_trace()`,
  `signal_pulse()`, `chip()`, `via()`, `silkscreen_label()` (core API only:
  VMobject, Annulus, Dot, RoundedRectangle, Line, DashedVMobject,
  MoveAlongPath, AddTextLetterByLetter). Hello:
  `pack_hellos/hello_silicon.py`.
