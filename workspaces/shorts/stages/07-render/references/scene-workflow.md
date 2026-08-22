# Scene Workflow

## Where files go

```
[build-dir]/[slug]/
├── voice/      narration.wav, alignment.json, captions.json, captions.srt   (from stage 06)
├── scenes/     s01.mp4 ... sNN.mp4, one per storyboard scene, plus each scene's source folder
└── render/     final.mp4, lint.json, safe-zone.json
```

`[build-dir]` is `BLAI_BUILD_DIR` from `build/.env` (default `~/blai/builds`).

## Parallelism and retries

- One worker (subagent) per scene, three in parallel. Each worker receives only: its scene row from the storyboard, the scene's target duration from the Timing table, the style pack file, `rules/scene-agent.md`, and the tool rule file for its renderer.
- Draft quality first (low resolution or short frame range), verify against the scene brief and the duration, then final quality.
- At most 5 attempts per scene, feeding the exact error text back each time. After 5, mark the scene blocked with the last error and stop; do not thrash.
- Duration tolerance: 0.15 s. Captions own the caption band; scene content never enters it.

## Assembly

`assemble.py` generates the Remotion props from the storyboard and the scene files, renders with captions and music, and runs `lint_video.py`. Run `safe_zone_check.py` yourself afterwards. On a failure, fix the scene named in the report and re-assemble; never patch the mp4.

## Preview delivery

`telegram-video`: attach `final.mp4` to the gate card when it is under 48 MB (Shorts always are). Otherwise upload with `skills/blotato-publish/scripts/r2.py upload` and send the link. Record the message id in the render note.

## Re-render feedback

When the hub note carries `feedback` from a Re-render tap, apply it to the scene it names (or every scene if it names none) before rendering; quote the feedback in the render note's Attempts section.
