"""Pack hello: terminal -- phosphor CLI world (~5 s).

Run from skills/render-shorts/manim/ (manim.cfg cwd rule):
    draft:  .venv/bin/manim render -r 540,960 --fps 15 pack_hellos/hello_terminal.py HelloTerminal
    final:  .venv/bin/manim render pack_hellos/hello_terminal.py HelloTerminal
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import DOWN, LEFT, RIGHT, Scene

from blai_layout import BRAND_OK, place_in_safe
from blai_packs import cursor_blink, terminal_frame, terminal_text, typewriter, use_pack


class HelloTerminal(Scene):
    """Window at frame 1; typed hook line; blinking cursor; exit 0. 5.0 s."""

    def construct(self):
        T = use_pack(self, "terminal")

        win = terminal_frame(6.0, 4.2)
        place_in_safe(win, "center")
        window, dots = win

        line1 = terminal_text(
            "> SHRINK THE NUMBERS",
            font_size=42,
            t2c={">": T["secondary"], "NUMBERS": T["accent"]},
        )
        max_w = window.width - 0.7
        if line1.width > max_w:
            line1.scale_to_fit_width(max_w)
        line1.next_to(dots, DOWN, buff=0.5).align_to(dots, LEFT)

        line2 = terminal_text("exit 0", font_size=34, color=BRAND_OK)
        line2.next_to(line1, DOWN, buff=0.45).align_to(line1, LEFT)

        cur, blink = cursor_blink(blinks=2)

        # 0.4 + 1.1 + 2.65 + 0 (hard add) + 0.85 = 5.0 s
        # (Blink with hide_at_end=False runs blinks*(on+off) + one extra "on")
        self.add(win)                        # window visible at frame 1
        self.wait(0.4)
        self.play(typewriter(line1, run_time=1.1))     # mechanical steps
        cur.next_to(line1, RIGHT, buff=0.12)
        self.add(cur)
        self.play(blink)                                # 2.65 s
        self.add(line2)                                 # hard cut, no fade
        self.wait(0.85)
