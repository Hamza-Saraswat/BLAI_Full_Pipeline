# Publish and Published Note Formats

## `output/[slug]-publish.md`

```
---
slug: [slug]
blotato_post_id: [postSubmissionId]
scheduled_time: 2026-08-25T18:00:00-05:00
privacy: public
media_url: https://.../previews/[slug]/final.mp4
---

# Publish: [slug]

- Title: ...
- Slot: ... (rule that chose it)
- Blotato response: 201, id ...
- Status polls: 2026-08-25T18:07Z published, https://youtube.com/shorts/...
```

## `published/[slug].md`

```
---
slug: [slug]
workspace: shorts
title: ...
pillar: ...
structure: ...
style_pack: ...
published_slot: 2026-08-25T18:00:00-05:00
youtube_url: ""
blotato_post_id: ...
views_7d: 0
---

# [title]

Hub note: [[../videos/[slug]]]
Package: [[../stages/05-package/output/[slug]-package]]
```

The published note is read by the radar (dedupe), the package stage (no duplicate titles, related links) and the weekly retro (views). Keep its frontmatter flat.
