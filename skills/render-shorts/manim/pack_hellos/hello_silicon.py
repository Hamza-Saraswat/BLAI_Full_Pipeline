"""Pack hello: silicon -- matte-black circuit board (~5 s).

Requires the silicon block merged into blai_packs.py (PACKS["silicon"] +
pcb_trace/signal_pulse/chip/via/silkscreen_label -- see the pack's patch).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_silicon.py HelloSilicon
    final:  .venv/bin/manim render pack_hellos/hello_silicon.py HelloSilicon
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    BOLD,
    RIGHT,
    AnimationGroup,
    Create,
    FadeIn,
    FadeOut,
    GrowFromCenter,
    AddTextLetterByLetter,
    NumberPlane,
    Scene,
    Text,
    rate_functions,
)

from blai_layout import FRAME_H, FRAME_W, SAFE_X_MIN, fit_safe_width, place_in_safe
from blai_packs import (
    SILICON_FONT,
    chip,
    pcb_trace,
    signal_pulse,
    silkscreen_label,
    use_pack,
    via,
)


class HelloSilicon(Scene):
    """Board grid + Chakra Petch hook at frame 1; copper routes UNLIT
    (45°/90° bends only), a LINEAR amber pulse energizes it, a via pops
    at the endpoint, the chip drops onto its footprint, and a silkscreen
    designator types in. Machine placement -- no wobble. 5.0 s."""

    def construct(self):
        T = use_pack(self, "silicon")

        # board grid: 60 px squares of the pack's dark grid tone -- it is
        # the board, not content, so full-frame is fine (Y~31, margin-legal)
        step = 60.0 * FRAME_W / 1080.0
        grid = NumberPlane(
            x_range=[-FRAME_W / 2, FRAME_W / 2, step],
            y_range=[-FRAME_H / 2, FRAME_H / 2, step],
            background_line_style={
                "stroke_color": T["board_grid"],
                "stroke_width": 1.0,
                "stroke_opacity": 1.0,
            },
            faded_line_ratio=1,
            axis_config={
                "stroke_color": T["board_grid"],
                "stroke_width": 1.0,
                "stroke_opacity": 1.0,
                "include_ticks": False,
                "include_tip": False,
            },
        )

        title = Text(
            "SHRINK THE NUMBERS",
            font=SILICON_FONT,
            weight=BOLD,
            color=T["fg"],
            font_size=58,
        )
        fit_safe_width(title, 0.92)
        place_in_safe(title, "top")

        # trace route, 45°/90° law: H, then 45° (|dx| == |dy|), then H.
        # pcb_trace validates the discipline and raises on a bad segment.
        x0 = SAFE_X_MIN + 0.4
        pts = [
            [x0, 1.6, 0.0],
            [x0 + 1.4, 1.6, 0.0],
            [x0 + 2.4, 0.6, 0.0],   # 45°: dx = 1.0, dy = -1.0
            [x0 + 4.0, 0.6, 0.0],
        ]
        trace_unlit = pcb_trace(pts)                 # deep copper, no light
        trace_lit = pcb_trace(pts, lit=True)         # stacked-stroke amber
        pulse, pulse_anim = signal_pulse(trace_lit, run_time=0.8)

        via_pop = via()
        via_pop.move_to(pts[-1])

        gpu = chip(1.8, 1.8, pins=6, label="GPU")
        gpu.move_to([0.0, -1.2, 0.0])   # bottom edge stays above the caption band

        silk = silkscreen_label("VRAM0")
        silk.next_to(gpu, RIGHT, buff=0.25)

        # 0.4 + 1.0 + 0.8 + 0.4 + 0.5 + 0.3 + 0.4 + 1.2 = 5.0 s
        self.add(grid, title)                        # board + hook at frame 1
        self.wait(0.4)
        self.play(                                   # copper routes, UNLIT
            Create(trace_unlit),
            run_time=1.0,
            rate_func=rate_functions.ease_in_out_quad,
        )
        self.add(pulse)                              # signal: pulse leads,
        self.play(                                   # amber lights behind it
            AnimationGroup(
                Create(trace_lit, lag_ratio=0.0),    # all 3 glow copies together
                pulse_anim,
            ),
            run_time=0.8,
            rate_func=rate_functions.linear,         # pulses are LINEAR, always
        )
        self.play(                                   # via pop -- the ONE overshoot
            GrowFromCenter(via_pop, rate_func=rate_functions.ease_out_back),
            FadeOut(pulse),                          # pulse dissolves into the via
            run_time=0.4,
        )
        self.play(                                   # chip drops onto footprint
            FadeIn(gpu, scale=1.15),
            run_time=0.5,
            rate_func=rate_functions.ease_out_cubic,
        )
        self.play(Create(silk[0]), run_time=0.3)     # dashed silkscreen box
        self.play(                                   # designator types in
            AddTextLetterByLetter(silk[1], run_time=0.4)
        )
        self.wait(1.2)
