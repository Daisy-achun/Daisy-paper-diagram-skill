---
name: paper-framework-diagram
description: >-
  Draw publication-ready computer-science paper framework, pipeline, system,
  and method figures (论文流程图 / Fig.1 / method diagram). Use for any request to draw,
  redraw, polish, or export such figures. Enforces clear visual grammar: large
  readable type, no text/image overlap, true math subscripts, accurate
  flowchart chips, editable PPTX — not low-quality demos or flattened
  screenshots. Composition follows the Method text; do not force any single
  canned layout. Do not use for decorative infographics or generic slide
  styling without a paper method.
---

# Computer-science paper framework / pipeline diagram

## When to use

Trigger on: computer-science paper figure, 论文流程图, pipeline/architecture/
framework/system/method figure, Fig.1, algorithm flow, system workflow, agent
loop, database query plan, compiler pipeline, network protocol, security
pipeline, distributed workflow, HCI interaction flow, ML/CV training figure,
or polish of an existing paper figure/PPTX. Apply across computer science,
including systems, software engineering, algorithms and theory, databases,
networking, security, distributed computing, HCI, and AI/ML/CV.

Also follow this skill when another architecture-diagram skill is present;
**prefer this skill’s quality gates** if they conflict with demo SVGs.

## Absolute priorities (read first)

1. **Faithful to Method** — no invented modules, losses, datasets, or numbers.
2. **Readable at paper scale** — type hierarchy large; hard floor ≥10pt.
3. **Layout integrity** — no text/image overlap; no text outside boxes.
4. **True math** — `R_task` style ASCII is banned for symbols; use real subscripts.
5. **Editable deliverable** — native PPTX shapes + SVG vector; never “PPTX =
   one pasted PNG” as the master.
6. **Follow this skill’s style packs** (`styles/`) — not random demo SVGs or
   unrelated slide templates.

## Host portability

This is an instruction-only Agent Skill. It must work when loaded by Claude
Code, Codex, or Cursor from any supported skill directory. Use the host's
available filesystem, image, PDF, PowerPoint, and computer-use tools; do not
assume a tool name, GUI application, shell, or image-generation integration.
If a requested capability is unavailable, continue with the best deterministic
fallback and state the limitation in the delivery note. Never claim that a
PPTX, PDF, or raster export was created without checking the file on disk.

The `references/` directory is part of this skill. Resolve links relative to
the directory containing this `SKILL.md`; do not depend on the repository root
or on another skill being installed. The companion skill may be used together
with this one, but this file remains complete on its own.

---

## Style sources (what to follow)

| Source | Use? |
|--------|------|
| Current Method text / equations / module names | **Yes — primary** |
| This skill’s `styles/DESIGN_GRAMMAR.md` + locked look pack | **Yes — visual grammar** |
| User-named style preference or “copy this sketch” | Yes — map to nearest core look |
| Prior good exports **in the same project** | Yes — keep continuity |
| Random GitHub demo SVGs / slide templates | Weak fallback only |
| One-shot AI “concept boards” | Exploration only; **never** final technical figure |

If the user rejects a look, switch packs — do not invent a third grammar.

---

## Why clear method figures look good (shared grammar)

Apply all of these:

1. **Clear type hierarchy** — Fig title ≫ panel title ≫ module title ≫ body.
   Dense 7–8pt walls are banned.
2. **Fewer words, larger size** — shorten labels so type can grow. Prefer
   `go_high` over a sentence inside a card.
3. **Semantic color roles** — assign restrained colors to the paper's actual
   stages, actors, trust boundaries, or data classes. Example mappings are
   defaults only; do not reuse a palette when its meanings do not fit.
4. **One peach/coral hero** — novel module once, stronger stroke; details in
   inset or dashed leader — not peach everywhere.
5. **Concrete visual evidence** — use a real input crop, intermediate
   representation, query/result sample, protocol message, state snapshot, plot,
   or other domain-appropriate artifact when it clarifies the method. Keep
   labels outside images; do not bake technical text into generated assets.
