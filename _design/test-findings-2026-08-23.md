# Test findings: local dry run, 2026-08-23

Everything the dry run catches, in the order it was caught. Branch `test/dry-run-2026-08-23`.

Severity: **blocker** stops a real run; **quality** ships bad work; **friction** costs time or trust; **blocked** cannot be tested here.

| # | Stage | Severity | Finding | Status |
|---|-------|----------|---------|--------|
| 1 | 01 radar | quality | No relevance gate: Hacker News ranks by discussion volume, so a missing-crypto-executive story scored 49 and a marathon-medal story 38, both with no product and no AI topic, and both landed in the top 10 | **fixed** |
| 2 | 01 radar | quality | Lane assignment classifies the *source*, not the video you could make: 54 of 64 items landed in `news-react` because GitHub releases and HN posts are news-shaped. A llama.cpp release is equally a how-to or a myth-bust | open |
| 3 | 01 radar | blocked | Reddit returns 403 without OAuth. r/LocalLLaMA is where myth-bust and explainer material lives, so without it the radar is a release feed, which is most of the cause of finding 2 | blocked on credentials |
| 4 | 02 ideas | blocked | No YouTube key and no vidIQ connector, so competition and volume are unmeasured and every competition z-score is 0.00. Opportunity collapses to autocomplete depth, which rewards broad brand keywords | blocked on credentials |
| 5 | 02 ideas | quality | **Search demand is structurally blind to breaking news, and credentials will not fix it.** "ollama claude desktop" scored depth 1 and ranked last of 11; the Ollama and Claude Desktop integration shipped three hours before the sweep and is arguably the biggest story in the window. vidIQ volume for a one-day-old phrase is also near zero | open |

| 6 | 03 research | friction | Research depth is real but source count is below the contract: 4 fetched sources per pick against the 8-12 the scope file asks for. Without FireCrawl every source is one WebFetch, so depth costs wall-clock rather than money | open |
| 7 | 03 research | quality | **The two briefs each surfaced a source contradiction the writer would otherwise have spoken as fact.** Unsloth: the release notes describe LAN access as shipped while issue 9207 still reads open and unresolved. Ornith: Terminal-Bench 2.1 is 46.2 on the model card and 47.0 in secondary coverage, and the card claims a single 80GB GPU while giving the BF16 size as ~19 GB | working as designed |

| 8 | 04 script | quality | Style-pack rotation is sequential-only: `style_rotation.py --pick` compares against the last recorded entry, so two Shorts produced in the same morning both returned `signal`. It is order-dependent, and the contract's pick-then-record sequence only saves it if the two runs are strictly serial | open |

| 9 | 04 script | quality | **`entity_spend` and `top2` are unsatisfiable and fire on almost everything.** The extractor pulled 22 "entities" from the Ornith brief for a 104-word script, including sentence fragments (`GB and BF16`, `OpenHands for SWE-bench and Harbor`, `Terminus-2 46.2`), quantization format names and the license. From the Unsloth brief it produced `LAN`, `Auto`, `Settings`. Both gates failed on all four drafts, and `entity_spend` fails on 35 of the 38 v1 boards | open |
| 10 | 04 script | friction | The ported `styles/history.json` is v1's live history, so assigning a pack by topic fit collides with it silently: `terminal` drew a rotation advisory because v1 used `terminal` on 2026-08-22 | open |

| 11 | 04 script | blocker | **Two parallel writers collided on a shared scratchpad path.** Both generated their storyboard with a script at `scratchpad/build_b.py`; the second overwrote the first and its run regenerated the other writer's output file. In production these two drafts are parallel subagents inside one stage, so this is a live data-loss path | open |

| 12 | 04 script | quality | **Blind writers converged on the same hook.** The two Unsloth drafts, written by workers who could not see each other, opened with "Unsloth won't answer from the couch" and "Unsloth won't answer from your couch". The variety in the two-draft design comes from structure, not from the opening | open |

