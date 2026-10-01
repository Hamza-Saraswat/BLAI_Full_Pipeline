---
slug: 2026-10-01-llmxray-local-llm-observabilit
format: smooth-explainer
structure: worked-example
style_pack: signal
value_types: EQUIPS,TEACHES
promise: After this video you can point npx llmxray at your own Ollama daemon and measure what your prompt layout costs every turn.
target_duration_s: 114
brief: 2026-10-01-llmxray-local-llm-observabilit-brief.md
drafts: 2026-10-01-llmxray-local-llm-observabilit-drafts.md
---

# Local LLM observability: the gauges you've never opened

## Decisions
- Structures tried: worked-example (A) and myth-bust (B); both cleared the rotation rule (last two were number-first and comparison-ladder). A won 18-17 on the judge rubric; no grafts applied (B's hook needed a 2-point row-1 win, scored level; the myth-still-right sentence would have needed restructuring).
- Hook: candidate 9 of 10, "Ollama already publishes gauges on localhost. You've never opened them." (Situation pattern; number-shock and decision banned by the last-two ledger entries). Frame-1 text "Gauges you've never opened".
- Number budget: 4 tokens / 290 tokens / 3.5x, one per beat, all hedged per the brief (3.5x spoken as the maintainer's illustration, not a benchmark). B spent 64.6 ms / 18.6 ms / 3.5x.
- Fix round 1 inside draft B: "three hundred twenty-four tokens" substring-matched the "4 tokens" key number row and failed number_spend (heard=4); removed the 324 setup figure from B's s7. Winner A untouched by this.
- Post-judge cleanup in A: filler "actually" removed (s4); sfx normalized from object to list form (same 4 cues; the dict form double-counted to 8).
- Validator on winner: 0 blockers, 4 advisories kept with reasons: hashtag/tag counts are stage-05 fields the package stage overwrites; s3/s7 long-scene advisories (14.4 s / 14.1 s est, ~47-48 narration words) are the writer's compound explain beats, each with a visual brief promising change every ~3 s; splitting them would push the scene count to 11 of 12 for no pacing gain.
- Hook motion onset: gauge outline scales and needle ticks at 0.35 s, named in s1's visual brief.

## Hook candidates
1. "You run Ollama every day. You've never seen one number about it."
2. "Your Ollama model isn't slow. Your prompt layout is."
3. "Three and a half times faster. Same words, one timestamp moved."
4. "One command turns your local model's hidden numbers into gauges."
5. "Free, no cloud, no keys: an instrument panel for your local model."
6. "That timestamp at the top of your prompt is costing you every turn."
7. "Four tokens reused, or two hundred ninety. Same prompt."
8. "Your chat window throws away the most interesting number in the room."
9. "Ollama already publishes gauges on localhost. You've never opened them." *
10. "Watch your model think, token by token, tonight."

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | Ollama already publishes gauges on localhost. You've never opened them. You chat with your local model and see only finished words. | Gauges you've never opened | Frame 1: dark charcoal background, hook text centered in large amber type, fully legible immediately; a faint circular gauge outline sits behind the text at low opacity. At 0.35 s the gauge outline scales up slightly and its needle ticks once. On "You chat with your local model" a plain chat bubble fades in below the text; on "finished words" two grey text lines rise-in-place inside the bubble while the gauge stays dark. At most two elements animating at once. | hyperframes | centered-stack | 7.2 |
| s2 | explain | Underneath, your model writes one token at a time. A token is a small chunk of text it reads and writes piece by piece. How fast each chunk arrives is information. A plain chat window throws all of it away. | one token at a time \| arrival speed is information | Manim: a sentence breaks into token chips (word fragments) that stack; each chip lights amber as "written"; a speed readout blinks per chip on "how fast each chunk arrives"; on "throws all of it away" the readouts fade to grey and the chat window shrinks them into two finished lines. | manim | diagram-flow | 12.5 |
| s3 | explain | Now those gauges get a face. A free tool called llmxray, just posted to Hacker News, works like a dashboard for that engine. It needs Ollama running, plus Node.js eighteen or newer. One command, npx llmxray, then a page at localhost, port fifty-one seventy-four. | npx llmxray \| localhost:5174 \| needs Node.js 18+ | Terminal window: the command `npx llmxray` types on screen; a browser frame rises beside it and fills with a dark dashboard: gauges, a token stream, badge icons. Requirement chips ("Ollama", "Node.js 18+") pop in as spoken; the URL bar types localhost:5174 on "port fifty-one seventy-four". Typewriter text, hard cuts. | hyperframes | split-compare | 13.8 |
| s4 | explain | Each token arrives colored by how fast it showed up. That color is a timing approximation, not real probability, and the app says so. A dashboard only displays what sensors report. Badges appear only when something is wrong: repetition, refusal, gibberish, a truncated reply. | colored by arrival speed \| labeled approximation \| badges when wrong | Grid of token cells filling left to right, each tinted along an amber-to-red scale by arrival speed; a small "approximation" tag sits pinned under the color legend; on "badges appear" four badge icons (loop, block, scramble, scissors) hard-cut in, one per named failure. | hyperframes | grid | 13.4 |
| s5 | foreshadow | Now for the cost you never saw. Your chat app resends the same prompt every turn. The maintainer's test prompt was three hundred twenty-four tokens, with a live timestamp near the top. That timestamp changes every turn. That small change is expensive. | same prompt every turn \| 324 tokens \| timestamp changes every turn | Timeline strip: the same prompt block repeats as tiles left to right, one tile per turn; the top line of each tile is a timestamp that re-draws a new value on every tile while the body below stays identical; on "expensive" the timestamp line pulses amber and a cost ticker under the strip starts climbing. | hyperframes | timeline | 13.4 |
| s6 | explain | Now the state flips. The model keeps a saved memory of having read your prompt, the KV cache. It can reuse that memory only while the prompt still matches. Cache Lab, the tool's measurement mode, counted what survived the moving timestamp: four tokens reused. | KV cache: saved prompt memory \| 4 tokens reused | Giant number builds: "4" scales up center-frame over a cache block whose tiles flip from amber (reused) to grey (discarded); only four tiles stay lit at the top of the stack; the Cache Lab panel label draws under the number. | hyperframes | giant-number | 13.8 |
| s7 | explain | Why so brutal? The cache holds only while the prompt matches from its very first token. One changed value near the top makes a stranger of everything below it. So each turn, the model re-reads nearly the whole prompt before writing. That reading work is called prefill. | match must start at the top \| below the change: re-read \| that re-reading is prefill | Manim: the prompt block from s5 returns; the changed timestamp tile at top tints red and a match-line draws from the first tile, stops dead at the red tile, everything below flips grey; a bracket labels the grey span "re-read"; the label "prefill" writes in under the bracket. | manim | diagram-flow | 14.4 |
| s8 | explain | Now move the timestamp to the back of the same prompt. The words are identical, the order barely changed. But the top of the prompt finally matches turn after turn, so the cache holds. Cache Lab counted two hundred ninety tokens reused. | timestamp moves to the back \| 290 tokens reused | Mirror of s6: the timestamp tile slides to the bottom of the block (fade-out top, fade-in bottom), the match-line now runs the full height, tiles flip grey-to-amber top down, and "290" scales up center-frame over the fully lit cache. | hyperframes | giant-number | 13.1 |
| s9 | payoff_close | The same words ran three point five times faster, just by moving one timestamp. That's the maintainer's own illustration on one prompt, not a benchmark. But Cache Lab runs against your own daemon, so you can measure your own prompts tonight. | 3.5x faster, same words \| illustration, not benchmark \| measured on your own daemon | Split: left, "3.5x" in giant amber type over the two Cache Lab readings; right, the terminal from s3 still open, a new Cache Lab row drawing in with the viewer's own numbers; the frame settles on the number as the wordmark lands, last frame rhyming with s1's gauge. | hyperframes | centered-stack | 12.8 |

## Notes for review
- The voice read of "port fifty-one seventy-four" must agree with the on-screen localhost:5174 (s3); check the rendered captions.
- "Node.js eighteen or newer" is spoken next to the three key numbers (s3); it is a prerequisite fact, not a metric, but a strict listener may hear four numbers in the script. The three budget numbers stay 4 / 290 / 3.5x.
- The 3.5x claim is hedged twice (s9): "maintainer's own illustration" and "not a benchmark", per the brief's note.
- "just posted to Hacker News" (s3) is the why-now, deliberately not "released yesterday"; the project dates to March per the changelog.
