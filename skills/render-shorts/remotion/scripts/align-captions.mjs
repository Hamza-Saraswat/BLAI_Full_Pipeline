#!/usr/bin/env node
/**
 * align-captions.mjs <vo.wav> <storyboard.json> <captions-out.json>
 *
 * Deterministic caption + scene-timing generation for the BLAI pipeline:
 *   1. resample vo.wav -> 16kHz mono 16-bit wav (whisper.cpp requirement)
 *   2. ensure whisper.cpp + base.en model are installed (idempotent)
 *   3. transcribe with token-level timestamps -> @remotion/captions Caption[]
 *   4. write captions.json
 *   5. compute per-scene timings from the storyboard's narration word counts
 *      (drift-tolerant proportional mapping) -> timing.json (same dir)
 *
 * Run from skills/render-shorts/remotion/ (where @remotion/install-whisper-cpp is a dep):
 *   node scripts/align-captions.mjs ../../out/<slug>/vo.wav \
 *     ../../out/<slug>/storyboard.json ../../out/<slug>/captions.json
 */
import {execFileSync} from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {
  downloadWhisperModel,
  installWhisperCpp,
  toCaptions,
  transcribe,
} from '@remotion/install-whisper-cpp';

const WHISPER_VERSION = '1.7.4';
const WHISPER_MODEL = 'base.en';
const LAST_SCENE_EXTRA_S = 1.0; // loop-friendly hold on the final scene

const here = path.dirname(fileURLToPath(import.meta.url));
const whisperDir = path.join(here, '..', 'whisper.cpp');

const [voPath, storyboardPath, captionsOut, narrationNormPath] = process.argv.slice(2);
if (!voPath || !storyboardPath || !captionsOut) {
  console.error(
    'usage: node align-captions.mjs <vo.wav> <storyboard.json> <captions-out.json> [narration.norm.json]',
  );
  process.exit(2);
}

const storyboard = JSON.parse(fs.readFileSync(storyboardPath, 'utf8'));

// Optional: the normalized narration the TTS engine was actually given
// ("twenty seven billion", not "27B"). Whisper hears the spoken form, so both
// the drift check and the scene slicing must measure against it. Absent =>
// legacy behaviour, measuring against the raw storyboard text.
let norm = null;
if (narrationNormPath && fs.existsSync(narrationNormPath)) {
  try {
    const parsed = JSON.parse(fs.readFileSync(narrationNormPath, 'utf8'));
    if (parsed?.full && parsed.scenes?.length === storyboard.scenes.length) norm = parsed;
    else console.warn('normalized narration ignored: scene count mismatch');
  } catch {
    console.warn('normalized narration unreadable -- falling back to storyboard text');
  }
}

// 1. resample to what whisper.cpp expects
const tmp16k = path.join(os.tmpdir(), `blai-vo-16k-${Date.now()}.wav`);
execFileSync('ffmpeg', [
  '-hide_banner', '-loglevel', 'error', '-y',
  '-i', voPath, '-ar', '16000', '-ac', '1', '-c:a', 'pcm_s16le', tmp16k,
]);

// 2. idempotent install (no-ops when already present)
await installWhisperCpp({to: whisperDir, version: WHISPER_VERSION});
await downloadWhisperModel({model: WHISPER_MODEL, folder: whisperDir});

// 3. transcribe with word-level timestamps
const whisperCppOutput = await transcribe({
  inputPath: tmp16k,
  whisperPath: whisperDir,
  whisperCppVersion: WHISPER_VERSION,
  model: WHISPER_MODEL,
  tokenLevelTimestamps: true,
  splitOnWord: true,
});
fs.rmSync(tmp16k, {force: true});

const {captions} = toCaptions({whisperCppOutput});
const words = captions.filter((c) => c.text.trim().length > 0);
if (words.length === 0) {
  console.error('alignment produced zero words -- check the audio');
  process.exit(1);
}
fs.mkdirSync(path.dirname(captionsOut), {recursive: true});
fs.writeFileSync(captionsOut, JSON.stringify(words, null, 2));

// 4. sanity: word-count drift vs the known script
const countWords = (s) => (s.match(/[\w']+/g) ?? []).length;
const scriptWords = countWords(norm ? norm.full : storyboard.narration_full);
const drift = Math.abs(words.length - scriptWords) / scriptWords;

// 5. proportional scene boundaries (tolerates transcription drift)
const sceneWordCounts = norm
  ? norm.scenes.map((s) => countWords(s.text))
  : storyboard.scenes.map((s) => countWords(s.narration));
const totalSceneWords = sceneWordCounts.reduce((a, b) => a + b, 0);
// Scenes must tile the VO timeline CONTIGUOUSLY: at assembly the voiceover
// plays straight through while segments play back-to-back, so any per-scene
// padding accumulates as visual/audio drift. Rule: scene i runs from its
// narration start to scene i+1's narration start (natural speech gaps are
// absorbed by the earlier scene); scene 1 starts at 0 to absorb the lead-in;
// only the final scene gets a +1.0s loop-friendly hold past its last word.
let cum = 0;
let prevIdx = 0;
const sliceBounds = storyboard.scenes.map((_, i) => {
  cum += sceneWordCounts[i];
  const endIdx =
    i === storyboard.scenes.length - 1
      ? words.length
      : Math.max(prevIdx + 1, Math.round((words.length * cum) / totalSceneWords));
  const b = {startIdx: prevIdx, endIdx};
  prevIdx = endIdx;
  return b;
});
const timing = storyboard.scenes.map((scene, i) => {
  const {startIdx, endIdx} = sliceBounds[i];
  const slice = words.slice(startIdx, endIdx);
  const isLast = i === storyboard.scenes.length - 1;
  const videoStartMs = i === 0 ? 0 : words[startIdx].startMs;
  const videoEndMs = isLast
    ? slice[slice.length - 1].endMs + LAST_SCENE_EXTRA_S * 1000
    : words[endIdx].startMs; // next scene's first word
  return {
    scene_id: scene.id,
    start_ms: videoStartMs,
    end_ms: videoEndMs,
    duration_s: Math.round(((videoEndMs - videoStartMs) / 1000) * 100) / 100,
    words: slice.length,
  };
});

const timingOut = path.join(path.dirname(captionsOut), 'timing.json');
fs.writeFileSync(timingOut, JSON.stringify(timing, null, 2));

const report = {
  captions: captionsOut,
  timing: timingOut,
  aligned_words: words.length,
  script_words: scriptWords,
  drift_pct: Math.round(drift * 1000) / 10,
  vo_span_ms: words[words.length - 1].endMs - words[0].startMs,
  scenes: timing,
};
console.log(JSON.stringify(report, null, 2));
if (drift > 0.1) {
  console.error(
    `WARN: word-count drift ${(drift * 100).toFixed(1)}% > 10% -- review captions vs script`,
  );
  process.exit(3);
}
