import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, BG, CHANNEL_HANDLE, MUTED, SAFE, TEXT, WORDMARK } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, fitFontSize, useEnter } from "../ui";

export const TitleCard: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const title = getString(p.scene.data, "title", p.spec.title);
  const tag = getString(p.scene.data, "series_tag", p.spec.series ?? "");
  const tagIn = useEnter(4);
  const titleIn = useEnter(12);
  const line = interpolate(frame, [0.8 * fps, 1.6 * fps], [0, 1], clamp);
  const mark = interpolate(frame, [1.2 * fps, 1.8 * fps], [0, 1], clamp);
  const size = fitFontSize(title, 112, 64, 1.4);
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords} lowerThird={false}>
      <div
        style={{
          position: "absolute",
          left: SAFE.left,
          top: SAFE.top + 180,
          width: SAFE.width - 120,
        }}
      >
        {tag ? (
          <div
            style={{
              display: "inline-block",
              padding: "10px 26px",
              borderRadius: 999,
              backgroundColor: ACCENT,
              color: BG,
              fontSize: 30,
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              opacity: tagIn,
              transform: `translateX(${(1 - tagIn) * -40}px)`,
            }}
          >
            {tag.replace(/-/g, " ")}
          </div>
        ) : null}
        <div
          style={{
            marginTop: 40,
            fontSize: size,
            fontWeight: 800,
            lineHeight: 1.08,
            color: TEXT,
            opacity: titleIn,
            transform: `translateY(${(1 - titleIn) * 40}px)`,
          }}
        >
          {title}
        </div>
        <div style={{ marginTop: 40, height: 12, width: 520 * line, borderRadius: 6, backgroundColor: ACCENT }} />
      </div>
      <div
        style={{
          position: "absolute",
          right: SAFE.left,
          bottom: 1080 - SAFE.bottom,
          textAlign: "right",
          opacity: mark,
          color: MUTED,
          fontSize: 30,
          fontWeight: 700,
          letterSpacing: 3,
        }}
      >
        {WORDMARK}
        <div style={{ fontSize: 24, letterSpacing: 1, fontWeight: 600, marginTop: 6 }}>{CHANNEL_HANDLE}</div>
      </div>
    </SceneFrame>
  );
};