| 13 | tooling | blocker | **`tools/reset-run.py` silently skipped every ledger.** It assumed a bare JSON list; `script-ledger.json` is `{_doc, entries}` and `styles/history.json` is `{_rule, used}`, so a reset removed the files and left the ledger entries behind. That is exactly the half-cleaned state the plan warned would make the next run lie | **fixed** |
| 14 | 04 script | quality | **The judge found permitted labels still failing the content test.** Draft A's two labels were legal (has_process true, under the cap, each naming an action) and the gate passed them, but deleting "Step one:" loses nothing, and the draft opened a count it never closed: Step one, Step two, then "Now pick up the laptop" | open |
| 15 | 04 script | quality | **Both judges, independently, said the rubric rewards engineering over teaching.** Ornith: the draft that explains the mechanism lost by seven to the one that skips it. Unsloth: "the rubric picked the better-engineered one over the better-written moment." The rubric scores hook mechanics in three places and teaching in none | open |
| 16 | 04 script | quality | The rubric is structurally biased against `myth-bust`: rows 1, 2 and 6 all punish a shape that must state the belief before breaking it. B lost four points on shape before a question of craft was asked; on craft rows alone A led 12-9, not 21-14 | open |
| 17 | 04 script | quality | A factual drift no gate can see: the winning Ornith draft says "Nobody outside Ornith has reproduced that yet" where the brief says "No independent reproduction was found". Absence of evidence compressed into an assertion | open |
| 18 | 04 script | friction | The voice rules contain rules no gate checks and readers disagree about. The Unsloth judge read the winner as breaking "not antithetical, at most once per script" at least twice; a mechanical scan finds one, which is compliant. Neither `validate_storyboard.py` nor `eval_short.py` contains the word | open |

| 19 | 05 package | friction | The validator advises every description to contain "(narration is ai-generated", inherited from v1 where narration was a stock synthetic voice. `shared/playbook/compliance.md` says an own-voice clone is explicitly exempt from disclosure. The gate and the playbook now disagree | open |

| 20 | long-form 01 | quality | The long-form radar's series spread is healthy where the Shorts lane spread was not: benchmarks 25, inference-engineering 15, my-dgx-spark-projects 12, beyond-llms 5, local-ai-for-dummies 3. But `dgx-spark-specific` returned **0 items in seven days**, which is a content-planning signal rather than a defect | note |
| 21 | long-form 02 | quality | **Second confirmation of finding 5.** `llama.cpp` scored 94.2 and ranked first on an autocomplete depth of 90, which is what any broad brand head term scores. It is a changelog, not an episode. `selection-rules.md` discards before sorting, so the rule order caught it, but the score alone would have chosen it | open |

| 22 | long-form 03 | quality | **The deep research caught a vendor formula that would have produced a wrong episode.** NVIDIA's published KV-cache formula counts attention heads; every modern grouped-query model (Qwen3-8B: 32 query heads, 8 key-value heads) is overstated four times by it. A script quoting the vendor doc verbatim would tell viewers to budget four times the memory they need | working as designed |
| 23 | long-form 03 | quality | The researcher assigned to interrogate a piece of folklore found the folklore is narrower than believed and reverses under measurement. That instruction is worth keeping in the research contract | working as designed |
| 24 | long-form 03 | friction | A units trap no gate could catch: Ollama prints context tiers in GiB, GPU vendors print GB. "24 GiB" is about 25.8 GB, so a 24 GB card sits just under Ollama's threshold, not at it | recorded in the brief |

| 25 | long-form 04 | quality | **A brief can contradict itself and nothing checks it.** The brief's `process_steps` told the writer to "leave about a gigabyte of slack" while its own `unverified` list called specific headroom advice folklore with no measurements behind it. The outline writer noticed, refused the instruction, and substituted a sourced check instead | open |

| 26 | long-form 04 | quality | **Finding 12 reproduces in long-form.** Both outline writers, blind to each other, chose the same 0:20 number (6.19 GB) and built their hook on the same collision between a parameter count and a file size. Convergence is not a Shorts-only effect | open |
| 27 | long-form 04 | note | **The private scratch directory fixed finding 11.** Each writer was given `.local-builds/<slug>/outline-<A\|B>/` and told never to use a shared path. No collision, and one writer left its verification script in its own directory where it belongs | **fix validated** |
| 28 | long-form 04 | quality | Both writers independently refused the brief's folklore instruction, not just one. Two blind readers treating the `unverified` list as binding on the rest of the brief is stronger evidence than one | working as designed |

