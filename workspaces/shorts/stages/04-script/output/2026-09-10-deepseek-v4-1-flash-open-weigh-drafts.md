# `output/2026-09-10-deepseek-v4-1-flash-open-weigh-drafts.md`

**Topic:** DeepSeek V4.1 Flash open weights and the KV cache compression story
**Draft A:** news-react-so-what / named-contradiction | **Draft B:** number-first / number-shock
**Ledger window checked:** last five entries, 2026-09-02 through 2026-09-09

---

## Gate check (before scoring)

Both drafts were scanned against the hard constraints. Neither is bounced:

- No hype words, no fake urgency, no em dashes in narration, no positional labels. All digits stay on screen; all spoken numbers are words with units and referents.
- Sentence caps hold. Longest sentence is 17 words (A, s02) and 16 (B, s04); both averages sit near 9.
- Person is clean. "We" in both drafts is legal: "our arithmetic" and "we couldn't find one yet" are things the channel actually did.
- Finding 17: both keep absence as absence ("We couldn't find one yet") and both hedge the 0.9 GB figure as "our arithmetic." No drift spoken as assertion.
- Fairness note (finding 16): neither draft is myth-bust; no row-2 adjustment applied.

**Watch items logged, not gated (shared by both, so no scoring effect):**
1. "Quant" is spoken in both closes with no same-breath gloss. Audience-fluent, but constraint 3 reads strictly on it. Voice-rules candidate.
2. Both s04 sentences carry two new numbers ("a million-token context… one gigabyte"), grazing constraint 5. Scored under row 3, not bounced.
3. Neither draft glosses "parameters"; A also never glosses "token." Logged as voice-rules candidates, consistent with how the gate passed both.

---

## Draft A (structure: news-react-so-what, hook pattern: named-contradiction) — in full

