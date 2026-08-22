# HyperFrames scene rules, part 2: style packs

Load after `rules/hyperframes-1.md` for scenes with `tool: hyperframes`. The storyboard's `style_pack` picks ONE of seven looks; the specs are frozen in `styles/<pack>.md` and the shared anchors in `styles/README.md`. Paths are relative to `skills/render-shorts/`.

## What a pack ships

- `hyperframes/packs/<pack>.css`: background, texture, fonts (`@font-face` over `packs/fonts/*.woff2`), type classes, line styles, the `.safe` container.
- `hyperframes/packs/<pack>-snippet.html`: the pack's signature techniques wired for HyperFrames (paused GSAP timeline on `window.__timelines`, `data-*` timing). Each snippet is itself a renderable 5 s hello composition: `cp packs/<pack>-snippet.html index.html` to preview it. (v1 kept a rendered `hello-<pack>.mp4` next to each; they are not ported, re-render the snippet if you need a reference clip.)
- `hyperframes/packs/vendor/rough.js`: vendored for the sketch pack.

How a scene worker uses a pack: replace the brand CSS block with `<link rel="stylesheet" href="packs/<pack>.css">` and copy the snippet's patterns into the scene. The anchors never move: amber `#FFB347` accent, dark-family background, `--ok` / `--bad` semantics, identical safe-area geometry (`--safe-left: 90px`, `--safe-right: 160px`, `--safe-top: 240px`, `--safe-bottom: 660px`). Hook text on screen at frame 1; motion only inside frames 9..(N-8); then the standard self-check.

## signal (`packs/signal.css`), the default

Easing personality professional-snappy: `power2.out` entrances, `expo.out` emphasis, scale-punch 1.0 to 1.12 to 1.0 on beats, rise-in-place inside `overflow:hidden` `.line` wrappers, proxy-object count-ups. Don'ts: no texture of any kind, no gradients or shadows, no whole-scene push-ins (margin creep), never slide elements in from off-screen, hard cuts only between scenes.

## terminal (`packs/terminal.css`), phosphor CLI

Easing personality mechanical: stepped or instant reveals (`ease: "none"` plus floor), the typewriter is a proxy tween slicing the command string one char per tick (seek-safe; the cursor hugs the last typed char), cursor `█` blinks via 530 ms timeline `.set()` toggles. Don'ts: no CSS animations for the blink, no flicker or CRT wobble (motion-boundary rules), no rounded corners except the `.term-window` frame (radius 10), no smooth easing curves; this pack snaps. Park the cursor solid before the stable tail.

## sketch (`packs/sketch.css`), chalk on dark slate

Easing personality human: gentle overshoot `back.out(1.2)` pops, `sine.inOut` draw-ons, nothing perfectly linear. All strokes come from the seeded rough.js factory (`pathLength="1"`, then tween `strokeDashoffset` 1 to 0); the grain overlay is static feTurbulence with a fixed seed. Don'ts: NEVER call rough.js without a `seed` (nondeterministic renders), no straight CSS borders for lines (off-brand), never animate the grain, do not drift to a light "notebook" background: it is a chalkboard, and the linter's bright-pixel detection depends on dark margins.

## blueprint (`packs/blueprint.css`), engineering schematic

Easing personality drafting-machine: near-linear `power1.inOut` everywhere; strict order of appearance: dashed construction guides BEFORE the shape, stroke-draw the shape (dasharray fallback), corner ticks, ref markers 1 2 3 in circles, dimension labels fade in AFTER. Don'ts: no fills (stroke-only, `fill: none`), no rounded corners, do not draw dashed guides with dashoffset (dash patterns clash; fade them in), no bouncy or organic eases, "SECTION A-A" labels are used straight, never ironic.

## axon (`packs/axon.css`), calm 2.5D machine-room