6. **Consistent color roles** across the whole figure (route vs tool vs
   observe / real vs fake / trainable vs frozen).
7. **Sparse 🔥 / ❄ / ⚙** with a single top-right legend.
8. **Concrete examples when they help** — domain paths, sample I/O, or
   short trajectories only if the Method is agentic / multi-step; skip if
   the figure is a pure network rail or loss diagram.
9. **Stages when present** — show the paper's actual phases (such as
   preprocessing/execution, train/deploy, setup/query/measurement, or protocol
   states) as distinct panels when that improves comprehension. Omit phases
   irrelevant to the contribution.
10. **Clean connectors** — solid = data flow; dashed = optional / inset;
    operators (⊕, C) as clear circles.

---

## Typography scale (mandatory)

Layout 里的字号一律按 **印刷磅 pt** 设计（对标 PPT 13.333″ × 7.5″）。  
Canvas ≈ **1400×760–860** SVG user units；**禁止**把同一个数字既当 SVG 像素又当 PPT pt——那会导致 PNG 与 PPT 字号不一致、且 PNG 普遍偏小。

| Role | Size (pt) | Weight |
|------|-----------|--------|
| Fig. title | 17–18 | Bold |
| Panel `(a)(b)` | 14–15 | Bold |
| Module title | 13–14 | Bold |
| Primary body / actions | 11–12 | Reg/Bold |
| Secondary / legend | 10–11 | Regular |
| **Hard floor** | **≥10** | — |

**Same-source 字号换算（强制）：**

```text
SLIDE_W_IN = 13.333
PT_PER_IN  = 72
svg_font_px = pt * (SVG_W / (SLIDE_W_IN * PT_PER_IN))
pptx_font   = Pt(pt)    # 直接用 pt，不要再用 SVG 像素数
```

例：`SVG_W=1480` 时，12pt → SVG ≈ `12 * 1480 / 960 ≈ 18.5` user units；PPTX 仍为 `Pt(12)`。

PPT 文本框：关闭自动缩字（勿用 shrink-on-overflow）；框宽按内容加宽，宁删字不压到 floor 以下。

If it does not fit at ≥10pt: **cut words**, widen the box, or move detail to
an inset — **never** shrink below the floor.

Font: Helvetica / Arial only. Italic for math identifiers.

### Math & subscripts (mandatory)

| Wrong | Right |
|-------|--------|
| `R_task`, `R_route` as plain text | \(R_{\mathrm{task}}\), \(R_{\mathrm{route}}\) |
| `O_G` as `O_G` with underscore | \(O_G\) with true subscript G |
| Formula as one long ASCII string | Multi-line, spaced operators, italic vars |

Implementation:
- **SVG**: `R<tspan baseline-shift="sub" font-size="…">task</tspan>`
- **PPTX**: run with `a:rPr/@baseline="-25000"` (subscript). Provide a
  `txt_math(segments)` helper: list of `(text, is_subscript)`.

**Keep underscores only for code tokens**: `go_high`, `go_low`, JSON keys
like `fake_score`. Never for reward/loss/feature symbols.

Formula box must fully contain every line with padding; wrap between terms
(`+ γ…` on next line), not mid-subscript.

---

## Layout integrity (mandatory)

Hard QA before delivery:

- [ ] **No overlap** — text never intersects chips, icons, images, or other boxes
- [ ] **No overflow** — every label inside its parent with ≥8–10px padding
- [ ] **No truncation** — subtitles fully visible; tool names not clipped by card edge
- [ ] Chip/icon placement: **reserved slot only** (left column / bottom band / top-right
  of card). Never float an icon over a title or body line.
- [ ] Trajectory / sample cards: final lines stay inside; tag chips do not cover body text
- [ ] **White (or near-white) figure background** — avoid large flat gray stage washes
  that make the figure look empty; stage shells use light pastel fills or thin dashed
  borders, not heavy gray slabs
