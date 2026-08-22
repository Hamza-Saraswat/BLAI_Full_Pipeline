// Boxes and arrows from data.nodes [{id,label}] and data.edges [{from,to,label?}].
// Layout: nodes are placed in columns by their depth from the sources (a flow
// left to right); nodes at the same depth stack vertically. Arrows draw after
// both ends are on screen. A sync point `node:<id>` can time a node's entry.
import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, BG, CARD, CARD_BORDER, MUTED, SAFE, TEXT } from "../constants";
import { getArray } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, syncAt } from "../ui";

type Node = { id: string; label: string; accent?: boolean };
type Edge = { from: string; to: string; label?: string };
type Placed = Node & { x: number; y: number; w: number; h: number; order: number; col: number };

const NODE_H = 120;

const layoutNodes = (nodes: Node[], edges: Edge[]): Placed[] => {
  const depth = new Map<string, number>();
  nodes.forEach((n) => depth.set(n.id, 0));
  for (let iter = 0; iter < nodes.length + 1; iter++) {
    let changed = false;
    for (const e of edges) {
      if (!depth.has(e.from) || !depth.has(e.to)) continue;
      const d = (depth.get(e.from) ?? 0) + 1;
      if (d > (depth.get(e.to) ?? 0) && d < nodes.length) {
        depth.set(e.to, d);
        changed = true;
      }
    }
    if (!changed) break;
  }
  const columns = new Map<number, Node[]>();
  nodes.forEach((n) => {
    const d = depth.get(n.id) ?? 0;
    columns.set(d, [...(columns.get(d) ?? []), n]);
  });
  const cols = [...columns.keys()].sort((a, b) => a - b);
  const areaW = SAFE.width - 80;
  const areaH = SAFE.height - 260;
  const colGap = cols.length > 1 ? areaW / cols.length : areaW;
  const nodeW = Math.min(400, colGap - 70);
  const placed: Placed[] = [];
  let order = 0;
  cols.forEach((c, ci) => {
    const list = columns.get(c) ?? [];
    const rowGap = Math.min(NODE_H + 70, areaH / Math.max(1, list.length));
    const totalH = rowGap * list.length;
    list.forEach((n, ri) => {
      placed.push({
        ...n,
        w: nodeW,
        h: NODE_H,
        x: SAFE.left + 40 + ci * colGap + colGap / 2 - nodeW / 2,
        y: SAFE.top + 130 + (areaH - totalH) / 2 + ri * rowGap + (rowGap - NODE_H) / 2,
        order: order++,
        col: ci,
      });
    });
  });
  return placed;
};

