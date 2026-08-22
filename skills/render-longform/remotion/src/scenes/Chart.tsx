// Bar or line chart from data.series [{label, values[]}] with optional
// data.categories (x labels), data.unit, data.title. Flat fills, count-ups,
// axis labels. A sync point `series:<n>` times a series' entry.
import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, CARD_BORDER, DIM, ERR, MUTED, OK, SAFE, TEXT } from "../constants";
import { formatNumber, getArray, getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, syncAt } from "../ui";

type Series = { label: string; values: number[] };
const PALETTE = [ACCENT, OK, TEXT, ERR];

const niceMax = (v: number): number => {
  if (v <= 0) return 1;
  const p = Math.pow(10, Math.floor(Math.log10(v)));
  const m = v / p;
  const step = m <= 1 ? 1 : m <= 2 ? 2 : m <= 2.5 ? 2.5 : m <= 5 ? 5 : 10;
  return step * p;
};

export const Chart: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const kind = getString(p.scene.data, "kind", "bar") === "line" ? "line" : "bar";
  const unit = getString(p.scene.data, "unit", "");
  const title = getString(p.scene.data, "title", "");
  const series = getArray<Series>(p.scene.data, "series")
    .filter((s) => s && Array.isArray(s.values))
    .map((s) => ({ label: String(s.label ?? ""), values: s.values.map((v) => Number(v) || 0) }));
  const nCat = Math.max(0, ...series.map((s) => s.values.length));
  const categories = getArray<unknown>(p.scene.data, "categories").map(String);
  const maxVal = niceMax(Math.max(1e-9, ...series.flatMap((s) => s.values)) * 1.08);
  const decimals = series.some((s) => s.values.some((v) => !Number.isInteger(v))) ? 1 : 0;

  const left = SAFE.left + 150;
  const top = SAFE.top + (title ? 210 : 120);
  const width = SAFE.width - 200;
  const bottom = SAFE.bottom - 230;
  const height = bottom - top;
  const yOf = (v: number) => bottom - (v / maxVal) * height;
  const ticks = [0, 0.25, 0.5, 0.75, 1].map((f) => f * maxVal);
  const entry = (si: number) => syncAt(p.layout, `series:${si + 1}`) ?? 0.4 + si * 0.5;

  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      {title ? (
        <div style={{ position: "absolute", left: SAFE.left, top: SAFE.top + 60, fontSize: 48, fontWeight: 800, color: TEXT }}>{title}</div>
      ) : null}
      <div style={{ position: "absolute", right: SAFE.left, top: SAFE.top + 64, display: "flex", gap: 28 }}>
        {series.map((s, si) => (
          <div key={si} style={{ display: "flex", alignItems: "center", gap: 12, fontSize: 30, fontWeight: 700, color: MUTED }}>
            <span style={{ width: 26, height: 26, borderRadius: 6, backgroundColor: PALETTE[si % PALETTE.length] }} />
            {s.label}
          </div>
        ))}
      </div>
      <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
        {ticks.map((v, i) => (
          <g key={i}>
            <line x1={left} x2={left + width} y1={yOf(v)} y2={yOf(v)} stroke={i === 0 ? DIM : CARD_BORDER} strokeWidth={i === 0 ? 3 : 2} />
            <text x={left - 18} y={yOf(v) + 10} textAnchor="end" fontSize={28} fontWeight={700} fill={MUTED} fontFamily="inherit">
              {formatNumber(v, Number.isInteger(v) ? 0 : decimals)}
            </text>
          </g>
        ))}
        {unit ? (
          <text x={left - 18} y={top - 30} textAnchor="end" fontSize={28} fontWeight={700} fill={ACCENT} fontFamily="inherit">
            {unit}
          </text>
        ) : null}
        {Array.from({ length: nCat }).map((_, ci) => {
          const slotW = width / Math.max(1, nCat);
          const cx = left + slotW * ci + slotW / 2;
          return (
            <text key={ci} x={cx} y={bottom + 48} textAnchor="middle" fontSize={32} fontWeight={700} fill={TEXT} fontFamily="inherit">
              {categories[ci] ?? `#${ci + 1}`}
            </text>
          );
        })}
        {kind === "bar"
          ? series.map((s, si) => {
              const slotW = width / Math.max(1, nCat);
              const barW = Math.min(140, (slotW * 0.7) / Math.max(1, series.length));
              return s.values.map((v, ci) => {
                const at = entry(si) + ci * 0.12;
                const prog = interpolate(t, [at, at + 0.6], [0, 1], clamp);
                const shown = v * prog;
                const groupW = barW * series.length + 12 * (series.length - 1);
                const x = left + slotW * ci + slotW / 2 - groupW / 2 + si * (barW + 12);
                return (
                  <g key={`${si}-${ci}`}>
                    <rect x={x} y={yOf(shown)} width={barW} height={bottom - yOf(shown)} rx={8} fill={PALETTE[si % PALETTE.length]} />
                    {prog > 0.2 ? (
                      <text x={x + barW / 2} y={yOf(shown) - 14} textAnchor="middle" fontSize={34} fontWeight={800} fill={TEXT} fontFamily="inherit">
                        {formatNumber(shown, decimals)}
                      </text>
                    ) : null}
                  </g>
                );
              });
            })
          : series.map((s, si) => {
              const slotW = width / Math.max(1, nCat);
              const pts = s.values.map((v, ci) => ({ x: left + slotW * ci + slotW / 2, y: yOf(v), v }));
              const at = entry(si);
              const prog = interpolate(t, [at, at + 1.4], [0, 1], clamp);
              const d = pts.map((pt, i) => `${i === 0 ? "M" : "L"} ${pt.x} ${pt.y}`).join(" ");
              let len = 0;
              for (let i = 1; i < pts.length; i++) len += Math.hypot(pts[i].x - pts[i - 1].x, pts[i].y - pts[i - 1].y);
              const color = PALETTE[si % PALETTE.length];
              return (
                <g key={si}>
                  <path d={d} fill="none" stroke={color} strokeWidth={8} strokeLinejoin="round" strokeLinecap="round" strokeDasharray={len || 1} strokeDashoffset={(len || 1) * (1 - prog)} />
                  {pts.map((pt, i) => {
                    const shownAt = pts.length > 1 ? i / (pts.length - 1) : 0;
                    if (prog < shownAt) return null;
                    return (
                      <g key={i}>
                        <circle cx={pt.x} cy={pt.y} r={12} fill={color} />
                        <text x={pt.x} y={pt.y - 24 - si * 36} textAnchor="middle" fontSize={32} fontWeight={800} fill={TEXT} fontFamily="inherit">
                          {formatNumber(pt.v, decimals)}
                        </text>
                      </g>
                    );
                  })}
                </g>
              );
            })}
      </svg>
    </SceneFrame>
  );
};
