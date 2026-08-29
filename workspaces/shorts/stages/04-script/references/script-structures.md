# Script Structures

A structure is the shape of the story, not the length band (bands live in `skills/script-gates/formats.json`). The script stage picks the **two** best-fitting structures and writes a draft of each; the judge picks the winner. Both must clear the rotation rule: neither may be the structure of either of the last two scripts in `output/script-ledger.json`.

| Structure | Shape | Best for | Key rule | Avoid when |
|-----------|-------|----------|----------|------------|
| `worked-example` | One concrete situation carried the whole way, advanced in 3-5 turns, each named by what changes | explainers, mechanisms, anything with a before and after | one example, never two; each turn changes the state of that example, and you say what changed | the topic has no state that moves |
| `myth-bust` | State the belief everyone holds, show the measurement that breaks it, explain what is true instead, say when the myth is still right | "you need a 4090", "local is slow" | the measurement lands by second 4; the myth is named, not mocked | there is no number to break the belief with |
| `comparison-ladder` | Two named things on one axis, climbed in three rungs (cost, speed, what fits), ending in a one-line decision rule | DGX Spark vs RTX 5090, Q4 vs Q8 | each rung is one number pair; the decision rule is repeatable | more than two things, or no shared axis |
| `news-react-so-what` | What shipped, the one consequence for home builders, the catch, what to do tonight | releases, price changes, policy | the consequence is spoken before the feature list; never a changelog read | the news has no local consequence |
| `how-to-three-moves` | Three moves from nothing to running; each move is a command or a setting shown on screen; the payoff is the thing running | install, load, serve, tune | moves are verbs the viewer performs; the third move ends with the result, not a recap | more than three moves are needed (the idea is too big for a Short; shrink it or drop it) |
| `contrarian-take` | The consensus, the evidence against it, the narrower claim we can defend, the trade-off | "cloud is cheaper", "bigger is better" | the narrower claim is smaller than the consensus, never just its opposite | we cannot cite the evidence |
| `story-first` | A named person or shop with a problem, the wall they hit, the fix, the number that proves it worked | a real thread, a real failure, an enterprise case | the person is a type unless they are public; the number is real | no real case exists |
| `number-first` | Open on the number, then what it measures, then why it is surprising, then what changes because of it | benchmarks, memory math, bandwidth | the number is spoken in the first sentence and shown on screen at frame 1 | the number needs more than one sentence of setup |

## Positional labels

Only `how-to-three-moves` and `worked-example` may use them, and only for steps the viewer performs. At most three, each naming the action ("Step two: quantize it"), ascending from one. Everything else navigates by content: see "Navigation" in `../../../../brand-vault/voice-rules.md`, which is the canonical list of transitions and the source of the anti-examples.

Numbering things that are not steps is the single most common failure in our published corpus. Components are pieces, layers are layers, reasons are reasons, and moves in an argument are none of the above. If you are tempted to write "stage four", ask what changed since stage three; if nothing did, the beat is decoration.

## Universal physics (every structure)

- Payoff starts by second 4; by second 8 the viewer has learned one concrete thing.
- New information every 5 to 8 seconds; one concept per Short.
- Nothing follows the payoff. `classic` stops within a second of it; `smooth-explainer` may resolve the opening in at most two sentences. No ask, no tease.
- The viewer's situation is named inside the first three sentences.

## Choosing the two

Match the brief, not the mood. A measurement suggests `number-first` or `myth-bust`. A release suggests `news-react-so-what`. A process the viewer performs (the brief's `has_process` is true) suggests `how-to-three-moves` or `worked-example`. A mechanism suggests `worked-example`. A real case suggests `story-first`. A widely held belief with evidence against it suggests `contrarian-take`.

Pick the best fit as draft A. For draft B, pick the best-fitting structure that would tell the story a **different** way, not the second-closest cousin: if A is `worked-example`, B is more useful as `number-first` or `myth-bust` than as `how-to-three-moves`. The point of two drafts is two shapes, not two phrasings.
