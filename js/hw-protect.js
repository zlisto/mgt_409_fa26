(function () {
  var root = document.documentElement;
  if (!root.hasAttribute("data-mgt409")) return;

  // Shared scenario/brief:
  //   <div data-hw-brief="scenario.html"></div>
  //   <div data-hw-brief="scenario.html" data-hw-brief-open></div>  ← open on P1
  document.querySelectorAll("[data-hw-brief]").forEach(function (slot) {
    var src = slot.getAttribute("data-hw-brief");
    if (!src) return;
    var startOpen = slot.hasAttribute("data-hw-brief-open");
    fetch(src)
      .then(function (res) {
        if (!res.ok) throw new Error("brief " + res.status);
        return res.text();
      })
      .then(function (html) {
        var wrap = document.createElement("div");
        wrap.innerHTML = String(html).trim();
        var node = wrap.firstElementChild;
        if (node && startOpen && node.tagName === "DETAILS") {
          node.setAttribute("open", "");
        }
        if (node) {
          slot.replaceWith(node);
        } else {
          slot.outerHTML = html;
        }
      })
      .catch(function () {
        slot.innerHTML =
          '<p class="hw-brief-error">Could not load scenario. Open this page from the course site (not a raw file).</p>';
      });
  });

  function block(event) {
    event.preventDefault();
    return false;
  }

  document.addEventListener("copy", function (event) {
    if (document.body.getAttribute("data-hw-allow-copy") === "1") return;
    return block(event);
  }, true);
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

  // Terminal commands: chrome bar + Copy (clipboard API; assignment text stays unselectable)
  document.querySelectorAll("pre.terminal").forEach(function (pre) {
    if (pre.parentElement && pre.parentElement.classList.contains("hw-terminal-wrap")) {
      return;
    }
    var wrap = document.createElement("div");
    wrap.className = "hw-terminal-wrap";
    pre.parentNode.insertBefore(wrap, pre);

    var chrome = document.createElement("div");
    chrome.className = "hw-terminal-chrome";

    var label = document.createElement("span");
    label.className = "hw-terminal-label";
    label.textContent = "Terminal";

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "hw-terminal-copy";
    btn.textContent = "Copy";
    btn.setAttribute("aria-label", "Copy terminal command");

    chrome.appendChild(label);
    chrome.appendChild(btn);
    wrap.appendChild(chrome);
    wrap.appendChild(pre);

    btn.addEventListener("click", function () {
      var code = pre.querySelector("code");
      var text = ((code || pre).textContent || "").replace(/\s+$/, "");

      function flash(ok) {
        btn.textContent = ok ? "Copied" : "Failed";
        btn.classList.toggle("is-copied", ok);
        btn.classList.toggle("is-failed", !ok);
        setTimeout(function () {
          btn.textContent = "Copy";
          btn.classList.remove("is-copied", "is-failed");
        }, 1600);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          flash(true);
        }).catch(function () {
          flash(false);
        });
        return;
      }

      try {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        document.body.setAttribute("data-hw-allow-copy", "1");
        var ok = document.execCommand("copy");
        document.body.removeAttribute("data-hw-allow-copy");
        document.body.removeChild(ta);
        flash(ok);
      } catch (err) {
        document.body.removeAttribute("data-hw-allow-copy");
        flash(false);
      }
    });
  });

  // Split problem panels: only one half visible at a time
  document.querySelectorAll(".hw-split-problem").forEach(function (card) {
    var buttons = card.querySelectorAll(".hw-split-toggle button");
    var panels = card.querySelectorAll(".hw-split-panel");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var target = btn.getAttribute("data-panel");
        buttons.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle("is-active", on);
          b.setAttribute("aria-selected", on ? "true" : "false");
        });
        panels.forEach(function (panel) {
          panel.classList.toggle("is-active", panel.getAttribute("data-panel") === target);
        });
      });
    });
  });
})();
