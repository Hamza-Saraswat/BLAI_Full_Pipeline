// 1280x720 still for one thumbnail concept {words, focus}. Three variants so
// the reviewer can A/B them: 1 words-left / focus-right, 2 focus-first,
// 3 split block. Rules: at most 4 words, dark background, amber accent,
// warm white text, one focal object, readable at 160 px wide.
import React from "react";
import { AbsoluteFill } from "remotion";
import { ACCENT, BG, CARD, TEXT, WORDMARK } from "./constants";
import { splitWords } from "./data";
import { ensureFont, FONT_FAMILY } from "./fonts";
import type { ThumbnailProps } from "./types";

const wordsOf = (s: string): string[] => splitWords(s).slice(0, 4);

/** Largest font size (px) at which `text` fits in `maxWidth` (Inter 800 is about 0.6 em per glyph). */
const fitSize = (text: string, maxWidth: number, base: number): number =>
  Math.round(Math.max(40, Math.min(base, maxWidth / (0.6 * Math.max(1, text.length)))));

/** Pack up to 4 words into at most `maxLines` lines, balancing length. */
const packLines = (words: string[], maxLines: number): string[] => {
  if (words.length <= maxLines) return words;
  const lines: string[] = [];
  const per = Math.ceil(words.length / maxLines);
  for (let i = 0; i < words.length; i += per) lines.push(words.slice(i, i + per).join(" "));
  return lines;
};

export const Thumbnail: React.FC<ThumbnailProps> = ({ concept, variant, series }) => {
  ensureFont();
  const words = wordsOf(concept.words);
  const focus = concept.focus.trim();
  const v = ((variant - 1) % 3 + 3) % 3 + 1;
  const tag = (series ?? "").replace(/-/g, " ").toUpperCase();
  const base: React.CSSProperties = { backgroundColor: BG, fontFamily: FONT_FAMILY, color: TEXT, overflow: "hidden" };

  if (v === 1) {
    const lines = packLines(words, 2);
    const size = Math.min(...lines.map((l) => fitSize(l, 720, 150)), Math.floor(460 / lines.length));
    return (
      <AbsoluteFill style={base}>
        <div style={{ position: "absolute", right: -120, top: -120, width: 620, height: 620, borderRadius: "50%", backgroundColor: CARD }} />
        <div style={{ position: "absolute", left: 70, top: 0, height: 620, width: 740, display: "flex", flexDirection: "column", justifyContent: "center", fontSize: size, fontWeight: 800, lineHeight: 1.02 }}>
          {lines.map((l, i) => (
            <div key={i} style={{ color: i === lines.length - 1 ? ACCENT : TEXT }}>{l}</div>
          ))}
        </div>
        <div
          style={{
            position: "absolute",
            right: 70,
            top: 140,
            width: 400,
            height: 400,
            borderRadius: "50%",
            backgroundColor: ACCENT,
            color: BG,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            textAlign: "center",
            fontSize: fitSize(focus, 340, 150),
            fontWeight: 800,
            lineHeight: 1,
            padding: 30,
            boxSizing: "border-box",
          }}
        >
          {focus}
        </div>
        <div style={{ position: "absolute", left: 70, bottom: 44, fontSize: 30, fontWeight: 800, letterSpacing: 6, color: ACCENT }}>{WORDMARK}</div>
      </AbsoluteFill>
    );
  }

  if (v === 2) {
    return (
      <AbsoluteFill style={{ ...base, alignItems: "center", justifyContent: "center", textAlign: "center" }}>
        <div style={{ fontSize: fitSize(focus, 1100, 300), fontWeight: 800, lineHeight: 1, color: ACCENT }}>{focus}</div>
        <div style={{ marginTop: 30, fontSize: fitSize(words.join(" "), 1140, 110), fontWeight: 800, lineHeight: 1.05, maxWidth: 1140 }}>{words.join(" ")}</div>
        {tag ? <div style={{ position: "absolute", top: 40, fontSize: 28, fontWeight: 800, letterSpacing: 6, color: TEXT, opacity: 0.7 }}>{tag}</div> : null}
        <div style={{ position: "absolute", bottom: 40, fontSize: 28, fontWeight: 800, letterSpacing: 6, color: ACCENT }}>{WORDMARK}</div>
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={base}>
      <div style={{ position: "absolute", left: 0, top: 0, width: 540, height: 720, backgroundColor: ACCENT, display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center", padding: 40, boxSizing: "border-box" }}>
        <div style={{ fontSize: fitSize(focus, 470, 220), fontWeight: 800, lineHeight: 1, color: BG }}>{focus}</div>
      </div>
      <div style={{ position: "absolute", left: 600, right: 50, top: 0, bottom: 0, display: "flex", flexDirection: "column", justifyContent: "center" }}>
        <div style={{ fontSize: Math.min(...packLines(words, 3).map((l) => fitSize(l, 620, 130)), Math.floor(480 / Math.max(1, packLines(words, 3).length))), fontWeight: 800, lineHeight: 1.02 }}>
          {packLines(words, 3).map((l, i) => (
            <div key={i}>{l}</div>
          ))}
        </div>
        <div style={{ marginTop: 34, height: 12, width: 220, backgroundColor: ACCENT, borderRadius: 6 }} />
      </div>
      <div style={{ position: "absolute", right: 50, bottom: 40, fontSize: 28, fontWeight: 800, letterSpacing: 6, color: ACCENT }}>{WORDMARK}</div>
    </AbsoluteFill>
  );
};