```json
{
  "slug": "2026-09-10-deepseek-v4-1-flash-open-weigh",
  "topic": "DeepSeek V4.1 Flash open weights and the KV cache compression story",
  "title": "DeepSeek V4.1 Flash: open weights just landed",
  "description": "working value, package stage overwrites",
  "hashtags": [
    "#deepseek",
    "#localai",
    "#llm"
  ],
  "hook_text": "Flash beat Pro. Your card can't.",
  "hook_candidates": [
    "Eight hundred ninety bytes. That is what one token costs now.",
    "DeepSeek V4.1 Flash just dropped its weights, free.",
    "This model's notes shrank four hundred thirty-seven times.",
    "You've got twenty-four gigabytes. A million-token context just got cheap.",
    "Your GPU isn't the problem. Your notes are.",
    "DeepSeek just shrank the cost of context memory 437 times.",
    "Your chat history is about to stop filling your RAM.",
    "DeepSeek's new Flash beat its own Pro. Your card is the catch. *",
    "One token used to cost 389,120 bytes. Now 890. *",
    "Twenty-four gigabytes won't hold the weights. The notes will fit."
  ],
  "style_pack": "signal",
  "script_format": "classic",
  "structure": "news-react-so-what",
  "value_types": [
    "TEACHES",
    "EQUIPS"
  ],
  "analogy": {
    "vehicle": "a kitchen where most cooks share one clipboard of running prep notes",
    "mapping": "the clipboard is the KV cache; sharing it across layers is CSA2 cross-layer reuse; half-size shorthand is FP4",
    "limit": "FP4 really does lose precision and sharing only works because the model was trained to share"
  },
  "music_mood": "curious-tech",
  "tags": [
    "deepseek v4.1 flash",
    "deepseek",
    "kv cache",
    "local ai",
    "run local llm",
    "open weights",
    "quantization",
    "gguf",
    "mixture of experts",
    "huggingface",
    "local llm",
    "ai news",
    "free ai model",
    "llm memory",
    "mac studio llm",
    "dgx spark"
  ],
  "scenes": [
    {
      "id": "s01",
      "role": "hook",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "DeepSeek's new Flash beat its own Pro. Your card is the catch. Free weights dropped this morning.",
      "on_screen_text": "Flash beat Pro. Your card can't.",
      "visual_brief": "Frame 1 composition: finished amber-on-dark kinetic headline \"Flash beat Pro. Your card can't.\" fully legible, GPU-card silhouette below. Motion onset within 0.5 s of frame 1: a slow pulse on \"can't\" starting at 0.4 s. On 'Free weights dropped this morning' a small HF-style download tag rises in place under the headline.",
      "est_duration_s": 6
    },
    {
      "id": "s02",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "One token of context now costs eight hundred ninety bytes of KV cache, a model's running notes.",
      "on_screen_text": "890 bytes per token",
      "visual_brief": "On 'One token of context' a single token chip fades in at center. On 'eight hundred ninety bytes' the giant amber 890 scales in with 'bytes per token' beneath. On 'a model's running notes' two thin note-lines fade in stacked beside the number.",
      "est_duration_s": 6
    },
    {
      "id": "s03",
      "role": "explain",
      "tool": "manim",
      "layout_archetype": "diagram-flow",
      "narration": "DeepSeek's layers share one set of notes, written in half-size shorthand. Sous chefs, one clipboard; the model trained to share.",
      "on_screen_text": "One shared clipboard, half-size notes",
      "visual_brief": "On 'share one set of notes' three layer boxes fade in left, each holding a note-card; the three cards fade out as one shared card scales in at center. On 'half-size shorthand' the shared card scales to half size. On 'the model trained to share' a tiny dumbbell glyph fades in beside it.",
      "est_duration_s": 7
    },
    {
      "id": "s04",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "split-compare",
      "narration": "By our arithmetic, a million-token context needs under one gigabyte of cache. The weights: five hundred fifty-two billion parameters. They won't fit your card.",
      "on_screen_text": "0.9 GB cache vs 552B parameters",
      "visual_brief": "Split screen, cache left, weights right. On 'under one gigabyte of cache' a small amber bar labeled 0.9 GB scales in left, tagged 'our math'. On 'five hundred fifty-two billion parameters' a massive dark block labeled 552B rises right, dwarfing the bar. On \"won't fit your card\" the GPU silhouette from frame 1 fades in under the block with an amber X scaling onto it.",
      "est_duration_s": 8
    },
    {
      "id": "s05",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "timeline",
      "narration": "That beat-its-Pro score is DeepSeek's own harness. And a finished local build? We couldn't find one yet.",
      "on_screen_text": "Vendor harness. No finished quant yet.",
      "visual_brief": "On 'That beat-its-Pro score' a small vendor-harness tag fades in top corner over a faint benchmark row. On \"We couldn't find one yet\" three empty quant-listing slots appear along a thin timeline, each flashing empty; no fill animation.",
      "est_duration_s": 6
    },
    {
      "id": "s06",
      "role": "payoff_close",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "Your twenty-four gigabyte card is the gate. Watch for the first quant that fits.",
      "on_screen_text": "Your card is the gate",
      "visual_brief": "Frame rhymes with frame 1: same amber-on-dark centered geometry. On 'Your card is the gate' the line fades in alone, mirroring the frame-1 headline. On 'the first quant that fits' one slot from the timeline fills amber once, then the wordmark settle.",
      "est_duration_s": 5,
      "render_notes": "wordmark settle; last frame rhymes with frame 1"
    }
  ],
  "narration_full": "DeepSeek's new Flash beat its own Pro. Your card is the catch. Free weights dropped this morning. One token of context now costs eight hundred ninety bytes of KV cache, a model's running notes. DeepSeek's layers share one set of notes, written in half-size shorthand. Sous chefs, one clipboard; the model trained to share. By our arithmetic, a million-token context needs under one gigabyte of cache. The weights: five hundred fifty-two billion parameters. They won't fit your card. That beat-its-Pro score is DeepSeek's own harness. And a finished local build? We couldn't find one yet. Your twenty-four gigabyte card is the gate. Watch for the first quant that fits.",
  "target_duration_s": 38,
  "notes_for_review": "Rounded nothing; 0.9 GB is our arithmetic per the brief and is hedged on screen. The benchmark scores are DeepSeek own-harness, said out loud. Analogy limit stated in the catch scene."
}
```

