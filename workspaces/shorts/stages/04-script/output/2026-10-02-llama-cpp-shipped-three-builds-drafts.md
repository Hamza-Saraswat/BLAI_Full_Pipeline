# Drafts: 2026-10-02-llama-cpp-shipped-three-builds

Both drafts written blind on kimi-k3 (separate processes, no shared context), passed validate_storyboard (0 blockers) and eval_short (all hard gates) before judging. Judge was a third blind kimi-k3 call with the rubric as system file and both boards plus voice rules and the last five ledger entries as user file.

## Draft A (news-react-so-what, hook pattern Tonight) -- WINNER 21/24

Narration: Rebuild tonight: ten tagged builds this morning. You built llama.cpp from source once and never updated. A release bot tagged ten builds before breakfast. Three landed within four hours and twenty-five minutes. Those b numbers are documented nightlies, automated development builds. The seven forty-two bus you board again tomorrow. Two builds can differ, not just schedules. Your old binary rejects new GGUF files, single-file model containers. The file is fine. The binary predates the architecture. The catch: a pinned commit pins code, not compiler or GPU flags. Builds target the hardware they see. Tonight, read the build line, fetch the tags, check out one exact nightly, rebuild. The GGUF that failed loads, and your setup is only as reproducible as the tag you write down.

Six scenes: hook (centered-stack), burst timeline (timeline), nightly-vs-bus (split-compare), GGUF rejection (diagram-flow), pin-the-code catch (centered-stack), re-pin close (grid). Target 42 s, 125 words, zero positional labels, bus analogy with its limit spoken in the same beat.

## Draft B (how-to-three-moves, hook pattern Wrong diagnosis) -- 20/24

Narration: Your GGUF isn't broken, your llama.cpp is ten tagged builds behind. Three landed fast. Four hours, twenty-five minutes, one morning. Each tag is a single fix, published by a bot. Step one: read the build line at startup. A stale binary usually answers. Maintainers dated one to January. Step two: fetch the tags and check one out. Now you hold a pinned commit, one exact build. Step three: rebuild and run it. The compiler targets the hardware it sees, CUDA cards, Metal Macs. The GGUF that failed loads. Same machine, same flags, same answer.

Six scenes, three legal action labels, target 33 s, 94 words. Validator and eval both green when withdrawn from contention.

## Judge's score table

| row | draft A | draft B |
|---|---|---|
| Hook | 2 | 2 |
| Payoff timing | 3 | 3 |
| Specificity without cramming | 2 | 2 |
| Voice | 3 | 2 |
| Navigation | 3 | 3 |
| Difference | 3 | 3 |
| The repeat test | 2 | 3 |
| Teaching | 3 | 2 |
| TOTAL | 21 | 20 |

## Grafts applied (from B into A)

1. "fetch the tags" folded into A's close ("read the build line, fetch the tags, check out one exact nightly, rebuild"): on a stale clone the checkout fails without the fetch; sixteen words, under the sentence cap.
2. "The GGUF that failed loads" placed before A's closing aphorism so the cure is demonstrated, not asserted; the reproducibility line stays the last spoken sentence (Hard Constraint 7 intact) and the abrupt-ending budget holds with the pair folded into one sentence.

## What the losing shape needed

Per the judge: B needed GGUF defined in the same breath both times the term carries the script, and it needed the diagnosis demonstrated rather than asserted, the way A's "the binary predates the architecture" explains the rejection the viewer actually hit. Its "ten tagged builds behind" also clashed with the January build its own third scene cites, and "each tag is a single fix" was drift the brief does not source for all ten.

## Gate record

- Draft A final: validator exit 0, zero advisories; eval exit 0 (number_spend 2, hook_concrete via number:10, scene_specificity 5/6 needed 5, skeleton 0.0, positional_labels 0, sameness ok vs last 5, entity_spend and top2 soft advisories only).
- Draft B final: validator exit 0, zero advisories; eval exit 0 (number_spend 3, hook_concrete via number:10, scene_specificity 6/6, positional_labels 3 legal action labels, sameness ok).
- Writer A's first call died on a network read timeout and was retried once (transport, not quota); draft B's writer and the judge completed first try.
