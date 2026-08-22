// Small accessors for the untyped `scene.data` object.
import type { SceneData } from "./types";

export const getString = (data: SceneData | undefined, key: string, fallback = ""): string => {
  const v = data?.[key];
  return typeof v === "string" ? v : v == null ? fallback : String(v);
};

export const getNumber = (data: SceneData | undefined, key: string, fallback: number | null = null): number | null => {
  const v = data?.[key];
  if (typeof v === "number" && Number.isFinite(v)) return v;
  if (typeof v === "string") {
    const n = Number(v.replace(/[^0-9.eE+-]/g, ""));
    if (Number.isFinite(n) && v.trim() !== "") return n;
  }
  return fallback;
};

export const getBool = (data: SceneData | undefined, key: string, fallback = false): boolean => {
  const v = data?.[key];
  return typeof v === "boolean" ? v : fallback;
};

export const getArray = <T = unknown>(data: SceneData | undefined, key: string): T[] => {
  const v = data?.[key];
  return Array.isArray(v) ? (v as T[]) : [];
};

export const getStringArray = (data: SceneData | undefined, key: string): string[] =>
  getArray<unknown>(data, key).map((x) => (typeof x === "string" ? x : String(x)));

export const splitWords = (s: string): string[] => s.split(/\s+/).filter((w) => w.length > 0);

/** Chunk a line into groups of at most `max` words. */
export const chunkWords = (line: string, max: number): string[] => {
  const words = splitWords(line);
  const out: string[] = [];
  for (let i = 0; i < words.length; i += max) out.push(words.slice(i, i + max).join(" "));
  return out.length > 0 ? out : [""];
};

/** Parse a numeric value such as "41.7", "1,250", "$3,999" or 128. */
export const parseNumeric = (value: unknown): { num: number | null; decimals: number; prefix: string; suffix: string } => {
  if (typeof value === "number") {
    const decimals = Number.isInteger(value) ? 0 : Math.min(2, (String(value).split(".")[1] || "").length);
    return { num: value, decimals, prefix: "", suffix: "" };
  }
  const s = String(value ?? "").trim();
  const m = s.match(/^([^0-9-]*)(-?[0-9][0-9,]*(?:\.[0-9]+)?)(.*)$/);
  if (!m) return { num: null, decimals: 0, prefix: "", suffix: s };
  const raw = m[2].replace(/,/g, "");
  const num = Number(raw);
  const decimals = (raw.split(".")[1] || "").length;
  return { num: Number.isFinite(num) ? num : null, decimals, prefix: m[1], suffix: m[3] };
};

export const formatNumber = (n: number, decimals: number): string =>
  n.toLocaleString("en-US", { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
