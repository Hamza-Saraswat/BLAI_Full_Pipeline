---
slug: 2026-09-06-dgx-spark-firmware-week-two-cv
format: classic
structure: number-first
style_pack: silicon
value_types: EQUIPS,TEACHES
promise: After this Short you can check and patch all five UEFI flaws on your DGX Spark tonight: five terminal commands or the DGX Dashboard, landing on firmware 1.110.13.
target_duration_s: 51
brief: 2026-09-06-dgx-spark-firmware-week-two-cv-brief.md
drafts: 2026-09-06-dgx-spark-firmware-week-two-cv-drafts.md
---

# DGX Spark firmware week: five UEFI flaws, patch tonight (working title)

## Decisions
- Structures tried: how-to-three-moves (A) vs number-first (B). B won 18-16: it pays faster, spends numbers one at a time, and teaches the foothold model; the grafts below came from A.
- Hook: candidate 2 (Tonight pattern) for A, candidate 1 (Number shock) for B. Different patterns enforced per the hook library's divergence rule (finding 12).
- Grafts from A: the apt and fwupdmgr command sentences into B's fix beat -- B said "five terminal commands" without content. Step labels stayed behind (B is not a how-to).
- Post-judge audit fix: same-breath glosses for "out-of-bounds write" and "null pointer dereference" (the judge's shared row-4 zero; Hard Constraint 3); commands moved into their own scene so each is spoken where shown.
- Duration: 51 s against the 32-38 sweet band (validator warning accepted): the grafts plus glosses cost the seconds; the hard cap is 60.
- Value lines: EQUIPS via s05 (five commands or Dashboard, apt then fwupdmgr); TEACHES via s03/s04 (what the write classes mean and that they grow a foothold, not plant one).

## Hook candidates
1. Eight point two out of ten. Your DGX Spark's boot firmware just got patched. * (B, winner)
2. Five commands close five firmware holes in your DGX Spark tonight. (A)
3. Five firmware holes. Five commands. One sitting.
4. Your DGX Spark shipped with five open firmware holes.
5. The box under your desk boots through flawed firmware. NVIDIA just patched it.
6. You've never touched your Spark's firmware. This week you should.
7. Patch tonight or wait? The score says eight point two.
8. Five commands and your Spark's firmware is current tonight.
9. Your Spark isn't slow. Its boot firmware is exposed.
10. NVIDIA rates these firmware flaws eight point two. The patch is five commands.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|--------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Eight point two out of ten for your DGX Spark's boot firmware. NVIDIA just patched it this week. | 8.2/10 · DGX Spark firmware | Frame 1: the giant numeral 8.2 over /10 fills the safe area, fully legible at frame 1, motion onset immediate. On "boot firmware," a chip silhouette wipes in beneath the numeral. On "just got patched," a patch badge stamps onto the chip. | hyperframes | giant-number | 6 |
| s02 | explain | It's NVIDIA's severity score for five flaws in the UEFI. Three of those rate eight point two out of ten. That's the firmware that boots your Spark underneath DGX OS. | 5 flaws · 3 rated 8.2 | On "severity score," the 8.2 shrinks into a severity gauge. On "five flaws," five red markers pop across the chip. On "three of those," three markers glow brighter. On "boots your Spark underneath DGX OS," a two-layer stack draws with the UEFI slab below the DGX OS slab and a boot arrow rising through them. | manim | diagram-flow | 10 |
| s03 | explain | An out-of-bounds write means code scribbles past the end of its memory. A null pointer dereference means the firmware follows a pointer to nothing. Either can let it run code. | out-of-bounds write · NULL pointer dereference | On "out-of-bounds write", a write arrow spills past the end of a memory row into the neighboring cell; on "pointer to nothing", the pointer snaps to an empty cell; on "run code", a shell prompt flashes in the firmware layer. | manim | split-compare | 10 |
| s04 | explain | The attacker must already be privileged and local. This grows a foothold; it doesn't plant one. Every version before the fix is exposed. | privileged + local · 0 to 1.110.12 | On "privileged and local," a badged figure is already inside the door while the front door stays shut to outsiders. On "grows a foothold," the figure steps down from the OS layer into the firmware layer. On "every version before the fix," a version bar sweeps from 0 to 1.110.12, all of it red. | manim | timeline | 8 |
| s05 | explain | The fix is five terminal commands, or the DGX Dashboard. Run sudo apt update and sudo apt dist-upgrade. Then fwupdmgr refresh and fwupdmgr upgrade. | 5 commands: apt + fwupdmgr | On "five terminal commands", a count of 5 rises beside a terminal card; on "apt update" and "dist-upgrade", each line types as spoken; on "fwupdmgr refresh" and "fwupdmgr upgrade", the firmware lines type and an approve prompt flashes. | hyperframes | grid | 11 |
| s06 | payoff_close | Reboot, and your Spark boots the fixed firmware. All five holes, closed. | UEFI 1.110.13 | On "Reboot", the screen blacks and POST runs; on "boots the fixed firmware", the version readout resolves to UEFI 1.110.13; on "All five holes, closed", five red dots flip green; wordmark settles in the final half second. | hyperframes | centered-stack | 6 |

## Notes for review
Judge's two grafts applied: A's apt and fwupdmgr command sentences spoken in the fix beat. Audit fixes after judging: same-breath glosses for out-of-bounds write and null pointer dereference (the judge's row-4 zero); commands moved into their own scene so each is spoken where shown; firmware versions stay on-screen digits, never narrated; target runs long of the 32-38 s sweet band (validator warning, accepted: the grafts plus glosses cost the seconds). Firmware versions 1.110.12 and 1.110.13 are on-screen digits narrated as "every version before the fix" and "the fixed firmware"; the never-narrate-the-version rule overrides speaking them aloud. The five-item impact list was compressed to "code execution and data tampering" for breath. The privileged-local prerequisite stays explicit in s04; nothing claims exploitation in the wild. No analogy used, so no limit clause needed; "tonight" follows the brief's one-sitting framing. The severity sentence names "three of those" so the 8.2 score is not blended onto all five flaws.
