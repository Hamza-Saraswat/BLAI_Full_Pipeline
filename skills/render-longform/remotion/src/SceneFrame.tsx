// The wrapper every scene renders inside: background, optional chapter badge,
// lower-third on-screen text (at most 8 words visible, 52 px) and, when the
// scene asks for it, the word-timed captions. Everything stays in the safe area.
import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { CaptionOverlay } from "./Captions";
import {
  ACCENT,
  BG,
  CAPTION_BAND_PX,
  DIM,
  LOWER_THIRD_PX,
  MAX_WORDS_VISIBLE,
  MUTED,
  SAFE,
  TEXT,
} from "./constants";
import { chunkWords, getBool } from "./data";
import { FONT_FAMILY } from "./fonts";
import type { CaptionWord, LayoutScene, SpecScene } from "./types";
import { clamp } from "./ui";

const NO_BADGE = new Set(["title-card", "chapter-card", "end-card"]);

export const ChapterBadge: React.FC<{ number: number; label: string }> = ({ number, label }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const opacity = interpolate(frame, [0, 0.4 * fps], [0, 1], clamp);
  return (
    <div
      style={{
        position: "absolute",
        left: SAFE.left,
        top: SAFE.top,
        display: "flex",
        alignItems: "center",
        gap: 14,
        opacity,
        fontFamily: FONT_FAMILY,
        fontSize: 26,
        fontWeight: 700,
        letterSpacing: 2,
        color: MUTED,
        textTransform: "uppercase",
      }}
    >
      <span style={{ color: ACCENT }}>{String(number).padStart(2, "0")}</span>
      <span style={{ width: 2, height: 22, backgroundColor: DIM }} />
      <span>{label}</span>
    </div>
  );
};

/** Cycles the scene's on_screen_text lines across its duration. */
export const LowerThird: React.FC<{ lines: string[]; durationInFrames: number; raised: boolean }> = ({
  lines,
  durationInFrames,
  raised,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const chunks = React.useMemo(() => lines.flatMap((l) => chunkWords(l, MAX_WORDS_VISIBLE)), [lines]);
  if (chunks.length === 0) return null;
  const slot = durationInFrames / chunks.length;
  const idx = Math.min(chunks.length - 1, Math.floor(frame / slot));
  const local = frame - idx * slot;
  const enter = interpolate(local, [0, 0.3 * fps], [0, 1], clamp);
  const leave = idx < chunks.length - 1 ? interpolate(local, [slot - 0.25 * fps, slot], [1, 0], clamp) : 1;
  const opacity = Math.min(enter, leave);
  const bottom = 1080 - SAFE.bottom + (raised ? CAPTION_BAND_PX : 0);
  return (
    <div
      style={{
        position: "absolute",
        left: SAFE.left,
        bottom,
        maxWidth: SAFE.width,
        display: "flex",
        alignItems: "stretch",
        gap: 22,
        opacity,
        transform: `translateY(${(1 - enter) * 18}px)`,
        fontFamily: FONT_FAMILY,
      }}
    >
      <div style={{ width: 10, borderRadius: 5, backgroundColor: ACCENT }} />
      <div
        style={{
          fontSize: LOWER_THIRD_PX,
          fontWeight: 700,
          lineHeight: 1.15,
          color: TEXT,
          padding: "8px 0",
        }}
      >
        {chunks[idx]}
      </div>
    </div>
  );
};

export const SafeAreaOverlay: React.FC = () => (
  <div
    style={{
      position: "absolute",
      left: SAFE.left,
      top: SAFE.top,
      width: SAFE.width,
      height: SAFE.height,
      border: "3px dashed rgba(123, 216, 143, 0.8)",
      boxSizing: "border-box",
      pointerEvents: "none",
    }}
  />
);

export const SceneFrame: React.FC<{
  scene: SpecScene;
  layout: LayoutScene;
  sceneWords: CaptionWord[];
  /** Scenes that draw on_screen_text themselves (kinetic-text) disable the lower third. */
  lowerThird?: boolean;
  children?: React.ReactNode;
}> = ({ scene, layout, sceneWords, lowerThird = true, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const captionsOn = getBool(scene.data, "captions_on", false) && sceneWords.length > 0;
  const opacity = interpolate(frame, [0, 0.25 * fps], [0, 1], clamp);
  const lines = scene.on_screen_text ?? [];
  return (
    <AbsoluteFill style={{ backgroundColor: BG, color: TEXT, fontFamily: FONT_FAMILY, opacity }}>
      {children}
      {layout.chapter && !NO_BADGE.has(scene.type) ? (
        <ChapterBadge number={layout.chapter.number} label={layout.chapter.label} />
      ) : null}
      {lowerThird && lines.length > 0 ? (
        <LowerThird lines={lines} durationInFrames={layout.durationInFrames} raised={captionsOn} />
      ) : null}
      {captionsOn ? <CaptionOverlay sceneWords={sceneWords} sceneStartS={layout.startS} /> : null}
    </AbsoluteFill>
  );
};
