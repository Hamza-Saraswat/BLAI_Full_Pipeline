// The mascot talks in the corner. Mouth energy comes from the narration audio
// (useAudioData + visualizeAudio on audioSrc) when the audio is available,
// otherwise from the caption word timing (a word being spoken opens the mouth).
import React from "react";
import { useAudioData, visualizeAudio } from "@remotion/media-utils";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { resolveAsset } from "../assets";
import { ACCENT, CARD, SAFE, TEXT } from "../constants";
import { getString } from "../data";
import { Mascot } from "../mascot/Mascot";
import { SceneFrame } from "../SceneFrame";
import type { CaptionWord, SceneProps } from "../types";
import { clamp } from "../ui";

const MASCOT_SIZE = 460;

/** 0..1 from caption word density around absolute time `t`. */
export const captionEnergy = (words: CaptionWord[], t: number): number => {
  let inWord = false;
  for (const w of words) {
    if (t >= w.start - 0.03 && t <= w.end + 0.03) {
      inWord = true;
      break;
    }
  }
  if (!inWord) return 0;
  // A syllable-like flutter while a word is spoken.
  return 0.45 + 0.55 * Math.abs(Math.sin(2 * Math.PI * 4.5 * t));
};

const Stage: React.FC<{ p: SceneProps; energy: number }> = ({ p, energy }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const headline = getString(p.scene.data, "headline", "");
  const blinkPeriod = Math.round(3.2 * fps);
  const blink = frame % blinkPeriod < 4 ? 1 : 0;
  const bob = Math.sin(frame / 9) * 4 + energy * 6;
  const headIn = interpolate(frame, [0, 0.5 * fps], [0, 1], clamp);
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      <div
        style={{
          position: "absolute",
          right: SAFE.left - 40,
          bottom: 1080 - SAFE.bottom - 40,
          width: MASCOT_SIZE + 120,
          height: MASCOT_SIZE + 120,
          borderRadius: "50%",
          backgroundColor: CARD,
        }}
      />
      <div style={{ position: "absolute", right: SAFE.left + 20, bottom: 1080 - SAFE.bottom + 10, transform: `translateY(${-bob}px)` }}>
        <Mascot energy={energy} blink={blink} size={MASCOT_SIZE} />
      </div>
      {headline ? (
        <div
          style={{
            position: "absolute",
            left: SAFE.left,
            top: SAFE.top + 150,
            width: SAFE.width - MASCOT_SIZE - 200,
            fontSize: 84,
            fontWeight: 800,
            lineHeight: 1.1,
            color: TEXT,
            opacity: headIn,
          }}
        >
          {headline}
          <div style={{ marginTop: 28, height: 10, width: 300 * headIn, backgroundColor: ACCENT, borderRadius: 5 }} />
        </div>
      ) : null}
    </SceneFrame>
  );
};

const WithAudio: React.FC<{ p: SceneProps; src: string }> = ({ p, src }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const audioData = useAudioData(src);
  const absoluteT = p.layout.startS + frame / fps;
  let energy = captionEnergy(p.sceneWords, absoluteT);
  if (audioData) {
    const bins = visualizeAudio({ fps, frame: p.layout.from + frame, audioData, numberOfSamples: 32 });
    const speech = bins.slice(0, 12);
    const mean = speech.reduce((a, b) => a + b, 0) / Math.max(1, speech.length);
    energy = Math.min(1, mean * 2.8);
  }
  return <Stage p={p} energy={energy} />;
};

const WithCaptions: React.FC<{ p: SceneProps }> = ({ p }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return <Stage p={p} energy={captionEnergy(p.sceneWords, p.layout.startS + frame / fps)} />;
};

export const MascotTalk: React.FC<SceneProps> = (p) => {
  if (p.audioSrc) return <WithAudio p={p} src={resolveAsset(p.assetsBase, p.audioSrc)} />;
  return <WithCaptions p={p} />;
};
