import React from "react";
import { Composition } from "remotion";
import { FPS, HEIGHT, THUMB_HEIGHT, THUMB_WIDTH, WIDTH } from "./constants";
import { DEFAULT_EPISODE_PROPS, DEFAULT_THUMBNAIL_PROPS } from "./defaults";
import { calculateEpisodeMetadata, Episode } from "./Episode";
import { Thumbnail } from "./Thumbnail";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Episode"
        component={Episode}
        // Placeholder; calculateEpisodeMetadata sets the real duration from the scene layout.
        durationInFrames={30 * FPS}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
        defaultProps={DEFAULT_EPISODE_PROPS}
        calculateMetadata={calculateEpisodeMetadata}
      />
      <Composition
        id="Thumbnail"
        component={Thumbnail}
        durationInFrames={1}
        fps={FPS}
        width={THUMB_WIDTH}
        height={THUMB_HEIGHT}
        defaultProps={DEFAULT_THUMBNAIL_PROPS}
      />
    </>
  );
};
