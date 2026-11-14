#!/usr/bin/env python3
"""Minimal agent-loop × agent-panel template — SINGLE SPINE only.

Copy → rename → replace ALL labels with the current Method.
Do NOT ship this placeholder text as a real paper figure.

Storyboard rules (mandatory):
  - One primary rail: Input → Policy → Loop → Tool runtime → Output
  - Tools / traj hang ON the rail (on-path evidence)
  - DO NOT add a Verify / ablation side column
  - DO NOT keep (b1)/(b2) footers unless Method truly has those stages
  - Offline eval → title footnote or separate figure
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scene_export import (  # noqa: E402
    CREAM, CREAM_STROKE, BLUE, BLUE_STROKE,
    PEACH, PEACH_STROKE, TOOLS, TOOLS_STROKE, MINT, MINT_STROKE,
    FONT, Scene, to_svg, export_svg_png, export_pptx,
)

OUT = Path(__file__).resolve().parent / "_out_agent_panel"


def build() -> Scene:
    s = Scene()
    s.text(22, 28, "Fig. 1. <Paper>: Agent loop (REPLACE — single spine)",
           size=FONT["title"], bold=True)
    s.rect(1100, 8, 360, 32, "#FAFAFA", "#BDBDBD", rx=8, dash=True)
    s.text(1114, 28, "❄/🔥 legend · offline eval → see text", size=FONT["sec"], fill="#444444")

    # Full-width cream hero — one narrative
    s.rect(16, 52, 1448, 760, CREAM, CREAM_STROKE, rx=14, sw=1.8)
    s.text(34, 78, "Inference spine — Input → Policy → Loop → Tools → Output",
           size=FONT["panel"], bold=True, fill="#5D4037")

    s.rect(34, 110, 150, 190, "#FFE082", "#C9A227", rx=10)
    s.text(109, 190, "Input", size=FONT["module"], bold=True, anchor="middle")
    s.text(109, 214, "x / image", size=FONT["sec"], anchor="middle", fill="#5D4037")
    s.line(184, 205, 214, 205)

    s.rect(214, 110, 170, 190, PEACH, PEACH_STROKE, rx=10, sw=2.0)
    s.text(299, 190, "Policy ❄/🔥", size=FONT["module"], bold=True, anchor="middle", fill="#BF360C")
    s.text(299, 216, "MLLM / rules", size=FONT["body"], anchor="middle", fill="#E65100")
    s.line(384, 205, 414, 205)

    s.rect(414, 100, 620, 210, "#FFFDE7", "#5B9BD5", rx=12, dash=True, sw=1.8)
    s.text(430, 128, "Agent loop  ·  Thought → Call → Observe",
           size=FONT["module"], bold=True, fill="#1565C0")
    s.rect(434, 148, 160, 90, "#BBDEFB", "#1976D2", rx=10)
    s.text(514, 190, "Thought", size=FONT["module"], bold=True, anchor="middle", fill="#0D47A1")
    s.line(594, 193, 620, 193)
    s.rect(620, 148, 170, 90, PEACH, PEACH_STROKE, rx=10, sw=2.0)
    s.text(705, 190, "Call tool", size=FONT["module"], bold=True, anchor="middle", fill="#BF360C")
    s.line(790, 193, 816, 193)
    s.rect(816, 148, 170, 90, "#FFF59D", "#F9A825", rx=10)
    s.text(901, 190, "Observe", size=FONT["module"], bold=True, anchor="middle", fill="#F57F17")
    s.text(720, 278, "loop until finish", size=FONT["sec"], bold=True, anchor="middle", fill="#1565C0")

    s.line(1034, 180, 1064, 180, color="#1976D2", sw=1.8)

    s.rect(1064, 100, 380, 210, TOOLS, TOOLS_STROKE, rx=12, sw=1.8)
    s.text(1254, 160, "Tool runtime ❄", size=FONT["module"], bold=True, anchor="middle", fill="#0D47A1")
    s.text(1254, 190, "hot-plug · fixed obs schema", size=FONT["body"], anchor="middle", fill="#1565C0")
    s.text(1084, 240, "· tool_a  · tool_b  · tool_c  (REPLACE)", size=FONT["body"], fill="#333333")

    # On-path evidence (not a second story)
    s.rect(34, 340, 500, 180, BLUE, BLUE_STROKE, rx=10)
    s.text(50, 370, "Tool family A  (on-path)", size=FONT["module"], bold=True, fill="#0D47A1")
    s.text(50, 400, "REPLACE names + chips", size=FONT["body"], fill="#1565C0")
    s.rect(550, 340, 500, 180, PEACH, PEACH_STROKE, rx=10, sw=1.8)
    s.text(566, 370, "Tool family B  (on-path / novel)", size=FONT["module"], bold=True, fill="#BF360C")
    s.text(566, 400, "REPLACE names + chips", size=FONT["body"], fill="#E65100")
    s.line(705, 238, 705, 320, color="#EF6C00", sw=1.6, arrow=False)
    s.line(705, 320, 284, 340, color="#EF6C00", sw=1.5, arrow=True)
    s.line(705, 320, 800, 340, color="#EF6C00", sw=1.5, arrow=True)

    s.rect(1070, 340, 374, 180, BLUE, BLUE_STROKE, rx=12, dash=True, sw=1.4)
    s.text(1257, 380, "Obs / evidence card", size=FONT["module"], bold=True, anchor="middle", fill="#0D47A1")
    s.text(1257, 420, "fixed schema → policy", size=FONT["body"], anchor="middle", fill="#1565C0")

    s.rect(34, 550, 1410, 70, "#FFFDE7", "#E0C86A", rx=10, dash=True)
    s.text(50, 592, "traj:  Think → tool → … → finish   (REPLACE turns)",
           size=FONT["body"], bold=True, fill="#5D4037")

    s.rect(34, 650, 1410, 120, MINT, MINT_STROKE, rx=12, sw=1.8)
    s.text(50, 700, "Output · verdict + evidence_refs (+ maps). REPLACE.",
           size=FONT["panel"], bold=True, fill="#1B5E20")
    s.text(50, 736, "No Verify/ablation column · No offline dual footer unless Method needs it",
           size=FONT["sec"], fill="#2E7D32")
    return s


def main():
    sc = build()
    svg = to_svg(sc)
    svg_p, png_p = export_svg_png(svg, OUT, "agent_panel_minimal")
    pptx_p = export_pptx(sc, OUT, "agent_panel_minimal", png_p)
    print(svg_p)
    print(png_p)
    print(pptx_p)


if __name__ == "__main__":
    main()
