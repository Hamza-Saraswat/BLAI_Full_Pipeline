---
slug: 2026-10-20-fine-tune-deepseek-v4-1-with-u
stage: 04-script
generated_at: 2026-10-20T13:05:00Z
judge: kimi-k3 (blind, rubric as system file)
winner: B (news-react-so-what) 22-16
---

# Drafts and scores

## Draft A (how-to-three-moves, hook: tonight)
| s01 | Three moves to your own fine-tuned Llama tonight. You watched DeepSeek V four point one land yesterday and wanted your own.
| s02 | Here is the honest catch. Unsloth's new beta runs that model in about one hundred twenty-five gigabytes of memory. But support means running it. Running shipped; the training recipe stayed home. Fine-tuning, teaching it your own examples, shipped no recipe.
| s03 | So tonight you train the stock Unsloth recipe on a model that fits your card. Memory follows the whole checkpoint, every saved weight, not the slice that thinks. If a V four point one training path lands later, this same recipe inherits it.
| s04 | Move one: install Unsloth with one pasted command. Pip is Python's installer, and this one line grabs the toolkit. The stock recipe fine-tunes with just three gigabytes of V RAM, your graphics card's memory.
| s05 | Move two: load a four-bit Llama and attach LoRA. Four bit squeezes each weight to a quarter of its size, about a four-times memory cut. LoRA adds thin trainable layers while the base model stays frozen.
| s06 | Think vinyl wrap, not repaint, and the wrap still needs the whole car in your garage. So you pick a model that fits and paste one string. LoRA on a four-bit copy: that is Q LoRA.
| s07 | Move three: train on your question-and-answer pairs. Two columns, questions and answers, and the loss, your error score, falls while you watch. Write them yourself or generate them.
| s08 | Save the adapter, your small trained file, then export to G G U F, the one file Ollama runs. Ollama, LM Studio and llama dot C P P all read it.
| s09 | Ollama loads it and you ask your question. The answer comes back in your voice: your fine-tuned Llama, running tonight.

## Draft B (news-react-so-what, hook: number-shock) -- WINNER
| s01 | V four point one runs locally, about one hundred twenty-five gigabytes of memory.
| s02 | Yesterday, Unsloth shipped a beta whose headline is DeepSeek V four point one running locally. You watched it land wanting your own copy, fine-tuned, meaning retrained on your examples.
| s03 | Here is what changes for you. Park the Engram table, a giant lookup memory, on your S S D. Then V four point one runs in about one hundred twenty-five gigabytes of memory.
| s04 | Picture a library. The Engram table is the basement archive; each word pages up only the rows it needs. The limit: the reading room alone still overflows any gaming card.
| s05 | The model holds five hundred fifty-two billion parameters. It is a mixture of experts: a router wakes only a few specialist blocks per word. And memory bills you for the whole model, not the slice that fires.
| s06 | Here is the honest part: in this release, support means running. No fine-tuning recipe, no notebook, no training checkpoint shipped for V four point one.
| s07 | Unsloth's own guide points its training advice at other models. V four point one even ships without a chat template, the rules that shape your prompts. Support, it turns out, is a spectator sport.
| s08 | So tonight, run Unsloth's stock Q LoRA recipe. That is thin LoRA adapters trained on a four-bit compressed copy of a model that fits your card.
| s09 | It runs on the free tier of Colab. The stock recipe fine-tunes with just three gigabytes of V RAM, your graphics card's memory. Load a four-bit Llama checkpoint and attach the adapters. Train on your question-and-answer dataset, save the adapter, and export to guff, the file Ollama runs.
| s10 | If a V four point one training path ever ships, this same recipe inherits it. Tonight, you train the model that fits your card.

## Judge's score table
| Row | A | B |
|---|---|---|
| 1 Hook | 2 | 3 |
| 2 Payoff timing | 1 | 3 |
| 3 Specificity | 2 | 3 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 3 | 3 |
| 6 Difference | 1 | 1 |
| 7 Repeat test | 2 | 3 |
| 8 Teaching | 2 | 3 |
| Total | 16 | 22 |

Row justifications (judge's words) and the full verdict are in the run's judge scratch dir; the two graft-relevant lines:

- Row 2: A fronts the catch, so its first hard fact lands around second 13; B's number-shock hook is self-paying, the claim lands by second 4.
- Row 3: A's key number drops both conditions (1-bit, Engram on SSD); B keeps the Engram-on-SSD condition and spends 552B once.

## Grafts
- From A to B (s09): "The stock recipe fine-tunes with just three gigabytes of V RAM, your graphics card's memory." -- names a concrete hardware floor for the tonight-plan where B only gestured at Colab; inserts whole after the Colab sentence, one new number in its own sentence.

## What the losing shape would have needed
A needed to pay its promise faster: the catch-first structure delayed the first hard number to about 13 seconds, and its key number needed its conditions (1-bit, Engram on SSD) to survive the fidelity check. It also needed an opening rhythm and closing line that did not rerun the 10-16 "tonight" how-to, since repeating a four-day-old shape left it no room to lose a single content row.