| 29 | 03 research | quality | **Root cause of the convergence finding, and it is mechanical.** Every brief's `## Summary` is byte-identical to its `## Thesis`, in both workspaces. `brief-format.md` asks Summary for three to five lines carrying the thesis, the most arresting number, the strongest concrete case, what could not be verified and any source conflict. Collapsing five things into one sentence removed most of what a writer had to diverge on | open |
| 30 | long-form 04 | friction | The outline judge's tiebreak could not have worked: it falls back to "missing or empty ledger scores everyone 3", but the ledger is present with the episode in it and merely has no structure recorded yet, which is a third state the rubric does not name | open |

| 31 | long-form 05 | quality | **A scene hint carries an implicit truth claim, and no gate knows it.** The writer refused `terminal-replay` for two beats because nothing ran on this machine: using it would "dress published documentation as a measurement". It chose `code-typing` instead. Nothing in the spec, the schema or the validator connects a scene type to whether a capture exists | open |
| 32 | long-form 05 | quality | The writer rejected the brief's own suggested analogy because the analogy's stated limit contradicted the chapter it was meant to serve, then caught a second analogy that had crept in disguised as a different picture. The one-analogy rule held only because the writer enforced it on itself; the gate counts markers and found zero | working as designed |

## Detail

### 1. Radar relevance gate (fixed)

Live run, 82 candidates. `Four Years Ago, a Crypto Boss Went Missing` scored 49 on 50 points and 16 comments; `Sydney Marathon medal mistakenly depicts Munich stadium` scored 38. Both had `products: []` and an empty summary. Fix: an item must name a known product or carry one topic term (about 35 patterns: llm, local ai, gpu, vram, quantization, kv cache, tokens per second, inference, mixture of experts and the rest) in its title, summary or URL. Re-run dropped 17 of 81. Deliberately generous: `ai` alone passes.

Files: `skills/trend-radar/scripts/scoring.py` (`relevance()`, `TOPIC_TERMS`), `scripts/radar.py` (gate after dedupe, count on the stats line), `rules/scoring.md`.

### 2. Lane assignment classifies the source (open)

Observed spread: news-react 54, how-to 2, explainer 2, enterprise-privacy 2, myth-bust 0, comparison 0. The selection rules require the two daily picks to come from different lanes with at most one news-react, so on this digest the second pick had six items to choose from. It did not block the run because the ideas stage assigns a lane per candidate, but a one-dimensional digest biases the writer toward news-react.

Proposed fix, not yet applied: the radar should tag an item with the lanes it *could* serve rather than the one its source implies, or drop lane grouping from the digest and let the ideas stage own it entirely.

### 3. Reddit dead without OAuth (blocked)

`[radar] reddit: every subreddit failed`. The public `.json` endpoint answers 403 to this client regardless of user agent. Moves Reddit credentials up the priority list: free, and the cheapest fix for topic variety.

### 4 and 5. Opportunity scoring (blocked, and open)

Live autocomplete depths: unsloth 57, ornith 1.5 34, deepseek api pricing 17, abliterated model 16, local llm quality 14, local whisper dictation 14, sglang 12, local text to speech 10, qwen 3.8 27b 7, ollama claude desktop 1, ollama time to first token 0. With competition unmeasured, `opportunity = 50 + 15 x z(depth) + 10 for a named product`, so the ranking is a popularity contest between keywords.

The structural half of the problem: a story that broke this morning has no search history, so both autocomplete and vidIQ score it near zero forever. Proposed fix, not yet applied: measure demand per lane. Evergreen lanes keep autocomplete and vidIQ volume; `news-react` uses the story's spread, which the radar already computes as `signals.signal` and the ideas stage currently discards.

### 6. Research depth without FireCrawl (open)

Each brief cites 4 distinct fetched URLs and 7 claims. `shorts-research-scope.md` asks for 8-12 sources at standard depth. Nothing failed, because `validate_research.py` enforces claim count and URL presence rather than source count, but the briefs are thinner than production would be. With a FireCrawl key the search-and-scrape loop gets cheaper and wider; without it every source is a separate fetch and depth is bounded by patience rather than by budget.

### 7. Contradictions surfaced rather than swallowed (working as designed)

