#!/usr/bin/env python3
"""Smoke-test paper-framework-diagram skill packs + routing + gold agent-panel render.

Run from repo root:
  .venv/bin/python .cursor/skills/paper-framework-diagram/scripts/smoke_test_skill.py
Optional: --render to re-export gold Band-Routing figure.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # skill dir
REPO = ROOT.parents[2] if (ROOT.parents[2] / "scripts").exists() else Path.cwd()
# skill at .cursor/skills/paper-framework-diagram → repo is parents[2]
for cand in [Path.cwd(), ROOT.parents[2], ROOT.parents[3]]:
    if (cand / "scripts" / "render_tool_aware_framework_fig.py").exists():
        REPO = cand
        break

CORES = [
    "agent-panel",
    "morandi-pipeline",
    "rl-grpo-chain",
    "stage-band-pastel",
    "dual-modality-gradient",
    "paradigm-compare",
    "benchmark-dense",
    "method-overview-flat",
]
COMPS = ["agent-loop", "dual-stream", "network-rail", "two-stage-train"]


def audit_docs() -> list[str]:
    errs: list[str] = []
    for c in CORES:
        p = ROOT / "styles" / "looks" / c / "LOOK.md"
        if not p.exists():
            errs.append(f"missing LOOK {c}")
            continue
        t = p.read_text(encoding="utf-8")
        if "## Palette" not in t and "Palette" not in t:
            errs.append(f"{c}: missing Palette section")
        if not re.search(r"#[0-9A-Fa-f]{6}", t):
            errs.append(f"{c}: no hex colors in LOOK.md")
    for c in COMPS:
        if not (ROOT / "styles" / "compositions" / c / "STYLE.md").exists():
            errs.append(f"missing composition {c}")

    for need in [
        "SKILL.md",
        "styles/router.md",
        "styles/looks/CATALOG.md",
        "styles/TYPE_RECIPES.md",
        "reference-qa.md",
    ]:
        if not (ROOT / need).exists():
            errs.append(f"missing {need}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    router = (ROOT / "styles" / "router.md").read_text(encoding="utf-8")
    catalog = (ROOT / "styles" / "looks" / "CATALOG.md").read_text(encoding="utf-8")
    qa = (ROOT / "reference-qa.md").read_text(encoding="utf-8")

    for name, text, needles in [
        ("SKILL.md", skill, ["按图结构自己选", "主动问用户", "8 个核心"]),
        ("router.md", router, ["唯一命中", "主动问", "≥2 个合理核心"]),
        ("CATALOG.md", catalog, ["AI 按 Method 结构自选", "主动问"]),
        ("reference-qa.md", qa, ["Style routing", "8 cores", "主动问"]),
    ]:
        for n in needles:
            if n not in text:
                errs.append(f"{name} missing {n!r}")

    for c in CORES:
        if c not in router or c not in catalog:
            errs.append(f"core {c} not listed in router/catalog")

    # anti-residue (ignore ROLLBACK)
    bad = [
        r"不要列 A/B/C",
        r"用户要换风格时必须",
    ]
    for p in ROOT.rglob("*.md"):
        if "ROLLBACK" in p.name:
            continue
        t = p.read_text(encoding="utf-8")
        for pat in bad:
            if re.search(pat, t):
                errs.append(f"BAD UX in {p.relative_to(ROOT)}: {pat}")
    return errs


def simulate_routing() -> list[str]:
    """Structure → expected look; multi-hit should ask."""
    errs: list[str] = []
    catalog = (ROOT / "styles" / "looks" / "CATALOG.md").read_text(encoding="utf-8")

    cases = [
        ("控制环 + 工具", "agent-panel", True),
        ("L→R 模块轨", "morandi-pipeline", True),
        ("监督微调 → 强化学习", "rl-grpo-chain", True),
        ("明确 Stage1/2/3", "stage-band-pastel", True),
        ("两路并行再汇合", "dual-modality-gradient", True),
        ("左基线 vs 右本文", "paradigm-compare", True),
        ("数据集/基准**构建**", "benchmark-dense", True),
    ]
    for label, look, must in cases:
        if must and look not in catalog:
            errs.append(f"routing table missing look {look}")
        if label.split()[0] not in catalog and label not in catalog:
            # soft: structure keywords should appear in CATALOG structure table
            if not any(k in catalog for k in label.replace("**", "").split(" + ")):
                errs.append(f"catalog may miss structure cue for {label}")

    # multi-hit policy present
    if "多信号" not in catalog and "多解" not in (ROOT / "styles" / "router.md").read_text(encoding="utf-8"):
        errs.append("no multi-hit / 多解 policy documented")
    return errs


def qa_gold_png(png: Path) -> list[str]:
    errs: list[str] = []
    try:
        from PIL import Image
    except ImportError:
        return ["PIL missing"]
    if not png.exists() or png.stat().st_size < 50_000:
        return [f"png missing/small: {png}"]
    im = Image.open(png)
    W, H = im.size

    def px(x, y):
        return im.getpixel((int(x * W / 1400), int(y * H / 800)))[:3]

    def near(rgb, target, tol=30):
        return all(abs(a - b) <= tol for a, b in zip(rgb, target))

    cream = px(80, 60)
    policy = px(300, 200)
    if not near(cream, (255, 248, 236)):
        errs.append(f"cream shell off: {cream}")
    if not near(policy, (247, 214, 200)):
        errs.append(f"policy peach off: {policy}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--render", action="store_true", help="re-run gold Band-Routing export")
    args = ap.parse_args()

    errs = audit_docs() + simulate_routing()

    gold_py = REPO / "scripts" / "render_tool_aware_framework_fig.py"
    png = REPO / "figures" / "tool_aware_vlm_grpo_framework.png"
    svg = REPO / "figures" / "tool_aware_vlm_grpo_framework.svg"
    pptx = REPO / "figures" / "tool_aware_vlm_grpo_framework_editable.pptx"

    if args.render:
        if not gold_py.exists():
            errs.append(f"gold script missing: {gold_py}")
        else:
            r = subprocess.run([sys.executable, str(gold_py)], cwd=str(REPO), capture_output=True, text=True)
            print(r.stdout)
            if r.returncode != 0:
                errs.append(f"render failed: {r.stderr[-500:]}")

    for p in (png, svg, pptx):
        if not p.exists():
            errs.append(f"deliverable missing: {p}")
        elif p.stat().st_size < 1000:
            errs.append(f"deliverable too small: {p}")

    if svg.exists():
        t = svg.read_text(encoding="utf-8")
        for n in ["#FFF8EC", "#F7D6C8", "#EAF2FB", "#F0EAF8", 'baseline-shift="sub"', "Policy Agent", "Tool Bank"]:
            if n not in t:
                errs.append(f"svg missing {n}")
        if 'height="342"' not in t:
            errs.append("svg missing tall Policy column (height=342)")

    errs.extend(qa_gold_png(png))

    print("=== paper-framework-diagram smoke test ===")
    print("skill", ROOT)
    print("repo ", REPO)
    if errs:
        print("FAIL", len(errs))
        for e in errs:
            print(" -", e)
        return 1
    print("PASS")
    print("gold PNG", png, png.stat().st_size if png.exists() else 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
