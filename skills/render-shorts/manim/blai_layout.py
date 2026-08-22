"""BLAI layout helpers for vertical 9:16 (YouTube Shorts) Manim scenes.

Canvas design: 1080 x 1920 px.  Logical frame: 8.0 x 14.2222 scene units,
both pinned in ``manim.cfg``.  (Manim CE only ever derives frame_width FROM
frame_height -- never the reverse -- so in portrait ``frame_height`` must be
set explicitly: ``frame_height = 8.0 * 1920/1080 = 14.2222``.  Verified in
manim/_config/utils.py:669-674, v0.20.1.)

Safe area for SCENE content: 870 x 950 px.  YouTube Shorts UI reserves the
bottom ~450 px and the right ~120 px; the pipeline's caption band occupies
y 1260-1470 (captions are composited there at assembly); we keep 310 px top
and 90 px left clear (matching safe_zone_check.py's strips):

    width:  1080 - 90 (left) - 120 (right)  = 870 px
    height: 1920 - 310 (top) - 660 (bottom incl. caption band) = 950 px

px -> scene units (at the 1080x1920 design size):
    1 px = frame_width / 1080 = 8.0 / 1080 = 0.0074074 u
    (vertical is identical: frame_height / 1920 = 14.2222 / 1920 = 0.0074074 u)

Margins are stored as *fractions* of the live frame dims, so they remain
correct for draft renders at other 9:16 resolutions (e.g. -r 540,960).

All brand colors live here -- import them; never hardcode hex elsewhere.
NOTE: this pipeline is Text()/Pango only.  Tex/MathTex (LaTeX) are banned.
"""

from __future__ import annotations

import numpy as np
from manim import Mobject, Rectangle, config

__all__ = [
    "BRAND_BG",
    "BRAND_FG",
    "BRAND_ACCENT",
    "BRAND_OK",
    "BRAND_ERROR",
    "BRAND_FONT",
    "brand_text",
    "FRAME_W",
    "FRAME_H",
    "SAFE_TOP",
    "SAFE_BOTTOM",
    "SAFE_LEFT",
    "SAFE_RIGHT",
    "SAFE_X_MIN",
    "SAFE_X_MAX",
    "SAFE_Y_MIN",
    "SAFE_Y_MAX",
    "SAFE_W",
    "SAFE_H",
    "SAFE_CENTER",
    "safe_zone_debug",
    "place_in_safe",
    "fit_safe_width",
]

# --- Brand palette (placeholders until the real brand kit lands) -----------
BRAND_BG = "#0B1020"      # near-black navy -- scene background
BRAND_FG = "#F5F0E8"      # warm off-white -- body text
BRAND_ACCENT = "#FFB347"  # amber -- highlights / accents
BRAND_OK = "#7BD88F"      # success green (AGENTS.md token)
BRAND_ERROR = "#FF6B6B"   # error red (AGENTS.md token)
BRAND_FONT = "Sans"       # Pango generic family -- resolves cross-platform;
                          # Pango's default is serif, which is off-brand

# --- Canvas design and UI reservations (px, at 1080x1920) ------------------
CANVAS_W_PX = 1080
CANVAS_H_PX = 1920
MARGIN_TOP_PX = 310      # breathing room below any top-of-screen clutter
MARGIN_BOTTOM_PX = 660   # Shorts UI (450) + the caption band (y 1260-1470):
                         # captions are composited there at assembly, so
                         # scene content must stay above y=1260
MARGIN_LEFT_PX = 90      # MUST match safe_zone_check.py's left_90 strip --
                         # 60 let flush-left content land at 87px and fail QA
MARGIN_RIGHT_PX = 120    # Shorts UI: like/comment/share/remix rail

# --- Scene-unit equivalents (computed from the live manim config) ----------
# Frozen at import time; the CLI has already digested manim.cfg + flags by
# the time a scene module (and hence this module) is imported.
FRAME_W: float = float(config.frame_width)   # 8.0
FRAME_H: float = float(config.frame_height)  # 14.2222...

SAFE_TOP: float = FRAME_H * MARGIN_TOP_PX / CANVAS_H_PX        # 2.2963 u
SAFE_BOTTOM: float = FRAME_H * MARGIN_BOTTOM_PX / CANVAS_H_PX  # 3.3333 u
SAFE_LEFT: float = FRAME_W * MARGIN_LEFT_PX / CANVAS_W_PX      # 0.4444 u
SAFE_RIGHT: float = FRAME_W * MARGIN_RIGHT_PX / CANVAS_W_PX    # 0.8889 u