This is the research stage doing its job, and it is worth recording as evidence rather than as a defect.

**Unsloth.** The v0.1.801-beta release notes describe LAN Remote Access as shipped in preview with a Settings section, QR codes and a forced password change. Issue 9207, which asked for exactly this feature, still reads as open with no maintainer response and a user-documented batch-file workaround. One of the two is stale. The brief's `unverified` list says so and tells the writer not to claim the issue was closed by the release.

**Ornith.** Terminal-Bench 2.1 is 46.2 on the model card and 47.0 in secondary coverage, so the brief forbids speaking the number without picking one. The same card says the model "serves on a single 80GB GPU" in BF16 while giving the BF16 size as ~19 GB; the 80GB line looks inherited from the 397B family member. Every benchmark is self-reported, though with unusually strict controls (five runs averaged, git history stripped, network disabled during solving), and the brief records both halves of that.

Both briefs also carry the three new writer fields. `has_process` is true for Unsloth with four real steps and false for Ornith, which means positional labels are legal in one script and banned in the other. That is the first live exercise of the label rule.

### 8. Style packs collide between same-day siblings (open)

`python3 skills/render-shorts/scripts/style_rotation.py --pick --slug <slug>` returned `signal` for both of today's Shorts, because the ledger's last entry is the only thing it compares against and neither had been recorded yet. Two videos on the same feed, the same day, in the same look.

The stage contract does say pick then record, so a strictly serial run would give the second one a different pack. That makes the rule correct but fragile: the two picks of a day are produced by the same routine and nothing forces them to be serial, and a re-run of one slug would re-pick against a ledger that now contains the other.

Two options, neither applied yet. Make `--pick` accept the packs already claimed today and exclude them, or fold the style pack into the `sameness` gate, which already refuses a structure, a hook pattern and a duration that repeat.

Sidestepped for this run by assigning packs on topic fit, which is what `styles/README.md` asks for anyway: `signal` for the Ornith model release (kinetic type, benchmarks and news) and `terminal` for the Unsloth video, which is entirely about flags and settings.

### 9. The entity gates are noise (open)

What the extractor returns for the two briefs written today:

- Ornith: `Ornith`, `Ornith-1.5`, `Terminus-2`, `Terminal`, `Terminus`, `Qwen3.5 and Gemma4`, `GB and BF16`, `GPQA Diamond 86.4`, `Ornith AI`, `OpenHands for SWE-bench and Harbor`, `Terminus-2 for Terminal-Bench`, `Ornith-1.5-9B`, `Qwen3.5`, `Gemma4`, `Q5_K_M`, `Q6_K`, `Q8_0`, `BF16`, `Terminus-2 46.2`, `MIT`, `OpenHands`, `Harbor`. That is 22 for a script the band caps at 130 words, so `entity_spend`'s floor of half is arithmetically out of reach.
- Unsloth: `LAN`, `Auto`, `Settings`, `LAN Remote Access`, `Cloudflare`. `Auto` is the adjective from "Auto compaction"; `Settings` is a menu; `LAN` duplicates `LAN Remote Access`. `top2` demanded `Auto`, which would have forced an unrelated feature into the video.

Three failure modes in one: phrases split across conjunctions and prepositions, file-format and license tokens treated as named examples, and generic capitalised words admitted. Both writers noticed, refused, and recorded the reason in `notes_for_review`, which is the behaviour we want from a writer and the wrong reason to need it.

This is not new. `entity_spend` fails on 35 of the 38 v1 boards, so the gate has been firing on nearly everything since v1 and has been trained into background noise. A gate that always fails teaches you to ignore gates.

**The gate is wrong in both directions.** It fails good scripts, and it passes on accidents. Unsloth draft B scored `entity_spend` 1.00 and `top2` present, apparently naming every entity including `Auto`. The script never mentions Auto compaction. The match came from the phrase "replace the auto-generated admin password": the entity regex uses word boundaries, and a hyphen is a word boundary, so `\bAuto\b` matched inside `auto-generated`. A gate satisfied by a coincidental substring carries no signal at all.

