# Hook Library

The first thirty seconds of a long-form episode is a spec, not a mood. Four lines have to land, in this order, and nothing else belongs in front of them. Write eight hook candidates, score them, keep one.

## The four lines

| Line | Lands by | Job | Fails when |
|------|----------|-----|------------|
| Hook | sentence 1 | One concrete thing: a number, a named product, a wrong diagnosis, a failure, a decision | it needs a sentence of setup first |
| Why you | inside the first three sentences | Names the viewer's situation in second person: what they already own or already tried | it says "users" or "people often" |
| Promise | 0:30 | What the viewer can do or decide by the end, in one sentence, no list | it promises understanding in general instead of one usable thing |
| The number | 0:20 | The one surprising number, spoken and shown on screen at the same moment | the number arrives after the promise, or only on screen |

The promise is a sentence the viewer could hold you to: "by the end you will know which of these two boxes to buy, and the one number that decides it". Not "we will explore memory bandwidth".

## Hook patterns

| Pattern | Template | Example | Best for | Avoid when |
|---------|----------|---------|----------|------------|
| Number shock | "[number with unit], [the comparison that stings]" | "Twenty-two tokens a second. The card that costs twice as much does thirty." | `buyers-guide`, `concept-deep-dive` | the number needs setup to mean anything |
| Wrong diagnosis | "Your [thing] isn't [what you blame]. Its [real cause] is." | "Your model isn't too big. Your memory doorway is too narrow." | `concept-deep-dive` | the real cause takes two sentences to name |
| The failure you hit | "I [did the thing]. [What broke], [when]." | "I loaded it at midnight. It fell over before the first token." | `build-along` | nothing actually broke |
| The decision | "[A] or [B]? One number decides, and it isn't [the obvious one]." | "Spark or 5090? One number decides, and it isn't teraflops." | `buyers-guide` | there is no single deciding axis |
| The situation | "You [did the ordinary thing]. Then [the wall]." | "You downloaded the seventy-billion-parameter model. It will not load." | `concept-deep-dive`, `build-along` | the viewer has never been in that situation |

## Scoring the eight

Give each candidate one point for each row it satisfies. Keep the highest; on a tie prefer the one a viewer could repeat to a friend.

| Point | Test |
|-------|------|
| Concrete | it carries a number, a named product, or a named failure |
| No setup | it makes sense as the very first thing the viewer hears |
| Length | 5 to 16 words, sayable in one breath |
| Second person or first person singular | "you" for the viewer's situation, "I" for what I ran; never "one might", never "users" |
| Legible on screen | it survives being cut to eight words as the opening card |
| Honest | it is true per the brief, and the episode actually delivers it |
| Not the title | it is not the video title read aloud; the package stage writes the title separately |

Record all eight in the script note under `## Decisions`, with the winner marked.

## Anti-patterns

- **Channel intro.** No "welcome back", no "hey everyone", no wordmark before the first sentence. The wordmark is an end card.
- **Agenda slide.** No "here is what we will cover". A chapter list belongs in the description, not in the narration.
- **"In this video".** Also "today we", "let's dive in", "before we get started". `validate_longform.py` flags all four.
- **Reading the title aloud.** The viewer clicked the title. Repeating it spends the first five seconds saying nothing new.
- **Deferred payoff.** "Stay to the end and I will show you the number." Show the number at 0:20 and earn the rest.

## A complete opening

> I loaded a seventy-billion-parameter model on the Spark at midnight, and it fell over before the first token. You have probably hit the same wall on a smaller box: the file fits on disk, the model will not run. By the end of this you will know which number to check before you download anything, and the one flag that fixed it here. It took the memory from a hundred and twelve gigabytes down to thirty-eight.

Hook, why you, promise, number: four sentences, about twenty-two seconds, nothing in front of them.
