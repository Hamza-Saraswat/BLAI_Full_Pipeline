---
slug: 2026-08-23-which-model-fits-gpu
target_duration_s: 720
scenes: 44
---

# Spec: Which build fits the card you own

One scene per script beat, 44 of them, narration lifted verbatim from `05-script/output/2026-08-23-which-model-fits-gpu-narration.txt`. Nothing was measured on this machine, there is no experiment plan and no `capture.json`, so the Capture column is empty on every row and no scene is a `terminal-replay`.

## Scene sequence

| # | Id | Beat | Type | Chapter | Est s | On-screen text | Visual intent | Capture |
|---|----|------|------|---------|-------|----------------|---------------|---------|
| 1 | s01 | 1.1 | `title-card` | 1 | 16.4 | - | The episode's name and its series tag: this is a buyer's guide about which build to download, not a news item. | - |
| 2 | s02 | 1.2 | `quote` | 1 | 17.6 | Not measured here. Every source named. | A plain card admitting that no number in this episode was measured on this channel's own hardware. | - |
| 3 | s03 | 1.3 | `kinetic-text` | 1 | 21.6 | The model page hands you a parameter count / That number tells you almost nothing / What decides is how many gigabytes sit resident / Only one of those numbers is printed | A parameter count is the number you are shown; gigabytes resident is the number that decides, and it is printed somewhere else. | - |
| 4 | s04 | 1.4 | `diagram` | 1 | 16.8 | one model, many builds | One model name fans out into several differently sized builds; the decision is which build, not which model. | - |
| 5 | s05 | 1.5 | `diagram` | 1 | 16.0 | 8 / 12 / 24 GB | One card's memory, drawn once and fixed: no second card, no rented server, so everything else has to move instead. | - |
| 6 | s06 | 1.6 | `comparison-table` | 1 | 17.6 | unsloth/Qwen3.8-27B-GGUF | A published file listing with sizes in gigabytes and the publisher's name in frame; that size is where the arithmetic starts. | - |
| 7 | s07 | 2.1 | `chapter-card` | 2 | 15.2 | - | Chapter two opens: the file is only one of the three things sharing the card's memory. | - |
| 8 | s08 | 2.2 | `diagram` | 2 | 19.6 | KV cache = running notes | The weights sit still while a second block, the KV cache, grows with every word sent and every word returned. | - |
| 9 | s09 | 2.3 | `kinetic-text` | 2 | 15.2 | Think of the loaded weights as one room / Your conversation keeps a desk in that room / the desk grows all evening / the room does not stretch to help | A room that never changes size with a desk inside it that keeps growing; the room does not stretch to help. | - |
| 10 | s10 | 2.4 | `kinetic-text` | 2 | 14.8 | NVIDIA publishes the arithmetic for that cache / 2xlayersxheadsxdimxbytes (NVIDIA) / That is the cost of one token | NVIDIA's per-token cache cost written as words multiplied by words, not as symbols. | - |
| 11 | s11 | 2.5 | `stat-callout` | 2 | 17.2 | ~2 GB @ 4,096 tokens (NVIDIA) | Two gigabytes of cache, from NVIDIA's own worked example, taking a visible bite out of an eight gigabyte card. | - |
| 12 | s12 | 2.6 | `diagram` | 2 | 15.6 | 32 query heads / 8 KV heads | Thirty-two query heads collapse into eight shared key-value groups; the printed formula still counts the thirty-two. | - |
| 13 | s13 | 2.7 | `kinetic-text` | 2 | 17.2 | That sharing is grouped-query attention / it cuts the notes several times over / you overstate its cache by 4 times / config.json - Qwen3-8B | Grouped-query attention cuts the cache several times over, so the printed formula overstates a modern model fourfold. | - |
| 14 | s14 | 2.8 | `quote` | 2 | 16.0 | "no easy way to calculate" | A maintainer's own sentence: the last cost has no easy calculation, so the band at the top of the bar gets no number. | - |
| 15 | s15 | 2.9 | `diagram` | 2 | 17.2 | longer context = more memory | The context length you type is a purchase: set it longer and the memory required goes up, paid out of the same card. | - |
| 16 | s16 | 2.10 | `diagram` | 2 | 16.4 | file + cache < card - slack | The finished bar: file, cache and a top band that still carries no number, with slack deliberately left over. | - |
| 17 | s17 | 3.1 | `chapter-card` | 3 | 16.8 | - | Chapter three opens: one dial, quantization, turns the same parameter count into different file sizes. | - |
| 18 | s18 | 3.2 | `chart` | 3 | 17.2 | 6.19 GB -> 25.3 GB (Unsloth) | One model's published ladder, bottom rung to top rung, for the same twenty-seven billion parameters. | - |
| 19 | s19 | 3.3 | `chart` | 3 | 15.6 | 8 GB and 24 GB, same model | The ladder's rungs line up against consumer card tiers: one model reaches all of them, as different builds. | - |
| 20 | s20 | 3.4 | `kinetic-text` | 3 | 17.6 | You can do this sum yourself / 27B x 4 bits = 13.5 GB / The published file table does not agree | The viewer's own parameters-times-bits sum appears, then the published file table refuses to agree with it. | - |
| 21 | s21 | 3.5 | `comparison-table` | 3 | 19.2 | Q4_K_M 4.8944 bpw / Q8_0 8.5008 | Nominal quantization labels sit beside their measured widths, and none of them line up. | - |
| 22 | s22 | 3.6 | `comparison-table` | 3 | 15.2 | perplexity: lower is better | The episode's table gains its quality column, measured in perplexity, and the column is still empty. | - |
| 23 | s23 | 3.7 | `chart` | 3 | 18.0 | +0.0535 vs +0.8698 ppl (7B) | Two published perplexity penalties side by side: one barely visible, one long. | - |
| 24 | s24 | 3.8 | `comparison-table` | 3 | 16.8 | Row A: biggest model that fits | Row A fills across every column: take the largest build that fits, and stop before the bottom rungs. | - |
| 25 | s25 | 4.1 | `chapter-card` | 4 | 13.6 | - | Chapter four opens: same axis, same units, a second row underneath the first. | - |
| 26 | s26 | 4.2 | `chart` | 4 | 15.2 | 5.63 GB (4-bit) / 9.53 GB (8-bit) | A short ladder whose top rung, the eight-bit build, still sits below the ten gigabyte line. | - |
| 27 | s27 | 4.3 | `diagram` | 4 | 19.6 | top rung fits 12 GB | The whole ladder drops inside a twelve gigabyte card with space left over, so the question changes from whether to how much. | - |
| 28 | s28 | 4.4 | `quote` | 4 | 16.4 | arXiv 2212.09720 (2022) | The sentence everyone quotes, with the paper and the year that produced it. | - |
| 29 | s29 | 4.5 | `kinetic-text` | 4 | 14.8 | Read what the paper says it measured / Zero-shot accuracy, no worked examples first / No instruction-tuned models in the sweep / No reasoning evaluation of any kind | The paper's own stated scope, line by line, each one narrowing what the quoted sentence covers. | - |
| 30 | s30 | 4.6 | `kinetic-text` | 4 | 16.8 | The sizes it tested ran from 19M parameters / up to 176B of them / Every model in it was released before 2022 / The people quoting it usually are not | The sizes the sweep covered, and the date stamp that greys the whole source out. | - |
| 31 | s31 | 4.7 | `diagram` | 4 | 19.6 | more training data = more damage | More training tokens on one side, more damage under quantization on the other; the arrow between them is the finding. | - |
| 32 | s32 | 4.8 | `stat-callout` | 4 | 14.8 | ~1,700 scenarios (arXiv 2510.10964) | The size of the controlled reasoning study, and the result that runs the rule backwards. | - |
| 33 | s33 | 4.9 | `comparison-table` | 4 | 16.0 | 32B @ 4-bit: strictly dominated | Three builds ranked on reasoning: the largest one, at four bits, sits lowest of the three. | - |
| 34 | s34 | 4.10 | `comparison-table` | 4 | 15.6 | Row B wins on quality | Row B fills across the same columns and the quality cell is the only one that flips which row reads better. | - |
| 35 | s35 | 5.1 | `chapter-card` | 5 | 15.6 | - | Chapter five opens: the gap is widest on long documents, which is where the exceptions start. | - |
| 36 | s36 | 5.2 | `comparison-table` | 5 | 13.6 | -59% on long context | The table again, with one row ringed: long context and cheap builds are a bad pairing. | - |
| 37 | s37 | 5.3 | `diagram` | 5 | 14.4 | MoE: all experts resident | A router wakes a few experts per word while every expert stays resident in memory anyway. | - |
| 38 | s38 | 5.4 | `diagram` | 5 | 16.0 | 47B resident, 12B of compute | You pay memory for a dense forty-seven billion parameter model and get the compute of a twelve billion one. | - |
| 39 | s39 | 5.5 | `stat-callout` | 5 | 16.8 | 82.5 GB smallest build | One file block dwarfing the memory bar it was meant to sit inside; no build on that page gets you there. | - |
| 40 | s40 | 5.6 | `diagram` | 5 | 14.0 | it splits, it does not refuse | Layers spilling out of the card into system memory while the runtime keeps answering and never says a word about it. | - |
| 41 | s41 | 5.7 | `code-typing` | 5 | 16.8 | 48% CPU / 52% GPU / shape of the documented output, not a capture | The shape of the process listing Ollama documents, typed out, with the split percentages in the processor column; not a recording of our own run. | - |
| 42 | s42 | 5.8 | `diagram` | 5 | 17.6 | no published figure for runtime | The unlabelled band from chapter two, still carrying no number, with the instruction not to fill the card to the brim. | - |
| 43 | s43 | 5.9 | `code-typing` | 5 | 16.0 | ollama ps | The one check to run tonight, typed out: load the model, then ask for the process listing and read the split. | - |
| 44 | s44 | 5.10 | `end-card` | 5 | 12.0 | - | The channel wordmark and what comes next; the decision rule is the last thing spoken and nothing follows it. | - |