Proposed fix, not applied: rebuild `extract_entities` on the curated product vocabulary that already exists in `skills/trend-radar/scripts/scoring.py` (`PRODUCTS`, about 60 named products, vendors and hardware with regexes), plus proper nouns that appear in the brief's thesis. Reject anything containing " and ", " for ", a digit-only tail, a license identifier or a quantization format. Then re-check the floor: half of three or four real entities is reachable, half of twenty-two is not.

### 10. The inherited style ledger is live (open)

`skills/render-shorts/styles/history.json` came across from v1 with its real rotation history, whose most recent entry is `terminal` on 2026-08-22. Assigning `terminal` to today's Unsloth video on topic fit therefore drew "style_pack 'terminal' same as previous video -- rotate". Harmless here, but it means the ledger is not a clean slate and any hand-assignment has to be checked against it. Related to finding 8.

### 11. Parallel writers overwrote each other's work (open)

Reported by the `unsloth-B` writer, unprompted: "Another agent in this session overwrote `scratchpad/build_b.py` with its own generator mid-run, and my next invocation of that filename regenerated `2026-08-23-ornith-1-5-9b-draft-B.json` from *its* script, not mine."

Two independent writers, told to write their own storyboard JSON, both reached for the same obvious scratch filename. The second write won, and running it emitted the wrong slug's file. The Ornith draft B file was later re-verified as coherent and carrying its own content, so nothing was lost this time, but only because the affected writer was still running and rewrote it.

This is not a test artifact. The stage contract runs draft A and draft B as parallel subagents inside one stage, every day, for every video, and the same collision is available every time. Two videos are produced each morning, so four writers can be live at once.

Proposed fix, not applied: the stage contract should hand each writer a private scratch directory (`.local-builds/<slug>/draft-<A|B>/`) and say so, and writers should be told to write only to their own draft path. A cheaper belt-and-braces version: have the stage verify after each draft that the file's `slug` and `structure` match what that writer was assigned, which is a two-line check and would have caught this immediately.

### 12. Two blind writers wrote the same hook (open)

Draft A: `Unsloth won't answer from the couch`. Draft B: `Unsloth won't answer from your couch`. One word apart, from two workers with no access to each other's files.

This is the brief working as designed and the draft design working less well than intended. `viewer_situation` in the brief reads "Your model runs on the box in the other room and you are on the couch with a laptop or a phone", the hook library awards a point for naming the viewer's situation, and both writers took the same shortest path from that sentence to a hook. The Ornith pair converged less sharply but still both led on the file size (`5.63 GB fixes real bugs` and `6 GB file. It fits your card.`), because the brief names the size as the surprise.

The consequence is that two drafts buy less variety than the plan assumed. The shapes differ, the payoffs differ, the endings differ, but the first three seconds, which is where the retention cliff is, can be nearly identical. The judge then chooses between two videos that open the same way.

Proposed fixes, none applied. Assign each writer a different hook pattern from the library alongside its structure, so A opens on a number and B opens on a situation. Or have the judge score hook distance between the drafts and refuse a pair whose hooks share their first four words, which is a check the variety ledger already computes for the between-video case (`hook_head`).

### 13. The reset tool did not reset (fixed)

Written in Phase 0 precisely so repeated runs would not inherit each other, and it handled one of the three ledger shapes. `python3 tools/reset-run.py --slug ... --dry-run` listed eight files to remove and no ledger lines at all. `prune_ledger` tested `isinstance(data, list)` and returned early otherwise, so `script-ledger.json` (`{_doc, entries}`) and `styles/history.json` (`{_rule, used}`) were skipped in silence. Fixed to handle all three shapes and to log loudly when a fourth appears rather than returning quietly.

### 14 to 16. What the judges found in the rubric

Two judges with fresh context, no access to each other, reached the same verdict about the instrument they were given.

**Labels can be legal and still be the old habit.** The Unsloth judge scored draft A's navigation 1 of 3 and explained why better than the rule does: "Delete 'Step one:' and you get 'Open Settings and switch on network access' -- nothing lost, and stronger for opening on the verb." Worse, the draft announced a count and abandoned it: Step one, Step two, then "Now pick up the laptop", so a viewer waits for a third that never lands. And the labels arrive at second thirty-seven, after a four-sentence detour, functioning as a re-entry marker after a digression rather than as help for someone's hands. The gate's structure whitelist is necessary and not sufficient; the judge's row 5 is doing the real work.

