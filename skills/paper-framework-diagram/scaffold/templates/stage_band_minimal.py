#!/usr/bin/env python3
"""Minimal network-rail × stage-band-pastel template. Replace all labels."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scene_export import (  # noqa: E402
    FONT, Scene, to_svg, export_svg_png, export_pptx,
)

OUT = Path(__file__).resolve().parent / "_out_stage_band"
STAGES = [
    ("(a) Stage 1 · REPLACE", "#E6F2E8", "#6A9A6E", "#2F6B3A"),
    ("(b) Stage 2 · REPLACE", "#E4EEF7", "#6A8AB0", "#2F5A8A"),
    ("(c) Stage 3 · REPLACE", "#F8E8DC", "#C48B6A", "#8A4A28"),
]


def build() -> Scene:
    s = Scene()
    s.text(22, 28, "Fig. 1. <Paper>: multi-stage pipeline (REPLACE TITLE)",
           size=FONT["title"], bold=True)
    y = 52
    for title, fill, stroke, tc in STAGES:
        s.rect(16, y, 1448, 240, fill, stroke, rx=12, dash=True, sw=1.6)
        s.text(34, y + 28, title, size=FONT["panel"], bold=True, fill=tc)
        # three modules on tinted cards — NOT nested white
        for i, lab in enumerate(["Module A", "Module B", "Module C / novel"]):
            x = 40 + i * 460
            tint = fill
            sw = 2.0 if i == 2 else 1.3
            st = stroke if i != 2 else "#C48B6A"
            s.rect(x, y + 56, 420, 150, tint, st, rx=10, sw=sw)
            s.text(x + 16, y + 90, lab, size=FONT["module"], bold=True)
            s.text(x + 16, y + 118, "replace with Method bullets", size=FONT["body"], fill="#444444")
            s.text(x + 16, y + 146, "no white inner card", size=FONT["sec"], fill="#666666")
            if i < 2:
                s.line(x + 420, y + 130, x + 460, y + 130)
        y += 260
    return s


def main():
    sc = build()
    svg = to_svg(sc)
    svg_p, png_p = export_svg_png(svg, OUT, "stage_band_minimal")
    pptx_p = export_pptx(sc, OUT, "stage_band_minimal", png_p)
    print(svg_p); print(png_p); print(pptx_p)


if __name__ == "__main__":
    main()
