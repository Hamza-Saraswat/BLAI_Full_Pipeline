# Voice Rules: Build Local AI

## Hard Constraints

These are errors. If narration, on-screen text, a title or a description contains any of these, rewrite before saving.

1. No hype words: revolutionary, insane, game-changer, mind-blowing, secret, unlock, seamless, next-level.
2. No fake urgency, no "they don't want you to know", no rage bait, no clickbait a viewer would resent after watching.
3. Every technical term gets a plain definition in the same breath, preferably as an appositive: "a replica, a second server that keeps a copy of everything".
4. Narration is read aloud by a voice engine. Numbers are written as words ("twenty-seven billion"), acronyms the way they are said ("H two hundred"), and every number names its unit and its referent ("twenty-four gigabytes of memory", "thirty-two billion parameters"). Digits belong on screen, never in narration.
5. Never make the viewer hold more than one new number at a time. A listener cannot rewind.
6. No claim that is not verified in our own setup or traced to a cited source in the research brief.
7. **Nothing follows the payoff.** No spoken call to action, no "next up" tease, no summary of the summary. The ask lives in the description and the pinned comment; the wordmark settle is visual only. The last spoken sentence is the payoff itself, and the video stops within a second of it.
8. No em dashes in narration. Write like people talk; contractions are welcome.
9. Sentence length: hard cap 20 words; average at most 15 in Shorts and 18 in long-form.
10. **No positional labels.** "Stage one", "step two", "part three", "phase one" are banned unless the video walks the viewer through a process they will perform. Then, and only then, at most three of them, each naming the action ("Step two: quantize it"). Numbering components, layers, reasons or moves in an argument is always wrong: those are not stages.
11. **You are talking to one person.** Second person is the default. "We" is reserved for things we actually did ("we measured twenty-two tokens a second on our Spark"). Never "one might", never "users can", never "people often".

## Sentence Rules

| Wrong | Right |
|-------|-------|
| "This revolutionary model changes everything." | "This model runs on one gaming GPU. Last year's needed four." |
| "It uses MoE architecture." | "It's a mixture of experts, a model that wakes up only a slice of itself for each word." |
| "It holds 24GB." | "It holds twenty-four gigabytes of memory." |
| "Make sure to like and subscribe." | (nothing: the ask never goes in narration) |
| "First, we... Then, we... Finally, we..." | "Now the old server goes dark." |
| "Stage two, the shape." | "That covers the score. The shape is where it gets interesting." |
| "Stage four, then." | (cut it: a label carrying no information is not a sentence) |
| "Users can run the model locally." | "You can run it on the box you already own." |
| "You may want to consider quantization." | "Quantize it. You lose a little accuracy, and here's when you'd care." |
| "A 70B model needs a lot of VRAM." | "A seventy-billion-parameter model needs about forty gigabytes of memory, so it does not fit a gaming card." |

## Navigation

Beats are joined by content, never by numbering. Every transition is one of these moves:

| Move | Example |
|------|---------|
| Name what changes | "Now the file is three-bit." |
| Answer the question the last beat raised | "So which one fits? Neither, at full precision." |
| Contradict the expectation | "That reads like a yes. One question breaks it." |
| Jump to the consequence | "Your chat history sits in that same memory, and it grows with every word." |
| Introduce the new actor | "Now meet the router." |
| Zoom out to the stakes | "That's the difference between a box that works and a box still cooking with the power off." |

Anti-examples, all from our own published scripts: "Stage three." / "Stage four, then." / "Stage four is the strange one." None of them carries information, and each can be deleted with nothing lost. If a beat needs a label to make sense, the beat is in the wrong place.

## Wit

The register is warm and wry: personality lives in the phrasing, not in jokes you could lift out and quote.

- At most one wry beat per twenty seconds of narration, and never two in a row.
- Never in the hook, never in the payoff sentence. Those two carry the video.
- It lands on the thing: the number, the box, the model, the situation. Never on the viewer, never on a named person.
- No setup and punchline. A wry beat is usually one short sentence that undercuts the one before it.
- No puns on product names, no memes, no "am I right".
- If it needs explaining, it is a joke that failed. Cut it.

| Wrong | Right |
|-------|-------|
| "This thing is an absolute unit, am I right?" | "It gets there. It just takes its time." |
| "Your GPU is basically a very expensive space heater lol." | "You bought a card that does trillions of operations a second. Most of its day is spent waiting." |
| "Spoiler alert: it does not fit!!" | "It does not fit. Not at full precision, not on this box." |

## Direct Address

- The viewer's situation is named inside the first three sentences: "You've got a 4090." "You downloaded the model and it will not load."
- Ask a question only when the viewer can answer it from what they own ("How much memory is in your box?"). A question they cannot answer is filler.
- Second person for what the viewer does. First person plural for what we measured. First person singular in long-form for what I ran.

| Format | Person | Example |
|--------|--------|---------|
| Shorts, both bands | second person | "You download it. Then you hit the wall." |
| Long-form, concept-deep-dive and buyers-guide | second person | "You are choosing between two boxes." |
| Long-form, build-along | first person singular for the work, second person for the advice | "I loaded it at midnight and it fell over. You would want the FP8 build." |
| Our own measurements, any format | first person plural | "We measured twenty-two tokens a second on our Spark." |

## Pacing

Concrete first. Reach for the specific thing, the named product and the real number, before reaching for a metaphor. One idea per beat. New information every 5 to 8 seconds in a Short and at least every 30 seconds in long-form. State the honest trade-off when one exists ("you lose a little accuracy, and here's when you'd care") and only then. Rhythm: short sentence, short sentence, one longer sentence that explains. Read every line aloud; if you run out of breath or have to back up to parse it, it fails.

## What the Voice Is NOT

- **Not a slide deck.** Navigation is carried by content, never by numbering. See Navigation and Hard Constraint 10.
- **Not antithetical.** "Not X, but Y" at most once per script.
- **Not rhetorical.** Questions the viewer cannot answer are filler. Bad: "But what does this mean for the future?" Fine: "So which flag do you flip tonight?"
- **Not a template.** No First/Then/Finally skeleton, no "in this video we'll", no recap of a recap. The skeleton gate in `skills/script-gates` measures this.
- **Not condescending.** Never insult the builder reading over the beginner's shoulder; never assume the beginner is slow.
- **Not a salesman.** A product name is information, not an endorsement; the trade-off always rides along.

## Strategic Rationale

Concrete sentences are checkable; abstract ones are not. The wrong/right pairs exist so an agent pattern-matches instead of interpreting, and several of the Wrong entries are lines we actually published: they are here because we wrote them, not as hypotheticals.

The spoken-number rules exist because the narration is synthesized: a digit string is a coin flip in any voice engine, and a number without a referent is noise to a listener who cannot rewind.

Hard Constraint 10 exists because of a measured failure. Across our first thirty-eight scripts the word "stage" opened 8.6 percent of all sentences in the long band, and six of the ten most common sentence openers in the whole corpus were "stage one" through "stage five". Ten of twelve scripts used the pattern; eight of those landed on exactly five stages. Only one of them described anything sequential. The rule that produced it asked for labels that carry content, and what arrived was numbering with the content removed.

Agents writing prose load the sections above this one and skip this section.
