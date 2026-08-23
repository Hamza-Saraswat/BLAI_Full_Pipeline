---
slug: 2026-08-23-which-model-fits-gpu
workspace: long-form
stage: 10-render
lint_pass: false
---

# Render: LLM GPU Requirements: Which Qwen Build Fits Your Card

**LOCAL TEST RENDER.** Voiced by Kokoro `am_eric`, not the ElevenLabs clone. Not publishable (see the package's compliance note).

## Output

| | |
|---|---|
| File | `.local-builds/2026-08-23-which-model-fits-gpu/render/final.mp4` |
| Duration | **493.4 s** (8:13) |
| Video | 1920x1080, h264, yuv420p, 30/1 |
| Audio | aac 48 kHz |
| Size | 28.8 MB |
| Render wall time | 386.9 s (0.0 min) for 14,799 frames |
| Scenes | 44, all 44 re-timed from caption words |
| Warnings | [] |

## Linter

**`lint_longform.py` FAILED on one row: duration.**

```
FAIL duration: 493.4 (expected 648 to 792 s (target 720 +/- 10 %))
```

Passing: exists, codec, resolution (1920x1080), fps (30), pix_fmt (yuv420p), color_range (`tv`, so `--color-space=bt709` applied), audio_stream, audio_codec (aac), audio_rate (48000).

This is **not a render defect**. It is finding 48: the outline targets 150 words per minute, the script wrote 1,838 words for twelve minutes at that rate, and the voice runs at 3.691 words per second. The episode is 8:13. To land inside the window at this rate the script needs roughly 2,400-2,900 words, against the 1,500-2,100 band stage 05 enforces. The script gate and the render gate are asking for incompatible things and were never reconciled against a measured voice.

## Audit

| Check | Result |
|---|---|
| Linter | **FAIL** (duration only, see above) |
| Thumbnails | PASS -- 3 stills, all 1280x720, 0.05-0.07 MB (limit 2 MB) |
| Chapters | PASS -- 5, one per spec chapter, ascending, all >= 10 s apart |
| Captures | PASS -- the spec has zero `terminal-replay` scenes and zero `capture_ref`s, so nothing rendered as a placeholder. **Stage 08 skipping cleanly is confirmed:** the Spark was unreachable, no capture note was needed, and nothing blocked |

## Verify

| Compare | Result |
|---|---|
| Narration heard in the cut vs `narration.txt` | PASS -- the 44 scene narrations concatenate to 10,249 characters identical to the narration file; no beat dropped |
| Scene order and count vs the spec | PASS -- identical ids in identical order |
| Chapter cards at chapter starts | PASS -- the `chapter-card` set equals chapters 2-5's start scenes exactly |

## Chapters (measured, replacing the estimates)

| # | Measured | Estimated | Label | Scene |
|---|---|---|---|---|
| 1 | **00:00** | 00:00 | Which Build Actually Fits | s01 |
| 2 | **01:07** | 01:46 | File Plus Cache | s07 |
| 3 | **02:57** | 04:30 | More Parameters, Fewer Bits | s17 |
| 4 | **04:30** | 06:46 | Fewer Parameters, More Bits | s25 |
| 5 | **06:27** | 09:29 | The Rule And Its Exceptions | s35 |

The estimates were out by up to three minutes. `publish.py --chapters` replaces the description block with these at upload.

## Voice

| | |
|---|---|
| Engine | kokoro (`am_eric`, speed 1.05) -- ElevenLabs key absent |
| Alignment | whisper.cpp `ggml-base.en.bin`, 1,758 words heard mapped onto 1,809 |
| Words per second | **3.691** (measured; the pipeline assumed 2.9) |
| Chunks | 3, concatenated -- the first real exercise of the multi-chunk path that finding 43 fixed |
| Pronunciation aliases | 19 hits across 8 terms (Qwen, Ollama, NVIDIA, Unsloth, DGX, DeepSeek, KV cache, Mixtral) |

## Defects found in this render

- **Finding 45** -- the lower third overlaps the quote attribution. `SceneFrame.tsx:70` raises the lower third by `CAPTION_BAND_PX` (110) when captions are on; `Quote.tsx:41` pins the attribution at +150. Visible at 0:18.
- **Finding 47** -- the hook's numbers (27B, 6.19 GB) are spoken at 0:03 and first drawn at 0:22, because `TitleCard` renders `lowerThird={false}`. Same cause leaves the payoff decision rule untypeset on the end card.
- **Finding 46** (reviewer call) -- 15 of 44 scenes set `captions_on`, so 36 % of the episode carries burned-in captions. This follows `scene-library.md:24`, and the SRT sidecar ships alongside.
- Minor: the chart's y-axis tops at 50 for a 25.3 maximum; a chart label rounds 6.19 to 6.2 while the narration says 6.19.

## What rendered correctly

Comparison tables with headers and source lines, charts with labelled GB axes and value labels, kinetic text with amber emphasis, chapter headers, the chapter progress bar, word-timed captions with the active word in amber, and the end card. The scene library holds up at 1920x1080.
