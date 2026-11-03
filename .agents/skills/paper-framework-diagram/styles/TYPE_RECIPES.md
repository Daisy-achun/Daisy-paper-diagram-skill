# Type A / B / C 布局配方

> 恢复自 GitHub `Daisy-paper-framework-skill` @ `55aa806` / `a71b770`（2026-10-31 ~22:00）。  
> Type A/B/C 是**粗标签**；真正决策面是 CATALOG **8 核心 look**（见 `router.md`）。  
> AI 按 Method **自选**；多解时**主动问**适配候选——不是等用户说换风格，也不是永远二选一。

画之前可先粗分（可组合），再落到 8 核心：

| Type | 何时 | 布局抓手 | 常映射 look（可多解） |
|------|------|----------|-----------|
| **A. Framework overview** | Agent / 推理环+SFT+RL | pastel region cards；奶油壳+Tools+轨迹 | 常 `agent-panel`；若更偏奖励样本卡也可问 `rl-grpo-chain` |
| **B. Network architecture** | 模块、张量、损失、L→R 骨干 | 主轨 + 虚线 zoom inset | 常 `morandi-pipeline`；多 Stage 可问 `stage-band-pastel` |
| **C. Prompt / contrastive** | Prompt bank、CLIP 头、分布 inset | 外壳 + 上下分带 | `dual-modality-gradient` / `rl-grpo-chain` / `paradigm-compare` |

**Band-Routing / Tool-Aware / RoT**：结构上通常 → `agent-loop × agent-panel`（金标准竖 Policy）。  
若用户附图已是奶油壳，跟附图；若 Method 同时强依赖 GRPO 样本卡叙事，可**主动问** `agent-panel` vs `rl-grpo-chain`。

## Type A 硬色板

| Role | Fill | Stroke |
|------|------|--------|
| Vision / processing | `#D6E6F5` | `#5B7A9D` |
| Text / language | `#D9E8F8` | `#5B7A9D` |
| Novel / Policy / head | `#F7D6C8` / `#FAD7C5` | `#C48B6A` |
| Real / positive | `#D8F0D8` | `#5A9A5A` |
| **Region cream（推理壳）** | `#FFF6E0` | `#E0D2B8` |
| **Region blue（SFT / Tools）** | `#EAF2FB` | `#A8BFD4` |
| **Region lavender（RL/GRPO）** | `#F0EAF8` | `#D0C4E0` |
| Region mint | `#E7F2E9` | muted |
| Canvas | `#FFFFFF` | — |
| Main arrows | `#4A6FA5` | — |

## Type A 结构（必须对齐）

```
┌─ cream #FFF6E0 Inference ─────────────────────────────────┬─ blue Tools ❄ ─┐
│ Input → candidates → peach Policy (Route/Call/Observe)     │ T1..T4 cards     │
│ Example trajectories (numbered 1/2/3 + chips)              │ Step B call/fuse │
│ Answer path log JSON                                       │                  │
└────────────────────────────────────────────────────────────┴──────────────────┘
┌─ blue #EAF2FB SFT ──────────────┐  ┌─ lavender #F0EAF8 GRPO ─────────────────┐
│ prefer cards + Route→Call→Ans   │  │ O1/O2/OG + peach R=… + reward chips     │
└─────────────────────────────────┘  └─────────────────────────────────────────┘
```

## Type B 结构

见 `looks/morandi-pipeline/LOOK.md`（冰蓝 `#D0E0F0` / 桃色 `#FAD7C5`）。

## QA

- [ ] Type 选对了（Agent ≠ 莫兰迪横条）  
- [ ] Type A 三壳色：cream / blue / lavender 一眼可辨  
- [ ] 有轨迹或样本芯片；Tools 在推理壳右侧（或明确 call 箭头）  
- [ ] 箭头主色 `#4A6FA5`，非彩虹  
