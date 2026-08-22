// Brand and canvas constants for the BLAI long-form renderer.
// Colors come from brand-vault (thumbnails.md, identity.md); the canvas and
// safe area from shared/platform-specs.md (long-form row).

export const WIDTH = 1920;
export const HEIGHT = 1080;
export const FPS = 30;

export const THUMB_WIDTH = 1280;
export const THUMB_HEIGHT = 720;

export const BG = "#0B1020";
export const TEXT = "#F5F0E8";
export const ACCENT = "#FFB347";
export const OK = "#7BD88F";
export const ERR = "#FF6B6B";
// Derived tones (flat, no gradients).
export const CARD = "#141B33";
export const CARD_BORDER = "rgba(245, 240, 232, 0.12)";
export const MUTED = "rgba(245, 240, 232, 0.62)";
export const DIM = "rgba(245, 240, 232, 0.35)";
export const OVERLAY = "rgba(11, 16, 32, 0.55)";

export const FONT_FALLBACK = "'Helvetica Neue', Helvetica, Arial, sans-serif";
export const MONO_FONT = "'JetBrains Mono', 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace";

// 5 % margins: lower thirds and captions stay inside 1728 x 972 centered.
export const SAFE_MARGIN = 0.05;
export const SAFE = {
  left: Math.round(WIDTH * SAFE_MARGIN),
  top: Math.round(HEIGHT * SAFE_MARGIN),
  right: Math.round(WIDTH * (1 - SAFE_MARGIN)),
  bottom: Math.round(HEIGHT * (1 - SAFE_MARGIN)),
  width: Math.round(WIDTH * (1 - 2 * SAFE_MARGIN)),
  height: Math.round(HEIGHT * (1 - 2 * SAFE_MARGIN)),
} as const;

// On-screen text: at most 8 words visible at once, never below 44 px at 1080p.
export const MAX_WORDS_VISIBLE = 8;
export const MIN_TEXT_PX = 44;
export const CAPTION_PX = 46;
export const LOWER_THIRD_PX = 52;
export const CAPTION_BAND_PX = 110;

export const TYPING_CHARS_PER_SECOND = 18;
export const END_CARD_SECONDS = 8;
export const WORDMARK = "BUILD LOCAL AI";
export const CHANNEL_HANDLE = "@BuildLocalAI";
