---
slug: 2026-11-06-offline-ai-on-a-usb-stick-loca
stage: 04-script
generated_at: 2026-11-06
winner: A (how-to-three-moves)
---

# Drafts and scores: 2026-11-06-offline-ai-on-a-usb-stick-loca

Both drafts passed validator (0 blockers) and all eval hard gates before judging. Judge call: kimi-k3, rubric verbatim, brief and last-5 ledger rows attached; neither draft's author saw the other.

## Draft A (winner, how-to-three-moves) -- final, graft applied

```json
{
  "slug": "2026-11-06-offline-ai-on-a-usb-stick-loca",
  "topic": "Offline AI on a USB stick: local LLM plus Kiwix, no network",
  "title": "Offline AI on a USB Stick: llamafile + Kiwix, No Network",
  "description": "Download one 2.02 GB llamafile and one Wikipedia ZIM, copy both plus the Kiwix Reader to a spare USB stick, and ask questions with the network off. Covers the Windows 4 GB executable cap and the honest catch: the model cannot search the library, so you verify answers yourself. Built from Mozilla's llamafile README, the Kiwix sizing post, and the bartowski model card.",
  "hashtags": [
    "#llamafile",
    "#Kiwix",
    "#OfflineAI"
  ],
  "tags": [
    "llamafile",
    "kiwix offline wikipedia",
    "offline ai",
    "usb stick ai",
    "local llm",
    "zim file",
    "kiwix reader",
    "llama 3.2 3b",
    "q4_k_m gguf",
    "run llm without internet",
    "offline wikipedia zim",
    "portable ai usb stick",
    "mozilla llamafile",
    "ai without wifi",
    "private local ai",
    "llamafile windows 4gb",
    "offline ai kit",
    "kiwix mini wikipedia"
  ],
  "hook_text": "3 moves. Network off. Tonight.",
  "hook_candidates": [
    "Ninety-one gigabytes. All of Wikipedia in your pocket.",
    "Your AI should work when the internet doesn't.",
    "All of Wikipedia, no internet. Really.",
    "The offline AI kit that fits on one USB stick.",
    "No internet. No cloud. Still answers.",
    "Offline Wikipedia plus AI: build it tonight.",
    "All of Wikipedia, on a USB stick, tonight.",
    "Three moves and your AI answers with the network off tonight.",
    "A glovebox kit for when the network dies.",
    "The AI survival kit: brain, library, one stick."
  ],
  "style_pack": "terminal",
  "script_format": "classic",
  "structure": "how-to-three-moves",
  "value_types": "TEACHES,EQUIPS",
  "target_duration_s": 34,
  "narration_full": "Three moves and your AI answers with the network off tonight. That spare USB stick becomes the kit. Step one: download the brain, a llamafile, a model and its engine in one program. A two point zero two gigabyte file, no install. Step two: download the library, a ZIM file, one website squeezed into one archive. The free Kiwix Reader app opens it. Mini Wikipedia was twelve gigabytes at the last count. Step three: copy everything to the stick. Windows caps single files at four gigabytes of executable, and the brain can't search the library. It explains; you verify. Two tools, one kit. Unplug the network. It still answers, straight off the stick.",
  "music_mood": "steady-build",
  "scenes": [
    {
      "id": "s01",
      "role": "hook",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "Three moves and your AI answers with the network off tonight. That spare USB stick becomes the kit.",
      "on_screen_text": "3 MOVES | NETWORK OFF | TONIGHT",
      "visual_brief": "Frame 1 composition: dark background, one centered terminal window with sharp corners, already showing a half-full amber #FFB347 download bar and a lit cursor. Motion onset at 0.4 s: the bar creeps right on 'three moves'. On 'network off' a tiny ASCII wifi glyph fades out beside the prompt. On 'spare USB stick' a blocky stick glyph fades in below the window. Only the bar plus one glyph animate at once; entrances fade or rise in place; text at least 64 px. First and last 8 frames static; last frame: same terminal, bar full, cursor steady, the loop anchor.",
      "est_duration_s": 6.3,
      "sfx": [
        {
          "at": "start",
          "name": "type"
        }
      ]
    },
    {
      "id": "s02",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "Step one: download the brain, a llamafile, a model and its engine in one program. A two point zero two gigabyte file, no install.",
      "on_screen_text": "STEP 1: THE BRAIN | wget llamafile | 2.02 GB | NO INSTALL",
      "visual_brief": "Giant-number layout, dark terminal pack. On 'download the brain' the command 'wget llamafile' (under 19 monospace chars) typewrites at the window top. On 'two point zero two gigabyte' giant amber digits '2.02 GB' scale in place center screen, the only element then animating. On 'no install' a single file glyph rises in place beneath the digits. Sharp corners, typewriter text, at most two elements animating and one text block; text at least 64 px; first and last 8 frames static.",
      "est_duration_s": 8.3,
      "sfx": [
        {
          "at": "mid",
          "name": "blip"
        }
      ]
    },
    {
      "id": "s03",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "split-compare",
      "narration": "Step two: download the library, a ZIM file, one website squeezed into one archive. The free Kiwix Reader app opens it. Mini Wikipedia was twelve gigabytes at the last count.",
      "on_screen_text": "STEP 2: THE LIBRARY | wget wiki.zim | 12 GB | READER",
      "visual_brief": "Split-compare layout. On 'download the library' the command 'wget wiki.zim' typewrites in. Major left side: an archive glyph labeled 'WIKI.ZIM' rises in place, and on 'twelve gigabytes' amber '12 GB' fades in beneath it. Minor right side: the label 'READER' (6 chars) fades in on 'Kiwix Reader app'. Text at least 64 px, one text block animating at a time, at most two elements moving, hard cut in from s02; first and last 8 frames static.",
      "est_duration_s": 10.4,
      "sfx": [
        {
          "at": "mid",
          "name": "blip"
        }
      ]
    },
    {
      "id": "s04",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "diagram-flow",
      "narration": "Step three: copy everything to the stick. Windows caps single files at four gigabytes of executable, and the brain can't search the library. It explains; you verify. Two tools, one kit.",
      "on_screen_text": "STEP 3: COPY TO THE STICK | 4 GB WINDOWS CAP | TWO TOOLS, ONE KIT",
      "visual_brief": "Diagram-flow layout, terminal style. On 'copy everything to the stick' three labeled glyphs 'LLAMAFILE', 'WIKI.ZIM', 'KIWIX' rise in place in a row, then amber arrows fade in pointing into a blocky USB-stick glyph at right. On 'four gigabytes' an amber '4 GB' stamp scales in beside a small wall glyph. On 'can't search' a broken-link glyph fades in. At most two elements animate at once; text at least 64 px; first and last 8 frames static.",
      "est_duration_s": 10.7,
      "sfx": [
        {
          "at": "mid",
          "name": "blip"
        }
      ]
    },
    {
      "id": "s05",
      "role": "payoff_close",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "Unplug the network. It still answers, straight off the stick.",
      "on_screen_text": "NETWORK: OFF | ANSWERS ANYWAY | Build Local AI",
      "visual_brief": "Centered-stack payoff in the terminal pack. Opens on the same centered window as s01 frame 1, download bar full, amber status line 'NETWORK: OFF'. On 'it answers anyway' a short question and its answer type out, then all motion stops. The wordmark 'Build Local AI' fades in centered beneath the window and settles. Last frame static: bar full, cursor steady, wordmark holding, rhyming s01 frame 1 for the loop.",
      "est_duration_s": 3.5
    }
  ],
  "notes_for_review": "Spoken numbers held to three: 2.02 GB model file, 12 GB mini Wikipedia hedged with 'at the last count' (Kiwix's October 2022 sizing, so past tense, never a live catalog number; 91 GB dropped for budget), and the 4 GB Windows executable cap. Objection answered straight in one beat: the brain cannot search the ZIM, conceded on camera as 'two tools, one kit' rather than strawmanning. No analogy key used; 'kit' is plain language here, not the glovebox mapping."
}
```

