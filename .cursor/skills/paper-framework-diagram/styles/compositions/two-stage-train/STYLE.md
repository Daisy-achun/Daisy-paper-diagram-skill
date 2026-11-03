# Composition: `two-stage-train`

**轴：构图 only。** 默认观感 `looks/rl-grpo-chain`（样本卡主视觉时可开别名 `sample-card-reward`）；或 `stage-band-pastel`。

## Composition

```
┌─ Stage 1 Warm-Start (top band) ─────────────────────────────┐
│ sample cards → Base → Inject → Initial Policy               │
│              → prefer/reject align → Cold / warm policy     │
└─────────────────────────────────────────────────────────────┘
┌─ Stage 2 Group RL (bottom band) ────────────────────────────┐
│ online o1…oG → Group → Incentivize → Final policy           │
│                         ↘ dashed Reward panel (right)       │
└─────────────────────────────────────────────────────────────┘
```

## Visual grammar

- Soft gray stage shells；训练步用 **mint green**；策略/结果用 **warm peach**；样本卡用 **dashed** 边框。
- 领域相关证据 chip；模型与人用 **2D 产品插画图标**（见 `references/icon-generation.md`）。
- 短标签轨迹；✓ / ✗；🔥 标可训；不要笑脸 emoji 人。

## Forbidden

- 无控制环需求时硬套 Agent + Tool Bank
- 整页同一 peach 卡片墙、无样本/奖励叙事
- PPT 与 PNG 两套不同构图
