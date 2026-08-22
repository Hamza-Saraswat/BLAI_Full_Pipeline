# Pack: sketch -- chalk on slate (hand-drawn explainer)

Identity: a sharp friend explaining on a board. Rough strokes, handwritten
type, draw-on reveals. Progressive-revelation energy (+15% retention
evidence for sketch styles) with warmth no other pack has.

**Deliberate constraint: DARK slate, not light paper** -- keeps the brand's
dark-family feed signature and the safe-zone linter's bright-pixel
detection valid. This is "chalkboard", not "notebook".

## Tokens
- bg: `#151C25` (dark slate) + very subtle grain (feTurbulence data-URI at
  low opacity -- static, never animated)
- fg: `#F2EDE4` (chalk white) · accent: `#FFB347` (amber chalk)
- secondary: `#9FD8CB` (mint chalk, sparingly)
- Fonts -- HF: 'Shantell Sans' (headlines, animation-friendly), 'Caveat'
  (annotations); self-hosted woff2. Manim: registered handwriting font via
  `manimpango.register_font` + `sketch_text()` helper (fallback: Sans
  BOLD if registration fails -- report, don't break).
- Line: irregular hand-drawn 3–5px strokes -- HF: rough.js (SEEDED per
  scene id → deterministic renders) or feTurbulence displacement on SVG
  strokes; Manim: `sketch_jitter()` helper (controlled point perturbation,
  seeded) + DashedVMobject accents.
- Easing personality: **human** -- gentle overshoot `back.out(1.2)`,
  draw-on reveals (DrawSVG / `Create`/`Write`), nothing perfectly linear.
- Transitions: chalk-swipe wipe (masked erase), or draw-over.
- Motifs: circled words, underlines that overshoot, arrows with wobble,
  crossed-out wrong answers.

## Topic fit
Intuition-heavy concepts best explained the way you'd sketch them on a napkin --
a rough drawing carries the idea faster than a precise diagram would.

## Implementation
- HF: `skills/render-shorts/hyperframes/packs/sketch.css` + snippet (rough.js seeded
  shape factory, grain overlay, chalk text classes).
- Manim: `blai_layout.py` → `SKETCH` token set + `sketch_jitter(mobject,
  seed)`, `sketch_text()`, `chalk_underline()` helpers.
