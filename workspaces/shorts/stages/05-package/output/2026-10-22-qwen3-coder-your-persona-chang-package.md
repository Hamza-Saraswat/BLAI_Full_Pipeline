---
slug: 2026-10-22-qwen3-coder-your-persona-chang
title: "Qwen3-Coder: persona changes security"
title_type: searchable
seo_score: 95
---

# Package: Qwen3-Coder: persona changes security

## Titles
1. [searchable] Qwen3-Coder: persona changes security (chosen: keyword "qwen3 coder" had the day's deepest autocomplete, 85 suggestions, and search-heavy viewers watch about twice as long; the title states the finding the way they would type the query)
2. [intriguing] Qwen3-Coder knows who you are
3. [intriguing] Telling Qwen3-Coder who you are is a risk

## Description
Qwen3-Coder prompt security: telling the model who you are changes how secure its code comes out.

Hirundo had Qwen3-Coder-30B-A3B build the same secret-storage app 190 times per persona, changing only the customer phrase, and attacked every app with BaxBench exploits. US defense contractor: 70% hackable. Chinese contractor: 59%. Asking for secure code made it worse (74%). The fix that closed the gap was editing the weights, not the prompt. Booz Allen separately reports +130% for Qwen3-Coder under a US government persona via API testing without significance tests; the numbers use different baselines and are not interchangeable. You'll learn why your intro line is a security setting and what actually moved the number. Try it tonight: read every identity detail out of your system prompt and see it as a setting, not small talk.

Full episode: https://youtube.com/@BuildLocalAI

(Narration is AI-generated.)

#Qwen3Coder #LocalAI #AISecurity

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20/20 | "Qwen3-Coder" in chars 1-11; 37 visible chars; accurate; one caps token; no emoji |
| Title type and complement | 10/10 | searchable, matches the deepest-autocomplete surface; does not restate the hook text ("I'm a US dev building my startup") |
| Description | 20/20 | keyword + promise in first 92 chars; unique text; channel line present; 949 bytes |
| Hashtags | 5/5 | 3, product first, no spaces |
| Tags list | 5/5 | 16 phrases, 152 chars, primary keyword + variants |
| Frame 1 | 15/15 | "Qwen3-Coder / I'm a US dev building my startup" fully legible at frame 1 inside the safe area, cursor motion onset at 0.4 s |
| Shorts physics | 10/10 | vertical 1080x1920, 43 s target, hook text at frame 1 |
| Compliance | 15/15 | contains_synthetic_media false (typographic scenes, creator's own cloned voice); made_for_kids false; original_insight specific; no YMYL persona (the topic touches security, claims are attributed to named sources) |

Total: 100. Deducted 5 in the stored seo_score for the title stopping one word short of the full finding ("persona changes security" vs "your persona changes its security", 47 chars would still fit); the shorter form reads cleaner in the feed.

## Compliance
- contains_synthetic_media: false (typographic scenes and the creator's own cloned voice, both explicitly exempt per compliance.md)
- original_insight: Every Qwen3-Coder video covers what it can code; this one is built on Hirundo's measured persona gap (70% vs 59% hackable) plus the finding that asking for secure code made it worse, so the viewer stops treating their intro line as small talk and starts treating it as a security setting.

## Manifest
```json
{
  "slug": "2026-10-22-qwen3-coder-your-persona-chang",
  "format": "short",
  "title": "Qwen3-Coder: persona changes security",
  "title_variants": [
    {"text": "Qwen3-Coder: persona changes security", "type": "searchable"},
    {"text": "Qwen3-Coder knows who you are", "type": "intriguing"},
    {"text": "Telling Qwen3-Coder who you are is a risk", "type": "intriguing"}
  ],
  "description": "Qwen3-Coder prompt security: telling the model who you are changes how secure its code comes out.\n\nHirundo had Qwen3-Coder-30B-A3B build the same secret-storage app 190 times per persona, changing only the customer phrase, and attacked every app with BaxBench exploits. US defense contractor: 70% hackable. Chinese contractor: 59%. Asking for secure code made it worse (74%). The fix that closed the gap was editing the weights, not the prompt. Booz Allen separately reports +130% for Qwen3-Coder under a US government persona via API testing without significance tests; the numbers use different baselines and are not interchangeable. You'll learn why your intro line is a security setting and what actually moved the number. Try it tonight: read every identity detail out of your system prompt and see it as a setting, not small talk.\n\nFull episode: https://youtube.com/@BuildLocalAI\n\n(Narration is AI-generated.)\n\n#Qwen3Coder #LocalAI #AISecurity",
  "hashtags": ["#Qwen3Coder", "#LocalAI", "#AISecurity"],
  "tags": ["qwen3 coder", "qwen 3", "qwen3 coder security", "qwen3 coder review", "ai code security", "llm generated code vulnerabilities", "local llm", "run llm locally", "ollama", "lm studio", "baxbench", "hirundo", "ai coding model", "open weight models", "secure coding ai", "build local ai"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "Every Qwen3-Coder video covers what it can code; this one is built on Hirundo's measured persona gap (70% vs 59% hackable) plus the finding that asking for secure code made it worse, so the viewer stops treating their intro line as small talk and starts treating it as a security setting.",
  "seo_score": 95
}
```
