// data.columns: string[]; data.rows: (string|number)[][]; rows reveal one by
// one (sync point `row:<n>` overrides). Winner cells: data.winners[rowIndex] =
// column index (-1 for none) or data.winner_col for a single winning column.
import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, BG, CARD_BORDER, MUTED, SAFE, TEXT } from "../constants";
import { getArray, getNumber, getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { Card, clamp, syncAt } from "../ui";

export const ComparisonTable: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const columns = getArray<unknown>(p.scene.data, "columns").map(String);
  const rows = getArray<unknown[]>(p.scene.data, "rows").map((r) => (Array.isArray(r) ? r.map((c) => (c == null ? "" : String(c))) : [String(r)]));
  const winners = getArray<number>(p.scene.data, "winners");
  const winnerCol = getNumber(p.scene.data, "winner_col", null);
  const title = getString(p.scene.data, "title", "");
  const durationS = p.layout.durationInFrames / fps;
  const t = frame / fps;
  const step = (durationS * 0.65) / Math.max(1, rows.length);
  const headIn = interpolate(t, [0.2, 0.6], [0, 1], clamp);
  const cellPx = columns.length > 4 ? 40 : 44;
  const winnerOf = (ri: number): number => (winners.length > ri ? Number(winners[ri]) : winnerCol ?? -1);

  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      {title ? (
        <div style={{ position: "absolute", left: SAFE.left, top: SAFE.top + 60, fontSize: 48, fontWeight: 800, color: TEXT, opacity: headIn }}>
          {title}
        </div>
      ) : null}
      <Card style={{ position: "absolute", left: SAFE.left, top: SAFE.top + (title ? 140 : 80), width: SAFE.width, overflow: "hidden" }}>
        <div style={{ display: "grid", gridTemplateColumns: `1.3fr repeat(${Math.max(1, columns.length - 1)}, 1fr)`, opacity: headIn }}>
          {columns.map((c, ci) => (
            <div
              key={ci}
              style={{
                padding: "22px 28px",
                fontSize: cellPx,
                fontWeight: 800,
                color: ci === winnerCol ? ACCENT : MUTED,
                borderBottom: `3px solid ${CARD_BORDER}`,
                textTransform: "uppercase",
                letterSpacing: 1,
              }}
            >
              {c}
            </div>
          ))}
        </div>
        {rows.map((row, ri) => {
          const at = syncAt(p.layout, `row:${ri + 1}`) ?? 0.8 + ri * step;
          const prog = interpolate(t, [at, at + 0.35], [0, 1], clamp);
          if (prog <= 0) return null;
          const win = winnerOf(ri);
          return (
            <div
              key={ri}
              style={{
                display: "grid",
                gridTemplateColumns: `1.3fr repeat(${Math.max(1, columns.length - 1)}, 1fr)`,
                opacity: prog,
                transform: `translateX(${(1 - prog) * -30}px)`,
                borderBottom: ri < rows.length - 1 ? `2px solid ${CARD_BORDER}` : "none",
              }}
            >
              {columns.map((_, ci) => {
                const cell = row[ci] ?? "";
                const isWin = ci === win;
                return (
                  <div
                    key={ci}
                    style={{
                      padding: "22px 28px",
                      fontSize: cellPx,
                      fontWeight: ci === 0 || isWin ? 800 : 500,
                      color: isWin ? BG : TEXT,
                      backgroundColor: isWin ? ACCENT : "transparent",
                      borderRadius: isWin ? 12 : 0,
                    }}
                  >
                    {cell}
                  </div>
                );
              })}
            </div>
          );
        })}
      </Card>
    </SceneFrame>
  );
};
