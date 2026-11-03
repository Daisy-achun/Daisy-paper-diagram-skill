# Icon & chip generation (paper figures)

Use with `paper-framework-diagram`. Goal: assets that survive zoom on a
publication Fig.1 — not emoji placeholders.

## Before generating

1. Prefer crops from the **paper PDF** or user-supplied boards.
2. If generating, write a one-line brief per asset: role, colors, forbidden
   elements.
3. Keep a consistent set: same perspective (slight 3/4 or flat 2D), soft
   shadow, no competing styles in one figure.

## Green-screen generation (default for AI icons)

When **generating** process/actor icons (not paper photo crops), use a
**solid chroma-key green background** so cutout is reliable:

| Spec | Value |
|------|--------|
| Background | Flat `#00FF00` or `#00B140` (pure chroma green) — **no** gradient, texture, or vignette |
| Subject | Keep subject colors **away from pure green** (no green fill on the glyph itself) |
| Margin | ≥8% empty green margin around the subject |
| Master size | 512×512 (or 768×768); downscale after cutout |
| Soft shadow | OK **on the subject only**; must not tint the green field |

Brief must include: `Background: solid chroma green #00FF00 for cutout`.

Do **not** ask the model for “transparent PNG” as the first output — many
generators bake white/checker mats. Prefer green → local matting.

## Cutout / 抠图 (mandatory before PPT insert)

**Never paste a green-screen (or white-boxed) master straight into PPTX.**

Pipeline:

1. Generate / save master: `figures/icons/_raw/NN_role_green.png`
2. **抠图** → RGBA with true alpha:
   - Remove chroma green (tolerance enough for mild anti-alias fringing)
   - Despill green edges if needed
   - Soften edge 0.5–1 px; keep subject shadow only if it still looks natural
3. Save cutout: `figures/icons/NN_role.png` (transparent)
4. Visual QA on **dark and light** cards before embed
5. Insert **only** the cutout into SVG / PPTX / layout

Suggested local helper (Pillow / rembg / PowerPoint「删除背景」均可):

```text
raw (green) → matte → NN_role.png (RGBA) → layout / python-pptx picture
```

If using PowerPoint GUI: Picture Format → Remove Background / Set Transparent
Color on green, then **re-export PNG with transparency** back into the
project assets — do not leave the editable slide as the only cutout copy.

### Forbidden at insert time

- Green-screen masters still visible behind the icon
- White / gray rectangle mattes around icons on cream or colored cards
- “Temporary” opaque icons left in the final PPTX

## Icon brief template

```text
Role: <base model | human annotation | reward | tool | dataset>
Style: clean 2D product illustration, soft gradient, light shadow
Size: 512×512 master → cutout → downscale to 64–96 px in figure
Background: solid chroma green #00FF00 (for cutout) — subject must not use pure green
Palette: <blue tech | coral human | green accept | red reject>
Must show: <1–2 concrete objects>
Must NOT: smile-face stickers, emoji heads, tiny unreadable text, watermark,
          green used as subject fill
Filename raw: _raw/NN_role_green.png
Filename cutout: NN_role.png   # transparent; this is what PPT uses
```

## Evidence chips (photos / maps)

Photo crops, heatmaps, ELA, draft grids: **no green screen**. Keep natural
background or paper crop. Still reserve a chip slot; labels stay outside the
image. Prefer PNG without unnecessary white borders.

## QA gate

- Recognizable at ~64 px
- Cutout has **no** green fringe / white box on cream or mint cards
- No baked-in equations or paper titles
- Distinct from other icons in the same figure
- Reject and regenerate on failure — do not ship smile faces or uncut green masters
