# Look: `rl-grpo-chain`


## One-line vibe

组采样卡片 o1…oG 为主视觉；奖励公式放大；SFT 短条 + RL 主舞台；token 色块；虚线策略回环。

## Design thinking

```text
Left: generation / rollout through the model with token squares. Center-right: group
of answer cards o1..oG as the largest visual mass. Far right or inset: reward
terms and group-relative update with dashed loop back to the policy. Keep SFT as a
thin warm-start strip only. Optional: coral/lavender minimal token style OR peach
model block + frozen reward snowflake OR pastel training band inside a larger figure.
左生成/rollout+token方块；中右把o1…oG组卡片画最大；奖励虚线回环；
SFT只留短条；可选极简珊瑚token风或peach模型块+❄奖励模型。
```

## Prompt keywords

```text
GRPO RL training figure, group sampling cards o1..oG hero, reward formula dashed inset,
SFT warm-start strip then RL stage, peach or coral MLLM block, lavender prompt tokens,
frozen reward model snowflake, policy dashed loop, entropy branch optional,
flat academic white background sparse shadows
组采样卡片主视觉, 奖励公式, SFT短条+RL, token色块, 虚线回环, ❄奖励模型
```

## Palette

| Role | Fill | Stroke |
|------|------|--------|
| Sample / rollout | `#E3F2FD` / coral `#F28E82` tokens | `#64B5F6` |
| Bad / reject | `#FFEBEE` | `#E57373` |
| Incentive | `#C8E6C9` | `#66A86A` |
| MLLM / policy | `#FDEBD0` peach | `#E0A060` |
| RL shell | `#F3E5F5` / `#FFF3E0` | `#9575CD` |

## Forbidden

- 只有双塔 CLIP 无采样组  
- 把 AUC 曲线当 GRPO 图
