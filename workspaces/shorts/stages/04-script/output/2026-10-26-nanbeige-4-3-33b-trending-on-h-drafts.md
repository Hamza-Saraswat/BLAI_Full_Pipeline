---
slug: 2026-10-26-nanbeige-4-3-33b-trending-on-h
stage: 04-script
---

# Drafts: Nanbeige 4.3 33B (24 GB card vs 19 GB file)

Two blind kimi-k3 writers, different structures, different hook patterns. Both passed every gate before judging.

## Draft A -- number-first, hook pattern number-shock ("Nanbeige 4.3: 19 GB on disk")

```json
{
  "title": "Nanbeige 4.3 33B: 19 GB File, Will It Fit Your RAM?",
  "description": "Nanbeige4.3-33B is trending on Hugging Face; here is the nineteen-gigabyte file and the memory math that decides whether your machine runs it tonight.",
  "hashtags": ["#Nanbeige43", "#LocalLLM", "#GGUF"],
  "hook_text": "Nanbeige 4.3: 19 GB on disk",
  "music_mood": "curious-tech",
  "analogy": null,
  "scenes": [
    {
      "id": "s1",
      "role": "hook",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "Nanbeige four point three is trending. The real number is a nineteen-gigabyte file. Your hardware has to hold it.",
      "on_screen_text": "Nanbeige 4.3 33B: 19 GB on disk | trending on Hugging Face",
      "visual_brief": "Frame 1: dark background, giant amber '19 GB' centered, small caption 'Nanbeige 4.3: 19 GB on disk' beneath. Motion onset at 0.35 s: the digits scale from 92% to 100% with a soft fade. On 'is trending' a thin amber ticker line rises-in-place under the caption, labeled 'trending on Hugging Face'. On 'Your hardware has to hold it' a small desktop-tower icon fades in beside the number. Visual change at least every 2.5 s, amber accent only.",
      "sfx": [{"at": "number-reveal", "name": "ding"}]
    },
    {
      "id": "s2",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "It's a G G U F, the single file local models ship in. Bartowski's Hugging Face conversion squeezes each weight to four bits.",
      "on_screen_text": "GGUF: one file to load | bartowski on Hugging Face | 4 bits per weight",
      "visual_brief": "A single file icon labeled 'GGUF' fades in center on 'the single file local models ship in'. On 'Bartowski's Hugging Face conversion' the label 'bartowski on Hugging Face' rises-in-place above the icon. On 'squeezes each weight to four bits' the icon scales down slightly and the beat '4 bits per weight' ticks in below it. Dark background, amber accent, entrances are fade or scale only, change at least every 3 s.",
      "sfx": [{"at": "start", "name": "pop"}]
    },
    {
      "id": "s3",
      "role": "explain",
      "tool": "manim",
      "layout_archetype": "timeline",
      "narration": "The K V cache, its working memory, grows with context. The card claims half a million tokens. Filling that context wants about a hundred and four gigabytes of cache.",
      "on_screen_text": "KV cache: working memory | 524,288 tokens claimed | ~104 GiB for the cache",
      "visual_brief": "A horizontal axis labeled 'context' draws left to right on 'grows with context', with a short amber bar above the origin. On 'half a million tokens' the axis extends to a far amber tick labeled '524,288 tokens'. On 'about a hundred and four gigabytes' a tall amber bar labeled '~104 GiB for the cache' rises-in-place at that tick, dwarfing the first bar. Fade and rise entrances only, dark background, one amber accent, visual change at least every 3 s.",
      "sfx": [{"at": "number-reveal", "name": "tick"}]
    },
    {
      "id": "s4",
      "role": "foreshadow",
      "tool": "hyperframes",
      "layout_archetype": "split-compare",
      "narration": "A twenty-four gigabyte GPU runs that G G U F with modest context. A machine with one hundred and twenty-eight gigabytes takes weights plus serious context.",
      "on_screen_text": "24 GB GPU: modest context | 128 GB: weights + big context",
      "visual_brief": "Screen splits into two cards on a dark background. The left card fades in on 'twenty-four gigabyte GPU', labeled '24 GB GPU', with a short amber bar marked 'modest context'. The right card fades in on 'one hundred and twenty-eight gigabytes', labeled '128 GB', and its tall amber bar fills on 'weights plus serious context'. Amber accent only, fade and scale entrances, change at least every 3 s."
    },
    {
      "id": "s5",
      "role": "payoff_close",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "Load it in LM Studio or Ollama tonight. Your memory decides, not Hugging Face's trending page.",
      "on_screen_text": "LM Studio or Ollama | no official Ollama tag yet | your RAM decides",
      "visual_brief": "The line 'LM Studio or Ollama' fades in centered on 'Load it in LM Studio or Ollama tonight'; a small note 'no official Ollama tag yet' rises-in-place beneath it on 'or Ollama tonight'. Final frame rhymes with frame 1: same dark background, same giant centered amber type and caption layout as the opening, now reading 'your RAM decides' on 'Your memory decides, not the trending page'. This closing composition is the loop anchor matching the first frame.",
      "sfx": [{"at": "end", "name": "pop"}]
    }
  ],
  "notes_for_review": "Rounded: 19.36 GiB to 'nineteen gigabytes' (packet-fixed hook string), 524,288 tokens to 'half a million tokens'; kept 'about' on the 104 GiB cache since the source value is approximate. Hedged: no tokens-per-second or Q4 quality claims (unverified in brief); the 8K-16K context range is glossed as 'modest context' to stay at five key numbers. Flag: 'four bits' is spoken as the quant name, not a sixth brief key number; no analogy used."
}
```

