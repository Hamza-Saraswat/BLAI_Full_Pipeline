# Pack: axon -- calm 2.5D machine-room (dimensional diagram)

Identity: every system is a small glowing diorama you can take apart.
Iso-projected blocks rise from a floor grid, split into exploded views,
and amber data packets ride right-angle conveyors between them.
Reference: Animagraffs exploded diagrams, ByteByteGo system flows.

**The one law of color: structure is cool steel; the DATA is amber.**
Boxes, floors, leaders, labels stay in the graphite/steel family -- the
tokens, packets, and weight cubes moving through them are `#FFB347`.

## Tokens

| role | value | notes |
|---|---|---|
| bg | `#14161F` | graphite-violet, full-bleed |
| floor grid | `#232838` | diamond grid on the floor plane |
| face top | `#3D465E` | iso shading triplet -- flat fills, NO gradients |
| face left | `#2A3147` | (the y-far face, lower-left on screen) |
| face right | `#1D2334` | (the x-far face, lower-right on screen) |
| secondary | `#7FB4C9` | steel-cyan -- leader lines, ticks, sub-labels |
| fg / label | `#D8DEE9` | off-white -- center-frame only (bright!) |
| accent | `#FFB347` | LOCKED brand amber = the data payload |
| ok / bad | `#7BD88F` / `#FF6B6B` | LOCKED semantics |

- Fonts -- HF: **Sora** headlines (600/700 static instances), **Sometype
  Mono** labels (400/700); self-hosted woff2 in `packs/fonts/`. Manim:
  same families as static TTFs in `skills/render-shorts/manim/fonts/` (registered via
  `blai_packs`; `AXON_FONT` / `AXON_MONO` fall back to Sans / Monospace).
- THE iso projection, defined ONCE per lane and used everywhere:
  `x' = (x−y)·cos30°, y' = (x+y)·sin30° − z` (screen y down; Manim flips
  the sign of y'). Blocks are top-rhombus + 2 side faces at 2:1 iso 30°.
- Line/texture: flat fills separated by thin bg-colored strokes (2px);
  dashed steel-cyan leader lines; no gradients, no shadows, no outlines
  brighter than the face they sit on. Manim has no z-buffer -- draw order
  is hand-sorted back-to-front (floor → far blocks → near blocks →
  packets).
- Easing personality: **weighty-premium** -- `power3.inOut` builds,
  `back.out(1.2)` block landings, `sine.inOut` conveyor loops, stagger
  lag ≈0.08. Unhurried; nothing snaps, nothing wobbles.
- Transitions: hard cuts; within a scene, one mechanism moves at a time.
- Motifs: iso extrusion build, exploded-view separation along the iso
  up-axis with dashed leaders, amber packet conveyors on right-angle iso
  paths, floor-grid diamond ripple, face-fold cutaway (vertex tween
  between two polygon states).

## Motion vocabulary (storyboard verbs → axon moves)

| verb | axon move | ease |
|---|---|---|
| reveal | iso extrusion build -- block rises from the floor plane | `power3.inOut` |
| punch | block landing / settle at its exploded position | `back.out(1.2)` |
| stream | amber packet conveyor along right-angle iso paths | `sine.inOut` per segment |
| compare | exploded-view separation, dashed leaders fade in after | `power3.inOut` + landing |
| pulse | floor-grid diamond ripple ordered by distance | opacity/fill stagger, lag 0.08 |
| cutaway | face-fold vertex tween between two polygon states | `power3.inOut` |

## Topic fit

| topic shape | fit |
|---|---|
| system topology: GPU/VRAM flow, RAG architecture, serving stacks | ★ the lane |
| "what happens inside the box" internals with moving data | ★ |
| CLI/tooling walkthroughs | no -- terminal's turf |
| intuition/analogy napkin talk | no -- sketch's turf |
| typography-led hot takes / benchmarks | no -- signal/halftone turf |

## Don'ts (distinctiveness laws)

- vs **blueprint**: axon is filled dimensional shapes; blueprint is flat
  stroke-only drafting. Never render an axon block as an outline.
- No typography-led scenes -- kinetic type is signal's turf; here type
  only labels the diorama.
- No hand wobble, jitter, or roughness -- that's sketch's turf.
- Amber NEVER paints structure (boxes, floors, leaders) -- data only.
- No gradients, no shadows, no Three.js, no perspective cameras -- the
  2.5D is projected math, not a 3D engine.
- No MotionPathPlugin in HTML (manual per-segment tweens); in Manim use
  `MoveAlongPath` over an `iso_path(...)` corner path.

## Linter playbook

- Margins stay dark: bright values (`#D8DEE9` labels, `#7FB4C9` steel,
  `#FFB347` amber, `#3D465E` top faces) live center-frame inside the
  safe area. Only bg `#14161F` and floor `#232838` (both far under the
  Y>140 luma threshold) may approach the margin strips (left 90px,
  right 120px, top 240px, bottom 450px).
- Caption band (y 1260–1470, checked with `--scene`): the safe area's
  bottom edge sits exactly on y 1260 -- keep every polygon, leader
  overshoot and packet path inside the safe box and nothing can leak.
- Exploded stacks grow upward: re-check the separated group against the
  top margin before settling on spacing.
- Deterministic only: paused GSAP core timelines (proxy tweens rewrite
  polygon points through the iso formula -- no plugins); Manim core API,
  Text/Pango digits (no `Integer`/`DecimalNumber` -- they route through
  banned LaTeX).

## Implementation

- HF: `skills/render-shorts/hyperframes/packs/axon.css` + `axon-snippet.html`
  (iso floor grid, proxy-tween extrusion, exploded leaders, two-segment
  packet conveyor).
- Manim: `blai_packs.py` → `PACKS["axon"]` token set + `iso_project()`,
  `iso_prism()`, `iso_explode()`, `iso_path()`, `axon_floor()` helpers;
  hello scene at `pack_hellos/hello_axon.py`.
