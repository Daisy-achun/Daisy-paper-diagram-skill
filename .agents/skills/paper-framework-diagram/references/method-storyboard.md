# Method storyboard（叙事分镜 · 先于 Style lock）

装 look pack **不等于**会选对结构。远端掉档的主因是：一上来套 `agent-panel` /
`stage-band` 模板，再往空板里塞标签，结果一张图里出现 3–4 条平行故事。

**强制顺序：分镜 → Style lock → scaffold 绘制。** Look 服务主脊，禁止为塞满模板而加板。

## 必须输出的分镜块

画图前在回复里写出（可短，不可省略）：

```text
【叙事分镜】
Contribution spine: <本图只回答的一句话>
Primary rail: <有序模块链，≤1 条主路径>
On-path evidence: <挂在主脊上的工具带/芯片/轨迹；不是新故事>
Secondary panel: <0 或 1；默认 0>
Out of figure: <消融矩阵 / 结果表 / 离线协议细节 / …>
选用风格：compositions/<x> + looks/<y>
```

### 字段规则

| 字段 | 规则 |
|------|------|
| Contribution spine | 一句话；读者看完主脊应能复述 |
| Primary rail | 左→右（或上→下）一条有序链；禁止双主脊抢戏 |
| On-path evidence | 工具、芯片、轨迹必须从主脊某节点引出 |
| Secondary panel | 训练侧栏 / inset 等至多 1 个；默认 0 |
| Out of figure | 点名不画的内容；尤其是消融矩阵与结果表 |

## 反例 → 正例（Work-1）

### 反例（逻辑乱）

一张图同时塞：

1. ReAct 推理环  
2. Forensic-MCP / Obs  
3. `(c) Verify · W1-0…W1-7` 消融列  
4. 底部大块 `(b1) T-Eval` + `(b2) SPTR`  

→ 四条故事并置，箭头交叉，读者不知道 Fig.1 在讲什么。

### 正例（单主脊）

```text
【叙事分镜】
Contribution spine: 未训练 ReAct 鉴伪 Agent 在 Forensic-MCP 上选择性调用工具并给出可核查输出
Primary rail: Input → MLLM❄ → ReAct(Thought→call_tool/finish→Observe) → Forensic-MCP → Output
On-path evidence: Semantic / Artifact 双工具带 + traj 标签 + Obs card
Secondary panel: 0
Out of figure: W1 消融矩阵；T-Eval/SPTR 细节（仅标题脚注或另图）
选用风格：compositions/agent-loop + looks/agent-panel
```

## Look 模板常见陷阱

| Look | 模板诱惑 | 正确做法 |
|------|----------|----------|
| `agent-panel` | 默认画蓝/紫训练底栏 | Method 无 SFT/RL → **删掉**底栏 |
| `agent-panel` | 右侧塞满 Tools + 再加 Verify 列 | 工具挂在环上；Verify 属实验图 |
| `rl-grpo-chain` | 为对称硬塞双阶段 | 只有一段训练 → 单轨 |
| `stage-band-pastel` | 为凑 Stage 发明阶段名 | 阶段名必须来自 Method |
| `benchmark-dense` | 把结果表画进框架图 | 结果另图 |

## 与 router 的关系

[`styles/router.md`](../styles/router.md) 只在 **分镜写完之后** 使用：用 Primary rail
的结构信号选 composition×look，而不是用关键词硬套后再往图里加实验板。
