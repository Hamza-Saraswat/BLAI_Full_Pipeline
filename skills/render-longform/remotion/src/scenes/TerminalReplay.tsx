// Replays a captured command. The command is typed first; then either the
// asciinema v2 cast plays (scaled to fit the scene by default) or the stdout
// transcript appears line by line. Exit code and measured metrics show at the end.
import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, BG, ERR, MONO_FONT, MUTED, OK, SAFE, TEXT } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { Capture, SceneProps } from "../types";
import { Card, syncAt } from "../ui";

const VISIBLE_LINES = 20;
const COMMAND_CPS = 30;

type CastEvent = { t: number; data: string };

/** Parse an asciinema v2 file (header line + one JSON event per line). */
export const parseCast = (cast: string): { events: CastEvent[]; duration: number } => {
  const events: CastEvent[] = [];
  const lines = cast.split(/\r?\n/).filter((l) => l.trim().length > 0);
  for (let i = 0; i < lines.length; i++) {
    try {
      const v = JSON.parse(lines[i]);
      if (Array.isArray(v) && v.length >= 3 && typeof v[0] === "number" && (v[1] === "o" || v[1] === "i")) {
        if (v[1] === "o") events.push({ t: v[0], data: String(v[2]) });
      }
    } catch {
      // header or a broken line; skip
    }
  }
  return { events, duration: events.length ? events[events.length - 1].t : 0 };
};

const ANSI_RE = /\x1b\[[0-9;?]*[A-Za-z]|\x1b\][^\x07]*(\x07|\x1b\\)|\x1b[()][A-Za-z0-9]|\x1b[=>]/g;

/** Turn raw terminal output into screen lines (handles \r overwrites). */
export const toLines = (raw: string): string[] => {
  const text = raw.replace(ANSI_RE, "").replace(/\r\n/g, "\n");
  const lines: string[] = [""];
  for (const ch of text) {
    if (ch === "\n") lines.push("");
    else if (ch === "\r") lines[lines.length - 1] = "";
    else if (ch === "\t") lines[lines.length - 1] += "    ";
    else if (ch === "\b") lines[lines.length - 1] = lines[lines.length - 1].slice(0, -1);
    else lines[lines.length - 1] += ch;
  }
  return lines;
};

const metricChips = (capture: Capture | undefined): string[] => {
  const m = capture?.metrics ?? {};
  const chips: string[] = [];
  if (m.tok_s != null) chips.push(`${m.tok_s} tok/s`);
  if (m.vram_gb != null) chips.push(`${m.vram_gb} GB used`);
  if (m.load_s != null) chips.push(`load ${m.load_s} s`);
  if (m.ttft_ms != null) chips.push(`TTFT ${m.ttft_ms} ms`);
  return chips;
};

export const TerminalReplay: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const ref = p.scene.capture_ref ?? getString(p.scene.data, "capture_ref", "");
  const capture = p.captures[ref];
  const command = capture?.command ?? getString(p.scene.data, "command", ref ? `# capture ${ref}` : "");
  const playback = getString(p.scene.data, "playback", "fit");
  const durationS = p.layout.durationInFrames / fps;
  const t = frame / fps;
  const cmdTyped = Math.min(command.length, Math.floor((t - 0.3) * COMMAND_CPS));
  const cmdDone = 0.3 + command.length / COMMAND_CPS;
  const startS = syncAt(p.layout, "run") ?? cmdDone + 0.5;
  const available = Math.max(0.5, durationS - startS - 0.6);
  const local = t - startS;

  const parsed = React.useMemo(() => (capture?.cast ? parseCast(capture.cast) : null), [capture?.cast]);
  let lines: string[] = [];
  let finished = false;
  if (parsed && parsed.events.length > 0) {
    const factor = playback === "realtime" ? 1 : Math.min(1, available / Math.max(0.01, parsed.duration));
    let raw = "";
    for (const ev of parsed.events) {
      if (ev.t * factor <= local) raw += ev.data;
      else break;
    }
    lines = toLines(raw);
    finished = parsed.duration * factor <= local;
  } else if (capture?.stdout) {
    const all = capture.stdout.replace(/\n+$/, "").split("\n");
    const per = available / Math.max(1, all.length);
    const n = Math.max(0, Math.min(all.length, Math.floor(local / per) + (local >= 0 ? 1 : 0)));
    lines = all.slice(0, n);
    finished = n >= all.length;
  } else if (local >= 0) {
    lines = [`(no capture found for "${ref}")`];
    finished = true;
  }
  const shown = lines.slice(Math.max(0, lines.length - VISIBLE_LINES));
  const exit = capture?.exit;
  const chips = finished ? metricChips(capture) : [];

  return (
    <SceneFrame scene={p.scene} layout={p.layout} sceneWords={p.sceneWords}>
      <Card
        style={{
          position: "absolute",
          left: SAFE.left,
          top: SAFE.top + 70,
          width: SAFE.width,
          height: SAFE.height - 240,
          overflow: "hidden",
          backgroundColor: "#070B18",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 10, padding: "16px 28px", borderBottom: "2px solid rgba(245,240,232,0.12)" }}>
          <span style={{ width: 16, height: 16, borderRadius: 8, backgroundColor: ERR }} />
          <span style={{ width: 16, height: 16, borderRadius: 8, backgroundColor: ACCENT }} />
          <span style={{ width: 16, height: 16, borderRadius: 8, backgroundColor: OK }} />
          <span style={{ marginLeft: 18, fontSize: 24, color: MUTED, fontWeight: 700 }}>dgx-spark</span>
          <span style={{ flex: 1 }} />
          {finished && typeof exit === "number" ? (
            <span style={{ fontSize: 24, fontWeight: 700, color: exit === 0 ? OK : ERR }}>exit {exit}</span>
          ) : null}
        </div>
        <pre
          style={{
            margin: 0,
            padding: "24px 32px",
            fontFamily: MONO_FONT,
            fontSize: 32,
            lineHeight: 1.35,
            whiteSpace: "pre-wrap",
            wordBreak: "break-all",
            color: TEXT,
          }}
        >
          <span style={{ color: OK, fontWeight: 700 }}>$ </span>
          <span style={{ color: TEXT, fontWeight: 700 }}>{command.slice(0, Math.max(0, cmdTyped))}</span>
          {t < startS ? <span style={{ display: "inline-block", width: 18, height: 36, backgroundColor: ACCENT, verticalAlign: "text-bottom" }} /> : null}
          {local >= 0 ? "\n" : ""}
          {shown.join("\n")}
        </pre>
        {chips.length > 0 ? (
          <div style={{ position: "absolute", right: 28, bottom: 22, display: "flex", gap: 14 }}>
            {chips.map((c) => (
              <span key={c} style={{ padding: "8px 18px", borderRadius: 10, backgroundColor: ACCENT, color: BG, fontSize: 28, fontWeight: 800 }}>
                {c}
              </span>
            ))}
          </div>
        ) : null}
      </Card>
    </SceneFrame>
  );
};
