# Script Structures

A structure is the shape of the story, not the length band (bands live in `skills/script-gates/formats.json`). Pick one per Short; never the same structure as the other pick that day or as the previous two runs in `output/structure-ledger.json`. The labelled-stages shape that v1 used for every smooth-explainer is now one option among eight.

| Structure | Shape | Best for | Key rule | Avoid when |
|-----------|-------|----------|----------|------------|
| `worked-example` | One concrete situation carried the whole way, advanced in 3-5 labelled stages ("stage two: we cut the old server off") | explainers, how-to with a visible state change | labels only when they help navigation; one example, never two | the topic has no process to walk through |
| `myth-bust` | State the belief everyone holds, show the measurement that breaks it, explain what is true instead, say when the myth is still right | "you need a 4090", "local is slow" | the measurement lands by second 4; the myth is named, not mocked | there is no number to break the belief with |
| `comparison-ladder` | Two named things on one axis, climbed in three rungs (cost, speed, what fits), ending in a one-line decision rule | DGX Spark vs RTX 5090, Q4 vs Q8 | each rung is one number pair; the decision rule is repeatable | more than two things, or no shared axis |
| `news-react-so-what` | What shipped (one sentence), the one consequence for home builders, the catch, what to do tonight | releases, price changes, policy | the consequence is spoken before the feature list; never a changelog read | the news has no local consequence |
| `how-to-three-moves` | Three moves from nothing to running; each move is a command or a setting shown on screen; the payoff is the thing running | install, load, serve, tune | moves are verbs; the third move ends with the result, not a recap | more than three moves are needed (make it long-form) |
| `contrarian-take` | The consensus, the evidence against it, the narrower claim we can defend, the trade-off | "cloud is cheaper", "bigger is better" | the narrower claim is smaller than the consensus, never just its opposite | we cannot cite the evidence |
| `story-first` | A named person or shop with a problem, the wall they hit, the local fix, the number that proves it worked | enterprise-privacy, clinic/law-firm cases | the person is a type, not a real named individual unless public; the number is real | no real case exists |
| `number-first` | Open on the number, then what it measures, then why it is surprising, then what changes because of it | benchmarks, memory math, bandwidth | the number is spoken in the first sentence and shown on screen at frame 1 | the number needs more than one sentence of setup |

## Universal physics (every structure)

- Payoff starts by second 4; by second 8 the viewer has learned one concrete thing.
- New information every 5-8 seconds; one concept per Short.
- Ending per band: `classic` stops within 1 s of the payoff; `smooth-explainer` resolves the opening and may recap in two sentences.
- No spoken call to action. The ask lives in the description.

## Choosing

Match the brief, not the mood: a measurement suggests `number-first` or `myth-bust`; a release suggests `news-react-so-what`; a process suggests `worked-example` or `how-to-three-moves`; a case suggests `story-first`. When two fit, take the one the ledger has not seen longest.
