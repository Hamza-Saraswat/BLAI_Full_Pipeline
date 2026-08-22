# Pack: signal -- the flagship kinetic-type look (videos #1–2, formalized)

Identity: confident modern tech-editorial. Big bold type, flat diagram
shapes, generous dark space. The channel's default voice.

## Tokens
- bg: `#0B1020` flat (no gradients, no texture)
- fg: `#F5F0E8` · accent: `#FFB347` · ok: `#7BD88F` · bad: `#FF6B6B`
- muted: fg at 40–60% opacity
- Fonts -- HF: Inter (700/800), fallback Helvetica Neue/Arial. Manim: `brand_text()` (Sans BOLD).
- Line: solid 4px strokes, rounded rects (radius 12–24px), flat fills
- Easing personality: **professional-snappy** -- `power2.out` entrances,
  `expo.out` emphasis, scale-punch 1.0→1.12→1.0 on beats. Manim: default
  smooth + `Indicate` for punches.
- Transitions: hard cuts between scenes; within scenes, fade-swap one
  element at a time.
- Texture: none. Cleanliness IS the texture.

## Topic fit
Default pack. Best: benchmarks/numbers, comparisons (X vs Y), takes on
news, anything without a better-fitting specialist pack.

## Implementation
- HF: `skills/render-shorts/hyperframes/packs/signal.css` + reference `index.html` (the
  existing hello template is this pack).
- Manim: existing `blai_layout.py` defaults (BRAND_* + brand_text).
