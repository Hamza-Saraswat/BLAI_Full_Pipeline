---
slug: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f
stage: 04-script
generated_at: 2026-11-14
hub: "[[videos/2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f]]"
---

# Drafts and judgment

### Draft A: comparison-ladder (Pro or Flash? One number decides)

Target 107 s, 10 scenes, 317 words.

| Scene | Role | Narration | On-screen | Est s |
|---|---|---|---|---|
| s01 | hook | Tonight it's DeepSeek Pro or Flash, and one number decides. | Pro or Flash? One number decides | 3.4 |
| s02 | explain | You're picking between two DeepSeek downloads tonight. The Pro's smallest published file is eight hundred fifty gigabytes on disk. The Flash's smallest is two hundred thirty-three gigabytes on your drive. | Pro: smallest file 850 GB | Flash: smallest file 233 GB | 10.3 |
| s03 | explain | Both are quantized, stored at lower precision to shrink the file. One file each. Both ship as a single-file build you can run tonight. Unsloth publishes them on Hugging Face, fully open weights. | Quantized: lower precision, smaller file | One file, runs tonight | GGUF from Unsloth on Hugging Face | 11.4 |
| s04 | explain | Each is a mixture of experts, a model that wakes only a slice of itself per word. Those active parameters, the slice that does the work, stay small. Every expert still has to sit on your drive or in your memory. | Mixture of experts | Active slice per word | Every expert still sits somewhere | 14.1 |
| s05 | explain | So what fits tonight? Drive streaming, pulling parts of the model from your fast drive into memory when they are needed, is the trick. On Unsloth's numbers, a big Spark-class machine holds the Flash. Nothing published yet holds the Pro. | SSD STREAMING | Flash: fits tonight | Pro: no published fit | 13.8 |
| s06 | explain | Picture a master carpenter with a rolling tool chest. The daily tools ride inside; the rare ones fetch from the store across the street, your drive. Except a router inside the model picks per word, and the fetch costs seconds instead of a trip across town. | Rolling chest: daily tools | Rare tools fetch from the drive | Router picks per word | 15.9 |
| s07 | explain | Here's the twist. On DeepSeek's own table, the Flash scores ninety point six on the terminal bench, ahead of the Pro. The smaller pull is the quality pick for coding and agents, not the compromise. | DeepSeek's own table | Terminal-Bench: Flash 90.6 | Quality pick, not compromise | 12.1 |
| s08 | explain | The Pro still leads the world-knowledge rows, where its bigger backbone earns its keep. And if you ever rent these in DeepSeek's cloud, the Flash is the cheaper seat there too. | Knowledge rows: Pro leads | Coding rows: Flash leads | Cloud: Flash costs less | 10.7 |
| s09 | explain | So tonight: count your free memory. Grab the Unsloth single-file build that fits. Run it in llama dot cpp or Unsloth Desktop. Let your drive hold the overflow. Set reasoning effort to trade speed against depth. | Count free memory | Pull the Unsloth GGUF that fits | llama.cpp + Unsloth Desktop | Drive holds overflow | Set reasoning effort | 12.4 |
| s10 | payoff_close | The rule to keep: your free memory picks the model. Tonight, it picks the Flash. | Your memory picks the model | Tonight: Flash | 5.2 |

### Draft B: contrarian-take (552B beat 1.6T)

Target 94 s, 9 scenes, 273 words.

