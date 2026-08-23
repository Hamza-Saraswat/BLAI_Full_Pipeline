# Judge record: 2026-08-23-unsloth-lan-remote

Judged against `references/judge-rubric.md` and `brand-vault/voice-rules.md`.
Both drafts cleared the validator with zero blockers. `entity_spend` and `top2` were
excluded from consideration: the extractor behind them is defective, so draft A's `top2`
warning is not evidence about the writing and was not scored.

`output/script-ledger.json` is empty, so row 6 could not be scored against history.
**Row 6 was therefore scored on distance from the obvious treatment of this topic** -- the
tutorial that writes itself from the release notes: state the feature, walk the settings,
flip the switch, append the security note.

---

## Draft A -- `how-to-three-moves`, 101s, 10 scenes

> Unsloth won't answer from the couch

Your model runs on the box in the other room. You are on the couch, and Unsloth will not answer your laptop. That is not a bug. By default Unsloth answers on one twenty-seven dot zero dot zero dot one. That address is loopback. It is the one a machine uses to talk to itself. So nothing outside that machine can reach it. That is deliberate. Unsloth does document a Cloudflare tunnel, a relay that gives your server a public web address. That tunnel is the right tool from a hotel. From your own couch, it routes your rig through somebody else's service. To reach a room away. Step one: open Settings and switch on network access. Or launch it with the host flag set to all zeros. Either one is a wildcard bind. Unsloth listens on every address the machine has, not just its own. Step two: change the admin password Unsloth generated for you. It stops and asks, because the toggle will not move until you do. Now pick up the laptop. Unsloth shows you the address to type and a code you can scan. The toggle takes effect without a restart, so nothing has to reload. Here is the part the release notes do not lead with. Server-side tools run as your user. Anyone who reaches that server with your API key can run code on that machine. That is Unsloth's own banner. It sits on the same docs page as the tunnel. Network reach and code execution are the same switch here. So pass the disable tools flag unless you meant to hand that out. Now Unsloth answers your laptop from the other room, with nothing in the path. The password change is forced, and the tools decision is yours.

---

## Draft B -- `myth-bust`, 96s, 9 scenes

> Unsloth won't answer from your couch

Unsloth will not answer from your couch. Your model is in the other room. You are not. The fix you reach for is a tunnel through somebody else's service. Unsloth binds to loopback, the address a machine uses to talk to itself. The docs call that this machine only. Nothing outside can reach it. That is the default, and it is deliberate. Change what it listens on, and the tunnel stops being necessary. In the desktop app that is Settings, then API keys, then the local network switch. It ships in preview. Or start it from the terminal with dash H, zero dot zero dot zero dot zero. That is a wildcard bind, listening on every address the machine has instead of only its own. It does not just flip on. Unsloth stops and makes you replace the auto-generated admin password first. After that it shows you the address to type on the other device. You can toggle it without restarting. Here is the part the release notes do not lead with. This is not a convenience toggle. It is an execution boundary. Unsloth's own docs say server-side tools run as your user. Anyone who reaches that server with your API key can run code on your machine. Network reach is code reach. So pass dash dash disable tools unless you meant to hand that out. Outside the house, the tunnel is right. Cloudflare publishes a public web address, and your own network cannot do that. Inside, nothing sits in the path. So no, reaching your own machine never needed somebody else's service. It needed three settings, one password, and one honest look at what your tools can run.

---

## Scores

| # | Row | A | B | Reason |
|---|-----|---|---|--------|
| 1 | Hook | 2 | 3 | A's spoken first five words ("Your model runs on the") name neither product nor number; "Unsloth" arrives at roughly second five and the failure completes at second seven. B names the product at word one and the tension is complete by word five. B's spoken hook and its on-screen card are the same sentence; A's diverge. |
| 2 | Payoff timing | 2 | 2 | Both put a takeaway before second eight and both reach the loopback diagnosis at nine to ten seconds. A burns 3.4s on a scene-set with no product-specific content and then spends "That is not a bug" before the mechanism; B front-loads product and failure at second one but its own hook scene runs a full ten seconds. Neither pays the mechanism by second four. Even. |
| 3 | Specificity without cramming | 2 | 2 | A spends its single spoken number on the default bind address, the fact that explains the whole problem, and puts the digits on screen where hard constraint 4 wants them. Against that it carries slack: four sentences on the hotel comparison, "so nothing has to reload" restating "without a restart", and "It sits on the same docs page as the tunnel". B carries the preview caveat and the full three-level Settings path, both of which a viewer performing this needs, but it leaves the strongest number in the brief unspent in narration and unshown on screen. One draft has decoration, the other has an omission. Even. |
| 4 | Voice | 3 | 2 | Both clean, both second person throughout, no hard breaks either side. A earns the third point: "To reach a room away." is a genuine wry beat, one short fragment undercutting the sentence before it, landing on the situation rather than the viewer, unexplained, correctly placed away from hook and payoff. B has no wry beat, and its myth-bust runs the antithetical engine at least twice ("not a convenience toggle / it is an execution boundary", "never needed X / it needed Y") against a rule capping it at once. A's row. |
| 5 | Navigation | 1 | 3 | See below. |
| 6 | Difference | 1 | 3 | Scored against the obvious treatment, ledger being empty. A **is** the obvious treatment, executed well: a numbered walkthrough of a release-notes feature, a standard scene-set opening, a summarising close, with the hotel comparison as its one departure. The security catch is appended after the process finishes. B turns the how-to into an argument: it names what the viewer would reach for, concedes exactly where the tunnel is right, and refuses it only inside the house, which lets the security beat be the turn rather than an appendix. Different shape, different opening rhythm, different landing. |
| 7 | The repeat test | 2 | 3 | A has a repeatable line ("Network reach and code execution are the same switch here") but it is neither the payoff nor last. A's payoff scene is two sentences and the second, "The password change is forced, and the tools decision is yours", is administrative; the repeatable phrase "with nothing in the path" is the one before it. B's payoff is the repeatable line and it is the last thing heard, calling the hook's exact phrase back. B also lands the harder version of the shared idea: "Network reach is code reach". |
| | **Total** | **13** | **18** | |

