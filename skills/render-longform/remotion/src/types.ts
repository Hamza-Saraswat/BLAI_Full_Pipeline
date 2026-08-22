// Props and spec types. The spec mirrors shared/schemas/longform-spec.schema.json.

export type SceneType =
  | "title-card"
  | "chapter-card"
  | "kinetic-text"
  | "code-typing"
  | "terminal-replay"
  | "diagram"
  | "comparison-table"
  | "chart"
  | "stat-callout"
  | "quote"
  | "mascot-talk"
  | "b-roll"
  | "end-card";

export type SceneData = Record<string, unknown>;

export type SyncPoint = { phrase: string; event: string };

export type SpecScene = {
  id: string;
  type: SceneType;
  narration: string;
  est_duration_s: number;
  visual_intent: string;
  on_screen_text?: string[];
  data?: SceneData;
  capture_ref?: string;
  sync_points?: SyncPoint[];
  mood?: string;
};

export type SpecChapter = { label: string; starts_at_scene: string };

export type ThumbnailConcept = { words: string; focus: string };

export type Spec = {
  slug: string;
  title: string;
  target_duration_s: number;
  series?: string;
  chapters: SpecChapter[];
  scenes: SpecScene[];
  thumbnail_concepts: ThumbnailConcept[];
  music_mood?: string;
};

/** One word of the narration with absolute times in seconds. */
export type CaptionWord = { word: string; start: number; end: number };

/** One captured command from skills/dgx-capture (capture.json + <id>.cast). */
export type Capture = {
  command?: string;
  cast?: string;
  stdout?: string;
  metrics?: Record<string, number | string | null>;
  exit?: number;
  duration_s?: number;
};

export type ResolvedSyncPoint = { event: string; phrase: string; atS: number | null };

export type LayoutScene = {
  id: string;
  type: string;
  index: number;
  from: number;
  durationInFrames: number;
  startS: number;
  endS: number;
  estDurationS: number;
  matched: boolean;
  wordStart: number | null;
  wordEnd: number | null;
  chapter: { number: number; label: string } | null;
  syncPoints: ResolvedSyncPoint[];
};

export type LayoutChapter = { number: number; label: string; sceneId: string; startS: number };

export type Layout = {
  fps: number;
  hasCaptions: boolean;
  audioDurationS: number | null;
  totalFrames: number;
  totalS: number;
  scenes: LayoutScene[];
  chapters: LayoutChapter[];
};

export type BrollMeta = { missing: boolean; durationS: number | null; src: string | null };

export type EpisodeProps = {
  spec: Spec;
  captions: CaptionWord[];
  audioSrc: string | null;
  captures: Record<string, Capture>;
  /** Folder under public/ that holds this episode's media, for example "<slug>/". */
  assetsBase: string;
  /** Filled in by calculateMetadata. */
  layout?: Layout;
  /** Filled in by calculateMetadata. */
  broll?: Record<string, BrollMeta>;
  /** Draw the 5 % safe-area rectangle for debugging. */
  showSafeArea?: boolean;
};

export type SceneProps = {
  spec: Spec;
  scene: SpecScene;
  layout: LayoutScene;
  /** Caption words spoken during this scene, absolute times. */
  sceneWords: CaptionWord[];
  captures: Record<string, Capture>;
  assetsBase: string;
  audioSrc: string | null;
  broll?: Record<string, BrollMeta>;
};

export type ThumbnailProps = {
  concept: ThumbnailConcept;
  title: string;
  variant: number;
  series?: string;
};
