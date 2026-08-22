"""Scene s2 -- 100 specialists grid, dense model bottleneck.

Narration: "Picture a company with one hundred specialists. A dense model
wakes every one of them for every question, even to ask what time it is.
All of them drag through the memory doorway, every single word. It crawls."

Visual beats (video-relative times, VO starts at 6.37s):
  0.0–2.0  10x10 grid of dots builds (LaggedStart)
  2.7      label "100 specialists" fades in
  4.9      label transforms to "dense = wake ALL of them"
  5.8–6.7  all 100 dots pulse amber (scale 1→1.3→1)
  7.2      narrow doorway glyph appears at right safe-area edge
  7.6      label fades out
  10.1     dots clump right and jam into a queue at the doorway gap
  10.7     label fades in "it crawls" in error red
  13.03    hold final state (dots stuck queuing)
"""

from manim import *
from blai_layout import *


class SceneS2(Scene):
    def construct(self):
        self.camera.background_color = BRAND_BG

        # === Group A: 100 specialists as a 10x10 grid of dots ===
        spacing = 0.26
        grid_w = 9 * spacing  # 2.34 u
        grid_h = 9 * spacing
        dots = VGroup()
        for i in range(10):
            for j in range(10):
                x = -grid_w / 2 + i * spacing
                y = -grid_h / 2 + j * spacing
                d = Dot(
                    point=SAFE_CENTER + np.array([x, y, 0]),
                    radius=0.04,
                    color=BRAND_FG,
                )
                dots.add(d)

        # === Group B: labels (one shown at a time) ===
        label_y = SAFE_CENTER[1] - grid_h / 2 - 0.6  # below grid, inside safe
        label1 = brand_text("100 specialists", font_size=34)
        label1.move_to(np.array([SAFE_CENTER[0], label_y, 0]))
        label1 = fit_safe_width(label1, 0.8)

        label2 = brand_text("dense = wake ALL of them", font_size=26,
                            color=BRAND_ACCENT)
        label2.move_to(np.array([SAFE_CENTER[0], label_y, 0]))
        label2 = fit_safe_width(label2, 0.9)

        label3 = brand_text("it crawls", font_size=34, color=BRAND_ERROR)
        label3.move_to(np.array([SAFE_CENTER[0], label_y, 0]))
        label3 = fit_safe_width(label3, 0.7)

        # === Group C: doorway glyph (two bars + amber gap) ===
        door_w = 0.12
        door_h = 1.0
        door_gap = 0.22
        door_x = SAFE_X_MAX - 0.4        # inside safe area, near right edge
        door_y = SAFE_CENTER[1]          # vertically centred in safe area

        left_bar = Rectangle(
            width=door_w, height=door_h,
            fill_color=BRAND_FG, fill_opacity=0.8, stroke_width=0,
        )
        right_bar = Rectangle(
            width=door_w, height=door_h,
            fill_color=BRAND_FG, fill_opacity=0.8, stroke_width=0,
        )
        gap_marker = Rectangle(
            width=door_gap, height=0.05,
            fill_color=BRAND_ACCENT, fill_opacity=0.9, stroke_width=0,
        )
        left_bar.move_to(np.array([
            door_x - door_gap / 2 - door_w / 2, door_y, 0]))
        right_bar.move_to(np.array([
            door_x + door_gap / 2 + door_w / 2, door_y, 0]))
        gap_marker.move_to(np.array([door_x, door_y, 0]))
        doorway = VGroup(left_bar, right_bar, gap_marker)

        # Queue target positions: vertical stack at the doorway gap
        queue_x = door_x
        queue_start_y = door_y + 3.0
        queue_spacing = 0.065  # 100 × 0.065 = 6.5 u  (fits in safe area)
        queue_targets = [np.array([queue_x,
                                   queue_start_y - i * queue_spacing, 0])
                         for i in range(100)]

        # ============================================================
        # Animations -- total run_time must = 13.03 ± 0.15 s
        #
        #  2.00  LaggedStart FadeIn grid of 100 dots
        #  0.20  wait
        #  0.50  FadeIn label1 "100 specialists"
        #  1.60  wait
        #  0.60  ReplacementTransform → "dense = wake ALL of them"
        #  0.90  pulse dots amber (scale 1→1.3)
        #  0.90  pulse dots back (scale 1.3→1, colour → FG)
        #  0.50  FadeIn doorway
        #  0.40  FadeOut label2
        #  2.50  all dots clump into queue at doorway
        #  0.60  FadeIn label3 "it crawls"
        #  2.33  hold still (covers 8+ frames at 30fps → end-of-scene rest)
        #  ─────────────────────────────
        #  13.03 total
        # ============================================================

        # 1. Build the 10x10 specialist grid
        self.play(LaggedStart(
            *[FadeIn(d, run_time=0.02) for d in dots],
            lag_ratio=0.02,
        ), run_time=2.0)
        self.wait(0.20)

        # 2. Introduce with label
        self.play(FadeIn(label1, shift=UP * 0.3), run_time=0.50)
        self.wait(1.60)

        # 3. On "wakes every one of them" → label becomes "dense = wake ALL"
        self.play(ReplacementTransform(label1, label2), run_time=0.60)

        # 4. All 100 dots pulse amber
        self.play(*[d.animate.set_color(BRAND_ACCENT).scale(1.3)
                    for d in dots], run_time=0.90)
        self.play(*[d.animate.set_color(BRAND_FG).scale(1 / 1.3)
                    for d in dots], run_time=0.90)

        # 5. On "memory doorway" → doorway glyph appears
        self.play(FadeIn(doorway, shift=RIGHT * 0.3), run_time=0.50)

        # 6. Fade out old label, then all dots clump into the queue
        self.play(FadeOut(label2), run_time=0.40)
        self.play(
            *[d.animate.move_to(queue_targets[i])
              .set_color(BRAND_FG)
              .set_opacity(0.30)
              for i, d in enumerate(dots)],
            run_time=2.50,
        )

        # 7. On "It crawls." → red label
        self.play(FadeIn(label3, shift=UP * 0.3), run_time=0.60)

        # 8. Hold final state
        self.wait(2.33)