---

## Draft B (structure: number-first, hook pattern: number-shock) — in full

```json
{
  "slug": "2026-09-10-deepseek-v4-1-flash-open-weigh",
  "topic": "DeepSeek V4.1 Flash open weights and the KV cache compression story",
  "title": "DeepSeek V4.1 Flash: open weights just landed",
  "description": "working value, package stage overwrites",
  "hashtags": [
    "#deepseek",
    "#localai",
    "#llm"
  ],
  "hook_text": "389,120 bytes then. 890 now.",
  "hook_candidates": [
    "Eight hundred ninety bytes. That is what one token costs now.",
    "DeepSeek V4.1 Flash just dropped its weights, free.",
    "This model's notes shrank four hundred thirty-seven times.",
    "You've got twenty-four gigabytes. A million-token context just got cheap.",
    "Your GPU isn't the problem. Your notes are.",
    "DeepSeek just shrank the cost of context memory 437 times.",
    "Your chat history is about to stop filling your RAM.",
    "DeepSeek's new Flash beat its own Pro. Your card is the catch. *",
    "One token used to cost 389,120 bytes. Now 890. *",
    "Twenty-four gigabytes won't hold the weights. The notes will fit."
  ],
  "style_pack": "signal",
  "script_format": "classic",
  "structure": "number-first",
  "value_types": [
    "TEACHES",
    "EQUIPS"
  ],
  "analogy": {
    "vehicle": "a kitchen where most cooks share one clipboard of running prep notes",
    "mapping": "the clipboard is the KV cache; sharing it across layers is CSA2 cross-layer reuse; half-size shorthand is FP4",
    "limit": "FP4 really does lose precision and sharing only works because the model was trained to share"
  },
  "music_mood": "curious-tech",
  "tags": [
    "deepseek v4.1 flash",
    "deepseek",
    "kv cache",
    "local ai",
    "run local llm",
    "open weights",
    "quantization",
    "gguf",
    "mixture of experts",
    "huggingface",
    "local llm",
    "ai news",
    "free ai model",
    "llm memory",
    "mac studio llm",
    "dgx spark"
  ],
  "scenes": [
    {
      "id": "s01",
      "role": "hook",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "One token used to cost nearly three hundred ninety thousand bytes. Now it's eight hundred ninety, on DeepSeek's new Flash.",
      "on_screen_text": "389,120 bytes then. 890 now.",
      "visual_brief": "Frame 1 composition: struck-through '389,120 bytes then.' above giant amber '890 now.' on dark, both fully legible. Motion onset within 0.5 s of frame 1: the 890 block scales up once at 0.4 s. On 'DeepSeek's new Flash' a small GPU-card icon and a Mac silhouette fade in lower third.",
      "est_duration_s": 7
    },
    {
      "id": "s02",
      "role": "explain",
      "tool": "manim",
      "layout_archetype": "diagram-flow",
      "narration": "That price is the KV cache, the running notes a model keeps on your chat. A token is roughly a word.",
      "on_screen_text": "KV cache = running notes",
      "visual_brief": "Static chat transcript at left. On 'A token is roughly a word' one transcript word splits into two amber chunks that fade into place. On 'the running notes a model keeps on your chat' a notepad stack rises in place beside the transcript and grows one page.",
      "est_duration_s": 6
    },
    {
      "id": "s03",
      "role": "explain",
      "tool": "manim",
      "layout_archetype": "split-compare",
      "narration": "The twist: Flash got bigger, not smaller. Its layers share one set of notes.",
      "on_screen_text": "Bigger model. Smaller notes.",
      "visual_brief": "Split-compare, both halves pre-drawn: left, five layer boxes each holding a private notepad; right, five layer boxes wired to one shared notepad. On 'Its layers share one set of notes' the private pads fade out while the shared pad scales up with an amber glow.",
      "est_duration_s": 5
    },
    {
      "id": "s04",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "timeline",
      "narration": "Our arithmetic: a million tokens of context costs nine-tenths of a gigabyte of cache. The weights, five hundred fifty-two billion parameters, won't fit.",
      "on_screen_text": "1M tokens = 0.9 GB cache (our math)",
      "visual_brief": "On 'a million tokens of context' '1M tokens' fades in over a thin context bar that fills. On 'nine-tenths of a gigabyte' '= 0.9 GB cache' scales in beneath with an 'our math' caption. On \"won't fit\" the bar's right end stops against a dark 552B block labeled with the parameter count.",
      "est_duration_s": 8
    },
    {
      "id": "s05",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "grid",
      "narration": "Every benchmark is DeepSeek's own. And a finished local build? We couldn't find one yet.",
      "on_screen_text": "Vendor harness. No finished quant yet.",
      "visual_brief": "On 'Every benchmark is DeepSeek's own' a small vendor-harness tag fades in top corner over a faint benchmark row. On \"We couldn't find one yet\" a three-slot grid of quant listings appears, each slot flashing empty; no fill animation.",
      "est_duration_s": 5
    },
    {
      "id": "s06",
      "role": "payoff_close",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "The cache stopped being your bottleneck; the weights are it. Watch for the first DeepSeek quant that fits.",
      "on_screen_text": "Cache shrank. Weights did not.",
      "visual_brief": "Frame rhymes with frame 1: identical dark background and centered amber geometry, headline words in place of the digits. On 'the weights are it' the headline scales up once. On 'the first DeepSeek quant that fits' a small download-arrow icon fades in beneath, then the wordmark settle.",
      "est_duration_s": 6,
      "render_notes": "wordmark settle; last frame rhymes with frame 1"
    }
  ],
  "narration_full": "One token used to cost nearly three hundred ninety thousand bytes. Now it's eight hundred ninety, on DeepSeek's new Flash. That price is the KV cache, the running notes a model keeps on your chat. A token is roughly a word. The twist: Flash got bigger, not smaller. Its layers share one set of notes. Our arithmetic: a million tokens of context costs nine-tenths of a gigabyte of cache. The weights, five hundred fifty-two billion parameters, won't fit. Every benchmark is DeepSeek's own. And a finished local build? We couldn't find one yet. The cache stopped being your bottleneck; the weights are it. Watch for the first DeepSeek quant that fits.",
  "target_duration_s": 37,
  "notes_for_review": "Spoken hook rounds 389,120 to 'nearly three hundred ninety thousand' for the ear, once; exact digits on screen. 0.9 GB is our arithmetic per the brief, hedged on screen. Vendor-harness benchmarks named as such; absence-of-evidence kept as absence."
}
```

