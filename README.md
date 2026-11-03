# Daisy Paper Framework Diagram Skill

**把计算机科学论文 Method 画成可投稿的 Fig.1** —— 面向 Cursor / Claude Code / Codex 的
[Agent Skill](https://agentskills.io/)。

从 Method、算法/系统描述、公式和用户附图出发，生成技术语义准确、适合双栏排版的
framework / pipeline / architecture / system 图。覆盖系统与软件、算法与理论、
数据库、网络、安全、分布式、HCI、AI/ML/CV 等方向。

> 本仓库是 **`paper-framework-diagram` 单技能**独立发行版（质量门槛 + 构图/风格路由）。
> 若需要「端到端画图流程」姊妹技能，见
> [`Daisy-paper-framework-skill`](https://github.com/Daisy-achun/Daisy-paper-framework-skill)。

### 这个 Skill 做什么

| 能力 | 说明 |
|------|------|
| **忠于 Method** | 不臆造模块、损失、数据集或数字 |
| **结构选风格** | 按图结构从核心 look 自选；多解时主动问你 |
| **排版可读** | 字号硬下限 ≥10pt、真下标公式、芯片不挡字 |
| **反套娃白框** | 禁止 pastel 柱内再嵌白底信息卡；字直接落在色带上 |
| **可编辑交付** | 同源 SVG + 高分辨率 PNG + **原生可编辑 PPTX** |

### GitHub About（可直接粘贴）

- **Description：**  
  `Agent Skill: publication-ready CS paper Fig.1 / framework / pipeline diagrams. Method-faithful, style looks from structure, no nested white boxes, editable SVG+PPTX. Cursor / Claude Code / Codex.`
- **Topics：** `agent-skills` · `cursor` · `claude-code` · `codex` · `paper-figures` · `scientific-visualization` · `svg` · `pptx` · `computer-science`

## 一份技能，多端安装

| 层 | 说明 |
|---|---|
| `skills/paper-framework-diagram/` | **唯一编辑处** |
| `.claude/skills` · `.agents/skills` · `.cursor/skills` | 由 sync 生成的宿主镜像 |

```bash
./scripts/sync-skills.sh
./scripts/validate-skills.sh
```

## 快速安装

```bash
git clone https://github.com/Daisy-achun/Daisy-paper-framework-diagram-skill.git
cd Daisy-paper-framework-diagram-skill
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

安装后在对话里触发：`论文流程图` / `Fig.1` / `framework diagram`，或显式
`/paper-framework-diagram`。

## 作者

**Daisy**（[@Daisy-achun](https://github.com/Daisy-achun)）

## License

MIT