## Chapter cards

| # | Chapter | Starts at | Scene type there |
|---|---------|-----------|------------------|
| 1 | Which Build Actually Fits | `s01` | `title-card` (chapter 1 opens the episode, so the title card is its card) |
| 2 | File Plus Cache | `s07` | `chapter-card` |
| 3 | More Parameters, Fewer Bits | `s17` | `chapter-card` |
| 4 | Fewer Parameters, More Bits | `s25` | `chapter-card` |
| 5 | The Rule And Its Exceptions | `s35` | `chapter-card` |

## Thumbnail concepts

1. words: "27 billion parameters" | focus: the number `6.19 GB` -- the hook's contradiction, a huge parameter count against a small file (variant 1: words left, focus in the amber disc).
2. words: "It splits, not refuses" | focus: `48% CPU` -- the silent failure, the number the runtime never warns you about (variant 2: the number is the thumbnail).
3. words: "More bits beats parameters" | focus: `8-bit vs 4-bit` -- the reversal, the episode's thesis as a versus (variant 3: amber block left, words right).

Three different ideas, not three wordings: a contradiction, a failure, a rule. None repeats the title.

## Scene-type histogram

| Type | Count |
|------|-------|
| `diagram` | 12 |
| `kinetic-text` | 7 |
| `comparison-table` | 7 |
| `chapter-card` | 4 |
| `chart` | 4 |
| `quote` | 3 |
| `stat-callout` | 3 |
| `code-typing` | 2 |
| `title-card` | 1 |
| `end-card` | 1 |

