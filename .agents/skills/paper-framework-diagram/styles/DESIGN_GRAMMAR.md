# 方法图共享设计语法

画任意 Method 时：先读本文件，再按 `CATALOG.md`「结构优先」锁定 look，套用对应 **设计思路 + 风格关键词**；**Method 文本优先；用户明确的风格偏好次之**。

---

## 0. 共享语法（默认遵守）

| 维度 | 规律 |
|------|------|
| 背景 | 纯白或极浅灰；**不用**深色底、紫光晕、渐变大海报 |
| 容器 | 大圆角矩形；**虚线描边** = 阶段壳 / 逻辑分组；**实线** = 可执行模块 |
| 色板 | 低饱和 pastel；一阶段一色（绿/蓝/橙/紫）；同一语义跨图一致 |
| 状态符号 | 🔥 可训 / ❄ 冻结 / ⚙ 适配；**右上角或图例虚线框只出现一次** |
| 证据 | 领域相关的输入/中间结果缩略图；短轨迹标签；✓✗；token 色块（若 Method 需要） |
| 公式 | 真下标 \(L_{clip}, o_G\)；奖励框用虚线大 inset，不挤进正文箭头 |
| 箭头 | 细黑/深灰实线主路径；虚线 = 旁路、反馈、阶段过渡；少用粗彩箭头 |
| 字号 | 模块名最大；壳标题次之；snippet ≥10pt 等效；宁删字不缩小 |
| 禁止 | 把结果表/词云当框架；编造 Method 没有的模块；绿幕未抠图图标 |

**设计思路总关键词（任何 Method 先过一遍）：**

```text
publication-ready CS method figure, white canvas, pastel semantic color roles,
rounded modules, dashed stage shells vs solid operator boxes,
one legend for fire/snowflake/adapter, concrete I/O evidence chips,
true math subscripts, sparse clean arrows, no text overlap, readable ≥10pt,
faithful to the user's Method only
白底pastel分区, 虚线阶段壳+实线模块, 状态图例一次,
真实样本证据, 真下标公式, 只画当前 Method
```

---

## 1. 结构簇 → 风格关键词

### A. 控制环 / 工具 / 轨迹面板

**设计思路：** 先画「运行时决策环」，再挂「训练底栏」（若有）；轨迹要有真实证据 + 短标签，不能只画空环。

**风格关键词 → look `agent-panel` / `dual-agent-split`：**

```text
cream-yellow agent main panel, soft drop shadow cards, blue dashed Think-Call-Observe loop,
floating Tools UI panel, trajectory timeline with colored tags,
photo or domain evidence crops, pastel blue SFT + lavender RL footers when present,
sticker-flat icons after green-screen matting, JSON final answer chip
淡黄控制主面板, Tools浮层, 轨迹时间线, 可选蓝紫训练底栏, 双轨Agent+细节下探
```

---

### B. 两阶段训练 + 样本卡 + 奖励侧栏

**设计思路：** 样本与奖励是主视觉，模型图标是配角；Stage 用灰壳分隔，不要糊成一块。

**风格关键词 → `sample-card-reward` / `stage-band-pastel`：**

```text
two-tier training pipeline, gray stage shells, sample chips with short tags,
green check red cross preference cards, product-style icons matted,
mint train pills with fire, dashed green reward sidebar with formula hero,
soft peach warm-start band, KL dashed to frozen reference when present
两阶段训练, 样本轨迹卡, ✓✗, 奖励虚线侧栏
```

---

### C. 组采样 / 相对策略优化主视觉

**设计思路：** 把「一组回答卡片」画大；奖励公式单独成框；监督预热只占短条。

**风格关键词 → `rl-grpo-chain`：**

```text
group sampling cards o1..oG as hero, reward formula in dashed inset,
SFT warm-start strip then RL stage, frozen reward model snowflake,
peach model block, coral or lavender token squares, entropy branch optional,
policy dashed loop back to model
组采样卡片主视觉, 奖励公式放大, SFT短条+RL主舞台, token色块, 虚线回环
```

---

### D. 冻结双塔 / 对比 / 适配轨

**设计思路：** 模态颜色锁死（Vision 暖 / Text 冷，或按 Method 自定两色）；冻结与可训必须图例化；对比损失画在两塔之间。

