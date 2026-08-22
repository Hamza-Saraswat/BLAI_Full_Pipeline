"""Pack hello: halftone -- midnight comic press (~5 s).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_halftone.py HelloHalftone
    final:  .venv/bin/manim render pack_hellos/hello_halftone.py HelloHalftone
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    DEGREES,
    DOWN,
    UP,
    FadeIn,
    Scene,
    SpinInFromNothing,
    Text,
    rate_functions,
)

from blai_layout import SAFE_CENTER, SAFE_H, SAFE_W, place_in_safe
from blai_packs import benday_grid, comic_panel, punch_card, starburst, use_pack


class HelloHalftone(Scene):
    """Panel + hook card on frame 1; Ben-Day dot screen prints on;
    starburst pops; POW stat card slams in with back.in(2). 5.0 s."""

    def construct(self):
        T = use_pack(self, "halftone")

        # comic panel fills the safe area (the frame margins outside it
        # are the pack's perimeter gutter -- pure bg ink, per THE LAW)
        panel = comic_panel(SAFE_W - 0.2, SAFE_H - 0.2)
        panel.move_to(SAFE_CENTER)

        # hook punch card -- cream face, ink Bangers caps, twin ink
        # shadow. Upper half of the panel, clear of the dot screen.
        hook = punch_card("NO H100\nNEEDED", font_size=88)
        hook.move_to(SAFE_CENTER).shift(UP * 2.4)
        hook.rotate(-2 * DEGREES)

        # Ben-Day screen: 10 x 22 = 220 dots (budget <=600), size-ramp
        # radius r = f(row) -- bigger toward the bottom = fake shading
        dots = benday_grid(
            rows=10,
            cols=22,
            spacing=0.27,
            radius_fn=lambda row, col: 0.035 + 0.009 * row,
            color=T["dot_field"],
        )
        dots.move_to(SAFE_CENTER).shift(DOWN * 2.55)

        # frame 1: panel + hook card already on screen (hook rule)
        self.add(panel, hook)

        # dot screen prints on (row-by-row lag = the press pass)
        self.play(FadeIn(dots, lag_ratio=0.002), run_time=0.9)
        self.wait(0.2)

        # starburst pops behind the stat card position
        burst = starburst(n=12, outer_radius=1.55, inner_radius=0.85)
        burst.move_to(SAFE_CENTER).shift(DOWN * 0.9)
        self.play(SpinInFromNothing(burst), run_time=0.5)

        # POW card slam: built at rest, wound up 1.6x/+6deg, then
        # slammed home with ease_in_back -- the pack's signature impact
        stat = punch_card("40 TOK/S!", font_size=96, face_color=T["accent"])
        stat.move_to(burst.get_center()).rotate(-3 * DEGREES)
        stat.scale(1.6).rotate(6 * DEGREES)
        self.add(stat)
        self.play(
            stat.animate.scale(1 / 1.6).rotate(-6 * DEGREES),
            run_time=0.4,
            rate_func=rate_functions.ease_in_back,
        )

        note = Text(
            "pack: halftone", font=T["mono"], font_size=34, color=T["muted"]
        )
        place_in_safe(note, "bottom")
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)

        # 0.9 + 0.2 + 0.5 + 0.4 + 0.4 + 2.6 = 5.0 s
        self.wait(2.6)
