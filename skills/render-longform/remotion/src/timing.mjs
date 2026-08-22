// Scene timing for the BLAI long-form composition.
//
// Plain JavaScript on purpose: the Remotion bundle imports it (src/Episode.tsx)
// and so does scripts/layout.mjs, which scripts/render_longform.py calls from
// Node to write chapters.json and the per-scene timings in render.json.
// One implementation, two callers; keep it dependency free.
//
// Rules (see rules/spec-to-composition.md):
// 1. Without captions every scene lasts est_duration_s.
// 2. With captions a scene starts where its first narration words are spoken
//    (fuzzy match on the first 3, 2 or 1 words, lowercase, punctuation
//    stripped, searched forward from the previous scene's last word).
// 3. Scenes are contiguous: a scene ends where the next one starts. Scenes
//    that did not match share the gap to the next match in proportion to
//    their est_duration_s.
// 4. The last scene covers the end of the narration audio plus a short tail.
// 5. The end card lasts at least END_CARD_SECONDS.

export const END_CARD_SECONDS = 8;
export const TAIL_SECONDS = 0.75;
export const MIN_SCENE_SECONDS = 1;

/** @param {unknown} w */
export const normalizeWord = (w) =>
  String(w == null ? "" : w)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "");

/** @param {unknown} text */
export const tokenize = (text) =>
  String(text == null ? "" : text)
    .split(/\s+/)
    .map(normalizeWord)
    .filter((t) => t.length > 0);

/** @param {string} a @param {string} b */
const wordsMatch = (a, b) => {
  if (a === b) return true;
  if (a.length >= 4 && b.length >= 4) return a.startsWith(b) || b.startsWith(a);
  return false;
};

/**
 * First index >= cursor (and <= limit when given) where `seq` occurs in `norm`.
 * @param {string[]} norm @param {string[]} seq @param {number} cursor @param {number} [limit]
 */
export const findSequence = (norm, seq, cursor, limit) => {
  if (seq.length === 0) return -1;
  const last = limit === undefined ? norm.length - seq.length : Math.min(limit, norm.length - seq.length);
  for (let i = Math.max(0, cursor); i <= last; i++) {
    let ok = true;
    for (let j = 0; j < seq.length; j++) {
      if (!wordsMatch(norm[i + j], seq[j])) {
        ok = false;
        break;
      }
    }
    if (ok) return i;
  }
  return -1;
};

/**
 * Match a narration string against the normalized caption words.
 * Returns inclusive word indexes {start, end} or null.
 * @param {string[]} norm normalized caption words
 * @param {string} narration
 * @param {number} cursor first word index allowed
 */
export const matchNarrationSpan = (norm, narration, cursor) => {
  const toks = tokenize(narration);
  if (toks.length === 0 || norm.length === 0) return null;
  let start = -1;
  for (const n of [3, 2, 1]) {
    if (toks.length < n) continue;
    start = findSequence(norm, toks.slice(0, n), cursor);
    if (start >= 0) break;
  }
  if (start < 0) return null;
  const expectedEnd = start + toks.length - 1;
  let end = -1;
  for (const n of [3, 2, 1]) {
    if (toks.length < n) continue;
    const tail = toks.slice(toks.length - n);
    const windowEnd = start + Math.ceil(toks.length * 1.6) + 8;
    let best = -1;
    let bestDist = Infinity;
    let from = start;
    for (;;) {
      const idx = findSequence(norm, tail, from, windowEnd);
      if (idx < 0) break;
      const candidateEnd = idx + n - 1;
      const dist = Math.abs(candidateEnd - expectedEnd);
      if (dist < bestDist) {
        best = candidateEnd;
        bestDist = dist;
      }
      from = idx + 1;
    }
    if (best >= 0) {
      end = best;
      break;
    }
  }
  if (end < start) end = Math.min(norm.length - 1, expectedEnd);
  return { start, end };
};

