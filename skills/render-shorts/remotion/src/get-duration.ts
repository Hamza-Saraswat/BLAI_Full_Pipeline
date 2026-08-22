import { ALL_FORMATS, Input, UrlSource } from "mediabunny";

/**
 * Probes the duration of a media file (in seconds) using mediabunny.
 *
 * Note: the older @remotion/media-parser `parseMedia({fields:
 * {slowDurationInSeconds}})` API has been superseded by mediabunny
 * (`Input.computeDuration()`), which is what the official Remotion
 * skill recommends as of 4.0.48x.
 *
 * Runs in the browser context (Remotion Studio and the headless renderer),
 * so sources must be URLs - use resolveSrc() to turn public/-relative
 * paths into served URLs.
 */
export const getMediaDurationInSeconds = async (
  url: string,
): Promise<number> => {
  const input = new Input({
    formats: ALL_FORMATS,
    source: new UrlSource(url, {
      getRetryDelay: () => null,
    }),
  });

  return input.computeDuration();
};
