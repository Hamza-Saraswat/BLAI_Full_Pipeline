# Compliance (every upload)

Source: YouTube Partner Program "inauthentic content" policy (July 2025, clarified July 2026) and the altered-or-synthetic-content disclosure rules. Research section 4.

## Every video must

1. Carry an original argument or research angle, not a template with swapped nouns. The package note states the original insight in one sentence (`original_insight` field).
2. Vary structure, hook, visuals and narration across episodes (the rotation ledgers enforce this).
3. Keep a real human voice and editorial stance: the creator's own cloned voice, the creator's own measurements where possible.
4. Never present an AI persona as a human expert on health, legal, finance or political topics. When a topic touches those (EU AI Act, HIPAA, pricing advice), the narration attributes claims to named sources and speaks as the creator.
5. Avoid slideshow-plus-TTS formats, templated storylines and scrolling-text videos.
6. Log the human reviewer's sign-off: the Approve tap is recorded in the hub note with a timestamp.

## `containsSyntheticMedia`

Set `true` only when the video contains realistic synthetic footage of real people, places or events, or altered real footage. Set `false` for: the creator's own voice clone (explicitly exempt), the animated mascot and typographic scenes (clearly unrealistic), AI-assisted scripts, titles, thumbnails and research (production assistance). Disclosing does not restrict reach; failing to disclose when required can.

## Other flags

`selfDeclaredMadeForKids` is always `false` (the side effects of `true` are effectively irreversible). Shorts set `notifySubscribers=false`; long-form `true`.

## Reused content

Stock b-roll (Phase 4) is always transformed: overlays, commentary, and never more than a few seconds uncut. Compilations without narrative are not allowed.
