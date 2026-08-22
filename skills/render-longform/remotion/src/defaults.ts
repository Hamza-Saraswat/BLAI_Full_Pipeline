// Default props so Remotion Studio shows something without a props file.
// Real renders always pass --props written by scripts/render_longform.py.
import type { EpisodeProps, ThumbnailProps } from "./types";

export const DEFAULT_EPISODE_PROPS: EpisodeProps = {
  spec: {
    slug: "2026-01-01-studio-preview",
    title: "DeepSeek V4 Flash on a DGX Spark: the real numbers",
    target_duration_s: 480,
    series: "benchmarks",
    chapters: [
      { label: "The setup", starts_at_scene: "s01" },
      { label: "The numbers", starts_at_scene: "s03" },
      { label: "What it means", starts_at_scene: "s05" },
    ],
    scenes: [
      { id: "s01", type: "title-card", narration: "Studio preview title.", est_duration_s: 6, visual_intent: "title" },
      { id: "s02", type: "kinetic-text", narration: "Three things to know.", est_duration_s: 8, visual_intent: "three lines", on_screen_text: ["One model, one box", "Forty tokens a second", "No cloud bill"] },
      { id: "s03", type: "stat-callout", narration: "Forty-one point seven tokens per second.", est_duration_s: 8, visual_intent: "big number", data: { value: "41.7", unit: "tok/s", caption: "generation speed, Q4" } },
      { id: "s04", type: "chart", narration: "Speed by quantization.", est_duration_s: 10, visual_intent: "bars", data: { kind: "bar", unit: "tok/s", categories: ["Q4", "Q8", "FP8"], series: [{ label: "DGX Spark", values: [41.7, 28.3, 24.9] }] } },
      { id: "s05", type: "mascot-talk", narration: "So what does that mean for you?", est_duration_s: 8, visual_intent: "mascot", on_screen_text: ["What it means for your box"] },
      { id: "s06", type: "end-card", narration: "Next time: two Sparks, one model.", est_duration_s: 8, visual_intent: "end card", data: { next_title: "Two Sparks, one model" } },
    ],
    thumbnail_concepts: [
      { words: "41 tokens a second", focus: "41.7" },
      { words: "Fits in one box", focus: "128 GB" },
      { words: "No cloud bill", focus: "$0" },
    ],
  },
  captions: [],
  audioSrc: null,
  captures: {},
  assetsBase: "",
  showSafeArea: false,
};

export const DEFAULT_THUMBNAIL_PROPS: ThumbnailProps = {
  concept: { words: "41 tokens a second", focus: "41.7" },
  title: "DeepSeek V4 Flash on a DGX Spark: the real numbers",
  variant: 1,
  series: "benchmarks",
};
