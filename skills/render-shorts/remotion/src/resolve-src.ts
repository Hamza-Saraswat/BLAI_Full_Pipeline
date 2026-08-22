import { staticFile } from "remotion";

/**
 * Resolves a media source given in input props to a URL usable by
 * <OffthreadVideo> / <Audio> and by mediabunny during calculateMetadata.
 *
 * - "http://", "https://", "data:", "blob:" URLs are passed through.
 * - Anything else is treated as a path RELATIVE TO public/ and resolved
 *   via staticFile() (e.g. "smoke/s1.mp4").
 * - Absolute filesystem paths ("/Users/...") are rejected with a clear
 *   error: the render happens inside headless Chrome which cannot read
 *   arbitrary local paths. The pipeline must copy files into public/.
 */
export const resolveSrc = (src: string): string => {
  if (
    src.startsWith("http://") ||
    src.startsWith("https://") ||
    src.startsWith("data:") ||
    src.startsWith("blob:")
  ) {
    return src;
  }
  if (src.startsWith("/")) {
    throw new Error(
      `Assembly: "${src}" looks like an absolute filesystem path. ` +
        `Copy the file into skills/render-shorts/remotion/public/ and pass a path relative to public/ ` +
        `(e.g. "segments/scene1.mp4"). See SETUP-NOTES.md.`,
    );
  }
  return staticFile(src);
};
