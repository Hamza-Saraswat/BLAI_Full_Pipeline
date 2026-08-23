# Test findings: local dry run, 2026-08-23

Everything the dry run catches, in the order it was caught. Branch `test/dry-run-2026-08-23`.

Severity: **blocker** stops a real run; **quality** ships bad work; **friction** costs time or trust; **blocked** cannot be tested here.

## Result: three videos rendered, both pipelines run end to end

| | Ornith 1.5 9B | Unsloth LAN | Which build fits your GPU |
|---|---|---|---|
| Workspace | shorts | shorts | long-form |
| Stages run | 01-07 | 01-07 | 01-10 |
| Output | 30.13 s, 1080x1920 | 74.50 s, 1080x1920 | **8:13**, 1920x1080 |
| Loudness | -14.0 LUFS | -14.1 LUFS | -14.0 LUFS |
| Release gates | **all pass** | **all pass** | **1 of 9 fails: duration** |
| Hub note | `review` | `review` | `review` |

**66 findings.** 12 fixed during the run, 4 blocked on credentials, the rest open with a proposed fix.

The blockers that would have stopped a real run, in the order they would have hit: Manim was never installed (33); GSAP was never vendored, so all fifteen HyperFrames renders depended on a live CDN (54); the ffmpeg concat list used relative paths, which breaks every multi-chunk narration and so every episode (43); the pronunciation gate scored tokens instead of words and fed 44.1 kHz audio to a 16 kHz-only binary, so it could never have run (44); the documented Manim safe area is 210 px looser than the shipped code, so anything laid out to the docs fails its own linter (51); and `publish.py` could not read the `chapters.json` the render stage writes (63).

The one that is not a bug but a contradiction: the script stage's 1,500-2,100 word band and the render stage's 720 s target cannot both be satisfied at the voice's measured 3.69 words per second (42, 48). A script that passes stage 05 produces an episode that fails stage 10. That is why the long-form lint failure above is left standing rather than waived.

What could not be tested here remains: the Spark, the paid APIs, the cloud routine environment, and the Telegram round trip.

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

