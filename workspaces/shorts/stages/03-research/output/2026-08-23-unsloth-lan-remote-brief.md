# Unsloth v0.1.801-beta lets you reach Unsloth Desktop from another device on your own network: research brief

## Summary

Unsloth can now be reached from any device in your house without a Cloudflare tunnel, which is three settings and one password, and the same switch also lets anyone on your network run code as you.

## Thesis

Unsloth can now be reached from any device in your house without a Cloudflare tunnel, which is three settings and one password, and the same switch also lets anyone on your network run code as you.

## Explanation path

Start where the viewer already is: the model runs on the box in the other room and they are on the couch. Establish that Unsloth binds to loopback by default, so it is deliberately unreachable. Then the change: a wildcard bind exposes it to the network, either from Settings or with a flag. Then the password gate, which is not optional. Close on the risk the release notes do not lead with: server-side tools run as your user, so network reach is code execution reach.

## Viewer situation

Your model runs on the box in the other room and you are on the couch with a laptop or a phone.

## Has process

true

- Open Settings, API keys, LAN access, or launch with `unsloth studio -H 0.0.0.0`
- Change the auto-generated bootstrap admin password when Unsloth stops and asks
- Connect from the other device using the shown address or QR code
- Pass `--disable-tools` if you do not want server-side tools reachable

## Objection

Unsloth already documents a Cloudflare tunnel, so why bother with a LAN bind?

## Claims

1. Unsloth v0.1.801-beta shipped on 2026-08-20 with LAN Remote Access in preview and auto compaction, merging more than 200 pull requests. [primary, high confidence] -- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta (accessed 2026-08-23)
2. LAN access is disabled by default and requires changing the generated admin password, and can be toggled without restarting from a dedicated Settings section that also shows connection addresses and QR codes. [primary, high confidence] -- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta (accessed 2026-08-23)
3. Unsloth binds to 127.0.0.1 by default, which the docs describe as 'this machine only'; `unsloth studio -H 0.0.0.0` makes the raw port reachable on 'your network'. [docs, high confidence] -- https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth (accessed 2026-08-23)
4. The default port is 8888, and `--secure` publishes only through Cloudflare while keeping the raw port on loopback. [docs, high confidence] -- https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth (accessed 2026-08-23)
5. Unsloth's own banner warns that 'Server-side tools run as your user' and that 'anyone reaching the server with your API key can run code on that machine', recommending `--disable-tools` when exposing it. [docs, high confidence] -- https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth (accessed 2026-08-23)
6. The feature was asked for because users did not want to route their own rig through a third party: 'I don't have internet access or I don't want to pipe everything though a Cloudflare temp URL just to access my local AI rig remotely.' [community, high confidence] -- https://github.com/unslothai/unsloth/issues/9207 (accessed 2026-08-23)
7. Auto compaction keeps long chats going past the context limit by evicting whole oldest turns into a searchable per-thread archive, and deliberately does not summarize because summarization 'showed little benefit and added ~190s per compaction'. [primary, high confidence] -- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta (accessed 2026-08-23)

## Key numbers

- **Default bind address**: 127.0.0.1 -- https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth
- **Default port**: 8888 -- https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth
- **Time summarization added per compaction, which is why it was dropped**: ~190s -- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta
- **Pull requests merged in the release**: 200+ -- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta
- **Accuracy gain claimed for Qwen3.8-27B Dynamic v3.0 GGUFs**: >10% higher top-1 accuracy -- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta

## Analogy candidates

- **a door that only opens from the inside, until you fit it with a handle on the outside**: loopback is the inside-only door; the wildcard bind fits the outside handle; the admin password is the lock you are forced to change before the handle works. Breaks when: a real door does not let a visitor run your errands, and this one does: server-side tools execute as your user

## Misconceptions

- **Myth**: Reaching your own machine from your own network needs a tunnel through someone else's service.  
  **Reality**: Cloudflare publishes a public URL, which is useful outside the house. Inside it, a wildcard bind reaches the same server with nothing in the path.
- **Myth**: Turning on LAN access is just a convenience toggle.  
  **Reality**: It is an execution boundary. Unsloth's own docs say anyone reaching the server with your API key can run code on that machine, which is why the password change is forced and `--disable-tools` exists.

## Glossary

- **loopback**: the address a machine uses to talk to itself, so nothing outside it can connect
- **wildcard bind**: listening on every network address the machine has, instead of only its own
- **tunnel**: a relay that gives your local server a public web address by routing traffic through an outside service
- **compaction**: dropping the oldest turns of a chat once it outgrows the model's context window

## Unverified

- Issue 9207 still reads as open and unresolved with no maintainer response, while the release notes describe the feature as shipped in preview. One of the two is stale; do not claim the issue was closed by this release.
- The release notes do not state a port or URL for the Settings path; the port 8888 figure comes from the CLI docs and may differ in the desktop app.
- No independent test of the LAN path was run for this brief.

## Suggested outline

1. You are on the couch and the model is in the other room, and Unsloth will not answer. 2. It binds to itself on purpose: one setting, or one flag, changes that, and it stops to make you set a real password. 3. The catch the release notes bury: anyone who reaches it with your key runs code as you, so disable tools unless you meant it.

## Sources

- https://github.com/unslothai/unsloth/issues/9207 -- unsloth issue 9207: allow remote access without Cloudflare
- https://github.com/unslothai/unsloth/releases/tag/v0.1.801-beta -- unsloth v0.1.801-beta release notes
- https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth -- Unsloth docs: secure remote access

## Notes

Format is smooth-explainer, so at most three spoken numbers. The strongest are the default port, the forced password, and the ~190s summarization figure, but the security line matters more than any of them.
