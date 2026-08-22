"""Pack hello: sketch -- chalk on dark slate (~5 s).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_sketch.py HelloSketch
    final:  .venv/bin/manim render pack_hellos/hello_sketch.py HelloSketch
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    LEFT,
    RIGHT,
    UP,
    Circle,
    Create,
    FadeIn,
    Scene,
    VGroup,
    Write,
    rate_functions,
)

from blai_layout import SAFE_X_MAX, SAFE_X_MIN, fit_safe_width, place_in_safe
from blai_packs import chalk_underline, sketch_jitter, sketch_text, use_pack


class HelloSketch(Scene):
    """Chalk hook writes on; jittered circle around the key word;
    chalk underline with overshoot. 5.0 s."""

    def construct(self):
        T = use_pack(self, "sketch")

        hook = sketch_text("SHRINK THE\nNUMBERS", font_size=110)
        fit_safe_width(hook, 0.8)   # leave room for the circle's overshoot
        place_in_safe(hook, "center")

        # circle the key word -- "NUMBERS" = the last 7 glyphs (spaces have
        # no glyphs in Text submobjects)
        word = hook[-7:]
        circle = Circle(
            stroke_color=T["accent"],
            stroke_width=T["stroke_width"],
            fill_opacity=0.0,
        )
        circle.surround(word, stretch=True, buffer_factor=1.3)
        sketch_jitter(circle, seed=7, amplitude=0.03)

        under = chalk_underline(hook, color=T["secondary"], seed=3)

        # the circle/underline overshoot past the hook's bbox -- clamp the
        # whole composition back inside the safe box (chalk bleeds, QA doesn't)
        comp = VGroup(hook, circle, under)
        left_over = (SAFE_X_MIN + 0.15) - comp.get_left()[0]
        if left_over > 0:
            comp.shift(RIGHT * left_over)
        right_over = comp.get_right()[0] - (SAFE_X_MAX - 0.15)
        if right_over > 0:
            comp.shift(LEFT * right_over)

        note = sketch_text("pack: sketch", font_size=46, color=T["muted"])
        place_in_safe(note, "bottom")

        # 1.5 + 0.2 + 0.8 + 0.6 + 0.5 + 1.4 = 5.0 s
        self.play(Write(hook), run_time=1.5)            # draw-on reveal
        self.wait(0.2)
        self.play(Create(circle), run_time=0.8)
        self.play(Create(under), run_time=0.6)
        self.play(
            FadeIn(note, shift=UP * 0.25),
            run_time=0.5,
            rate_func=rate_functions.ease_out_back,     # gentle human overshoot
        )
        self.wait(1.4)
