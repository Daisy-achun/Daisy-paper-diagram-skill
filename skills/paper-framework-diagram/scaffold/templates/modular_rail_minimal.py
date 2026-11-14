#!/usr/bin/env python3
"""Minimal network-rail × modular-pastel-stack template. Replace all labels."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scene_export import (  # noqa: E402
    FONT, Scene, to_svg, export_svg_png, export_pptx,
)

OUT = Path(__file__).resolve().parent / "_out_modular_rail"
COLS = [
    (28, 200, "#D6E6F5", "#5B7A9D", "1 · Encoder", "REPLACE"),
    (250, 220, "#EAF2FB", "#B0C4D8", "2 · Blocks", "Nx stack"),
    (494, 240, "#F7D6C8", "#C48B6A", "3 · Novel", "hero once"),
    (758, 200, "#E7F2E9", "#5A9A5A", "4 · Head", "logits"),
    (982, 180, "#F0EAF8", "#D0C4E0", "5 · Out", "y"),
]


def build() -> Scene:
    s = Scene()
    s.text(22, 28, "Fig. 1. <Paper>: modular rail (REPLACE TITLE)", size=FONT["title"], bold=True)
    s.rect(14, 56, 1140, 520, "#FAFAF7", "#CFCFC4", rx=12, dash=True)
    s.text(30, 84, "(a) Forward rail — pastel ops, no nested white cards",
           size=FONT["panel"], bold=True, fill="#444444")
    cy, ch = 110, 420
    for i, (x, w, fill, stroke, title, sub) in enumerate(COLS):
        sw = 2.2 if "Novel" in title else 1.4
        s.rect(x, cy, w, ch, fill, stroke, rx=10, sw=sw)
        s.text(x + 14, cy + 36, title, size=FONT["module"], bold=True)
        s.text(x + 14, cy + 64, sub, size=FONT["body"], fill="#555555")
        s.text(x + 14, cy + 100, "Method labels here", size=FONT["sec"], fill="#666666")
        s.text(x + 14, cy + 128, "· bullet 1", size=FONT["sec"])
        s.text(x + 14, cy + 150, "· bullet 2", size=FONT["sec"])
        if i < len(COLS) - 1:
            s.line(x + w, cy + ch / 2, COLS[i + 1][0], cy + ch / 2)
    # inset
    s.rect(1170, 56, 290, 520, "#FFF5EE", "#C48B6A", rx=12, dash=True, sw=1.8)
    s.text(1186, 88, "Inset · novel detail", size=FONT["panel"], bold=True, fill="#8A4A28")
    s.text(1186, 120, "Zoom the hero module", size=FONT["body"], fill="#8A4A28")
    s.text(1186, 150, "formula / sub-blocks", size=FONT["sec"], fill="#666666")
    return s


def main():
    sc = build()
    svg = to_svg(sc)
    svg_p, png_p = export_svg_png(svg, OUT, "modular_rail_minimal")
    pptx_p = export_pptx(sc, OUT, "modular_rail_minimal", png_p)
    print(svg_p); print(png_p); print(pptx_p)


if __name__ == "__main__":
    main()
