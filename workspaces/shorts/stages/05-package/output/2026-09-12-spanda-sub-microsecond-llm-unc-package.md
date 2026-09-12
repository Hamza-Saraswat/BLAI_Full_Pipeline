---
slug: 2026-09-12-spanda-sub-microsecond-llm-unc
title: "LLM uncertainty: 652 ns, no GPU"
title_type: searchable
seo_score: 92
---

# Package: LLM uncertainty: 652 ns, no GPU

## Titles
1. [searchable] LLM uncertainty: 652 ns, no GPU (chosen)
2. [intriguing] Your local model knows when it's guessing
3. [intriguing] Spanda catches hallucinations before you read them

## Description
LLM uncertainty scoring in 652 nanoseconds: Spanda stamps every local reply as guess or known.
Ask the same question three times; agreement means trust, scatter means guessing. Spanda, a
small Rust gateway, runs that check on a CPU core beside Ollama for 0.076 ms per reply -- the
neural detector it replaces burns 92.4 ms on a GPU. The catch: only the scoring is that fast,
and a tuned giant can repeat one wrong answer every time.

Everything here is the author's own benchmark, not yet independently replicated.

Spanda on GitHub: https://github.com/Adarshent/Spnda

Channel: https://youtube.com/@BuildLocalAI

#LocalLLM #Ollama #Spanda

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20/20 | "LLM uncertainty" (the primary keyword) opens the title; 28 visible chars <= 40; accurate; no caps-lock, no emoji |
| Title type and complement | 10/10 | tagged searchable (search-heavy topic: the ideas note's keyword gap is a physical explanation of "llm uncertainty"); title does not restate the hook ("Six hundred fifty-two nanoseconds. Spanda just ratted your local model out.") |
| Description | 20/20 | keyword + promise in the first 150 chars ("LLM uncertainty scoring in 652 nanoseconds"); unique text; first line above names the promise, channel line present; ~700 bytes << 5,000 |
| Hashtags | 5/5 | 3 hashtags, product names first, no spaces |
| Tags list | 5/5 | 12 phrases, ~150 chars, primary keyword + variants + misspelling + topic + format |
| Frame 1 | 15/15 | storyboard s01: "652 ns" giant-number fills the safe area at frame 1, fully legible, motion onset t=0.30s |
| Shorts physics | 10/10 | 1080x1920 vertical, storyboard target 38 s (band 32-38, hard max 60), hook text at frame 1 within 0.5 s |
| Compliance | 15/15 | contains_synthetic_media false (typographic scenes + creator's own cloned voice, both exempt); made_for_kids false; original_insight written; no YMYL persona |
| **Total** | **92/100** | pass (>= 80) |

## Compliance
- contains_synthetic_media: false (typographic animated scenes and the creator's own cloned voice; both explicitly exempt under the altered-or-synthetic rules)
- original_insight: This Short is the only walkthrough that separates what the 652 ns buys (the scoring arithmetic, per reply) from what it does not (the K=3 sampling runs and the 120B Confident Mode Collapse inversion), which the README's own parity claim blurs.

## Manifest
```json
{
  "slug": "2026-09-12-spanda-sub-microsecond-llm-unc",
  "format": "short",
  "title": "LLM uncertainty: 652 ns, no GPU",
  "title_variants": [
    {"text": "LLM uncertainty: 652 ns, no GPU", "type": "searchable"},
    {"text": "Your local model knows when it's guessing", "type": "intriguing"},
    {"text": "Spanda catches hallucinations before you read them", "type": "intriguing"}
  ],
  "description": "LLM uncertainty scoring in 652 nanoseconds: Spanda stamps every local reply as guess or known.\n\nAsk the same question three times; agreement means trust, scatter means guessing. Spanda, a small Rust gateway, runs that check on a CPU core beside Ollama for 0.076 ms per reply -- the neural detector it replaces burns 92.4 ms on a GPU. The catch: only the scoring is that fast, and a tuned giant can repeat one wrong answer every time.\n\nEverything here is the author's own benchmark, not yet independently replicated.\n\nSpanda on GitHub: https://github.com/Adarshent/Spnda\n\nChannel: https://youtube.com/@BuildLocalAI\n\n#LocalLLM #Ollama #Spanda",
  "hashtags": ["#LocalLLM", "#Ollama", "#Spanda"],
  "tags": ["llm uncertainty", "llm uncertainty detection", "llm confidence scores", "hallucination detection local llm", "spanda", "spnda", "ollama hallucination check", "local llm", "rust llm gateway", "epistemic uncertainty", "semantic entropy", "local ai short"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "18:00 CT",
  "related_long_form_url": "",
  "original_insight": "This Short is the only walkthrough that separates what the 652 ns buys (the scoring arithmetic, per reply) from what it does not (the K=3 sampling runs and the 120B Confident Mode Collapse inversion), which the README's own parity claim blurs.",
  "seo_score": 92
}
```

## Notes
Publish slot hint 18:00 CT: today's other Short (local-llm-vs-claude) holds the 11:00 slot per
pick order. Description wording keeps the unreplicated-benchmark hedge that the script's Notes
for review asks to carry into packaging.
