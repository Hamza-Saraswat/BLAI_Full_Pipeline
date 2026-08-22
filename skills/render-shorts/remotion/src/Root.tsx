import { Composition } from "remotion";
import {
  Assembly,
  calculateAssemblyMetadata,
  FPS,
  HEIGHT,
  WIDTH,
} from "./Assembly";
import { assemblySchema } from "./schema";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Assembly"
        component={Assembly}
        // Placeholder - overridden by calculateMetadata (sum of segments).
        durationInFrames={10 * FPS}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
        schema={assemblySchema}
        calculateMetadata={calculateAssemblyMetadata}
        defaultProps={{
          // Studio defaults point at the bundled smoke fixture (public/smoke/).
          segments: [{ src: "smoke/s1.mp4" }, { src: "smoke/s2.mp4" }],
          voiceoverSrc: "smoke/vo.wav",
          captions: [
            {
              text: "This",
              startMs: 70,
              endMs: 370,
              timestampMs: 160,
              confidence: 1,
            },
            {
              text: " is",
              startMs: 370,
              endMs: 610,
              timestampMs: 320,
              confidence: 1,
            },
            {
              text: " the",
              startMs: 610,
              endMs: 820,
              timestampMs: 480,
              confidence: 1,
            },
          ],
          musicVolumeDb: -22,
          showSafeZones: false,
        }}
      />
    </>
  );
};
