(function () {
  const slides = [...document.querySelectorAll(".slide")];
  if (!slides.length) return;

  let index = 0;
  const counter = document.querySelector(".slide-counter");
  const total = slides.length;

  function show(i) {
    index = Math.max(0, Math.min(i, total - 1));
    slides.forEach((s, j) => s.classList.toggle("active", j === index));
    if (counter) counter.textContent = `${index + 1} / ${total}`;
    history.replaceState(null, "", `#slide-${index + 1}`);
  }

  function next() { show(index + 1); }
  function prev() { show(index - 1); }

  document.getElementById("next")?.addEventListener("click", next);
  document.getElementById("prev")?.addEventListener("click", prev);

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
    }
  });

  const hash = location.hash.match(/^#slide-(\d+)$/);
  if (hash) show(parseInt(hash[1], 10) - 1);
  else show(0);
})();
