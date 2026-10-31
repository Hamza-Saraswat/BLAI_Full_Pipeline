# Drafts and judge: 2026-10-31-fake-qwen2-checkpoints-the-tru

Two blind writers on Kimi K3, one packet each, private scratch dirs; judge on Kimi K3 with the
rubric as system file. Both drafts passed the full gate battery (validator 0 blockers 0
advisories, eval gates green, variety ok against the 55-entry ledger) before judging.

## Draft A (how-to-three-moves, hook: tonight)

HOOK: Three moves and your next Hugging Face model stays clean tonight.

| id | narration |
| s01 hook | Three moves and your next Hugging Face model stays clean tonight. |
| s02 | You download models by name, clicking through trust_remote_code, the flag that runs the repo's Python. Fake Qwen checkpoints turned that click into a miner. |
| s03 | Move one: check the org. The real publisher is Qwen. The fakes were random-string accounts, thirty-one across seven orgs. |
| s04 | Move two: open the files page. One fake's weights were forty-two bytes. Keep trust_remote_code off unless you read the Python beside them. |
| s05 | One honest catch: Ollama and llama.cpp never type that prompt. Pluto tracked trust_remote_code repos only, so pin your sources there. |
| s06 payoff | Move three: pin the revision and verify the hash before loading from Hugging Face. Your GPU stays yours. |

## Draft B (worked-example, hook: situation) -- WINNER

HOOK: You download open models from Hugging Face and click trust.

Full script in [slug]-script.md. Six scenes: page -> files -> click -> miner -> cleanup.

## Judge scores (Kimi K3)

| row | A | B |
|-----|---|---|
| 1 Hook | 2 | 2 |
| 2 Payoff timing | 2 | 3 |
| 3 Specificity | 2 | 2 |
| 4 Voice | 2 | 3 |
| 5 Navigation | 2 | 3 |
| 6 Difference | 3 | 3 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 2 | 3 |

TOTALS: A=18 B=20. Winner: B. Grafts: none (A's hook did not clear the two-point threshold on
row 1).

Judge rationale (condensed): B lands the mechanism by second four and is what the hook promised;
its transitions name what changed and cannot be reordered; "The weights never mattered." is the
dry beat that lands unexplained; a viewer could flag the next variant. A spends its first ten
seconds enumerating and asserts the danger rather than showing it.

## Corrections to the judge (recorded, not rescoring)

The judge saw only a brief excerpt and flagged as "invented": Pluto attribution, svc.py, and
PRL-as-Pearl. All three are in the research brief (Pluto Security's disclosure; the svc.py
startup-file grep is Pluto's own quick check; PRL is Pearl). Row 3 was scored 2-2 regardless,
so the verdict stands.

## What the losing shape needed

A's how-to needed the flagship artifact (the 42-byte weights file) up front as proof and moves
that each advance the causal chain instead of labeling steps, and it needed to show the
config->Python mechanism rather than assert the click->miner chain.

## Gate results

- Validator: A exit 0, B exit 0 (0 blockers, 0 advisories each; warnings: FK 5.0, hook-brief
  motion onset noted).
- eval_short.py (against the real 56-entry ledger path): A all gates pass, B all gates pass.
- variety_check check: both ok, no violations, no advisories; winner recorded as entry 56.
- normalize_narration.py: 126 words, 6 scenes, 2 scenes changed; .txt + .norm.json written to
  stages/06-voice/output/.