**The rubric cannot see teaching.** The Ornith judge: "it scores hook mechanics three separate times (rows 1, 2, and half of 6) and scores teaching zero times, which is why the draft that explains the mechanism lost by seven to the draft that skips it." The losing draft owned the only real explanation in the pair, that a four-bit build keeps fewer bits per stored number so the file shrinks, and the grafting rules correctly forbade rescuing it. The Unsloth judge reached the same place from the other side: draft A held "the only moment in either script with a pulse" and lost.

**And it is biased against shapes that must set up before they pay off.** Rows 1, 2 and 6 all reward getting concrete in the first five words. A myth-bust has to state the belief first. Four of B's seven-point deficit were structural, not craft.

Proposed fixes, none applied. Add a teaching row (does a viewer who did not know the mechanism now know it). Score rows 1 and 2 once rather than three times. Let row 6 compare against the ledger only, not against "the obvious treatment", which double-counts shape. And consider whether a perfect 21 on the first run means the ceiling is too low.

### 17 and 18. Two things no gate can catch

The winning Ornith draft narrows "No independent reproduction was found" into "Nobody outside Ornith has reproduced that yet". Its own description field states it correctly, so the drift is in the spoken line only. No gate compares a claim's strength against the brief's wording, and it is not obvious one could.

Separately, the voice rules' "not antithetical, at most once per script" is checked by nothing, and the two readings of the winning Unsloth draft disagree: the judge counted at least two, a regex scan counts one. A rule that careful readers score differently and no gate measures is a rule that will drift. Either give it a checkable definition, or move it out of Hard Constraints and into the judge's rubric where a human-style reading belongs.

### 19. The AI-disclosure advisory contradicts the compliance rule (open)

`validate_storyboard.py` raises an advisory when a description does not contain the substring `(narration is ai-generated`. That rule came from v1, where narration was Kokoro, a stock synthetic voice.

The v2 compliance page says the opposite for the production case: YouTube's disclosure policy does not require a label for "cloning one's own voice to create voice overs or dubs", so a channel narrated by the creator's own professional clone should not be carrying a synthetic-media disclosure at all. Both package notes were written to the playbook and neither carries the string, so the advisory will fire on every future script.

It is only an advisory, which is the mild version of finding 9: a check that fires on everything teaches people to stop reading checks. Proposed fix, not applied: make the advisory conditional on the voice engine recorded in `voice.config.json`, firing for a stock or designed voice and staying silent for a professional clone of the creator. That also keeps it honest during local test runs, which use Kokoro and therefore genuinely should disclose.

### 20 and 21. The long-form thinking half, stages 01 and 02

**The radar is healthier in long-form than in Shorts.** Same sources, same relevance gate, a seven-day window instead of forty-eight hours: 158 candidates, 29 dropped off-topic, 124 kept, and the series grouping actually spreads (benchmarks 25, inference-engineering-at-home 15, my-dgx-spark-projects 12, beyond-llms 5, local-ai-for-dummies 3). Finding 2, where a source-shaped lane classifier pushed 54 of 64 Shorts items into `news-react`, does not reproduce here, because the long-form series are defined by subject rather than by recency.

`dgx-spark-specific` returned zero items across seven days. Not a bug: there was no DGX Spark news this week. Worth noticing because that series is one of six in the rotation and the rotation rule assumes each has viable candidates.

**The head-term problem is now confirmed twice.** In Shorts it buried the day's biggest story at rank 11 of 11. In long-form it promoted a changelog to rank 1 of 7 at 94.2, on an autocomplete depth of 90 for the bare string `llama cpp`. Both are the same defect seen from opposite ends: search depth measures how established a phrase is, not how good an episode would be.

The pipeline survived it because `selection-rules.md` orders the operations correctly, discarding candidates that cannot carry ten minutes before sorting by opportunity, and the radar's episode-signal line had already called that candidate a changelog. That is a real safeguard and it should be said plainly: the rule order is doing work the score cannot.

