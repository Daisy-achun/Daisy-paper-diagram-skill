# 布局粗标签 → 核心 look

Type A/B/C 只是**粗标签**；真正决策面是 CATALOG **8 核心 look**（见 `router.md`）。  
按 Method **按图结构自己选**；出现 **≥2 个合理核心** 时**主动问用户**（2–3 个适配候选），不要等用户说「换风格」，也不要永远二选一。

画之前可先粗分（可组合），再落到 8 核心：

| Type | 何时 | 布局抓手 | 常映射 look（可多解） |
|------|------|----------|-----------|
| **A. Framework overview** | Agent / 推理环+SFT+RL | pastel region cards；奶油壳+Tools+轨迹 | 常 `agent-panel`；若更偏奖励样本卡也可问 `rl-grpo-chain` |
| **B. Network architecture** | 模块、张量、损失、L→R 骨干 | 主轨 + 虚线 zoom inset | 常 `modular-pastel-stack`；多 Stage 可问 `stage-band-pastel` |
| **C. Prompt / contrastive** | Prompt bank、CLIP 头、分布 inset | 外壳 + 上下分带 | `dual-modality-gradient` / `rl-grpo-chain` / `paradigm-compare` |

控制环 + 工具/轨迹：通常 → `agent-loop × agent-panel`（竖向 Policy 主栏）。  
若用户明确要求奶油壳控制面板，跟该偏好；若 Method 同时强依赖 GRPO 样本卡叙事，可**主动问** `agent-panel` vs `rl-grpo-chain`。

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

见 `looks/modular-pastel-stack/LOOK.md`（冰蓝 `#D0E0F0` / 桃色 `#FAD7C5`）。

## QA

- [ ] Type 选对了（Agent ≠ 横条模块轨）
- [ ] Type A 三壳色：cream / blue / lavender 一眼可辨
- [ ] 有轨迹或样本芯片；Tools 在推理壳右侧（或明确 call 箭头）
- [ ] 箭头主色 `#4A6FA5`，非彩虹
