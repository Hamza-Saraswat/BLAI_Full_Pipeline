---
slug: 2026-11-20-mapping-every-neuron-in-qwen3
format: smooth-explainer
structure: worked-example
style_pack: blueprint
value_types: TEACHES,REFRAMES
promise: After ninety seconds you can say what the Qwen3-8B neuron map is, why its switches are not screenshot luck, and what that buys you over re-prompting.
target_duration_s: 110
brief: 2026-11-20-mapping-every-neuron-in-qwen3-brief.md
drafts: 2026-11-20-mapping-every-neuron-in-qwen3-drafts.md
---

# Mapping every neuron in Qwen3-8B

## Decisions
- Two structures tried: worked-example (draft A, won 21-20) and myth-bust (draft B). A carried one moving example (your copy of Qwen, unpoked to German dial to labelled panel) through method, honest catch and payoff; the judge scored its hook 3 (product + tension in five words) against B's 2.
- Hook: "Your Qwen isn't a mystery anymore. Every neuron inside it got mapped." (named-contradiction, candidate 1 of 10, 6 pts). Situation and tonight patterns were barred by the ledger's last two entries.
- One graft from B: the German swing split into two sentences ("Unpushed, it writes German seven percent of the time. Pushed a single notch, it answers in German a hundred percent of the time."), curing A's only one-sentence-two-numbers break. Net cost about two seconds.
- Style pack: blueprint (topic fit, internals; previous video's pack was terminal).
- Value delivery: TEACHES lands on the s03-s06 run (what a push is, what a verified switch must beat, the atlas shape); REFRAMES lands on s09-s10 ("you don't re-prompt it. You look it up.").

## Hook candidates
1. Your Qwen isn't a mystery anymore. Every neuron inside it got mapped. (NC)
2. Four hundred forty-two thousand neurons. One of them speaks German. (NS)
3. You prompt it. You curse at it. Now you can open it. (S)
4. Your Qwen isn't broken. One of its neurons is. (WD)
5. This week, someone mapped every neuron in your local model. (T)
6. One number turns your Qwen German. A map found it. (NS/NC)
7. Qwen3-8B, the model you already run, has a public parts diagram. (NC)
8. You run Qwen3-8B. Someone just read its mind. (S/NC)
9. Stop re-prompting. Start reading the map. (WD)
10. The black box has a wiring diagram now. (NC)
11. A lab mapped all 442,368 neurons in Qwen3-8B. (NS)
12. One dial turns your Qwen German. Now you have the full list. (NS/NC)

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Your Qwen isn't a mystery anymore. Every neuron inside it got mapped. You run it in Ollama or LM Studio, and when it does something weird, you shrug and re-prompt. | Qwen's neurons: mapped | Ollama · LM Studio · shrug → re-prompt | 1080x1920, deep charcoal. Frame 1: small 'QWEN3-8B' tag above giant centered 'Qwen's neurons: mapped' (96px, safe area).... | hyperframes | centered-stack | 9.3 |
| s02 | explain | Inside, your Qwen is a stack of identical layers. Every word it writes climbs through every layer before the next word appears. Each layer is packed with neurons, the small calculators inside it. Until now, that whole climb was invisible to you. | a tall stack of identical layers | every word climbs them all | Manim, same charcoal palette. Frame 1: vertical stack of a tall stack translucent slabs centered, side label 'a tall sta... | manim | diagram-flow | 14.1 |
| s03 | explain | That map is built on one rude little move. A push means adding a fixed amount to one neuron's number at every word. No prompt. No fine-tune. One number, changed. | push = +constant at every word | no prompt · no fine-tune | Frame 1: single neuron card centered on the dimmed dot grid from s02, labelled 'one neuron'. Motion 0.35s. On 'fixed amo... | hyperframes | centered-stack | 10.3 |
| s04 | explain | Isn't poking a neuron just brain damage? Often, yes. A verified switch is a push that changes exactly one behaviour, like which language your copy answers in. It must beat a panel of matched random neurons and keep working on questions it has never seen. | random pushes barely move it | a switch moves one behaviour | Split screen. Frame 1: left half only, 'random neurons' header over ~30 tiny bars jittering near zero, '+a sliver/100' m... | hyperframes | split-compare | 15.5 |
| s05 | explain | Fermion Research ran that test on every neuron. Picture a mixing desk: four hundred forty-two thousand faders, one per neuron. About one fader in a hundred does one clear job. The rest do nothing you can name. One hundred thirty-two faders are verified switches. | 442,368 faders | 132 verified switches | Frame 1: a vast dim mixing-desk grid of faders filling the safe area, counter at 0. Motion 0.35s. On 'four hundred forty... | hyperframes | grid | 15.5 |
| s06 | explain | One fader is labelled German. Unpushed, it writes German seven percent of the time. Pushed a single notch, it answers in German a hundred percent of the time. A couple of notches later, it babbles. | L5.N5224 German | 7% to 100% in one notch | Giant number composition: '7%' redrawn as '100%' the moment narration says 'a hundred percent', one notch tick sliding o... | hyperframes | giant-number | 11.7 |
| s07 | explain | That's the limit: faders are independent and linear, neurons interact. Push past the sweet spot and the whole desk squeals. | faders: independent | neurons: they interact | Diagram-flow: two fader nodes drawn separately on 'independent and linear', then arrows knit them into one tangled web o... | hyperframes | diagram-flow | 6.2 |
| s08 | explain | Now the honest catch, because a cute German trick is not understanding. These switches set who is speaking and how. None of them sets whether the speaker is telling the truth. The map admits what it did not find. | switches set: who & how | truthfulness: no switch found | Frame 1: two atlas cards side by side, 'WHO is speaking' (persona icons) and 'HOW' (register dial), both ticked. Motion ... | hyperframes | split-compare | 13.4 |
| s09 | foreshadow | And no, this is not a chat-party trick. The same switches still fire in the raw pretrained model. The switch-hunting framework is promised, not shipped. The atlas itself is public tonight. | still fires pre-trained | framework: promised | atlas: public | Horizontal timeline across safe area. Frame 1: line draws in from left. Motion 0.35s. On 'raw pretrained model,' first n... | hyperframes | timeline | 10.7 |
| s10 | payoff_close | Your black box just grew a labelled panel. The next time Qwen does something weird, you don't re-prompt it. You look it up. | you look it up | Fermion Research | Rhymes with frame 1 of s01: same charcoal neuron field, now a few faders carry labels. Frame 1: centered line 'Your blac... | hyperframes | centered-stack | 7.9 |

## Notes for review
The German swing was split into two sentences by graft; check the added beat still sits inside s06's 11.7 s estimate. The analogy limit is spoken in s07 ("faders are independent and linear, neurons interact"). The close spends no number: "You look it up" is the payoff, with "Fermion Research" as the only on-screen credit. Rounds worth checking: "a hundred percent" for 100%, "one hundred thirty-two" for 132, both verbatim-compatible with the brief.
