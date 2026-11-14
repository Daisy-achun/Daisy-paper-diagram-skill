# Pre-delivery QA (paper framework figure)

Run this checklist before telling the user the figure is done.

## Execution contract（远端质量关键）
- [ ] Opened `DESIGN_GRAMMAR.md` + `CATALOG.md` + `method-storyboard.md` + locked `STYLE.md`/`LOOK.md`
- [ ] Printed **叙事分镜** block (spine / primary rail / on-path / secondary≤1 / out-of-figure) **before** style lock
- [ ] Exactly **one** primary rail; no competing spines
- [ ] No ablation / Verify / result matrix on the method figure
- [ ] Printed one line: `选用风格：compositions/<x> + looks/<y>` after storyboard
- [ ] Used `scaffold/scene_export.py` (or a template under `scaffold/templates/`) as same-source layout
- [ ] Did **not** ship Mermaid / ASCII boxes / one-shot AI concept board as the final figure
- [ ] Exported PNG was **opened/read** at ~100%; at least one fix-and-re-export if issues found

## Style routing
- [ ] Look chosen to **serve the storyboard**, not to fill every template panel
- [ ] Deleted look-template footers/side columns the Method does not have (e.g. SFT/RL bars)
- [ ] If ≥2 cores fit equally → **主动问**用户（2–3 个适配选项）后再画
- [ ] Did **not** wait for the user to say「换风格」before selecting
- [ ] `agent-panel` keeps the cream inference hero as the only spine
- [ ] Opened the locked `LOOK.md` Design thinking + Style keywords before drawing

## Content
- [ ] Modules / losses / numbers match Method (nothing invented)
- [ ] Novel block appears once (peach hero); inset explains mechanism
- [ ] Trainable / frozen / LoRA badges match reality; legend once
- [ ] On-path evidence (tools/chips/traj) hangs off the primary rail

## Typography
- [ ] Fig title 17–18; panel 14–15; module 13–14; body ≥11; floor ≥10
- [ ] No 7–8pt walls; shortened labels where needed
- [ ] Math uses true subscripts (not `R_task` ASCII)
- [ ] Code tokens may keep underscores (`go_high`, JSON keys)

## Layout
- [ ] No text overlapping chips / shapes
- [ ] No text overflowing card borders (≥6–8px pad)
- [ ] No truncated subtitles
- [ ] No nested white cards inside pastel stage columns
- [ ] Chip in reserved slot (below text or own column)
- [ ] Trajectory final lines inside card
- [ ] Dense panels checked at 100% zoom

## Assets
- [ ] Chips are flowchart-sized, no baked-in text/watermark
- [ ] Semantics match role (input / attn / residual / domain evidence)
- [ ] Failed generations rejected and redone

## Deliverables
- [ ] Native editable PPTX (not screenshot-only)
- [ ] SVG + PNG exported from the **same** Scene and visually inspected
- [ ] Caption + assumptions + locked style pack + same-source OK
  - [ ] Clickable `file://` links (or host open) for PNG / PPTX / SVG
