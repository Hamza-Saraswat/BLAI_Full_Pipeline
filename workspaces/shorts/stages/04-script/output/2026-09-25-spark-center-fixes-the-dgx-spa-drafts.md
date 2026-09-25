---
slug: 2026-09-25-spark-center-fixes-the-dgx-spa
stage: 04-script
generated_at: 2026-09-25T12:15:44Z
---

# Drafts: DGX Spark updates fixed by Spark Center

Both drafts written blind by separate kimi-k3 calls from the same brief; both passed validator (0 blockers) and all nine eval gates before judging.

### Draft A (news-react-so-what, hook: One button. Every update.)

**s1 (hook, giant-number, 6.9 s)** One button updates everything on the DGX Spark. You press it when the badge appears. Every package, then a reboot.
- on screen: One button. Every update.|Every repo it can find|Forced reboot

**s2 (explain, centered-stack, 4.5 s)** On September twenty-fourth, one owner posted Spark Center to NVIDIA's forum. Open-source, free to inspect.
- on screen: Sep 24, 2026|Spark Center|Open-source license

**s3 (explain, diagram-flow, 6.9 s)** For your box, you pick the packages. A dry run shows what apt, the installer, will touch. No reboot unless you decide.
- on screen: You pick the packages|apt dry run|No reboot unless you say

**s4 (explain, grid, 5.9 s)** The monitor reads the GPU every two seconds. It catches one stuck at six hundred eleven megahertz.
- on screen: GPU gauges, sampled 2 s|611 MHz: failure flagged

**s5 (explain, split-compare, 7.2 s)** The catch: one maintainer, one variant of the box tested. Tick the kernel without NVIDIA's signed modules and the GPU driver is gone.
- on screen: 1 maintainer, 1 variant|Kernel ticked, modules unsigned|GPU driver gone

**s6 (explain, grid, 4.1 s)** Tonight: clone the repo, run the installer, open port eleven thousand one.
- on screen: git clone, ./install.sh|127.0.0.1:11001

**s7 (payoff_close, centered-stack, 2.8 s)** The Dashboard updated everything. Spark Center asks.
- on screen: The panel asks.

### Draft B (worked-example, hook: You press Update.)

**s1 (hook, centered-stack, 5.2 s)** You press Update, and the Spark decides. One hundred twenty-eight gigabytes of memory. It upgrades Chrome.
- on screen: You press Update. | The Spark decides. | 128 GB of memory

**s2 (explain, diagram-flow, 4.5 s)** That button drives apt, the package installer, across every repository. Then it reboots.
- on screen: One button, every repo | apt: the package installer | Then it reboots

**s3 (explain, split-compare, 7.2 s)** Now the Spark gets brakes. Spark Center, one owner's open-source panel. You pick packages. A simulation shows what it will touch.
- on screen: Spark Center | Pick your packages | Simulation shows what it will touch

**s4 (explain, giant-number, 7.2 s)** It never reboots. The monitor samples the GPU every two seconds. It catches the chip stuck at six hundred eleven megahertz.
- on screen: GPU sampled every 2 s | Stuck at 611 MHz

**s5 (explain, timeline, 6.9 s)** A firmware flash can claim success and change nothing. Spark Center reads fwupd, the Linux firmware tool, and flags it.
- on screen: fwupd: Linux firmware tool | Success reported, version unchanged | Flagged: mismatch

**s6 (explain, grid, 4.1 s)** The catch: the kernel without NVIDIA's signed modules means no GPU driver.
- on screen: Kernel ticked, modules unsigned|No GPU driver

**s7 (payoff_close, centered-stack, 2.8 s)** The DGX Dashboard decided everything. Now you decide.
- on screen: Now you decide.


## Judge verdict (kimi-k3, rubric as system packet)

SCORES

| row | A | B |
|-----|---|---|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 3 | 3 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 2 | 3 |
| 5 Navigation | 3 | 3 |
| 6 Difference | 3 | 3 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 2 | 3 |
| TOTAL | 22 | 23 |

WINNER: B, by 1 point

GRAFTS: none. A's hook beats B's by only one point on row 1, under the two-point bar; A's install beat ("clone the repo, run the installer, open port eleven thousand one") has no counterpart line in B it improves, and inserting it before B's payoff close would force re-timing and restructure, so it stays out.

WHAT THE LOSER NEEDED: A needed to show mechanism, not just features: it never says why the stock button reaches Chrome (apt across every repo) and drops the fwupd version-compare entirely, so the viewer leaves knowing THAT Spark Center works, not WHY it can be trusted. It also admits zero wry beats in its own notes, capping voice at clean-and-correct where B's "Now the Spark gets brakes" lands one.

PAYOFF LINE OF THE WINNER: The DGX Dashboard decided everything. Now you decide.

## Record
- Winner: draft B (worked-example), saved as `2026-09-25-spark-center-fixes-the-dgx-spa-script.md` and `2026-09-25-spark-center-fixes-the-dgx-spa-storyboard.json`.
- Grafts: none (judge found none legal or needed).
