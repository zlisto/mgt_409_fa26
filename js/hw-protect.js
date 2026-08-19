(function () {
  var root = document.documentElement;
  if (!root.hasAttribute("data-mgt409")) return;

  function block(event) {
    event.preventDefault();
    return false;
  }

  document.addEventListener("copy", block, true);
  document.addEventListener("cut", block, true);
  document.addEventListener("selectstart", block, true);
  document.addEventListener("contextmenu", block, true);

  document.addEventListener("keydown", function (event) {
    var key = (event.key || "").toLowerCase();
    var combo = event.ctrlKey || event.metaKey;
    if (!combo) return;
    if (key === "c" || key === "x" || key === "a" || key === "u" || key === "s" || key === "p") {
      event.preventDefault();
    }
  }, true);

  window.addEventListener("beforeprint", function () {
    document.body.setAttribute("data-hw-print-block", "1");
  });
  window.addEventListener("afterprint", function () {
    document.body.removeAttribute("data-hw-print-block");
  });
})();
