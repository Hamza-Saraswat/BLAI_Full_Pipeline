# Voice Rules: Build Local AI

## Hard Constraints

These are errors. If narration, on-screen text, a title or a description contains any of these, rewrite before saving.

1. No hype words: revolutionary, insane, game-changer, mind-blowing, secret, unlock, seamless, next-level.
2. No fake urgency, no "they don't want you to know", no rage bait, no clickbait a viewer would resent after watching.
3. Every technical term gets a plain definition in the same breath, preferably as an appositive: "a replica, a second server that keeps a copy of everything".
4. Narration is read aloud by a voice engine. Numbers are written as words ("twenty-seven billion"), acronyms the way they are said ("H two hundred"), and every number names its unit and its referent ("twenty-four gigabytes of memory", "thirty-two billion parameters"). Digits belong on screen, never in narration.
5. Never make the viewer hold more than one new number at a time. A listener cannot rewind.
6. No claim that is not verified in our own setup or traced to a cited source in the research brief.
7. No spoken call to action, ever. The ask lives in the description and the pinned comment.
8. No em dashes in narration. Write like people talk; contractions are welcome.
9. Sentence length: hard cap 20 words; average at most 15 in Shorts and 18 in long-form.

## Sentence Rules

| Wrong | Right |
|-------|-------|
| "This revolutionary model changes everything." | "This model runs on one gaming GPU. Last year's needed four." |
| "It uses MoE architecture." | "It's a mixture of experts, a model that wakes up only a slice of itself for each word." |
| "It holds 24GB." | "It holds twenty-four gigabytes of memory." |
| "Make sure to like and subscribe." | (nothing: the ask never goes in narration) |
| "First, we... Then, we... Finally, we..." | "Stage two: we cut the old server off." (labels only when they help the viewer navigate) |
| "You may want to consider quantization." | "Quantize it. You lose a little accuracy; here's when you'd care." |
| "A 70B model needs a lot of VRAM." | "A seventy-billion-parameter model needs about forty gigabytes of memory, so it does not fit a gaming card." |

## Pacing

Concrete first. Reach for the specific thing, the named product and the real number, before reaching for a metaphor. One idea per beat. New information every 5 to 8 seconds in a Short and at least every 30 seconds in long-form. State the honest trade-off when one exists ("you lose a little accuracy; here's when you'd care") and only then. Rhythm: short sentence, short sentence, one longer sentence that explains. Read every line aloud; if you run out of breath or have to back up to parse it, it fails.

## Person by Format

| Format | Person | Example |
|--------|--------|---------|
| Shorts, classic | first person plural | "We run this at home on our box." |
| Shorts, smooth-explainer | second person; the viewer is the protagonist | "You download it. Then you hit the wall." |
| Long-form, my experiments | first person singular for what I did, second person for what you should do | "I loaded it on the Spark. You'd want the FP8 weights." |

## What the Voice Is NOT

- **Not antithetical.** "Not X, but Y" at most once per script.
- **Not rhetorical.** Questions the viewer cannot answer are filler. Bad: "But what does this mean for the future?" Fine: "So which flag do you flip tonight?"
- **Not a template.** No First/Then/Finally skeleton, no "in this video we'll", no recap of a recap. The slop gate in `skills/script-gates` measures this.
- **Not condescending.** Never insult the builder reading over the beginner's shoulder; never assume the beginner is slow.
- **Not a salesman.** A product name is information, not an endorsement; the trade-off always rides along.

## Strategic Rationale

Concrete sentences are checkable; abstract ones are not. The wrong/right pairs exist so an agent pattern-matches instead of interpreting. The spoken-number rules exist because the narration is synthesized: a digit string is a coin flip in any voice engine, and a number without a referent is noise to a listener who cannot rewind. Agents writing prose load the sections above this one and skip this section.