Ten distinct types. No type appears three times in a row. No `terminal-replay`, no `mascot-talk`, no `b-roll`.

## Decisions

**No `terminal-replay` anywhere, and no `capture_ref` on any scene.** Nothing in this episode ran on our bench: the outline records the Spark as unreachable, there is no `03-research/output/...-experiment.md` and no `capture.json`. A replayed cast renders as a recording of a real run and would present Ollama's published documentation as our own measurement. The script's author already made this call for beats 5.7 and 5.9 and used `code-typing`; it is honoured everywhere, and no beat in this script carried a `terminal-replay` hint that needed downgrading. Beat 5.7's `data.title` says "shape of Ollama's documented output" and its lower third repeats "shape of the documented output, not a capture", so the claim is on screen, not just in the spec.

**One scene per beat, so the cards carry beat narration.** The Verify rule requires the scene narrations, concatenated, to equal the narration file; every scene needs non-empty narration; and the narration file contains nothing but the 44 beats. A title card, chapter card or end card with invented card-only narration would break that check, so each card carries its beat instead. The consequence is that the cards run long against the scene library's guidance (`title-card` 8-15 s, `chapter-card` 4-8 s): here they run 13.6-16.8 s. Every one is far inside the binding 45 s cap. If a future edit wants short cards, the narration file has to gain card-only lines first.

**Beat 1.2, `mascot-talk` -> `quote` (disabled type).** The mascot has no design yet. The beat is the episode's honesty statement and reads as one sentence worth reading twice, so `quote` carries it, attributed to the channel, with the narration's own words as the quote text.

**Beat 1.6, `b-roll` -> `comparison-table` (disabled type).** No stock source exists. The beat asks the viewer to open a published file listing and read a size, so the scene is that listing: `unsloth/Qwen3.8-27B-GGUF` as the table title with the publisher's name in frame, and the two published rungs the episode actually cites (6.19 GB and 25.3 GB) as its rows. No file size is invented to pad the table.

**Beat 4.7, `chart` -> `diagram`.** The script asked for "a curve climbing as training tokens climb". The Scaling Laws for Precision result is directional -- degradation increases with training data size -- and no numbers for that curve are cited anywhere upstream. A `chart` needs `series.values`, and inventing them to draw a plausible curve would fabricate a measurement. The scene states the same finding as a causal chain instead.

