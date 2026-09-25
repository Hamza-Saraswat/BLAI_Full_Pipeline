---
slug: 2026-09-25-spark-center-fixes-the-dgx-spa
format: classic
structure: worked-example
style_pack: silicon
value_types: EQUIPS,TEACHES
promise: After this Short you can swap the DGX Spark's one-button update for Spark Center's selective one, and you know the kernel catch.
target_duration_s: 35
brief: 2026-09-25-spark-center-fixes-the-dgx-spa-brief.md
drafts: 2026-09-25-spark-center-fixes-the-dgx-spa-drafts.md
---

# DGX Spark updates fixed by Spark Center

## Decisions
- Structures tried: news-react-so-what (draft A) and worked-example (draft B); both cleared the rotation rule (last two ledger entries were how-to-three-moves and comparison-ladder). B won 23 to 22 on the judge rubric; no grafts (A's hook led row 1 by one point, under the two-point bar).
- Hook: candidate 2, situation pattern ("You press Update. The Spark decides."), polished to "You press Update, and the Spark decides." to clear the 5-word hook-sentence advisory; assigned to draft B for divergence from A's number-shock opener.
- Style pack: silicon (rotation pick, 3 keyword hits; previous pack signal excluded).
- Gates on the winner: validator 0 blockers / 0 advisories; eval_short all nine gates pass (entity_spend soft-advisory 0.235, top2 satisfied); variety_check clean against the last five.
- Judge packet's ledger section rendered empty (dict-shaped ledger, my tail failed); row 6 scored 3/3 for both drafts and the machine sameness gate had already passed both against the real ledger, so the verdict stands.
- Fixes applied inside draft B before judging: hook sentence lengthened to 5+ words, motion onset made explicit in the hook visual brief, catch beat split to its own scene to satisfy the abrupt-ending tail rule, close rewritten to name the DGX Dashboard entity.

## Hook candidates
1. One button updates everything on the DGX Spark. (number-shock, 6)
2. You press Update. The Spark decides. (situation, 7) *
3. Your Spark just updated Chrome. By itself. (situation, 6)
4. One button, no brakes, one forced reboot. (number-shock, 5)
5. The Spark's update button has no brakes. (named-contradiction, 6)
6. A 128 GB AI box, updating Chrome on its own. (number-shock, 5)
7. Your Spark reboots mid-update. On purpose. (situation, 6)
8. One maintainer just fixed NVIDIA's update button. (tonight, 6)
9. 128 GB of memory, zero update choices. (number-shock, 5)
10. The DGX Spark updates what it wants. (named-contradiction, 5)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | You press Update, and the Spark decides. One hundred twenty-eight gigabytes of memory. It upgrades Chrome. | You press Update. | The Spark decides. | 128 GB of memory | Frame 1: dark stage, the stock DGX Dashboard window centered, a blue 'Update Available' badge glowing, large text 'You press Update.' above it, small '128 GB of memory' below. No motion before t=0.30 s. At about t=0.4 s a cursor fades in and presses the button on 'You press Update.' On 'The Spark decides.' the badge scales up and holds. On 'It upgrades Chrome.' a Chrome icon rises into the update list beside the button. Motion onset explicitly at t=0.30 s (within 0.5 s): the word Update scales from 1.0 to 1.06 and settles; first and last 8 frames otherwise stable. | hyperframes | centered-stack | 5.2 |
| s2 | explain | That button drives apt, the package installer, across every repository. Then it reboots. | One button, every repo | apt: the package installer | Then it reboots | One rounded 'Update' button node center-left on a dark grid. On 'drives apt, the package installer,' thin lines fade out from the button toward a stack of repository boxes labeled Ubuntu, Chrome and VS Code, the boxes rising in one by one on 'across every repository.' On 'Then it reboots.' the whole diagram fades to black and a small reboot spinner scales in at center. | manim | diagram-flow | 4.5 |
| s3 | explain | Now the Spark gets brakes. Spark Center, one owner's open-source panel. You pick packages. A simulation shows what it will touch. | Spark Center | Pick your packages | Simulation shows what it will touch | Split screen. Left: the stock Dashboard's single grey Update button, dimmed. Right: the Spark Center Updates tab brightening in on 'the Spark gets brakes.' On 'You pick packages.' checkboxes fade in beside package rows and three tick themselves. On 'A simulation shows what it will touch.' a dependency panel rises below the list, package rows fading in one at a time, each indented under what pulled it in. | hyperframes | split-compare | 7.2 |
| s4 | explain | It never reboots. The monitor samples the GPU every two seconds. It catches the chip stuck at six hundred eleven megahertz. | GPU sampled every 2 s | Stuck at 611 MHz | A row of dark gauge dials. On 'It never reboots.' a small reboot icon fades in crossed out. On 'every two seconds' a '2 s' tick label pulses beside a sweeping gauge needle. On 'stuck at six hundred eleven megahertz' the clock-speed graph flatlines low, giant digits '611 MHz' scale in at center, and the pinned line glows red beneath them. | manim | giant-number | 7.2 |
| s5 | explain | A firmware flash can claim success and change nothing. Spark Center reads fwupd, the Linux firmware tool, and flags it. | fwupd: Linux firmware tool | Success reported, version unchanged | Flagged: mismatch | A horizontal timeline on a dark field. A flash event node fades in with a green check on 'claim success.' On 'change nothing' two version strings fade in side by side, identical. On 'reads fwupd, the Linux firmware tool' a small 'fwupd' label rises below the pair. On 'flags it' a red 'MISMATCH' tag scales in over the matching versions and the green check dims. | manim | timeline | 6.9 |
| s6 | explain | The catch: the kernel without NVIDIA's signed modules means no GPU driver. | Kernel ticked, modules unsigned|No GPU driver | Two small cards side by side: left card shows a kernel package checkbox ticked, right card shows a GPU chip icon going dark, joined by a broken trace line that draws on the phrase 'no GPU driver'. Amber warning tint on the right card only. Hard cut in, motion onset t=0.30 s, rise-in-place, no edge slides, visual change on both narration phrases. | hyperframes | grid | 4.1 |
| s7 | payoff_close | The DGX Dashboard decided everything. Now you decide. | Now you decide. | The single stock Update button from frame 1 sits center, dimmed; beside it a small checkbox list with one box ticking on the phrase 'Now you decide'. Wordmark settle in the last 0.5 s, final frame rhymes with frame 1. Motion onset t=0.30 s, fade and scale only, nothing enters from an edge. | hyperframes | centered-stack | 2.8 |

## Notes for review
- "One hundred twenty-eight gigabytes of memory" is the verbatim brief number (128 GB LPDDR5x unified); check the referent reads as memory of the box, not VRAM.
- The 611 MHz stuck-clock failure is attributed to what the monitor detects; we have not reproduced it on our own Spark (brief, Unverified).
- The kernel/signed-modules catch is the README's own warning; the script keeps it as the honest catch, per the brief's objection.
- Numbers spent: 128 GB (spoken), 2 s sampling (spoken), 611 MHz (spoken); port 11001 and 1 PFLOP stay out of this draft.
