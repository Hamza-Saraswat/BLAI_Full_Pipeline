# Pack: blueprint -- engineering schematic (authority mode)

Identity: the systems-diagram look of someone who has actually built it.
Faint grid, stroke-only shapes drawing themselves, dashed construction
lines, stencil headlines. ByteByteGo-class authority signal.

## Tokens
- bg: `#0A1A2F` (deep drafting blue)
- grid: 1px lines `#1E3A5F` at 25% opacity, 50px major / 10px minor
- fg: `#E8F1FF` (blue-white) · accent: `#FFB347` (brand anchor -- the
  "annotated in amber" callout color)
- construction: `#5FB4FF` at 55% (dashed guides, dimension lines)
- Fonts -- HF: 'Allerta Stencil' (headlines only), Inter (labels/body).
  Manim: Sans BOLD labels; stencil headline via registered font if
  available, else Sans BOLD + letter-spacing.
- Line: 2px stroke-only shapes (fill_opacity 0), sharp corners, dashed
  guides (`DashedLine` / CSS dashed borders), corner tick marks,
  small circled reference numbers ①②③.
- Easing personality: **drafting-machine** -- near-linear `power1.inOut`,
  line-draw reveals (DrawSVG / `Create`), guides appear BEFORE the shape
  they define, dimension labels fade in after.
- Transitions: grid-pan (content slides along grid axes), draw/erase.
- Motifs: title-block corner stamp (small wordmark box), dimension arrows,
  "SECTION A-A" style labels used straight (never ironic).

## Topic fit
Architecture/"how it works" internals: KV cache, vLLM request flow,
unified memory, networking/serving diagrams, image-vs-container-vs-cache.

## Implementation
- HF: `skills/render-shorts/hyperframes/packs/blueprint.css` + snippet (grid bg,
  stroke-draw pattern, tick/label components).
- Manim: `blai_layout.py` → `BLUEPRINT` token set + `blueprint_grid()`
  (NumberPlane background_line_style, clipped to safe area),
  `construction_line()`, `ref_marker(n)` helpers.
