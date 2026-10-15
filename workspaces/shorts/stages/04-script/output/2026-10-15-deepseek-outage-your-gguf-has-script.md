---
slug: 2026-10-15-deepseek-outage-your-gguf-has
format: smooth-explainer
structure: myth-bust
style_pack: halftone
value_types: TEACHES,REFRAMES
promise: After this you can say what actually failed in the Oct 14 DeepSeek outage, why a local GGUF file kept working, and which copy fits your GPU.
target_duration_s: 95
brief: 2026-10-15-deepseek-outage-your-gguf-has-brief.md
drafts: 2026-10-15-deepseek-outage-your-gguf-has-drafts.md
---

# DeepSeek outage: your GGUF has no status page

## Decisions

- Structures tried: myth-bust (draft A) and comparison-ladder (draft B); both cleared the
  rotation rule (last two shipped: news-react-so-what, worked-example). Judge: A wins 21-16,
  no grafts.
- Hook: candidate 1 of 10, "DeepSeek went down last night. Yours didn't have to." (situation
  pattern; names the event and the tension in five words, and the outage duration lands inside
  the hook scene). Draft B drew a decision-pattern hook to force divergence.
- Number budget: three on-screen numbers (4h 52m, 404.43 GB, 24 GB); the 671B parameter count
  was dropped from both drafts after the first eval round failed number_spend at four distinct.
- Value delivery: TEACHES lands on "DeepSeek is two things stacked" and "the files did not
  change" (s03-s04); REFRAMES lands on the payoff "The API was never the model. A file on your
  disk has no status page."
