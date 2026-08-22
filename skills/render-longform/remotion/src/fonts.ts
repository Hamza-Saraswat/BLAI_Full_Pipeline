// Inter via @remotion/google-fonts, with the CSS fallback stack always attached.
// Set REMOTION_OFFLINE_FONTS=1 in the environment to skip the network fetch
// (the render then uses Helvetica Neue / Arial). The variable is read lazily
// because Remotion fills process.env in the browser after the bundle loads.
import { loadFont } from "@remotion/google-fonts/Inter";
import { FONT_FALLBACK } from "./constants";

declare const process: { env: Record<string, string | undefined> } | undefined;

export const FONT_FAMILY = `Inter, ${FONT_FALLBACK}`;

let requested = false;

/** Request Inter once; safe to call from any component render. */
export const ensureFont = (): void => {
  if (requested) return;
  requested = true;
  let offline = false;
  try {
    offline = typeof process !== "undefined" && process.env.REMOTION_OFFLINE_FONTS === "1";
  } catch {
    offline = false;
  }
  if (offline) return;
  try {
    loadFont("normal", { weights: ["400", "600", "700", "800"], subsets: ["latin"] });
  } catch (err) {
    console.warn("Inter could not be loaded; rendering with the fallback font stack", err);
  }
};
