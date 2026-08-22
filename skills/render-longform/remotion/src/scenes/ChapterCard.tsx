import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, MUTED, SAFE, TEXT } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, useEnter } from "../ui";

export const ChapterCard: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const number = p.layout.chapter?.number ?? 1;
  const label = getString(p.scene.data, "label", p.layout.chapter?.label ?? "");
  const numIn = useEnter(2);
  const labelIn = useEnter(10);
  const bar = interpolate(frame, [0.3 * fps, 1.1 * fps], [0, 1], clamp);
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords} lowerThird={false}>
      <div style={{ position: "absolute", left: SAFE.left, top: 300, width: SAFE.width }}>
        <div style={{ fontSize: 34, fontWeight: 700, letterSpacing: 6, color: MUTED, opacity: numIn }}>CHAPTER</div>
        <div
          style={{
            fontSize: 260,
            fontWeight: 800,
            lineHeight: 1,
            color: ACCENT,
            opacity: numIn,
            transform: `translateX(${(1 - numIn) * -60}px)`,
          }}
        >
          {String(number).padStart(2, "0")}
        </div>
        <div style={{ height: 10, width: 760 * bar, backgroundColor: ACCENT, borderRadius: 5, marginTop: 16 }} />
        <div
          style={{
            marginTop: 30,
            fontSize: 92,
            fontWeight: 700,
            color: TEXT,
            opacity: labelIn,
            transform: `translateY(${(1 - labelIn) * 30}px)`,
          }}
        >
          {label}
        </div>
      </div>
    </SceneFrame>
  );
};
