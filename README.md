# Daisy Paper Diagram Skill

**把计算机科学论文 Method 画成可投稿的 Fig.1 / 框架流程图** —— 面向
Cursor / Claude Code / Codex 的 [Agent Skill](https://agentskills.io/)。

仓库命名遵循 Daisy 技能规范：`Daisy-<name>-skill`。  
本仓库：**[`Daisy-paper-diagram-skill`](https://github.com/Daisy-achun/Daisy-paper-diagram-skill)**。

---

## 项目介绍

写论文时 Method 往往已经清楚，难的是 Fig.1：既要忠于算法 / 系统结构，又要在双栏版心里一眼可读。这个 Skill 专做这件事——根据 Method、公式与模块关系，自动锁定一套构图与观感，导出可编辑的论文框架图。

它不是通用信息图或演示文稿美化工具，而是面向 **CS 论文方法图** 的绘制规范：

- **忠于 Method**：不臆造模块、损失、数据集或数字  
- **结构选风格**：按图结构从核心 look 中自选；多解时主动询问  
- **排版可读**：字号硬下限 ≥10pt、真下标公式、芯片不挡字  
- **反套娃白框**：禁止 pastel 色带内再嵌一层白底信息卡  
- **同源交付**：同一 layout 导出 SVG + 高分辨率 PNG + 原生可编辑 PPTX  

适用方向包括系统与软件、算法与理论、数据库、网络、安全、分布式、HCI，以及 AI / ML / CV 等方法图。

---

## 生成什么风格的论文流程图

视觉气质定位为 **学术 pastel 方法图**（白底、低饱和分区、细箭头、大字号），而不是海报风或深色霓虹风。

| 维度 | 风格约定 |
|------|----------|
| 画布 | 纯白 / 极浅灰 |
| 容器 | 大圆角矩形；虚线 = 阶段壳；实线 = 可执行模块 |
| 配色 | 低饱和 pastel；一阶段一色（绿 / 蓝 / 橙 / 紫等） |
| 强调 | 通常只留一个桃色 / coral「新颖模块」 |
| 状态 | 🔥 可训 / ❄ 冻结 / ⚙ 适配；图例只出现一次 |
| 证据 | 领域相关的输入 / 中间结果芯片；短标签轨迹 |
| 公式 | 真下标（如 \(L_{clip}\)、\(BA_i\)），奖励框可用虚线 inset |
| 箭头 | 细黑 / 深灰主路径；虚线表示旁路或阶段过渡 |
| 禁止 | 柱内白底套娃、彩虹粗箭、霓虹阴影、把结果大表当框架图 |

### 四种构图（怎么摆盒子）

| Composition | 典型结构 |
|-------------|----------|
| `network-rail` | 左→右模块轨 + 可选右侧 inset |
| `dual-stream` | 双塔 / 双路径汇合，或左右范式对比 |
| `agent-loop` | 决策环 + Tool 浮层 + 轨迹 |
| `two-stage-train` | 两阶段训练 + 样本 / 奖励侧栏 |

### 八种核心观感（长什么样）

| Look | 适合什么样的 Method | 画面长什么样 |
|------|---------------------|--------------|
| `stage-band-pastel` | 明确 Stage 1/2/3 流水线 | 多层彩色虚线色带，带内左→右 |
| `modular-pastel-stack` | 编码器堆、Nx 残差、算子轨 | 功能色圆角块 + 浅灰 Nx 壳 + 残差弯箭 |
| `dual-modality-gradient` | 双塔 / 双模态再汇合 | 左右两路 + ❄/🔥，中部融合 |
| `agent-panel` | Agent + Tool + 轨迹 | 奶油主控壳、Tools 浮层、短轨迹 |
| `rl-grpo-chain` | SFT → 组采样 / 奖励优化 | 样本卡组、奖励公式虚线 inset |
| `paradigm-compare` | 旧范式 vs 新方法 | 左右对比、虚线分隔 |
| `benchmark-dense` | 数据 / 基准**构建**框架 | 构建 + 评测双面板（不是结果表） |
| `method-overview-flat` | 结构暂时说不清时的兜底 | 中央骨干 + 扁平 pastel 模块 |

一篇 Method 只锁定 **1 套** `composition × look`，例如：

- 多阶段检测流水线 → `network-rail` × `stage-band-pastel`  
- Agent + Tool + 轨迹 → `agent-loop` × `agent-panel`  
- 经典网络 / 编译器管线 → `network-rail` × `modular-pastel-stack`  
- SFT → 组相对优化 → `two-stage-train` × `rl-grpo-chain`  

---

## 快速开始

```bash
git clone https://github.com/Daisy-achun/Daisy-paper-diagram-skill.git
cd Daisy-paper-diagram-skill
./scripts/sync-skills.sh
```

### 安装到你的项目

```bash
# Claude Code
./scripts/install-skill.sh --target claude --project /path/to/project

# Codex
./scripts/install-skill.sh --target codex --project /path/to/project

# Cursor
./scripts/install-skill.sh --target cursor --project /path/to/project

# 三个宿主一起
./scripts/install-skill.sh --target all --project /path/to/project
```

安装后在对话里触发：`论文流程图` / `Fig.1` / `framework diagram`，或显式 `/paper-framework-diagram`。

给 Skill 一段 Method（或 PDF / 公式），它会：锁定风格 → 绘制 → 交付可点开的 PNG / PPTX / SVG。

---

## 仓库结构

| 路径 | 说明 |
|------|------|
| `skills/paper-framework-diagram/` | **唯一编辑处**（主 Skill） |
| `.claude/skills` · `.agents/skills` · `.cursor/skills` | 由 sync 生成的宿主镜像 |
| `styles/`（位于 skill 内） | 构图 packs + 8 核心 look + 设计语法 |
| `references/` | 图标抠图、PPT 导出、交付前 QA |

```bash
./scripts/sync-skills.sh
./scripts/validate-skills.sh
```

---

## GitHub About（可直接粘贴）

- **简介：**  
  `学术论文 Fig.1 / 方法流程图 Agent Skill：pastel 色带、模块轨、双塔与 Agent 面板；忠于 Method，可编辑 SVG+PPTX。支持 Cursor / Claude Code / Codex。`
- **Topics：** `agent-skills` · `cursor` · `claude-code` · `codex` · `paper-figures` · `scientific-visualization` · `svg` · `pptx` · `computer-science`

---

## 姊妹仓库（勿混淆）

| 仓库 | Skill 名 | 特色 |
|------|----------|------|
| **本仓** [`Daisy-paper-diagram-skill`](https://github.com/Daisy-achun/Daisy-paper-diagram-skill) | `paper-framework-diagram` | **画图发行版**：多端 install/sync，开箱画 Fig.1 |
| [`Daisy-fig-lookpack-skill`](https://github.com/Daisy-achun/Daisy-fig-lookpack-skill) | `fig-lookpack` | **风格包源**：扁平目录，维护 composition×look |
| [`Daisy-paper-framework-skill`](https://github.com/Daisy-achun/Daisy-paper-framework-skill) | 合集 | 含额外流程技能的历史合集版 |

两套出图门禁一致；按「要装来画」还是「要改风格包」选仓即可。

## 作者

**Daisy**（[@Daisy-achun](https://github.com/Daisy-achun)）

## License

MIT
