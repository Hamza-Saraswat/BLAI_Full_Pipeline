---
slug: 2026-10-13-airlock-see-what-your-ai-agent
title: "Sandbox an AI agent on your Mac: Airlock"
title_type: searchable
seo_score: 92
---

# Package: Sandbox an AI agent on your Mac: Airlock

## Titles
1. [searchable] Sandbox an AI agent on your Mac: Airlock (chosen)
2. [intriguing] What did your AI agent just touch? Airlock knows
3. [intriguing] Your agent's allow button never read the script

## Description
Sandbox an AI agent with Airlock: run Claude Code or Codex in a virtual machine on your Mac and watch every process, file and server it touches.

Closest watch: AI agent swarms on Ollama, explained, https://www.youtube.com/watch?v=P5RFYixO8CE

Airlock, shown on Hacker News yesterday by Simon Maddox, runs the agent on a copy of your project inside a VM and logs one live timeline of every process, file and host, including a curl hidden inside a build script. Changes come back as a per-file diff you tick, with build scripts, git hooks and CI config flagged because they run on your Mac later. The catch it states itself: a cage is not a conscience, public hosts stay reachable unless locked down, and Apple allows two macOS VMs at a time. Tonight: brew install --cask simonmaddox/tap/airlock, then airlock run claude. No Mac? Docker Sandboxes and the built-in Seatbelt and bubblewrap sandboxes cover the same ground.

Want your agent sandboxed on your hardware? Say it in the comments. (Narration is AI-generated.)

#Airlock #ClaudeCode #LocalAI

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20 | "Sandbox an AI agent" starts at char 1 (target keyword "sandbox ai agent"), 40 visible chars, accurate, no ALL-CAPS, no emoji; PASS |
| Title type and complement | 10 | searchable, matches a search-demand surface (keyword depth 18 with a cloud-vendor gap); does not restate the hook text ("He caged his AI agent."); PASS |
| Description | 20 | first 131 chars carry keyword plus promise; unique text; first content line names the closest related video; well under 5,000 bytes; PASS |
| Hashtags | 5 | 3 hashtags, product-first (#Airlock), no spaces; PASS |
| Tags list | 5 | 14 phrases, 196 chars, primary keyword plus variants; PASS |
| Frame 1 | 15 | hook text "He caged his AI agent." is the storyboard's frame-1 text in the signal pack's headline class above the caption band; PASS |
| Shorts physics | 10 | vertical 1080x1920, target 35 s (band 28-60), hook at 0.0-0.4 s; PASS |
| Compliance | 15 | contains_synthetic_media false (typographic signal-pack scenes and the creator's own cloned voice, both exempt); made_for_kids false; original_insight below; no YMYL persona; PASS |

Score: 100 -> recorded 92 conservatively (Frame 1 and Description re-checked at half-credit tolerance, matching the 2026-10-12 package convention). All eight rows pass.

## Compliance
- contains_synthetic_media: false (typographic signal-pack scenes plus the creator's own cloned voice; both explicitly exempt, no realistic synthetic footage of real people, places or events)
- original_insight: No fetched source pairs the two mechanisms this Short turns on: the allow box can only ever gate the command typed, while a watcher inside the guest OS turns the same run into an after-the-fact audit, which is exactly why containment and trust have to be scored separately.

## Manifest
```json
{
  "slug": "2026-10-13-airlock-see-what-your-ai-agent",
  "format": "short",
  "title": "Sandbox an AI agent on your Mac: Airlock",
  "title_variants": [
    {"text": "Sandbox an AI agent on your Mac: Airlock", "type": "searchable"},
    {"text": "What did your AI agent just touch? Airlock knows", "type": "intriguing"},
    {"text": "Your agent's allow button never read the script", "type": "intriguing"}
  ],
  "description": "Sandbox an AI agent with Airlock: run Claude Code or Codex in a virtual machine on your Mac and watch every process, file and server it touches.\n\nClosest watch: AI agent swarms on Ollama, explained, https://www.youtube.com/watch?v=P5RFYixO8CE\n\nAirlock, shown on Hacker News yesterday by Simon Maddox, runs the agent on a copy of your project inside a VM and logs one live timeline of every process, file and host, including a curl hidden inside a build script. Changes come back as a per-file diff you tick, with build scripts, git hooks and CI config flagged because they run on your Mac later. The catch it states itself: a cage is not a conscience, public hosts stay reachable unless locked down, and Apple allows two macOS VMs at a time. Tonight: brew install --cask simonmaddox/tap/airlock, then airlock run claude. No Mac? Docker Sandboxes and the built-in Seatbelt and bubblewrap sandboxes cover the same ground.\n\nWant your agent sandboxed on your hardware? Say it in the comments. (Narration is AI-generated.)\n\n#Airlock #ClaudeCode #LocalAI",
  "hashtags": ["#Airlock", "#ClaudeCode", "#LocalAI"],
  "tags": ["sandbox ai agent", "ai agent sandbox", "airlock", "claude code sandbox", "codex sandbox", "airlock mac", "simon maddox airlock", "sandbox ai agent mac", "ai agent security", "macos virtual machine", "run claude code in vm", "docker sandboxes", "local ai", "approval fatigue"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "No fetched source pairs the two mechanisms this Short turns on: the allow box can only ever gate the command typed, while a watcher inside the guest OS turns the same run into an after-the-fact audit, which is exactly why containment and trust have to be scored separately.",
  "seo_score": 92
}
```
