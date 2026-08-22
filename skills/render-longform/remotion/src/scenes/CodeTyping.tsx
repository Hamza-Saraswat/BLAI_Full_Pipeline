// Code typed onto a card at about 18 characters per second with a caret.
// No syntax library: a few regex token classes colored with the brand palette.
import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, MONO_FONT, MUTED, OK, SAFE, TEXT, TYPING_CHARS_PER_SECOND } from "../constants";
import { getString } from "../data";
import { SceneFrame } from "../SceneFrame";
import type { SceneProps } from "../types";
import { Card, syncAt } from "../ui";

const KEYWORDS = new Set([
  "def", "return", "import", "from", "if", "else", "elif", "for", "while", "in", "not", "and", "or", "with", "as",
  "class", "const", "let", "var", "function", "export", "async", "await", "true", "false", "null", "None", "True",
  "False", "docker", "run", "pull", "serve", "python3", "pip", "npm", "npx", "ollama", "vllm", "curl", "export",
  "FROM", "RUN", "CMD", "ENV", "sudo", "apt", "git", "cd", "echo", "huggingface-cli", "hf", "llama-server",
]);

type Token = { text: string; color: string; bold?: boolean };

const TOKEN_RE = /(#[^\n]*|\/\/[^\n]*)|("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')|(--?[A-Za-z][\w-]*)|(\b\d+(?:\.\d+)?[A-Za-z%]*\b)|([A-Za-z_][\w-]*)|(\s+|[^\sA-Za-z_\d"'#\/-]+|\/|-)/g;

const tokenize = (code: string): Token[] => {
  const out: Token[] = [];
  for (const m of code.matchAll(TOKEN_RE)) {
    if (m[1] !== undefined) out.push({ text: m[1], color: MUTED });
    else if (m[2] !== undefined) out.push({ text: m[2], color: OK });
    else if (m[3] !== undefined) out.push({ text: m[3], color: ACCENT });
    else if (m[4] !== undefined) out.push({ text: m[4], color: TEXT, bold: true });
    else if (m[5] !== undefined) out.push({ text: m[5], color: KEYWORDS.has(m[5]) ? ACCENT : TEXT, bold: KEYWORDS.has(m[5]) });
    else out.push({ text: m[0], color: TEXT });
  }
  return out;
};

const VISIBLE_LINES = 18;

export const CodeTyping: React.FC<SceneProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const code = getString(p.scene.data, "code", "").replace(/\r\n/g, "\n").replace(/\n+$/, "");
  const language = getString(p.scene.data, "language", "shell");
  const title = getString(p.scene.data, "title", getString(p.scene.data, "filename", ""));
  const durationS = p.layout.durationInFrames / fps;
  const startS = syncAt(p.layout, "type") ?? 0.4;
  const available = Math.max(1, durationS * 0.85 - startS);
  const cps = Math.max(TYPING_CHARS_PER_SECOND, code.length / available);
  const typed = Math.max(0, Math.min(code.length, Math.floor((frame / fps - startS) * cps)));
  const done = typed >= code.length;
  const caretOn = done ? Math.floor(frame / (fps / 2)) % 2 === 0 : true;
  const tokens = React.useMemo(() => tokenize(code), [code]);

  // Tokens up to `typed` characters, then only the last VISIBLE_LINES lines.
  const shown: Token[] = [];
  let count = 0;
  for (const tk of tokens) {
    if (count >= typed) break;
    const take = Math.min(tk.text.length, typed - count);
    shown.push({ ...tk, text: tk.text.slice(0, take) });
    count += take;
  }
  const text = shown.map((s) => s.text).join("");
  const lineCount = text.split("\n").length;
  const skip = Math.max(0, lineCount - VISIBLE_LINES);
  let skipped = 0;
  const visible: Token[] = [];
  for (const tk of shown) {
    if (skipped >= skip) {
      visible.push(tk);
      continue;
    }
    const parts = tk.text.split("\n");
    const need = skip - skipped;
    if (parts.length - 1 <= need) {
      skipped += parts.length - 1;
    } else {
      visible.push({ ...tk, text: parts.slice(need).join("\n") });
      skipped = skip;
    }
  }

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
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 16,
            padding: "18px 32px",
            borderBottom: "2px solid rgba(245,240,232,0.12)",
            fontSize: 26,
            fontWeight: 700,
            color: MUTED,
          }}
        >
          <span style={{ padding: "4px 14px", borderRadius: 8, backgroundColor: ACCENT, color: "#0B1020" }}>
            {language}
          </span>
          <span>{title}</span>
        </div>
        <pre
          style={{
            margin: 0,
            padding: "28px 36px",
            fontFamily: MONO_FONT,
            fontSize: 38,
            lineHeight: 1.35,
            whiteSpace: "pre-wrap",
            wordBreak: "break-word",
            color: TEXT,
          }}
        >
          {visible.map((tk, i) => (
            <span key={i} style={{ color: tk.color, fontWeight: tk.bold ? 700 : 400 }}>
              {tk.text}
            </span>
          ))}
          <span
            style={{
              display: "inline-block",
              width: 20,
              height: 44,
              marginLeft: 2,
              verticalAlign: "text-bottom",
              backgroundColor: ACCENT,
              opacity: caretOn ? 1 : 0,
            }}
          />
        </pre>
      </Card>
    </SceneFrame>
  );
};
