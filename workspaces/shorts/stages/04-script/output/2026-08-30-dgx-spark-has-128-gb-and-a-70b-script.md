---
slug: 2026-08-30-dgx-spark-has-128-gb-and-a-70b
format: smooth-explainer
structure: myth-bust
style_pack: blueprint
value_types: TEACHES, REFRAMES
promise: after this video the viewer can predict whether any model will chat fast on a DGX Spark before downloading it
target_duration_s: 110
brief: 2026-08-30-dgx-spark-has-128-gb-and-a-70b-brief.md
drafts: 2026-08-30-dgx-spark-has-128-gb-and-a-70b-drafts.md
---

# DGX Spark speed math: bandwidth beats gigabytes (working title)

## Decisions

- Structures tried: worked-example (draft A) vs myth-bust (draft B). Judge picked B, 22-20: B's tension lands inside the first five words (row 1), its break pays the 803 / 2.7 evidence immediately (row 2, fairness note applied), and its belief-to-payoff chain cannot be reordered (row 5). A took only row 7 (the more repeatable payoff line).
- Hook: candidate 2 ("Your Spark isn't slow. Its doorway is narrow.", wrong-diagnosis pattern). The situation hook went to draft A; two different patterns by design (finding 12). hook_pattern is set explicitly on the storyboard for both drafts because the number-first classifier rule mislabels any hook containing a number; the assigned patterns are the true labels.
- Graft: one, per the rubric's sentence rule. From A scene 7 into B scene 7: "You give up a little accuracy, and casual chat never notices." B's quantize beat stated the benefit with no cost. No hook graft (A's hook scored lower), no second graft (A's 41.14 line would break B's three-number budget).
- sameness gate: first run flagged draft A's hook as number-shock (the classifier fires on any number word); fixed by setting the explicit hook_pattern field documented in rules/variety.md, then both drafts passed. Yesterday's closing move ("before you download ...") echoes in both closes; the judge capped row 6 at 2 for each and still picked B. Recorded here because two closes in a row on the same gambit is the retro's signal, not a gate failure today.
- Payoff timing: the hook scene's first sentence (the diagnosis) ends at ~second 4 on the measured 3.35 wps clock and the measured number (two point seven) is spoken immediately after inside the same scene; the judge scored payoff timing 3/3 under the myth-bust fairness note.
- Ending: the payoff line is the last spoken sentence; zero tail sentences on the validator's anchor.
- Advisor notes kept: the validator's long-scene advisories use the provisional 2.9 wps clock while voicing will be chatterbox at 3.35 measured; scenes are all under 20 s on the measured clock. entity_spend and top2 advisories are soft gates; the script spends named products (Spark, NVIDIA, Ollama, GPT-OSS) instead of repeating the DGX Spark full name.

## Hook candidates

1. You load the biggest model that fits. It answers like a fax machine.
2. Your Spark isn't slow. Its doorway is narrow.
3. This 120B model outruns a 70B on the same desk.
4. Eight hundred three tokens in. Two point seven out.
5. You unbox the Spark, feed it a 70B, and wait. And wait.
6. The model isn't dumb. The road it walks is narrow.
7. Seventy or one-twenty billion? One division decides.
8. LMSYS benchmarked a 70B on the Spark. The decode crawled.
9. The model that fits is not the model that talks.
10. You bought 128 gigabytes. Your chatbot still types two words a second.

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | Your Spark isn't slow, its doorway is narrow. L M S Y S measured two point seven tokens a second from a seventy-billion-parameter model on one. | Your Spark isn't slow. Its doorway is narrow. | 2.7 tok/s, LMSYS | Frame 1: the hook line sits over a DGX Spark on a desk, fully legible; on "Your Spark isn't slow" the line holds; on "two point seven tokens a second" a chat bubble stalls mid-word and 2.7 tok/s snaps in beneath the hook line within half a second. | hyperframes | giant-number | 6.6 |
| s2 | explain | You ordered the Spark for a hundred twenty-eight gigabytes of unified memory, or the order page is still open. The plan writes itself: load the biggest model that fits, expect chat speed. Everyone's math says fitting is the whole game. | 128 GB unified memory | fits = fast? | On "a hundred twenty-eight gigabytes" the spec sheet line 128 GB highlights; on "load the biggest model that fits" a giant model box drops cleanly into the memory pool; on "the whole game" a checkmark appears beside "fits = fast?" and wobbles. | hyperframes | centered-stack | 11.9 |
| s3 | explain | Same box, same model, two speeds. It reads your prompt at eight hundred three tokens a second. It writes the answer at two point seven, slower than your group chat types. | reads: 803 tok/s | writes: 2.7 tok/s | On "reads your prompt" the prompt whooshes in as one fast bar labeled 803 tok/s; on "writes the answer" the reply types out letter by letter under 2.7 tok/s, stalling between words. | hyperframes | split-compare | 9.3 |
| s4 | explain | Why the gap. Reading is one wide pass of math, and the Spark's compute eats it. Writing is one token at a time, and each token re-reads the model's weights from memory. The compute barely works during decode. The memory does the hauling. | every token re-reads the weights | On "one wide pass" the whole prompt lights up as a single block flowing into the chip; on "each token re-reads" a loop arrow cycles from memory to chip once per written word, the weight stack pulsing each cycle; on "the memory does the hauling" the arrow thickens while the compute block idles. | manim | diagram-flow | 12.8 |
| s5 | explain | Picture a kitchen where the chef chops instantly and every ingredient fits through one narrow door. The chef is the compute. The door is the memory bus: two hundred seventy-three gigabytes a second. For reading your prompt, one wide delivery, the picture breaks. | doorway = 273 GB/s | On "chef chops instantly" the knife blurs through a pile; on "one narrow door" ingredients queue single file through a small door labeled 273 GB/s on "two hundred seventy-three"; on "the picture breaks" one wide prompt crate skips the door entirely. | hyperframes | centered-stack | 12.8 |
| s6 | explain | So the speed ceiling is one division. Bandwidth divided by the gigabytes each token re-reads. A dense seventy-billion model in eight-bit re-reads about seventy gigabytes per token. The ceiling sits under four tokens a second. Two point seven is that ceiling with overhead. | ~70 GB/token, ceiling < 4 tok/s | 2.7 = ceiling + overhead | On "one division" a fraction assembles; on "about seventy gigabytes" the divisor fills with ~70 GB/token; on "under four tokens a second" the result line draws at < 4 tok/s; on "Two point seven" a measured bar lands just beneath that line. | manim | giant-number | 12.8 |
| s7 | explain | What a token re-reads is the active weights, the slice the model actually uses. Quantize to four-bit and each token carries half the bytes. You give up a little accuracy, and casual chat never notices. Or a mixture of experts, a model that wakes only a few specialists per word. G P T O S S one twenty B is bigger on paper and chats comfortably. | 4-bit: half the bytes | GPT-OSS-120B: bigger, chats | On "carries half the bytes" the parcel moving through the door shrinks to half size; on "wakes only a few specialists" a grid of expert cells stays dark while three light up per word; on "GPT-OSS one twenty B" its chat bubble types out smoothly. | hyperframes | grid | 19.7 |
| s8 | explain | The spec sheet did not lie. It printed the doorway's width in smaller type. A model that does not fit does not run. And those hundred twenty-eight gigabytes are why a two-hundred-billion-parameter model loads on a desk at all. Capacity picks what loads. Bandwidth picks how it talks. | 128 GB decides what loads | 200B-class, on a desk | On "does not fit" an oversized model box bounces off the Spark outline; on "loads on a desk" the 200B-class box settles inside the 128 GB pool; on "Bandwidth picks" a speed gauge hand rises beside the memory pool. | hyperframes | split-compare | 14.3 |
| s9 | payoff_close | Before you download a model for this box, find the gigabytes it re-reads per token. Divide two hundred seventy-three by it. That one number tells you the chat speed before the download starts. | GB re-read per token | 273 | that = your tok/s | On "find the gigabytes" the active-bytes line on a model card highlights; on "Divide two hundred seventy-three" the mini formula fills with 273 over that number; on "chat speed" the result lands in the green; the doorway line from frame 1 settles back with the wordmark. | hyperframes | centered-stack | 9.9 |

## Notes for review

- The 3.9 tok/s ceiling and the 4.423 tok/s Q4 measurement are deliberately paraphrased ("under four tokens a second", "half the bytes") to hold the smooth-explainer three-number cap; the spoken numbers are 128 GB, 803 / 2.7, and 273.
- "two-hundred-billion-parameter model" in scene 8 is NVIDIA's advertising line (brief claim 3), not a measurement; NVIDIA's name was dropped from the line at drafting, noted by the judge.
- The analogy's limit is stated in scene 5 ("For reading your prompt, one wide delivery, the picture breaks").
- hook_text was trimmed to six words for the schema; the hook's first narration sentence was merged to one clause to clear the 5-14 word rule.
