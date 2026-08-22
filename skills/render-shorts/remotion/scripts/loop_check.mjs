#!/usr/bin/env node
/**
 * loop_check.mjs <video.mp4> [--threshold 0.5]
 *
 * Loop-frame ("visual rhyme") check: extracts the first and last frames of
 * the video with ffmpeg, scores them with ffmpeg's SSIM filter, and prints
 * JSON {similar, ssim, threshold, video} to stdout.
 *
 * The threshold is deliberately loose (default 0.5): the loop rule wants the
 * first and last frames to RHYME (same family of composition/palette), not
 * be identical.
 *
 * Exit 0 = similar (ssim >= threshold), exit 1 = not similar, exit 2 = error.
 */
import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const args = process.argv.slice(2);
const positional = args.filter((a) => !a.startsWith("--"));
const video = positional[0];
const thresholdArg = args.indexOf("--threshold");
const threshold =
  thresholdArg !== -1 ? Number(args[thresholdArg + 1]) : 0.5;

if (!video || Number.isNaN(threshold)) {
  console.error("usage: node scripts/loop_check.mjs <video.mp4> [--threshold 0.5]");
  process.exit(2);
}
if (!existsSync(video)) {
  console.error(`loop_check: file not found: ${video}`);
  process.exit(2);
}

const run = (cmd, cmdArgs) =>
  execFileSync(cmd, cmdArgs, { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] });

const workDir = mkdtempSync(join(tmpdir(), "loop-check-"));
const firstPng = join(workDir, "first.png");
const lastPng = join(workDir, "last.png");

try {
  // First frame.
  run("ffmpeg", ["-y", "-hide_banner", "-loglevel", "error",
    "-i", video, "-frames:v", "1", firstPng]);

  // Last frame: decode the final ~0.5s and let -update overwrite the still
  // with every decoded frame - the survivor is the last frame.
  run("ffmpeg", ["-y", "-hide_banner", "-loglevel", "error",
    "-sseof", "-0.5", "-i", video, "-update", "1", lastPng]);

  // SSIM between the two stills (scale the last onto the first's geometry
  // defensively; they should already match). stats_file=- puts the
  // per-frame line (n:1 ... All:0.87) on stdout, which execFileSync returns.
  const ssimOut = run("ffmpeg", ["-hide_banner", "-loglevel", "error",
    "-i", firstPng, "-i", lastPng,
    "-filter_complex", "[1][0]scale2ref[b][a];[a][b]ssim=stats_file=-",
    "-f", "null", "-"]);
  const match = ssimOut.match(/All:\s*([0-9.]+)/);
  if (!match) {
    console.error("loop_check: could not parse SSIM output:\n" + ssimOut);
    process.exit(2);
  }
  const ssim = Number(match[1]);
  const similar = ssim >= threshold;
  console.log(JSON.stringify({ similar, ssim, threshold, video }));
  process.exit(similar ? 0 : 1);
} catch (err) {
  console.error("loop_check: " + (err.stderr ?? err.message ?? err));
  process.exit(2);
} finally {
  rmSync(workDir, { recursive: true, force: true });
}
