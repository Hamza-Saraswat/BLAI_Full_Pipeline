---
slug: 2026-08-29-glm-5-3-just-went-open-weight
workspace: shorts
stage: 04-script
---

# Drafts: GLM-5.3 just went open-weight

## Style pack

`style_rotation.py --pick` chose **silicon** (topic fit 2: gpu, vram terms; history empty after the
v2 ledger reset, so no rotation constraint). Recorded to the ledger on approval, per the rule.

## The 10 hook candidates

Scored per hook-library.md (one point each: payoff word in first five; product or number; length
band; frame-1 legible; no hype; true per brief; names the viewer's situation).

| # | Pattern | Hook | Score |
|---|---------|------|-------|
| 1 | Number shock | "Ninety-three gigabytes. That's the small one." | 6 |
| 2 | Number shock | "One bit per weight. Still ninety-three gigabytes." | 5 |
| 3 | Named contradiction | "GLM-5.3 went free today. Your GPU still can't have it." | 6 |
| 4 | Named contradiction | "GLM-5.3-Flash wakes eighteen billion. It eats three hundred twenty." | 4 |
| 5 | Wrong diagnosis | "Your GPU isn't too slow for GLM-5.3. It's sixty-one gigabytes too small." | 5 |
| 6 | Situation | "You saw open-weight. You reached for the download button." | 3 (slow for classic) |
| 7 | Decision | "Download GLM-5.3 or skip it? One number decides." | 4 |
| 8 | Tonight | (disqualified: nothing runs tonight on the viewer's box, and the pattern would promise it) | 0 |
| 9 | Price | "Free license. Ninety-three-gigabyte ticket." | 4 |
| 10 | Named contradiction | "The week's biggest open model fits exactly zero consumer GPUs." | 5 |

**Picks, one per draft, two different patterns (finding 12 rule):**
- Draft A (myth-bust): #3, Named contradiction.
- Draft B (number-first): #1, Number shock.

Unattended decision: #1 and #3 tie at 6; they are different patterns, so both survive. #10 was the
runner-up contradiction; #3 beats it by naming the viewer's own hardware.

## Writers

Two blind writers, private directories (`.local-builds/<slug>/draft-A/`, `draft-B/`), packets per
the stage contract. Neither sees the other. Gates run by each writer; the judge reads both after.

Both drafts passed all gates (validator advisories only: the assigned hook's referent, and the
stale-2.9wps pacing line; eval `gate1_ready: true` for both). Full drafts archived as
`[slug]-draft-A.json` / `-draft-B.json`; prose in each writer's private directory.

Live proof of the finding-9 demotion: the winning board scores `entity_spend 0.154` -- under the
old hard gate that alone would have blocked it; as an advisory it informs and blocks nothing.

## Judge report (fresh context, amended rubric: 8 rows, max 24)

**Winner: Draft B (number-first), 23 to 21.**

| Row | A (myth-bust) | B (number-first) |
|---|---|---|
| Hook | 3 | 3 |
| Payoff timing | 2 (fairness note applied; the break still lands ~6s) | 3 |
| Specificity | 3 | 3 |
| Voice | 3 | 3 |
| Navigation | 2 (s5/s6 commute) | 3 (locked chain) |
| Difference | 3 (empty ledger, by rule) | 3 |
| Repeat test | 2 | 2 |
| Teaching (new row) | 3 | 3 |
| **Total** | **21** | **23** |

**Drift ruling** (new rubric check): Draft A's "GLM-5.3" shorthand over Flash's 93.09 GB ruled
FAIR (headline's own wording; error direction conservative; description names Flash) -- and the
ruling is outcome-robust (a stricter cap still leaves B ahead 23-19). Symmetric flag on B's
"your gaming card holds thirty-two gigabytes" (flagship spoken as the viewer's own): same
conservative class, no cap, carried into notes_for_review for the human reviewer.

**Graft applied (the full two-sentence budget):** A's "The license opened. The memory didn't."
now closes B's s6 -- the most repeatable line in either draft, patching B's row-7 weakness; zero
rewriting of surrounding beats; the payoff line remains the last thing spoken. Post-graft: 133
words, ~36.5s at the measured 3.65 wps, inside the classic sweet band.

**No hook graft:** rows tied at 3; the rule did not trigger.

**What myth-bust needed:** the measurement inside the hook, and a spine whose beats cannot
commute. Recorded for the weekly retro.

