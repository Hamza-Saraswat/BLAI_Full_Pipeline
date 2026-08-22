// Word-timed captions for scenes that set data.captions_on: true.
// Pages of at most 6 words (8 is the hard cap for on-screen text), 46 px,
// inside the 5 % safe area. The spoken word is highlighted in the accent color.
import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, CAPTION_PX, SAFE, TEXT } from "./constants";
import { FONT_FAMILY } from "./fonts";
import { pageWords } from "./timing.mjs";
import type { CaptionWord } from "./types";

export const CaptionOverlay: React.FC<{
  sceneWords: CaptionWord[];
  sceneStartS: number;
}> = ({ sceneWords, sceneStartS }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = sceneStartS + frame / fps;
  const pages = React.useMemo(() => pageWords(sceneWords, 6, 2.4), [sceneWords]);
  const page = pages.find((p, i) => {
    const next = pages[i + 1];
    const end = next ? next.start : p.end + 0.4;
    return t >= p.start - 0.12 && t < end;
  });
  if (!page) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: SAFE.left,
        width: SAFE.width,
        bottom: 1080 - SAFE.bottom,
        textAlign: "center",
        fontFamily: FONT_FAMILY,
        fontSize: CAPTION_PX,
        fontWeight: 700,
        lineHeight: 1.2,
        color: TEXT,
      }}
    >
      <span
        style={{
          display: "inline-block",
          padding: "10px 26px",
          borderRadius: 14,
          backgroundColor: "rgba(11, 16, 32, 0.82)",
        }}
      >
        {page.words.map((w, i) => {
          const active = t >= w.start && t < Math.max(w.end, w.start + 0.15);
          return (
            <span key={`${w.start}-${i}`} style={{ color: active ? ACCENT : TEXT }}>
              {i > 0 ? " " : ""}
              {w.word}
            </span>
          );
        })}
      </span>
    </div>
  );
};
