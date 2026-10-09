---
slug: 2026-10-09-ecosia-ditched-mistral-for-chi
stage: 04-script
generated_at: 2026-10-09
---

# Drafts: 2026-10-09-ecosia-ditched-mistral-for-chi

Two blind drafts on Kimi K3 from the same brief, different structures and hook patterns. Judge on Kimi K3 per judge-rubric.md.

### Draft A (myth-bust, hook: Ecosia dumped Mistral for open weights)
| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | Ecosia dumped Mistral for Chinese open weights. Costs roughly halved, its CEO says. | Ecosia dumped Mistral for open weights | costs roughly halved | 4.5 |
| s02 | explain | You've heard open weights are a hobby. They're model files anyone can download and run. Ecosia says quality went up, not down. | open weights = hobby? | model files anyone can run | 15M users | 7.6 |
| s03 | explain | Its new route is Melious, a German host serving only public weights, chiefly Z.ai's GLM. Mistral's Large four preview ranks eighth; every open model above it is Chinese. Even Mistral hosts GLM. | Ecosia → Melious → GLM | Mistral preview: 8th | even Mistral hosts GLM | 11.0 |
| s04 | explain | That family is downloadable tonight: GLM four point seven Flash on Ollama, a nineteen-gigabyte download. | ollama pull glm-4.7-flash | 19GB | tonight | 5.2 |
| s05 | payoff_close | The grain of truth: Ecosia still rents servers, and open weights don't scrub bias. The hobby excuse is dead. | still renting servers | run + inspect, bias included | hobby: dead | Build Local AI | 6.6 |

### Draft B (number-first, hook: AI bill: 50% off)
| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | Ecosia says switching its AI provider cut costs roughly in half. Quality went up, not down. | AI BILL: 50% OFF | QUALITY UP, NOT DOWN | 5.5 |
| s02 | explain | Not a benchmark you run for fun. It is the bill Ecosia pays for AI answers on search. | NOT A BENCHMARK | A REAL COMPANY'S AI BILL | 6.2 |
| s03 | explain | Open weights, model files anyone can download and serve, are supposed to be a hobby. The paying customer just dumped Mistral for GLM. | MYTH: OPEN WEIGHTS = HOBBY | RECEIPT: MISTRAL OUT, GLM IN | 7.9 |
| s04 | explain | On the open-model ranking, Mistral's Large four preview sits eighth. Every model ahead is Chinese, and even Mistral now hosts GLM. | OPEN-MODEL RANKING | 8TH: MISTRAL LARGE 4 PREVIEW | EVERY MODEL ABOVE: CHINESE | MISTRAL NOW HOSTS GLM | 7.2 |
| s05 | payoff_close | That family's small sibling, GLM four point seven Flash, is a nineteen-gigabyte download on Ollama tonight. The catch: Ecosia rents servers; open weights do not scrub bias. | GLM-4.7-FLASH ON OLLAMA | 19GB DOWNLOAD | CATCH: RENTED SERVERS, BIAS STAYS | 9.3 |


## Judge scores
| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 3 | 2 |
| 2 | Payoff timing | 3 | 3 |
| 3 | Specificity without cramming | 2 | 3 |
| 4 | Voice | 3 | 0 |
| 5 | Navigation | 3 | 3 |
| 6 | Difference | 3 | 3 |
| 7 | The repeat test | 3 | 2 |
| 8 | Teaching | 2 | 2 |
| | **Total** | **23** | **21** |

Winner: **A** (23 to 21).

## Grafts
- From B into A s03: "Mistral's Large four preview ranks eighth" -- A said "newest preview", which decays when Mistral ships a newer one; B names the ranked model. In-place swap, no structure or timing change.

## What the loser needed
Number-first needed the catch spoken before the payoff, so the last spoken sentence lands on the download instead of 'bias stays'; ending on the caveat breaks hard constraint 7, and that single inversion cost the draft the duel. Its hook also needed the tension inside the first five words: 'Ecosia says switching its AI provider' spends the opening on attribution, while something like 'Half price. Better answers. Ecosia's new AI bill.' would have put the number and the jolt up front.

## Gate results (winner, after graft)
- validate_storyboard: 0 blockers, 0 advisories.
- eval_short: all nine gates pass; entity_spend soft-advisory 0.227 (top2 Mistral + Ecosia present), recorded in the hub note.
- variety_check: no violations against the last five.
