# PowerPoint and Computer Use checklist

Use this reference when the task requires an editable PPT figure. The main
skill contains the decision rules; this file contains the interaction details
that are easy to miss in a dense diagram.

## Before editing

1. Inspect the current desktop/window state with Computer Use. Confirm the
   presentation app and whether an existing deck is already open.
2. If editing an existing file, save a versioned copy before changing it. Keep
   unrelated slides and speaker notes intact.
3. Confirm slide size, orientation, language, and target paper width. Set the
   custom slide size before adding objects.
4. Establish guides or a simple grid. Reserve a safe margin around the canvas
   and keep the densest panel away from the edges.

## Building rules

- Use native PowerPoint text boxes for all technical text. Do not bake labels
  into a generated image.
- Use connectors rather than freehand lines so arrows remain attached when
  modules move.
- Build one repeated component, group it, and duplicate it before changing
  labels. Ungroup only when a local edit is required.
- Align and distribute objects after every rail or panel. Keep the z-order
  deliberate: shells behind modules, arrows behind labels, inset leaders above
  panels.
- Keep one legend for trainable/frozen/adapters and one operator legend for
  `+`, `C`, `x`, or other symbols. Avoid repeating legends inside every card.
- Use a consistent text hierarchy. Do not reduce font size to solve overflow;
  shorten labels, widen the panel, or move detail into an inset.
- Use real crops, heatmaps, masks, or plots only when they communicate a real
  input or intermediate. Crop them cleanly and add a small label outside the
  image rather than overprinting dense text.
- Save after each major stage and keep the source filename deterministic.

## Visual QA loop

After the first layout pass:

1. Zoom to fit and inspect the overall reading order.
2. Zoom to 100% on the densest panel and the smallest labels.
3. Check that every connector lands on the correct edge and that no line runs
   through text or hides behind an unrelated object.
4. Check that groups do not contain accidental off-canvas objects and that
   the canvas has no clipped shapes.
5. Check contrast in grayscale or with a color-blind simulation when possible.
6. Save, export a preview, reopen the exported file or render it, and repeat
   once after fixing issues.

## Export rules

- Keep PPTX as the editable master.
- Export PDF first when possible; it preserves text/vector geometry.
- Create PNG/TIFF from the PDF at the target physical width and 300–600 dpi
  when direct PowerPoint raster export is too small.
- Check the raster pixel dimensions against the requested dpi and width.
- Reopen the final PPTX and PDF, or render a preview, before reporting them as
  complete.

## Fallbacks

If PowerPoint is unavailable, try Keynote or LibreOffice and state the choice.
If no presentation GUI is available, use the repository's programmatic SVG
path, preserve vector output, and report that an editable PowerPoint file could
not be produced. Do not silently present an SVG or screenshot as a PPTX.
