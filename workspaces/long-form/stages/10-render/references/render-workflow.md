# Render Workflow (long-form)

## Files

```
[build-dir]/[slug]/
├── voice/      narration.wav, alignment.json, captions.json, captions.srt
├── capture/    capture.json, cmd*.cast
└── render/     final.mp4, thumbnails/1.png 2.png 3.png, chapters.json, captions.srt, render.json, lint.json
```

## Draft then final

A draft renders at a third of the resolution and only the first 900 frames; use it to catch a missing capture, a table that overflows, a sync point that misses. Fix the spec (scene `data`, durations, sync points) rather than the renderer. Then render final. A long episode takes 30-60 minutes on the Spark; do not run two renders at once.

## Preview delivery

Episodes exceed Telegram's attachment limit, so the gate card carries an R2 link (`r2.py upload`). The link is unguessable but public; delete the object after publish (`r2.py delete`) or let the weekly cleanup do it.

## Chapters

Measured chapter times come from the voice note's Chapters table (the first word of each chapter's first beat in `captions.json`). Write them to `chapters.json`; the publish stage replaces the description's chapter block with them. The first entry is always `00:00`.

## Thumbnails

Three stills from the spec's concepts. The card shows all three; the hub note's `thumbnail_pick` (1, 2 or 3) chooses, default 1. Export JPG under 2 MB if a PNG is too large.

## Re-render feedback

Apply `feedback` to the scenes it names before rendering, quote it in the render note, and clear it from the hub note after a successful render.
