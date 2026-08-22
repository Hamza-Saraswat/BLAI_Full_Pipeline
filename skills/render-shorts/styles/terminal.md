# Pack: terminal -- phosphor CLI world (Fireship-adjacent)

Identity: you're inside our box. Monospace everything, prompt cursors,
typewriter reveals, faint scanlines. In-group credibility for the
programmer/tinkerer audience.

## Tokens
- bg: `#060A08` (near-black, green-tinged)
- fg: `#C9F7CF` (pale phosphor) · secondary: `#38E07A` (terminal green)
- accent: `#FFB347` (brand anchor -- reads as amber phosphor; used for the
  key word/number, exactly like other packs)
- muted: fg at 45%
- Fonts -- HF: 'JetBrains Mono', 'Space Mono', Menlo, monospace (self-host
  woff2 or verify renderer resolution). Manim: monospace via
  `terminal_text()` helper (Menlo/registered JetBrains Mono).
- Texture: scanlines `repeating-linear-gradient(0deg, rgba(0,0,0,.14) 0 1px,
  transparent 1px 3px)`; phosphor glow `text-shadow: 0 0 8px currentColor`
  at low alpha; NO flicker animation (motion-boundary rules apply).
- Line: sharp 1–2px, NO rounded corners except the terminal window frame
  (RoundedRect, radius 10, stroke green, header dots).
- Easing personality: **mechanical** -- `steps(10)` / `SteppedEase`,
  typewriter text (`AddTextLetterByLetter` in Manim; per-char stagger or
  ScrambleText decode in HF), cursor `█` blink 530ms.
- Transitions: hard cut, or 200ms scramble-decode on the incoming headline.
- Motifs: `>` prompt prefix on beat lines, `$` for commands, exit-code
  jokes sparingly (`echo $? → 0` as a success beat).

## Topic fit
CLI/how-to/setup topics: vLLM serving, Docker, tokens/keys, Ollama,
network serving, benchmarks-as-command-output. Anything where the natural
visual IS a terminal.

## Implementation
- HF: `skills/render-shorts/hyperframes/packs/terminal.css` + snippet (window frame,
  prompt line, typewriter + cursor GSAP pattern).
- Manim: `blai_layout.py` → `TERMINAL` token set + `terminal_frame()`,
  `terminal_text()`, `cursor_blink()` helpers (core API only:
  RoundedRectangle, Text, AddTextLetterByLetter, Blink).
