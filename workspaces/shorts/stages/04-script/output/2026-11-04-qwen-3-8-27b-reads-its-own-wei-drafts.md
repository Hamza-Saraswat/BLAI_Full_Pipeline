# Drafts: 2026-11-04-qwen-3-8-27b-reads-its-own-wei

Both drafts written blind on kimi-k3 (separate llm_call.py processes, private scratch dirs), gated, then judged blind on kimi-k3 per judge-rubric.md.

## Draft A (worked-example) -- final gated form

Hook: "Qwen just read a stranger's mind." (other-pattern after sameness forced the number-shock form out)

- s01 (hook): Qwen, the model on your laptop, can read another network's mind. A pasted network, and it names the game.
- s02 (foreshadow): Those weights are a toy network: seventeen thousand two hundred fifty-three parameters, pasted as text. Simon's run went three of four games right.
- s03 (foreshadow): One number alone says nothing. Together they are clues: rows become cells, cells become a grid.
- s04 (foreshadow): Asked what it does, the model answers: Pac-Man. That is a big model reading a small network's weights. It never read its own.
- s05 (payoff_close): The repo has the prompts waiting. Tonight your machine reads a mind, seventeen gigabytes of download, and knows its limits.

101 words, 34.8s target, 5 scenes. Gates: all pass (entity_spend advisory).

## Draft B (myth-bust) -- WINNER

Hook: "Your feed said Qwen read its own weights."

- s01 (hook): Your feed said Qwen read its own weights. It named a game from seventeen thousand numbers.
- s02 (foreshadow): Those seventeen thousand two hundred fifty-three parameters are a toy network, built for the test. Not the model's own twenty-seven billion parameters.
- s03 (explain): Given that toy's raw weights, it named three of four games right. The full run took forty-six minutes and twelve seconds. It guessed Pac-Man on the obscure one, and the trace is almost incomprehensible.
- s04 (explain): Weight reading is real: it answered questions about numbers handed to it, the toy's raw weights. It never once looked inward.
- s05 (payoff_close): The prompts are waiting in RikiyaT's repo. Your laptop can read real weights tonight.

107 words, 36.8s target, 5 scenes. Gates: all pass (entity_spend advisory).

## Judge score table (kimi-k3, blind)

| Row | A | B | One-line reason |
|-----|---|---|-----|
| 1 Hook | 2 | 3 | A names Qwen but the tension lands after the setup clause; B carries product + felt tension inside five words. |
| 2 Payoff timing | 2 | 2 | A's first hard concrete lands ~6-7s; B's break lands ~7s, scored from the break per the myth-bust fairness note. |
| 3 Specificity | 3 | 3 | One number per sentence, none decorative, no drift from the brief. |
| 4 Voice | 3 | 3 | Clean person, no hard breaks; one dry beat each, unexplained. |
| 5 Navigation | 3 | 3 | No positional filler; scene order load-bearing in both. |
| 6 Difference | 1 | 2 | A repeats the "tonight, do this" closing move (2026-10-30) and a used duration; B's shape and opening differ from the last two scripts. |
| 7 Repeat test | 3 | 2 | A's quotable payoff is the last thing heard; B's quotable line is penultimate (fixed post-judge: payoff line moved last). |
| 8 Teaching | 3 | 3 | A shows the encoding mechanism concretely; B shows the boundary; each lets a viewer predict an unmentioned case. |
| Total | 20 | 21 | B edges it on hook strength and structural freshness. |

WINNER: B

GRAFTS: none. A's hook scores lower, so no hook graft; A's superior close would have to replace B's structural payoff, which is out of bounds.

LOSER-WOULD-HAVE-NEEDED: The worked-example needed a hook that fronts the tension inside the first five words (its own candidate list held one) instead of spending the opening clause on product setup, and a landing and duration that do not repeat the recent run, since the "tonight on your machine" close and the ~35/38s band both echo the last five entries and capped its difference score at 1.

Post-judge fix (orchestrator, inside winner only): B's s05 ended repo-pointer-last; swapped the two sentences so the payoff line is the final spoken sentence (ending audit). Gates re-run after the swap: validator 0 blockers, eval exit 0, variety ok.

Gate log (both drafts, after fixes): validate_storyboard 0 blockers each; eval_short A exit 4 -> 0 (number_spend 1->3, hook_concrete via entity:Qwen, scene_specificity 4/5 -> 5/5; sameness cleared by reclassifying the hook out of number-shock), eval_short B exit 4 -> 0 (sameness: hook reworded to situation-classified "Your feed said Qwen read its own weights", concreteness kept via entity:Qwen). Soft advisory kept with reason: entity_spend below 0.5 because the brief's entity set is dominated by runtime/hardware names a 107-word myth-bust cannot name without breaking number pacing; Qwen (top-2 entity) is present.