## Draft B -- worked-example, hook pattern situation ("24 GB card vs 19 GB model") -- WINNER

```json
{
  "title": "Nanbeige 4.3 33B on a 24 GB Card: The Memory Math",
  "description": "Nanbeige 4.3 33B is trending on Hugging Face, so here is the memory math for the 24 GB card you already own.",
  "hashtags": ["#Nanbeige43", "#LocalLLM", "#GGUF"],
  "hook_text": "24 GB card vs 19 GB model",
  "music_mood": "steady-build",
  "analogy": null,
  "scenes": [
    {
      "id": "s1",
      "role": "hook",
      "tool": "manim",
      "layout_archetype": "split-compare",
      "narration": "You've got a twenty-four gigabyte card. Nanbeige four point three is a nineteen-gigabyte file.",
      "on_screen_text": "24 GB card vs 19 GB model",
      "visual_brief": "Frame 1: dark background, giant text '24 GB card vs 19 GB model' top center, two empty vertical amber-outlined bars below, left labeled 'your card', right labeled 'the model'. Motion onset at 0.35 s: the left bar fades in and fills amber on 'twenty-four gigabyte card'; the right bar rises-in-place to just below the left bar's rim on 'nineteen-gigabyte file', leaving a thin dark gap that pulses once.",
      "sfx": [{"at": "number-reveal", "name": "pop"}]
    },
    {
      "id": "s2",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "Step one: load the file onto your card. It downloads as a G G U F, the one file local models ship in.",
      "on_screen_text": "Step 1: fit the file | GGUF: one file, whole model",
      "visual_brief": "Centered stack on dark: the line 'Step 1: fit the file' fades in on 'Step one'. A single amber document icon labeled 'GGUF' scales in center-frame on 'G G U F'. On 'the one file local models ship in' the icon settles onto a horizontal card outline at the bottom and the card's memory bar fills amber to about four-fifths, holding there.",
      "sfx": [{"at": "number-reveal", "name": "tick"}]
    },
    {
      "id": "s3",
      "role": "foreshadow",
      "tool": "manim",
      "layout_archetype": "timeline",
      "narration": "The model also promises half a million tokens of context. Each token rents working memory, a cache that piles beside the weights.",
      "on_screen_text": "context: 524,288 tokens | cache grows per token",
      "visual_brief": "A horizontal amber timeline labeled 'context' stretches rightward on 'half a million tokens of context', tick marks multiplying toward an end label reading '524,288'. On 'rents working memory' small amber blocks begin stacking upward above the ticks, forming a second growing bar. On 'piles beside the weights' the cache stack rises until it rivals a static 'weights' block drawn at the left.",
      "sfx": []
    },
    {
      "id": "s4",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "Step two: cap the context window before loading. Your leftovers hold roughly eight to sixteen thousand tokens. Bartowski's build loads in LM Studio tonight.",
      "on_screen_text": "Step 2: cap the context | room left: 8K-16K tokens",
      "visual_brief": "On 'cap the context window' an amber slider fades in and its handle pins near the low end of a track. Giant amber text '8K-16K' scales in center on 'eight to sixteen thousand tokens', with 'tokens of context left' beneath it. On 'Bartowski's build' a lower line 'bartowski / LM Studio' rises-in-place and stays.",
      "sfx": [{"at": "number-reveal", "name": "ding"}]
    },
    {
      "id": "s5",
      "role": "payoff_close",
      "tool": "manim",
      "layout_archetype": "split-compare",
      "narration": "A hundred and twenty-eight gigabytes buys the long conversations. Your card still runs it, and trending never got a vote.",
      "on_screen_text": "128 GB: long conversations | your card still runs it",
      "visual_brief": "Rhymes with frame 1: the same two-bar split-compare composition from the hook returns, card bar left, model bar nested inside it. On 'hundred and twenty-eight gigabytes' a much taller amber bar rises-in-place to the right, dwarfing the pair. On 'Your card still runs it' the original card bar pulses once. On 'trending never got a vote' all motion stops, holding the frame-1 layout for the loop.",
      "sfx": [{"at": "end", "name": "tick"}]
    }
  ],
  "notes_for_review": "Rounded for the ear: 19.36 GiB to 'nineteen gigabytes', 524,288 tokens to 'half a million' (screen shows the exact 524,288 in the same scene), 8K-16K to 'eight to sixteen thousand tokens'; 24 GB and 128 GB are as the brief states them. Hedged: the 24 GB fit and 8K-16K window come from webdiga's config-math analysis (medium confidence), so no speed or quality claims are made anywhere. No analogy used; the single wry beat is 'rents working memory' in scene 3, aimed at the cache."
}
```

