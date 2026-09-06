---
slug: 2026-09-06-dgx-spark-firmware-week-two-cv
stage: 04-script
winner: B (number-first)
score: "A 16 / 24, B 18 / 24"
---

# Drafts: DGX Spark firmware week -- five UEFI flaws, patch tonight

Both writers blind (separate kimi-k3 calls, private scratch dirs, no shared context). Writer A: how-to-three-moves with a Tonight-pattern hook. Writer B: number-first with a Number-shock hook. Both cleared the validator and all eval gates before judging (round-1 gate failures fixed inside each draft: A's step labels rewritten to carry actions, B's hook rewritten to carry the product).

## Draft A (as judged) -- how-to-three-moves

| Scene | Role | Narration | On-screen |
|-------|------|-----------|-----------|
| s01 | hook | Five commands close five firmware holes in your DGX Spark tonight. | 5 commands · 5 firmware holes |
| s02 | explain | Your Spark boots through UEFI, the firmware beneath your operating system. NVIDIA just patched five flaws there, three rated eight point two out of ten. | UEFI · 5 flaws · CVSS 8.2 |
| s03 | explain | The catch: the attacker must already hold privileged local access. Then an out-of-bounds write or a NULL pointer dereference can mean code execution. | Privileged local access required |
| s04 | explain | Step one: bring DGX OS current with apt. Run sudo apt update, then sudo apt dist-upgrade. | sudo apt update · sudo apt dist-upgrade |
| s05 | explain | Step two: run fwupdmgr refresh, then fwupdmgr upgrade, and approve the new firmware. | sudo fwupdmgr refresh · sudo fwupdmgr upgrade |
| s06 | payoff_close | Step three: reboot the box and let the update finish. Your Spark now boots the fixed firmware, all five holes closed. | UEFI 1.110.13 |

## Draft B (as judged) -- number-first

| Scene | Role | Narration | On-screen |
|-------|------|-----------|-----------|
| s01 | hook | Eight point two out of ten for your DGX Spark's boot firmware. NVIDIA just patched it this week. | 8.2/10 · DGX Spark firmware |
| s02 | explain | It's NVIDIA's severity score for five flaws in the UEFI. Three of those rate eight point two out of ten. That's the firmware that boots your Spark underneath DGX OS. | 5 flaws · 3 rated 8.2 |
| s03 | explain | Behind the score: an out-of-bounds write and a null pointer dereference in system firmware. Either can end in code execution and data tampering. | out-of-bounds write · NULL pointer dereference |
| s04 | explain | The attacker must already be privileged and local. This grows a foothold; it doesn't plant one. Every version before the fix is exposed. | privileged + local · 0 to 1.110.12 |
| s05 | payoff_close | The fix is five terminal commands, or the DGX Dashboard. Run them tonight, and your Spark boots the fixed firmware. | 5 commands → UEFI 1.110.13 |

## Score table (judge: kimi-k3, rubric as system file, both boards as user file)

| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 3 | 3 |
| 2 | Payoff timing | 2 | 3 |
| 3 | Specificity | 2 | 3 |
| 4 | Voice | 0 | 0 |
| 5 | Navigation | 3 | 3 |
| 6 | Difference | 3 | 2 |
| 7 | Repeat test | 2 | 2 |
| 8 | Teaching | 1 | 2 |
| | **Total** | **16** | **18** |

Row 4 was scored 0 for both drafts: neither glossed "out-of-bounds write" or "null pointer dereference" in the same breath (Hard Constraint 3). The judge recorded it as a shared pattern for the retro; the winner was repaired after judging (same-breath glosses added, see the script note's Decisions).

## Winner: B (number-first), 18-16

## Grafts applied (both from A, per the judge)

1. "Run sudo apt update, then sudo apt dist-upgrade." into B's fix beat -- B said "five terminal commands" without content; A's line says it better.
2. "Then fwupdmgr refresh and fwupdmgr upgrade." (adapted from A's s05 line) into the same beat -- same reason.

The Step one/Step two labels stayed behind: B is not a how-to, and an opened-but-unclosed count would cap its navigation row. No hook graft: A scored equal on row 1, not two higher.

## What the losing shape needed

The how-to had to pay its hook earlier -- the first command landed near mid-script, so it needed the apt line inside the first eight seconds or a hook promising understanding before action. It also needed plain-language glosses for its exploit terms and one sentence of why these holes outlive a reinstall.
