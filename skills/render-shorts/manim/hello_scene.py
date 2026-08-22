"""Smoke-test scene for the BLAI vertical (1080x1920 @ 30) Manim pipeline.

Text()/Pango only -- Tex/MathTex (LaTeX) are banned in this pipeline.

Run from skills/render-shorts/manim/ so manim.cfg is picked up (see SETUP-NOTES.md):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 hello_scene.py HelloVertical
    final:  .venv/bin/manim render hello_scene.py HelloVertical
"""

from manim import FadeIn, Scene, Text, Transform, UP

from blai_layout import (
    BRAND_ACCENT,
    BRAND_BG,
    BRAND_FG,
    fit_safe_width,
    place_in_safe,
    safe_zone_debug,
)


class HelloVertical(Scene):
    """~5 s: hook fades in, transforms into the resolution card, footer rises.

    The faint amber outline is safe_zone_debug() -- everything must stay
    inside it (Shorts UI covers the bottom ~450 px and right ~120 px).
    """

    def construct(self):
        self.camera.background_color = BRAND_BG

        safe = safe_zone_debug(stroke_width=1.5, stroke_opacity=0.25)

        hook = Text("Hello, Shorts.", font_size=72, color=BRAND_FG, weight="BOLD")
        fit_safe_width(hook, 0.9)
        place_in_safe(hook, "center")

        card = Text("1080 × 1920 @ 30", font_size=56, color=BRAND_ACCENT)
        fit_safe_width(card, 0.9)
        place_in_safe(card, "center")

        footer = Text("BLAI Animator", font_size=36, color=BRAND_FG)
        place_in_safe(footer, "bottom")

        # 1.0 + 0.8 + 1.0 + 0.7 + 1.0 + 0.5 = 5.0 s total
        self.play(FadeIn(hook, shift=UP * 0.4), FadeIn(safe), run_time=1.0)
        self.wait(0.8)
        self.play(Transform(hook, card), run_time=1.0)
        self.wait(0.7)
        self.play(FadeIn(footer, shift=UP * 0.3), run_time=1.0)
        self.wait(0.5)
