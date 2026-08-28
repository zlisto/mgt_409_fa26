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
    const exitBtn = document.getElementById("exit-present");
    const on = isPresentationActive();

    if (btn) {
      btn.hidden = on;
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      btn.setAttribute(
        "aria-label",
        on ? "Exit presentation mode" : "Start presentation"
      );
      btn.title = on ? "Exit presentation" : "Start presentation";
    }

    if (exitBtn) {
      exitBtn.hidden = !on;
    }
  }

  async function exitPresentation() {
    if (isNativeFullscreen()) {
      try {
        await exitNativeFullscreen();
      } catch (_) {
        /* ignore */
      }
    }
    presentationMode = false;
    updatePresentButton();
    updateFullscreenLayout();
  }

  async function togglePresentation() {
    if (isPresentationActive()) {
      await exitPresentation();
      return;
    }

    try {
      await requestNativeFullscreen();
      updatePresentButton();
      updateFullscreenLayout();
      return;
    } catch (_) {
      /* iOS Safari and some mobile browsers block document fullscreen. */
    }
    presentationMode = true;
    updatePresentButton();
    updateFullscreenLayout();
  }

  function exitPresentIconSvg() {
    return (
      '<svg class="exit-present-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
      '<path d="M7 7l10 10M17 7L7 17" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round"/>' +
      "</svg>"
    );
  }

  if (!document.getElementById("present")) {
    const header = document.querySelector(".slide-deck-header");
    const headerEnd = document.createElement("div");
    headerEnd.className = "slide-deck-header-end";
    const presentBtn = document.createElement("button");
    presentBtn.type = "button";
    presentBtn.id = "present";
    presentBtn.className = "slide-present-btn";
    presentBtn.innerHTML = presentIconSvg();
    presentBtn.setAttribute("aria-pressed", "false");
    presentBtn.setAttribute("aria-label", "Start presentation");
    presentBtn.title = "Start presentation";
    headerEnd.appendChild(presentBtn);
    const counter = document.querySelector(".slide-counter");
    if (counter) headerEnd.appendChild(counter);
    if (header) header.appendChild(headerEnd);
    else document.body.appendChild(presentBtn);
  }

  const presentBtn = document.getElementById("present");
  if (presentBtn && !presentBtn.dataset.bound) {
    presentBtn.dataset.bound = "1";
    presentBtn.addEventListener("click", togglePresentation);
    updatePresentButton();
  }

  if (!document.getElementById("exit-present")) {
    const exitBtn = document.createElement("button");
    exitBtn.type = "button";
    exitBtn.id = "exit-present";
    exitBtn.className = "slide-exit-present-btn";
    exitBtn.innerHTML = exitPresentIconSvg();
    exitBtn.hidden = true;
    exitBtn.setAttribute("aria-label", "Exit presentation");
    exitBtn.title = "Exit presentation";
    exitBtn.addEventListener("click", exitPresentation);
    document.body.appendChild(exitBtn);
  }

  function onFullscreenChange() {
    if (!isNativeFullscreen()) presentationMode = false;
    updatePresentButton();
    updateFullscreenLayout();
  }

  document.addEventListener("fullscreenchange", onFullscreenChange);
  document.addEventListener("webkitfullscreenchange", onFullscreenChange);

  function syncDeckToolbarOffset() {
    const nav = document.querySelector(".site-nav");
    if (!nav) return;
    document.body.style.setProperty("--deck-toolbar-top", `${nav.offsetHeight}px`);
  }

  syncDeckToolbarOffset();
  window.addEventListener("resize", syncDeckToolbarOffset);
  window.addEventListener("orientationchange", syncDeckToolbarOffset);

  window.addEventListener("resize", () => {
    if (isPresentationActive()) updateFullscreenLayout();
  });

  function bindSwipeNavigation(surface) {
    if (!surface) return;

    let startX = 0;
    let startY = 0;
    let tracking = false;
    let swipeAxis = null;

    function isInteractiveTarget(target) {
      return Boolean(
        target.closest(
          "a, button, input, textarea, select, label, canvas, .slide-chart-wrap, .intel-chart-wrap, .pareto-chart-wrap"
        )
      );
    }

    surface.addEventListener(
      "touchstart",
      (e) => {
        if (e.touches.length !== 1) return;
        if (isInteractiveTarget(e.target)) {
          tracking = false;
          swipeAxis = null;
          return;
        }
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        tracking = true;
        swipeAxis = null;
      },
      { passive: true }
    );

    surface.addEventListener(
      "touchmove",
      (e) => {
        if (!tracking || e.touches.length !== 1) return;
        const dx = e.touches[0].clientX - startX;
        const dy = e.touches[0].clientY - startY;
        if (!swipeAxis && (Math.abs(dx) > 12 || Math.abs(dy) > 12)) {
          swipeAxis = Math.abs(dx) > Math.abs(dy) * 1.05 ? "h" : "v";
        }
        if (swipeAxis === "h") e.preventDefault();
      },
      { passive: false }
    );

    surface.addEventListener(
      "touchend",
      (e) => {
        if (!tracking) return;
        tracking = false;
        if (swipeAxis !== "h") {
          swipeAxis = null;
          return;
        }
        const touch = e.changedTouches[0];
        const dx = touch.clientX - startX;
        const dy = touch.clientY - startY;
        swipeAxis = null;
        if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) return;
        if (dx < 0) next();
        else prev();
      },
      { passive: true }
    );

    surface.addEventListener(
      "touchcancel",
      () => {
        tracking = false;
        swipeAxis = null;
      },
      { passive: true }
    );
  }

  bindSwipeNavigation(document.querySelector(".slide-deck-body") || viewport);

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
    } else if (e.key === "Escape") {
      if (isPresentationActive()) {
        e.preventDefault();
        exitPresentation();
      }
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
