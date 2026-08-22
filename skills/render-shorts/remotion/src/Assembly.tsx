import {
  AbsoluteFill,
  OffthreadVideo,
  Sequence,
  Series,
  staticFile,
  useVideoConfig,
} from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import { Audio } from "@remotion/media";
import { Captions } from "./Captions";
import { SafeZones } from "./SafeZones";
import { getMediaDurationInSeconds } from "./get-duration";
import { resolveSrc } from "./resolve-src";
import type { AssemblyProps } from "./schema";

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

/** Constant music bed level ("ducking" v1). -22 dBFS ~= gain 0.079. */
const DEFAULT_MUSIC_VOLUME_DB = -22;

/**
 * SFX levels. `gainDb` on a cue is the TARGET PEAK in dBFS relative to full
 * scale in the mix. The bundled sfx wavs are peak-normalized to -20 dBFS
 * (skills/render-shorts/assets/sfx/README.md), so the played volume compensates by
 * (gainDb - SFX_ASSET_PEAK_DB). Default target: -16 dBFS (~0.16 of full
 * scale); ceiling: -6 dBFS so a cue never rivals VO prominence.
 */
const DEFAULT_SFX_GAIN_DB = -16;
const MAX_SFX_GAIN_DB = -6;
const SFX_ASSET_PEAK_DB = -20;
/** Window a one-shot SFX <Audio> stays mounted (covers all bundled wavs). */
const SFX_WINDOW_SECONDS = 2;

const dbToGain = (db: number): number => 10 ** (db / 20);

/**
 * Probes every segment with mediabunny, assigns per-segment
 * durationInFrames, and sets the total composition duration to their sum.
 * The voiceover may be slightly shorter than the video - the total always
 * follows the video segments.
 */
export const calculateAssemblyMetadata: CalculateMetadataFunction<
  AssemblyProps
> = async ({ props }) => {
  const durations = await Promise.all(
    props.segments.map((segment) =>
      getMediaDurationInSeconds(resolveSrc(segment.src)),
    ),
  );

  const segments = props.segments.map((segment, i) => ({
    ...segment,
    durationInFrames: Math.max(1, Math.round(durations[i] * FPS)),
  }));

  const totalDurationInFrames = segments.reduce(
    (sum, segment) => sum + segment.durationInFrames,
    0,
  );

  return {
    durationInFrames: totalDurationInFrames,
    props: {
      ...props,
      segments,
    },
  };
};

export const Assembly: React.FC<AssemblyProps> = ({
  segments,
  voiceoverSrc,
  musicSrc,
  captions,
  sfx,
  musicVolumeDb,
  showSafeZones,
}) => {
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      {/* Scene segments, back to back. */}
      <Series>
        {segments.map((segment, i) => (
          <Series.Sequence
            key={`${segment.src}-${i}`}
            // Filled in by calculateAssemblyMetadata; the fallback only
            // matters if the component is mounted without it.
            durationInFrames={segment.durationInFrames ?? 4 * fps}
            premountFor={4 * fps}
          >
            <OffthreadVideo
              src={resolveSrc(segment.src)}
              pauseWhenBuffering
              // Scene mp4s are visual-only; the voiceover carries the audio.
              muted
              style={{ width: "100%", height: "100%", objectFit: "cover" }}
            />
          </Series.Sequence>
        ))}
      </Series>

      {/* Voiceover at full volume, from frame 0. */}
      <Audio src={resolveSrc(voiceoverSrc)} />

      {/* Optional music bed at a constant low volume; loops if shorter
          than the video and is cut off at the end of the composition. */}
      {musicSrc ? (
        <Audio
          src={resolveSrc(musicSrc)}
          loop
          // Constant "ducking" level for v1 (the eslint rule wants a callback).
          volume={() => dbToGain(musicVolumeDb ?? DEFAULT_MUSIC_VOLUME_DB)}
        />
      ) : null}

      {/* One-shot sound effects (scene boundaries, number reveals). Each
          cue mounts a short <Audio> at its timestamp; the wav ends on its
          own well inside the window. gainDb = target peak in dBFS
          (default -16, clamped at -6 so SFX never rival the voiceover);
          the played volume compensates for the -20 dBFS asset peak. */}
      {(sfx ?? []).map((cue, i) => {
        const from = Math.round((cue.atMs / 1000) * fps);
        const targetPeakDb = Math.min(
          cue.gainDb ?? DEFAULT_SFX_GAIN_DB,
          MAX_SFX_GAIN_DB,
        );
        const volumeDb = targetPeakDb - SFX_ASSET_PEAK_DB;
        return (
          <Sequence
            key={`sfx-${cue.name}-${cue.atMs}-${i}`}
            from={from}
            durationInFrames={SFX_WINDOW_SECONDS * fps}
          >
            <Audio
              src={staticFile(`sfx/${cue.name}.wav`)}
              volume={() => dbToGain(volumeDb)}
            />
          </Sequence>
        );
      })}

      {/* Word-timed TikTok-style captions inside the safe area. */}
      <Captions captions={captions} />

      {showSafeZones ? <SafeZones /> : null}
    </AbsoluteFill>
  );
};