**风格关键词 → `dual-modality-gradient` / `frozen-encoder-rail` / `encoder-lora-rail`：**

```text
dual-stream figure, cool tower snowflake, warm tower adapter fire,
vertical encoder bars, contrastive loss dashed bridge, classification head oval,
panel (a)(b)(c) optional, shallow-deep dashed split, pastel fills no heavy shadow
双塔, ❄一侧🔥适配另一侧, 竖条编码器, 对比损失桥, 浅层深层虚线分隔
```

---

### E. 模块堆叠 / 网络轨 / 残差

**设计思路：** 同类算子同色；重复层用 Nx 外壳；细节放右侧 inset，主轨保持疏。

**风格关键词 → `modular-pastel-stack` / `method-overview-flat`：**

```text
modular pastel architecture, rounded operator blocks thin black stroke,
Nx gray stack shell, residual curved skip arrows, circled plus ops,
optional right dashed inset zoom, isometric CNN blocks only if Method is CNN,
bottom-up or left-right rail, white background
pastel功能色模块, Nx灰壳, 残差弯箭, 右侧虚线inset, CNN才用等距方块
```

---

### F. 多 Stage 虚线色壳（流水线总览）

**设计思路：** 阶段色 = 壳色 = 标题色；内部模块浅一号；过渡用宽箭头或 `>>>`。

**风格关键词 → `sidebar-stage` / `stage-band-pastel` / `benchmark-dense`：**

```text
multi-stage pipeline, thick dashed colored stage shells green blue orange,
wide soft transition arrows, nested rounded cards, optional model logo wall,
metric tiles only if Method is a construction framework, flat academic vector
多阶段彩色虚线壳, 宽过渡箭, 嵌套圆角卡, 可选logo墙与指标砖
```

---

### G. 检索增强 / 分步推理 / 范式对比

**设计思路：** 证据与推理文字用**同色高亮**绑定；对比基线时用竖虚线对开。

**风格关键词 → `retrieval-augment` / `paradigm-compare`：**

```text
retrieval-augmented pipeline, cylinder database icon, top-k evidence with boxes,
vertical model pillar, numbered reasoning steps, color-linked highlights,
side-by-side paradigm compare with dashed divider, action chips
检索证据墙, 竖直模型柱, 分步推理, 同色高亮绑定, 左右范式对比
```

---

### H. Prompt 模块网格 / 聊天式单元

**风格关键词 → `compact-column`：**

```text
dashed module grid P1..Pn, chat-turn cards System User Assistant,
payload pills, ROI thumbnail strip, fusion summary beige card, monospaced snippets
虚线模块网格, 对话回合卡, ROI底栏, Fusion汇总
```

---

## 2. Method 信号 → 选包（画图前 10 秒）

**先按图结构锁定**（完整表：`looks/CATALOG.md`「结构优先」）。领域时髦词只是快捷入口；别名仅落笔细化。

| 若 Method **结构**是… | 锁定核心 look | 配 composition |
|----------------------|---------------|----------------|
| L→R 模块 / Nx / 管线 | `modular-pastel-stack` | `network-rail` |
| 双路汇合 | `dual-modality-gradient` | `dual-stream` |
| 多 Stage 色带 | `stage-band-pastel` | `network-rail` |
| 控制环 + 工具/API | `agent-panel` | `agent-loop` |
| 监督→RL / 组奖励（无控制环） | `rl-grpo-chain` | `two-stage-train` |
| a vs b 对比 | `paradigm-compare` | `dual-stream` |
| 基准构建双面板 | `benchmark-dense` | `dual-stream` |
| 说不清 | `method-overview-flat` | `network-rail` |

快捷词（Agent / GRPO / CLIP / RAG…）命中且与结构一致时，结果同上。  
非 LLM：**禁止**无中生有 Think-Call-Obs、Tool Bank、适配器火焰、无关人脸样本。

**硬规则：** 一篇 Method **只出一套**；结构优先于领域时髦词。

---

## 3. 生成时自检清单

1. 色角色是否全程一致？  
2. 🔥❄ 是否只在图例定义一次？  
3. 有没有真实 I/O 证据（图/视频条/标签）？  
4. 虚线壳 vs 实线盒是否分工清楚？  
5. 字是否可读、有无叠字出框？  
6. 模块是否都能在 Method 里找到出处？
