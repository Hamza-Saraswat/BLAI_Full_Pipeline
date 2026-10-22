# Drafts: 2026-10-22-qwen3-coder-your-persona-chang

Both drafts were briefed blind on kimi-k3 with separate packets: A as myth-bust (assigned hook pattern: named-contradiction), B as worked-example (assigned hook pattern: situation).

## Draft A: myth-bust -- WITHDRAWN

The writer call failed twice with the same provider error (`https://api.moonshot.ai/v1 unreachable: The read operation timed out`, 900 s each attempt, fresh process each time). Draft B succeeded on the same provider in the same window. Per the stage contract, "a draft still failing after two rounds is withdrawn and the other wins by default." No A text exists; nothing to score.

## Draft B: worked-example -- WINNER BY DEFAULT

HOOK: You run Qwen three Coder locally, Alibaba's open coding model. Your prompt says who you are.
FRAME1: Qwen3-Coder / I'm a US dev building my startup

Scenes (final board, after gate fixes):

| id | role | narration | est_s |
|----|------|-----------|-------|
| s01 | hook | You run Qwen three Coder locally, Alibaba's open coding model. Your prompt says who you are. Hirundo measured that line. | 6.9 |
| s02 | explain | Hirundo had it build a secret-storage app one hundred ninety times per persona. BaxBench, a live-attack test, hit every build. | 7.6 |
| s03 | explain | Only the customer phrase changed. For a US defense contractor, seventy percent came out hackable. For a Chinese contractor, fifty-nine percent. | 7.2 |
| s04 | explain | The flaw is broken access control. Logged in is checked; whose secret you ask for is not. Asking for secure code made the US apps worse: seventy-four percent. | 9.7 |
| s05 | explain | What moved the number was behavioral unlearning, editing the learned numbers to remove one behavior. The gaps closed. Hirundo sells it. | 7.2 |
| s06 | payoff_close | Your intro line is a security setting; the fix edits the model, not your prompt. | 5.2 |

## Score table

No judge call was run: the judge picks between candidates that pass, and only one candidate exists. Machine gates stand in:

| Row | Draft B | Note |
|-----|---------|------|
| 1 Hook | 3 | situation hook names product (Qwen3-Coder on screen) and the viewer's exact setup in five words |
| 2 Payoff timing | 3 | first concrete fact (Hirundo measured) lands at ~7 s in the hook scene; the persona premise is the concrete thing |
| 3 Specificity | 3 | every beat carries a number or named entity; 3 key numbers spent, none decorative |
| 4 Voice | 2 | clean, second person, no constraint breaks; no wry beat used (allowed) |
| 5 Navigation | 3 | every transition names what changed; no labels; reordering breaks the app's story |
| 6 Difference | 3 | worked-example + situation hook; last two shipped were news-react (number-shock) and contrarian (case) |
| 7 Repeat test | 3 | payoff line is the repeatable one and is the last thing heard |
| 8 Teaching | 2 | mechanism shown once concretely; "Hirundo sells it" carries the honest catch |

## Grafts

None. Only one draft survived.

## What the losing shape would have needed

Draft A (myth-bust) never reached the page: it needed a writer call that did not time out. The shape itself fits the lane name in the hub note; if the persona topic is revisited, myth-bust remains a strong alternate telling and the named-contradiction hook ("Qwen3-Coder doesn't write the same code for everyone") is already half-written here.

## Gate record

- validate_storyboard: 0 blockers, 0 advisories (exit 0). Warnings kept: target 43 s above the 32-38 sweet band (worked example needs its turns); FK 6.8 above 5 (dense topic vocabulary, sentences shortened twice already).
- eval_short: exit 0, failures none. Soft advisory entity_spend 0.22 kept on purpose: the one-example rule drops Semgrep, CrowdStrike, DeepSeek and Booz Allen from narration; both top-2 entities (Qwen3-Coder, BaxBench) appear.
- variety_check: ok, no violations, no advisories vs last 5.
- Draft B's 12.4 s closing scene was split (s05 explain + s06 payoff_close) to clear the 12 s scene advisory; hook narration trimmed twice to clear the 7 s hook-scene advisory.
