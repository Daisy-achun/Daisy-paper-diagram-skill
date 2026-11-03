# Composition: `agent-loop`

**轴：构图 only。** 默认配对 `looks/agent-panel`（一篇 Method 只此一套）。

控制环 / 多步工具调用推理。

## Composition

Inference band：Input → Policy loop (Think/Call/Observe) → Trajectories → Tool Bank  
可选底部：SFT / RL 训练条。

## Default look pairing

`looks/agent-panel` — 淡黄主面板 + 蓝/紫训练底栏。  
若用户要换气质，换 look（如 `sidebar-stage` / `stage-band-pastel`），不要只重排盒子。

## Forbidden

把纯网络轨或纯两阶段训练硬套成控制环；  
为凑多样性改换无关 look。
