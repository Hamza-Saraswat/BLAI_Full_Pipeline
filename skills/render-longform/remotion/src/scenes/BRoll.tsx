// Plays data.src (a clip under public/<slug>/) with a dark overlay so the
// on-screen text stays readable. When the clip is missing (calculateMetadata
// could not probe it) a labelled placeholder card renders instead of crashing.
import React from "react";
import { Loop, OffthreadVideo, useVideoConfig } from "remotion";
import { resolveAsset } from "../assets";
import { ACCENT, CARD, ERR, MUTED, OVERLAY, SAFE, TEXT } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";

export const BRoll: React.FC<SceneProps> = (p) => {
  const { fps } = useVideoConfig();
  const src = getString(p.scene.data, "src", "");
  const meta = p.broll?.[p.scene.id];
  const missing = !src || meta?.missing === true;
  const clipFrames = meta?.durationS ? Math.max(1, Math.floor(meta.durationS * fps)) : null;
  const video = !missing ? (
    <OffthreadVideo
      src={resolveAsset(p.assetsBase, src)}
      muted
      pauseWhenBuffering
      style={{ width: "100%", height: "100%", objectFit: "cover" }}
    />
  ) : null;
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      {missing ? (
        <div
          style={{
            position: "absolute",
            left: SAFE.left,
            top: SAFE.top + 80,
            width: SAFE.width,
            height: SAFE.height - 260,
            borderRadius: 24,
            backgroundColor: CARD,
            border: `4px dashed ${ERR}`,
            boxSizing: "border-box",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            textAlign: "center",
            padding: 60,
          }}
        >
          <div style={{ fontSize: 34, fontWeight: 800, letterSpacing: 4, color: ERR }}>B-ROLL PLACEHOLDER</div>
          <div style={{ marginTop: 18, fontSize: 30, fontWeight: 600, color: MUTED, fontFamily: "monospace" }}>{src || "(no data.src)"}</div>
          <div style={{ marginTop: 40, fontSize: 52, fontWeight: 700, color: TEXT, maxWidth: 1300, lineHeight: 1.2 }}>{p.scene.visual_intent}</div>
          <div style={{ marginTop: 40, height: 8, width: 240, backgroundColor: ACCENT, borderRadius: 4 }} />
        </div>
      ) : (
        <div style={{ position: "absolute", inset: 0 }}>
          {clipFrames && clipFrames < p.layout.durationInFrames ? <Loop durationInFrames={clipFrames}>{video}</Loop> : video}
          <div style={{ position: "absolute", inset: 0, backgroundColor: OVERLAY }} />
        </div>
      )}
    </SceneFrame>
  );
};
