(function () {
  const slides = [...document.querySelectorAll(".slide")];
  if (!slides.length) return;

  let index = 0;
  const counter = document.querySelector(".slide-counter");
  const total = slides.length;

  function isFullscreen() {
    return Boolean(document.fullscreenElement);
  }

  function clearSlideScale(slide) {
    if (!slide) return;
    slide.style.removeProperty("transform");
    slide.style.removeProperty("width");
    slide.style.removeProperty("max-width");
    slide.style.removeProperty("max-height");
  }

  function updateFullscreenLayout() {
    slides.forEach(clearSlideScale);
    document.body.classList.toggle("is-fullscreen-deck", isFullscreen());
  }

  function show(i) {
    index = Math.max(0, Math.min(i, total - 1));
    slides.forEach((s, j) => s.classList.toggle("active", j === index));
    if (counter) counter.textContent = `${index + 1} / ${total}`;
    history.replaceState(null, "", `#slide-${index + 1}`);
    updateFullscreenLayout();
  }

  function next() { show(index + 1); }
  function prev() { show(index - 1); }

  document.getElementById("next")?.addEventListener("click", next);
  document.getElementById("prev")?.addEventListener("click", prev);

  function updateFullscreenButton() {
    const btn = document.getElementById("fullscreen");
    if (!btn) return;
    const on = isFullscreen();
    btn.textContent = on ? "Exit full screen" : "Full screen";
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    btn.setAttribute(
      "aria-label",
      on ? "Exit full screen" : "Enter full screen"
    );
  }

  async function toggleFullscreen() {
    try {
      if (isFullscreen()) {
        await document.exitFullscreen();
      } else {
        await document.documentElement.requestFullscreen();
      }
    } catch (_) {
      /* Browser blocked fullscreen (e.g. not a user gesture). */
    }
  }

  const footer = document.querySelector(".slide-deck-footer");
  if (footer && document.fullscreenEnabled && !document.getElementById("fullscreen")) {
    const fsBtn = document.createElement("button");
    fsBtn.type = "button";
    fsBtn.id = "fullscreen";
    fsBtn.textContent = "Full screen";
    fsBtn.setAttribute("aria-pressed", "false");
    fsBtn.setAttribute("aria-label", "Enter full screen");
    fsBtn.addEventListener("click", toggleFullscreen);
    footer.appendChild(fsBtn);
  }

  document.addEventListener("fullscreenchange", () => {
    updateFullscreenButton();
    updateFullscreenLayout();
  });

  window.addEventListener("resize", () => {
    if (isFullscreen()) updateFullscreenLayout();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
      e.preventDefault();
      next();
    } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
      e.preventDefault();
      prev();
    } else if (e.key === "Home") {
      e.preventDefault();
      show(0);
    } else if (e.key === "End") {
      e.preventDefault();
      show(total - 1);
    } else if (e.key === "f" || e.key === "F") {
      const tag = (e.target && e.target.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA" || e.target?.isContentEditable) return;
      e.preventDefault();
      toggleFullscreen();
    }
  });

  const hash = location.hash.match(/^#slide-(\d+)$/);
  if (hash) show(parseInt(hash[1], 10) - 1);
  else show(0);
})();
