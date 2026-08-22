#!/usr/bin/env node
// Print the scene layout for an Episode props file as JSON.
// Usage: node scripts/layout.mjs props.json [--audio-duration S] [--fps 30]
// Used by scripts/render_longform.py to write chapters.json and render.json
// with the same timings the composition renders (src/timing.mjs).
import { readFileSync } from "node:fs";
import { computeLayout } from "../src/timing.mjs";

const args = process.argv.slice(2);
if (args.length === 0 || args.includes("--help")) {
  console.log("usage: node scripts/layout.mjs props.json [--audio-duration S] [--fps 30]");
  process.exit(args.length === 0 ? 1 : 0);
}
const file = args[0];
const opt = (name, fallback) => {
  const i = args.indexOf(name);
  return i >= 0 && args[i + 1] !== undefined ? args[i + 1] : fallback;
};
const props = JSON.parse(readFileSync(file, "utf8"));
const fps = Number(opt("--fps", 30));
const audio = opt("--audio-duration", null);
const layout = computeLayout({
  spec: props.spec,
  captions: props.captions || [],
  fps,
  audioDurationS: audio === null ? null : Number(audio),
});
process.stdout.write(JSON.stringify(layout, null, 2) + "\n");
