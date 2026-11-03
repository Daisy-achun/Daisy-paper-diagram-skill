# Pre-delivery QA (paper framework figure)

Run this checklist before telling the user the figure is done.

## Content
- [ ] Modules / losses / numbers match Method (nothing invented)
- [ ] Novel block appears once (peach hero); inset explains mechanism
- [ ] Trainable / frozen / LoRA badges match reality; legend once

## Typography
- [ ] Fig title 17–18; panel 14–15; module 13–14; body ≥11; floor ≥10
- [ ] No 7–8pt walls; shortened labels where needed
- [ ] Math uses true subscripts (not `R_task` ASCII)
- [ ] Code tokens may keep underscores (`go_high`, JSON keys)

## Layout
- [ ] No text overlapping chips / shapes
- [ ] No text overflowing card borders (≥6–8px pad)
- [ ] No truncated subtitles
- [ ] Chip in reserved slot (below text or own column)
- [ ] Trajectory final lines inside card
- [ ] Dense panels checked at 100% zoom

## Assets
- [ ] Chips are flowchart-sized, no baked-in text/watermark
- [ ] Semantics match role (input / attn / ELA / residual)
- [ ] Failed generations rejected and redone

## Deliverables
- [ ] Native editable PPTX (not screenshot-only)
- [ ] SVG + PNG exported and visually inspected
- [ ] Caption + assumptions + which refs were followed