---

## Score table

| # | Row | A | B | Justification |
|---|-----|---|---|----------------|
| 1 | Hook | **3** | **2** | A names the product in the first two words and the tension is felt by "beat" (word five), resolving on "its own Pro" inside the first sentence, then personalized ("Your card is the catch") inside the first four seconds. B names numbers, but the spoken first five words ("One token used to cost") carry no tension; the shock arrives in sentence two. Frame 1 shows the contrast instantly on screen, but the row scores the spoken hook. |
| 2 | Payoff timing | **2** | **2** | A pays concretely by second ~6 ("Free weights dropped this morning"), with the 890 number landing by ~second 8. B's promised drop completes ~second 5, its meaning (the KV cache gloss) by ~second 8. Neither pays inside four seconds. |
| 3 | Specificity | **2** | **2** | Both spend numbers where they land and hedge their own math, but both load two new numbers into the s04 sentence ("a million-token context… one gigabyte"), past the one-new-number-per-sentence ceiling. No finding-17 drift: absence stays absence in both. |
| 4 | Voice | **3** | **3** | Both clean, second person, legal "we," no em dashes, caps held. Each lands one wry beat without explaining it: A's "Sous chefs, one clipboard"; B's "Flash got bigger, not smaller." |
| 5 | Navigation | **3** | **3** | No labels used, none needed. In both, every transition names what changed (cost → mechanism → consequence → credibility → gate), and the caveat scene is load-bearing for the close — "watch for the first quant" breaks without it adjacent. Neither script survives reordering intact. |
| 6 | Difference | **1** | **1** | Neither matches the last two scripts (comparison-ladder, worked-example), so not 0. But A runs 38s, duplicating the most recent video's duration, and its structure aired three days ago (09-07). B runs 37s, duplicating 09-08, and repeats 09-06's exact number-first/number-shock combo. Both close in the same viewer-imperative family as 09-06 and 09-07. |
| 7 | Repeat test | **2** | **2** | A's "Your card is the gate" and B's "the cache stopped being your bottleneck; the weights are it" are both repeatable — but in both drafts a "watch for the first quant" line follows the punchline, so the repeatable line is not the last thing heard. Tier 3 is unreachable for both. |
| 8 | Teaching | **3** | **2** | A shows two mechanisms (cross-layer sharing, half-size shorthand) and states the limit ("the model trained to share"), so the viewer can predict a case the script never mentions: an older model cannot retrofit this trick without retraining. B shows the sharing mechanism once, concretely, but omits the trained-to-share limit; the viewer leaves knowing the cache shrank, not why rivals can't simply copy it. |
| | **Total** | **19** | **17** | |

