# Render scaffold（让远端 Agent 也能画出本地级 Fig.1）

本目录是 **可运行的同源导出脚手架**。Skill 正文只定规范；**真正接近本仓库金标效果**，必须用 Python `Scene` 布局 → SVG → PNG → 原生 PPTX，并做 PNG 视觉质检。

## Agent 强制用法

1. 复制本目录到用户项目（或 `import` 相对路径）：
   - `scene_export.py` — 通用 Scene / `to_svg` / `export_svg_png` / `export_pptx`
2. 按锁定的 look **新建** `render_<paper>.py`（可从 `templates/` 拷贝最近似模板改 Method 标签）。
3. 运行：`python render_<paper>.py`
4. **打开 PNG**（或用读图工具）检查重叠 / 白框套娃 / 字号 / 溢出；不过关就改 layout 再跑。
5. 禁止：Mermaid / draw.io 截图 / 单次 AI 概念图 作为终稿。

## 模板

| 模板 | 对应 look | 何时用 |
|------|-----------|--------|
| `templates/agent_panel_minimal.py` | `agent-loop` × `agent-panel` | Agent / 工具环 / 轨迹 |
| `templates/stage_band_minimal.py` | `network-rail` × `stage-band-pastel` | 多 Stage 色带流水线 |
| `templates/modular_rail_minimal.py` | `network-rail` × `modular-pastel-stack` | L→R 模块轨 |

模板是 **几何与配色骨架**，模块名必须换成当前 Method；不要原样交作业。

## 依赖

```bash
pip install python-pptx pillow lxml
# PNG 栅格化：macOS 用 Chrome headless（脚本已写好路径）
# 或: brew install librsvg  → rsvg-convert
```

## 画布约定

- 逻辑画布 **1480×860** px → PPT **13.333″×7.5″**
- 字号：`svg_pt(pt) = pt * 1480 / (13.333*72)`；PPTX 用 `Pt(pt)`；**禁止**同一数字当 SVG px 又当 PPT pt
- 硬下限 ≥10pt；pastel 色带上直接写字，**禁止**柱内再套白底信息卡
