# Look: `sample-card-reward`

## One-line vibe

样本轨迹卡为主：证据条 + `<tag>`；✓/✗；产品风图标；灰/桃/薄荷绿分区；虚线奖励侧栏放大公式。

## Design thinking

```text
Split the canvas into Stage-1 (warm start / SFT) and Stage-2 (group RL) with soft
gray shells. Make sample cards the densest region: domain evidence chips,
XML-like tags, check/cross. Park reward formulas in a large dashed sidebar —
do not bury math in arrows. Model icons are product renders after matting;
mint pills with fire mark train steps. Optional side strip with semantic colors.
画布上下两Stage灰壳；样本卡+标签+✓✗成最密区域；奖励公式放大进虚线侧栏；
产品风图标抠图；薄荷绿训练胶囊带火；可选侧条语义色。
```

## Style keywords

```text
two-stage training figure, sample trajectory cards with evidence chips,
XML tags thought reasoning answer, green check red cross,
product icons matted, mint train steps with fire, peach preference panel,
dashed reward sidebar formula hero, gray stage shells, monospace snippets,
KL dashed to frozen reference optional
样本卡+标签轨迹, ✓✗, 薄荷绿训练步, 虚线奖励侧栏, 两阶段灰壳
```

## Palette

| Role | Fill | Stroke |
|------|------|--------|
| Stage shell | `#F2F2F2` | `#D0D0D0` |
| Preference / MiPO | `#F3E5D8` | `#C4A090` |
| Train / inject | `#C8E6C9` | `#66A86A` |
| Policy / warm | `#FFE0B2` | `#E0A060` |
| Good / bad | `#E3F2FD` / `#FFEBEE` | matching |
| Fake / Real strip | blue / orange accents | |

## Forbidden

- 扁平黄脸 emoji 当样本  
- 无样本卡的空 GRPO 框  
- 绿幕未抠
