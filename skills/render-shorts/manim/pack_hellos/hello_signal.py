"""Pack hello: signal -- flagship kinetic-type look (~5 s).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_signal.py HelloSignal
    final:  .venv/bin/manim render pack_hellos/hello_signal.py HelloSignal
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import DOWN, UP, FadeIn, Indicate, Rectangle, Scene

from blai_layout import brand_text, fit_safe_width, place_in_safe
from blai_packs import use_pack


class HelloSignal(Scene):
    """Hook on screen at frame 1; scale-punch beat; accent bar. 5.0 s."""

    def construct(self):
        T = use_pack(self, "signal")

        hook = brand_text(
            "SHRINK THE\nNUMBERS",
            font_size=96,
            t2c={"NUMBERS": T["accent"]},
        )
        fit_safe_width(hook, 0.92)
        place_in_safe(hook, "center")

        bar = Rectangle(
            width=hook.width * 0.55,
            height=0.09,
            stroke_width=0,
            fill_color=T["accent"],
            fill_opacity=1.0,
        ).next_to(hook, DOWN, buff=0.4)

        sub = brand_text("pack: signal", font_size=34, color=T["muted"])
        place_in_safe(sub, "bottom")

        # 0.7 + 0.9 + 0.6 + 0.4 + 0.6 + 1.8 = 5.0 s
        self.add(hook)                       # hook visible at frame 1
        self.wait(0.7)
        self.play(Indicate(hook, scale_factor=1.12, color=T["accent"]),
                  run_time=0.9)
        self.play(FadeIn(bar, shift=UP * 0.25), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.6)
        self.wait(1.8)
