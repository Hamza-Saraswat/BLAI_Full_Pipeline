// Placeholder mascot. A round head, two eyes that blink, and a mouth whose
// opening follows `energy` (0..1). Replace this file with the real design;
// keep the props so MascotTalk does not change.
import React from "react";
import { ACCENT, BG, TEXT } from "../constants";

export type MascotProps = {
  /** 0 = mouth closed, 1 = fully open. */
  energy: number;
  /** 0..1, 1 = eyes closed. */
  blink?: number;
  size?: number;
  style?: React.CSSProperties;
};

export const MASCOT_DEFAULT_SIZE = 320;

export const Mascot: React.FC<MascotProps> = ({ energy, blink = 0, size = MASCOT_DEFAULT_SIZE, style }) => {
  const e = Math.max(0, Math.min(1, energy));
  const mouthHeight = 3 + e * 20;
  const mouthWidth = 26 + e * 10;
  const eyeOpen = Math.max(0.08, 1 - blink);
  return (
    <svg width={size} height={size} viewBox="0 0 200 200" style={style} role="img" aria-label="mascot">
      {/* body */}
      <rect x="58" y="132" width="84" height="56" rx="22" fill={ACCENT} />
      <rect x="86" y="150" width="28" height="14" rx="7" fill={BG} opacity="0.35" />
      {/* antenna */}
      <line x1="100" y1="30" x2="100" y2="12" stroke={TEXT} strokeWidth="5" strokeLinecap="round" />
      <circle cx="100" cy="10" r="7" fill={ACCENT} />
      {/* head */}
      <circle cx="100" cy="86" r="58" fill={TEXT} />
      <circle cx="100" cy="86" r="58" fill="none" stroke={ACCENT} strokeWidth="5" />
      {/* eyes */}
      <ellipse cx="78" cy="78" rx="9" ry={9 * eyeOpen} fill={BG} />
      <ellipse cx="122" cy="78" rx="9" ry={9 * eyeOpen} fill={BG} />
      <circle cx="81" cy={78 - 3 * eyeOpen} r={2.6 * eyeOpen} fill={TEXT} />
      <circle cx="125" cy={78 - 3 * eyeOpen} r={2.6 * eyeOpen} fill={TEXT} />
      {/* cheeks */}
      <circle cx="66" cy="100" r="6" fill={ACCENT} opacity="0.45" />
      <circle cx="134" cy="100" r="6" fill={ACCENT} opacity="0.45" />
      {/* mouth */}
      <rect
        x={100 - mouthWidth / 2}
        y={112 - mouthHeight / 2 + 4}
        width={mouthWidth}
        height={mouthHeight}
        rx={Math.min(mouthHeight / 2, 10)}
        fill={BG}
      />
      {e > 0.45 ? <rect x="90" y={117 + mouthHeight / 2 - 6} width="20" height="5" rx="2.5" fill={ACCENT} /> : null}
    </svg>
  );
};
