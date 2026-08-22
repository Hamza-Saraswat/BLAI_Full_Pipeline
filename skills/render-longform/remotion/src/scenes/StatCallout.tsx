// One big number (data.value), its unit (data.unit) and a caption
// (data.caption), counted up from zero. Sync point `count` starts the count.
import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, MUTED, SAFE, TEXT } from "../constants";
import { formatNumber, getString, parseNumeric } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { clamp, syncAt } from "../ui";

export const StatCallout: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const parsed = parseNumeric(p.scene.data?.value);
  const unit = getString(p.scene.data, "unit", "");
  const caption = getString(p.scene.data, "caption", "");
  const context = getString(p.scene.data, "context", "");
  const startS = syncAt(p.layout, "count") ?? 0.3;
  const prog = interpolate(t, [startS, startS + 1.3], [0, 1], clamp);
  const eased = 1 - Math.pow(1 - prog, 3);
  const shown = parsed.num == null ? String(p.scene.data?.value ?? "") : `${parsed.prefix}${formatNumber(parsed.num * eased, parsed.decimals)}${parsed.suffix}`;
  const capIn = interpolate(t, [startS + 0.8, startS + 1.3], [0, 1], clamp);
  const digits = shown.length;
  const size = digits <= 4 ? 300 : digits <= 7 ? 240 : 180;
  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      <div
        style={{
          position: "absolute",
          left: SAFE.left,
          right: SAFE.left,
          top: SAFE.top + 60,
          bottom: 1080 - SAFE.bottom + 140,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
        }}
      >
        {context ? <div style={{ fontSize: 40, fontWeight: 700, color: MUTED, marginBottom: 10, opacity: Math.min(1, prog * 3) }}>{context}</div> : null}
        <div style={{ display: "flex", alignItems: "baseline", gap: 24, opacity: Math.min(1, prog * 4 + 0.05) }}>
          <span style={{ fontSize: size, fontWeight: 800, lineHeight: 1, color: TEXT, fontVariantNumeric: "tabular-nums" }}>{shown}</span>
          {unit ? <span style={{ fontSize: Math.round(size * 0.3), fontWeight: 800, color: ACCENT }}>{unit}</span> : null}
        </div>
        <div style={{ marginTop: 24, height: 10, width: 360 * eased, borderRadius: 5, backgroundColor: ACCENT }} />
        {caption ? (
          <div style={{ marginTop: 30, fontSize: 52, fontWeight: 700, color: TEXT, opacity: capIn, maxWidth: 1400, lineHeight: 1.2 }}>{caption}</div>
        ) : null}
      </div>
    </SceneFrame>
  );
};