- [ ] **Flowchart readability** — numbered steps (①②③ / Step 1·2·3) with visible
  connectors between them; reader can tell order at a glance
- [ ] **Tool Bank / side panels in-flow** — if tools are only used on some paths,
  draw a call arrow from that path (e.g. `go_low` / `call_tool`) into the Tool Bank;
  do not leave an orphan side column with no “when used” cue
- [ ] **Prefer sparse labels** — cut prose; enlarge type; avoid wall-of-text cards
- [ ] **Tighten empty space** — large vacant regions inside shells are banned; either
  shrink the shell or fill with meaningful modules (not sparse floating cards)
- [ ] Visually inspect densest panels at **100% zoom** after export

If both text and image are needed in one card:

```
┌─ card ─────────────┐
│ [icon]  Title       │  ← icon in left reserved column; title never under icon
│ 1 / 2 / 3 lines     │  ← text-only band
│ → outcome           │
└─────────────────────┘
```

---

## Domain assets and evidence

Add compact visual evidence when it helps explain the method. Examples include:

| Domain | Useful evidence |
|--------|-----------------|
| CV / ML | Input crops, attention maps, masks, embeddings, or output examples |
| Systems / distributed computing | Nodes, queues, traces, placement, or message snippets |
| Databases / data systems | Query plans, schema fragments, indexes, or result samples |
| Compilers / programming languages | Source-to-IR-to-code stages, AST fragments, or type/state transitions |
| Networking / security | Protocol messages, trust boundaries, packet/state transitions, or threat surfaces |
| HCI / interactive systems | User actions, interface states, feedback, or study task flow |
| Algorithms / theory | Compact pseudocode structure, recurrence, invariant, or proof dependency |

Use evidence from the paper or clearly marked illustrative examples. Never
invent empirical results or present synthetic evidence as measured data.
Generated assets may not contain technical text, watermarks, UI chrome, or
decorative material unrelated to the method.

Do **not** invent fake metrics or dataset screenshots that claim to be real
results.

---

## One main skill + packs（不要一风格一 skill）

**主 skill** 只此一份：质量门禁、同源导出、抠图、数学、workflow。  
**风格**用 `styles/` 分包；**禁止**为每个视觉风格复制整份 `SKILL.md`。

两轴必须分开（否则会出现「构图不同、长得一样」）：

| 轴 | 路径 | 含义 |
|----|------|------|
| Composition | `styles/compositions/*` | 盒子怎么摆 |
| Look | `styles/looks/*` | 色板/字体/图标/箭头气质 |

方案 = **1 套 composition + 核心 look**（决策面 **8 个核心**，其余为别名；见  
[`styles/looks/CATALOG.md`](styles/looks/CATALOG.md)）。路由：  
[`styles/router.md`](styles/router.md) 与 [`styles/DESIGN_GRAMMAR.md`](styles/DESIGN_GRAMMAR.md)。  
**按图结构自己选**（模块轨 / 双塔 / Stage / 控制环 / 训练奖励 / 对比 / 基准），大模型信号只是快捷入口；非 LLM 论文同样走结构表，只借语法不借模块名。  
读 Method 后锁定一套、一句话告知，然后绘制；勿列 A/B/C。若 ≥2 个核心同样合适，**主动问用户** 2–3 个选项。落笔可开同族别名 `LOOK.md` 细化。  
风格真源是 `DESIGN_GRAMMAR.md` + 所选 `looks/*/LOOK.md`；Method 文本决定模块与结构。  
画图前把所选 look 的 **Design thinking + Style keywords** 整段注入绘制指令。

Method families（选构图时参考）：system / algorithm / data pipeline /
protocol / learning / hybrid — **按结构归类，不按是否大模型归类**。

---

## Same-source export (mandatory)

