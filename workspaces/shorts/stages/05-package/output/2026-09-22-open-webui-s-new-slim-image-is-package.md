---
slug: 2026-09-22-open-webui-s-new-slim-image-is
title: "Open WebUI slim image: the 175 MB pull"
title_type: searchable
seo_score: 100
---

# Package: Open WebUI slim image: the 175 MB pull

## Titles
1. [searchable] Open WebUI slim image: the 175 MB pull (chosen: keyword topic for a search-heavy surface, autocomplete depth 208, competing titles are install guides)
2. [intriguing] Your Open WebUI pull just lost 89%
3. [intriguing] Open WebUI without the ML stack

## Description
Open WebUI's new slim image pulls at about 175 MB, 89% smaller than the last release. Here is what got cut, and the one tag to swap tonight.

Build Local AI runs all of this on local boxes: https://youtube.com/@BuildLocalAI

The standard image carried torch, bundled speech models and ffmpeg for work you probably delegate to Ollama or a hosted API anyway. Slim drops them: the registry itself lists the slim tag at 168.31 MB compressed, while the standard image stays at 1.54 GB. The catch is real: slim refuses to start on MySQL or S3 storage, and voice, PDF reading and local embeddings move to external services. Chatting through Ollama changes nothing, and your Docker volume keeps every chat.

#openwebui #localai #docker

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20 | 20: "Open WebUI" starts at char 1, 38 visible chars, accurate, no ALL-CAPS, no emoji |
| Title type and complement | 10 | 10: searchable, matches search surface; does not restate the hook text ("download just shrank eighty-nine percent") |
| Description | 20 | 20: keyword + promise in first 140 chars, unique text, channel line present, 330 bytes |
| Hashtags | 5 | 5: three, product name first, no spaces |
| Tags list | 5 | 5: 12 phrases, 138 chars, primary keyword + variants + misspelling guard |
| Frame 1 | 15 | 15: storyboard s01 holds a static giant "89%" centered in the safe area at frame 1 with motion onset at 0.30 s |
| Shorts physics | 10 | 10: vertical 1080x1920, target 38.6 s, hook is sentence one and frame-1 text |
| Compliance | 15 | 15: contains_synthetic_media false (typographic scenes, creator's own cloned voice), made_for_kids false, original_insight below, no YMYL |

Score: 100.

## Compliance
- contains_synthetic_media: false (typographic terminal scenes and the creator's own cloned voice; no realistic synthetic footage)
- original_insight: The registry's own tag page is the receipt nobody reads: 168.31 MB compressed sits beside the 1.44 GB previous slim and the 1.54 GB standard, and the 89% is slim versus last slim, not versus standard -- the framing the release headline does not give you.

## Manifest
```json
{
  "slug": "2026-09-22-open-webui-s-new-slim-image-is",
  "format": "short",
  "title": "Open WebUI slim image: the 175 MB pull",
  "title_variants": [
    {"text": "Open WebUI slim image: the 175 MB pull", "type": "searchable"},
    {"text": "Your Open WebUI pull just lost 89%", "type": "intriguing"},
    {"text": "Open WebUI without the ML stack", "type": "intriguing"}
  ],
  "description": "Open WebUI's new slim image pulls at about 175 MB, 89% smaller than the last release. Here is what got cut, and the one tag to swap tonight.\n\nBuild Local AI runs all of this on local boxes: https://youtube.com/@BuildLocalAI\n\nThe standard image carried torch, bundled speech models and ffmpeg for work you probably delegate to Ollama or a hosted API anyway. Slim drops them: the registry itself lists the slim tag at 168.31 MB compressed, while the standard image stays at 1.54 GB. The catch is real: slim refuses to start on MySQL or S3 storage, and voice, PDF reading and local embeddings move to external services. Chatting through Ollama changes nothing, and your Docker volume keeps every chat.\n\n#openwebui #localai #docker",
  "hashtags": ["#openwebui", "#localai", "#docker"],
  "tags": ["open webui", "open webui slim", "open webui docker", "open webui update", "open webui 0.11.4", "openwebui", "local ai", "self hosted llm", "docker image size", "ollama web ui", "local llm", "run llm locally"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "The registry's own tag page is the receipt nobody reads: 168.31 MB compressed sits beside the 1.44 GB previous slim and the 1.54 GB standard, and the 89% is slim versus last slim, not versus standard -- the framing the release headline does not give you.",
  "seo_score": 100
}
```
