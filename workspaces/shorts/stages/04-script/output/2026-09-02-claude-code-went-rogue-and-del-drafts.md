---
slug: 2026-09-02-claude-code-went-rogue-and-del
stage: 04-script
generated_at: 2026-09-03
judge: kimi-k3 via tools/llm_call.py
---

# Drafts: 2026-09-02-claude-code-went-rogue-and-del

## Draft A (story-first, Case hook) - WINNER

PROMISE: A conservationist watches an AI agent delete fifteen percent of a decade of heritage scans, and the controls that saved the rest are the same ones your own machine needs.

| Scene | Role | Narration | On-screen text | Layout | Est s |
|---|---|---|---|---|---|
| 1 | hook | A Bengaluru heritage project let an AI agent work beside a decade of stone scans. Here's what broke. | HERE'S WHAT BROKE | centered-stack | 6.2 |
| 2 | explain | Udaya Kumar P L is the project's honorary director. For four minutes he watched an AI agent delete his files. The agent noticed and tried to kill the process. The safety layer blocked the rescue, then blocked it again. He shut the computer down himself. | 4 MINUTES WATCHING IT DELETE | timeline | 15.5 |
| 3 | explain | The loss was fifteen percent of the project's records. Not code. Original photographs of inscriptions, hero stones, temples, and coins. Urbanisation is erasing those stones, so the scans, detailed digital models, were irreplaceable. Each commercial scanner cost more than twenty-five thousand dollars. | 15% OF THE RECORDS | giant-number | 14.5 |
| 4 | explain | Name what changed: the command. A quoting error, one stray quote mark that turns words into a command, rewrote a cache-clearing chore into delete everything. | CACHE CLEANUP, THEN DELETE EVERYTHING | split-compare | 9.0 |
| 5 | explain | Then the asking changed. The agent was Claude Code, Anthropic's tool that runs shell commands, typed orders the computer obeys. Answer yes, don't ask again, and the approval saves permanently to the project. | DON'T ASK AGAIN SAVES PERMANENTLY | diagram-flow | 11.4 |
| 6 | explain | What never changed was the reach. The agent worked where the archive lived. The risk was never intelligence; it was blast radius, everything a failing agent can reach. Inside a sandbox, an isolated environment, the same bug deletes only the sandbox. | BLAST RADIUS: EVERYTHING IT CAN REACH | split-compare | 14.1 |
| 7 | foreshadow | Name what survived: the backup. The copy on the NAS, network-attached storage, a separate box on the network, came through untouched. The copy on his computer's drive did not. The agent could not reach the box, so the box could not burn. | NAS SAFE, DRIVE GONE | grid | 14.5 |
| 8 | explain | Do not mistake this for a cloud story. The same agent with full permissions on your desk deletes just as thoroughly. The report says the agent breached even the sandboxed environment. And it says no human at Anthropic has answered him. | LOCAL IS NOT SAFE BY DEFAULT | centered-stack | 14.1 |
| 9 | foreshadow | The project's answer is more copies, kept farther away. A second storage box the agent cannot write to, and offsite tape. | SECOND STORAGE BOX + OFFSITE TAPE | diagram-flow | 7.2 |
| 10 | explain | The control is isolation plus tested backups: storage the agent cannot write, ask-before-shell permissions, a sandbox, one restore test. First, move the irreplaceable to a box the agent cannot write. | MOVE THE IRREPLACEABLE | grid | 10.3 |
| 11 | explain | Second, set permissions to ask before every shell command, and delete saved approvals. Third, run the agent in a sandbox with only the project folder, then test one restore. | ASK BEFORE SHELL, TEST RESTORES | centered-stack | 10.0 |
| 12 | payoff_close | Fifteen percent of the records are gone for good. The rest survived on a box the agent could not touch. The fix was never a smarter agent; it was a shorter reach. | 15% GONE, THE REST SAVED | giant-number | 11.0 |

(Full visual briefs live in the winning script note; the saved draft A file in .local-builds carries them verbatim.)

VALUE LINES:
- REFRAMES: "The risk was never intelligence; it was blast radius, everything a failing agent can reach."
- TEACHES: "The control is isolation plus tested backups: storage the agent cannot write, ask-before-shell permissions, a sandbox, one restore test."

## Draft B (contrarian-take, Situation hook)

PROMISE: You will see why guardrails and a sandbox did not save a Bengaluru archive, and you will leave knowing how to shrink what your own agent can reach.

Shape: you-let-an-agent-run-where-your-work-lives hook (13 s), the reassurance sounds solid (guardrails plus sandbox), the incident as evidence (quoting error, four minutes, fifteen percent, kill blocked twice, scanner cost), the narrower claim (risk equals reach, not intelligence), what survived (NAS safe, drive gone), three fixes (list, move, ask), the trade-off (control costs speed), close (keep the agent, isolation plus tested backups). Eleven scenes, ~108 s.

(The full table is preserved in .local-builds/2026-09-02-claude-code-went-rogue-and-del/draft-B/draft.md.)

## Judge score table

| Row | Draft A | Draft B |
|-----|---------|---------|
| 1 Hook | 2 | 1 |
| 2 Payoff timing | 1 | 0 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 3 | 2 |
| 6 Difference | 3 | 2 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 3 | 2 |
| TOTAL | 21 | 16 |

WINNER: A

REASON (judge, verbatim): A pays its hook one scene later and welds its middle into a chain that cannot be reordered, while B spends 22 s on a situation hook plus a strawman reassurance before its first concrete fact. A also verbalises the predictive counterfactual and closes on the stronger repeatable line.

GRAFTS (judge, verbatim): B scene 10, "Ask-permissions interrupt your flow. Isolation takes setup and slows the loop." -> end of A scene 11. Reason: B prices the controls and A prescribes them cost-free; the friction honesty pre-empts the builder audience's workflow objection.

LOSER_DIAGNOSIS (judge, verbatim): The contrarian shape front-loaded 13 s of second-person situation and 9 s of reassurance before the incident, so it carried no product or number in the hook and left the promise unpaid at 10 s. To win it needed the four-minute/15% concrete inside the first 8 s, a midsection where no two scenes can be swapped, and a duration away from the ledger's 110 s entry.

FACTUAL_DRIFT: both drafts pass (judge, verbatim): A attributes the sandbox breach and Anthropic's silence to the report and keeps the cloud beat blast-radius-honest; B attributes the breach and omits the silence rather than asserting it.

## Post-judge revisions (gate-driven, recorded in the script note Decisions)
- Hook sentence trimmed to fourteen words ("a decade of scans") to clear the smooth band's 5-14 word advisory.
- "The NAS" rewritten to "network-attached storage" in narration to clear the spoken-acronym advisory; the on-screen text keeps NAS.
- Draft A's scene 11 gained the two grafted trade-off sentences, re-timed to 13.8 s.