## Row 5 in full

Draft A uses two positional labels, "Step one" and "Step two". Both are legal. The brief sets
`has process: true` with four steps the viewer performs, so hard constraint 10's exemption
genuinely applies; two is under the cap of three; and each label names its action, as the rule
requires. The gate was right to allow them. The question row 5 asks is different: not whether
the labels are permitted, but whether they carry content.

They do not. Delete "Step one:" and the sentence becomes "Open Settings and switch on network
access" -- nothing is lost, and the line is stronger for opening on the verb. Delete "Step two:"
and the same holds, but worse for the label: the very next clause is "It stops and asks, because
the toggle will not move until you do." That clause already states the ordering constraint, and
states it as mechanism rather than as counting. It is the "answer the question the last beat
raised" move from the voice rules' own table, sitting immediately beside a number that is trying
to do the same job less well. Where a script states why a step must follow another, the label on
that step is redundant by construction.

Two further costs. First, the count is opened and never closed. A's own review note says the
third move was deliberately left unlabelled because it belongs to the payoff -- but a viewer who
hears "Step one" and "Step two" is primed to wait for a third, and instead gets "Now pick up the
laptop." Announcing scaffolding and then abandoning it is worse than never raising it, because it
sets an expectation the script does not honour. Second, the labels arrive at second thirty-seven,
after four sentences of Cloudflare-and-hotel detour. They are functioning as a re-entry marker
after a digression -- which is diagnostic. The label is compensating for a structure that
wandered, not serving the viewer's hands.

So: legal, restrained, correctly attached to real steps, and mechanical. That is row 5 = 1
exactly as written, "labels used legally but mechanically." The permitted badge is real, and the
badge does not make the label carry content. This is the habit we removed, wearing it.

Draft B scores 3. Every join is a move from the voice rules' navigation table and every one names
what changed: "Change what it listens on, and the tunnel stops being necessary" (name what
changes, and the pivot of the whole argument), "It does not just flip on" (contradict the
expectation), "Network reach is code reach" (jump to the consequence), "Outside the house, the
tunnel is right" (answer the objection the brief raised). Reorderability is the harder half of
the anchor and B mostly survives it: the password beat requires the flip to exist, the Cloudflare
concession requires both the security beat and the inside path to be established before it can
read as a concession rather than a retreat, and the payoff requires all of it. The one soft
spot is the desktop path and the terminal flag, which are an explicit "or" and could swap. That
is not enough to pull it down.

## Winner

**Draft B**, 18 to 13. Not a tie, so the row 6 tiebreak was not needed; B would have won it
anyway.

## Grafts

**None.** Four candidates were considered and all four were declined:

- **A's hook.** Not eligible. The rule permits taking the loser's hook only when it scores at
  least two points higher on row 1; A scores one point lower.
- **"By default Unsloth answers on one twenty-seven dot zero dot zero dot one."** The strongest
  case for a graft: B never says the address and never puts it on screen, and it is the top entry
  in the brief's key numbers. Declined because a graft must not break the winner's number budget,
  and B spends zero spoken numbers by design. The real remedy is not a graft: hard constraint 4
  says digits belong on screen, and B's scene two on-screen text ("loopback = this machine only")
  has room for the address with no narration change at all. Flagged for the next stage; no draft
  JSON was modified.
- **"That tunnel is the right tool from a hotel."** A good concrete image, but B already runs a
  house metaphor and says the same thing as "Outside the house, the tunnel is right". Grafting
  would collide with the surrounding beat and require rewriting it.
- **"Unsloth shows you the address to type and a code you can scan."** A mentions the scannable
  code, B does not. This would be an edit to B's existing sentence rather than a whole-sentence
  graft, and the QR code is convenience detail, not mechanism. Declined as below the bar.

## What the losing shape would have needed

The how-to would have needed to open on the product and the failure inside five words and cut the
four-sentence Cloudflare detour that pushes its first mechanism past second nine, so the shape it
promises -- here is the thing you do -- starts doing it instead of describing the room. And it
would have needed to drop both step labels, because the sentence beside them already states the
dependency they were standing in for, which leaves them as removable scaffolding that opens a
count the script never closes.
