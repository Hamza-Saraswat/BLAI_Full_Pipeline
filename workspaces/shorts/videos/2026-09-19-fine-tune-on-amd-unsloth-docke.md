---
slug: 2026-09-19-fine-tune-on-amd-unsloth-docke
workspace: shorts
title: "Fine-tune on AMD: the ROCm Docker image"
status: expired
pillar: how-to
structure: myth-bust
format: smooth-explainer
style_pack: terminal
value_types: "EQUIPS,TEACHES"
created: 2026-09-19
updated: "2026-09-20T13:35:30Z"
publish_slot: ""
seo_score: 95
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Fine-tune on AMD: Unsloth Docker in three moves

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-19-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-19-ideas]]
- Research: [[stages/03-research/output/2026-09-19-fine-tune-on-amd-unsloth-docke-brief]]
- Script: [[stages/04-script/output/2026-09-19-fine-tune-on-amd-unsloth-docke-script]]
- Package: [[stages/05-package/output/2026-09-19-fine-tune-on-amd-unsloth-docke-package]]
- Voice: [[stages/06-voice/output/2026-09-19-fine-tune-on-amd-unsloth-docke-narration]] (normalized narration written at script stage)
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- 2026-09-19T11:50:37Z - Checkpoint (stage 03, step 2): angle confirmed as the ideas-note line -- from bare AMD box to training in three moves, the new Docker image replaces the hand-pinned ROCm stack; slug 2026-09-19-fine-tune-on-amd-unsloth-docke unchanged.
- Why: the pick's why-now (v0.1.811-beta NVIDIA+AMD Docker, RDNA1/2) is exactly this angle; no redirect signal in the ideas note.
- 2026-09-19T11:57:27Z - Checkpoint (stage 04, step 1): draft A structure how-to-three-moves (brief has_process true; the four doc-grounded steps collapse to install Docker / run the unsloth-rocm container with its smoke test / train), draft B myth-bust (belief 'fine-tuning needs CUDA and a big NVIDIA card', broken by the 3GB/8GB VRAM floors). Rotation clear: last two ledger structures are contrarian-take and number-first. Value types locked EQUIPS,TEACHES. Promise: after this Short you can start fine-tuning on the AMD box you already own, tonight, with one Docker pull and no hand-built ROCm stack.
- Why: has_process true makes how-to-three-moves the natural A; B must be a different shape, not a cousin, and misconception 4 plus the measured floors give myth-bust a real number to break the belief with.
- Checkpoint (stage 04, step 2): ten hooks scored 5-7; picks A 'Your Radeon fine-tunes tonight, straight out of Docker.' (tonight pattern) and B 'AMD boxes don't need a CUDA card anymore.' (named-contradiction). Both 7/7: payoff word inside five words, named product, situation named, frame-1 legible, true per brief. Number-shock openers (the three-gigabytes and eight-gigabytes hooks) scored equal but are rotation-vetoed: hook_pattern number-shock is 2026-09-18's, wrong-diagnosis is 2026-09-17's, and the classifier fires number-shock on any number word.
- Why: two different patterns forced (finding 12); neither hook contains a digit or number word, so the classifier cannot land on a banned pattern; the numbers stay for the payoff scenes inside the number cap.
- 2026-09-19T12:34:01Z - Stage 04 gates (winner, draft B myth-bust): validator exit 0, zero blockers, zero advisories; eval_short exit 0 (number_spend 3/3 cap, hook_concrete via entity AMD, scene_specificity 9/9+2 allowance, skeleton and positional_labels clean); variety_check ok vs 15-entry ledger, then recorded (16 entries). Soft advisory entity_spend 0.312 vs 0.5 and top2 partial: kept, the extractor's missing entities are unspent on purpose (MI300X benchmark rows capped out; QLoRA/VRAM are glossary terms, not product names). Lexicon gained AMD/RDNA/TRL/PEFT/UI/SFT spoken forms; normalizer self-test 150/150.
- Why proceed on the soft failures: the number cap is the calibrated rule and the three spent numbers are the floors the video is about; padding narration with benchmark step-times to lift the entity ratio would break the cap and the one-number-at-a-time constraint.
- Judge: B beat A 19-18 (rows 2, 4, 8 for B; 5, 6, 7 for A); one graft taken (number-free honest-catch sentence), logged in drafts.md.
- 2026-09-19T12:36:04Z - Checkpoint (stage 05, step 3): title kept searchable 'Fine-tune on AMD: the ROCm Docker image' (39 chars, keyword chars 0-16); rubric 95 (description row 15/20 held back, first-150 window tight at 148 chars); description leads keyword-plus-promise, names the closest published video (Qwen Unsloth run, 2026-09-16), 3 hashtags, 14 tags.
- Why searchable over intriguing: autocomplete depth 16 on 'unsloth docker' is an install-hungry search audience; the two intriguing variants stay in the manifest for the human to swap at the gate.
- Compliance: contains_synthetic_media false (typographic scenes + the creator's own cloned voice, both exempt); original_insight names the stack-not-silicon framing plus the 1.39x-vs-2x honesty.

## Build journal
- 2026-09-19T11:50:56Z 03-research ok: 8 sources, 9 claims, validator exit 0
- 2026-09-19T12:34:01Z 04-script ok: draft B myth-bust wins 19-18, gates clean, ledger entry 16
- 2026-09-19T12:36:05Z 05-package ok: rubric 95, check_outputs clean, ready-to-build
- 2026-09-19T12:36:12Z 05-package ok: rubric 95, check_outputs clean, ready-to-build
- 2026-09-19T12:36:31Z build start on gn100-83c4
- 2026-09-19T12:42:15Z 06-voice fail 341s (voice QA failed: WER 0.067, 10 mismatch(es): expected 'point five finetunes in' heard 'five fine tunes and'; expected 'unslothrocm' heard 'unsloth rockum'; expe)
- 2026-09-19T12:46:23Z 06-voice fail 248s (voice QA failed: WER 0.097, 12 mismatch(es): expected 'point five finetunes' heard 'five fine tunes'; expected 'unslothrocm image' heard 'unsloth rock mimage'; )
- 2026-09-19T12:46:23Z blocked at 06-voice
- 2026-09-20T13:35:30Z 2026-09-20T13:35:30Z expired: not from today's picks (2026-09-20); the factory carries no backlog
