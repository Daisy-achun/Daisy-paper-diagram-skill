# Look: `dual-modality-gradient`


## One-line vibe

上蓝 Text❄ / 下橙 Image🔥LoRA 双塔；竖条编码器；对比损失虚线桥；可选 Shallow|Deep。

## Design thinking

```text
Lock modality colors: Text = cool blue/lavender + snowflakes; Vision = warm
orange/gold + fire/LoRA. Draw encoders as vertical bar stacks. Put L_clip or
contrastive loss as a dashed bridge between towers; classification oval at the
end of the image stream. Optional vertical dashed split Shallow|Deep with small
adapter bridges on fire. Keep domain evidence thumbnails on the vision side.
模态色锁死：Text冷蓝❄，Vision暖橙🔥LoRA；编码器画竖条；对比损失做两塔间虚线桥；
可选浅/深层虚线分隔与小Adapter桥；视觉侧放领域证据缩略图。
```

## Prompt keywords

```text
dual-stream CLIP academic figure, blue text tower frozen snowflake,
orange image tower LoRA fire, vertical encoder bars, contrastive loss dashed bridge,
classification head Fake/True oval, shallow-deep dashed split optional,
pastel fills thin strokes, face thumbnail grid on vision rail
蓝橙双塔, ❄文本🔥图像, 竖条编码器, 对比损失桥, 浅深层分隔
```

## Palette

| Role | Fill | Stroke |
|------|------|--------|
| Text stream shell | `#E3F2FD` | `#64B5F6` dashed |
| Image stream shell | `#FFF3E0` | `#FFB74D` dashed |
| Text feature | `#1565C0` | — |
| Image feature | `#EF6C00` | — |
| Loss bridge | `#E8F5E9` | `#66BB6A` dashed |
| Adapter / MFA | `#FFE0B2` | fire |

## Forbidden

- Agent Tools 浮层抢戏  
- 两塔同色
