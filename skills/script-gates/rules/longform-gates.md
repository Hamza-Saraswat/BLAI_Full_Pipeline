# Long-form Gates

`validate_longform.py` is the machine gate for a long-form episode script, the sibling of `validate_storyboard.py`. It asks whether the script is buildable and whether it sounds like the channel. It does not ask whether the idea is good; the outline stage's judge rubric does that.

```
python3 skills/script-gates/scripts/validate_longform.py \
  --script    workspaces/long-form/stages/05-script/output/<slug>-script.md \
  --narration workspaces/long-form/stages/05-script/output/<slug>-narration.txt \
  --outline   workspaces/long-form/stages/04-outline/output/<slug>-outline.md
```

`--json` prints the JSON report instead of the text one; `--dry-run` runs every check, prints the report, then exits 0 whatever it found. Exit 0 clean, 1 blockers, 3 advisories only, 2 usage error. The report always carries `blockers`, `advisories` and `warnings`.

Only `--script` is required. Without `--narration` the beat narrations are joined and used instead. Without `--outline` the chapter-order check does not run and `target_minutes` falls back to the script frontmatter; both absences are reported as warnings.

## Pacing arithmetic

Every duration in this file is an estimate at **150 spoken words per minute**, which is 2.5 words per second, the figure `outline-format.md` and the long-form row of `shared/platform-specs.md` both use. Sixty seconds of chapter is therefore 150 words. Nothing here reads audio; the voice stage's real durations supersede these estimates once they exist.

## Blockers (exit 1)

| Check | Blocks when | Threshold |
|-------|-------------|-----------|
| Word band | narration words fall outside the band for the target | `target_minutes` x 150, plus or minus 15 percent. `target_minutes` comes from the outline, or from the script when no outline is given |
| Chapter count | the script has fewer chapters than the minimum, or no `## Chapter N: label` headings at all | at least 3 chapters |
| Chapter length | a chapter's beats are too short to be a chapter | 60 s by word estimate, so 150 words |
| Beat length | a beat row is outside the beat range | 20 to 60 words of narration |
| Measured numbers | a beat's narration carries `[measured]` and its Capture cue cell is empty | every `[measured]` number needs a cue id the experiment plan defines |
| Chapter match | script chapter labels differ from the outline's in order or in count | compared case-insensitively, with punctuation and repeated spaces ignored. Skipped when no outline is given |

A blocker means the next stage cannot do its job: the spec stage maps beats to scenes one for one, the capture stage rewrites `[measured]` lines by cue id, and the package stage builds the description's chapter list from the outline.

## Advisories (exit 3, never blocking)

| Check | Fires when | Threshold |
|-------|------------|-----------|
| Hype | narration contains a banned hype word | the `BANNED_HYPE` list in `validate_storyboard.py` |
| Spoken CTA | narration asks for a follow, a like or a subscribe | the `BANNED_CTA` list in `validate_storyboard.py` |
| Banned opener | the first three sentences contain a template opener | the `BANNED_OPENERS` list plus "in this video", "today we", "let's dive in", "welcome back" |
| Sentence cap | any sentence runs long | more than 20 words, one finding per sentence |
| Sentence average | the script reads long overall | average above 18 words |
| Positional labels | a sentence opens with stage, step, part or phase plus a number | any hit when `structure` is not `build-along`; more than 3 hits when it is |
| Direct address | the first three sentences never say you, your or you're | one marker inside the first three sentences |
| New-information gap | consecutive beats carrying nothing new run too long | more than 30 s by word estimate |
| Opening number | the first 50 words (about 0:20) contain no number | a digit or a number word |
| Analogies | more than one analogy marker in the episode | at most 1 ("think of it as", "imagine a", "like a", "as if", "the way a", "picture a") |

An advisory is a craft note with an owner. Fix it, or keep the line and write the reason in the hub note `## Decisions`, exactly as the Shorts validator's advisories work.

## Warnings (never move the exit code)

No outline given; no narration file given; no `structure` in either frontmatter; a `structure` that is not in the episode-structure library; frontmatter `words` or `chapters` disagreeing with the text; a positional label sentence under 6 words, which means the label names no action.

## Positional labels in detail

The sentence-opening pattern is `(in |that's |and )?(stage|step|part|phase) (one..ten|digit)`, case-insensitive, tested against every narration sentence. The rule it enforces is Hard Constraint 10 in `brand-vault/voice-rules.md`: labels are allowed only when the viewer performs the steps themselves, which for long-form means the `build-along` shape, at most three of them, each naming the action. `structure` is read from the script frontmatter first, then the outline's. When neither carries one, labels are judged as if the shape were not `build-along`, which is the safe direction.

## New information, as the gate measures it

A beat counts as new information when it carries a capture cue id, a digit, a number word, or a capitalised token that is not the first word of its sentence (a product, a company, a file format). Beats that carry none of those accumulate; when a run of them exceeds 30 seconds by word estimate, the gate names the first and last beat of the run. The heuristic is deliberately generous: it catches dead stretches, not weak sentences.

## Shared vocabulary

The banned-word lists and the sentence splitter are imported from `validate_storyboard.py` in the same folder, so Shorts and long-form ban the same words and split sentences the same way. If that import fails, the gate falls back to a shorter built-in list and says so in `warnings`. Change a banned word in `validate_storyboard.py` and both gates move together.

## Thresholds live in the script

`formats.json` is the source of truth for the two Shorts bands and nothing else: long-form has no entry there, so its numbers live here instead. The constants at the top of `validate_longform.py` (`WPM`, `BAND`, `MIN_CHAPTERS`, `MIN_CHAPTER_S`, `BEAT_WORDS`, `SENTENCE_CAP`, `SENTENCE_AVG_MAX`, `MAX_LABELS`, `HOOK_NUMBER_S`, `NEW_INFO_GAP_S`, `MAX_ANALOGIES`) hold every number in this file. Change one there and update the table here in the same commit.

## Fixtures

`fixtures/longform/clean-*.md` is a five-minute `build-along` that reports clean. `fixtures/longform/bad-*.md` is the same gate exercised the other way: six positional labels in a `concept-deep-dive`, a ninety-word beat, a spoken call to action and no second person. Run both after any change to the thresholds.