SVG、PNG、可编辑 PPTX **必须同源**，禁止「两套手写布局」。

1. 先写 **layout 源**（Python dict / JSON：框、字、图、坐标）。
2. `layout → SVG`（矢量主稿）。
3. `SVG → PNG`（唯一预览栅格）。
4. `layout → PPTX` 原生形状（与 SVG 同一坐标映射）；可另附一页「PNG 校对页」，
   但可编辑主页不得与 PNG 构图分叉。
5. 交付前目视：PNG 与 PPTX 主页结构一致（阶段划分、模块名、公式一致）。

若暂时无法原生复刻全部装饰：PPTX 主页仍须同源 layout；缺失项写进交付说明，
**不要**另画一版更好看的 SVG 却留着旧 PPT。

---

## Deliverables

1. **Vector `.svg`** — layout 导出的矢量主稿  
2. **High-res `.png`** — 仅由该 SVG 栅格化  
3. **Editable `.pptx`** — 同一 layout 的原生形状（可加 PNG 校对页）

Rules:
- Never ship a PPTX whose only content is one flattened screenshot **as the
  sole editable master** without a layout-backed shape page.
- Version before overwriting (`*_editable.pptx` if lock exists).
- Delivery note: caption; style pack chosen; assumptions; same-source OK?

Suggested paths:
`figures/<name>.svg`, `.png`, `_editable.pptx`, `figures/chips/`,
`figures/icons/`, `layout/`, `styles/`.

### Delivery UX（强制）

用户要的是**能直接点开看**的结果，不是让他们自己去找路径。

1. 在最终回复里，对每个交付物给出 **Markdown 可点链接**，使用绝对 `file://` URI  
   （路径含中文/空格时做百分号编码），例如：  
   `[RoT 框架图 PNG](file:///Users/…/rot_framework.png)`  
   `[可编辑 PPTX](file:///Users/…/rot_framework_editable.pptx)`
2. **禁止**只甩相对路径、裸绝对路径、或「文件在 xxx 目录」而不附链接。  
   路径可作为链接显示文字的补充，但不能代替链接。
3. 若宿主支持 `open_resource` / 等价打开能力：交付时**主动打开** PNG（预览）和 PPTX（编辑）。
4. 链接顺序建议：PNG（先看效果）→ PPTX（可编辑）→ SVG（矢量源）。

---

## Anti-patterns (do not ship)

- Equal-weight empty card walls
- **Nested white boxes** inside every pastel column (box-in-box) — put labels
  directly on the stage fill; reserve white only for tiny chips/metrics if needed
- 7–8pt dense paragraphs; unreadably small type
- Text overlapping chips or spilling outside rounded cards
- ASCII math `R_task` / `L_cls` instead of true subscripts
- Rainbow arrows, neon, heavy decorative shadows
- AI concept board as the final technical figure
- Wrong/misplaced GitHub demo grammar when a locked look pack already fits
- Invented modules / numbers not in Method
- PPTX = pasted PNG only
- Inventing a second “alternate style” option when the Method already maps to one scheme
- Smile-face / emoji people as scientific placeholders
- Copying the previous paper’s layout with only labels swapped
- Green-screen / white-box icons pasted into PPTX without 抠图

---

## Style lock (one scheme per Method)

After reading the Method, **lock one**
`composition × 核心 look` via [`styles/router.md`](styles/router.md) /
[`styles/looks/CATALOG.md`](styles/looks/CATALOG.md):

- User named a style or attached “copy this sketch” → map to nearest core look.
- Otherwise → Method 结构信号表的那一套；一句话告知后 **直接绘制**.

**Do not** present A/B/C or wait for a letter. User can override mid-flight by naming another look.

Never reuse the last project’s layout (e.g. agent-loop + Tool Bank + twin
SFT/GRPO cards) just because it is familiar.

---

## Icon & chip generation spec

Placeholders must look like **publication figure assets**, not toy drawings.