| Scene | Role | Narration | On-screen | Est s |
|---|---|---|---|---|
| s01 | hook | Five hundred fifty-two billion parameters just beat one point six trillion parameters. If you're picking a DeepSeek for your own machine, that flips the choice. | 552B beat 1.6T | DeepSeek's own table | 8.6 |
| s02 | foreshadow | The obvious pick is the Pro, the giant flagship. Bigger is supposed to be better. That's the consensus. | the obvious pick | V4 Pro | bigger means better? | 6.2 |
| s03 | explain | The smallest Pro build so far needs memory your machine doesn't have. The smallest Flash build is two hundred thirty-three gigabytes on disk, one file from Unsloth. They say it runs on a high-memory home machine. | smallest builds | Pro: memory you don't have | Flash: 233 GB | 12.4 |
| s04 | explain | Both are a mixture of experts, a model that wakes only a slice of itself per word. That slice is the active parameters, the weights one word touches. Every expert still has to live on your disk or in memory. | mixture of experts | one slice per word | active parameters | all experts sit on disk | 13.8 |
| s05 | explain | Offloading keeps rarely used experts on your fast drive until they're needed. | SSD offload | rare experts wait on drive | 4.1 |
| s06 | explain | The Pro is a full workshop installed on site. The Flash is a master carpenter with a rolling chest, and rare tools fetch from across the street. A router inside the model picks, not a carpenter, and the fetch costs speed. | workshop vs rolling chest | fetch costs speed | 14.1 |
| s07 | explain | Now the twist. On DeepSeek's own table, the Flash outscores the Pro on Terminal-Bench and DeepSWE, the coding and agent benches. Artificial Analysis puts the Flash near the top of its intelligence index; the Pro sits mid-pack. | Flash wins Terminal-Bench | Flash wins DeepSWE | Flash near top, Pro mid-pack | 12.8 |
| s08 | explain | So the claim stays narrow. For coding and agents on your machine, the Flash is the better pull. The Pro still wins the knowledge rows. Nobody has timed either model well on home hardware, so speed claims are untested. | the narrow claim | coding + agents: Flash | knowledge rows: Pro | home speed: untested | 13.4 |
| s09 | payoff_close | Count your free memory, grab the Flash build that fits, and let your drive hold the rest. Tonight, the small one is the right pull. | count free memory | pull the Flash | tonight's pick | 8.6 |


## Judge verdict (kimi-k3, blind, rubric 0-3 x 8)

```
SCORES
Hook | A 3 | B 3 | A names both products and the decision tension inside five words ("DeepSeek Pro or Flash"); B's upset number is named in the first breath and the shock lands in the same sentence.
Payoff timing | A 2 | B 3 | A spends a full sentence restating the pick ("You're picking between two DeepSeek downloads tonight") before the 850 GB lands around second 9-10; B's hook is itself the promised concrete, paid immediately.
Specificity | A 3 | B 1 | A: one number per sentence, each attributed ("On Unsloth's numbers", "On DeepSeek's own table"), absence phrased as absence ("Nothing published yet holds the Pro"). B capped at 1 (finding 17): "Nobody has timed either model well on home hardware" asserts as fact what the brief frames as absence of evidence; the bench beat also goes vague ("near the top", "mid-pack") where 90.6 was available, and "They say" is unattributed.
Voice | A 3 | B 3 | Both clean second person, every term defined in the same breath, one dry undercut each that lands unexplained ("the fetch costs seconds instead of a trip across town" / "a router inside the model picks, not a carpenter").
Navigation | A 3 | B 3 | No positional labels anywhere; transitions are question-answer and contradiction moves ("So what fits tonight?", "So the claim stays narrow"). "Here's the twist" / "Now the twist" are legal expectation-contradiction moves, not labels. Neither script reorders without breaking.
Difference | A 3 | B 2 | A: comparison-ladder, decision opener, rule landing -- none in the last five (mild "tonight" echo from 11-11 noted, but the rhythm is a choice, not a tonight-promise). B: contrarian shape is fresh, but the number-shock opener repeats 2026-11-10's hook pattern.
Repeat test | A 3 | B 2 | A's payoff is a portable rule and it is the last thing spoken. B's most quotable line is the hook (552B beat 1.6T); the payoff verdict ("the small one is the right pull") is generic enough to close any video.
Teaching | A 3 | B 2 | A hands over a rule that predicts cases never mentioned: any future model, any machine, free memory decides, drive holds overflow. B shows the mechanism concretely once, but its only predictive content (knowledge rows go to the Pro) is a case it already mentions.

TOTALS: A 23/24, B 19/24

WINNER: A

GRAFTS: none. The hook graft requires the loser's hook to score at least two points higher on row 1; both scored 3. B's two candidate sentences both fail graft rules: the untested-speed line is the drifted claim itself and would cap the winner's row 3, and the 552B/1.6T sentence would break A's number budget (two new numbers in one sentence added to a script that spends exactly three).

LOSER-WOULD-HAVE-NEEDED: B needed to phrase the home-speed caveat as absence of evidence ("nothing published yet times them well on home boxes") instead of asserting nobody has timed them, and to spend the ninety point six at the twist instead of "near the top, mid-pack". It also needed an opening rhythm that does not repeat the 11-10 number-shock and a payoff that hands the viewer a rule rather than a verdict.

REPEAT-TEST: "Your free memory picks the model."
```

## Outcome

Winner: draft A (comparison-ladder), 23/24 to 19/24, no grafts. Both drafts passed validator
(0 blockers), all nine eval gates and the variety check before judgment.
