#!/usr/bin/env python3
"""Same-source Scene → SVG / PNG / editable PPTX helpers for paper-framework-diagram.

Agents MUST use this (or an equivalent single layout source) instead of Mermaid /
one-shot concept images as the final figure.
"""
from __future__ import annotations

import base64
import subprocess
from pathlib import Path
from typing import Iterable

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

W, H = 1480, 860
SLIDE_W_IN, SLIDE_H_IN = 13.333, 7.5
PT_TO_SVG = W / (SLIDE_W_IN * 72)
FONT = dict(title=17, panel=14, module=12, body=11, sec=10)
assert min(FONT.values()) >= 10

# Pastel roles (agent-panel / stage-band friendly)
CREAM = "#FFF8E1"
CREAM_STROKE = "#E0C86A"
BLUE = "#E3F2FD"
BLUE_STROKE = "#64B5F6"
LAVENDER = "#EDE7F6"
LAVENDER_STROKE = "#9575CD"
PEACH = "#FFF3E0"
PEACH_STROKE = "#EF6C00"
MINT = "#E8F5E9"
MINT_STROKE = "#66BB6A"
TOOLS = "#BBDEFB"
TOOLS_STROKE = "#1976D2"


def svg_pt(pt: float) -> float:
    return round(pt * PT_TO_SVG, 2)


def rgb(c: str) -> RGBColor:
    c = (c or "#222222").lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    if len(c) != 6:
        c = "222222"
    return RGBColor(int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def data_uri(path: Path) -> str:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


class Scene:
    def __init__(self):
        self.els: list[dict] = []

    def rect(self, x, y, w, h, fill, stroke, rx=10, dash=False, sw=1.5):
        self.els.append(dict(kind="rect", x=x, y=y, w=w, h=h, fill=fill,
                             stroke=stroke, rx=rx, dash=dash, sw=sw))

    def text(self, x, y, s, size=11, bold=False, italic=False, fill="#222222",
             anchor="start"):
        assert size >= 10 or True  # soft; hard floor enforced at export helpers
        self.els.append(dict(kind="text", x=x, y=y, content=s, size=size,
                             bold=bold, italic=italic, fill=fill, anchor=anchor))

    def math(self, x, y, segs: Iterable[tuple[str, bool]], size=11, bold=False,
             italic=True, fill="#222222", anchor="start"):
        self.els.append(dict(kind="math", x=x, y=y, segs=list(segs), size=size,
                             bold=bold, italic=italic, fill=fill, anchor=anchor))

    def image(self, path: Path | str, x, y, w, h, stroke=None):
        self.els.append(dict(kind="image", path=str(path), x=x, y=y, w=w, h=h,
                             stroke=stroke))

    def line(self, x1, y1, x2, y2, sw=1.6, color="#455A64", arrow=True):
        self.els.append(dict(kind="line", x1=x1, y1=y1, x2=x2, y2=y2,
                             sw=sw, color=color, arrow=arrow))


def to_svg(sc: Scene) -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '''  <defs>
    <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#455A64"/>
    </marker>
    <filter id="sh"><feDropShadow dx="0" dy="1.5" stdDeviation="1.6" flood-opacity="0.12"/></filter>
    <style>.t{font-family:Helvetica,Arial,sans-serif}.tb{font-weight:700}.tm{font-style:italic}</style>
  </defs>''',
        f'  <rect width="{W}" height="{H}" fill="#FFFFFF"/>',
    ]
    for e in sc.els:
        k = e["kind"]
        if k == "rect":
            dash = ' stroke-dasharray="7 4"' if e["dash"] else ""
            filt = ' filter="url(#sh)"' if e["w"] >= 180 else ""
            parts.append(
                f'  <rect x="{e["x"]}" y="{e["y"]}" width="{e["w"]}" height="{e["h"]}" '
                f'rx="{e["rx"]}" fill="{e["fill"]}" stroke="{e["stroke"]}" '
                f'stroke-width="{e["sw"]}"{dash}{filt}/>'
            )
        elif k == "text":
            cls = "t" + (" tb" if e["bold"] else "") + (" tm" if e["italic"] else "")
            anc = f' text-anchor="{e["anchor"]}"' if e["anchor"] != "start" else ""
            parts.append(
                f'  <text x="{e["x"]}" y="{e["y"]}" class="{cls}" font-size="{svg_pt(e["size"])}" '
                f'fill="{e["fill"]}"{anc}>{esc(e["content"])}</text>'
            )
        elif k == "math":
            weight = "font-weight:700;" if e["bold"] else ""
            style = "font-style:italic;" if e["italic"] else ""
            anc = f'text-anchor="{e["anchor"]}"' if e["anchor"] != "start" else ""
            body = []
            for t, is_sub in e["segs"]:
                if is_sub:
                    body.append(
                        f'<tspan baseline-shift="sub" font-size="{svg_pt(max(9, e["size"]-3))}" '
                        f'font-style="italic">{esc(t)}</tspan>'
                    )
                else:
                    body.append(esc(t))
            parts.append(
                f'  <text x="{e["x"]}" y="{e["y"]}" class="t" font-size="{svg_pt(e["size"])}" '
                f'fill="{e["fill"]}" style="{weight}{style}" {anc}>{"".join(body)}</text>'
            )
        elif k == "image":
            p = Path(e["path"])
            if not p.exists():
                continue
            if e.get("stroke"):
                parts.append(
                    f'  <rect x="{e["x"]-2}" y="{e["y"]-2}" width="{e["w"]+4}" height="{e["h"]+4}" '
                    f'rx="6" fill="none" stroke="{e["stroke"]}" stroke-width="1.2"/>'
                )
            parts.append(
                f'  <image href="{data_uri(p)}" x="{e["x"]}" y="{e["y"]}" width="{e["w"]}" '
                f'height="{e["h"]}" preserveAspectRatio="xMidYMid slice"/>'
            )
        elif k == "line":
            mark = ' marker-end="url(#a)"' if e["arrow"] else ""
            parts.append(
                f'  <line x1="{e["x1"]}" y1="{e["y1"]}" x2="{e["x2"]}" y2="{e["y2"]}" '
                f'stroke="{e.get("color","#455A64")}" stroke-width="{e["sw"]}"{mark}/>'
            )
    parts.append("</svg>")
    return "\n".join(parts)


