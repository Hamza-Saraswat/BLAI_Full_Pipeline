import { AbsoluteFill } from "remotion";
import { CAPTION_BOX } from "./Captions";

// 900x1160 safe area centered on the 1080x1920 canvas.
export const SAFE_AREA = {
  left: (1080 - 900) / 2, // 90
  top: (1920 - 1160) / 2, // 380
  width: 900,
  height: 1160,
} as const;

/** Bottom 450px is covered by the YouTube Shorts UI. */
const SHORTS_UI_TOP = 1920 - 450; // 1470

const labelStyle: React.CSSProperties = {
  position: "absolute",
  fontFamily: "Helvetica, Arial, sans-serif",
  fontSize: 30,
  fontWeight: 700,
  padding: "4px 12px",
  color: "black",
};

/**
 * Debug overlay (enabled via the `showSafeZones` prop): draws the centered
 * 900x1160 safe-area rectangle, the Shorts bottom-UI boundary (y=1470),
 * and the caption anchor line (y=1380).
 */
export const SafeZones: React.FC = () => {
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      {/* Safe area rect */}
      <div
        style={{
          position: "absolute",
          left: SAFE_AREA.left,
          top: SAFE_AREA.top,
          width: SAFE_AREA.width,
          height: SAFE_AREA.height,
          border: "6px dashed #00FF6A",
          boxSizing: "border-box",
        }}
      />
      <div
        style={{
          ...labelStyle,
          left: SAFE_AREA.left,
          top: SAFE_AREA.top - 44,
          backgroundColor: "#00FF6A",
        }}
      >
        SAFE AREA 900x1160 (x 90-990, y 380-1540)
      </div>

      {/* Shorts bottom UI boundary */}
      <div
        style={{
          position: "absolute",
          left: 0,
          top: SHORTS_UI_TOP,
          width: 1080,
          height: 1920 - SHORTS_UI_TOP,
          backgroundColor: "rgba(255, 0, 80, 0.25)",
          borderTop: "6px solid #FF0050",
          boxSizing: "border-box",
        }}
      />
      <div
        style={{
          ...labelStyle,
          left: 12,
          top: SHORTS_UI_TOP + 10,
          backgroundColor: "#FF0050",
          color: "white",
        }}
      >
        SHORTS UI ZONE (bottom 450px, y &gt;= 1470)
      </div>

      {/* Caption bottom-anchor line */}
      <div
        style={{
          position: "absolute",
          left: CAPTION_BOX.left,
          top: CAPTION_BOX.bottomAnchorY,
          width: CAPTION_BOX.width,
          height: 0,
          borderTop: "4px solid #FFB347",
        }}
      />
      <div
        style={{
          ...labelStyle,
          left: CAPTION_BOX.left,
          top: CAPTION_BOX.bottomAnchorY + 8,
          backgroundColor: "#FFB347",
        }}
      >
        caption anchor y=1380 (text grows upward)
      </div>
    </AbsoluteFill>
  );
};