## Judge scores (0-3 each row, max 24)

| Row | A | B |
|-----|---|---|
| 1_hook | 2 | 2 |
| 2_payoff | 3 | 3 |
| 3_specificity | 3 | 3 |
| 4_voice | 3 | 3 |
| 5_navigation | 3 | 2 |
| 6_difference | 2 | 3 |
| 7_repeat | 3 | 3 |
| 8_teaching | 3 | 3 |
| **Total** | **22** | **22** |

Winner: **B** -- Tied at 22, B wins the row-6 tiebreak: its situation opening and 'trending never got a vote' landing are fresh across the whole ledger tail, while A's giant-number shock replays the 10-23 script's opening rhythm and shape.

Grafts: none.

What A would have needed: A needed an opening rhythm that did not replay the 10-23 number-shock, and it needed the viewer's own 24 GB card on screen before the verdicts so the close feels like math the viewer did rather than a decree. Trading one stat beat for the explicit 24-minus-19 subtraction would have matched B's predictive payoff without touching its clean number budget.

Factual drift: none; nearest miss is A's spoken 'Load it in LM Studio or Ollama tonight,' which leans past the brief's LM Studio/llama.cpp load path but is hedged on screen by 'no official Ollama tag yet' in the same beat, so the absence is disclosed, not contradicted

## Gate trail
- Draft A after writer round 1: eval failure scene_specificity (3/5); fixed (GGUF term into s4, Hugging Face into s5, 33B on screen in s1); final validator 0 blockers 0 advisories, eval all gates pass, variety clean.
- Draft B after writer round 1: eval failures number_spend (heard 1) + positional_labels (label verb "fit" not an action verb) + 2-sentence tail advisory; fixed ("is a nineteen-gigabyte file", "load the file", tail merged); final validator 0 blockers 0 advisories, eval all gates pass, variety clean.
- Soft gates failed with reason on both: entity_spend (0.18 / 0.06) and top2 want the exact token "Nanbeige4.3-33B"; the script speaks "Nanbeige four point three" per the spoken-number rules, exact id on screen in scene 1.