| 33 | render pre-flight | blocker | **Manim was never installed and both Shorts need it.** The Ornith storyboard assigns two scenes to `manim` and the Unsloth one four. `skills/render-shorts/setup.md` documents a venv at `skills/render-shorts/manim/.venv`; nobody had run it, so the first Manim scene of the render would have failed | **fixed** |
| 34 | long-form 06 | quality | **The two scenes that most need text render none.** `TitleCard.tsx:20` and `EndCard.tsx:18` pass `lowerThird={false}`, and `SceneFrame.tsx:136` gates all on-screen text behind it. The outline's binding "6.19 GB on screen by 0:20" fails -- the digits first draw at s03, ~34 s in -- and the payoff decision rule at beat 5.10 is spoken over a card that types nothing | open |
| 35 | long-form 06 | friction | `ComparisonTable.tsx` caps at 4 columns and 6 rows; the outline specified six columns. The outline stage has no visibility into renderer capacity, so it can specify a table that cannot be drawn and nothing says so until the spec silently truncates | open |
| 36 | long-form 06 | friction | **The verify rule and the card scene types are in tension.** Narration must concatenate back byte for byte and every scene's narration must be non-empty, so a chapter card has to carry its whole beat. The five cards run 13.6-16.8 s against the library's 4-15 s guidance | open |
| 37 | long-form 06 | quality | **Finding 31 recurring one stage down.** Three `chart` beats were downgraded to `diagram`, `stat-callout` and `comparison-table` because those findings are published as orderings, not scores, and inventing `series.values` would fabricate a measurement. Two agents, two stages, same unforced refusal -- and still no gate behind it | working as designed |
| 38 | hub notes | friction | **No stage fills the Artifacts block.** After seven long-form and five Shorts stages, every hub note still read "(filled by stage 03)". Frontmatter updated correctly because the audits and `hub-note.schema.json` check frontmatter; nothing checks the body, which is the surface a human opens in Obsidian | **fixed** |
| 39 | long-form 05 | quality | The "nothing here was measured by us" beat lands at ~0:16, over a card that draws no text, in the window where long-form retention is decided. Editorially right, structurally three disadvantages on one beat. A reviewer call, not a gate | open |
| 40 | 07 package | quality | **The SEO rubric cannot fail this package.** It scored 100/100 honestly and the score carries no information: one row scores the script's promise and calls it packaging (missing finding 34 entirely), another asks stage 07 to certify pixel dimensions of stills stage 10 has not rendered. Self-scored, with no fresh-context reader, unlike the script stage | open |
| 41 | tooling | friction | **`git add -A` commits other agents' in-progress work.** I swept a running agent's half-finished voice shim into an unrelated commit. `tools/git-sync.sh` does the same `add -A` in production, and the repo root is a live Obsidian vault the user hand-edits, so a routine firing mid-edit will commit and push a half-written note | open |
| 42 | 09 voice | quality | **The episode-length target rests on a constant nobody measured, and it is 41% off.** Kokoro `am_eric` measured at 4.22 wps against the assumed 2.9; the outline targets 2.5. The same 1,838-word script is 7:15 or 12:15 depending on which file you believe. The render re-times from captions so it still renders, but every upstream length target is wrong | open |
| 43 | 09 voice | blocker | **`concat_wavs` wrote relative paths into the ffmpeg concat list**, which ffmpeg resolves against the list file's directory, so every relative `--out` doubled the path and failed. Shared code path, so ElevenLabs would have hit it on any narration needing more than one chunk -- i.e. every episode | **fixed** |
| 44 | 09 voice | blocker | **The pronunciation gate measured tokens, not words, and could never have run.** `-ml 1` without `-sow` split `petaflop` into `pet af l op`, over-reporting WER by 3.4x (0.1038 vs 0.0309); it also fed 44.1 kHz audio to a 16 kHz-only binary. Both fixed; local mode now warns rather than blocks, since the true 0.0309 is all `base.en` homophones | **fixed** |
| 45 | 10 render | quality | **The lower third overlaps the quote attribution.** `SceneFrame.tsx:70` raises the lower third by `CAPTION_BAND_PX` (110) when captions are on; `Quote.tsx:41` fixes the attribution at +150. 40 px apart, both drawing taller text. Triggers precisely when the feature is used as intended | open |
| 46 | 10 render | note | 15 of 44 scenes set `captions_on`, so **36% of the episode carries burned-in captions**. This follows `scene-library.md:24` and the SRT sidecar ships alongside, so it is a deliberate rule -- but muted autoplay is how a small channel gets watched, so it deserves an explicit decision rather than an inherited default | reviewer call |
| 47 | 10 render | quality | **Finding 34 measured against real audio.** The hook's numbers are spoken at 0:03 and first drawn at 0:22 (`s01` title-card 0-10.6 s draws no text, `s02` quote 10.6-22.0 s, `s03` first digits). Better than the 34 s the estimates implied, still twenty-two seconds of the thumbnail's promise being undrawn | open |
| 48 | 10 render | blocker | **The episode renders and fails its own release gate.** 493.4 s against a 648-792 s window; every other lint check passes. The script stage's 1,500-2,100 word band and the render stage's 720 s target were set independently and never reconciled: at the measured 3.69 wps a script that passes stage 05 cannot produce an episode that passes stage 10 | open |
| 49 | 10 render | note | **The scene library holds up at full resolution.** Tables, charts with labelled axes, kinetic text, chapter headers, progress bar and word-timed captions all render correctly in brand colours. Minor: chart y-axis auto-scale leaves half the plot empty, and a chart label rounds 6.19 to 6.2 while the narration says 6.19 | working as designed |
| 50 | 07 render | note | **Both Shorts pilots published clean on attempt 2**, 0 linter violations each. Rendering costs under 17 s of compute per scene; each scene took ~13 min end to end, almost all of it reading rule files and working around findings 51-55. The cost of a scene is comprehension, not computation | working as designed |
| 51 | 07 render | blocker | **The documented Manim safe area is not the one in the code.** Docs say 900x1160 / `SAFE_Y_MIN -3.7778`; shipped `blai_layout.py` uses 870x950 / `-2.2222`. Laying out to the documented value puts content 210 px into the caption band and fails `safe_zone_check --scene`. Stale numbers survive in two rule files and in the module's own inline comments | open |
| 52 | 07 render | quality | **The documented reference scene is the wrong style pack.** `SETUP-NOTES.md` and `styles/signal.md` both call `index.html` the signal hello-world; it is a finished axon-pack scene, and the `hello.mp4` beside it does not exist. A worker following the docs silently produces the wrong pack, and nothing linted would catch it | open |
| 53 | 07 render | quality | **The pack's own snippet fails `hyperframes inspect`, and `inspect` is not in the verify list.** Masked text rises trip `clipped_text`/`text_box_overflow`; root-caused into the CLI's `isVisibleElement()` opacity-0.2 cutoff. Fix: start opacity >= 0.2 plus `data-layout-allow-overflow`. `lint` passes through all of it. Also `data-layout-bleed` does not exist in pinned 0.7.31 | open |
| 54 | 07 render | blocker | **GSAP was never vendored, so all 15 HyperFrames renders depended on a live CDN fetch** -- on a stack meant to run unattended on a Spark. `rules/hyperframes-1.md` already said where the copy belonged. Vendored 3.14.2 there. Still open: `package.json` scripts call `npx --yes` and bypass the lockfile pin | **fixed** |
| 55 | 07 render | quality | **Two silent Manim degradations.** `mob_class=Text` still yields serif digits, because `DecimalNumber` calls `mob_class(string)` with no kwargs -- bind font/weight with `functools.partial` first. And non-frame-aligned `run_time`s inflate duration, since Manim emits `ceil(run_time*fps)` per animation and the rounding accumulates | open |
| 56 | 04 script | quality | **Finding 42 reaches the Shorts briefs.** Scenes came in 9-38% shorter than `est_duration_s`, and briefs schedule beats by wall clock, so beats land after their scene ends (s1's 4 s beat in a 3.16 s scene). Briefs should specify beats by narration phrase, not by second -- phrase timing survives re-timing | open |
| 57 | 07 render | note | **Both Shorts assembled, every gate passes.** Ornith 30.13 s / -14.0 LUFS / loop 0.956; Unsloth 74.50 s / -14.1 LUFS / loop 0.791. 15 of 15 scenes published, none hit the 5-attempt limit, worst duration delta +0.030 s. No music by design | working as designed |
| 58 | 07 render | quality | **Every pack's shipped body class breaks the 64 px minimum text height.** `signal .label` 40 px, `terminal .term-text` 40 px, `terminal .label` 36 px. A worker who uses the pack's own class fails the brand rule by following the pack. Three workers hit it independently and all overrode | open |
| 59 | 07 render | quality | **Three undocumented HyperFrames audit traps.** `terminal.css`'s `.cursor` silently beats `.accent` on cascade order; `data-layout-allow-occlusion` must sit on the occluded text, not the coverer; `inspect` samples only 9 timeline points by default and catches mid-animation defects by luck. Also `styles/terminal.md` specifies a scramble-decode the pack does not ship | open |
| 60 | 07 render | quality | **Two more silent Manim failures.** `Scene.remove()` does not extract families in CE 0.20.1, so removing a VGroup is a no-op when children were added by `play()`. And `Blink` sums children's run_times in float, so whole-frame arithmetic still ceils off by one -- finding 55's rule is necessary but not sufficient | open |
| 61 | 04 script | quality | **The storyboard stage writes briefs the format rules forbid** -- 3 of 15 scenes: a slide through the UI margin, `on_screen_text` carrying 12 words against an 8-word cap, and rounded pills in a pack that bans them. Every worker substituted correctly, but the stage has no visibility into the scene rules or pack constraints it writes against | open |
| 62 | process | note | **The worker briefing I wrote mid-run was wrong twice and the workers caught it.** The YAVG stillness test false-positives on the frame-250 GOP keyframe (any scene over 8.33 s); the 0.2 opacity floor is mask-specific and produces a visible ghost on unmasked elements. Both corrected mid-flight. Same failure mode as findings 51-52, in fresh documentation | working as designed |
| 63 | 11 publish | blocker | **`publish.py --chapters` could not read the `chapters.json` the render stage writes.** Render emits `timestamp`, publish read `time`; and past that guard it assigned the render's richer shape into a manifest whose schema wants `{time,label}` only, so a one-line fix would have moved the error not removed it. Invisible to every unit check -- both files are individually valid | **fixed** |
| 64 | 11 publish | quality | **The composed description put its hashtags in the middle.** `publish.py` strips the estimated chapter lines from their correct position and `compose_description` re-appends the measured block past the hashtags already in the string. `titles-descriptions.md` wants hashtags last | **fixed** |
| 65 | 11 publish | quality | **The manifest thumbnail path resolves against the package note, but the stills live in the build dir.** Three valid 1280x720 thumbnails exist and the upload proceeds silently without one. A long-form episode publishing with no custom thumbnail should be an error, not a log line | open |
| 66 | 11 publish | note | **Publish dry-runs are otherwise correct on all three videos.** Privacy, notify, kids and synthetic flags all right per format; Shorts drew an 18:00 CT slot and the episode the next 09:00 CT, exactly per `publish-timing.md`; the stale `publish_slot_hint` was caught rather than scheduled into the past | working as designed |

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

### 33. A documented prerequisite that nobody executed (fixed)

Caught by pre-flighting the render stack instead of discovering it mid-render. `python3 -c "import manim"` failed everywhere on this machine except v1's own venv at `BLAI_Animator/render/manim/.venv`. The ported skill shipped the Manim scene code, the fonts, the pack helpers and a setup document, and no environment to run any of it in.

It would have failed on the first Manim scene of the first render, roughly ten minutes into Phase 4, after the voice stage had already succeeded.

Fixed by running exactly what `setup.md` prescribes: `uv venv --python 3.12 .venv && uv pip install --python .venv manim==0.20.1`. Eight seconds, because uv, python3.12, cairo and pango were all already present. The documented smoke render then produced 540x960 at 15 fps, 4.93 s, in 1.5 s of wall clock, and the ported `blai_layout` and `blai_packs` helpers import cleanly against it. `.gitignore` already covers `.venv/` and `skills/render-shorts/**/media/`, so nothing from this leaks into the repo.

The general lesson is worth more than the fix: the ICM validator checks that a tool has a setup guide, not that the guide was ever run. Every skill with a `setup.md` is a prerequisite nobody has verified until something renders. A cheap `tools/preflight.py` that runs each skill's documented verification command and reports what is missing would have caught this in seconds, and would catch the equivalent gap on the Spark before the first cloud-triggered build rather than after it.

### 34. The two scenes that most need text are the two that render none (open)

`TitleCard.tsx:20` and `EndCard.tsx:18` both pass `lowerThird={false}` to `SceneFrame`, and `SceneFrame.tsx:136` gates all on-screen text behind that flag. So a title card and an end card draw no `on_screen_text` at all, whatever the spec puts there.

Both ends of this episode are damaged by it:

- **The hook.** Beat 1.1 is the contradiction the whole episode hangs on -- twenty-seven billion parameters in a 6.19 GB file -- and it is also thumbnail concept 1. The outline made "6.19 GB on screen by 0:20" a binding requirement. It fails: beat 1.1 is `s01`, `s01` must be the title card, and the digits first render at `s03`, about 34 seconds in. A viewer who clicked the thumbnail for those two numbers does not see them again for half a minute.
- **The payoff.** Beat 5.10 is the decision rule, the one line a viewer would pause and screenshot. `end-card` draws nothing, so it is spoken and gone.

The script and spec are both innocent here; the spec author flagged both and could not route around them, because the chapter/card scene types are the only ones allowed at those positions.

Fix: give `TitleCard` a subtitle slot and `EndCard` a persistent rule line, or drop the `lowerThird={false}` override on both and let the layout decide. This is a render-library change, roughly one prop each.

### 35. The comparison table caps below what the outline asked for (open)

`ComparisonTable.tsx` is built for 4 columns and 6 rows. The winning outline specified a six-column running table. The spec correctly clipped to Contender | File size | Fits | Quality, repeated at `s22`, `s24`, `s34` and `s36` with rows accumulating and only the Quality cell changing -- which preserves the discipline the outline was actually protecting, so the damage is small.

Worth recording anyway, because the outline stage has no visibility into renderer capacity. It can specify a table the renderer cannot draw and nothing says so until the spec stage quietly truncates it. The scene library's caps belong in the outline stage's references.

### 36. The verify rule and the card scene types pull against each other (open)

Stage 06's binding check is that the scenes' narration concatenates back to the narration file byte for byte -- the guarantee that no beat is dropped, merged or invented. The schema also requires every scene's `narration` to be non-empty. Together they mean a chapter card cannot carry a short card-only line: it must carry the whole beat that sits at that position.

Result: the five chapter and title cards run 13.6 to 16.8 seconds each, against the scene library's 4-15 second guidance for cards. Nothing is broken -- the binding 45 second cap is nowhere near -- but a 16 second chapter card is a 16 second pause in an episode, five times.

The tension is structural, not a bug in either rule. The honest fix is for the script stage to write short card lines into the narration file itself, so the cards have their own text to carry and the concat check still holds.

### 37. The spec refused to draw charts it had no numbers for (working as designed)

Three beats carried a `chart` hint. The spec author downgraded all three -- to `diagram`, `stat-callout` and `comparison-table` -- with the reason that those findings are published as orderings and directions, not as scores. A `chart` scene needs `series.values`; inventing plausible heights to draw a curve or a bar swap would have fabricated a measurement.

This is finding 31 recurring at the next stage down, and again nothing forced it. Two different agents, at two different stages, independently refused to let a visual assert something the sources do not support. The pattern is worth protecting: it is the difference between a channel whose numbers are real and one whose numbers look real.

Same structural gap as 31, though. Nothing in the schema or the renderer would have stopped a fabricated `series.values`. The rule lives in the agents' judgement, not in a gate.

### 38. No stage fills the hub note's Artifacts block (fixed)

Every stage contract's Process ends with "Update the hub", and the Outputs table names the Artifacts link. After seven long-form stages and five Shorts stages, every hub note still read:

```
- Research: (filled by stage 03)
- Script: (filled by stage 04)
```

Stages did update the frontmatter -- `status` moved correctly through `idea`, `researched`, `scripted` -- because the audit tables check frontmatter fields and `check_outputs.py` validates them against `hub-note.schema.json`. Nothing checks the note's body, so the placeholders survived every stage in both workspaces.

This matters more than it looks. The hub note is the human surface: the thing that opens in Obsidian on a phone when the Telegram card says a video is ready for review. Its navigation section was a list of unfulfilled promises pointing at nothing.

Fixed for the long-form run by filling all seven links. The general fix is a `check_outputs.py` rule that fails any committed hub note containing `(filled by stage`, for a stage whose output actually exists on disk -- three lines, and it makes the contract self-enforcing rather than aspirational.

### 39. The honesty beat sits in the most fragile window (open)

Beat 1.2 -- "Nothing in this episode was measured by us" -- lands at roughly 0:16, over a card that draws no text (finding 34). It is editorially the right call and I would not cut it. But putting the deflating beat second, in the window where long-form retention is decided, and giving it no visual, is three disadvantages stacked on one beat.

The alternative is not to hide it: move it after the first real payoff, so a viewer has been given something before being told what the episode cannot do. Worth putting to the reviewer rather than deciding in a gate.

### 40. The SEO rubric cannot fail this package (open)

Stage 07 scored 100 of 100. It is an honest score by the rubric's own rows -- I checked each one mechanically -- and it is close to worthless, because none of the eight rows tests anything that was actually wrong.

Two specific defects:

- **A row that scores the wrong thing.** "First 30 s carry the promise" passes because the promise is in the narration. Finding 34 is that the first 34 seconds render no text at all. The rubric asks about the script and calls it a packaging check.
- **A row that cannot be evaluated at all.** The thumbnail row asks stage 07 to certify `>= 1280x720` and `<= 2 MB` for stills that stage 10 has not created yet. Stage 07 can only score the concepts and assume the rest, which means the row is unfalsifiable at the moment it is scored.

Both Shorts scored 92 and 95, this episode 100, and the spread carries no information. The rubric is also self-scored by the agent that wrote the package, with no adversarial pass -- unlike the script stage, which gets a fresh-context judge.

Fix, in order of value: move the pixel conditions to stage 10 where the files exist; add a row that fails when a beat's on-screen text does not render (checkable from the spec plus the scene library); and give packaging the same fresh-context second reader the script gets.

### 41. `git add -A` commits whatever anyone else is mid-edit (open)

I committed `86e2353` ("Long-form stage 07 package; findings 34-40") while a background agent was part-way through the voice shim, and swept its entire in-progress working tree into my commit. The agent noticed and reported it: it never ran `git commit`, and the commit message describes maybe a third of what the commit contains. Nothing was lost, and the branch is a test branch, but the history now lies about what changed when.

The same pattern is in production code. `tools/git-sync.sh` runs `git add -A` on the whole repo, and its own header says it exists so that "two cloud routines and the Spark build agent can all push the same morning". Separate checkouts make that safe between hosts. What it is not safe against is the thing that makes this repo unusual: **the repo root is a live Obsidian vault the user edits by hand.** A routine firing at 09:00 while a half-written note sits in the vault will commit that note, under the pipeline's message, and push it.

Fix: give `git-sync.sh` an explicit path list from the caller (`git add "$@"`) and have the stage runner pass the directories that stage owns. It is a small change and it turns a whole-tree commit into a scoped one.

### 42. The episode length target rests on an unmeasured constant, and the measurement disagrees by 41 % (open)

The voice shim measured Kokoro `am_eric` at **4.22 words per second** over the 259-word golden narration: 61.373 s of audio, one chunk, ffprobe-confirmed. The pipeline had been assuming 2.9.

Three different rates are baked into three different files, and none of them was measured until today:

| Where | Rate | This 1,838-word script becomes |
|---|---|---|
| Outline chapter targets ("150 words per minute") | 2.50 | 12:15 |
| `skills/script-gates/voice.config.json` `wps` | 2.90 | 10:33 |
| v1's own measured `am_eric` | 3.67 | 8:20 |
| **Measured here today** | **4.22** | **7:15** |

So the episode written to be twelve minutes will render at about seven and a quarter. The render itself is fine -- `render_longform.py` re-times every scene from the caption words and only falls back to `est_duration_s` when captions are missing (line 447), which is the right design and is why this is a planning defect rather than a broken render. What it breaks is everything upstream: the outline's per-chapter second targets, the script stage's word bands, the spec's 722 s total, and the chapter times in the package.

Two caveats, both from the agent that measured it. This is the *Kokoro* rate, not the ElevenLabs clone that will actually ship, and `voice.config.json` describes the clone, so it was correctly left alone. And it is one voice on one text: v1 measured the same voice at 3.67, so text choice moves this by about 15 %.

The durable fix is already in: every run now writes `words_per_second` into `voice.json`, so the number accumulates from real renders instead of being guessed once. What still needs deciding, once the clone exists, is which rate the *script* stage should target -- and that decision belongs to the user, because it is really a question about how fast the channel should talk.

### 43. A path bug in the shared voice path that would have hit ElevenLabs too (fixed)

`concat_wavs` wrote relative paths into the ffmpeg concat list. ffmpeg resolves entries in a concat list against the list file's own directory, so any relative `--out` doubled the path and the concatenation failed. This sits in the shared code path, not the Kokoro branch, so the ElevenLabs run would have hit it the first time a narration was long enough to need more than one chunk -- which for a twelve-minute episode is always. Fixed with absolute paths.

Worth noting how it was found: only by running the thing. No gate, schema or review would have caught a relative-path assumption inside an ffmpeg helper.

### 44. The pronunciation gate was measuring tokens, not words, and could never have run (fixed)

Two compounding bugs in `qa_transcribe.py`, the Whisper check that is supposed to catch the voice mispronouncing a model name:

1. It passed `-ml 1` without `-sow`, so whisper.cpp returned **tokens** rather than words: `petaflop` came back as `pet af l op`. Every multi-syllable technical term -- which is most of what this channel says -- was scored as four errors. Measured WER on the golden take was **0.1038**; with `-sow` the same audio measures **0.0309**. The gate has been over-reporting error by 3.4x.
2. It fed 44.1 kHz audio to a whisper.cpp build that only reads 16 kHz. That path could never have produced a transcript at all.

Both fixed. The real WER of 0.0309 sits just over the 0.03 gate, and all eight mismatches are `base.en` homophones (`buy`/`by`, `Mac's`/`max`, `there`/`their`, `Spark's`/`sparks`) with no synthesis error among them. So local mode warns and journals rather than blocking -- otherwise no local run could reach the render stage -- and both voice CONTEXT files now record that the local check is a smoke test, not the pronunciation gate.

The general shape here is the same as finding 33: a documented quality gate that had never been executed, and was broken in two independent ways when it finally was.

### 45. The lower third and the quote attribution land on top of each other (open)

Visible in the first draft render, at 18 s. The quote scene's source line ("Build Local AI") is struck through by the lower third's text ("Not measured here. Every source named.").

The arithmetic, and it is exact:

- `SceneFrame.tsx:70` -- `const bottom = 1080 - SAFE.bottom + (raised ? CAPTION_BAND_PX : 0)`, and `CAPTION_BAND_PX = 110`.
- `Quote.tsx:41` -- attribution at `bottom: 1080 - SAFE.bottom + 150`.

So the two sit 40 px apart while both draw text taller than 40 px. And the lower third only raises when `captions_on` is true, which for a quote scene citing a source is exactly the case you would set it. The collision is not an edge case; it is what happens when the feature is used as intended.

Fix: either raise the quote attribution by `CAPTION_BAND_PX` too when captions are on, or give `Quote` its own attribution slot above the lower-third band. One line either way.

### 46. Two thirds of the episode carries no burned-in captions, by design (reviewer call)

15 of 44 scenes set `data.captions_on`, covering **177 s of 493 s -- 36 %**. The other 64 % renders with no on-screen words beyond its own lower third.

This is not a defect: `skills/render-longform/rules/scene-library.md:24` says to use captions "for scenes that define a term or cite a number, not everywhere; the SRT sidecar carries the full text", and the spec author followed that rule selectively and correctly. `captions.srt` (463 cues) ships alongside for YouTube's own caption track.

It is still worth a decision from the reviewer rather than a default, because the two things are not equivalent. The SRT covers accessibility and anyone who turns CC on. Burned-in captions are a retention device for muted autoplay, and muted autoplay is a large share of how a small channel gets watched. The current split means a viewer scrolling past with sound off sees words for about a third of the episode.

Recorded here as a question, not a change: the rule may well be right for a twelve-minute explainer where the visuals carry the argument. It should be an explicit choice, not an inherited default.

### 47. Finding 34, measured (open)

The estimated timings put the first on-screen digits at about 34 s. Against real audio it is better than that, and still bad:

| | Time | What is on screen |
|---|---|---|
| `s01` title-card | 0.0 - 10.6 s | title and series chip only; no numbers, no lower third (`lowerThird={false}`) |
| `s02` quote | 10.6 - 22.0 s | the "nothing was measured by us" card |
| `s03` kinetic-text | 22.0 - 34.6 s | **first appearance of the hook's numbers** |

So the contradiction the thumbnail sells -- 27 billion parameters, 6.19 GB -- is spoken at 0:03 and first drawn at 0:22. A viewer who clicked for those two numbers waits twenty-two seconds to see them.

The rest of the frame is sound: the title card renders correctly in brand colours with the series chip and wordmark, kinetic-text emphasises its key phrase in amber and reads cleanly, and the chapter header and progress bar are both present and correct. The problem is confined to what `TitleCard` is allowed to draw.

### 48. The episode renders, and fails its own release gate on duration (open)

The first full long-form render completed: **493.4 s, 1920x1080, h264, yuv420p, 30 fps, AAC 48 kHz, 27.4 MB, 386.9 s of wall clock** on this Mac. Every lint check passed except one.

```
FAIL duration: 493.4 (expected 648 to 792 s (target 720 +/- 10 %))
```

Passing: exists, codec, resolution, fps, pix_fmt, color_range (`tv`, so `--color-space=bt709` did apply), audio_stream, audio_codec, audio_rate. Failing: duration, by 155 seconds.

This is finding 42 arriving at the gate, and it is the whole chain in one line. The outline set chapter targets at 150 words per minute. The script wrote 1,838 words to fill twelve minutes at that rate. The voice actually runs at 3.69 words per second. The episode came out at 8:13, and `lint_longform.py --target-s 720` correctly refused it.

Two things follow.

**The gate works.** It caught a real inconsistency on the first episode that ever reached it, which is exactly what it is for. Nothing here argues for loosening it.

**Every long-form episode will fail it until the constant is fixed.** To land inside the 648-792 s window at 3.69 wps the script needs roughly **2,400 to 2,900 words**, against the 1,500-2,100 band the script stage currently enforces. So the script gate and the render gate are asking for incompatible things: a script that passes stage 05 cannot produce an episode that passes stage 10. The bands were set independently and never reconciled against a measured voice.

Fix, once the ElevenLabs clone exists and its rate is measured: derive the script stage's word band from `voice.config.json` rather than hard-coding it, so the two gates move together. Until then this failure is expected and should be journalled rather than treated as a render defect.

### 49. What the full render looks like (working as designed)

Worth recording what came out right, because most of it did. At 1920x1080 the scene library reads well:

- **comparison-table** -- Unsloth's file listing with FILE/SIZE headers, `UD-IQ1_S 6.19 GB` and `UD-Q6_K_XL 25.3 GB`, chapter header, lower third carrying the repository name as its source line.
- **chart** -- proper GB axis with gridlines and labelled ticks, two amber bars with value labels, category labels underneath, a legend, and the publisher named in the lower third.
- **kinetic-text** -- key phrase emphasised in amber, fully legible, good rhythm.
- **end-card** -- wordmark, handle and a next-episode line, cleanly set.
- Chapter header and chapter progress bar present and correct throughout; captions word-timed with the active word in amber.

Two small composition notes, neither worth a fix on its own: the chart's y-axis tops out at 50 for a 25.3 maximum, so the upper half is empty, and a two-row comparison table leaves a large gap between the table and the lower third. Both are auto-scaling questions, not defects.

One number to watch: the chart draws `6.2` where the lower third and the narration both say `6.19`. The brand rule is that a number on screen is also spoken. A one-decimal bar label against a two-decimal spoken figure is a small breach of it, and it will recur wherever a chart label rounds.

### 50. Both Shorts pilots published, and both spent most of their effort on wrong documentation (open)

The two pilot scenes -- s1 HyperFrames and s4 Manim, Ornith Short, `signal` pack -- both published clean on their second attempt with zero render errors:

| | duration | assigned | linters | render wall time |
|---|---|---|---|---|
| s1 hyperframes | 3.1667 s | 3.16 | `lint_video` 0/0, `safe_zone --scene` 0 violations (max luma 13 vs 140 threshold), `hyperframes lint`/`validate`/`inspect` all clean | 8.1 s draft + 8.3 s final |
| s4 manim | 6.9660 s | 6.96 | `lint_video` 0/0, `safe_zone --scene` 0 violations at `--stills 24` (max luma 15 vs 140) | 2.6 s draft + 6.8 s final |

Rendering is nearly free -- **under 17 seconds of compute per scene**. Each scene took roughly 13 minutes end to end, essentially all of it reading five rule files and working around the four documentation defects below. That ratio is the finding: the cost of a scene is comprehension, not computation, and most of the comprehension cost was avoidable.

Findings 51 to 57 are what they hit. All of them are now in `.local-builds/WORKER-BRIEFING.md`, which the remaining thirteen workers read after the rule files, so the same time is not spent fourteen more times.

### 51. The Manim safe area in the docs is not the safe area in the code (open)

The worst of the four, because it fails silently into a linter error rather than a crash.

| | `scene-agent.md` and `SETUP-NOTES.md` | shipped `blai_layout.py` |
|---|---|---|
| safe area | 900 x 1160 px | **870 x 950 px** |
| margins | left 60, right 120, top 310, bottom 450 | left **90**, right 120, top 310, bottom **660** |
| `SAFE_Y_MIN` | -3.7778 | **-2.2222** |
| `SAFE_CENTER` | (-0.2222, +0.5185) | **(-0.1111, +1.2963)** |

The code is the correct and stricter authority -- its own module docstring explains that the bottom margin deliberately absorbs the caption band and that left went 60 to 90. But the stale numbers survive in two rule files *and* in `blai_layout.py`'s own inline comments beside each constant. Anyone laying out to the documented `SAFE_Y_MIN` puts content 210 px into the caption band and fails `safe_zone_check.py --scene`.

Fix: correct the px-to-unit table in `SETUP-NOTES.md`, the "Safe area 900 x 1160" line in `scene-agent.md`, and the inline comments. Better still, have those docs quote the constants rather than restate them.

### 52. The documented reference scene is the wrong style pack (open)

`SETUP-NOTES.md` ("Reference artifacts") and `styles/signal.md` ("Implementation") both say `hyperframes/index.html` is the 5-second signal hello-world with `hello.mp4` beside it. Neither is true: `index.html` is a finished **axon-pack** scene from the DGX Spark video (9.71 s, loading `packs/axon.css`), and `hello.mp4` does not exist in that directory.

A worker who follows the docs and copies `index.html` as a starting point silently produces a scene in the wrong style pack. Nothing would catch it -- `style_pack` is checked by humans, not a linter -- so it could ship. The real reference is `packs/<pack>-snippet.html`.

### 53. The pack's own snippet fails the audit, and the check that catches it is not in the verify list (open)

`packs/signal-snippet.html` technique #4 does `tl.from("#stat-row", {y: 140, opacity: 0})` inside an `overflow:hidden` wrapper -- the documented way to do a text rise. That exact combination produces `clipped_text` and `text_box_overflow` **errors** plus a `container_overflow` warning.

The pilot traced it into the CLI source. `isVisibleElement()` drops any element whose opacity chain is below 0.2; once the text is dropped, `hasOwnTextCandidate()` promotes the `.line` **mask** to a text element; and `clippedTextIssue()` has no allow-overflow guard, so `data-layout-allow-overflow` cannot suppress it. Verified fix: keep the tween's start opacity at or above 0.2 (0.25 is visually identical, the text is behind a mask anyway) **and** put `data-layout-allow-overflow` on the wrapper. Probes: opacity 0 + allow-overflow = 1 error; pure rise, no opacity = 0 errors 2 warnings; opacity 0.25 + allow-overflow = clean.

The compounding problem: **`hyperframes lint` passes through all of it.** Only `inspect` catches it, and `inspect` appears in neither `scene-agent.md` rule 8 nor the `hyperframes-1.md` self-check, both of which ask only for `lint`. It is fast and it is the only thing that catches masked-text defects. It should be in both lists.

Related, same family: `data-layout-bleed="true"` is recommended by `vendor/hyperframes-core/references/data-attributes.md` as the narrow-scope opt-out and **does not exist in the pinned 0.7.31** -- the vendored docs are ahead of the pinned CLI, which knows only `data-layout-ignore`, `data-layout-check='ignore'` and `data-layout-allow-overflow`.

### 54. GSAP was a single point of failure for fifteen renders (fixed)

`rules/hyperframes-1.md` says GSAP 3.14.2 loads from jsdelivr "so the first render needs network **or a vendored copy next to `packs/vendor/rough.js`**". There was no vendored copy: `packs/vendor/` held only `rough.js`, and `gsap` was absent from `node_modules`. Every HyperFrames scene in both Shorts depended on a live CDN fetch at render time, with no fallback, on a stack whose whole point is to run unattended on a Spark.

Fixed: `gsap.min.js` 3.14.2 (72,779 bytes, verified header) is now vendored at `packs/vendor/gsap.min.js`, which is exactly where the rule file already said it should be.

Related and not yet fixed: `package.json`'s `check`, `render` and `dev` scripts all invoke `npx --yes hyperframes@0.7.31`, which re-resolves from the network instead of using the pinned local devDependency. `./node_modules/.bin/hyperframes` -- which `SETUP-NOTES.md` itself calls "THE verified command" -- is faster and cannot drift. The scripts should use it.

### 55. Two Manim traps that produce plausible-looking wrong output (open)

Neither raises an error; both silently degrade the frame.

**Serif digits.** `manim-1.md` whitelists `DecimalNumber`/`Integer` "for count-ups only with `mob_class=Text`". Necessary but not sufficient: `DecimalNumber._set_submobjects_from_number` calls `mob_class(string)` with **no kwargs**, so no font or weight ever reaches the digits and Pango falls back to its default serif face -- the exact failure the same rule file warns about two bullets earlier for raw `Text()`. The fix is to bind them first: `functools.partial(Text, font=BRAND_FONT, weight=BOLD)`. `color=` does propagate; `edge_to_fix=ORIGIN` is also needed for a centred count-up, since the default `LEFT` pins the left edge and the number drifts off-centre as its digit count grows. Worth promoting into `blai_layout.py` as a `brand_number()` helper so nobody has to know this.

**Duration inflation.** Manim emits `ceil(run_time * fps)` frames **per animation**, so every segment rounds up independently and the error accumulates. The pilot's human-round times summed to exactly 6.96 s and rendered at 7.066 s -- inside the 0.15 s tolerance by 0.04 s, and a scene with more cuts would miss outright. The fix is to express every `run_time` and `wait` as a whole number of frames chosen to sum to the target. Note the assigned duration may not even be representable: 6.96 s is 208.8 frames at 30 fps, so 209 is the nearest. This belongs in `manim-1.md` step 4; it is the difference between "usually fine" and deterministic.

### 56. Finding 42 reaches the Shorts briefs, and it costs beats (open)

The words-per-second error is not confined to long-form. Every Shorts scene brief was written against `est_duration_s`, and the narration came in 9 to 38 % shorter:

| Ornith | est | assigned | | Unsloth | est | assigned |
|---|---|---|---|---|---|---|
| s1 | 4.5 | 3.16 (-30%) | | s1 | 10.0 | 6.64 (-34%) |
| s2 | 5.5 | **3.41 (-38%)** | | s5 | 13.0 | 9.92 (-24%) |
| s4 | 8.0 | 6.96 (-13%) | | s6 | 8.0 | 5.32 (-34%) |

The concrete damage: briefs schedule beats by wall clock ("At 2s", "At 4s"), and those beats no longer exist. The s1 brief's 4-second beat -- the file glyph shrinking to a card slot -- cannot happen in a 3.16 s scene; the pilot dropped it. The s4 brief's clock runs 0/3/5/7 s against a 6.96 s scene, so its final beat would land after the scene ends; that pilot re-anchored every beat to the narration word timings instead, which is what scene-agent rule 6 asks for anyway.

So the storyboard stage is writing visual briefs in a unit (wall-clock seconds) that the voice stage then invalidates. The durable fix is for briefs to specify beats **by narration phrase**, not by second, since the phrase timing is what survives re-timing. That is a storyboard-format change, and it would also make the briefs read better.

Smaller, same root: several briefs specify "motion onset at 0.25s", but `hyperframes-1.md` forbids motion before frame 9 (t = 0.2667 s). Every such brief is 0.017 s inside the illegal zone. Either the boundary or the brief convention should move; right now they contradict for any brief that picks 0.25 as a round number.

### 57. Both Shorts assembled, every release gate passes (working as designed)

| | Ornith 1.5 9B | Unsloth LAN |
|---|---|---|
| Format | classic | smooth-explainer |
| Style pack | signal | terminal |
| Duration | 30.13 s (band 28-47) | 74.50 s (band 70-155) |
| Loudness | **-14.0 LUFS** | **-14.1 LUFS** |
| Video | 1080x1920 h264 yuv420p 30 fps | same |
| Audio | aac 48 kHz | same |
| Size | 3.2 MB | 5.2 MB |
| Scenes | 6 (4 HyperFrames, 2 Manim) | 9 (5 HyperFrames, 4 Manim) |
| `lint_video --final` | 0 violations, 0 warnings | 0 violations, 0 warnings |
| `safe_zone_check` | 0 violations | 0 violations |
| `loop_check` SSIM | **0.956** (threshold 0.5) | **0.791** |
| Captions | 101 words | 279 words |

**Fifteen scenes, fifteen published, none hit the five-attempt limit.** Every scene landed inside the +/-0.15 s tolerance; the worst was +0.030 s. Both Shorts carry the same honest assembly warning -- video total exceeds narration by about a second -- which is `scene_timing.py` giving the last scene its documented 1 s hold, not drift.

Neither Short has music: `assets/music/` is a deliberate manual step and the pipeline renders silent rather than pick a wrong mood. The Ornith cut fired both its sfx cues; the Unsloth storyboard asked for none.

### 58. The shipped pack CSS classes violate the brand's own minimum text height, in every pack tested (open)

Three separate workers on two packs hit this independently:

| Pack | Class | Ships at | Rule |
|---|---|---|---|
| signal | `.label` | 40 px | 64 px minimum at 1080 wide |
| terminal | `.term-text` | 40 px | same |
| terminal | `.label` | 36 px | same |

`scene-agent.md` and `shared/platform-specs.md` both require "minimum text height about 64 px at 1080 wide". **A worker who uses the pack's own body class for on-screen copy fails the rule by following the pack.** All three workers independently overrode to 62-78 px.

This is not a per-pack slip; it is every pack that has been exercised. Either the classes are sized for chrome rather than content and the docs should say so, or they are simply wrong. Worth checking the other five packs before they are used.

Related and measured, worth putting in the pack docs: JetBrains Mono's advance is 0.6 em, so at the 64 px floor each character costs 38.4 px and the 830 px safe width holds about **19 characters**. That constraint governs `terminal` far more than anything in its style file -- it is why a `split-compare` in this pack needs its minor-side word at seven characters or fewer, and why a three-node `timeline` with word labels is at the width limit.

### 59. Three more HyperFrames audit traps, none documented (open)

- **`terminal.css` has a silent cascade trap.** `.accent` and `.cursor` are both single-class selectors and `.accent` is declared first, so `class="cursor accent"` renders the block cursor phosphor-green and drops the amber with no warning. A draft shipped a green cursor beside an amber payoff before a still caught it. Needs higher specificity, or a note in `styles/terminal.md`.
- **`data-layout-allow-occlusion` must sit on the occluded TEXT element or an ancestor of it, never on the thing doing the covering.** Confirmed in the CLI source: `hasAllowOcclusionFlag()` is `element.closest("[data-layout-allow-occlusion]")` where `element` is the text. A worker put it on the strike bar and the error did not move. Same shape as the item-7 trap and belongs beside it.
- **`inspect` samples only 9 points on the timeline by default**, so it catches a mid-animation defect by luck. It accepts `--samples N`, `--at`, `--at-transitions` and `--strict`; `inspect --samples 40 --at-transitions --strict` cost about two seconds and covered 72 samples. That should be the standard invocation, not the bare command.

Also worth recording: `styles/terminal.md` specifies "a 200 ms scramble-decode on the incoming headline" as a signature technique, and **the pack ships no implementation of it** -- the snippet only demonstrates the typewriter. The obvious implementation reaches for `Math.random()`, which the seek-safety rules ban. One worker wrote a deterministic version (character `i` resolves at `p >= (i+1)/n`, glyph chosen by a pure function of tween progress) that should be folded into the snippet.

### 60. Two more silent Manim failures (open)

- **`Scene.remove()` does not extract mobject families in CE 0.20.1.** It calls `restructure_mobjects(..., extract_families=False)`, so `self.remove(some_vgroup)` is a **silent no-op** when the children were added individually by `play()`. A worker's first draft left an entire scene phase visible underneath the next one. The fix is to track the mobjects that actually reached the scene and remove them flat. `self.remove(*vgroup)` is also wrong for nested groups.
- **`Blink` breaks frame budgeting twice over.** It is a `Succession` that computes its own `run_time` internally, so it cannot be pinned to a whole frame count -- and its children's run_times sum in float, so `0.4 + 0.4 + 0.4` gives `1.2000000000000002` and `ceil(... * 30)` returns 37 frames, not 36. Two workers independently abandoned it and hand-cut the blink with `add`/`remove` between exact-frame waits, which is also more on-pack for `terminal`. Finding 55's whole-frame rule is necessary but not sufficient: it fails for any animation that sums its children.

One genuinely useful difference recorded: **HyperFrames rounds the frame count up once for the whole composition, not per animation.** So the accumulation problem is Manim-specific, and a HyperFrames scene's error is always bounded under one frame.

### 61. The storyboard stage keeps writing briefs the format rules forbid (open)

Finding 56 covered the clock. This is the other half, and it showed up three times in fifteen scenes:

- **"slides in from the right edge"** (Ornith s2) -- scene-agent rule 7 bans entrances through the UI margins.
- **`on_screen_text` carrying two full clauses** (Unsloth s1) -- both lines are six words, so honouring the brief puts twelve words on screen against an eight-word hard cap.
- **"three amber pills"** (Unsloth s3) -- the `terminal` pack bans rounded corners outside its window frame, and "amber stays the one accent" argues against three amber blocks plus an amber toggle in one frame.

Every worker substituted correctly and said so. But the storyboard stage has no visibility into the scene rules or the pack constraints it is writing against, so it will keep producing briefs that cannot be built as written. The cheap fix is to put the hard don'ts and the pack's own bans into the storyboard stage's references, so the brief is legal when it is written rather than repaired fifteen times downstream.

### 62. My own briefing was wrong twice, and the workers caught it (process note)

Worth recording honestly, because it is the same failure mode as findings 51 and 52 -- documentation drifting from what is true -- and it happened to documentation I wrote during this run.

- **The stillness metric.** I published "use YAVG with a ~0.05 threshold" from the pilots. A later worker found it false-positives on every scene longer than 8.33 s: x264 inserts an IDR at frame 250, which re-quantizes the whole frame and produces a diffuse YAVG spike at YMAX ~33, where real motion shows YMAX 150+. Corrected to require both statistics. Three running workers had scenes over 8.33 s when the correction landed.
- **The opacity floor.** I published the pilot's ">= 0.2 start opacity" fix without its scope. It is specific to text inside an `overflow:hidden` mask, where the audit promotes the mask to a text element. Applied to an **unmasked** element it produces a visible ghost, because `fromTo` renders its "from" state immediately -- a chip sitting at 0.25 opacity from frame 0 for the whole delay. No linter catches it; only a mid-scene still. Corrected and narrowed.

Both corrections came from workers testing the advice rather than trusting it, and one of them explicitly re-ran the pack default to check whether my precaution was even necessary (it was not). That is the behaviour worth keeping: the briefing was useful, and it was also wrong, and the way that got caught was people rendering stills instead of believing a document.

### 63. The two ends of the chapter handoff never agreed on a key name (fixed)

The long-form design says the render stage writes measured chapter times and `publish.py --chapters` swaps them into the description at upload. The first time those two programs were asked to talk to each other, they could not:

```
[publish] --chapters must be a non-empty list whose first entry is 00:00
```

`render_longform.py` writes `{number, label, scene, start_s, timestamp}`. `publish.py:366` read `measured[0].get("time")`. Neither is wrong on its own; nobody had ever run one against the other.

It was a **two-part** failure. Past the key-name guard, line 368 assigned the render's whole richer shape straight into `manifest["chapters"]`, which `publish-manifest.schema.json` requires to be `{time, label}` -- so the manifest would then have failed validation on the extra fields. A fix to only the guard would have moved the error, not removed it.

Fixed on the reader end: `publish.py` now accepts a list or a `{chapters: [...]}` wrapper, takes `time` or `timestamp`, and projects each entry down to `{time, label}` so the manifest still validates. The render's extra fields (`scene`, `start_s`) stay in `chapters.json` where they are useful for debugging.

This is the single most valuable thing the end-to-end run found on the publish side, because it is invisible to every unit check: both files are individually well-formed and schema-valid.

### 64. The description put its hashtags in the middle (fixed)

With chapters flowing, the composed description came out with the chapter block **after** the hashtags. `titles-descriptions.md` prescribes: body, chapters block, links, credits, "then 2-3 hashtags at the end."

Cause: `publish.py` strips the estimated chapter lines from wherever the package note had them (correctly placed, before the hashtags) and `compose_description` then *appends* the measured block to the end of the string -- past the hashtags that were already there.

Fixed: `compose_description` now splits off a trailing hashtag-only line, appends chapters and any related-video link above it, then puts the hashtags back last. Verified on all three: the long-form description ends with the five measured chapters followed by `#Qwen #LocalAI #GGUF`, and both Shorts still end with their hashtags.

### 65. The thumbnail path is relative to the wrong thing (open)

```
[publish] manifest thumbnail thumbnails/1.png not found next to the package note; continuing without it
```

The manifest carries `"thumbnail": "thumbnails/1.png"`, which is where `render_longform.py` actually writes them -- inside the **build directory**. `publish.py` resolves it relative to the **package note**, in `workspaces/long-form/stages/07-package/output/`. The stills exist and are valid (three, 1280x720, 0.05-0.07 MB), and the upload silently proceeds without a thumbnail.

Silently is the problem. A long-form episode publishing with no custom thumbnail is a significant loss, and the run continues with a log line rather than stopping. Two things needed: decide which directory the path is relative to (the build dir is the sane answer, since that is the only place the file exists), and make a missing thumbnail on a long-form upload an error rather than a warning.

### 66. Publish dry-runs are otherwise correct on all three videos (working as designed)

Everything else in the Blotato body matched the playbooks without intervention:

| | Ornith | Unsloth | Long-form |
|---|---|---|---|
| `privacyStatus` | public | public | **private** (the test-artifact setting held) |
| `shouldNotifySubscribers` | false | false | **true** (long-form default) |
| `isMadeForKids` | false | false | false |
| `containsSyntheticMedia` | false | false | false |
| Slot chosen | 2026-08-23 18:00 CT | 2026-08-23 18:00 CT | **2026-08-24 09:00 CT** |
| Description | 489 bytes | 724 bytes | 1,541 bytes |

The Shorts landed on an 18:00 CT slot and the episode on the next 09:00 CT, which is exactly what `publish-timing.md` specifies for each format. `publish.py` also noticed the Ornith package's `publish_slot_hint` was already in the past and said so before picking the next free slot rather than scheduling into history.

Both Shorts drew the same 18:00 slot, which is expected in dry-run: nothing is reserved because nothing is written. In a real run the first would set `publish_slot` on its hub note and the second would see it taken. Worth confirming once against a live run, but it is not evidence of a bug.