The pick is `2026-08-23-which-model-fits-gpu`, a `buyers-guide`-shaped episode on the `benchmarks` series. Value types are EQUIPS and TEACHES, deliberately not PROVES, because the DGX Spark is unreachable from this machine and the episode therefore rests on published file sizes and memory arithmetic rather than a first-party measurement. That also means stage 03 will produce no experiment plan, which is the input stage 08 needs in order to test its skip-cleanly path.

### 22 to 24. What deep research bought

Four researchers in parallel, one question each, 19 distinct fetched sources into a brief carrying 21 claims, 12 key numbers and 10 unverified items. Three results are worth recording as evidence that the stage pays for itself.

**A vendor's own formula is wrong for modern models.** NVIDIA publishes the per-token cache cost as two times layers times heads times head dimension times precision. That counts attention heads, which is correct only for older multi-head models such as Llama 2 7B. Qwen3-8B has thirty-two query heads and eight key-value heads, so the published formula overstates its cache four times over. A writer quoting the vendor documentation verbatim, which is exactly what a careful writer would do, would have told viewers to budget four times the memory they need. The brief now carries both the published formula and the correction.

**Interrogating folklore found the folklore.** One researcher was told that the "bigger model at lower precision beats smaller at higher precision" claim is widely repeated and often unsourced, and that finding weak support would be more valuable than a confident answer. It found the origin (Dettmers and Zettlemoyer 2023, four-bit almost universally optimal), established how narrow that result is (zero-shot accuracy only, models to 2022, no instruction tuning, no reasoning), and found a 2025 study across roughly seventeen hundred inference scenarios where the ordering reverses: eight billion at eight-bit beats fourteen billion at four-bit. That reversal is now the episode's spine. The instruction that produced it should live in the research contract rather than in one prompt.

**A units trap.** Ollama documents context tiers in GiB; every GPU vendor prints GB. Twenty-four GiB is about 25.8 GB, so a twenty-four gigabyte card sits just below Ollama's threshold rather than at it, and gets the smaller default context. No gate could catch this. It is in the brief's `unverified` section as a warning to the writer.

The same run also produced four more model-card contradictions, including Ornith's 9B card recommending an eighty-gigabyte GPU for a file its own table sizes at 17.9 GB, which independently reproduces the contradiction found in the Shorts brief for the same model.

### 25. The brief contradicted itself, and the writer caught it (open)

`process_steps` item three reads "Subtract both from your card's memory and leave about a gigabyte of slack". `unverified` item two reads "Specific headroom advice such as 'leave 512 MiB' or 'leave ten to twenty percent' is folklore. The guide that carries it contains no benchmarks and no author measurements."

Those cannot both be followed. The outline writer resolved it correctly and said so: it asserted no headroom figure anywhere, and replaced the slack line with the llama.cpp maintainer's statement that the runtime slice is not calculable, plus `ollama ps` as an empirical check the viewer can run. That is the better answer, and it came from the writer reading the `unverified` list as binding on the rest of the brief rather than as an appendix.

Two things follow. The good one: the `unverified` list is doing real work as a guard on the brief's own confident sections, which is more than it was designed for. The bad one: I wrote that brief, the research validator passed it, and nothing anywhere compares a brief's instructions against its own caveats. A brief that tells a writer to state a number it elsewhere calls folklore will usually be obeyed rather than questioned.

Proposed fix, not applied: add an audit row to the research contract requiring that no `process_step`, `suggested_outline` or `thesis` asserts something the same brief's `unverified` list disowns, and have the writer flag rather than silently resolve such a conflict. A mechanical version is possible for the obvious cases: flag when a number appears in both a confident field and an unverified entry.

### 26 to 28. The second draft pair, and one fix confirmed

**Convergence is structural, not a Shorts accident.** In Shorts, two blind writers produced hooks one word apart. In long-form, two blind writers picked the same number for the 0:20 beat and built the same collision: a parameter count against a file size. Outline A opens "Twenty-seven billion parameters, in a file of six point one nine gigabytes"; outline B opens on the viewer's twelve-gigabyte card and arrives at the same 6.19 GB sixteen seconds in. Both then rejected the same alternative for the same reason, the DGX Spark's bandwidth fact, because it measures a second axis.

