import { z } from "zod";

/**
 * Matches the `Caption` type from @remotion/captions:
 * { text, startMs, endMs, timestampMs, confidence }
 * timestampMs/confidence are nullable in the upstream type.
 */
export const captionSchema = z.object({
  text: z.string(),
  startMs: z.number(),
  endMs: z.number(),
  timestampMs: z.number().nullable(),
  confidence: z.number().nullable(),
});

export const segmentSchema = z.object({
  /**
   * Path relative to public/ (e.g. "smoke/s1.mp4") or an http(s) URL.
   * Absolute filesystem paths are NOT supported by the browser renderer -
   * copy segment mp4s into public/ first (see SETUP-NOTES.md).
   */
  src: z.string(),
  /**
   * Filled in automatically by calculateMetadata (probed with mediabunny).
   * Do not set manually.
   */
  durationInFrames: z.number().int().positive().optional(),
});

export const sfxCueSchema = z.object({
  /** When the cue fires, in ms on the composition timeline. */
  atMs: z.number().min(0),
  /**
   * Sound name, resolved to staticFile(`sfx/${name}.wav`) - the bundled set
   * lives in public/sfx/ (whoosh, pop, tick, ding, type; see
   * skills/render-shorts/assets/sfx/README.md).
   */
  name: z.string().regex(/^[A-Za-z0-9_-]+$/, "bare sound name, no path/ext"),
  /**
   * Target peak of the cue in dBFS relative to full scale. Default: -16 dB
   * (~0.16 of full scale). Clamped to <= -6 dB in Assembly so SFX never
   * rival the voiceover. The bundled assets are normalized to -20 dBFS
   * peak; Assembly compensates automatically.
   */
  gainDb: z.number().optional(),
});

export const assemblySchema = z.object({
  segments: z.array(segmentSchema).min(1),
  voiceoverSrc: z.string(),
  musicSrc: z.string().optional(),
  captions: z.array(captionSchema),
  /** Optional one-shot sound effects (scene boundaries, number reveals). */
  sfx: z.array(sfxCueSchema).optional(),
  /** Music loudness in dBFS relative to full scale. Default: -22 dB. */
  musicVolumeDb: z.number().optional(),
  /** Draw the 900x1160 safe-area rectangle + caption zone for debugging. */
  showSafeZones: z.boolean().optional(),
});

export type AssemblyProps = z.infer<typeof assemblySchema>;
export type SegmentProps = z.infer<typeof segmentSchema>;
export type SfxCue = z.infer<typeof sfxCueSchema>;
