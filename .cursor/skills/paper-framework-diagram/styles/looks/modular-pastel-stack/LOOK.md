# Look: `modular-pastel-stack`


## One-line vibe

功能色圆角算子块 + Nx 浅灰外壳 + 残差弯箭 + ⊕；可右挂虚线 zoom-in。

## Design thinking

```text
Assign one pastel fill per operator family (attention peach, FFN blue, norm
yellow, embed pink) and reuse that mapping everywhere. Wrap repeated stacks in
a light-gray Nx rounded shell. Draw residual skips as smooth curved arrows into
Add&Norm. Prefer bottom-up dual columns (encoder|decoder) or horizontal multi
towers. Put matrix/heatmap math in a right dashed inset, not in the main
rail. Thin black strokes, almost no drop shadow.
同类算子同色复用；重复层用Nx浅灰圆角壳；残差画平滑弯箭进Add&Norm；
双柱或多竖塔；热力/矩阵细节进右侧虚线inset；细黑描边少阴影。
```

## Style keywords

```text
2D modular architecture diagram, pastel color-coded operators, thin black outlines,
rounded rectangles, Nx gray stack shells, residual curved skip connections,
circled plus ops, encoder-decoder dual column or multi vertical towers,
white academic background, optional right dashed inset attention map
pastel功能色模块, Nx灰壳, 残差弯箭, ⊕, 双柱或多竖塔, 右侧inset
```

## Palette

| Role | Fill |
|------|------|
| Attention | peach / orange |
| FFN | sky blue |
| Norm / Add | pale yellow |
| Embed / IO | muted pink |
| Causal attn | mint |
| Cross attn | deep orange |
| Stack shell | `#EEEEEE` |

## Forbidden

- 等距 3D CNN 方块（那是另一路，仅 CNN Method）  
- 轨迹 Agent 时间线
