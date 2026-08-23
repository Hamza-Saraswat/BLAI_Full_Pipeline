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