export const Diagram: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const nodes = getArray<Node>(p.scene.data, "nodes").filter((n) => n && n.id);
  const edges = getArray<Edge>(p.scene.data, "edges").filter((e) => e && e.from && e.to);
  const placed = React.useMemo(() => layoutNodes(nodes, edges), [nodes, edges]);
  const durationS = p.layout.durationInFrames / fps;
  const stagger = Math.min(0.9, (durationS * 0.5) / Math.max(1, placed.length));
  const entryS = (n: Placed) => syncAt(p.layout, `node:${n.id}`) ?? 0.4 + n.order * stagger;
  const t = frame / fps;
  const byId = new Map(placed.map((n) => [n.id, n]));

  // Edge geometry, shared by the SVG arrows and the HTML labels (labels are
  // HTML so they draw above the boxes, which are HTML too).
  const geom = edges.map((e, i) => {
    const a = byId.get(e.from);
    const b = byId.get(e.to);
    if (!a || !b) return null;
    const startAt = Math.max(entryS(a), entryS(b)) + 0.2;
    const prog = interpolate(t, [startAt, startAt + 0.6], [0, 1], clamp);
    const horizontal = Math.abs(b.x - a.x) > Math.abs(b.y - a.y);
    const x1 = horizontal ? (b.x > a.x ? a.x + a.w : a.x) : a.x + a.w / 2;
    const y1 = horizontal ? a.y + a.h / 2 : b.y > a.y ? a.y + a.h : a.y;
    const x2 = horizontal ? (b.x > a.x ? b.x : b.x + b.w) : b.x + b.w / 2;
    const y2 = horizontal ? b.y + b.h / 2 : b.y > a.y ? b.y : b.y + b.h;
    const mx = (x1 + x2) / 2;
    // Edges that skip a column bow over it so they do not run behind other boxes.
    const skips = Math.abs(b.col - a.col) > 1;
    const bow = skips ? (a.y <= b.y ? -1 : 1) * 150 : 0;
    const d = skips
      ? `M ${x1} ${y1} C ${x1 + (x2 - x1) * 0.3} ${y1 + bow}, ${x2 - (x2 - x1) * 0.3} ${y2 + bow}, ${x2} ${y2}`
      : horizontal
        ? `M ${x1} ${y1} C ${mx} ${y1}, ${mx} ${y2}, ${x2} ${y2}`
        : `M ${x1} ${y1} L ${x2} ${y2}`;
    const len = Math.hypot(x2 - x1, y2 - y1) * 1.2 + Math.abs(bow) * 2;
    const diagonal = horizontal && Math.abs(y2 - y1) > 60;
    // Label: above the apex of a bowed edge; above the boxes for a short straight
    // edge; on the midpoint (with a backing) for a diagonal or vertical edge.
    const labelX = mx;
    const labelY = skips ? (y1 + y2) / 2 + bow * 1.05 : horizontal && !diagonal ? Math.min(a.y, b.y) - 22 : (y1 + y2) / 2;
    return { key: i, label: e.label, prog, d, len, labelX, labelY, backing: diagonal || !horizontal };
  });

  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill={ACCENT} />
          </marker>
        </defs>
        {geom.map((g) =>
          g && g.prog > 0 ? (
            <path
              key={g.key}
              d={g.d}
              fill="none"
              stroke={ACCENT}
              strokeWidth={6}
              strokeDasharray={g.len}
              strokeDashoffset={g.len * (1 - g.prog)}
              markerEnd={g.prog >= 0.98 ? "url(#arrow)" : undefined}
            />
          ) : null,
        )}
      </svg>
      {placed.map((n) => {
        const at = entryS(n);
        const prog = interpolate(t, [at, at + 0.45], [0, 1], clamp);
        if (prog <= 0) return null;
        const size = n.label.length > 22 ? 30 : n.label.length > 14 ? 36 : 44;
        return (
          <div
            key={n.id}
            style={{
              position: "absolute",
              left: n.x,
              top: n.y,
              width: n.w,
              height: n.h,
              borderRadius: 20,
              backgroundColor: n.accent ? ACCENT : CARD,
              border: `3px solid ${n.accent ? ACCENT : CARD_BORDER}`,
              color: n.accent ? BG : TEXT,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              textAlign: "center",
              padding: "0 18px",
              boxSizing: "border-box",
              fontSize: size,
              fontWeight: 700,
              lineHeight: 1.1,
              opacity: prog,
              transform: `scale(${0.85 + 0.15 * prog})`,
            }}
          >
            {n.label}
          </div>
        );
      })}
      {geom.map((g) =>
        g && g.label && g.prog >= 0.98 ? (
          <div
            key={`label-${g.key}`}
            style={{
              position: "absolute",
              left: g.labelX,
              top: g.labelY,
              transform: "translate(-50%, -50%)",
              padding: g.backing ? "4px 12px" : 0,
              borderRadius: 10,
              backgroundColor: g.backing ? BG : "transparent",
              color: MUTED,
              fontSize: 26,
              fontWeight: 700,
              whiteSpace: "nowrap",
            }}
          >
            {g.label}
          </div>
        ) : null,
      )}
    </SceneFrame>
  );
};
