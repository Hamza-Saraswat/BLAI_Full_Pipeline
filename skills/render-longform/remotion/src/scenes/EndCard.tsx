// Wordmark plus "next episode" text from data.next_title (8 s minimum).
import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, CHANNEL_HANDLE, MUTED, SAFE, TEXT, WORDMARK } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, useEnter } from "../ui";

export const EndCard: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const next = getString(p.scene.data, "next_title", getString(p.scene.data, "next", ""));
  const label = getString(p.scene.data, "label", "Next episode");
  const markIn = useEnter(2);
  const nextIn = interpolate(frame, [0.8 * fps, 1.5 * fps], [0, 1], clamp);
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords} lowerThird={false}>
      <div style={{ position: "absolute", left: SAFE.left, right: SAFE.left, top: 0, bottom: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", textAlign: "center" }}>
        <div style={{ fontSize: 120, fontWeight: 800, letterSpacing: 10, color: TEXT, opacity: markIn, transform: `scale(${0.9 + 0.1 * markIn})` }}>{WORDMARK}</div>
        <div style={{ marginTop: 10, fontSize: 36, fontWeight: 700, letterSpacing: 4, color: ACCENT, opacity: markIn }}>{CHANNEL_HANDLE}</div>
        {next ? (
          <div style={{ marginTop: 110, opacity: nextIn, transform: `translateY(${(1 - nextIn) * 20}px)` }}>
            <div style={{ fontSize: 32, fontWeight: 700, letterSpacing: 4, color: MUTED, textTransform: "uppercase" }}>{label}</div>
            <div style={{ marginTop: 16, fontSize: 64, fontWeight: 700, color: TEXT, maxWidth: 1500, lineHeight: 1.15 }}>{next}</div>
          </div>
        ) : null}
      </div>
    </SceneFrame>
  );
};
