// Lines from on_screen_text, one line on screen at a time, revealed word by
// word. With captions the words follow the narration (a line must start with
// the same words the narration uses to lock on); without captions the words
// are spread evenly over the line's share of the scene.
import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, MAX_WORDS_VISIBLE, SAFE, TEXT } from "../constants";
import { chunkWords, splitWords } from "../data";
import { SceneFrame } from "../SceneFrame";
import { revealTimes } from "../timing.mjs";
import type { SceneProps } from "../types";
import { syncAt } from "../ui";

type Line = { words: string[]; times: number[]; start: number };

export const KineticText: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const durationS = p.layout.durationInFrames / fps;
  const lines = React.useMemo<Line[]>(() => {
    const chunks = (p.scene.on_screen_text ?? []).flatMap((l) => chunkWords(l, MAX_WORDS_VISIBLE));
    const slot = durationS / Math.max(1, chunks.length);
    let cursor = 0;
    return chunks.map((chunk, i) => {
      const words = splitWords(chunk);
      const forced = syncAt(p.layout, `line:${i + 1}`);
      const slotStart = forced ?? i * slot + 0.3;
      const slotEnd = Math.min(durationS, slotStart + slot * 0.6);
      const r = revealTimes(words, p.sceneWords, p.layout.startS, slotStart, slotEnd, cursor);
      cursor = r.cursor;
      const times = forced != null && !r.matched ? r.times.map((x, k) => forced + (x - slotStart) * (k === 0 ? 0 : 1)) : r.times;
      return { words, times, start: times[0] ?? slotStart };
    });
  }, [p.scene.on_screen_text, p.sceneWords, p.layout, durationS]);

  let active = -1;
  for (let i = 0; i < lines.length; i++) if (t >= lines[i].start - 0.05) active = i;
  const line = active >= 0 ? lines[active] : null;
  const size = line ? (line.words.length <= 4 ? 110 : line.words.length <= 6 ? 92 : 76) : 92;

  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords} lowerThird={false}>
      <div
        style={{
          position: "absolute",
          left: SAFE.left + 40,
          right: SAFE.left + 40,
          top: SAFE.top,
          bottom: 1080 - SAFE.bottom,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
        }}
      >
        {line ? (
          <div style={{ fontSize: size, fontWeight: 800, lineHeight: 1.15, color: TEXT }}>
            {line.words.map((w, k) => {
              const at = line.times[k] ?? line.start;
              const age = (t - at) * fps;
              const visible = age >= 0;
              const pop = visible ? Math.min(1, age / 6) : 0;
              return (
                <span
                  key={`${active}-${k}`}
                  style={{
                    display: "inline-block",
                    marginRight: 26,
                    opacity: pop,
                    transform: `translateY(${(1 - pop) * 24}px) scale(${0.9 + 0.1 * pop})`,
                    color: k === line.words.length - 1 && line.words.length > 2 ? ACCENT : TEXT,
                  }}
                >
                  {w}
                </span>
              );
            })}
          </div>
        ) : null}
      </div>
      <div style={{ position: "absolute", left: SAFE.left, bottom: 1080 - SAFE.bottom, display: "flex", gap: 12 }}>
        {lines.map((_, i) => (
          <div
            key={i}
            style={{
              width: i === active ? 44 : 16,
              height: 8,
              borderRadius: 4,
              backgroundColor: i <= active ? ACCENT : "rgba(245,240,232,0.25)",
            }}
          />
        ))}
      </div>
    </SceneFrame>
  );
};
