(function () {
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");

  const moonIcon =
    '<svg class="theme-toggle-svg" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M21 14.5A8.5 8.5 0 1 1 9.5 3 6.5 6.5 0 0 0 21 14.5Z" fill="currentColor"/>' +
    "</svg>";

  const sunIcon =
    '<svg class="theme-toggle-svg" viewBox="0 0 24 24" aria-hidden="true">' +
    '<circle cx="12" cy="12" r="4.2" fill="currentColor"/>' +
    '<path d="M12 2.5v2.2M12 19.3v2.2M4.5 4.5l1.55 1.55M17.95 17.95l1.55 1.55M2.5 12h2.2M19.3 12h2.2M4.5 19.5l1.55-1.55M17.95 6.05l1.55-1.55" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>' +
    "</svg>";

  function buildToggle() {
    if (!toggle || toggle.querySelector(".theme-toggle-track")) return;
    toggle.innerHTML =
      '<span class="theme-toggle-track">' +
      '<span class="theme-toggle-icon theme-toggle-moon">' + moonIcon + "</span>" +
      '<span class="theme-toggle-thumb" aria-hidden="true"></span>' +
      '<span class="theme-toggle-icon theme-toggle-sun">' + sunIcon + "</span>" +
      "</span>";
    toggle.setAttribute("role", "switch");
  }

  function applyTheme(theme) {
    if (theme === "dark") {
      root.setAttribute("data-theme", "dark");
    } else {
      root.removeAttribute("data-theme");
    }
    localStorage.setItem("theme", theme);
    updateButton(theme);
  }

  function updateButton(theme) {
    if (!toggle) return;
    const isDark = theme === "dark";
    toggle.setAttribute("aria-checked", isDark ? "true" : "false");
    toggle.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
    toggle.title = isDark ? "Light mode" : "Dark mode";
  }

  buildToggle();

  if (toggle) {
    const saved = localStorage.getItem("theme") || "light";
    updateButton(saved);
    toggle.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
    });
  }
})();
