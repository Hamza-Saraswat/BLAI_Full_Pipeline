"""Pack hello: blueprint -- engineering schematic (~5 s).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_blueprint.py HelloBlueprint
    final:  .venv/bin/manim render pack_hellos/hello_blueprint.py HelloBlueprint
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    DL,
    DOWN,
    DR,
    LEFT,
    RIGHT,
    UL,
    UP,
    UR,
    Create,
    FadeIn,
    LaggedStart,
    Rectangle,
    Scene,
    rate_functions,
)

from blai_layout import brand_text, fit_safe_width, place_in_safe
from blai_packs import blueprint_grid, construction_line, ref_marker, use_pack


class HelloBlueprint(Scene):
    """Grid + title at frame 1; dashed guides draw FIRST, then the shape
    they define; annotations fade in after. 5.0 s."""

    def construct(self):
        T = use_pack(self, "blueprint")

        grid = blueprint_grid()

        title = brand_text("SHRINK THE NUMBERS", font_size=58, color=T["fg"])
        fit_safe_width(title, 0.92)
        place_in_safe(title, "top")

        rect = Rectangle(
            width=4.2,
            height=2.4,
            stroke_color=T["fg"],
            stroke_width=T["stroke_width"],
            fill_opacity=0.0,
        )
        place_in_safe(rect, "center")

        guides = [
            construction_line(rect.get_corner(UL) + LEFT * 0.5,
                              rect.get_corner(UR) + RIGHT * 0.5),
            construction_line(rect.get_corner(DL) + LEFT * 0.5,
                              rect.get_corner(DR) + RIGHT * 0.5),
            construction_line(rect.get_corner(UL) + UP * 0.5,
                              rect.get_corner(DL) + DOWN * 0.5),
            construction_line(rect.get_corner(UR) + UP * 0.5,
                              rect.get_corner(DR) + DOWN * 0.5),
        ]

        marker = ref_marker(1)
        marker.next_to(rect.get_corner(UR), UR, buff=0.12)

        label = brand_text("SECTION A-A", font_size=30, color=T["secondary"])
        label.next_to(rect, DOWN, buff=0.4)

        # 0.4 + 1.0 + 1.2 + 0.5 + 1.9 = 5.0 s
        self.add(grid, title)                # paper + hook at frame 1
        self.wait(0.4)
        self.play(                            # guides BEFORE the shape
            LaggedStart(*[Create(g) for g in guides], lag_ratio=0.15),
            run_time=1.0,
            rate_func=rate_functions.linear,
        )
        self.play(Create(rect), run_time=1.2,
                  rate_func=rate_functions.linear)      # drafting-machine
        self.play(FadeIn(marker), FadeIn(label), run_time=0.5)
        self.wait(1.9)
