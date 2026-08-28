# MGT 409 lecture slide style rules

Canonical patterns for `website/lectures/slides/*.html` and shared `website/css/slides.css`.

Read this before authoring or editing any lecture deck.

---

## Responsive figures (the cursor-founder pattern)

**Goal:** Photos, screenshots, PNG charts, and diagrams should grow on larger viewports and fill available space in full-screen mode — same behavior as the **Cursor Founder** slide.

### CSS variables (in `slides.css`)

| Variable | Default | Use |
| -------- | ------- | --- |
| `--slide-figure-max-h` | `58vh` | Photos / PNG figures |
| `--slide-figure-max-px` | `560px` | Pixel cap (large monitors) |
| `--slide-chart-max-h` | `62vh` | Chart.js / canvas wrappers |
| `--slide-chart-max-px` | `680px` | Pixel cap for charts |

### Static images (photos, PNG bar charts, diagrams)

```css
.slide-figure {
  display: block;
  width: 100%;
  max-height: min(var(--slide-figure-max-h), var(--slide-figure-max-px));
  height: auto;
  object-fit: contain;       /* never crop legible content */
  object-position: top center;
}
```

**Do not** use fixed pixel-only `max-height` (e.g. `480px`) without a `vh` term — that prevents scaling on tall screens.

**Do not** use `object-fit: cover` on screenshots, charts, or diagrams unless you deliberately want cropping (rare).

Reuse existing class names where possible: `.news-shot`, `.frontier-chart`, `.arch-diagram`, `.topic-photo`, etc. — all are wired in `slides.css`.

Optional alias class: `.slide-media` (same rules).

### Chart.js / canvas slides

Wrap canvas in a flex child:

```html
<div class="slide-chart-wrap intel-chart-wrap">
  <canvas id="..."></canvas>
</div>
```

Parent slide must be a **flex column** when active:

```css
.slide.my-chart-slide { flex-direction: column; }
.slide.my-chart-slide.active { display: flex; }
```

Chart wrapper uses shared rules in `slides.css` (`height: min(var(--slide-chart-max-h), var(--slide-chart-max-px))`).

On chart build/resize, call `chart.resize()` when the slide becomes active (see lec01 `MutationObserver` pattern).

### Full-screen (F key)

`slides.css` already promotes all major figure classes to `flex: 1; max-height: none; object-fit: contain` in full-screen. When adding a **new** image class, add it to the full-screen selector block in `slides.css`.

**Exception:** tiny logos (e.g. `.vibe-logos img`) stay fixed height — do not add them to the full-screen flex-grow list.

---

## Flex slides (show one slide at a time)

Slides that use `display: flex` must **only** set `display: flex` on `.active`:

```css
.slide.foo-slide { flex-direction: column; }
.slide.foo-slide.active { display: flex; }   /* correct */

/* WRONG — stacks multiple slides visible at once */
.slide.foo-slide { display: flex; }
```

Applies to: transformer blocks, intel-race, frontier-models, pareto, etc.

---

## File layout

| Item | Path |
| ---- | ---- |
| Shared deck CSS | `website/css/slides.css` |
| Deck JS (nav, fullscreen) | `website/js/slides.js` |
| Per-lecture overrides | `<style>` block in `lectures/slides/lecNN-slides.html` |
| Images | `lectures/images/lecNN/` |
| Instructor pacing | `lectures/slide_notes.md` |

lec01 is hand-maintained; later lectures may be built from scripts — still follow these rules.

---

## Checklist for new slides with figures

1. Parent slide: flex column when `.active`
2. Figure: `width: 100%`, `max-height: min(var(--slide-figure-max-h), …)`, `object-fit: contain`
3. Charts: `.slide-chart-wrap` + resize on activate
4. Add new figure class names to full-screen block in `slides.css`
5. Test at 1080p and full-screen (F) on a large monitor
