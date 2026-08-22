"""Pack hello: axon -- calm 2.5D machine-room (~5 s).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_axon.py HelloAxon
    final:  .venv/bin/manim render pack_hellos/hello_axon.py HelloAxon
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    BOLD,
    DOWN,
    FadeIn,
    LaggedStart,
    MoveAlongPath,
    ReplacementTransform,
    Scene,
    Text,
    rate_functions,
)

from blai_layout import fit_safe_width, place_in_safe
from blai_packs import (
    AXON_FONT,
    axon_floor,
    iso_path,
    iso_prism,
    iso_project,
    use_pack,
)


class HelloAxon(Scene):
    """Sora hook at frame 1; floor-grid diamond ripple, iso extrusion
    build (vertex tween), a lid landing on top, then an amber packet
    riding a two-segment right-angle conveyor. 5.0 s."""

    def construct(self):
        T = use_pack(self, "axon")

        title = Text(
            "SHRINK THE NUMBERS",
            font=AXON_FONT,
            weight=BOLD,
            color=T["fg"],
            font_size=58,
        )
        fit_safe_width(title, 0.92)
        place_in_safe(title, "top")

        # The diorama is built around the world origin (everything goes
        # through THE iso projection), then dropped into the lower half
        # of the safe area as a group shift. 1.15 keeps the amber packet's
        # whole conveyor above the caption band (y -2.22 in scene units).
        drop = DOWN * 1.15

        floor = axon_floor(cells=3, cell=0.5).shift(drop)

        # extrusion build: vertex tween from the h≈0 prism to the full
        # one (identical 3-polygon topology -- a pure point interpolation)
        slab_flat = iso_prism(-0.55, -0.55, 0.0, 1.1, 1.1, 0.001, T).shift(drop)
        slab = iso_prism(-0.55, -0.55, 0.0, 1.1, 1.1, 0.8, T).shift(drop)

        # the lid lands on the slab with a weighty overshoot
        lid = iso_prism(-0.55, -0.55, 0.8, 1.1, 1.1, 0.45, T).shift(drop)

        # amber packet (THE data payload) + its right-angle conveyor;
        # z = half the cube height so it rides ON the floor plane
        packet = iso_prism(-0.11, -0.11, 0.0, 0.22, 0.22, 0.22, T)
        packet.set_fill(T["accent"]).set_stroke(T["bg"], T["stroke_width"])
        route = iso_path(
            [(-1.6, 0.55, 0.11), (0.9, 0.55, 0.11), (0.9, 0.0, 0.11)]
        ).shift(drop)
        packet.move_to(iso_project(-1.6, 0.55, 0.11) + drop)

        # 0.4 + 0.8 + 1.0 + 0.5 + 0.3 + 1.1 + 0.9 = 5.0 s
        self.add(title)                       # hook at frame 1
        self.wait(0.4)
        self.play(                             # floor-grid diamond ripple
            LaggedStart(*[FadeIn(t) for t in floor], lag_ratio=0.08),
            run_time=0.8,
        )
        self.add(slab_flat)                    # painter order: floor->slab
        self.play(                             # iso extrusion build
            ReplacementTransform(slab_flat, slab),
            run_time=1.0,
            rate_func=rate_functions.ease_in_out_cubic,  # power3.inOut
        )
        self.play(                             # block landing
            FadeIn(lid, shift=DOWN * 0.35),
            run_time=0.5,
            rate_func=rate_functions.ease_out_back,      # back.out(1.2)
        )
        self.play(FadeIn(packet), run_time=0.3)          # payload appears
        self.play(                             # packet conveyor (in front:
            MoveAlongPath(packet, route),      # added last, path has the
            run_time=1.1,                      # larger x + y -- nearer)
            rate_func=rate_functions.ease_in_out_sine,   # sine.inOut
        )
        self.wait(0.9)
