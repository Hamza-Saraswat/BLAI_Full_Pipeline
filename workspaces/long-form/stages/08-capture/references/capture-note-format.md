# Capture Note Format

## Window

Captures run in the `night` window (01:00-06:00 America/Chicago) unless the hub note says `capture_window: any`. The build agent defers the stage until the window opens.

## Layout

```
---
slug: [slug]
commands: 5
ran: 5
refused: 0
reconciled_lines: 3
---

# Capture: [slug]

## Results
| Id | Command | Exit | Seconds | Metric | Measured | Expected | Delta | Within tolerance |
|----|---------|------|---------|--------|----------|----------|-------|------------------|

## Reconciled lines
- Beat 3.2: "about twenty-two tokens per second" -> "about nineteen tokens per second" (measured 19.4, scripted 22, tolerance 10 %: rewritten? no -> blocked) 

## Skipped or refused
- cmd4: skipped, GPU memory below the required 60 GB free

## Recordings
[build-dir]/[slug]/capture/cmd1.cast ...
```

Every number in the Results table is copied from `capture.json`.
