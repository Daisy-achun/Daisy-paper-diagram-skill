# Look: `paradigm-compare`


## One-line vibe

虚线分隔左右（或四格）对比基线 vs 提出方法；动作芯片（Locate/Examine）；token 紫方块；可选上绿/下橙/蓝三色带。

## Design thinking

```text
Use a dashed vertical divider. Left = multi-turn proposed method with action
chips and crops; Right = one-turn baseline. Or stack pastel bands: paradigms
(green), training (peach), inference (blue) optional. Mark failure modes in
red text sparingly. Keep both sides sharing the same input thumbnail for fair
compare.
竖虚线对开：左多轮提出法+动作芯片+crop，右单轮基线；或绿/桃/蓝三色带；
两侧共用同一输入缩略图。
```

## Prompt keywords

```text
side-by-side paradigm compare, dashed vertical divider, locate examine action chips,
purple token squares, shared input thumbnail, pastel band sections optional,
baseline vs proposed, magnifier crop callouts
左右范式对比, 虚线分隔, 动作芯片, token紫块, 可选三色带
```

## Forbidden

- 两边完全不同输入导致不可比  
- 把训练细节塞满对比格