**Beat 4.8, `chart` -> `stat-callout`.** The script asked for two bars swapping places. The only figure the beat carries is roughly 1,700 scenarios; the 8B-at-8-bit-beats-14B-at-4-bit result is published as an ordering, not as scores, so there is nothing to put on a bar's height. The number becomes the callout and its caption carries the result. The ordering is drawn one beat later at `s33`, as a ranked `comparison-table` (beat 4.9, also downgraded from `chart` for the same reason), which is where the three-way "strictly dominated" finding belongs anyway.

**The table has four columns, not six.** The outline's visual philosophy asks for one comparison table that never changes its six columns. `comparison-table` is capped at four columns and six rows by the renderer (`skills/render-longform/rules/scene-library.md`; `ComparisonTable.tsx` shrinks cells past four). The table is therefore the row label plus three: **Contender | File size | Fits | Quality**. Those four are identical at `s22`, `s24`, `s34` and `s36` -- the table gains a row per contender and its Quality cell is the only cell that changes, which is the discipline the outline was actually protecting.

**`kinetic-text` lines are narration-locked, not the script's shorthand.** The scene library requires each line to start with the narration's exact words so the reveal locks to the voice without a sync point. The script's on-screen cells are shorthand ("parameter count -> gigabytes resident"), which would not lock. Those beats get 3-4 lines of at most 8 words each, drawn from their own narration with digits substituted for spoken numbers. Where the script's cell already reads as a line it is kept verbatim: `2xlayersxheadsxdimxbytes (NVIDIA)` at `s10`, `config.json - Qwen3-8B` at `s13`, `27B x 4 bits = 13.5 GB` at `s20`. Every other scene uses the script's on-screen cell exactly as written.

**Sync points only where a number has to land on a word.** 32 of them, and every phrase was checked to occur in its own scene's narration: count-ups on `stat-callout`, `row:n` on the tables, `series:n` on the charts, `node:id` on the diagrams, `reveal` on the quotes and `type` on the two `code-typing` scenes. `kinetic-text` needs none -- its lines lock on their own first words.

**Durations.** `est_duration_s` is each beat's word count at 2.5 words a second, the rate the script wrote to. They sum to 722.0 s against a 720 s target, 0.3 % off. The longest scene is 21.6 s (`s03`), so the 45 s cap is never near, and nothing needed the `code-typing` exemption.

**Digits stay off the narration and on the screen.** No scene's `narration` was edited -- it is byte-for-byte the narration file -- so every number is spoken as words and written as digits in `data` and `on_screen_text`. The rounded figures the script flagged are on screen at full precision: 4.8944 and 8.5008 bpw at `s21`, +0.0535 and +0.8698 ppl at `s23`.

## Could not honour

**Beat 1.1's on-screen pairing does not appear at 0:00.** The outline's "number by 0:20" asks for 6.19 GB on screen beside the parameter count it contradicts. `s01` has to be the `title-card` (spec-format: one title card first) and `TitleCard.tsx` renders with `lowerThird={false}`, so a title card draws no `on_screen_text` at all. The pairing is spoken in the hook, it is thumbnail concept 1, and the digits first render at `s03`, about 34 s in. Fixing it properly means either a title that carries the numbers -- a stage 07 decision, not this stage's -- or a `title-card` variant that accepts a subtitle.

**Beat 5.1's long-context chart is displaced by the mandatory chapter card.** The -0.8 % against up to -59 % comparison is the strongest number in chapter 5 and the script wanted two accuracy bars for it. Chapter 5 starts on that beat, so `s35` is its `chapter-card`. Both figures are recovered one scene later at `s36`, in the Quality column of the running table with row B ringed, and "-59% on long context" is its lower third. Same information, one beat late, as a table row instead of bars.

**Beat 5.10's decision rule is not drawn on screen.** `end-card` also renders with `lowerThird={false}`; it draws the wordmark, the handle, and `next_title`. The payoff is spoken over it and nothing follows it, which is what the script asked for, but "Biggest that fits. Then spend on bits." is not typeset. `data.next_title` is "Memory bandwidth: the other axis" -- the episode the outline explicitly reserves the Spark's bandwidth figures for. It carries no unverified number.

**The three cards' on-screen text cells are dropped.** For the same `lowerThird={false}` reason at `s01`, `s07`, `s17`, `s25` and `s35`, the script's on-screen cells for beats 1.1, 2.1, 3.1, 4.1 and 5.1 have nowhere to render. `on_screen_text` is omitted on those five scenes rather than written and silently ignored.
