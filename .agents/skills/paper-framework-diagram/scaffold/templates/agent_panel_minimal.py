#!/usr/bin/env python3
"""Minimal agent-loop × agent-panel template.

Copy → rename → replace ALL labels with the current Method.
Do NOT ship this placeholder text as a real paper figure.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scene_export import (  # noqa: E402
    CREAM, CREAM_STROKE, BLUE, BLUE_STROKE, LAVENDER, LAVENDER_STROKE,
    PEACH, PEACH_STROKE, TOOLS, TOOLS_STROKE, MINT, MINT_STROKE,
    FONT, Scene, to_svg, export_svg_png, export_pptx,
)

OUT = Path(__file__).resolve().parent / "_out_agent_panel"


def build() -> Scene:
    s = Scene()
    s.text(22, 28, "Fig. 1. <Paper>: Agent loop over tool bank (REPLACE TITLE)",
           size=FONT["title"], bold=True)
    s.rect(1180, 8, 280, 34, "#FAFAFA", "#BDBDBD", rx=8, dash=True)
    s.text(1194, 30, "🔥 trainable   ❄ frozen/tools", size=FONT["sec"], fill="#444444")

    # cream hero
    s.rect(16, 52, 1148, 520, CREAM, CREAM_STROKE, rx=14, sw=1.8)
    s.text(34, 78, "(a) Inference — Think → Call → Observe", size=FONT["panel"], bold=True, fill="#5D4037")

    s.rect(34, 110, 140, 170, "#FFE082", "#C9A227", rx=10)
    s.text(104, 190, "Input", size=FONT["module"], bold=True, anchor="middle")
    s.text(104, 212, "x / image", size=FONT["sec"], anchor="middle", fill="#5D4037")
    s.line(174, 195, 200, 195)

    s.rect(200, 110, 160, 170, PEACH, PEACH_STROKE, rx=10, sw=2.0)
    s.text(280, 185, "Policy 🔥", size=FONT["module"], bold=True, anchor="middle", fill="#BF360C")
    s.text(280, 210, "MLLM / LoRA", size=FONT["body"], anchor="middle", fill="#E65100")
    s.line(360, 195, 386, 195)

    s.rect(386, 104, 520, 186, "#FFFDE7", "#5B9BD5", rx=12, dash=True, sw=1.8)
    s.text(402, 128, "Agent loop", size=FONT["module"], bold=True, fill="#1565C0")
    s.rect(402, 144, 140, 70, "#BBDEFB", "#1976D2", rx=10)
    s.text(472, 178, "Thought", size=FONT["module"], bold=True, anchor="middle", fill="#0D47A1")
    s.line(542, 179, 562, 179)
    s.rect(562, 144, 150, 70, PEACH, PEACH_STROKE, rx=10, sw=2.0)
    s.text(637, 178, "Call tool", size=FONT["module"], bold=True, anchor="middle", fill="#BF360C")
    s.line(712, 179, 732, 179)
    s.rect(732, 144, 150, 70, "#FFF59D", "#F9A825", rx=10)
    s.text(807, 178, "Observe", size=FONT["module"], bold=True, anchor="middle", fill="#F57F17")

    s.rect(34, 300, 340, 150, "#FFE082", "#C9A227", rx=10, dash=True)
    s.text(48, 326, "Trajectory (replace turns)", size=FONT["module"], bold=True, fill="#5D4037")
    s.rect(48, 344, 90, 80, BLUE, BLUE_STROKE, rx=8)
    s.text(93, 384, "T1", size=FONT["body"], bold=True, anchor="middle", fill="#0D47A1")
    s.rect(150, 344, 90, 80, PEACH, PEACH_STROKE, rx=8)
    s.text(195, 384, "T2", size=FONT["body"], bold=True, anchor="middle", fill="#E65100")
    s.rect(252, 344, 90, 80, MINT, MINT_STROKE, rx=8)
    s.text(297, 384, "Ans", size=FONT["body"], bold=True, anchor="middle", fill="#2E7D32")

    s.rect(390, 300, 250, 150, BLUE, BLUE_STROKE, rx=10)
    s.text(404, 330, "Stream / mode A", size=FONT["module"], bold=True, fill="#0D47A1")
    s.text(404, 356, "replace with Method", size=FONT["body"], fill="#1565C0")
    s.rect(656, 300, 250, 150, PEACH, PEACH_STROKE, rx=10, sw=1.8)
    s.text(670, 330, "Stream / mode B  (novel)", size=FONT["module"], bold=True, fill="#BF360C")
    s.text(670, 356, "replace with Method", size=FONT["body"], fill="#E65100")

    s.rect(34, 468, 872, 80, MINT, MINT_STROKE, rx=10)
    s.text(48, 504, "Output · label + explanation (+ evidence). REPLACE.",
           size=FONT["body"], bold=True, fill="#1B5E20")

    s.rect(930, 110, 218, 380, TOOLS, TOOLS_STROKE, rx=12, sw=1.8)
    s.text(1039, 150, "Tool Bank ❄", size=FONT["module"], bold=True, anchor="middle", fill="#0D47A1")
    for i, lab in enumerate(["tool_a", "tool_b", "tool_c", "… hot-plug"]):
        s.text(950, 190 + i * 28, "·  " + lab, size=FONT["body"], fill="#333333")

    # footers — rename if Method has no SFT/RL
    s.rect(16, 590, 718, 250, BLUE, BLUE_STROKE, rx=12)
    s.text(34, 622, "(b1) Offline / Stage A  (rename)", size=FONT["panel"], bold=True, fill="#0D47A1")
    s.text(34, 652, "Replace with Method offline/eval/SFT block", size=FONT["body"], fill="#1565C0")

    s.rect(746, 590, 718, 250, LAVENDER, LAVENDER_STROKE, rx=12)
    s.text(764, 622, "(b2) Offline / Stage B  (rename)", size=FONT["panel"], bold=True, fill="#4527A0")
    s.text(764, 652, "Replace with Method RL/analysis block — or delete if N/A",
           size=FONT["body"], fill="#5E35B1")
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
