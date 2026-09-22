---
slug: 2026-09-22-open-webui-s-new-slim-image-is
stage: 04-script
winner: B (number-first)
---

# Drafts: 2026-09-22-open-webui-s-new-slim-image-is

Both drafts passed every hard gate before judging (validator blockers 0, eval gate1_ready true,
variety ok). Judge: kimi-k3, blind to both writings, rubric as its system file.

## Draft A (news-react-so-what, hook: named-contradiction)
Hook: Open WebUI just shipped itself without the ML stack.

| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | Open WebUI just shipped itself without the ML stack. You pull it in Docker, gigabytes at a time. | Open WebUI just shipped itself without the ML stack. | 6.2 |
| s02 | explain | You chat through Ollama or an API key. It carried torch, the neural network library, speech models, and converters like ffmpeg. | INSIDE: torch, speech models, ffmpeg | 7.2 |
| s03 | explain | The slim build drops that stack: about one hundred seventy-five megabytes. Eighty-nine percent smaller than the last slim. The last slim pulled one point four four gigabytes. | SLIM 175 MB | 89% SMALLER | LAST SLIM 1.44 GB | 9.7 |
| s04 | foreshadow | Slim won't start on MySQL or S3 storage. Voice, PDFs, and embeddings, the numbers behind document search, move to outside services. | WON'T START: MySQL, S3 then hard cut to EXTERNAL: voice, PDFs, embeddings | 7.6 |
| s05 | payoff_close | Chatting through Ollama changes nothing. Swap the image suffix to main-slim tonight. Your volume, the folder with your chats, survives. | docker pull ghcr.io/open-webui/ open-webui:main-slim | 6.9 |

Target 37.6 s. Working title: Open WebUI Slim: 175 MB Without the ML Stack.

## Draft B (number-first, hook: number-shock) -- WINNER
Hook: Open WebUI's download just shrank eighty-nine percent.

| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | Open WebUI's download just shrank eighty-nine percent. You run it in Docker next to Ollama, wincing at every pull. | Open WebUI / 89% / smaller download | 6.2 |
| s02 | explain | Slim drops the bundled machine-learning stack: torch, the neural-network library, speech models, and ffmpeg, a media converter. Installed just in case. | torch / speech models / ffmpeg | 7.2 |
| s03 | explain | Eighty-nine percent is against the last slim, a one point four four gigabyte pull. The standard image stays one point five four gigabytes. | last slim / 1.44 GB / standard image | 8.6 |
| s04 | explain | Slim refuses MySQL or S3 storage at boot; voice and PDF reading move outside. Chat through Ollama and nothing changes. | ollama chat: same | 7.2 |
| s05 | payoff_close | Tonight, swap your compose file to the slim tag; your volume keeps every chat. Your next pull is about one hundred seventy-five megabytes. | image: openwebui/open-webui:slim / 175 MB / 89% smaller | 7.9 |

Target 37.1 s. Working title: Open WebUI Slim: An Honest 89 Percent Shrink.
Saved board reflects three advisory fixes on top of this draft: s03 and s05 number referents,
"S three" spelled out in s04, s05 on-screen block trimmed, sfx cues capped at 6.

## Judge score table
| Row | A | B |
|-----|---|---|
| Hook | 3 | 3 |
| Payoff timing | 2 | 3 |
| Specificity without cramming | 3 | 3 |
| Voice | 2 | 3 |
| Navigation | 3 | 3 |
| Difference | 2 | 1 |
| The repeat test | 2 | 1 |
| Teaching | 2 | 3 |
| TOTAL | 19 | 20 |

## Winner reason
B wins on craft by a single point: it holds the 175 MB payoff for the final frame with the 89% digit returning as a callback, and it explicitly grounds the 89% against the last slim while naming the 1.54 GB standard image, pre-empting the skeptic's core fact. Its number-first/number-shock pairing repeats the 2026-09-18 entry almost exactly, which cost it both freshness rows and is the only reason the margin is this thin.

## Grafts
None. [] (the loser's hook did not outscore the winner's by two, and no loser sentence beat its winner counterpart without breaking the number budget.)

## Drift check
A: none
B: none (the hook's bare 89% is grounded in s03 against the last slim, with the standard 1.54 GB kept separate; never framed as slim-vs-standard)

## What the losing shape would have needed
A needed to hold one number back for the close instead of spending all three in the middle scene, so the video ends on a benefit rather than a command, and it needed the 1.54 GB standard-image context so the 89% comparison fully arms the viewer against the main misconception. Cleaning up the spoken lines (the doubled 'last slim' beat and the stacked appositives in the catch and close) would also have erased B's voice edge.