/**
 * @typedef {{word: string, start: number, end: number}} CaptionWord
 * @typedef {{id: string, type: string, narration: string, est_duration_s: number, sync_points?: {phrase: string, event: string}[]}} SpecScene
 * @typedef {{label: string, starts_at_scene: string}} SpecChapter
 */

/**
 * Compute the scene layout.
 * @param {{spec: {scenes: SpecScene[], chapters?: SpecChapter[]}, captions?: CaptionWord[] | null, fps?: number, audioDurationS?: number | null}} input
 */
export const computeLayout = ({ spec, captions, fps = 30, audioDurationS = null }) => {
  const scenes = spec.scenes || [];
  const n = scenes.length;
  const words = (captions || [])
    .filter((w) => w && typeof w.start === "number" && typeof w.end === "number")
    .slice()
    .sort((a, b) => a.start - b.start);
  const norm = words.map((w) => normalizeWord(w.word));
  const hasCaptions = words.length > 0;

  const est = scenes.map((s) => {
    const base = Math.max(MIN_SCENE_SECONDS, Number(s.est_duration_s) || MIN_SCENE_SECONDS);
    return s.type === "end-card" ? Math.max(base, END_CARD_SECONDS) : base;
  });

  /** @type {(null | {start: number, end: number})[]} */
  const spans = new Array(n).fill(null);
  /** @type {(number | null)[]} */
  const anchors = new Array(n).fill(null);
  if (hasCaptions) {
    let cursor = 0;
    for (let i = 0; i < n; i++) {
      const m = matchNarrationSpan(norm, scenes[i].narration, cursor);
      if (m) {
        spans[i] = m;
        anchors[i] = words[m.start].start;
        cursor = m.end + 1;
      }
    }
  }
  anchors[0] = 0;

  const starts = new Array(n).fill(0);
  const ends = new Array(n).fill(0);
  let i = 0;
  while (i < n) {
    let j = i + 1;
    while (j < n && anchors[j] === null) j++;
    const runStart = i === 0 ? 0 : Math.max(anchors[i] ?? ends[i - 1], ends[i - 1]);
    starts[i] = runStart;
    if (j < n) {
      const available = Math.max(MIN_SCENE_SECONDS * (j - i), /** @type {number} */ (anchors[j]) - runStart);
      let total = 0;
      for (let k = i; k < j; k++) total += est[k];
      let t = runStart;
      for (let k = i; k < j; k++) {
        starts[k] = t;
        const dur = total > 0 ? (est[k] / total) * available : available / (j - i);
        t += dur;
        ends[k] = t;
      }
      ends[j - 1] = runStart + available;
    } else {
      let t = runStart;
      for (let k = i; k < j; k++) {
        starts[k] = t;
        let dur = est[k];
        const span = spans[k];
        if (span) dur = Math.max(dur, words[span.end].end - t + TAIL_SECONDS);
        t += dur;
        ends[k] = t;
      }
    }
    i = j;
  }
  if (n > 0 && audioDurationS != null && audioDurationS > 0) {
    ends[n - 1] = Math.max(ends[n - 1], audioDurationS + TAIL_SECONDS);
  }

  const chapters = (spec.chapters || [])
    .map((c, idx) => ({
      number: idx + 1,
      label: c.label,
      sceneId: c.starts_at_scene,
      sceneIndex: scenes.findIndex((s) => s.id === c.starts_at_scene),
    }))
    .filter((c) => c.sceneIndex >= 0)
    .sort((a, b) => a.sceneIndex - b.sceneIndex)
    .map((c) => ({ ...c, startS: starts[c.sceneIndex] }));

  const layoutScenes = scenes.map((scene, idx) => {
    const from = Math.round(starts[idx] * fps);
    const to = Math.round(ends[idx] * fps);
    let chapter = null;
    for (const c of chapters) if (c.sceneIndex <= idx) chapter = c;
    const span = spans[idx];
    const sceneWords = hasCaptions
      ? words.filter((w) => w.start >= starts[idx] && w.start < ends[idx])
      : [];
    const sceneNorm = sceneWords.map((w) => normalizeWord(w.word));
    const syncPoints = (scene.sync_points || []).map((sp) => {
      const toks = tokenize(sp.phrase);
      let atS = null;
      for (const k of [3, 2, 1]) {
        if (toks.length < k) continue;
        const hit = findSequence(sceneNorm, toks.slice(0, k), 0);
        if (hit >= 0) {
          atS = sceneWords[hit].start - starts[idx];
          break;
        }
      }
      return { event: sp.event, phrase: sp.phrase, atS };
    });
    return {
      id: scene.id,
      type: scene.type,
      index: idx,
      from,
      durationInFrames: Math.max(1, to - from),
      startS: starts[idx],
      endS: ends[idx],
      estDurationS: est[idx],
      matched: span !== null,
      wordStart: span ? span.start : null,
      wordEnd: span ? span.end : null,
      chapter: chapter ? { number: chapter.number, label: chapter.label } : null,
      syncPoints,
    };
  });

  const totalFrames = n > 0 ? Math.max(1, Math.round(ends[n - 1] * fps)) : 1;
  return {
    fps,
    hasCaptions,
    audioDurationS,
    totalFrames,
    totalS: n > 0 ? ends[n - 1] : 0,
    scenes: layoutScenes,
    chapters: chapters.map((c) => ({ number: c.number, label: c.label, sceneId: c.sceneId, startS: c.startS })),
  };
};

