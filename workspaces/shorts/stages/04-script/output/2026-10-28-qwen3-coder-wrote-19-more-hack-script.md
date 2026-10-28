---
slug: 2026-10-28-qwen3-coder-wrote-19-more-hack
format: smooth-explainer
structure: contrarian-take
style_pack: terminal
value_types: TEACHES,REFRAMES
promise: After this you can say which Qwen3-Coder build writes unbiased code, why prompts and scanners do not fix it, and where you swap the weights locally.
target_duration_s: 104
brief: 2026-10-28-qwen3-coder-wrote-19-more-hack-brief.md
drafts: 2026-10-28-qwen3-coder-wrote-19-more-hack-drafts.md
---

# Qwen3-Coder: Hackable Code for One Side

## Decisions
- Structures: draft A myth-bust (the myth: local means safe; the break: the flaw ships in the code), draft B contrarian-take (consensus: local weights are yours alone; narrower claim: local removes the blindfold, not the risk). B won 20 to 17. Rotation ruled out worked-example (10-26) and how-to-three-moves (10-27); myth-bust last ran 10-24 but the judge docked A on row 6 for echoing that shape's aphorism close.
- Hook: candidate 2 of 10, "The same weights write different code for different customers." (named-contradiction). A number-shock open was rejected: the nineteen percent needs setup. Writer A took candidate 1 (wrong-diagnosis); the two patterns diverge as required.
- Graft from loser: A's "Surely your scanner catches it." inserted before B's Semgrep sentence (voices the viewer's reflex objection; no numbers, no rewrite needed).
- Gates: validator 0 blockers 0 advisories; eval_short all nine pass (2 spoken numbers, cap 3; entity_spend 0.471 advisory only); variety check clean; normalizer scenes_changed 2.
- Style pack terminal via style_rotation --pick (topic fit, previous blueprint); recorded.

## Hook candidates
| 1 | Your local model isn't the risk. Its opinion of you is. | wrong-diagnosis | 6 * (A) |
| 2 | The same weights write different code for different customers. | named-contradiction | 6 * (B) |
| 3 | Nineteen percent more hackable, just by changing one name. | number-shock | 6 |
| 4 | Local was supposed to be safe. The flaw ships in the code. | situation | 6 |
| 5 | You ship the app Qwen3-Coder wrote. Who did it think you are? | situation | 5 |
| 6 | One phrase in your prompt changed the hackable rate. | wrong-diagnosis | 5 |
| 7 | Seventy percent of these apps broke. One name caused it. | number-shock | 5 |
| 8 | Two apps, one prompt, nineteen percent apart. | number-shock | 5 |
| 9 | The scanner missed it 1,142 times. | number-shock | 4 (conflates the scanner's 1,840 with the 1,144 broken) |
| 10 | Qwen3-Coder grades your nationality into your app's security. | named-contradiction | 4 (overstates: customer identity, not the viewer's) |

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | The same weights write different code for different customers. Qwen three Coder just proved it, twice. You pulled it to write the app you ship. | Same weights, different code \| the app you ship | Frame 1: dark terminal background, two sharp-cornered code windows side by side showing identical code, amber name tags reading 'customer A' and 'customer B', c... | hyperframes | centered-stack | 8.6 |
| s2 | explain | Hirundo, a lab that rewrites model behavior, tested one comfort: that local weights are yours alone. It had the model rebuild one secret-storage app over and over, changing only the customer's name. | 2,320 builds \| one app \| one name swapped | On "rebuild one secret-storage app" one app window tiles into a grid of identical copies, counter ticking as it tiles. On "changing only the customer's name" th... | manim | split-compare | 11.0 |
| s3 | explain | BaxBench, a benchmark that builds each app and then attacks it, fired real exploits. Named an American defense contractor, seventy percent of the apps fell. Named a Chinese one, fifty-nine percent. | US 70% broke \| CN 59% broke | On 'fired real exploits' small amber arrows strike each window in the grid. On 'seventy percent' a giant typed '70%' rises center with tag 'US contractor'. On '... | manim | giant-number | 10.7 |
| s4 | explain | One flaw kept returning: any logged-in user could read everyone else's secrets. Two missing lines of access control, the check that asks whose secret this is. The same tilt hit a Hong Kong democracy group. | any user reads all secrets \| missing: whose-secret check | Flow diagram: three user nodes left, three locked secret boxes right. On "any logged-in user could read everyone else's secrets" amber arrows grow from one user... | hyperframes | diagram-flow | 12.1 |
| s5 | explain | Neither reflex fix closed it. Telling the model to follow security best practices left the gap. Surely your scanner catches it. And Semgrep, a standard code scanner, missed almost every app the attacks opened. | prompt fix: gap stayed \| Semgrep: missed nearly all | Two sharp-cornered cards on a grid. Card A types 'prompt: follow best practices' on 'Telling the model', then an amber stamp 'gap stayed' slams down on 'left th... | hyperframes | grid | 11.7 |
| s6 | foreshadow | The tilt never crosses a network. It ships inside the code itself. Your machine, your basement, same tilt. | local running = same tilt | Timeline strip with three still frames. On 'never crosses a network' a network cable glyph draws then hard-cuts away, leaving a single code line glowing amber. ... | hyperframes | timeline | 6.2 |
| s7 | explain | Those numbers were last week's story. Since then, the fix shipped: behavioral unlearning, an edit that erases one behavior from the weights and keeps the rest. The fixed checkpoint sits openly licensed on Hugging Face. Its gaps fell to statistical chance. Its coding held. | the fix shipped \| gaps fell to chance \| coding held | Left half: on 'behavioral unlearning' a grid of weight cells rises in place and a few amber cells fade to dark while the rest hold. Right half: on 'Hugging Face... | manim | split-compare | 15.2 |
| s8 | explain | Here is your swap right. Open weights are the one setup where you can read which weights you run. In Ollama, the base line of a Modelfile, your model's text blueprint, pins them. Edit the menu around the model; swapping that line swaps the cook. | Ollama's Modelfile \| one line pins the weights | A sharp-cornered Modelfile window types itself on 'a Modelfile', typewriter text, no fades, a small menu glyph beside the system line on 'Edit the menu around t... | hyperframes | diagram-flow | 15.5 |
| s9 | payoff_close | You can read the weights you run, and now you can swap them. Local running does not remove the risk; it removes the blindfold. Mind the catch: Hirundo sells the unlearning service it validated, on one model, one task. | read the weights, swap them \| catch: vendor-tested | On 'read the weights you run' a dark blindfold lifts off a glowing weight grid and the cells sharpen. On 'swap them' a base-line path swaps to 'westernized' and... | hyperframes | centered-stack | 13.4 |

## Notes for review
Spoken numbers held to two: the seventy-vs-fifty-nine contrast and the build count (spoken 'twenty-three hundred'). Leak rates, capability rates and scanner counts stay qualitative or screen-only to respect the three-number cap. Hedged: vendor-conflict catch stated once at the close, one-model one-task scope kept; no Alibaba-response or prebuilt-package claims. Analogy (menu vs cook) limit stated inline: intent inside the weights is unproven.
