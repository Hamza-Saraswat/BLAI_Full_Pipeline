# Drafts: 2026-10-19-deepseek-v4-1-flash-1017-max-t

Two blind drafts on kimi-k3 (writer packets in `.local-builds/<slug>/draft-A|draft-B/`; judge packet in `judge/`). Both cleared every gate before judging: zero validator blockers, eval exit 0, variety check clean.

## Draft A -- number-first (lost, 16/24)

Working title: DeepSeek Flash 1017 costs 26 cents a task, and 128 GB to run it

| id | role | narration |
|----|------|-----------|
| s1 | hook | DeepSeek's Flash costs twenty-six cents a benchmark task. One task on the Artificial Analysis index, an independent scoreboard. |
| s2 | explain | The size will surprise you: five hundred fifty-two billion parameters. It's a mixture of experts, a receptionist waking the few each word needs. Sixteen billion wake per word. She re-picks for every word. |
| s3 | explain | The weights are MIT licensed, downloadable today. A community converter reports a build fitting one DGX Spark with one hundred twenty-eight gigabytes of shared memory. |
| s4 | foreshadow | Flash is a name, not a size. Your twenty-four-gigabyte card stays out, at any quant, any shrunken file. |
| s5 | payoff_close | What's yours is the number: twenty-six cents a task, no new box. |

## Draft B -- myth-bust (WON, 21/24)

Working title: DeepSeek Flash 1017: open weights your card can't run

| id | role | narration |
|----|------|-----------|
| s1 | hook | Your card still can't run DeepSeek's new open weights. Seven hundred sixty-three billion parameters on the spec sheet. |
| s2 | foreshadow | The old rule: DeepSeek's open weights shrink onto a gaming card. Not this time, at any compression. |
| s3 | explain | A community builder reports a repackaged copy loading on a single DGX Spark. That box shares its memory between processor and graphics: one hundred twenty-eight gigabytes of unified memory. |
| s4 | explain | Another community build reports a heavier recipe: a pair of ninety-six-gigabyte cards plus host memory. Flash is doing work in that name. |
| s5 | foreshadow | The rule survives one size up: a Spark with unified memory loads it at your desk. |
| s6 | payoff_close | Your card's way in: the API, renting DeepSeek's machines at twenty-six cents a task. |

## Score table (judge, kimi-k3, 2026-10-19)

| # | Row | A | B | Reason |
|---|-----|---|---|--------|
| 1 | Hook | 2 | 3 | A names product + number but no felt tension in five words; B's "Your card still can't run" lands exclusion in five words, then 763B. |
| 2 | Payoff timing | 3 | 2 | A pays the 26-cent promise inside the hook (~s3); B's break lands ~s10, the first route follows fast, but the hook's "your card" question only resolves in s6. |
| 3 | Specificity | 1 | 3 | A drifted: "at any quant, any shrunken file" asserts what the brief lists unverified, and it speaks 552B as the size against the card's 763B. B's 763B / 128 GB unified / 2x96 GB all match, community claims hedged with "reports". |
| 4 | Voice | 3 | 3 | Both clean second person, one unexplained wry beat each on the same word ("Flash is a name, not a size" / "Flash is doing work in that name"). |
| 5 | Navigation | 2 | 3 | A's middle scenes could swap without breaking; B's rule, break, two routes, synthesis, redirect order is load-bearing. |
| 6 | Difference | 0 | 2 | A repeats the 10-17 script's number-shock hook at the same 36 s; B's myth-bust shape and bad-news rhythm differ from both recent scripts. |
| 7 | Repeat test | 3 | 2 | A's closer is the repeatable line and last heard; B's repeatable lines are the hook and the Flash joke, not its telegraphic closer. |
| 8 | Teaching | 2 | 3 | A shows MoE routing but never ties 16B-active back to the 26-cent price; B's unified-memory mechanism lets a viewer predict cases the script never mentions. |
| | Total | 16 | 21 | |

## Grafts

None. A's hook scored lower than B's, so it is ineligible; A's receptionist sentence has no counterpart in B and would break B's time budget and hardware flow; A's closer would displace the line that resolves B's hook.

## What the loser would have needed

Number-first needed an opening the 10-17 number-shock script had not just shipped: leading with the same hook pattern at the same 36 s zeroed row 6 before the script started. It also needed to cash its own mechanism (sixteen-billion-active never connects to the twenty-six-cent price) and to hedge the 24 GB exclusion the brief lists as unverified instead of asserting it at any quant.