---

## Winner: Draft A (19–17)

No tie, so the row-6 tiebreak is not invoked. For the retro's benefit: had the totals tied, row 6 was level too, and the call would have turned on which collision is worse — A's duration match with the immediately previous video versus B's exact structure-and-hook repeat from 09-06.

---

## Grafts

**None performed.**

- **Hook graft:** not eligible. B's hook scored 2 against A's 3; the rule requires the loser's hook to score at least two points higher.
- **Sentence graft considered and rejected:** B's "A token is roughly a word." It fills a real gap — A uses "token" from s02 onward without a gloss. But its only natural home is inside A's giant-number scene, where it either rewrites that beat (forbidden) or trails the 890 reveal as a footnote, diluting the payoff timing the scene exists to serve. Logged instead as a voice-rules candidate: gloss "token" on first use for non-fluent viewers.
- **Second candidate rejected:** B's "The twist: Flash got bigger, not smaller." A's s04 split-compare already delivers the cache-cheap/weights-huge inversion; the line has no seam in A that doesn't require rewriting surrounding beats.

One phrasing note for the retro, not a graft: B's "Every benchmark is DeepSeek's own" is a universal claim where A scopes to "that beat-its-Pro score." Not scored as drift absent the brief text, but A's scoped phrasing is the safer pattern under finding 17.

---

## What the losing shape would have needed to win

Number-first needed its shock inside the first five words — leading with the drop itself, as its own first hook candidate did ("Eight hundred ninety bytes. That is what one token costs now."), instead of spending sentence one on setup and landing the tension in sentence two. And it needed the second mechanism, the trained-to-share limit, so the viewer leaves able to predict which models can't copy the trick rather than only knowing that Flash's cache got cheap.

---

## Retro flags

- Three of the last five ledger closes, plus both drafts here, end on a viewer imperative. The close pattern is calcifying; the repeatable payoff line keeps landing second-to-last, which caps row 7 at 2 channel-wide.
- Short durations are clustering at 37–38s (09-08, 09-09, both drafts today). Row 6 duration collisions will keep firing until the spread widens.
- Terminology glosses ("quant," "token," "parameters") are recurring borderline cases under constraint 3; the voice rules should say which community terms are exempt.