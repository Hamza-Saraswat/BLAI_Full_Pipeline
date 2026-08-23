---
slug: 2026-08-23-unsloth-lan-remote
format: smooth-explainer
structure: myth-bust
style_pack: terminal
value_types: EQUIPS, TEACHES
target_duration_s: 96
brief: 2026-08-23-unsloth-lan-remote-brief.md
drafts: 2026-08-23-unsloth-lan-remote-drafts.md
winner: draft B
---

# Unsloth LAN access without a tunnel

## Decisions

- Two structures written; the judge picked draft B. Scores and reasoning in `2026-08-23-unsloth-lan-remote-drafts.md`.
- Hook chosen from 10 candidates by the hook-library scoring.

## Hook candidates

1. Unsloth won't answer from your couch  *
2. Your model is in the other room
3. Unsloth ignores your phone on purpose
4. You don't need a tunnel to your own box
5. Same house, same network, no tunnel
6. Unsloth listens to itself and nobody else
7. One setting reaches Unsloth from the couch
8. Cloudflare is for outside the house
9. Unsloth's LAN switch is not a convenience
10. Turning on LAN access hands out your shell

## Script

| Scene | Role | Narration | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-----------|----------------|--------------|------|--------|-------|
| s1 | hook | Unsloth will not answer from your couch. Your model is in the other room. You are not. The fix you reach for is a tunnel through somebody else's service. | Unsloth won't answer from your couch / a tunnel through somebody else's service | Frame 1: on a near-black terminal field, the line UNSLOTH WON'T ANSWER FROM YOUR COUCH already fully legible i... | hyperframes | centered-stack | 10 |
| s2 | explain | Unsloth binds to loopback, the address a machine uses to talk to itself. The docs call that this machine only. Nothing outside can reach it. That is the default, and it is deliberate. | loopback = this machine only / nothing outside can connect | A single amber rectangle labelled YOUR BOX sits centre-frame. At 1s an arrow draws out of its right edge, curv... | manim | diagram-flow | 11 |
| s3 | explain | Change what it listens on, and the tunnel stops being necessary. In the desktop app that is Settings, then API keys, then the local network switch. It ships in preview. | Settings > API keys > LAN access / LAN Remote Access, preview | Three amber pills sit on a horizontal rule, left to right, each dim. At 1s the first pill lights and its label... | hyperframes | timeline | 10 |
| s4 | explain | Or start it from the terminal with dash H, zero dot zero dot zero dot zero. That is a wildcard bind, listening on every address the machine has instead of only its own. | unsloth studio -H 0.0.0.0 / wildcard bind: every address | A terminal prompt sits centred on black. At 0.5s the command types in character by character: unsloth studio -... | hyperframes | centered-stack | 11 |
| s5 | explain | It does not just flip on. Unsloth stops and makes you replace the auto-generated admin password first. After that it shows you the address to type on the other device. You can toggle it without restarting. | change the auto-generated password / toggle without a restart | The toggle from the settings row sits centre-frame, half thrown. At 1s it snaps back to off and a red-amber ba... | manim | diagram-flow | 13 |
| s6 | explain | Here is the part the release notes do not lead with. This is not a convenience toggle. It is an execution boundary. | LAN access is not a toggle / it is an execution boundary | The frame splits down the middle. At 0.5s the left half fades up with a small grey toggle icon and the word CO... | hyperframes | split-compare | 8 |
| s7 | explain | Unsloth's own docs say server-side tools run as your user. Anyone who reaches that server with your API key can run code on your machine. Network reach is code reach. So pass dash dash disable tools unless you meant to hand that out. | unsloth studio --disable-tools / LAN reach = code reach | A grid of small grey device tiles fills the frame, the box among them in amber. At 1s a key icon pops onto one... | manim | grid | 15 |
| s8 | explain | Outside the house, the tunnel is right. Cloudflare publishes a public web address, and your own network cannot do that. Inside, nothing sits in the path. | outside the house: Cloudflare tunnel / inside: nothing in the path | A house outline sits centre-frame with the amber box inside it. At 1s a phone slides in outside the walls and ... | manim | split-compare | 9 |
| s9 | payoff_close | So no, reaching your own machine never needed somebody else's service. It needed three settings, one password, and one honest look at what your tools can run. | no tunnel inside the house / three settings, one password | The grey dashed tunnel from the opening frame draws back in across the centre, then erases from both ends inwa... | hyperframes | centered-stack | 9 |

## Notes for review

myth-bust, smooth-explainer, terminal pack. No analogy: none of the signature pictures fits a bind address, so the mechanism is stated plainly. Zero numbers spoken on purpose. The port and the compaction figures are either off-topic or flagged unverified for the desktop path in the brief. Issue 9207 is not mentioned, and no claim is made about it being closed. Style-pack rotation will flag 'terminal' as a repeat of the previous video: the pack was assigned.
