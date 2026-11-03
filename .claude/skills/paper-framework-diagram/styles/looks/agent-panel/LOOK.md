# Look: `agent-panel`


## One-line vibe

奶油黄推理主面板 + 蓝虚线 Think→Call→Observe 环 + 彩色标签轨迹时间线 + 右侧 Tools 浮层 + 底栏蓝 SFT / 紫 RL。

## Design thinking（设计思路提示词）

```text
First draw the runtime agent loop as the hero cream panel; nest a dashed blue
Think → Call Tool → Observation cycle; put a floating Tools UI on the right
(search, crop/zoom, tool library counts). Below the loop, a horizontal trajectory
timeline with colored tags and real image evidence crops. Foot the figure with
two training stages (SFT blue-grey, RL lavender) as secondary cards — never let
training steal the hero. Keep JSON final-answer chip at the end of the timeline.
先画运行时Agent奶油黄主壳与蓝虚线推理环；右侧Tools浮层；环下轨迹时间线必须有真实crop与彩色标签；
训练底栏缩小为蓝/紫两卡；最终JSON答案芯片收束。
```

## Prompt keywords（风格提示词）

```text
publication agent framework figure, cream yellow inference panel soft shadow,
blue dashed Think Call Observe loop, floating Tools toolbox panel UI,
trajectory timeline colored XML tags Think grounding tool_call Observation,
photo evidence crops heatmaps, token color legend text/tool/image,
pastel blue SFT footer, lavender RL footer with reward cards,
robot agent icon matted from green screen, no text overlap
淡黄Agent主面板, Tools浮层, 轨迹时间线, 蓝紫训练底栏, 真实证据crop
```

## Palette

| Role | Fill | Stroke |
|------|------|--------|
| Inference shell | `#FFF4C3` / `#FFF8E1` | `#E0C86A` |
| Loop dashed | — | `#64B5F6` |
| SFT stage | `#E3F2FD` | `#64B5F6` |
| RL stage | `#EDE7F6` | `#9575CD` |
| Tools float | `#BBDEFB` | `#1976D2` |
| Tag Think / Act / Obs | blue / pink / yellow | |

## Type

Sans；轨迹内关键词加粗；JSON/伪代码等宽。

## Nodes & shells

三大圆角面板轻阴影；环用虚线；时间线用竖虚线分隔单元格。

## Icons

Robot / magnifier / toolbox；绿幕生成后抠图；证据用真实照片。

## Connectors

实线顺序箭；双箭头表迭代；虚线分组。

## Forbidden

- 做成纯 CLIP 双塔  
- 只有空环没有轨迹 chip  
- 绿幕残留
