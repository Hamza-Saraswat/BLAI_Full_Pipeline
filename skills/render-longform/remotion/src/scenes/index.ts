import type React from "react";
import type { SceneProps, SceneType } from "../types";
import { BRoll } from "./BRoll";
import { ChapterCard } from "./ChapterCard";
import { Chart } from "./Chart";
import { CodeTyping } from "./CodeTyping";
import { ComparisonTable } from "./ComparisonTable";
import { Diagram } from "./Diagram";
import { EndCard } from "./EndCard";
import { KineticText } from "./KineticText";
import { MascotTalk } from "./MascotTalk";
import { Quote } from "./Quote";
import { StatCallout } from "./StatCallout";
import { TerminalReplay } from "./TerminalReplay";
import { TitleCard } from "./TitleCard";

export const SCENES: Record<SceneType, React.FC<SceneProps>> = {
  "title-card": TitleCard,
  "chapter-card": ChapterCard,
  "kinetic-text": KineticText,
  "code-typing": CodeTyping,
  "terminal-replay": TerminalReplay,
  diagram: Diagram,
  "comparison-table": ComparisonTable,
  chart: Chart,
  "stat-callout": StatCallout,
  quote: Quote,
  "mascot-talk": MascotTalk,
  "b-roll": BRoll,
  "end-card": EndCard,
};
