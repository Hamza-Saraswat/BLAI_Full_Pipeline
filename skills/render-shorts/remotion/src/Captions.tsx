import { useMemo } from "react";
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { createTikTokStyleCaptions } from "@remotion/captions";
import type { Caption, TikTokPage } from "@remotion/captions";

/** How often caption pages switch. Higher = more words per page. */
const SWITCH_CAPTIONS_EVERY_MS = 1000;

/**
 * Caption pre-roll: a page becomes VISIBLE this many ms before its first
 * word's audio starts (captions leading audio by 100-300ms boosts early
 * retention). Only the page's display start is shifted (clamped at 0);
 * its own end time is untouched, so pages get slightly longer, never
 * shorter. Word highlighting still tracks the real audio times.
 */
const CAPTION_PRE_ROLL_MS = 150;

/** Currently-spoken token highlight (accent). */
const HIGHLIGHT_COLOR = "#FFB347";

/**
 * Safe-area geometry on the 1080x1920 canvas.
 *
 * Captions live ENTIRELY inside the pipeline's caption band (y 1260..1470),
 * which scene content is forbidden to enter (safe_zone_check.py --scene).
 * Horizontal: the right 120px (x >= 960) is the like/comment rail, so the
 * box is x 90..955 (width 865; 5px buffer because the 10px text stroke
 * bleeds past glyph edges -- a real linter catch at width=900 on a long
 * caption line). Bottom-anchored at y=1430: a single 72px line occupies
 * ~1347..1430; two lines start at ~1264 -- still inside the band, and 40px
 * clear of the bottom-UI overlay at 1470.
 */
export const CAPTION_BOX = {
  left: 90,
  width: 865,
  bottomAnchorY: 1430,
} as const;

const containerStyle: React.CSSProperties = {
  position: "absolute",
  left: CAPTION_BOX.left,
  width: CAPTION_BOX.width,
  bottom: 1920 - CAPTION_BOX.bottomAnchorY, // 540px up from the bottom edge
  textAlign: "center",
  fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif",
  fontSize: 72,
  fontWeight: 800,
  lineHeight: 1.15,
  color: "white",
  // Tokens carry their own leading spaces; preserve them but allow wrapping.
  whiteSpace: "pre-wrap",
  // Outline: stroke painted UNDER the fill (paint-order is supported by
  // the Chrome Headless Shell that Remotion 4.0.48x renders with).
  WebkitTextStroke: "10px black",
  paintOrder: "stroke fill",
  textShadow: "0 6px 28px rgba(0, 0, 0, 0.7)",
};

const CaptionPage: React.FC<{
  readonly page: TikTokPage;
  /** Composition time (ms) at which this page's <Sequence> starts. With
   *  pre-roll this is EARLIER than page.startMs, so the absolute clock must
   *  be derived from it - not from page.startMs - to keep the word
   *  highlight locked to the real audio times. */
  readonly sequenceStartMs: number;
}> = ({ page, sequenceStartMs }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Local frame -> absolute time on the composition timeline.
  const currentTimeMs = (frame / fps) * 1000;
  const absoluteTimeMs = sequenceStartMs + currentTimeMs;

  return (
    <AbsoluteFill>
      <div style={containerStyle}>
        {page.tokens.map((token) => {
          const isActive =
            token.fromMs <= absoluteTimeMs && token.toMs > absoluteTimeMs;

          return (
            <span
              key={token.fromMs}
              style={{ color: isActive ? HIGHLIGHT_COLOR : "white" }}
            >
              {token.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

export const Captions: React.FC<{ readonly captions: Caption[] }> = ({
  captions,
}) => {
  const { fps } = useVideoConfig();

  const { pages } = useMemo(() => {
    return createTikTokStyleCaptions({
      captions,
      combineTokensWithinMilliseconds: SWITCH_CAPTIONS_EVERY_MS,
    });
  }, [captions]);

  return (
    <AbsoluteFill>
      {pages.map((page, index) => {
        const nextPage = pages[index + 1] ?? null;
        // Pre-roll: the page appears CAPTION_PRE_ROLL_MS before its first
        // word's audio start (clamped at 0). End times are NOT shifted:
        // the page's own span still runs from the ORIGINAL startMs, and the
        // next-page clamp uses the next page's (shifted) display start, so
        // pages only ever get longer, never shorter, and never overlap.
        const displayStartMs = Math.max(0, page.startMs - CAPTION_PRE_ROLL_MS);
        const nextDisplayStartMs = nextPage
          ? Math.max(0, nextPage.startMs - CAPTION_PRE_ROLL_MS)
          : Infinity;
        const startFrame = Math.round((displayStartMs / 1000) * fps);
        // Show the page for at least the switch interval, but never cut off
        // a page whose tokens span longer, and never overlap the next page.
        const pageSpanMs = Math.max(SWITCH_CAPTIONS_EVERY_MS, page.durationMs);
        const endFrame = Math.round(
          Math.min(
            (nextDisplayStartMs / 1000) * fps,
            ((page.startMs + pageSpanMs) / 1000) * fps,
          ),
        );
        const durationInFrames = endFrame - startFrame;

        if (durationInFrames <= 0) {
          return null;
        }

        return (
          <Sequence
            key={index}
            from={startFrame}
            durationInFrames={durationInFrames}
            premountFor={fps}
          >
            <CaptionPage page={page} sequenceStartMs={displayStartMs} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