# Safe-area box in scene coordinates (origin = frame center, +y up)
SAFE_X_MIN: float = -FRAME_W / 2 + SAFE_LEFT    # -3.5556
SAFE_X_MAX: float = FRAME_W / 2 - SAFE_RIGHT    # +3.1111
SAFE_Y_MIN: float = -FRAME_H / 2 + SAFE_BOTTOM  # -3.7778
SAFE_Y_MAX: float = FRAME_H / 2 - SAFE_TOP      # +4.8148
SAFE_W: float = SAFE_X_MAX - SAFE_X_MIN         # 6.6667 u == 900 px
SAFE_H: float = SAFE_Y_MAX - SAFE_Y_MIN         # 8.5926 u == 1160 px
SAFE_CENTER: np.ndarray = np.array(
    [
        (SAFE_X_MIN + SAFE_X_MAX) / 2.0,  # -0.2222 (safe box sits left of center)
        (SAFE_Y_MIN + SAFE_Y_MAX) / 2.0,  # +0.5185 (and above center)
        0.0,
    ]
)

_POSITIONS: dict[str, tuple[str, str]] = {
    "center": ("center", "center"),
    "top": ("center", "top"),
    "bottom": ("center", "bottom"),
    "left": ("left", "center"),
    "right": ("right", "center"),
    "top_left": ("left", "top"),
    "top_right": ("right", "top"),
    "bottom_left": ("left", "bottom"),
    "bottom_right": ("right", "bottom"),
}


def safe_zone_debug(
    color: str = BRAND_ACCENT,
    stroke_width: float = 2.0,
    stroke_opacity: float = 1.0,
) -> Rectangle:
    """Rectangle outlining the safe area.

    Add it while designing (``self.add(safe_zone_debug())``); drop it for
    final renders (or keep it faint to eyeball framing on drafts).
    """
    box = Rectangle(
        width=SAFE_W,
        height=SAFE_H,
        stroke_color=color,
        stroke_width=stroke_width,
        stroke_opacity=stroke_opacity,
        fill_opacity=0.0,
    )
    box.move_to(SAFE_CENTER)
    return box


def brand_text(s: str, **kwargs) -> "Mobject":
    """Brand-conforming Text(): Sans, BOLD, warm-white unless overridden.

    Always prefer this over raw Text() -- Pango's default face is serif,
    which is off-brand and has bitten us in renders.
    """
    from manim import BOLD, Text

    kwargs.setdefault("font", BRAND_FONT)
    kwargs.setdefault("weight", BOLD)
    kwargs.setdefault("color", BRAND_FG)
    return Text(s, **kwargs)


def place_in_safe(mobject: Mobject, position: str = "center", buff: float = 0.15) -> Mobject:
    """Move ``mobject`` (in place, via ``.move_to``) inside the safe area.

    ``position``: one of ``center, top, bottom, left, right, top_left,
    top_right, bottom_left, bottom_right`` (edges/corners sit inside the
    safe-area boundary, inset by ``buff`` scene units).

    ``buff`` defaults to 0.15 u (~20 px): glyph descenders and anti-aliasing
    bleed past a Text mobject's bounding box, so flush-to-boundary placement
    fails the safe-zone linter. Only pass ``buff=0`` for non-text shapes.

    Chain relative layout off an already-placed anchor with ``.next_to``::

        title = place_in_safe(Text("Title"), "top")
        sub = Text("Sub").next_to(title, DOWN, buff=0.4)
    """
    key = position.lower().replace("-", "_").replace(" ", "_")
    try:
        h_key, v_key = _POSITIONS[key]
    except KeyError:
        raise ValueError(
            f"position must be one of {sorted(_POSITIONS)}, got {position!r}"
        ) from None

    half_w = mobject.width / 2.0
    half_h = mobject.height / 2.0
    x = {
        "left": SAFE_X_MIN + buff + half_w,
        "center": (SAFE_X_MIN + SAFE_X_MAX) / 2.0,
        "right": SAFE_X_MAX - buff - half_w,
    }[h_key]
    y = {
        "bottom": SAFE_Y_MIN + buff + half_h,
        "center": (SAFE_Y_MIN + SAFE_Y_MAX) / 2.0,
        "top": SAFE_Y_MAX - buff - half_h,
    }[v_key]
    mobject.move_to(np.array([x, y, 0.0]))
    return mobject


def fit_safe_width(mobject: Mobject, frac: float = 1.0) -> Mobject:
    """Scale ``mobject`` DOWN (never up) so its width <= ``frac * SAFE_W``.

    Run this before ``place_in_safe`` on any Text() whose length you don't
    control -- the #1 vertical-video failure is copy overflowing the rail.
    """
    max_w = SAFE_W * frac
    if mobject.width > max_w:
        mobject.scale_to_fit_width(max_w)
    return mobject
