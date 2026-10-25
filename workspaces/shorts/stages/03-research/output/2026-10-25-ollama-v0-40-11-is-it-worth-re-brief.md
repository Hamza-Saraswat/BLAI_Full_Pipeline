---
slug: 2026-10-25-ollama-v0-40-11-is-it-worth-re
stage: 03-research
topic: "Ollama v0.40.11: is it worth re-pulling your models?"
depth: standard
generated_at: 2026-10-25T11:52:27Z
sources: 10
hub: "[[videos/2026-10-25-ollama-v0-40-11-is-it-worth-re]]"
---

# Research brief: Ollama v0.40.11: is it worth re-pulling your models?

## Summary
The patch notes, not the version number, settle whether tonight involves a download: v0.40.11 shipped speech generation on macOS and the d3 decision-model family, one calendar day after v0.40.10, with no breaking changes flagged. The most arresting number is phonon:latest at 113MB -- the entire new speech capability downloads smaller than a photo album. The strongest concrete case is v0.40.2, where Ollama did change model formats and still upgraded models in the background with the original kept as a backup, forcing nobody to re-pull. What could not be verified: how widespread the "updates re-download your models" belief is (community pages returned 403) and any performance numbers for v0.40.11. No fetched sources conflict; the thin spot is that no official page states outright that updates leave models untouched -- that claim is assembled from where models are stored plus what each update mechanism replaces.

## Thesis
Ollama v0.40.11's patch notes settle the question: updating swaps the app and never your pulled models, so the only downloads worth your evening are the new ones -- phonon at 113MB and the d3 decision models.

## Explanation path
Establish what an update actually replaces before touching any feature: the Ollama application is one thing, and the models it pulled are files in a separate directory (~/.ollama/models and its siblings) that the updater does not write to. With that separation in place, read the v0.40.11 notes as a checklist of what changed in the app: speech generation on macOS, and the d3 decision-model family in four sizes. Then place .11 on the release calendar -- one calendar day after .10, two after .9 -- so the viewer can tell a routine bump from an urgent hotfix; the notes flag no breaking changes. The one counterexample that explains the re-download myth comes last: v0.40.2's background upgrades of pre-0.40 models, which kept the original on disk as a backup and only demanded a re-pull if you downgraded below 0.40. The payoff is the decision rule the viewer keeps: update the app always, re-pull never, pull new only when a feature names a model.

## Claims
1. **Ollama v0.40.11's headline change is speech generation on macOS: `ollama run` plays text or a chat model's reply aloud, and apps can stream audio through the OpenAI-compatible `/v1/audio/speech` endpoint.**
   - Source: Release v0.40.11 · ollama/ollama, https://github.com/ollama/ollama/releases/tag/v0.40.11
   - Tier: primary | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "Ollama can now generate speech on macOS."
2. **v0.40.11 also ships the d3 decision-model family from vLLM Semantic Router, sized 2B, 4B, 9B, and 27B, for classifying text, answering yes or no, and scoring options with probabilities.**
   - Source: Release v0.40.11 · ollama/ollama, https://github.com/ollama/ollama/releases/tag/v0.40.11
   - Tier: primary | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "The family includes 2B, 4B, 9B, and 27B sizes."
3. **v0.40.11 is a routine bump, not a hotfix: it was released 24 Oct 00:30, one calendar day after v0.40.10 (23 Oct 15:03) and two days after v0.40.9 (22 Oct 01:33), and none of those three release notes flag a breaking change.**
   - Source: Releases · ollama/ollama, https://github.com/ollama/ollama/releases
   - Tier: primary | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "released this yesterday 24 Oct 00:30" (v0.40.11) and "released this 2 days ago 23 Oct 15:03" (v0.40.10)
4. **An Ollama update replaces the application, not the models: pulled models live in `~/.ollama/models` on macOS, `/usr/share/ollama/.ollama/models` on Linux, and `C:\Users\%username%\.ollama\models` on Windows, directories the update mechanisms never write to.**
   - Source: FAQ - Ollama, https://docs.ollama.com/faq
   - Tier: docs | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "macOS: `~/.ollama/models` / Linux: `/usr/share/ollama/.ollama/models` / Windows: `C:\Users\%username%\.ollama\models`"
