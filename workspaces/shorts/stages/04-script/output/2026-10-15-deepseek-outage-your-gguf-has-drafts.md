---
slug: 2026-10-15-deepseek-outage-your-gguf-has
stage: 04-script
winner: A (myth-bust, 21-16)
generated_at: 2026-10-15T13:55:00Z
---

# Drafts: DeepSeek outage: your GGUF has no status page

Two blind writers on Kimi K3, packets in `.local-builds/2026-10-15-deepseek-outage-your-gguf-has/draft-A|draft-B/`. Both passed
validate_storyboard (0 blockers, 0 advisories) and eval_short (gate1_ready, soft entity_spend and
top2 advisories only) before the judge read them.

## Draft A: myth-bust (winner)

Hook pattern: situation. Hook: DeepSeek went down. Yours didn't.

| Scene | Role | Narration | On-screen | Layout | Est s |
|---|---|---|---|---|---|
| s01 | hook | DeepSeek went down last night. Yours didn't have to. You just watched its status page log four hours and fifty-two minutes of downtime. | DeepSeek went down. Yours didn't have to. | centered-stack | 7.9 |
| s02 | explain | You chat with DeepSeek in the browser, or you call its API from your side projects. Either way, it feels like one thing. Somewhere along the way, the website became the model. | the website is the model | split-compare | 11.0 |
| s03 | explain | DeepSeek is two things stacked. The model is files of numbers, called its parameters. The service is someone else's computers running those files for you. | model = files of numbers | diagram-flow | 8.6 |
| s04 | explain | Last night, that service went dark. The files did not change. One of those two things can live on your disk. | the files didn't change | centered-stack | 7.2 |
| s05 | explain | Treat the chat app like a streaming service. The GGUF file, a single file holding a whole model, is the disc on your shelf. The service going dark does not touch the disc. | the disc still plays | split-compare | 11.4 |
| s06 | explain | DeepSeek published the R one weights, the trained model files themselves, free for anyone under the MIT license. They sit on Hugging Face right now. LM Studio or llama.cpp runs the file on your machine. No account, no API key, no status page to check. | R1 weights on Hugging Face | grid | 15.5 |
| s07 | explain | Now the honest part. At the common download quality, the full DeepSeek R one is a four hundred four gigabyte file. Your gaming PC is not loading that. Neither is your Mac. | 404.43 GB | giant-number | 11.0 |
| s08 | explain | DeepSeek also shipped distills, smaller models trained to imitate the big one. One of those carries seven billion parameters. Unsloth's GGUF card sizes it against a twenty-four gigabyte gaming GPU, an RTX forty ninety for example. | 24 GB gaming GPU | grid | 12.4 |
| s09 | explain | One catch. A disc holds the identical movie. Your copy is cut down, so the quality genuinely drops. When you need the full model's best answers, the cloud is still where that brain lives. | same movie, cut-down copy | split-compare | 11.7 |
| s10 | payoff_close | The API was never the model. A file on your disk has no status page. | a file has no status page | centered-stack | 5.2 |

## Draft B: comparison-ladder

Hook pattern: decision. Hook: The cloud API or your own GGUF?

| Scene | Role | Narration | On-screen | Layout | Est s |
|---|---|---|---|---|---|
| s01 | hook | The cloud API, or your own GGUF? Last night, you learned the difference. You chat with DeepSeek in a browser tab, or call it from your side projects. | cloud API or your own GGUF? | centered-stack | 9.7 |
| s02 | explain | Last night, DeepSeek's chat app and its APIs, the services your code calls, went down together. The company's own status page clocks the downtime at four hours and fifty-two minutes. The history page lists five incidents for October alone. | 4h 52m, five incidents in October | giant-number | 13.4 |
| s03 | explain | Here's what actually broke. The model is files of numbers. The service is DeepSeek's computers reading those files for you. The model never went anywhere. Only one of those two things has a status page. | Model: files. Service: their computers | split-compare | 12.1 |
| s04 | explain | Now the giveaway. R one's weights, the trained numbers themselves, sit on Hugging Face under an MIT license. Yours to download. Yours to keep. Six distills shipped alongside, small models trained to imitate the big one. | Hugging Face, MIT license, your disk | diagram-flow | 12.4 |
| s05 | explain | What you buy from DeepSeek is the uptime. You are not buying the model; you are buying it awake, metered per million tokens, half price off-peak. Grid power, in other words. A basement battery is dimmer than the grid, and it answers in the dark. | grid power or basement battery | split-compare | 15.5 |
| s06 | explain | So run it yourself. The recommended GGUF, one file with the whole model inside, is a four hundred four gigabyte download. No gaming card holds that. Neither does your Mac. | 404 GB, the full R1 file | giant-number | 10.3 |
| s07 | explain | Meet the seven billion parameter distill. Unsloth's model card sizes it for twenty-four gigabytes of memory, an RTX forty ninety. It's a weaker brain. That's the honest trade, and it still answers. | distill fits 24 GB, RTX 4090 | centered-stack | 11.0 |
| s08 | payoff_close | Rent the service for the brain, keep the file for the blackout: the API was never the model. | rent the service, keep the file | split-compare | 6.2 |

## Judge (Kimi K3, rubric as system file, both boards as user file)

```
SCORES:
1 | A=3 B=1 | A names DeepSeek and the outage tension inside five words; B opens on an either/or question with no product, no number, and undefined jargon
2 | A=2 B=1 | A's four-hours-fifty-two-minutes number lands inside the hook, by second eight; B's first concrete fact waits for scene two, past second nine
3 | A=3 B=2 | A spends five numbers, one per sentence, none decorative; B spends eight and doubles up in scenes two and seven
4 | A=3 B=0 | B says "your own GGUF" in sentence one and defines it sixty seconds later, breaking hard constraint 3; A defines each term at first use and lands one wry beat ("Neither is your Mac") on the box, not the viewer
5 | A=2 B=3 | A's transitions carry content but only some name the turn; B names every turn ("Here's what actually broke," "Now the giveaway," "Meet the seven billion parameter distill") and the order is load-bearing
6 | A=2 B=3 | A reuses the myth-bust shape and the hundred-plus-second band from three scripts back; B's ladder shape, question open, and rent/keep landing match nothing in the last five
7 | A=3 B=3 | each ends on its repeatable line, A with "a file on your disk has no status page," B with "rent the service, keep the file... the API was never the model"
8 | A=3 B=3 | both show the files-versus-service mechanism concretely enough that a viewer could predict any open-weights model survives its provider's next outage

TOTALS: A=21 B=16

WINNER: A

GRAFTS: none -- B's hook scores lower, and its two strongest lines (the API gloss, the battery analogy) are load-bearing inside B's own beats, so moving either would force rewrites in A's disc-analogy through-line

LOSER-NOTES: The comparison-ladder had the better navigation and the fresher shape, but it spent its first ten seconds on an either/or question built on an undefined term, so its evidence landed after the winner had already spent its number. To win, it needed to open on the named event, define GGUF in the same breath it first uses it, and let "Meet the seven billion parameter distill" arrive as a turn the script had earned rather than a rescue.
```

## Why the numbers were what they were

- Both drafts were capped to three on-screen key numbers (4h 52m, 404.43GB, 24GB) after the first
  eval round failed number_spend at four distinct numbers (671B params dropped from both).
- Draft B's original hook ("DeepSeek gives away the model and sells the uptime") classified as
  hook pattern other, repeating 2026-10-13-airlock; it was replaced with a decision-pattern hook
  before the judge.
