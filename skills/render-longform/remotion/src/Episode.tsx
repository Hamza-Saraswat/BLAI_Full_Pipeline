// The Episode composition: scenes laid out back to back from the layout that
// calculateMetadata computes (src/timing.mjs), the narration audio from frame 0.
import React from "react";
import type { CalculateMetadataFunction } from "remotion";
import { AbsoluteFill, Audio, Sequence } from "remotion";
import { getAudioDurationInSeconds, getVideoMetadata } from "@remotion/media-utils";
import { resolveAsset } from "./assets";
import { BG, ERR, FPS, MUTED, SAFE } from "./constants";
import { getString } from "./data";
import { ensureFont, FONT_FAMILY } from "./fonts";
import { SafeAreaOverlay } from "./SceneFrame";
import { SCENES } from "./scenes";
import { computeLayout, wordsInScene } from "./timing.mjs";
import type { BrollMeta, EpisodeProps, Layout, SceneProps } from "./types";

export const calculateEpisodeMetadata: CalculateMetadataFunction<EpisodeProps> = async ({ props }) => {
  let audioDurationS: number | null = null;
  if (props.audioSrc) {
    try {
      audioDurationS = await getAudioDurationInSeconds(resolveAsset(props.assetsBase, props.audioSrc));
    } catch (err) {
      console.warn(`narration audio could not be probed (${props.audioSrc}); scenes keep their spec timing`, err);
    }
  }
  const layout = computeLayout({ spec: props.spec, captions: props.captions, fps: FPS, audioDurationS }) as Layout;

  const broll: Record<string, BrollMeta> = {};
  for (const scene of props.spec.scenes) {
    if (scene.type !== "b-roll") continue;
    const src = getString(scene.data, "src", "");
    if (!src) {
      broll[scene.id] = { missing: true, durationS: null, src: null };
      continue;
    }
    try {
      const meta = await getVideoMetadata(resolveAsset(props.assetsBase, src));
      broll[scene.id] = { missing: false, durationS: meta.durationInSeconds, src };
    } catch {
      console.warn(`b-roll clip missing for ${scene.id}: ${src}; rendering a placeholder card`);
      broll[scene.id] = { missing: true, durationS: null, src };
    }
  }

  return {
    durationInFrames: Math.max(1, layout.totalFrames),
    props: { ...props, layout, broll },
  };
};

const UnknownScene: React.FC<SceneProps> = ({ scene }) => (
  <AbsoluteFill style={{ backgroundColor: BG, alignItems: "center", justifyContent: "center", color: ERR, fontSize: 48, fontWeight: 800 }}>
    unknown scene type: {scene.type}
    <div style={{ color: MUTED, fontSize: 32, marginTop: 20 }}>{scene.id}</div>
  </AbsoluteFill>
);

export const Episode: React.FC<EpisodeProps> = (props) => {
  ensureFont();
  const layout: Layout = React.useMemo(
    () => props.layout ?? (computeLayout({ spec: props.spec, captions: props.captions, fps: FPS, audioDurationS: null }) as Layout),
    [props.layout, props.spec, props.captions],
  );
  return (
    <AbsoluteFill style={{ backgroundColor: BG, fontFamily: FONT_FAMILY }}>
      {layout.scenes.map((ls) => {
        const scene = props.spec.scenes[ls.index];
        if (!scene) return null;
        const Component = SCENES[scene.type] ?? UnknownScene;
        const sceneWords = wordsInScene(props.captions, ls);
        return (
          <Sequence key={ls.id} from={ls.from} durationInFrames={ls.durationInFrames} premountFor={FPS} name={`${ls.id} ${ls.type}`}>
            <Component
              spec={props.spec}
              scene={scene}
              layout={ls}
              sceneWords={sceneWords}
              captures={props.captures ?? {}}
              assetsBase={props.assetsBase}
              audioSrc={props.audioSrc}
              broll={props.broll}
            />
          </Sequence>
        );
      })}
      {props.audioSrc ? <Audio src={resolveAsset(props.assetsBase, props.audioSrc)} /> : null}
      {props.showSafeArea ? <SafeAreaOverlay /> : null}
      {props.showSafeArea ? (
        <div style={{ position: "absolute", left: SAFE.left, top: SAFE.top - 40, color: MUTED, fontSize: 24, fontWeight: 700 }}>
          SAFE AREA 1728 x 972
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