That the reasoning is sound in both cases is the point. Given one brief, one hook library and one value framework, two competent writers converge, because the brief names the surprise and the rules reward naming it early. The two-draft design buys different shapes reliably and different openings only by luck. The fix proposed under finding 12, assigning each writer a different hook pattern, applies here unchanged.

**The scratch fix works.** Finding 11 was a live data-loss path: two Shorts writers used `scratchpad/build_b.py` and one regenerated the other's output. This round each writer was given a private directory under `.local-builds/<slug>/` and told never to use a shared path. No collision occurred, and outline A's verification script sits in its own directory. The instruction is cheap and should go into the stage contracts rather than into individual prompts.

**And the guard held twice.** Both writers, independently, refused the brief's "leave about a gigabyte of slack" because the same brief's `unverified` list calls headroom figures folklore. One writer doing that is a good writer; two doing it blind means the `unverified` list is reliably read as binding. That is worth stating in the research contract explicitly, since it is currently an emergent property rather than a documented one.

### 29. Why both writers wrote the same hook, twice (open)

The outline judge traced the convergence to its cause rather than restating it: "the brief's `## Summary` and `## Thesis` are the same sentence word for word, and both `## Angle` lines restate it. The angle was decided before this stage opened, so two outlines could only buy ordering and shape."

Checked, and it is true of both briefs written today, Shorts and long-form. `brief-format.md` specifies Summary as "Three to five lines for the reviewer: the thesis, the most arresting number, the strongest concrete case, what could not be verified, any conflict between sources." What the briefs actually carry is the thesis sentence, repeated.

This is the mechanical half of findings 12 and 26. Two writers converge partly because writers converge, and partly because the document that is supposed to hand them five distinct things hands them one thing twice. Fixing the summary will not eliminate convergence, but it widens what there is to diverge on, and it costs nothing.

Fix: an audit row in the research contract stating that Summary is not a restatement of the thesis and must carry the five elements the format file names. Worth pairing with the finding 12 fix of assigning each writer a different hook pattern.

### 30. A third ledger state the rubric does not name (open)

The judge reported that its tiebreak was unusable. The rubric's Difference row says to score everyone 3 when the ledger is missing or empty; here the ledger exists and contains this very episode, but with an empty `structure` field, because stage 02 creates the entry and stage 04 fills the shape in. The judge handled it sensibly by scoring distance from the brief's own suggested outline and saying so, but the rubric should name the state rather than relying on a judge to invent a rule.

### 31. Scene hints make claims (open)

The winning outline's visual philosophy asked for a terminal capture in chapter five. The writer refused it: "because nothing ran on this bench, beats 5.7 and 5.9 use the `code-typing` scene hint rather than `terminal-replay`, since `terminal-replay` requires a `capture_ref` in `capture.json` and would dress published documentation as a measurement."

That is the right call and nothing forced it. `terminal-replay` renders as a recording of a command running, which tells a viewer, without a word being spoken, that we ran it. For an episode whose value types are deliberately EQUIPS and TEACHES rather than PROVES, and which states out loud that nothing here was measured by us, a terminal replay of somebody else's documentation is a lie told in pictures.

The gap is real: `longform-spec.schema.json` lets any scene name a `capture_ref`, and the render stage falls back to a labelled placeholder when a capture is missing, so a `terminal-replay` with no capture degrades quietly rather than failing. Nothing checks that a scene type implying first-party measurement is backed by one.

Proposed fix, not applied: make `terminal-replay` require a resolvable `capture_ref` at spec time, and have the spec stage refuse the scene type when the run has no experiment plan. That is a small validator rule and it protects the channel's strongest asset, which is that its measurements are real.

### 32. The one-analogy rule is self-enforced (working as designed)

Two behaviours worth recording. The writer rejected the brief's suitcase analogy because "its own stated break, a suitcase does not get heavier as the trip runs, contradicts the exact property chapter 2 exists to teach" -- reading an analogy's declared limit as a disqualifier rather than as a footnote. Then, during its own review, it found a second picture that had crept in: a mixture-of-experts beat ending on a company-of-employees line, which is the receptionist analogy from the signature file wearing different clothes, and replaced it with the plain mechanism.

The gate counts analogy markers and found zero, so neither the presence of the desk analogy nor the near-miss second one was visible to it. The rule held because the writer held it.
