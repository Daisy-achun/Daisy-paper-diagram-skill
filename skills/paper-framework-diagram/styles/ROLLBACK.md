# Why Type A cream broke (GitHub timeline)

Repo: https://github.com/Daisy-achun/Daisy-paper-framework-skill

| Time (CST) | Commit | What happened |
|---|---|---|
| **2026-10-31 22:00** | `55aa806` | **Good Type A.** Hard hex in SKILL: cream `#FFF6E0`, peach `#F7D6C8`, blue `#EAF2FB`, lavender `#F0EAF8`. Demo figs `examples/figure-*-v2/v3.{svg,png}` present. |
| **2026-10-31 23:06** | `cf7b1d9` | **Break.** Deleted demo figures + generator; renamed/rewrote skill; Type A recipes diluted. |
| 2026-11-02 | `8b75269`…`28d7c0f` | Scope rename + style-confirmation gates; still no restored Type A demos. |

## Local failure mode (this workspace)

After the public scrub, renders drifted to:

1. **RoT sparse** (`render_isf_band_routing_v2.py`) — white canvas, Material orange/blue **横条**（版式错）
2. **Wrong cream** (`render_isf_type_a.py`) — 色板近似但 **横排流水线**，不是金标准竖 Policy
3. Skill 曾误成「等用户说换风格」或「永远只给奶油/莫兰迪二选一」——应改为：  
   **AI 按 Method 从 8 核心自选；多解时主动问适配子集。**

**金标准版式（`agent-panel`）：** `scripts/render_tool_aware_framework_fig.py`  
左列 Input/Band → **竖向 peach Policy** → 中间轨迹卡 → 右 Tool Bank → 底栏蓝 SFT / 紫 GRPO。  
壳色 `#FFF8EC`，Policy `#F7D6C8`，Tools/SFT `#EAF2FB`，GRPO `#F0EAF8`。

## Restore path

1. 结构唯一 → AI 自选对应 look 绘制（Agent 环 → 上列金标准脚本）。  
2. 结构多解 → AI 主动问 2–3 个适配核心（从 8 心里筛）。  
3. 禁止稀疏横条冒充 `agent-panel`；禁止风格菜单缩成固定两种。
