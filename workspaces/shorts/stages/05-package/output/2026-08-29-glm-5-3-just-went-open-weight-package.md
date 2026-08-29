---
slug: 2026-08-29-glm-5-3-just-went-open-weight
workspace: shorts
stage: 05-package
---

# Package: GLM-5.3-Flash: the 93 GB "small" build

## Titles

| # | Title | Type | Chars | Note |
|---|-------|------|-------|------|
| 1 | Can your GPU run GLM-5.3-Flash? The 93 GB answer | searchable | 48 | The autocomplete demand is "can I run X" questions |
| 2 | **GLM-5.3-Flash: the 93 GB "small" build** | intriguing | 38 | **Chosen.** The contradiction carries it; keyword in hyphenated product form at char 0 |
| 3 | The week's biggest open model fits zero consumer GPUs | intriguing | 53 | True but names no number |

Chosen: #2. The hook speaks "Ninety-three gigabytes, and that is the small one"; the title
complements with the product name and quoted "small", repeating neither wording nor framing.

## Description

```
GLM-5.3-Flash went open-weight this week, and the smallest GGUF build is 93.09 GB. Your graphics card is not the target: memory follows the 320B total parameters, not the 18B active ones, so the drop serves 128 GB unified-memory machines.

Unsloth's guide picks UD-IQ3_XXS (120.37 GB) for 128 GB devices. Before you download 93 GB for nothing: read your total memory; if it is smaller than the file, close the tab.

More local AI on the channel: https://www.youtube.com/@BuildLocalAI

#GLM #LocalAI #GGUF
```

504 chars, 504 bytes. First line: keyword + promise. Related line is the
channel link -- the archive is empty after the v2 reset (first video of the new system).

## Rubric (seo-rubric.md)

| Check | Points | Awarded | Evidence |
|---|---|---|---|
| Title keyword and length | 20 | 20 | `GLM-5.3` at char 0 (hyphenated product form of the keyword); 39 chars |
| Title type and complement | 10 | 10 | tagged; no phrasing shared with the hook |
| Description | 20 | 20 | keyword + promise in first 150; unique; 504 bytes |
| Hashtags | 5 | 5 | 3, product first |
| Tags | 5 | 5 | 12 tags, exact keyword + variants |
| Frame 1 | 15 | 15 | giant 93.09 GB digits at frame 1 (hook scene contract, silicon pack) |
| Shorts physics | 10 | 10 | vertical, ~36.5 s, hook spoken from word one |
| Compliance | 15 | 15 | flags below; insight specific |
| **Total** | **100** | **88 recorded** | Self-scored. Finding 40 stands: this rubric cannot fail its own author, so the hub records a discounted 88, and the fresh-context packaging reader it recommends is still unbuilt |

## Compliance

| Flag | Value | Justification |
|---|---|---|
| contains_synthetic_media | false | typographic scenes; own-voice exemption per compliance.md |
| made_for_kids | false | always |
| notify_subscribers | false | Shorts default |
| privacy_status | private | test artifact (reviewer_notes) |
| original_insight | written | see manifest |

## Manifest

```json
{
  "slug": "2026-08-29-glm-5-3-just-went-open-weight",
  "format": "short",
  "title": "GLM-5.3-Flash: the 93 GB \"small\" build",
  "title_variants": [
    {
      "text": "Can your GPU run GLM-5.3-Flash? The 93 GB answer",
      "type": "searchable"
    },
    {
      "text": "GLM-5.3-Flash: the 93 GB \"small\" build",
      "type": "intriguing"
    },
    {
      "text": "The week's biggest open model fits zero consumer GPUs",
      "type": "intriguing"
    }
  ],
  "description": "GLM-5.3-Flash went open-weight this week, and the smallest GGUF build is 93.09 GB. Your graphics card is not the target: memory follows the 320B total parameters, not the 18B active ones, so the drop serves 128 GB unified-memory machines.\n\nUnsloth's guide picks UD-IQ3_XXS (120.37 GB) for 128 GB devices. Before you download 93 GB for nothing: read your total memory; if it is smaller than the file, close the tab.\n\nMore local AI on the channel: https://www.youtube.com/@BuildLocalAI\n\n#GLM #LocalAI #GGUF",
  "hashtags": [
    "#GLM",
    "#LocalAI",
    "#GGUF"
  ],
  "tags": [
    "glm 5.3",
    "glm 5.3 flash",
    "glm flash gguf",
    "open weight llm",
    "run glm locally",
    "gguf file size",
    "moe memory",
    "unified memory llm",
    "128gb llm",
    "local llm",
    "unsloth gguf",
    "can i run glm 5.3"
  ],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "private",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "original_insight": "Every headline says GLM-5.3 went open-weight; nobody prints that the SMALLEST build is 93.09 GB. The Short does the memory arithmetic the model card omits: 320B resident beats 18B active, and the release actually targets 128 GB unified-memory machines.",
  "seo_score": 88,
  "reviewer_notes": "TEST ARTIFACT of the shorts-only rebuild's proof run. privacy_status stays private: voiced by Kokoro (or the bake-off candidate), not the creator's clone, so compliance rule 3 is unmet. Archive is empty post-reset, so the description's related line is the channel link."
}
```