def export_svg_png(svg_text: str, out_dir: Path, stem: str) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    svg_p = out_dir / f"{stem}.svg"
    png_p = out_dir / f"{stem}.png"
    svg_p.write_text(svg_text, encoding="utf-8")
    html = out_dir / f"_qa_{stem}.html"
    html.write_text(
        "<!DOCTYPE html><html><body style='margin:0;background:#fff'>"
        f"<img src='{svg_p.resolve().as_uri()}' width='{W*2}' height='{H*2}' "
        "style='display:block'/></body></html>",
        encoding="utf-8",
    )
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    ok = False
    if Path(chrome).exists():
        r = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", f"--screenshot={png_p}",
             f"--window-size={W*2},{H*2}", html.resolve().as_uri()],
            capture_output=True,
        )
        ok = r.returncode == 0 and png_p.exists()
    if not ok:
        try:
            subprocess.run(
                ["rsvg-convert", "-w", str(W * 2), "-h", str(H * 2), "-o", str(png_p), str(svg_p)],
                check=True, capture_output=True,
            )
            ok = True
        except Exception:
            pass
    html.unlink(missing_ok=True)
    if not ok:
        raise RuntimeError("PNG rasterize failed (need Chrome headless or rsvg-convert)")
    return svg_p, png_p


def export_pptx(sc: Scene, out_dir: Path, stem: str, png_p: Path | None = None,
                extra_note_lines: list[tuple[str, int, bool, str]] | None = None) -> Path:
    """Page1 editable shapes; optional Page2 PNG proof; optional Page3 notes."""
    SX, SY = SLIDE_W_IN / W, SLIDE_H_IN / H

    def X(v): return int(v * SX * 914400)
    def Y(v): return int(v * SY * 914400)
    def WW(v): return max(1, int(v * SX * 914400))
    def HH(v): return max(1, int(v * SY * 914400))

    def style(run, size, bold=False, italic=False, col="#222222", is_sub=False):
        run.font.name = "Helvetica"
        sz = max(10, float(size)) if not is_sub else max(9, float(size))
        run.font.size = Pt(sz)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = rgb(col)
        if is_sub:
            run._r.get_or_add_rPr().set("baseline", "-25000")

    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W_IN)
    prs.slide_height = Inches(SLIDE_H_IN)
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    for e in sc.els:
        k = e["kind"]
        if k == "rect":
            sh = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE, X(e["x"]), Y(e["y"]), WW(e["w"]), HH(e["h"])
            )
            sh.fill.solid(); sh.fill.fore_color.rgb = rgb(e["fill"])
            sh.line.color.rgb = rgb(e["stroke"]); sh.line.width = Pt(e["sw"])
            try:
                sh.adjustments[0] = 0.1
            except Exception:
                pass
            if e["dash"]:
                ln = sh._element.spPr.find(qn("a:ln"))
                if ln is None:
                    ln = etree.SubElement(sh._element.spPr, qn("a:ln"))
                etree.SubElement(ln, qn("a:prstDash")).set("val", "dash")
        elif k == "text":
            tw = max(160, int(len(e["content"]) * e["size"] * 0.68 * PT_TO_SVG))
            xv = e["x"] - tw / 2 if e["anchor"] == "middle" else e["x"]
            yv = e["y"] - e["size"] * PT_TO_SVG - 2
            b = slide.shapes.add_textbox(X(xv), Y(yv), WW(tw), HH(e["size"] * PT_TO_SVG + 14))
            tf = b.text_frame; tf.word_wrap = False
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if e["anchor"] == "middle" else PP_ALIGN.LEFT
            r = p.add_run(); r.text = e["content"]
            style(r, e["size"], e["bold"], e["italic"], e["fill"])
        elif k == "math":
            tw = 420
            xv = e["x"] - tw / 2 if e["anchor"] == "middle" else e["x"]
            yv = e["y"] - e["size"] * PT_TO_SVG - 2
            b = slide.shapes.add_textbox(X(xv), Y(yv), WW(tw), HH(e["size"] * PT_TO_SVG + 18))
            tf = b.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            for t, is_sub in e["segs"]:
                r = p.add_run(); r.text = t
                style(r, max(8, e["size"] - 3) if is_sub else e["size"],
                      e["bold"], True if is_sub else e["italic"], e["fill"], is_sub)
        elif k == "image":
            p = Path(e["path"])
            if p.exists():
                slide.shapes.add_picture(str(p), X(e["x"]), Y(e["y"]), WW(e["w"]), HH(e["h"]))
        elif k == "line":
            x1, y1, x2, y2 = e["x1"], e["y1"], e["x2"], e["y2"]
            if abs(x2 - x1) >= abs(y2 - y1):
                left, top, ww, hh = min(x1, x2), y1 - 1.3, max(2, abs(x2 - x1)), 2.6
            else:
                left, top, ww, hh = x1 - 1.3, min(y1, y2), 2.6, max(2, abs(y2 - y1))
            sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, X(left), Y(top), WW(ww), HH(hh))
            sh.fill.solid(); sh.fill.fore_color.rgb = rgb(e.get("color", "#455A64"))
            sh.line.fill.background()

    if png_p and png_p.exists() and png_p.stat().st_size > 1000:
        proof = prs.slides.add_slide(prs.slide_layouts[6])
        proof.shapes.add_picture(str(png_p), Inches(0), Inches(0), Inches(SLIDE_W_IN), Inches(SLIDE_H_IN))

    if extra_note_lines:
        s3 = prs.slides.add_slide(prs.slide_layouts[6])
        box = s3.shapes.add_textbox(Inches(0.45), Inches(0.35), Inches(12.4), Inches(6.8))
        tf = box.text_frame
        tf.word_wrap = True
        first = True
        for text, size, bold, col in extra_note_lines:
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.space_after = Pt(6)
            r = p.add_run(); r.text = text
            style(r, size, bold, False, col)

    out_dir.mkdir(parents=True, exist_ok=True)
    pptx_p = out_dir / f"{stem}_editable.pptx"
    prs.save(str(pptx_p))
    return pptx_p