## Draft B (number-first) -- as judged

```json
{
  "slug": "2026-11-06-offline-ai-on-a-usb-stick-loca",
  "topic": "Offline AI on a USB stick: local LLM plus Kiwix, no network",
  "title": "Offline AI on a USB Stick: Wikipedia Plus a Local LLM",
  "description": "A spare USB stick can carry both halves of an offline answer machine: a 2.02 GB llamafile that runs with no install, next to all of English Wikipedia compressed by Kiwix. This build names both pieces and the honest catches.",
  "hashtags": [
    "#llamafile",
    "#Kiwix",
    "#OfflineAI"
  ],
  "tags": [
    "llamafile",
    "kiwix offline wikipedia",
    "offline ai",
    "usb stick ai",
    "local llm",
    "zim file",
    "llama 3.2 3b",
    "q4_k_m quantization",
    "kiwix reader",
    "wikipedia zim download",
    "run ai without internet",
    "offline wikipedia",
    "mozilla llamafile",
    "gguf model",
    "ai on a usb drive",
    "no internet ai",
    "private ai",
    "local ai assistant",
    "offline llm",
    "single file llm"
  ],
  "hook_text": "91 GB buys all of Wikipedia",
  "hook_candidates": [
    "Ninety-one gigabytes. All of Wikipedia in your pocket.",
    "Your AI should work when the internet doesn't.",
    "All of Wikipedia, no internet. Really.",
    "The offline AI kit that fits on one USB stick.",
    "No internet. No cloud. Still answers.",
    "Offline Wikipedia plus AI: build it tonight.",
    "All of Wikipedia, on a USB stick, tonight.",
    "Three moves and your AI answers with the network off tonight.",
    "A glovebox kit for when the network dies.",
    "The AI survival kit: brain, library, one stick."
  ],
  "style_pack": "terminal",
  "script_format": "classic",
  "structure": "NUMBER-FIRST",
  "value_types": "TEACHES,EQUIPS",
  "target_duration_s": 34,
  "narration_full": "Ninety-one gigabytes buys all of Wikipedia. All of English Wikipedia, with pictures, at the last official count. Your spare USB stick holds it. That size comes from Kiwix, free software that squeezes whole websites into ZIM files, compressed archives you read offline. The library half. The brain is a llamafile, a model and its engine fused into a single file. Two point zero two gigabytes of model, no install. Both halves ride a single stick, under twenty dollars of storage. The catch: it is slow, paraphrases, can invent citations, and cannot search the ZIM. It explains; you verify. The network is gone. The stick still answers.",
  "music_mood": "steady-build",
  "scenes": [
    {
      "id": "s01",
      "role": "hook",
      "tool": "hyperframes",
      "layout_archetype": "giant-number",
      "narration": "Ninety-one gigabytes buys all of Wikipedia. All of English Wikipedia, with pictures, at the last official count. Your spare USB stick holds it.",
      "on_screen_text": "91 GB | all of English Wikipedia + pictures | fits your spare USB stick",
      "visual_brief": "Frame 1: dark terminal, giant amber '91 GB' centered at 220px, already on screen and stable. On 'buys all of Wikipedia' (motion onset 0.40s) a typewriter line rises in place below it: 'all of English Wikipedia, with pictures'. On 'last official count' a dim caption fades in: 'source: Kiwix sizing post'. On 'spare USB stick' an amber USB stick outline fades in lower right. One text block animating at a time, entrances rise or fade only. First and last 8 frames hold the centered '91 GB' with a blinking cursor, the loop anchor.",
      "est_duration_s": 8.0,
      "sfx": [
        {
          "at": "start",
          "name": "type"
        }
      ]
    },
    {
      "id": "s02",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "diagram-flow",
      "narration": "That size comes from Kiwix, free software that squeezes whole websites into ZIM files, compressed archives you read offline. The library half.",
      "on_screen_text": "Kiwix | website → ZIM file | read offline",
      "visual_brief": "Dark terminal window. On 'Kiwix' the word 'kiwix' types in amber at the prompt. On 'squeezes whole websites into ZIM files' a diagram-flow builds left to right: a dim block labeled 'wikipedia.org' fades in, a hard amber arrow appears, then an amber block labeled 'wikipedia.zim' scales in place, smaller than the source block to show compression. On 'The library half' three dim ZIM filenames rise in place as a neat stack beneath. At most two elements moving at once, no edge slides, text 64px or taller.",
      "est_duration_s": 7.6
    },
    {
      "id": "s03",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "The brain is a llamafile, a model and its engine fused into a single file. Two point zero two gigabytes of model, no install.",
      "on_screen_text": "llamafile = model + engine | 2.02 GB | no install",
      "visual_brief": "Centered stack on dark. On 'The brain is a llamafile' a single file glyph labeled 'model.llamafile' fades in at center inside the terminal window. On 'fused into a single file' two amber outlines marked 'model' and 'engine' scale in place and merge into the one glyph, never sliding from an edge. On 'Two point zero two gigabytes' amber '2.02 GB' types beneath the glyph at 96px. On 'no install' a dim caption fades in below: 'no installer, runs from the stick'. One text block animating at a time.",
      "est_duration_s": 8.3,
      "sfx": [
        {
          "at": "on 'Two point zero two gigabytes'",
          "name": "ding"
        }
      ]
    },
    {
      "id": "s04",
      "role": "explain",
      "tool": "hyperframes",
      "layout_archetype": "grid",
      "narration": "Both halves ride a single stick, under twenty dollars of storage. The catch: it is slow, paraphrases, can invent citations, and cannot search the ZIM. It explains; you verify.",
      "on_screen_text": "under $20 of storage | slow | paraphrases + invents citations | can't search the ZIM | you verify",
      "visual_brief": "Two-row grid on dark, headers 'BRAIN' and 'LIBRARY' rising in place on 'Both halves'. On 'under twenty dollars' a dim tag fades in below the grid: 'under $20 of storage'. On 'The catch' short amber lines type one per beat beside BRAIN: 'slow', then 'paraphrases', then 'can invent citations'. On 'cannot search the ZIM' a dim arrow from BRAIN toward LIBRARY appears with an amber X over it. On 'you verify' an amber check mark scales in beside LIBRARY. Never more than two elements animating.",
      "est_duration_s": 10.1
    },
    {
      "id": "s05",
      "role": "payoff_close",
      "tool": "hyperframes",
      "layout_archetype": "centered-stack",
      "narration": "The network is gone. The stick still answers.",
      "on_screen_text": "offline | still answers | Build Local AI",
      "visual_brief": "The terminal status bar shows a dim 'offline' tag from frame 1. On 'The network is gone' the wifi glyph hard-cuts to a crossed-out state, no fade. On 'the stick still answers' one amber answer line prints at the prompt. Then 'Build Local AI' scales in centered at 128px and settles. Last frame: centered amber wordmark on dark, the same centered-weight composition as s01 frame 1, the loop anchor. First and last 8 frames fully stable.",
      "est_duration_s": 2.8,
      "sfx": [
        {
          "at": "on 'The network is gone'",
          "name": "click"
        }
      ]
    }
  ],
  "notes_for_review": "91 GB framed as scale via 'at the last official count' (October 2022 sizing, not a live number); slowness stated as the brief's known catch, no rate claimed. No analogy used, key omitted; the disconnection objection is answered in one beat with 'It explains; you verify.'"
}
```

