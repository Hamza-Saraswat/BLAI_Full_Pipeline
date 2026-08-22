import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, MUTED, SAFE, TEXT } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, fitFontSize, syncAt } from "../ui";

export const Quote: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const text = getString(p.scene.data, "text", "");
  const attribution = getString(p.scene.data, "attribution", "");
  const startS = syncAt(p.layout, "reveal") ?? 0.3;
  const textIn = interpolate(t, [startS, startS + 0.7], [0, 1], clamp);
  const attrIn = interpolate(t, [startS + 0.9, startS + 1.4], [0, 1], clamp);
  const size = fitFontSize(text, 76, 48, 0.28);
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      <div style={{ position: "absolute", left: SAFE.left + 60, top: SAFE.top + 80, fontSize: 260, lineHeight: 0.8, fontWeight: 800, color: ACCENT, opacity: 0.9 * textIn }}>
        {"“"}
      </div>
      <div
        style={{
          position: "absolute",
          left: SAFE.left + 120,
          right: SAFE.left + 120,
          top: SAFE.top + 250,
          fontSize: size,
          fontWeight: 700,
          lineHeight: 1.25,
          color: TEXT,
          opacity: textIn,
          transform: `translateY(${(1 - textIn) * 24}px)`,
        }}
      >
        {text}
      </div>
      {attribution ? (
        <div style={{ position: "absolute", left: SAFE.left + 120, bottom: 1080 - SAFE.bottom + 150, display: "flex", alignItems: "center", gap: 24, opacity: attrIn }}>
          <div style={{ width: 90, height: 6, backgroundColor: ACCENT, borderRadius: 3 }} />
          <div style={{ fontSize: 40, fontWeight: 700, color: MUTED }}>{attribution}</div>
        </div>
      ) : null}
    </SceneFrame>
  );
};