### Forbidden
- Stick smile faces / emoji-head “people” as model or data stand-ins
- Flat yellow emoji as human evaluation
- Random stock clutter, watermarks, UI chrome, baked-in technical labels
- Reusing the same peach pastel card wall across unrelated papers

### Preferred evidence chips
- **User-provided** domain crops when available
- Else **generated** domain chips: face/scene crops, attention/ELA maps,
  draft/verify grids, document snippets — photoreal or clean scientific
  illustration; labels stay **outside** the image

### Icons (process / actor glyphs)
When the figure needs icons (model, human annotation, reward, tools):
see full pipeline in [`references/icon-generation.md`](references/icon-generation.md).

1. Style target: clean **2D product illustration** — soft gradient, light
   shadow, readable at 48–96 px (see user `icon_examples` boards when
   provided).
2. One concept per icon; consistent stroke weight and corner radius across
   the set.
3. Palette roles: tech/logic = blue; human/annotation = warm orange/coral;
   success/accept = green; reject/error = red; novel module = one stronger
   accent. **Do not** paint the subject in chroma-key green.
4. **Generate on solid chroma green** (`#00FF00` / `#00B140`) so cutout is
   easy — not white/checker as the master.
5. Naming: raw `icons/_raw/NN_role_green.png` → cutout `icons/NN_role.png`.
6. Generate a small **icon sheet**, visual-QA, reject ugly/off-brief icons.
7. **抠图 mandatory before PPT/SVG insert** — only embed the transparent
   RGBA cutout. Never leave green-screen or white-box mattes on colored cards.
8. No tiny illegible text inside the glyph.

If generation quality is poor, fall back to **typography-first modules**
rather than shipping smile faces or uncut green masters.

---

## Workflow checklist

1. **Collect** Method text (+ optional user style notes); ignore bad demos.
2. **Truth table** — inputs/outputs, stages, components, actors, operations,
   states, objectives/metrics, and the novel contribution.
3. **Style lock** — use [`styles/router.md`](styles/router.md); pick **one**
   composition×核心 look from the Method 结构信号表 (core 8); state in one
   line, then draw.
4. **Compose** from Method + locked `compositions/*/STYLE.md` +
   core or same-family alias `looks/*/LOOK.md` style keywords; ≤1 hero accent
   per look rules.
5. **Layout source** — one Python/JSON scene; do not hand-fork SVG vs PPTX.
6. **Type** with the scale above; shorten copy to keep ≥10pt.
7. **Math** with true subscripts in SVG and PPTX.
8. **Assets** — domain chips and/or icons per [`icon-generation.md`](references/icon-generation.md):
   green-screen generate → **抠图** → transparent PNG; QA on light/dark cards;
   reserved slots only. Do not insert raw green masters into PPTX.
9. **Layout QA** — no overlap / no overflow / no truncation at 100% zoom;
   no green fringe / white box around icons.
10. **Export** layout → SVG → PNG; layout → native PPTX (+ optional PNG proof).
11. **Deliver** caption + assumptions + pack id + same-source OK?
    + note that icons were cut out before insert.
    + **必须**用可点 `file://` Markdown 链接给出 PNG / PPTX / SVG（见 Deliverables → Delivery UX）；
      禁止只给路径让用户自己找；并尽量 `open_resource` 打开预览。

## Implementation hints (Cursor)

- Maintain helpers: `chip()`, `r_sub()` / `math_term()`, `txt_math(segments)`.
- Assert font size ≥10 **pt** in PPTX; SVG must use `svg_pt(pt)=pt*(W/(13.333*72))`.
  Never pass the same raw number as both SVG px and PPT pt.
- Forbid `<!-- ... -->` with `--` inside SVG XML comments (breaks Chrome
  rasterize); prefer no XML comments in the SVG string.
- After layout edits, re-run the **same-source** renderer once — never patch
  only the SVG or only the PPTX by hand.
