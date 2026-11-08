# Drafts: 2026-11-08-aivim-a-vim-ai-editor-running

Two blind drafts (separate kimi-k3 calls, private scratch dirs), judge verdict from a third.
Writer packets: `.local-builds/2026-11-08-aivim-a-vim-ai-editor-running/draft-A|draft-B|judge/`.

## Draft A (worked-example) -- WINNER, 21 points

Title: AIVim: Plug Your Editor Into Ollama. Hook (Situation): "Your Ollama models are already running. This editor finally uses them."
Six scenes: hook -> install (pipx, Python 3.9+) -> connect (localhost 11434) -> live block (list the biggest logs here -> ls -S *.log) -> budgets and review (50 KiB, checked not run) -> payoff (subset and days old, but everything stays on your machine). 113 words, 39 s target, 6 scenes.

## Draft B (news-react-so-what) -- 18 points

Title: AIVim: Your Ollama Becomes the Editor. Hook (Named contradiction): "AIVim just shipped: a Vim-style editor running your Ollama model."
Five scenes: shipped yesterday on Hacker News -> consequence (Ollama becomes the brain of a real editor, not a chat tab) -> wiring (Python 3.9+, the plug, port 11434) -> catch (Vim subset, days old, unproven) -> tonight (pipx install, one live block). 110 words, 38 s target, 5 scenes.

## Scores

| Row | A | B |
|-----|---|---|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 2 | 2 |
| 3 Specificity | 3 | 2 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 3 | 2 |
| 6 Difference | 1 | 3 |
| 7 Repeat test | 3 | 2 |
| 8 Teaching | 3 | 2 |
| Total | 21 | 18 |

Judge notes: A's row 6 scored 1 because the worked-example closing rhymes with the recent run's durations (39 s matches 11-07) and it reuses a "tonight" move mid-script; it still wins on rows 1, 3, 5, 7 and 8. B's news shape restated its own hook at beat two and spent no number at the close.

## Grafts

None. B's hook was not two points better on row 1; its two candidate lines ("not a chat tab", "One person's project, unproven") would break A's word budget and force a close rewrite.

## What B would have needed

The news-react shape needed beat two to advance the story instead of restating the hook, and one concrete worked request to make the so-what felt rather than asserted. It also needed its repeatable line at the close instead of at second ten.

## Gate log (final board)

- validate_storyboard: 0 blockers, 0 advisories (warnings: FK 6.1 target 5, four consecutive >6-word sentences, 39 s just above the 32-38 evidence band).
- eval_short: all gates pass; advisory entity_spend 0.188 (soft). number_spend 2 spent of 6 (3.9+, 50 KiB), hook_concrete via Ollama, specificity 6/6, skeleton 0.0, labels 0, sameness ok with 5 comparisons.
- variety_check: ok, 5 comparisons, 0 violations. Ledger now 64 entries.
- Gate fixes applied to B's raw draft before judging: hedged adoption numbers out of narration (Unverified), added Python 3.9+ for number_spend, split a 25-word sentence, replaced the 16-word hook.
