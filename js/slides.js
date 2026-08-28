(function () {
  const slides = [...document.querySelectorAll(".slide")];
  if (!slides.length) return;

  let index = 0;
  let presentationMode = false;
  const counter = document.querySelector(".slide-counter");
  const total = slides.length;
  const viewport = document.querySelector(".slide-viewport");

  function getFullscreenElement() {
    return (
      document.fullscreenElement ||
      document.webkitFullscreenElement ||
      null
    );
  }

  function isNativeFullscreen() {
    return Boolean(getFullscreenElement());
  }

  function isPresentationActive() {
    return isNativeFullscreen() || presentationMode;
  }

  function requestNativeFullscreen() {
    const el = document.documentElement;
    const req = el.requestFullscreen || el.webkitRequestFullscreen;
    if (!req) return Promise.reject(new Error("unsupported"));
    return Promise.resolve(req.call(el));
  }

  function exitNativeFullscreen() {
    const exit = document.exitFullscreen || document.webkitExitFullscreen;
    if (!exit) return Promise.reject(new Error("unsupported"));
    return Promise.resolve(exit.call(document));
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
    document.body.classList.toggle("is-fullscreen-deck", isPresentationActive());
  }

  function show(i) {
    index = Math.max(0, Math.min(i, total - 1));
    slides.forEach((s, j) => s.classList.toggle("active", j === index));
    if (counter) counter.textContent = `${index + 1} / ${total}`;
    history.replaceState(null, "", `#slide-${index + 1}`);
    updateFullscreenLayout();
    window.dispatchEvent(new CustomEvent("slidechange", { detail: { index } }));
  }

  function next() {
    show(index + 1);
  }

  function prev() {
    show(index - 1);
  }

  document.getElementById("next")?.addEventListener("click", next);
  document.getElementById("prev")?.addEventListener("click", prev);

  function presentIconSvg() {
    return (
      '<svg class="present-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
      '<rect x="3" y="4" width="18" height="12" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.75"/>' +
      '<path d="M12 16v2.5M8 21h8M10 18.5h4" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>' +
      "</svg>"
    );
  }

  function updatePresentButton() {
    const btn = document.getElementById("present");
    if (!btn) return;
    const on = isPresentationActive();
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    btn.setAttribute(
      "aria-label",
      on ? "Exit presentation mode" : "Start presentation"
    );
    btn.title = on ? "Exit presentation" : "Start presentation";
  }

  async function togglePresentation() {
    if (isNativeFullscreen()) {
      try {
        await exitNativeFullscreen();
      } catch (_) {
        /* ignore */
      }
      presentationMode = false;
    } else if (presentationMode) {
      presentationMode = false;
    } else {
      try {
        await requestNativeFullscreen();
        updatePresentButton();
        updateFullscreenLayout();
        return;
      } catch (_) {
        /* iOS Safari and some mobile browsers block document fullscreen. */
      }
      presentationMode = true;
    }
    updatePresentButton();
    updateFullscreenLayout();
  }

  if (!document.getElementById("present")) {
    const presentBtn = document.createElement("button");
    presentBtn.type = "button";
    presentBtn.id = "present";
    presentBtn.className = "slide-present-btn";
    presentBtn.innerHTML = presentIconSvg();
    presentBtn.setAttribute("aria-pressed", "false");
    presentBtn.setAttribute("aria-label", "Start presentation");
    presentBtn.title = "Start presentation";
    presentBtn.addEventListener("click", togglePresentation);
    document.body.appendChild(presentBtn);
  }

  function onFullscreenChange() {
    if (!isNativeFullscreen()) presentationMode = false;
    updatePresentButton();
    updateFullscreenLayout();
  }

  document.addEventListener("fullscreenchange", onFullscreenChange);
  document.addEventListener("webkitfullscreenchange", onFullscreenChange);

  window.addEventListener("resize", () => {
    if (isPresentationActive()) updateFullscreenLayout();
  });

  if (viewport) {
    let startX = 0;
    let startY = 0;
    let tracking = false;

    viewport.addEventListener(
      "touchstart",
      (e) => {
        if (e.touches.length !== 1) return;
        const target = e.target;
        if (
          target.closest(
            "a, button, input, textarea, select, label, canvas, .slide-chart-wrap, .intel-chart-wrap, .pareto-chart-wrap"
          )
        ) {
          tracking = false;
          return;
        }
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        tracking = true;
      },
      { passive: true }
    );

    viewport.addEventListener(
      "touchend",
      (e) => {
        if (!tracking) return;
        tracking = false;
        const touch = e.changedTouches[0];
        const dx = touch.clientX - startX;
        const dy = touch.clientY - startY;
        if (Math.abs(dx) < 48 || Math.abs(dx) < Math.abs(dy) * 1.25) return;
        if (dx < 0) next();
        else prev();
      },
      { passive: true }
    );

    viewport.style.touchAction = "pan-y pinch-zoom";
  }

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
      if (tag === "INPUT" || tag === "TEXTAREA" || e.target?.isContentEditable) {
        return;
      }
      e.preventDefault();
      togglePresentation();
    }
  });

  const hash = location.hash.match(/^#slide-(\d+)$/);
  if (hash) show(parseInt(hash[1], 10) - 1);
  else show(0);
})();
