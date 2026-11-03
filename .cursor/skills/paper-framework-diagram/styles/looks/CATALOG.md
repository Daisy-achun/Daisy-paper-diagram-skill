# Look catalog

**必读：** [`../DESIGN_GRAMMAR.md`](../DESIGN_GRAMMAR.md)（共享语法 + 设计思路/风格提示词）  
**附图：** 仅使用**用户当次**提供的图；仓库不附第三方 Fig 裁切（见 `../refs_real/README.md`）。

> **先看图结构，再看领域词。** 非 LLM 论文走「结构优先」表；模型相关信号只是快捷入口。

---

## 决策面：只认核心 8

Agent **每篇 Method 只锁定 1 套** `composition × 核心 look`。  
近义 look 降为**别名**：落笔时可打开同族别名 `LOOK.md` 取细节。

| 核心 id | 一句话 | 同族别名（落笔细化） | 抓手 |
|---------|--------|----------------------|------|
| `agent-panel` | 控制壳 + Tools 浮层 + 轨迹 | `dual-agent-split`, `retrieval-augment` | cream panel, Think-Call-Obs, Tools float |
| `rl-grpo-chain` | 组采样 / 奖励公式 / 样本奖励 | `sample-card-reward` | group cards, reward loop |
| `stage-band-pastel` | 多 Stage 色带壳 | `sidebar-stage`, `curriculum-stack`, `stage-band` | tiered stages, dashed shells |
| `dual-modality-gradient` | 双塔汇合 + ❄/🔥 | `frozen-encoder-rail`, `encoder-lora-rail` | two-stream merge |
| `modular-pastel-stack` | 功能色模块 + Nx / 残差 | `method-overview-flat`, `compact-column` | pastel ops, backbone |
| `paradigm-compare` | 左右/多范式对比 | — | dashed divider, a vs b |
| `benchmark-dense` | 构建&评测双面板 | — | nested QC（确认真是框架） |
| `method-overview-flat` | 中央骨干兜底 | `taxonomy-infographic`（仅真 taxonomy） | central hub, flat pastel |

可用 composition：`agent-loop` · `dual-stream` · `network-rail` · `two-stage-train`。  
各 look 细则：`styles/looks/<id>/LOOK.md`。

---

## 使用顺序

1. 读 Method → 先归类 **图结构**，再看是否命中快捷信号  
2. **锁定 1 套** composition × 核心 look  
3. 一句话告知 → 打开 `LOOK.md` 注入提示词 → 绿幕抠图 → 绘制  
4. **不要**列 A/B/C  

证据芯片按领域换（见 `SKILL.md` Domain evidence）。

---

## Method → 推荐组合

### 1. 结构优先（领域无关 · 主表）

| 图结构（Method 长什么样） | 锁定组合 | 典型方向举例 |
|---------------------------|---------|--------------|
| L→R 模块轨、编码器堆、Nx 残差块 | `network-rail` × `modular-pastel-stack` | 编译器管线、经典网络、微服务链路 |
| 两路并行再汇合 | `dual-stream` × `dual-modality-gradient` | 双模态、控制-感知、在线-离线 |
| 明确 Stage1/2/3 色带 | `network-rail` × `stage-band-pastel` | 多阶段系统、课程学习、分治协议 |
| 控制环 + 工具/API/检索/执行器 | `agent-loop` × `agent-panel` | Agent、DB playbook、机器人 skill 环 |
| 监督微调 → 强化学习 / 组采样奖励 | `two-stage-train` × `rl-grpo-chain` | RLHF、组相对优化；也含非 LLM policy |
| 左基线 vs 右本文 / 多范式对比 | `dual-stream` × `paradigm-compare` | 旧协议 vs 新协议 |
| 数据集/基准**构建**框架（非结果表） | `dual-stream` × `benchmark-dense` | generation+evaluation 面板 |
| 结构暂时说不清 | `network-rail` × `method-overview-flat` | 先画骨干；**禁止**默认塞 Agent/GRPO |

### 2. 快捷信号（命中且与结构吻合时）

| 快捷信号 | 锁定组合 |
|----------|---------|
| Agent+Tool+轨迹 | `agent-loop` × `agent-panel` |
| SFT→组奖励（无控制环） | `two-stage-train` × `rl-grpo-chain` |
| 对比/双塔/适配 | `dual-stream` × `dual-modality-gradient` |
| 纯模块/Transformer | `network-rail` × `modular-pastel-stack` |
| 多 Stage 流水线 | `network-rail` × `stage-band-pastel` |
| RAG/证据推理 | `agent-loop` × `agent-panel`（落笔可开 `retrieval-augment`） |
| 范式对比 | `dual-stream` × `paradigm-compare` |
| 基准构建框架 | `dual-stream` × `benchmark-dense` |

双 Agent → 别名 `dual-agent-split`；样本卡主视觉 → `sample-card-reward`——**对外仍报核心 id**。

多信号时：先定结构 composition；有 Tool/轨迹仍用 `agent-loop`×`agent-panel`（底栏可画短训练条）。

---

## 质量门

- 学 `DESIGN_GRAMMAR.md` / `LOOK.md` 的**语法**；模块名必须来自**当前** Method。  
- 非 LLM 图：**禁止**无中生有 Think-Call-Obs、Tool Bank、无关人脸样本。  
- 决策面保持 **≤8 核心**；一篇 Method = 一套组合。  
- 用户附图若存在，优先映射到最近核心。
