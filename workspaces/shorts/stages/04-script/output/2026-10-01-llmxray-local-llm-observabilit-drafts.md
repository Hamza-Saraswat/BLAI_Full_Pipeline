# Drafts: 2026-10-01-llmxray-local-llm-observabilit

Two blind drafts from the same brief, written by two kimi-k3 writers in private scratch dirs (`.local-builds/<slug>/draft-A|draft-B/`), judged by a third kimi-k3 call per judge-rubric.md.

## Draft A -- worked-example, hook "Gauges you've never opened" (Situation)

One scenario carried end to end: the chat prompt with the moving timestamp. Turns: blind spot (gauges exist, unopened) -> the instrument arrives (npx llmxray) -> the state changes (timestamp changes every turn) -> the collapse (four tokens reused) -> the recovery (two hundred ninety reused) -> payoff (three point five times faster, measured on your own daemon). Numbers spent: 4 tokens / 290 tokens / 3.5x, one per beat. 365 words, 9 scenes, target 114 s.

Draft A's full script is the winner and lives in `[slug]-script.md`; its storyboard JSON is `[slug]-storyboard.json`.

## Draft B -- myth-bust, hook "Your model isn't slow. Your layout is." (Wrong diagnosis)

Belief: the model is slow. Break: the same prompt ran sixty-four point six milliseconds of prefill with the timestamp at the front, eighteen point six with it at the back. What is true instead: the KV cache only holds while the prompt matches from its first token, so one changing value at the top forfeits everything below. When the myth is still right: a model too big for the hardware stays slow no matter the layout. Close: move the timestamp, run Cache Lab tonight. Numbers spent: 64.6 ms / 18.6 ms / 3.5x. 330 words, 11 scenes, target 103 s.

Storyboard JSON (post-gate-fix) preserved at `.local-builds/<slug>/draft-B/storyboard.json`.

## Judge scores (kimi-k3, rubric of 8 rows, 0-3 each)

| Row | A | B |
|-----|---|---|
| Hook | 3 | 3 |
| Payoff timing | 2 | 3 |
| Specificity | 2 | 2 |
| Voice | 3 | 2 |
| Navigation | 2 | 2 |
| Difference | 2 | 2 |
| Repeat test | 2 | 2 |
| Teaching | 2 | 1 |
| **Total** | **18** | **17** |

Winner: **A**, margin 1.

Grafts considered, none applied:
- B's hook "Your Ollama model isn't slow. Your prompt layout is." -- rejected: needed a two-point row-1 win over A's hook; the judge scored the hooks level (both name the tension), so the graft condition was not met.
- B's myth-still-right sentence ("a model too big for your hardware stays slow no matter how you arrange the prompt") -- rejected: inserting it into A's worked-example would open a second claim structure in the payoff scene and need surrounding rewrites; the rubric forbids grafts that require rewriting beats.

What the losing shape would have needed: the myth-bust needed its honest-catch beat to land earlier than the winner's close (its "when the myth is still right" line arrived after the payoff rather than before it), and its break scene to show both prefill numbers side by side on screen instead of sequencing them across two scenes. With those two moves it wins on payoff timing and teaching.

## Gate history

- Round 1: draft B failed `number_spend` (heard=4): "three hundred twenty-four tokens" in setup substring-matched the brief's "4 tokens" row. Fixed inside B by dropping the 324 figure from the setup scene (it was scenario framing, not a budget number); B then passed all gates.
- Draft A passed all gates on first write; post-judge cleanup removed one filler word ("actually") and normalized the sfx field from object to list form (validator double-counted the dict form as 8 cues; actual cues 4).
- Final winner eval: gate1_ready=true, failures=[]; validator 0 blockers, 4 advisories (kept with reasons in the script note Decisions).
