"""BLAI style packs for Manim CE scenes -- tokens + pack-specific helpers.

One brand, seven looks (skills/render-shorts/styles/README.md is LOCKED; per-pack token specs
live in skills/render-shorts/styles/{signal,terminal,sketch,blueprint,axon,halftone,silicon}.md).
The storyboard picks ONE pack per video; a scene worker does::

    from blai_layout import *
    from blai_packs import *

    class SceneS3(Scene):
        def construct(self):
            T = use_pack(self, "terminal")   # sets bg, returns token dict
            line = terminal_text("> SHRINK THE NUMBERS")
            ...

Shared anchors (identical in every pack, never override):
- accent  #FFB347 (amber) -- THE highlight color
- ok      #7BD88F / error #FF6B6B (semantic, from blai_layout)
- dark-family backgrounds only (safe-zone linter's bright-pixel detection
  and the feed signature depend on dark margins)
- caption band / safe zones -- geometry never varies by pack

Core-API only: Text/Pango (no LaTeX), RoundedRectangle, Dot, Line,
DashedLine, Circle, Integer, NumberPlane, AddTextLetterByLetter, Blink.
No plugins.  ``sketch_jitter`` is the ONE sanctioned raw-point manipulation
in the whole pipeline (deterministic, seeded, subtle).

Fonts: OFL font files in ``skills/render-shorts/manim/fonts/`` are registered with Pango
at import time via ``manimpango.register_font`` (process-local, idempotent).
- terminal → 'JetBrains Mono' (fallback: Menlo, then generic Monospace)
- sketch   → 'Caveat' (fallback: Sans BOLD + a logged warning)
- axon     → 'Sora' headlines + 'Sometype Mono' labels
- halftone → 'Bangers' display (caps-only) + 'Space Mono' labels
  (fallbacks: Sans BOLD / Monospace)
- silicon  → 'Chakra Petch' headlines + 'IBM Plex Mono' designators
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from manim import (
    BOLD,
    DL,
    DOWN,
    DR,
    LEFT,
    RIGHT,
    UL,
    UP,
    AddTextLetterByLetter,
    Annulus,
    Blink,
    CapStyleType,
    Circle,
    DashedLine,
    DashedVMobject,
    Dot,
    Line,
    LineJointType,
    Mobject,
    MoveAlongPath,
    NumberPlane,
    Polygon,
    Rectangle,
    RoundedRectangle,
    Star,
    Text,
    VGroup,
    VMobject,
    linear,
)

from blai_layout import (
    BRAND_ACCENT,
    BRAND_BG,
    BRAND_ERROR,
    BRAND_FG,
    BRAND_FONT,
    BRAND_OK,
    FRAME_H,
    FRAME_W,
)

__all__ = [
    "PACKS",
    "use_pack",
    "TERMINAL_FONT",
    "SKETCH_FONT",
    # terminal
    "terminal_frame",
    "terminal_text",
    "cursor_blink",
    "typewriter",
    # sketch
    "sketch_text",
    "sketch_jitter",
    "chalk_underline",
    # blueprint
    "blueprint_grid",
    "construction_line",
    "ref_marker",
    # axon
    "AXON_FONT",
    "AXON_MONO",
    "iso_project",
    "iso_prism",
    "iso_explode",
    "iso_path",
    "axon_floor",
    # halftone
    "HALFTONE_FONT",
    "HALFTONE_MONO",
    "benday_grid",
    "punch_card",
    "starburst",
    "comic_panel",
    # silicon
    "SILICON_FONT",
    "SILICON_MONO",
    "pcb_trace",
    "signal_pulse",
    "chip",
    "via",
    "silkscreen_label",
]

# --- Font registration (import-time, idempotent) ----------------------------
_FONTS_DIR = Path(__file__).resolve().parent / "fonts"


def _register_bundled_fonts() -> set[str]:
    """Register every fonts/*.ttf|*.otf with Pango; return available families."""
    import manimpango

    for f in sorted(_FONTS_DIR.glob("*.[to]tf")) if _FONTS_DIR.is_dir() else []:
        try:
            manimpango.register_font(str(f))
        except Exception as exc:  # keep rendering; fall back below
            print(f"[blai_packs] WARNING: could not register {f.name}: {exc}",
                  file=sys.stderr)
    return set(manimpango.list_fonts())


_AVAILABLE_FONTS = _register_bundled_fonts()


def _pick_font(candidates: list[str], fallback: str | None) -> str | None:
    for name in candidates:
        if name in _AVAILABLE_FONTS:
            return name
    return fallback


#: Monospace family for the terminal pack (JetBrains Mono is bundled/OFL).
TERMINAL_FONT: str = _pick_font(
    ["JetBrains Mono", "Menlo", "Monaco", "Courier New"], "Monospace"
)
#: Handwriting family for the sketch pack; ``None`` means fall back to Sans
#: BOLD (sketch_text logs a warning once).
SKETCH_FONT: str | None = _pick_font(["Caveat", "Shantell Sans"], None)
#: Headline family for the axon pack (Sora 600/700 statics bundled/OFL);
#: falls back to the brand Sans.
AXON_FONT: str = _pick_font(["Sora"], BRAND_FONT)
#: Diagram-label family for the axon pack (Sometype Mono statics bundled/OFL).
AXON_MONO: str = _pick_font(
    ["Sometype Mono", "JetBrains Mono", "Menlo"], "Monospace"
)
#: Display family for the halftone pack -- Bangers ships ONE Regular weight
#: and plays a CAPS-ONLY role; ``None`` means fall back to Sans BOLD
#: (punch_card logs a warning once).
HALFTONE_FONT: str | None = _pick_font(["Bangers"], None)
#: Mono family for halftone captions/labels (Space Mono is bundled/OFL).
HALFTONE_MONO: str = _pick_font(
    ["Space Mono", "JetBrains Mono", "Menlo", "Courier New"], "Monospace"
)
#: Squared-techno family for the silicon pack (Chakra Petch is bundled/OFL;
#: static 400/600/700 -- no variable axes).
SILICON_FONT: str = _pick_font(["Chakra Petch"], BRAND_FONT)
#: Mono for reference designators/values -- IBM Plex Mono (bundled OFL,
#: static 400/600).  A DIFFERENT face from the terminal pack's JetBrains
#: Mono; never substitute one for the other.
SILICON_MONO: str = _pick_font(["IBM Plex Mono", "Menlo", "Monaco"], "Monospace")


# --- Token sets --------------------------------------------------------------
def _mix(fg_hex: str, bg_hex: str, alpha: float) -> str:
    """Blend ``fg`` over ``bg`` at ``alpha`` -> opaque hex (for muted text)."""
    fg = [int(fg_hex[i : i + 2], 16) for i in (1, 3, 5)]
    bg = [int(bg_hex[i : i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(f * alpha + b * (1 - alpha)):02X}"
                         for f, b in zip(fg, bg))


PACKS: dict[str, dict] = {
    # skills/render-shorts/styles/signal.md -- flagship kinetic-type look (channel default)
    "signal": {
        "bg": BRAND_BG,               # #0B1020
        "fg": BRAND_FG,               # #F5F0E8
        "accent": BRAND_ACCENT,       # #FFB347 (brand anchor, ALL packs)
        "secondary": _mix(BRAND_FG, BRAND_BG, 0.50),   # muted fg
        "muted": _mix(BRAND_FG, BRAND_BG, 0.50),
        "font": BRAND_FONT,           # Sans BOLD via brand_text()
        "stroke_width": 4.0,          # solid 4px strokes, flat fills
    },
    # skills/render-shorts/styles/terminal.md -- phosphor CLI world
    "terminal": {
        "bg": "#060A08",              # near-black, green-tinged
        "fg": "#C9F7CF",              # pale phosphor
        "accent": BRAND_ACCENT,       # reads as amber phosphor
        "secondary": "#38E07A",       # terminal green (prompt, frame, cursor)
        "muted": _mix("#C9F7CF", "#060A08", 0.45),     # fg at 45%
        "font": TERMINAL_FONT,        # JetBrains Mono / Menlo
        "stroke_width": 2.0,          # sharp 1-2px lines
    },
    # skills/render-shorts/styles/sketch.md -- chalk on DARK slate (never light paper)
    "sketch": {
        "bg": "#151C25",              # dark slate
        "fg": "#F2EDE4",              # chalk white
        "accent": BRAND_ACCENT,       # amber chalk
        "secondary": "#9FD8CB",       # mint chalk (sparingly)
        "muted": _mix("#F2EDE4", "#151C25", 0.50),
        "font": SKETCH_FONT or BRAND_FONT,  # Caveat, else Sans BOLD
        "stroke_width": 4.5,          # irregular hand-drawn 3-5px
    },
    # skills/render-shorts/styles/blueprint.md -- engineering schematic (authority mode)
    "blueprint": {
        "bg": "#0A1A2F",              # deep drafting blue
        "fg": "#E8F1FF",              # blue-white
        "accent": BRAND_ACCENT,       # "annotated in amber" callouts
        "secondary": "#5FB4FF",       # construction/dimension lines (@55%)
        "muted": _mix("#E8F1FF", "#0A1A2F", 0.50),
        "font": BRAND_FONT,           # Sans BOLD labels
        "stroke_width": 2.0,          # 2px stroke-only shapes
        "grid": "#1E3A5F",            # faint grid lines
        "construction_opacity": 0.55,
    },
    # skills/render-shorts/styles/axon.md -- calm 2.5D machine-room (dimensional diagram)
    "axon": {
        "bg": "#14161F",              # graphite-violet
        "fg": "#D8DEE9",              # label off-white (center-frame only)
        "accent": BRAND_ACCENT,       # amber = the DATA payload, never structure
        "secondary": "#7FB4C9",       # steel-cyan (leaders, ticks, sub-labels)
        "muted": _mix("#D8DEE9", "#14161F", 0.50),
        "font": AXON_FONT,            # Sora headlines (labels use "mono")
        "stroke_width": 2.0,          # thin bg-colored strokes between faces
        "face_top": "#3D465E",        # iso face shading triplet -- flat fills,
        "face_left": "#2A3147",       #   NO gradients; light reads from
        "face_right": "#1D2334",      #   upper-left
        "floor": "#232838",           # floor-grid diamond lines
        "mono": AXON_MONO,            # Sometype Mono
    },
    # skills/render-shorts/styles/halftone.md -- midnight comic press (print process)
    "halftone": {
        "bg": "#16121F",              # ink violet-black -- page + perimeter gutter
        "fg": "#F2E8D5",              # cream -- PANEL-INTERIOR ONLY, never margins
        "accent": BRAND_ACCENT,       # the "POW" ink -- bursts, POW cards
        "secondary": "#8B7A9E",       # muted mauve -- kickers, labels
        "muted": _mix("#F2E8D5", "#16121F", 0.55),
        "font": HALFTONE_FONT or BRAND_FONT,  # Bangers (caps-only), else Sans BOLD
        "stroke_width": 8.0,          # chunky ink card borders (panels run 10)
        "ink": "#0E0B16",             # panel-interior fill + twin shadows
        "dot_field": "#5E2A4D",       # deep red-violet Ben-Day screens
        "mono": HALFTONE_MONO,        # Space Mono -- captions/labels, never headlines
    },
    # skills/render-shorts/styles/silicon.md -- matte-black circuit board (hardware mode)
    "silicon": {
        "bg": "#0E1211",              # solder-mask charcoal (green CAST only)
        "fg": "#C9D2CC",              # silkscreen -- center-frame only
        "accent": BRAND_ACCENT,       # ENIG gold -- the energized-copper color
        "secondary": "#8FA0A8",       # tin/nickel (secondary traces, pads)
        "muted": _mix("#C9D2CC", "#0E1211", 0.50),
        "font": SILICON_FONT,         # Chakra Petch headlines/labels
        "stroke_width": 3.0,          # tin weight; copper core = w * 5/3,
                                      # glow copies scale off it (glow law)
        "mono": SILICON_MONO,         # IBM Plex Mono designators/values
        "copper_unlit": "#7A5A2E",    # deep copper shadow -- UNLIT traces
        "board_grid": "#1A211E",      # board grid / chip epoxy (margin-legal)
        "silkscreen": "#C9D2CC",      # silkscreen ink (alias of fg)
    },
}


def use_pack(scene, pack: str) -> dict:
    """Apply pack ``pack`` to ``scene`` (camera bg) and return its tokens.

    Call first thing in ``construct``::

        T = use_pack(self, "blueprint")
        title = brand_text("KV CACHE", color=T["fg"])
    """
    try:
        tokens = PACKS[pack]
    except KeyError:
        raise ValueError(
            f"unknown pack {pack!r}; expected one of {sorted(PACKS)}"
        ) from None
    scene.camera.background_color = tokens["bg"]
    return tokens


# =============================================================================
# terminal
# =============================================================================
def terminal_text(s: str, **kwargs) -> Text:
    """Monospace phosphor Text() for the terminal pack.

    Font resolves to the registered 'JetBrains Mono' (bundled OFL ttf) or
    Menlo.  Regular weight by default -- terminals aren't bold.
    """
    kwargs.setdefault("font", TERMINAL_FONT)
    kwargs.setdefault("color", PACKS["terminal"]["fg"])
    kwargs.setdefault("font_size", 40)
    return Text(s, **kwargs)


def terminal_frame(w: float = 6.0, h: float = 4.5, **kwargs) -> VGroup:
    """Terminal window: RoundedRectangle + 3 header dots (error/accent/ok).

    Radius 10px (~0.075 u) per spec -- the ONE rounded corner in this pack.
    Returns ``VGroup(window, dots)``; position the group with
    ``place_in_safe`` and put typed lines inside the window.
    """
    T = PACKS["terminal"]
    window = RoundedRectangle(
        width=w,
        height=h,
        corner_radius=0.075,
        stroke_color=kwargs.pop("stroke_color", T["secondary"]),
        stroke_width=kwargs.pop("stroke_width", T["stroke_width"]),
        fill_color=T["bg"],
        fill_opacity=1.0,
        **kwargs,
    )
    dots = VGroup(
        *[Dot(radius=0.055, color=c, stroke_width=0)
          for c in (BRAND_ERROR, BRAND_ACCENT, BRAND_OK)]
    ).arrange(RIGHT, buff=0.13)
    dots.next_to(window.get_corner(UL), DR, buff=0.16)
    return VGroup(window, dots)


def cursor_blink(
    height: float = 0.42,
    color: str | None = None,
    blinks: int = 2,
    time_on: float = 0.53,
    time_off: float = 0.53,
) -> tuple[Rectangle, Blink]:
    """Block cursor + its Blink animation (530 ms phases per spec).

    Returns ``(cursor, anim)``.  Position the cursor, then play::

        cur, blink = cursor_blink()
        cur.next_to(line, RIGHT, buff=0.08)
        self.play(blink)          # run_time = blinks * (on + off)
    """
    cur = Rectangle(
        width=height * 0.55,
        height=height,
        stroke_width=0,
        fill_color=color or PACKS["terminal"]["secondary"],
        fill_opacity=1.0,
    )
    anim = Blink(cur, time_on=time_on, time_off=time_off,
                 blinks=blinks, hide_at_end=False)
    return cur, anim


def typewriter(text: Text, time_per_char: float = 0.05, **kwargs) -> AddTextLetterByLetter:
    """Typewriter reveal for a (terminal_)Text mobject.

    Thin wrapper over ``AddTextLetterByLetter`` so scenes get the pack's
    mechanical pacing by default (run_time = chars * time_per_char).
    """
    return AddTextLetterByLetter(text, time_per_char=time_per_char, **kwargs)


# =============================================================================
# sketch
# =============================================================================
_warned_sketch_fallback = False


def sketch_text(s: str, **kwargs) -> Text:
    """Handwritten chalk Text() for the sketch pack (registered 'Caveat').

    Falls back to Sans BOLD with a stderr warning if no handwriting font
    could be registered -- report it, don't break the render.
    """
    global _warned_sketch_fallback
    if SKETCH_FONT is None:
        if not _warned_sketch_fallback:
            print(
                "[blai_packs] WARNING: no handwriting font registered "
                "(fonts/Caveat*.ttf missing?) -- sketch_text falling back to "
                "Sans BOLD.",
                file=sys.stderr,
            )
            _warned_sketch_fallback = True
        kwargs.setdefault("font", BRAND_FONT)
        kwargs.setdefault("weight", BOLD)
    else:
        kwargs.setdefault("font", SKETCH_FONT)
        kwargs.setdefault("weight", BOLD)  # Caveat carries a Bold instance
    kwargs.setdefault("color", PACKS["sketch"]["fg"])
    kwargs.setdefault("font_size", 72)
    return Text(s, **kwargs)


def sketch_jitter(
    mobject: Mobject, seed: int = 0, amplitude: float = 0.02
) -> Mobject:
    """Hand-drawn wobble: deterministic point perturbation (in place).

    THE one sanctioned raw-point manipulation in the pipeline.  Displacement
    is a smooth position-dependent field (sum of seeded sinusoids), so shared
    bezier anchors move together -- no cracks between segments -- and the same
    ``seed`` always renders the same wobble.  Keep ``amplitude`` subtle
    (~0.02 u ≈ 2.7 px at 1080x1920).
    """
    rng = np.random.RandomState(seed)
    n_waves = 3
    fx = rng.uniform(2.0, 6.0, (n_waves, 2))
    px = rng.uniform(0.0, 2.0 * np.pi, n_waves)
    fy = rng.uniform(2.0, 6.0, (n_waves, 2))
    py = rng.uniform(0.0, 2.0 * np.pi, n_waves)

    for sm in mobject.family_members_with_points():
        pts = sm.points.copy()
        x, y = pts[:, 0], pts[:, 1]
        dx = sum(np.sin(fx[i, 0] * x + fx[i, 1] * y + px[i])
                 for i in range(n_waves))
        dy = sum(np.sin(fy[i, 0] * x + fy[i, 1] * y + py[i])
                 for i in range(n_waves))
        pts[:, 0] += (amplitude / n_waves) * dx
        pts[:, 1] += (amplitude / n_waves) * dy
        sm.set_points(pts)
    return mobject


def chalk_underline(
    mobject: Mobject,
    color: str | None = None,
    stroke_width: float | None = None,
    overshoot: float = 0.14,
    buff: float = 0.18,
    seed: int = 1,
) -> VMobject:
    """Jittered chalk underline with hand-drawn overshoot past both ends.

    Endpoints derive from ``mobject``'s corners (no raw coordinates).  The
    right overshoot runs slightly longer -- like a real hand stroke.  Reveal
    with ``Create(...)``.
    """
    T = PACKS["sketch"]
    start = mobject.get_corner(DL) + DOWN * buff + LEFT * overshoot
    end = mobject.get_corner(DR) + DOWN * buff + RIGHT * (overshoot * 1.6)
    line = Line(
        start,
        end,
        color=color or T["accent"],
        stroke_width=stroke_width or T["stroke_width"],
    )
    line.insert_n_curves(12)              # enough anchors for visible wobble
    sketch_jitter(line, seed=seed, amplitude=0.025)
    return line


# =============================================================================
# blueprint
# =============================================================================
def blueprint_grid(major_px: float = 50.0, minor_per_major: int = 5) -> NumberPlane:
    """Full-frame drafting grid: faint #1E3A5F lines, 50px major / 10px minor.

    Faint enough (well under the safe-zone linter's luma threshold) to cover
    the FULL frame -- the grid is the paper, not content.  ``self.add`` it
    first (or FadeIn); everything else draws on top.
    """
    T = PACKS["blueprint"]
    step = major_px * FRAME_W / 1080.0    # px -> scene units (135 px/u)
    grid = NumberPlane(
        x_range=[-FRAME_W / 2, FRAME_W / 2, step],
        y_range=[-FRAME_H / 2, FRAME_H / 2, step],
        background_line_style={
            "stroke_color": T["grid"],
            "stroke_width": 1.0,
            "stroke_opacity": 0.25,
        },
        faded_line_style={
            "stroke_color": T["grid"],
            "stroke_width": 1.0,
            "stroke_opacity": 0.10,
        },
        faded_line_ratio=minor_per_major,  # 50px / 5 = 10px minor
        axis_config={
            "stroke_color": T["grid"],
            "stroke_width": 1.0,
            "stroke_opacity": 0.25,
            "include_ticks": False,
            "include_tip": False,
        },
    )
    return grid


def construction_line(a, b, dash_length: float = 0.12, **kwargs) -> DashedLine:
    """Dashed drafting guide #5FB4FF @ 55% between points ``a`` and ``b``.

    Derive the points from mobjects (``.get_corner()``, ``.get_center()``) or
    ``blai_layout`` constants.  Guides appear BEFORE the shape they define.
    """
    T = PACKS["blueprint"]
    kwargs.setdefault("color", T["secondary"])
    kwargs.setdefault("stroke_opacity", T["construction_opacity"])
    kwargs.setdefault("stroke_width", T["stroke_width"])
    return DashedLine(a, b, dash_length=dash_length, **kwargs)


def ref_marker(n: int, radius: float = 0.17, color: str | None = None) -> VGroup:
    """Small circled reference number (①-style): Circle + digit.

    Amber by default -- the pack's "annotated in amber" callout color.  The
    circle is bg-filled so it stays legible on top of the grid.  Position
    with ``.next_to`` the thing it annotates.

    NOTE: the digit is a brand-font ``Text``, not ``Integer`` --
    ``Integer``/``DecimalNumber`` render digits through ``MathTex`` by
    default (LaTeX is banned and not installed).  If a count-up ever needs
    ``DecimalNumber``, pass ``mob_class=Text``.
    """
    T = PACKS["blueprint"]
    c = color or T["accent"]
    ring = Circle(
        radius=radius,
        stroke_color=c,
        stroke_width=T["stroke_width"],
        fill_color=T["bg"],
        fill_opacity=1.0,
    )
    num = Text(str(int(n)), font=BRAND_FONT, weight=BOLD, color=c)
    num.scale_to_fit_height(radius * 1.05)
    num.move_to(ring.get_center())
    return VGroup(ring, num)


# =============================================================================
# axon
# =============================================================================
_ISO_COS = float(np.cos(np.pi / 6))   # cos 30°
_ISO_SIN = 0.5                        # sin 30°


def iso_project(x: float, y: float, z: float = 0.0) -> np.ndarray:
    """THE axon iso projection -- defined once, used for every point.

    Screen formula (skills/render-shorts/styles/axon.md)::

        x' = (x - y)·cos30°        y'_screen = (x + y)·sin30° - z

    Manim's y axis points UP, so y' flips sign: +z rises, larger x + y
    moves toward the viewer (down-screen).  Returns a scene-space point;
    build the diorama around the world origin, then shift the finished
    groups to place it in the safe area.
    """
    return np.array([
        (x - y) * _ISO_COS,
        -((x + y) * _ISO_SIN - z),
        0.0,
    ])


def iso_prism(
    x: float, y: float, z: float, w: float, d: float, h: float, tokens: dict
) -> VGroup:
    """Iso block: 2 visible side faces + top rhombus, flat pack fills.

    ``(x, y, z)`` is the min corner of the footprint; ``w``/``d`` run along
    world +x/+y, ``h`` along +z.  Three ``Polygon``s (left, right, top --
    painter order) with the pack's face triplet, separated by thin
    bg-colored strokes.  Manim has no z-buffer: order whole prisms
    back-to-front yourself when adding (smaller footprint x + y = farther;
    add it first).  An ``h≈0`` prism ReplacementTransform'd into the full
    one is the extrusion build (same vertex topology -- a pure vertex
    tween, which is also the face-fold cutaway trick).
    """
    def face(corners, fill) -> Polygon:
        return Polygon(
            *[iso_project(*p) for p in corners],
            stroke_color=tokens["bg"],
            stroke_width=tokens["stroke_width"],
            fill_color=fill,
            fill_opacity=1.0,
        )

    z1 = z + h
    left = face(
        [(x, y + d, z), (x + w, y + d, z), (x + w, y + d, z1), (x, y + d, z1)],
        tokens["face_left"],
    )
    right = face(
        [(x + w, y, z), (x + w, y + d, z), (x + w, y + d, z1), (x + w, y, z1)],
        tokens["face_right"],
    )
    top = face(
        [(x, y, z1), (x + w, y, z1), (x + w, y + d, z1), (x, y + d, z1)],
        tokens["face_top"],
    )
    return VGroup(left, right, top)


def iso_explode(group: VGroup, spacing: float = 0.5) -> list[np.ndarray]:
    """Exploded-view shift targets along the iso up-axis (screen UP).

    ``group``'s submobjects are the stacked slabs, bottom-to-top; slab
    ``i`` rises ``i * spacing`` (the bottom one stays put).  Play with::

        shifts = iso_explode(stack, spacing=0.6)
        self.play(*[s.animate.shift(v) for s, v in zip(stack, shifts)],
                  rate_func=rate_functions.ease_in_out_cubic)

    Pair with ``DashedLine`` leaders between the separated faces and fade
    them in AFTER the separation lands.  Re-check the risen group against
    the top of the safe area before settling on ``spacing``.
    """
    return [UP * (spacing * i) for i, _ in enumerate(group)]


def iso_path(points) -> VMobject:
    """Right-angle conveyor path through world ``points`` for MoveAlongPath.

    ``points`` is a sequence of ``(x, y, z)`` world tuples, each projected
    through ``iso_project``; corners stay sharp via
    ``set_points_as_corners``.  Give packets a ``z`` of half their height
    so they ride ON the floor.  The path is a guide, not content -- never
    add it to the scene; drive the amber packet with::

        self.play(MoveAlongPath(packet, route),
                  rate_func=rate_functions.ease_in_out_sine)
    """
    path = VMobject()
    path.set_points_as_corners([iso_project(*p) for p in points])
    return path


def axon_floor(
    cells: int = 3, cell: float = 0.5, tokens: dict | None = None
) -> VGroup:
    """Floor-grid diamonds centered on the world origin, ripple-ordered.

    A ``(2·cells+1)²`` grid of projected z=0 tiles, stroke-only in the
    pack's floor color.  Submobjects are sorted by distance from the
    center, so a plain LaggedStart IS the signature diamond ripple::

        floor = axon_floor().shift(DOWN * 1.7)
        self.play(LaggedStart(*[FadeIn(t) for t in floor], lag_ratio=0.08))

    The floor color is margin-legal (far under the luma threshold), but
    keep the diorama inside the safe area anyway -- exploded stacks and
    packet paths sit on top of it.
    """
    T = tokens or PACKS["axon"]
    half = cell / 2.0
    tiles: list[tuple[float, Polygon]] = []
    for i in range(-cells, cells + 1):
        for j in range(-cells, cells + 1):
            cx, cy = i * cell, j * cell
            tile = Polygon(
                iso_project(cx - half, cy - half, 0.0),
                iso_project(cx + half, cy - half, 0.0),
                iso_project(cx + half, cy + half, 0.0),
                iso_project(cx - half, cy + half, 0.0),
                stroke_color=T["floor"],
                stroke_width=1.5,
                fill_opacity=0.0,
            )
            tiles.append((abs(i) + abs(j), tile))
    tiles.sort(key=lambda t: t[0])
    return VGroup(*[tile for _, tile in tiles])


# =============================================================================
# halftone
# =============================================================================
_HALFTONE_DOT_BUDGET = 600
_warned_halftone_fallback = False


def _halftone_display_font() -> tuple[str, bool]:
    """Resolve the Bangers display font; warn once on fallback."""
    global _warned_halftone_fallback
    if HALFTONE_FONT is None:
        if not _warned_halftone_fallback:
            print(
                "[blai_packs] WARNING: no display font registered "
                "(fonts/Bangers-Regular.ttf missing?) -- punch_card falling "
                "back to Sans BOLD.",
                file=sys.stderr,
            )
            _warned_halftone_fallback = True
        return BRAND_FONT, True
    return HALFTONE_FONT, False


def benday_grid(
    rows: int,
    cols: int,
    spacing: float = 0.30,
    radius: float = 0.055,
    radius_fn=None,
    color: str | None = None,
    stagger: bool = True,
) -> VGroup:
    """Ben-Day dot screen: a REGULAR grid of Circles (VGroup), zero random.

    ``radius_fn(row, col) -> r`` overrides ``radius`` -- the pack's size-ramp
    convention is a deterministic function of row (``r = r0 + k*row``); dot
    ramps ARE the shading substitute (gradients are banned).  ``stagger``
    offsets odd rows by ``spacing/2`` (the classic 45-degree lattice).
    Enforces the pack's DOT BUDGET (<=600 dots per frame)::

        dots = benday_grid(10, 22, radius_fn=lambda r, c: 0.035 + 0.009 * r)
        self.play(FadeIn(dots, lag_ratio=0.002))   # the press pass
    """
    if rows * cols > _HALFTONE_DOT_BUDGET:
        raise ValueError(
            f"benday_grid: {rows}x{cols} = {rows * cols} dots exceeds the "
            f"halftone DOT BUDGET ({_HALFTONE_DOT_BUDGET}/frame) -- use a "
            "coarser grid or a smaller field."
        )
    T = PACKS["halftone"]
    c = color or T["dot_field"]
    dots = VGroup()
    for row in range(rows):
        x_off = (spacing / 2.0) if (stagger and row % 2) else 0.0
        for col in range(cols):
            r = radius_fn(row, col) if radius_fn is not None else radius
            dots.add(
                Circle(radius=r, stroke_width=0, fill_color=c, fill_opacity=1.0)
                .move_to([col * spacing + x_off, -row * spacing, 0.0])
            )
    dots.center()
    return dots


def punch_card(
    text: str,
    font_size: float = 96,
    face_color: str | None = None,
    text_color: str | None = None,
    pad_w: float = 0.42,
    pad_h: float = 0.24,
    corner_radius: float = 0.12,
    shadow_offset=(0.05, -0.065),
) -> VGroup:
    """Chunky Bangers punch card: RoundedRectangle face + twin ink shadow.

    The shadow is a COPY of the face, ink-filled, offset ~7x9px behind
    (``shadow_offset`` in scene units) -- never a blur.  Text is forced
    UPPERCASE (Bangers is a caps-only role).  Cream face by default; pass
    ``face_color=T["accent"]`` for a POW card.  Slam it in with the pack's
    impact ease::

        stat = punch_card("40 TOK/S!", face_color=T["accent"])
        stat.rotate(-3 * DEGREES).scale(1.6).rotate(6 * DEGREES)
        self.add(stat)
        self.play(stat.animate.scale(1 / 1.6).rotate(-6 * DEGREES),
                  run_time=0.4, rate_func=rate_functions.ease_in_back)
    """
    T = PACKS["halftone"]
    font, fell_back = _halftone_display_font()
    kwargs: dict = {"font": font, "font_size": font_size}
    if fell_back:
        kwargs["weight"] = BOLD          # fake the punch if Bangers is missing
    label = Text(text.upper(), color=text_color or T["ink"], **kwargs)

    face = RoundedRectangle(
        width=label.width + 2 * pad_w,
        height=label.height + 2 * pad_h,
        corner_radius=corner_radius,
        stroke_color=T["ink"],
        stroke_width=T["stroke_width"],
        fill_color=face_color or T["fg"],
        fill_opacity=1.0,
    )
    face.move_to(label.get_center())
    shadow = face.copy().set_style(
        fill_color=T["ink"], fill_opacity=1.0, stroke_width=0
    )
    dx, dy = shadow_offset                # (+x, -y) = the down-right press
    shadow.shift(RIGHT * dx + UP * dy)
    return VGroup(shadow, face, label)


def starburst(
    n: int = 12,
    outer_radius: float = 1.6,
    inner_radius: float = 0.9,
    color: str | None = None,
    **kwargs,
) -> Star:
    """Jagged amber ray burst: a core ``Star`` polygon, fill-only.

    Pops BEHIND a reveal -- add it first, then the card on top::

        burst = starburst(n=12)
        self.play(SpinInFromNothing(burst), run_time=0.5)   # or GrowFromCenter
    """
    T = PACKS["halftone"]
    kwargs.setdefault("fill_color", color or T["accent"])
    kwargs.setdefault("fill_opacity", 1.0)
    kwargs.setdefault("stroke_width", 0)
    return Star(n, outer_radius=outer_radius, inner_radius=inner_radius, **kwargs)


def comic_panel(
    w: float,
    h: float,
    border_color: str | None = None,
    stroke_width: float = 10.0,
) -> Rectangle:
    """Comic panel: thick cream-stroked Rectangle, ink fill, SQUARE corners.

    Panels are the halftone stage -- every bright element (cream/amber/
    dots/cards) sits inside one.  THE STYLE LAW: the frame margins outside
    the panel stay pure ``bg`` ink on every frame (left >=90px, right
    >=160px, top >=240px, bottom >=660px) -- size panels to the safe area
    (``comic_panel(SAFE_W - 0.2, SAFE_H - 0.2).move_to(SAFE_CENTER)``) and
    never let content leave them mid-transition.
    """
    T = PACKS["halftone"]
    return Rectangle(
        width=w,
        height=h,
        stroke_color=border_color or T["fg"],
        stroke_width=stroke_width,
        fill_color=T["ink"],
        fill_opacity=1.0,
    )


# =============================================================================
# silicon
# =============================================================================
def pcb_trace(points, lit: bool = False, stroke_width: float | None = None):
    """Copper trace: polyline with ONLY 90°/45° bends.

    ``points`` are corner coordinates (``set_points_as_corners``); the
    routing law is validated -- every segment must be horizontal, vertical,
    or exactly 45° (|dx| == |dy|) -- and an illegal segment raises.  Rounded
    caps/joins: etched copper, not drafted ink.

    ``lit=False`` (default): ONE VMobject in deep copper ``#7A5A2E`` --
    copper always routes unlit first; light only travels routed copper.
    ``lit=True``: the glow-law stack -- a VGroup of THREE copies of the same
    path (wide @ 12% -> mid @ 30% -> core @ 100% amber).  Reveal with
    ``Create(trace, lag_ratio=0.0)`` so the copies draw together (glow is
    stacked strokes, NEVER a blur).  Routing eases
    ``rate_functions.ease_in_out_quad``; energizing is LINEAR.
    """
    T = PACKS["silicon"]
    w = stroke_width or T["stroke_width"] * 5.0 / 3.0   # copper core ~5px
    pts = np.array(
        [[p[0], p[1], p[2] if len(p) > 2 else 0.0] for p in points]
    )
    for i in range(len(pts) - 1):
        dx = float(pts[i + 1][0] - pts[i][0])
        dy = float(pts[i + 1][1] - pts[i][1])
        if not (
            abs(dx) < 1e-6
            or abs(dy) < 1e-6
            or abs(abs(dx) - abs(dy)) < 1e-6
        ):
            raise ValueError(
                f"pcb_trace segment {i} breaks the 45°/90° law: "
                f"dx={dx:.3f}, dy={dy:.3f} (segments must be horizontal, "
                f"vertical, or |dx| == |dy|)"
            )

    def _copy(width: float, opacity: float, color: str) -> VMobject:
        path = VMobject(
            stroke_color=color,
            stroke_width=width,
            stroke_opacity=opacity,
            fill_opacity=0.0,
            cap_style=CapStyleType.ROUND,
            joint_type=LineJointType.ROUND,
        )
        path.set_points_as_corners(pts)
        return path

    if not lit:
        return _copy(w, 1.0, T["copper_unlit"])
    return VGroup(                                   # glow law: wide -> thin
        _copy(w * 4.5, 0.12, T["accent"]),
        _copy(w * 2.4, 0.30, T["accent"]),
        _copy(w, 1.00, T["accent"]),
    )


def signal_pulse(trace, run_time: float = 0.8, color: str | None = None):
    """Amber signal pulse for an already-routed trace.

    Returns ``(pulse, anim)``: a glow-dot stack (wide/mid/core Dots -- the
    glow law again) parked at the trace start, plus its ``MoveAlongPath``,
    rate_func LINEAR per spec -- signal never eases.  ``trace`` may be the
    VGroup from ``pcb_trace(lit=True)`` (the core copy is the path) or any
    VMobject.  Play together with the lit trace's Create so the copper
    lights behind the travelling pulse::

        pulse, anim = signal_pulse(lit)
        self.add(pulse)
        self.play(AnimationGroup(Create(lit, lag_ratio=0.0), anim),
                  run_time=0.8, rate_func=rate_functions.linear)
    """
    T = PACKS["silicon"]
    c = color or T["accent"]
    path = trace[-1] if isinstance(trace, VGroup) else trace
    pulse = VGroup(
        Dot(radius=0.16, color=c, fill_opacity=0.15, stroke_width=0),
        Dot(radius=0.09, color=c, fill_opacity=0.35, stroke_width=0),
        Dot(radius=0.05, color=c, fill_opacity=1.00, stroke_width=0),
    )
    pulse.move_to(path.get_start())
    anim = MoveAlongPath(pulse, path, rate_func=linear, run_time=run_time)
    return pulse, anim


def chip(w: float = 1.8, h: float = 1.8, pins: int = 6,
         label: str = "U1", **kwargs) -> VGroup:
    """Component: FILLED rounded-rect body + pin stubs + mono die label.

    Dark-epoxy body (the board-grid tone) with a tin outline, ``pins``
    Line stubs per side (left/right, tin), label in IBM Plex Mono SEMIBOLD
    silkscreen.  This pack has WEIGHT -- filled metal, never a stroke-only
    hero shape.  Drop onto a footprint with ``FadeIn(chip_g, scale=1.15)``
    + ``rate_functions.ease_out_cubic`` (machine placement: scale settles
    1.15 -> 1, no bounce).  Position with ``place_in_safe`` / ``move_to``.
    """
    T = PACKS["silicon"]
    body = RoundedRectangle(
        width=w,
        height=h,
        corner_radius=0.1,
        stroke_color=T["secondary"],
        stroke_width=T["stroke_width"],
        fill_color=T["board_grid"],
        fill_opacity=1.0,
        **kwargs,
    )
    stub = 0.16
    pin_lines = VGroup()
    for y in np.linspace(-0.35 * h, 0.35 * h, pins):
        for x_edge, direction in ((-w / 2.0, -1.0), (w / 2.0, 1.0)):
            start = np.array([x_edge, float(y), 0.0])
            end = start + np.array([direction * stub, 0.0, 0.0])
            pin_lines.add(
                Line(start, end, color=T["secondary"],
                     stroke_width=T["stroke_width"] * 1.6)
            )
    name = Text(label, font=SILICON_MONO, weight="SEMIBOLD",
                color=T["silkscreen"], font_size=40)
    name.move_to(body.get_center())
    return VGroup(body, pin_lines, name)


def via(radius: float = 0.14, color: str | None = None) -> VGroup:
    """Via: concentric rings at a trace endpoint (Annulus + Dot).

    Amber annulus (plus a wider low-opacity annulus -- the glow law) with a
    bg-colored drill hole on top.  Pop with
    ``GrowFromCenter(via_g, rate_func=rate_functions.ease_out_back)`` --
    the pack's ONE sanctioned overshoot, kept slight.  ``move_to`` the
    trace endpoint (e.g. the last routing point).
    """
    T = PACKS["silicon"]
    c = color or T["accent"]
    glow = Annulus(inner_radius=radius * 0.45, outer_radius=radius * 1.55,
                   fill_color=c, fill_opacity=0.15, stroke_width=0)
    ring = Annulus(inner_radius=radius * 0.45, outer_radius=radius,
                   fill_color=c, fill_opacity=1.0, stroke_width=0)
    hole = Dot(radius=radius * 0.45, color=T["bg"],
               fill_opacity=1.0, stroke_width=0)
    return VGroup(glow, ring, hole)


def silkscreen_label(s: str, font_size: float = 30, num_dashes: int = 24,
                     buff: float = 0.14) -> VGroup:
    """Silkscreen callout: dashed outline box + typed reference designator.

    Returns ``VGroup(box, text)`` -- ``[0]`` is a ``DashedVMobject`` frame
    (reveal with ``Create`` or ``FadeIn``), ``[1]`` the IBM Plex Mono
    designator (type it with ``AddTextLetterByLetter(lbl[1])`` -- both
    literally core API).  Designators read like ``U1``, ``VRAM0``, ``KV$``.
    Silkscreen is bright (Y~207): keep callouts inside the safe area.
    """
    T = PACKS["silicon"]
    text = Text(s, font=SILICON_MONO, weight="SEMIBOLD",
                color=T["silkscreen"], font_size=font_size)
    frame = Rectangle(
        width=text.width + 2.0 * buff + 0.1,
        height=text.height + 2.0 * buff,
        stroke_color=T["silkscreen"],
        stroke_width=2.0,
        fill_opacity=0.0,
    )
    box = DashedVMobject(frame, num_dashes=num_dashes)
    box.move_to(text.get_center())
    return VGroup(box, text)
