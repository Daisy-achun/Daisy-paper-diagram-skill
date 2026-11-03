# Style router（构图 × 观感）

先读 [`DESIGN_GRAMMAR.md`](DESIGN_GRAMMAR.md) 与 [`looks/CATALOG.md`](looks/CATALOG.md)。

读完 Method / 用户附图后，**锁定 1 套** `composition + 核心 look`，简述后直接绘制。  
**路由顺序：图结构 → 快捷信号（可选）→ 用户指定。**

## 构图 packs（`compositions/`）

| Pack | 骨架 | 用法 |
|------|------|------|
| `network-rail` | L→R 模块轨 + 右侧 inset | 默认骨干；多 Stage 时配 `stage-band-pastel` |
| `dual-stream` | 上下/左右双塔汇合 | 双路径、范式对比、基准双面板 |
| `agent-loop` | 控制环 + Tool 浮层 + 轨迹 | 任意「决策→调用→观察」环 |
| `two-stage-train` | 两阶段训练 + 样本/奖励侧栏 | 监督→强化学习叙事 |

## 观感 packs（核心 8）

| 核心 | 何时用 |
|------|--------|
| `modular-pastel-stack` | 模块轨、Nx（**非 LLM 默认常客**） |
| `stage-band-pastel` | 多 Stage 色带 |
| `dual-modality-gradient` | 双塔汇合 |
| `paradigm-compare` | a vs b |
| `agent-panel` | 控制环 / 工具 / 轨迹 / RAG |
| `rl-grpo-chain` | 组采样、奖励公式（无控制环时） |
| `benchmark-dense` | 基准构建（非结果表） |
| `method-overview-flat` | 结构不清时的兜底 |

## 输出格式（必须）

```text
选用风格：compositions/<x> + looks/<core-y>
— 结构：…；设计思路：…；参考：用户附图或 LOOK.md 关键词
（开始绘制；若要换风格请直接说。）
```

**不要**再列 A/B/C。
