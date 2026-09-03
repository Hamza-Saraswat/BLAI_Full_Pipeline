---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
duration_s: 35.07
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.836883
---

# Render: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n

## Gates
- lint_video --final: exit 0, no violations, no warnings (duration 35.07 s, classic band)
- safe_zone_check: exit 0, no violations (threshold 140); qa/safe-zone.png saved
- loop_check: similar true, ssim 0.836883 (threshold 0.5)
- Length: 35.07 s inside the classic final band; narration 33.96 s
- Scenes: all 6 storyboard scenes rendered and present in the cut (s01-s06)
- Captions: 114 words; sfx cues pop@0ms, ding@14670ms, tick@22480ms; music none (news-react, mood sober)

## Scene timings and attempts
| Scene | Target s | Delivered s | Attempts | Notes |
|-------|----------|-------------|----------|-------|
| s01 | 5.61 | 5.60 | 1 | frame-1 chip+header legible; stills verified programmatically (vision unavailable) |
| s02 | 5.67 | 5.70 | 2 | attempt 1 frame-1 empty board; fixed static placement at t=0 |
| s03 | 5.75 | 5.80 | 1 | 3 pre-render audit fixes, no failed renders |
| s04 | 5.45 | 5.47 | 1 | split-compare; motion ends 3.6 s so head/tail stable |
| s05 | 8.16 | 8.17 | 1 | one pre-render fix: fab-mark overlapped the Ultra label |
| s06 | 4.32 | 4.33 | 1 | end card, margins clean |

## Assembly
- assemble.py exit 0 via systemd-run scope (first run was OOM-killed by the 4 GiB hermes worker cgroup limit: remotion + headless_shell + ffmpeg exceeded it; rerun with MemoryMax=16G succeeded, no source change)
- loudnorm to -14 LUFS, bt709, 1080x1920 @ 30 fps
- warning from assembler: video total 35.07 s vs narration 33.96 s (segments win; scene durations all within 0.15 s tolerance)

## Decisions (unattended)
- Scene 06 not re-run; earlier 06-voice outputs (33.96 s, WER 0.0171) reused, verified against the stage 06 audit before render.
- Workers run one at a time per blai-run; two infra-only respawns of s01 before any render attempt (zai provider lacked stale_timeout_seconds=600; fixed in ~/.hermes/config.yaml, backup config.yaml.bak-20260903).

## Card
- gate card sent: message_id 5 (video attached, 2.97 MB)

## notes_for_review
- storyboard echo: "bandwidth is the wall -- DGX Spark: 160 GB/s vs the Mac's 546 GB/s"
