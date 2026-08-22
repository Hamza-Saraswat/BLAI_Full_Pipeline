# Package Note Format (long-form)

Same layout as the Shorts package note (titles, description, rubric, compliance, manifest), with these differences:

- `format` is `"long"`, `notify_subscribers` is `true`.
- The manifest carries `chapters`: `[{"time": "00:00", "label": "Intro"}, {"time": "01:32", "label": "What fits in 128 GB"}, ...]` with times estimated from the spec. The render stage writes the measured times to `[build-dir]/[slug]/render/chapters.json`; `publish.py --chapters` replaces the block in the description at upload time.
- The description's chapter block is generated from the manifest's `chapters` list, one line per chapter `MM:SS Label`, placed after the summary sentences and before links.
- `thumbnail` names the chosen still (`thumbnails/1.png` by default; the hub note's `thumbnail_pick` overrides).
- `related_long_form_url` is empty; instead list up to two related episodes from `published/` in the description.

Example manifest fields beyond the Shorts example:

```json
{
  "format": "long",
  "notify_subscribers": true,
  "chapters": [
    {"time": "00:00", "label": "The 128 GB question"},
    {"time": "01:40", "label": "Loading DeepSeek V4 Flash"},
    {"time": "05:10", "label": "Tokens per second, measured"},
    {"time": "09:30", "label": "What to run tonight"}
  ],
  "thumbnail": "thumbnails/1.png"
}
```
