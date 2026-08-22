# Scene Library

Thirteen scene types, one React component each under `remotion/src/scenes/`. Every scene renders inside `SceneFrame` (background, chapter badge, lower-third on-screen text, optional captions), so the table only lists what the scene itself draws. `data` keys not listed are ignored; keys listed as required make `render_longform.py` fail validation when missing.

| Scene type | When to use | `data` must carry | What a muted viewer understands | Duration |
|------------|-------------|-------------------|----------------------------------|----------|
| `title-card` | First scene of every episode | optional `title` (defaults to the spec title), `series_tag` | the episode's name and which series it belongs to | 8-15 s |
| `chapter-card` | The first scene of chapters 2 and later | optional `label` (defaults to the chapter label) | a new part starts; its number and name | 4-8 s |
| `kinetic-text` | The lines of the argument, one at a time, in sync with the voice | nothing; the lines come from `on_screen_text` (each at most 8 words, start a line with the narration's exact words to lock it to the voice) | the three to five claims, in order, and which word is being said | 6-12 s per line |
| `code-typing` | A command or config the viewer will type | `code` (string with newlines), optional `language`, `title` (filename) | what to type, and which flag is being talked about (lower third) | 4 s plus about 1 s per 18 characters; the speed rises so long code finishes at 85 % of the scene |
| `terminal-replay` | Proof: the real run on the Spark | `capture_ref` on the scene (an id in `capture.json`); optional `command` fallback, `playback: fit|realtime` | the command, the output scrolling, the exit code and the measured numbers as chips | 20-60 s; the cast is compressed to fit unless `playback: realtime` |
| `diagram` | How parts connect: data flow, memory, a pipeline | `nodes: [{id, label, accent?}]`, `edges: [{from, to, label?}]` (at most 12 nodes, labels at most 4 words) | the boxes, the direction of flow, the bottleneck (accent node or labelled edge) | 20-60 s; nodes enter left to right |
| `comparison-table` | Two or more named things, one decision | `columns` (first is the row label column), `rows` (arrays of cells), optional `winners` (column index per row, -1 for none) or `winner_col`, `title` | which option wins each row, row by row | 8 s plus 6-10 s per row; at most 6 rows and 4 columns |
| `chart` | Measured numbers across 2 to 6 categories | `series: [{label, values[]}]`, `kind: bar|line`, optional `categories[]`, `unit`, `title` | which bar is tallest and by how much; the numbers count up | 20-60 s; at most 4 series |
| `stat-callout` | The one number of the episode | `value` (number or string with a number), optional `unit`, `caption`, `context` | one big number and what it measures | 10-30 s |
| `quote` | One sentence worth reading twice | `text` (at most 40 words), optional `attribution` | the sentence, who said it | 10-25 s |
| `mascot-talk` | Framing, transitions, the honest caveat, anything without a visual of its own | optional `headline` (at most 6 words) | someone is talking to me; the lower third carries the claim | 20-60 s; never two in a row |
| `b-roll` | The physical box, hands, screens | `src` (path relative to the spec, for example `broll/spark.mp4`) | the real object; text from the lower third | 10-30 s; clips shorter than the scene loop |
| `end-card` | Last scene | `next_title`, optional `label` | the channel name and what comes next | 8 s minimum (enforced) |

## Shared fields every scene honors

- `on_screen_text`: lines shown as the lower third (except `kinetic-text`, which shows them as the main content, and cards that have none). Lines cycle evenly across the scene. At most 8 words are visible at once; longer lines are split.
- `data.captions_on: true`: draws word-timed captions in the safe area for this scene. Use it for scenes that define a term or cite a number, not everywhere; the SRT sidecar carries the full text.
- `sync_points: [{phrase, event}]`: ties an animation to the moment a phrase is spoken (needs captions). Events per scene type are listed in `rules/spec-to-composition.md`.
- `visual_intent` is required by the schema and is what the renderer shows in the b-roll placeholder; write it as the sentence a muted viewer should be able to say afterwards.

## Pacing rules the library assumes

- Visual change at least every 8 s (platform-specs): the components animate internally (rows, nodes, bars, typed text), so a scene may run 60 s only when its content keeps moving. A `quote` or `stat-callout` over 30 s goes static; split it.
- New information at least every 30 s: a chapter of five `kinetic-text` lines is fine; five `mascot-talk` scenes in a row are not.
- Digits belong on screen, words belong in the narration (`brand-vault/voice-rules.md`, Hard Constraint 4). Put `41.7 tok/s` in `data`, say "forty-one point seven tokens a second" in `narration`.
- Series defaults (`brand-vault/content-pillars.md`): benchmarks lean on `chart`, `comparison-table`, `terminal-replay`; explainers on `kinetic-text`, `diagram`, `mascot-talk`.

## Replacing the mascot

`remotion/src/mascot/Mascot.tsx` is a placeholder SVG. A real design replaces that file and keeps the props (`energy` 0..1 for the mouth, `blink`, `size`); `MascotTalk` does not change.
