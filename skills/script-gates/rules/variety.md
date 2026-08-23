# Variety

Nothing in the pipeline used to check whether today's Short felt like yesterday's. Eleven of twelve smooth boards in the v1 corpus were pinned to `target_duration_s: 113`, two shipped byte-identical narration, and the same closing move came back week after week. `scripts/variety_check.py` keeps a ledger of what shipped and the `sameness` gate refuses a board that repeats the last few.

Re-teaching a concept is expected and encouraged: every Short is a cold open for a feed viewer. The *wording* is what may not repeat.

## The ledger

`output/script-ledger.json`, one entry appended per shipped script, newest last. `variety_check.py` accepts a bare JSON array or `{"entries": [...]}` and writes the second shape. A missing, empty or unreadable ledger is treated as no history: every check passes and the run continues.

| Field | What it holds |
|-------|---------------|
| `slug` | the board's slug (`--slug` overrides it; the ledger keys off this) |
| `date` | `YYYY-MM-DD`, `--date` or today |
| `format` | `script_format`, or `classic` when absent |
| `structure` | the storyboard's `structure`, or `null` |
| `hook_pattern` | the storyboard's `hook_pattern` if it carries one, else classified (below) |
| `hook_head` | first four words of `hook_text`, lowercased |
| `closing_move` | first six words of the last scene's narration, lowercased |
| `target_duration_s` | as written in the storyboard |
| `opener_bigrams` | sorted unique lowercased first-two-words of every sentence in `narration_full` |
| `analogies` | `analogy.vehicle` when present, else `[]` |
| `shingles8` | hashes of every 8-word sequence in the narration, hex, capped at 400 |

`shingles8` is capped by keeping the 400 **lowest** hash values, not the first 400 in reading order. That is a min-hash sample: a 450-word smooth script and a 90-word classic still intersect at the right rate, and the cap is deterministic rather than "whatever came first".

## Hook patterns

The classifier is a small ordered keyword rule set in `variety_check.py` (`_HOOK_RULES`); first match wins. It exists to give the rotation something stable to compare, not to be a taxonomy. Keep this table and the code in step.

| Pattern | Fires on |
|---------|----------|
| `price` | a currency symbol, dollars, price, pricing, cost, cheaper, free |
| `tonight` | tonight, today, this week, right now, by tomorrow, just shipped/landed/dropped |
| `number-shock` | any digit or number word (hundred, billion, percent, twice, …) |
| `wrong-diagnosis` | wrong, mistake, misread, blame, you think, think it's, looks dumb/slow/broken |
| `named-contradiction` | everyone says, myth, actually, but, isn't, didn't, doesn't, won't, can't, not |
| `decision` | should you, which, vs, versus, worth it, buy, pick, or |
| `case` | law firm, clinic, shop, company, business, enterprise, team, employees |
| `situation` | opens on "you", or contains you've / you're / your |
| `other` | nothing matched |

A storyboard may set `hook_pattern` itself; an explicit value always wins over the classifier.

## The `sameness` rules

Hard, checked against the last **5** entries (fewer is fine). A ledger row carrying the same `slug` as the board under test is skipped, so re-checking a board that is already recorded never fails against itself.

| Rule | Fails when |
|------|-----------|
| `structure` | equal to either of the last two entries. Two boards that both leave `structure` unset count as the same shape |
| `hook_pattern` | equal to either of the last two entries |
| `closing_move` | equal to either of the last two entries |
| `target_duration_s` | identical to **all** of the last three (this alone breaks the "always 113" pin) |
| `opener_bigrams` | Jaccard against any of the last five is above 0.35 |

Advisory, never blocking, over the last **10** entries: `repeated_phrase` names every earlier script this narration shares an 8-word-or-longer sequence with, and quotes up to five examples from the current narration. The ledger stores only hashes, so the examples are reconstructed from the script being checked.

## Running it

```
python3 skills/script-gates/scripts/variety_check.py check \
  --storyboard workspaces/shorts/stages/04-script/output/<slug>-storyboard.json \
  --ledger     workspaces/shorts/output/script-ledger.json
```

Prints `{ok, violations, advisories, comparisons, …}`; exit 0 clean, 1 when any hard rule is violated. `--window N` widens or narrows the hard-rule lookback. `entry` prints the row without touching the ledger; `record` appends it once the script is final:

```
python3 skills/script-gates/scripts/variety_check.py record \
  --storyboard <slug>-storyboard.json --ledger output/script-ledger.json --date 2026-08-25
```

`--dry-run` works on every subcommand and never writes. `--slug NAME` overrides the storyboard's own slug for the entry.

`eval_short.py` runs the same rules as its `sameness` gate, but **only when `--ledger` is passed**. With no ledger the gate does not run at all and the eval JSON says so: `overall.detail.sameness.checked` is `false` with a reason, and the report chip reads "not checked (no ledger)". Silence there is not a pass.

## Proceeding past a failure

`sameness` is a hard gate, and like every other hard gate it has one written escape. When a run decides a repeat is right (a follow-up video that deliberately reuses the frame, a correction that must restate the original claim, a duration the physics genuinely pins), it may proceed by writing a **Decisions block** in the hub note before moving on:

```
## Decisions
- sameness: closing_move repeats 2026-08-24-moe-router. Kept on purpose, this is
  the part-two video and the callback is the point. Opener Jaccard 0.21, so the
  sentences themselves are fresh.
```

The block names the rule, the entry it clashed with, and why the repeat is deliberate. A gate failure with no Decisions block is a rewrite, not a judgement call. Two consecutive days of Decisions blocks on the same rule is the signal that the rule, not the script, needs the edit.

## What variety is not

- Not a ban on re-teaching. The memory-bandwidth explanation may open every third video; it may not open them with the same sentence.
- Not a style-pack check. Visual rotation lives in `skills/render-shorts/styles/history.json` and is enforced by `validate_storyboard.py`.
- Not a structure picker. Choosing the shape is the script stage's job; the ledger only refuses the shape it has just seen twice.