5. **The only model-touching change in the 0.40 line came in v0.40.2: models pulled with earlier versions were upgraded in the background on first run with the original kept on disk as a backup, and it is a downgrade below 0.40, not an update, that forces a re-pull.**
   - Source: Releases · ollama/ollama, https://github.com/ollama/ollama/releases
   - Tier: primary | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "Models downloaded with earlier versions of Ollama are upgraded in the background the first time you run them" and "If you later downgrade to a version older than 0.40, you'll need to re-pull those models."
6. **Updating is one step per platform: macOS and Windows download updates automatically and apply them by clicking Restart to update in the taskbar or menubar, and Linux re-runs the install script.**
   - Source: FAQ - Ollama, https://docs.ollama.com/faq
   - Tier: docs | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "Ollama on macOS and Windows will automatically download updates. Click on the taskbar or menubar item and then click "Restart to update" to apply the update."
7. **The new speech capability costs one new pull, not a re-pull: phonon:latest downloads at 113MB, and the packages require Apple Silicon and Ollama 0.40.9 or later.**
   - Source: phonon, https://ollama.com/library/phonon
   - Tier: primary | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "113MB · 8K context window" and "These Ollama packages require Apple Silicon and Ollama 0.40.9 or later."
8. **Trying the new decision models is an evening-sized pull measured in single digits: d3:2b downloads at 3.1GB - 3.2GB with a 256K context window, while the 27B sibling runs 29GB - 30GB.**
   - Source: d3, https://ollama.com/library/d3
   - Tier: primary | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "3.1GB - 3.2GB · 256K context window · Text, Image" and "29GB - 30GB · 256K context window · Text, Image"
9. **The Windows docs confirm the app/model separation from the removal side: even the uninstaller leaves downloaded models alone when OLLAMA_MODELS was moved.**
   - Source: Windows - Ollama, https://docs.ollama.com/windows
   - Tier: docs | Confidence: high | Accessed: 2026-10-25 | Via: web_extract
   - Quote: "If you have changed the OLLAMA_MODELS location, the installer will not remove your downloaded models"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | phonon:latest download size (the whole speech feature) | 113MB | https://ollama.com/library/phonon | "113MB · 8K context window" |
| 2 | d3:2b download size | 3.1GB - 3.2GB | https://ollama.com/library/d3 | "3.1GB - 3.2GB · 256K context window · Text, Image" |
| 3 | d3:27b download size | 29GB - 30GB | https://ollama.com/library/d3 | "29GB - 30GB · 256K context window · Text, Image" |
| 4 | d3 family sizes | 2B, 4B, 9B, and 27B | https://github.com/ollama/ollama/releases/tag/v0.40.11 | "The family includes 2B, 4B, 9B, and 27B sizes." |
| 5 | v0.40.11 release time (page-printed date) | 24 Oct 00:30 | https://github.com/ollama/ollama/releases | "released this yesterday 24 Oct 00:30" |

## Analogy candidates
- **Music player update**: Updating Ollama is like updating the music player app on your phone -- the player changes, the songs on your storage do not, and "re-downloading" only enters the picture when you want a new album (phonon, d3). Breaks when: models are not inert songs; they are format-coupled to the engine, and the v0.40.2 runner swap shows a player update can rewrite your library's format under you -- with a backup kept, but disk usage temporarily doubled.

## Misconceptions
- Myth: Every Ollama update re-downloads your models. Reality: The updater replaces the app while pulled models sit untouched in ~/.ollama/models, and the 0.40 line's only model change (v0.40.2) was an automatic background upgrade that kept the original as a backup (claims 4 and 5).
- Myth: v0.40.11 is an urgent hotfix you must drop everything for. Reality: It shipped one calendar day after v0.40.10 as a routine feature bump -- speech plus d3 -- with no breaking changes flagged in the notes (claim 3).

## Glossary
- **Ollama**: an app that downloads and runs open AI models locally on your own machine.
- **pull**: downloading a model from ollama.com's library onto your disk; the only large download in Ollama.
- **speech model**: a model that turns written text into spoken audio, streamed as it generates.
- **decision model**: a small model trained to classify input, answer yes or no, or score options instead of chatting.

