import { staticFile } from "remotion";

/**
 * Resolve a media path from the spec to a URL the renderer can load.
 * URLs pass through. Anything else is relative to `assetsBase` under public/
 * (scripts/render_longform.py copies media to public/<slug>/...).
 */
export const resolveAsset = (assetsBase: string, src: string): string => {
  if (/^(https?:|data:|blob:)/i.test(src)) return src;
  const base = assetsBase ? assetsBase.replace(/^\/+|\/+$/g, "") + "/" : "";
  const rel = src.replace(/^\/+/, "");
  const full = base && rel.startsWith(base) ? rel : base + rel;
  return staticFile(full);
};