## Score table

| Row | A | B |
|-----|---|---|
| 1 | 1 | 3 |
| 2 | 2 | 3 |
| 3 | 3 | 1 |
| 4 | 3 | 3 |
| 5 | 1 | 3 |
| 6 | 3 | 1 |
| 7 | 3 | 3 |
| 8 | 3 | 2 |

Totals: A 19, B 19. Tie broken on row 6 (difference): A 3, B 1.

Winner: A.

## Grafts

- From B, "It explains; you verify." into A s04 -- row 8: A conceded the paraphrase risk but never gave the viewer the verification practice; the line adds it with no number cost and no person shift.

## What the losing shape would have needed

B needed to keep its own hedge discipline on the second sizing-post number -- 'under twenty dollars of storage' is October 2022 microSD pricing spoken as a live USB-stick fact, and 'it is slow' asserts what the brief lists as unmeasured -- and one drifted claim capped its strongest suit. It also needed an opening rhythm the channel has not just run (11-03 was number-shock, and its scenes sum to exactly 11-04's 36.8s) plus one reusable rule in place of the symptom list.

## Judge row notes

- Row 1: B's 'Ninety-one gigabytes buys all of Wikipedia' is a topic number plus felt scale-shock inside five words; A's 'Three moves' is a structure promise naming no product and no topic number.
- Row 2: B's first sentence pays its own promise by second 4; A burns 6.3s of hook before 'llamafile' lands near second 8.
- Row 3: A spends three hedged numbers, one per beat, none decorative; B hedges 91 GB then states the same post's $20 microSD price as a live, medium-shifted fact (plus a flat 'slow') -- one drifted claim caps the row at 1.
- Row 4: Both clean, in the right person, with one unexplained wry beat that lands: A's 'Two tools, one kit,' B's 'It explains; you verify.'
- Row 5: A's spoken 'Step one/two/three' survive deletion since the count already rides the on-screen text, so finding 14 caps the row; B's transitions each name what changed and 'That size' plus 'Both halves' lock the order.
- Row 6: A's count-promise how-to matches none of the last five in shape, opening rhythm, or landing; B's number-shock opening repeats 11-03's hook pattern and its scene sum (36.8s) matches 11-04 exactly.
- Row 7: Both scripts end on their most repeatable line: 'It still answers, straight off the stick' and 'The stick still answers.'
- Row 8: A hands over a reusable rule (sub-4 GB model because of the Windows cap) so the viewer can predict cases never mentioned; B shows compression and fusion concretely but its catch remains a list of symptoms.

## Process notes

- Round 1 of judging ran on a draft B whose 7-second trim had stripped the October-2022 hedge; the judge's row-3 note flagged the resulting drift. The hedge was restored (advisory accepted, see the script note Decisions) and the duel re-run; both verdicts picked A, and the re-run is the recorded one.