- Gates: validate_storyboard 0 blockers 0 advisories; eval_short gate1_ready, failures none,
  soft advisories entity_spend and top2 (the entity top-2 is DeepSeek/DeepSeek-R1; kept: the
  video is about DeepSeek's own status record).

## Hook candidates

1. DeepSeek went down last night. Yours didn't have to. *
2. DeepSeek gives away the model and sells the uptime.
3. Four hours fifty-two minutes dark. Your copy didn't notice.
4. Your model isn't down. Its website is.
5. Cloud API or local file? One outage decides.
6. A four-hundred-gigabyte file that never goes down.
7. The API went down. The model didn't go anywhere.
8. You pay for uptime, not intelligence.
9. Five incidents in October. Your disk had zero.
10. When DeepSeek blinks out, your GPU doesn't care.

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | DeepSeek went down last night. Yours didn't have to. You just watched its status page log four hours and fifty-two minutes of downtime. | DeepSeek went down. Yours didn't have to. | Frame 1 composition: hook text centered and fully legible, a red status dot above it. Motion onset at 0.3s: the dot pulses. On "Yours didn't have to" the pulse stops on solid red. On "four hours and fifty-two minutes" a staged swap: hook text fades out, giant "4h 52m" scales in with caption "DeepSeek status page" beneath. One soft alert ping on "went down". Last 8 frames hold. | hyperframes | centered-stack | 11.0 |
| s02 | explain | You chat with DeepSeek in the browser, or you call its API from your side projects. Either way, it feels like one thing. Somewhere along the way, the website became the model. | the website is the model | Split screen, both panels static from frame 1: left a chat window labeled "chat", right a terminal panel labeled "API call". On "feels like one thing" the divider line between the panels fades out. On "the website became the model" the bottom caption rises in; it is the only text block animating then. | hyperframes | split-compare | 11.0 |
| s03 | explain | DeepSeek is two things stacked. The model is files of numbers, called its parameters. The service is someone else's computers running those files for you. | model = files of numbers | Stack diagram builds on "two things stacked": top block labeled "service" fades in, then bottom block labeled "model" rises in, never two text blocks at once. On "files of numbers" the model block's caption "model = files of numbers" fades in. | manim | diagram-flow | 8.6 |
| s04 | explain | Last night, that service went dark. The files did not change. One of those two things can live on your disk. | the files didn't change | Same stack, now centered: on "went dark" the top "service" block dims to grey. On "did not change" the bottom "model" block stays lit and the caption "the files didn't change" fades in. On "live on your disk" a small download-arrow icon fades in beside the bottom block. | hyperframes | centered-stack | 6.9 |
| s05 | explain | Treat the chat app like a streaming service. The GGUF file, a single file holding a whole model, is the disc on your shelf. The service going dark does not touch the disc. | the disc still plays | Left: a streaming app window, greyed, static text "service unavailable". Right: a shelf holding a disc case labeled "GGUF". On "goes dark" the left panel dims further. On "does not touch the disc" the disc case rises slightly in place and catches a highlight while the caption "the disc still plays" fades in. A faint disc-tray click on "disc on your shelf". | hyperframes | split-compare | 10.7 |
| s06 | explain | DeepSeek published the R one weights, the trained model files themselves, free for anyone under the MIT license. They sit on Hugging Face right now. LM Studio or llama.cpp runs the file on your machine. No account, no API key, no status page to check. | R1 weights on Hugging Face | Three-tile grid, tiles rising one at a time. On "published the R one weights" tile one fades in: a Hugging Face model card labeled "R1 weights". On "LM Studio or llama.cpp" tile two rises in with the LM Studio and llama.cpp logos. On "no status page to check" tile three rises in, labeled "no API call". On "right now" the full grid holds, all tiles lit. | hyperframes | grid | 17.6 |
| s07 | explain | Now the honest part. At the common download quality, the full DeepSeek R one is a four hundred four gigabyte file. Your gaming PC is not loading that. Neither is your Mac. | 404.43 GB | On "four hundred four gigabyte file" the digits "404.43 GB" scale in at center. Below, a download progress bar creeps and stalls near empty on "is not loading that". On "Neither is your Mac" a small laptop icon fades in beside the bar, equally stalled. A low thunk as the number lands. | manim | giant-number | 11.4 |
| s08 | explain | DeepSeek also shipped distills, smaller models trained to imitate the big one. One of those carries seven billion parameters. Unsloth's GGUF card sizes it against a twenty-four gigabyte gaming GPU, an RTX forty ninety for example. | 24 GB gaming GPU | Two-tile grid: left tile "full R1" with a tall file stack, right tile "the distill" with a small file. On "seven billion parameters" the right tile's caption "7B distill" fades in. On "twenty-four gigabyte gaming GPU" the text "24 GB gaming GPU" rises in under the right tile as a GPU outline fades in beside it. | hyperframes | grid | 14.5 |
| s09 | explain | One catch. A disc holds the identical movie. Your copy is cut down, so the quality genuinely drops. When you need the full model's best answers, the cloud is still where that brain lives. | same movie, cut-down copy | Split compare: left a disc labeled "same movie", right a smaller copy labeled "cut-down copy". On "quality genuinely drops" the small copy's image softens. On "still where that brain lives" a cloud icon above the left side stays lit. | hyperframes | split-compare | 10.7 |
| s10 | payoff_close | The API was never the model. A file on your disk has no status page. | a file has no status page | The caption "a file has no status page" centered from the first frame. On "The API was never the model" a dim status-page window behind it fades to black. On "no status page" a single file icon stays lit at center. After the last spoken word the wordmark settles into the corner, visual only. One short warm settle tone under the wordmark. | hyperframes | centered-stack | 4.8 |

## Notes for review

- 404.43GB is rounded once for the ear to "four hundred four gigabyte"; the storyboard shows the
  verbatim 404.43 GB on screen. 4h 52min likewise becomes "four hours and fifty-two minutes".
- The 671B parameter count was cut for the three-number budget; the "full R1" tile still carries
  the scale visually.
- The analogy is the streaming service vs the disc, and its limit (a local distill is a cut-down
  model, not an identical copy) is stated in s09, per the signature-analogies rule.
- est durations use the provisional 2.9 wps; re-time from the real voice render.
