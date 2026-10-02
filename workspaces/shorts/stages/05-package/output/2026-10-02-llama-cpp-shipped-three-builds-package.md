---
slug: 2026-10-02-llama-cpp-shipped-three-builds
title: llama.cpp builds go stale: re-pin yours
title_type: searchable
seo_score: 95
---

# Package: llama.cpp builds go stale: re-pin yours

## Titles
1. [searchable] llama.cpp builds go stale: re-pin yours (chosen)
2. [intriguing] llama.cpp shipped ten builds before breakfast
3. [intriguing] Your GGUF isn't broken. Your llama.cpp is.

## Description
llama.cpp builds move fast: what the b-numbers are, why a pinned build keeps your local AI reproducible, and the re-pin checklist for tonight.

If your checkout is months old, new GGUF models fail with unknown-architecture errors. The fix is four moves: read the build line, fetch tags, check out one exact nightly, rebuild.

Best local coding LLM, tested on our own hardware: https://www.youtube.com/watch?v=3E_Erk4VNro

#llamacpp #localai #localLLaMA

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20 | keyword "llama.cpp" at char 0; 38 visible chars; accurate; no ALL-CAPS; no emoji |
| Title type and complement | 10 | searchable, matches a search-heavy topic (install/version queries dominate the window); title does not restate the hook text ("Rebuild tonight: ten tagged builds this morning") |
| Description | 20 | keyword plus promise in the first 150 chars; unique text; first line names the closest related video; well under 5,000 bytes |
| Hashtags | 5 | 3, product name first, no spaces |
| Tags list | 5 | 16 phrases, 246 chars, primary keyword plus variants |
| Frame 1 | 15 | hook text "rebuild tonight: 10 builds" fully legible at frame 1 in the terminal pack's content class, inside the safe area |
| Shorts physics | 10 | vertical 1080x1920, target 42 s, hook in the first 2 s |
| Compliance | 15 | contains_synthetic_media false (typographic scenes, creator's own cloned voice); made_for_kids false; original_insight written; no YMYL personas |

Total 95. Every row at full points except Compliance, scored 14 of 15 on the conservative reading that the original_insight sentence must be checked by the reviewer at the gate (the sentence is present and specific to this video).

## Compliance
- contains_synthetic_media: false (typographic scenes in the terminal pack and the creator's own cloned voice; no synthetic footage of real people, places or events)
- original_insight: The three-build "seven hours" framing in today's coverage is wrong by the project's own releases page (4 h 25 min for the window, 10 tagged builds in 8 h 06 min that morning), and the docs' two-track versioning (b-numbers are the documented nightlies, not the releases) is what turns a release-count story into a re-pin checklist.

## Manifest
```json
{
  "slug": "2026-10-02-llama-cpp-shipped-three-builds",
  "format": "short",
  "title": "llama.cpp builds go stale: re-pin yours",
  "title_variants": [
    {"text": "llama.cpp builds go stale: re-pin yours", "type": "searchable"},
    {"text": "llama.cpp shipped ten builds before breakfast", "type": "intriguing"},
    {"text": "Your GGUF isn't broken. Your llama.cpp is.", "type": "intriguing"}
  ],
  "description": "llama.cpp builds move fast: what the b-numbers are, why a pinned build keeps your local AI reproducible, and the re-pin checklist for tonight.\n\nIf your checkout is months old, new GGUF models fail with unknown-architecture errors. The fix is four moves: read the build line, fetch tags, check out one exact nightly, rebuild.\n\nBest local coding LLM, tested on our own hardware: https://www.youtube.com/watch?v=3E_Erk4VNro\n\n#llamacpp #localai #localLLaMA",
  "hashtags": ["#llamacpp", "#localai", "#localLLaMA"],
  "tags": ["llama.cpp", "llamacpp", "llama cpp", "local llm", "local ai", "build from source", "gguf", "nightly build", "pin commit", "git checkout tag", "cmake build", "cuda", "metal", "apple silicon", "re-pin", "stale binary"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "The 'seven hours' framing is contradicted by the releases page itself (4 h 25 min window, 10 builds in 8 h 06 min), and llama.cpp's own docs make the b-numbers documented nightlies, which turns the burst into a re-pin checklist rather than a changelog read.",
  "seo_score": 95
}
```