Easing personality weighty-premium: `power3.inOut` builds, `back.out(1.2)` block landings, `sine.inOut` conveyor segments, stagger lag about 0.08; unhurried, nothing snaps. THE iso projection is defined ONCE per scene script (`x' = (x - y) * cos30`, `y' = (x + y) * sin30 - z`) and every polygon goes through it: floor-tile diamonds ripple in ordered by distance; the extrusion build is a proxy tween rewriting the prism's three polygon points (top rhombus plus two side faces, a pure function of `h`, seek-safe); exploded views translate slabs along the screen-vertical iso up-axis with dashed steel leaders faded in AFTER (never dashoffset-drawn); amber packets ride right-angle paths as manual per-segment x/y tweens (the projection is linear, so screen-lerp equals world-lerp). SVG groups are DOM-ordered back-to-front like a painter. Don'ts: amber is the DATA payload, never structure (boxes, floors, leaders stay steel); no stroke-only blocks (blueprint's turf), no kinetic type (signal's), no wobble (sketch's); no gradients or shadows, flat face fills only; bright faces, `#D8DEE9` labels, `#7FB4C9` steel and amber stay center-frame; only the `#14161F` bg and `#232838` floor may approach the margins.

## halftone (`packs/halftone.css`), midnight comic press

Easing personality percussive, beat-mapped: punch cards slam in at scale 1.6 to 1.0 with `back.in(2)` plus a rotation snap (opacity pops on hard, `ease: "none"`), dot screens print on with `power4.out` mask reveals, captions plate-flick with `steps(2)`, panels slide across the gutter with `power4.inOut`, at most ONE `elastic.out(1,0.4)` mega-punch per video. Ben-Day dots are an SVG `<pattern>` of equal circles on a 45 degree lattice revealed by tweening a mask `<rect>`'s height (attr tween); shading is a dot-size ramp `r = f(row)`; DOT BUDGET at most 600 visible dots per frame. Card shadows are twin elements offset about 7 px (never box-shadow); the misregistration flick `.set()`s amber and ink text plates 3 px apart for exactly 2 frames at keyframed marks. Don'ts: THE STYLE LAW is a full-perimeter gutter of pure `#16121F`, wider than the linter margin strips (left 90 px or more, right 160 or more, top 240 or more, bottom 660 or more), on EVERY frame; all bright content (cream, amber, dots) stays inside the `overflow: hidden` `.gutter-stage`, and panels slide between inset positions only, never through a margin. No randomness anywhere (patterns are regular grids, flick offsets are keyframed), no rough.js or jitter (sketch's turf), no CRT or scanlines (terminal's turf), no gradients or blur, Bangers is caps-only display, Space Mono never sets a headline.

## silicon (`packs/silicon.css`), matte-black circuit board

Easing personality machine-placement: `power2.inOut` trace routing (45 and 90 degree bends ONLY: every segment horizontal, vertical, or with |dx| equal to |dy|) drawn via the pathLength/dasharray fallback; strictly LINEAR signal pulses (a short amber dash, dasharray `0.08 1.92`, dashoffset 0.08 to -1.0, leads an energized amber copy drawing behind it at the same rate); chip drops scale 1.15 to 1 with `power3.out` plus `.set()` pad flashes; via pops `back.out(1.3)` (the one sanctioned overshoot); silkscreen designators typed via the seek-safe proxy-slice pattern. All glow is 2 or 3 stacked stroke copies (wide low-opacity to thin bright) of the same path. Don'ts: NEVER `filter: blur` or `text-shadow` (Manim parity; type does not glow here), no gradients, green only as the dark board cast (luminance under 40); anything bright is amber, silver, or white, never phosphor green (terminal's); no scanlines, CRT, or typewriter-as-identity; unlike blueprint this is a filled physical OBJECT: no dashed construction-guide choreography, no dimension labels; bright copper, tin, and silkscreen stay inside `.safe`; only the bg and board grid touch the margins, and traces never route a curve.
