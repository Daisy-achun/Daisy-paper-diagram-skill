# Style system：构图 × 观感（两轴）

**一个主 skill**（`paper-framework-diagram`）管质量门禁、同源导出、抠图、数学下标。  
**不要**为每个视觉风格复制一整份 `SKILL.md`。

| 轴 | 目录 | 回答的问题 |
|----|------|------------|
| **Composition** | `compositions/` | 盒子怎么摆？ |
| **Look** | `looks/` | 色板、字体、图标、箭头气质？ |

仅换构图、观感不变 → **不算两种风格**。

## 推荐流程

1. 读 Method + [`DESIGN_GRAMMAR.md`](DESIGN_GRAMMAR.md)  
2. [`looks/CATALOG.md`](looks/CATALOG.md)「结构优先」+ [`router.md`](router.md) → **锁定 1 套**  
3. 打开 `looks/<id>/LOOK.md`，注入 **Design thinking + Style keywords**  
4. 一句话告知后直接画；SVG/PNG/PPTX 同源  

## 风格来源

| 路径 | 说明 |
|------|------|
| [`DESIGN_GRAMMAR.md`](DESIGN_GRAMMAR.md) | 共享设计语法与风格关键词 |
| [`looks/CATALOG.md`](looks/CATALOG.md) | 核心 8 look + Method→单套组合 |
| `looks/*/LOOK.md` | 单套 look 的色板、气质与禁止项 |
| 用户偏好 / 草图 | 有明确改稿意见时，映射到最近核心 look |

## 新增 look

复制 `looks/_template`；写清 Design thinking、Style keywords、色板、禁止项。勿提交无关大图资源。
