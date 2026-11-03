# Look: `retrieval-augment`


## One-line vibe

左检索库圆柱 + Top-k 证据脸框；中央竖直 MLLM 蓝柱；右分步 Critical Reasoning；证据与文字同色高亮绑定。

## Design thinking

```text
Pipeline L→R: embed → DB cylinder → top-k evidence wall → vertical MLLM pillar →
numbered reasoning steps. Color-link nouns in the reasoning text to the same
colors on evidence boxes (eyebrows/chin). Prompt sits in a red dashed card into
the pillar. Keep density high but aligned in three columns.
左检索→中竖直MLLM柱→右分步推理；推理文字与证据框同色高亮绑定；Prompt红虚线卡接入柱。
```

## Prompt keywords

```text
retrieval-augmented MLLM figure, pink cylinder database, top-k evidence faces with boxes,
vertical blue gradient MLLM pillar, numbered critical reasoning steps,
color-linked text highlights, red dashed system prompt card, flat academic
检索库圆柱, Top-k证据墙, 竖直MLLM柱, 分步推理同色高亮
```

## Forbidden

- 无证据墙的空 RAG 箭头  
- 评测 logo 墙冒充检索
