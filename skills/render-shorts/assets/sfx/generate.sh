#!/usr/bin/env bash
# Regenerates the bundled SFX set (license-free, synthesized, deterministic).
# Requires only ffmpeg (verified with 8.1.1). Same ffmpeg build => identical
# bytes (anoisesrc uses a fixed seed; aevalsrc random() starts from state 0).
#
# Usage: bash skills/render-shorts/assets/sfx/generate.sh
# Output: assets/sfx/{whoosh,pop,tick,ding,type}.wav
#         (48 kHz mono pcm_s16le, each peak-normalized to ~-20 dBFS)
#
# After regenerating, re-copy into the Remotion project:
#   cp skills/render-shorts/assets/sfx/*.wav skills/render-shorts/remotion/public/sfx/
set -euo pipefail

cd "$(dirname "$0")"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

synth() { # synth <name> <lavfi-source> <filter-chain>
  local name="$1" src="$2" af="$3"
  ffmpeg -y -hide_banner -loglevel error -f lavfi -i "$src" -af "$af" \
    -ar 48000 -ac 1 -c:a pcm_s16le "$TMP/$name.raw.wav"
  # Peak-normalize to -20 dBFS: measure max_volume, apply the delta.
  local max gain
  max=$(ffmpeg -hide_banner -i "$TMP/$name.raw.wav" -af volumedetect -f null - 2>&1 \
        | sed -n 's/.*max_volume: \(-\{0,1\}[0-9.]*\) dB.*/\1/p')
  gain=$(awk -v m="$max" 'BEGIN { printf "%.1f", -20 - m }')
  ffmpeg -y -hide_banner -loglevel error -i "$TMP/$name.raw.wav" \
    -af "volume=${gain}dB" -c:a pcm_s16le "$name.wav"
  echo "$name.wav  (raw peak ${max} dB, applied ${gain} dB)"
}

# whoosh: ~350ms pink noise through a band-pass whose center sweeps
# 1800 -> 380 Hz (asendcmd steps every 50ms), fast fade-in, long fade-out.
synth whoosh \
  "anoisesrc=r=48000:colour=pink:amplitude=0.8:seed=20260704:duration=0.35" \
  "asendcmd=c='0.05 bandpass@s f 1450; 0.10 bandpass@s f 1150; 0.15 bandpass@s f 900; 0.20 bandpass@s f 700; 0.25 bandpass@s f 520; 0.30 bandpass@s f 380',bandpass@s=f=1800:width_type=o:w=1.4,afade=t=in:d=0.04:curve=tri,afade=t=out:st=0.18:d=0.17:curve=tri"

# pop: ~120ms sine burst, exponential frequency sweep 400 -> 80 Hz
# (phase term = 2*pi * f0*T/ln(f1/f0) * (e^(ln(f1/f0)*t/T) - 1), with
# f0=400, f1=80, T=0.12 => K = -29.8241), fast amplitude decay.
synth pop \
  "aevalsrc='sin(2*PI*(-29.8241)*(exp(log(0.2)*t/0.12)-1))*exp(-t*28)':s=48000:d=0.12" \
  "afade=t=out:st=0.10:d=0.02"

# tick: ~60ms 2 kHz click with a very fast exponential decay.
synth tick \
  "aevalsrc='sin(2*PI*2000*t)*exp(-t*90)':s=48000:d=0.06" \
  "afade=t=out:st=0.05:d=0.01"

# ding: ~450ms two-partial chime (E6 1318.51 Hz + E7 2637.02 Hz at half
# amplitude), gentle decay - pleasant, not alarm-y.
synth ding \
  "aevalsrc='(sin(2*PI*1318.51*t)+0.5*sin(2*PI*2637.02*t))*exp(-t*7)':s=48000:d=0.45" \
  "afade=t=in:d=0.004:curve=tri,afade=t=out:st=0.40:d=0.05"

# type: ~50ms band-limited noise click (softer/duller than tick).
# aevalsrc random(0) starts from expression-state 0 => deterministic.
synth type \
  "aevalsrc='(2*random(0)-1)*exp(-t*130)':s=48000:d=0.05" \
  "lowpass=f=2200,highpass=f=500,afade=t=out:st=0.04:d=0.01"
