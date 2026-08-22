// Shared motion helpers and small building blocks used by every scene.
import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { CARD, CARD_BORDER, TEXT } from "./constants";
import type { LayoutScene } from "./types";

export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

/** 0..1 spring that starts after `delayFrames`. */
export const useEnter = (delayFrames = 0, damping = 200): number => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - delayFrames, fps, config: { damping, mass: 0.8 } });
};

export const fadeIn = (frame: number, fps: number, seconds = 0.35, delayS = 0): number =>
  interpolate(frame, [delayS * fps, (delayS + seconds) * fps], [0, 1], clamp);

/** Local seconds of a sync point event, or null when the spec did not give one. */
export const syncAt = (layout: LayoutScene, event: string): number | null => {
  const hit = layout.syncPoints.find((p) => p.event === event && p.atS != null);
  return hit && hit.atS != null ? hit.atS : null;
};

export const Card: React.FC<{ style?: React.CSSProperties; children?: React.ReactNode }> = ({ style, children }) => (
  <div
    style={{
      backgroundColor: CARD,
      border: `2px solid ${CARD_BORDER}`,
      borderRadius: 24,
      color: TEXT,
      boxSizing: "border-box",
      ...style,
    }}
  >
    {children}
  </div>
);

/** Fit long text: shrink the font size as the character count grows. */
export const fitFontSize = (text: string, base: number, min: number, perChar = 0.9): number => {
  const len = text.length;
  const size = base - Math.max(0, len - 24) * perChar;
  return Math.max(min, Math.round(size));
};