/**
 * Caption words spoken inside a scene (absolute times preserved).
 * @param {CaptionWord[]} words @param {{startS: number, endS: number}} scene
 */
export const wordsInScene = (words, scene) =>
  (words || []).filter((w) => w.start >= scene.startS && w.start < scene.endS);

/**
 * When each word of an on-screen line should appear, in seconds relative to
 * the scene start. The line's first word is looked for in the scene's caption
 * words (from `cursor` on); when found, the following words follow the next
 * caption words. Otherwise the words are spread evenly over [slotStart, slotEnd].
 * @param {string[]} lineWords
 * @param {CaptionWord[]} sceneWords
 * @param {number} sceneStartS
 * @param {number} slotStart
 * @param {number} slotEnd
 * @param {number} cursor
 */
export const revealTimes = (lineWords, sceneWords, sceneStartS, slotStart, slotEnd, cursor) => {
  const toks = lineWords.map(normalizeWord);
  const norm = sceneWords.map((w) => normalizeWord(w.word));
  let idx = -1;
  for (const k of [2, 1]) {
    if (toks.length < k) continue;
    idx = findSequence(norm, toks.slice(0, k), cursor);
    if (idx >= 0) break;
  }
  if (idx >= 0) {
    const times = toks.map((_, k) => {
      const w = sceneWords[Math.min(idx + k, sceneWords.length - 1)];
      return w.start - sceneStartS;
    });
    return { times, cursor: Math.min(sceneWords.length, idx + toks.length), matched: true };
  }
  const span = Math.max(0.2, slotEnd - slotStart);
  const times = toks.map((_, k) => slotStart + (span * k) / Math.max(1, toks.length));
  return { times, cursor, matched: false };
};

/**
 * Group caption words into pages of at most `maxWords`, breaking on pauses.
 * @param {CaptionWord[]} words @param {number} maxWords @param {number} maxSeconds
 */
export const pageWords = (words, maxWords = 6, maxSeconds = 2.4) => {
  /** @type {{words: CaptionWord[], start: number, end: number}[]} */
  const pages = [];
  let current = null;
  for (const w of words) {
    const gap = current ? w.start - current.end : 0;
    const tooLong = current ? w.end - current.start > maxSeconds : false;
    if (!current || current.words.length >= maxWords || gap > 0.6 || tooLong) {
      current = { words: [w], start: w.start, end: w.end };
      pages.push(current);
    } else {
      current.words.push(w);
      current.end = Math.max(current.end, w.end);
    }
  }
  return pages;
};
