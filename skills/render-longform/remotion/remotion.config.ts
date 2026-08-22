// Remotion CLI configuration for the BLAI long-form renderer.
// These settings apply to `npx remotion render` and `npx remotion still`.
// Output contract (shared/platform-specs.md, long-form row): 1920x1080, 30 fps,
// H.264, yuv420p, bt709. Loudness is handled by scripts/render_longform.py.
import os from "node:os";
import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
Config.setCodec("h264");
Config.setPixelFormat("yuv420p");
// Without this Remotion emits full-range yuvj420p / bt601, which fails the lint.
Config.setColorSpace("bt709");
// Half the cores, capped at 8: every render worker decodes the narration
// audio for the mascot envelope, so more workers mostly cost memory.
Config.setConcurrency(Math.min(8, Math.max(1, Math.floor(os.cpus().length / 2))));