## Unverified
- How widespread the belief that updates re-download models actually is: the Reddit and forum threads surfaced by search could not be fetched this session (403), so the myth's reach is unmeasured.
- No first-party or benchmark performance numbers exist for v0.40.11; any tokens-per-second or load-time claim must wait for a measurement on our own hardware.
- When speech generation reaches Windows and Linux is not stated in the v0.40.11 notes, which say "on macOS" only.

## Suggested outline
1. Cold open on the two-line test: v0.40.11 shipped speech on macOS and the d3 decision models -- and its notes say nothing about the models you already have, which is exactly the point.
2. The mechanism that kills the myth: the updater swaps the app while models live in ~/.ollama, and the one time Ollama did touch models (v0.40.2) it upgraded them in the background with backups kept.
3. The rule and the one pull worth making: update always, re-pull never, pull new only when a feature names a model -- phonon at 113MB for speech, d3 at 3.1GB - 3.2GB for decisions.

## Viewer situation
You've got Ollama 0.40-point-something on your gaming PC or Mac with a few models already pulled, and every update ping makes you wonder whether tonight is the night you re-download a hundred gigabytes.

## Has process
`true`
- check the release notes for the version you are on, at github.com/ollama/ollama/releases
- apply the update: click Restart to update on macOS or Windows, or re-run `curl -fsSL https://ollama.com/install.sh | sh` on Linux (Docker: pull the ollama/ollama image again)
- run `ollama list` to confirm every pulled model is still there, untouched
- pull only what the notes actually add, e.g. `ollama pull phonon` for speech or `ollama run d3` for decision models
- re-pull an existing model only if you downgraded below 0.40 or deleted it, never because the app updated

## Objection
Absence of a warning is not a guarantee: Ollama has already changed model formats under users once with the v0.40.2 background upgrade, so "your models are safe" holds only until the next runner swap.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/ollama/ollama/releases | Releases · ollama/ollama | primary | web_extract | 2026-10-25 |
| 2 | https://github.com/ollama/ollama/releases/tag/v0.40.11 | Release v0.40.11 · ollama/ollama | primary | web_extract | 2026-10-25 |
| 3 | https://docs.ollama.com/linux | Linux - Ollama | docs | web_extract | 2026-10-25 |
| 4 | https://docs.ollama.com/macos | macOS - Ollama | docs | web_extract | 2026-10-25 |
| 5 | https://docs.ollama.com/windows | Windows - Ollama | docs | web_extract | 2026-10-25 |
| 6 | https://docs.ollama.com/docker | Docker - Ollama | docs | web_extract | 2026-10-25 |
| 7 | https://docs.ollama.com/faq | FAQ - Ollama | docs | web_extract | 2026-10-25 |
| 8 | https://docs.ollama.com/capabilities/speech | Speech - Ollama | docs | web_extract | 2026-10-25 |
| 9 | https://ollama.com/library/phonon | phonon | primary | web_extract | 2026-10-25 |
| 10 | https://ollama.com/library/d3 | d3 | primary | web_extract | 2026-10-25 |

## Notes
GitHub prints release times in the viewer's timezone: the v0.40.11 page shows 24 Oct 00:30 while the tag's source assets carry the ISO stamp 2026-10-23T23:15:08Z; the page-printed date is the one quoted verbatim. The docs.ollama.com/install URL is a 404; the per-platform pages (/linux, /macos, /windows, /docker, /faq) are the live install-and-update pages. Thin spots: no official page states outright that updates leave models untouched -- claim 4 is assembled from the documented storage locations plus what each update mechanism replaces -- and the community threads behind the re-download myth returned 403, so the misconception is grounded in Ollama's own v0.40.2 note rather than community measurement. The Linux docs corroborate claim 6 ("Update Ollama by running the install script again") and the speech docs corroborate claim 7 ("Start Ollama v0.40.9 or later, then download Phonon").

- 03 checkpoint (unattended): angle confirmed -- the v0.40.11 patch notes decide whether re-pulling your models is worth the evening; slug unchanged.
- 03 rationale: classic band, one fact one consequence; the viewer already runs Ollama, so the brief targets the update-or-re-pull decision, not an install walkthrough.
