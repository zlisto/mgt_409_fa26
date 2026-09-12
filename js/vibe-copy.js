/**
 * Copy buttons for vibe pages.
 * Wrap: .vibe-code-wrap[data-vibe-copy]
 * Optional: data-vibe-src="relative/path.py" loads file into pre>code
 */
(function () {
  function textFromWrap(wrap) {
    const code = wrap.querySelector("pre.vibe-code code, pre.vibe-code");
    return (code && code.textContent) ? code.textContent.replace(/\n$/, "") : "";
  }

  function setBtnState(btn, label, className) {
    btn.textContent = label;
    btn.classList.remove("is-copied", "is-failed");
    if (className) btn.classList.add(className);
    window.setTimeout(function () {
      btn.textContent = "Copy";
      btn.classList.remove("is-copied", "is-failed");
    }, 1400);
  }

  function copyText(text, btn) {
    if (!text) {
      setBtnState(btn, "Empty", "is-failed");
      return;
    }
    function ok() {
      setBtnState(btn, "Copied", "is-copied");
    }
    function fail() {
      setBtnState(btn, "Failed", "is-failed");
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(ok).catch(fail);
      return;
    }
    try {
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      const worked = document.execCommand("copy");
      document.body.removeChild(ta);
      if (worked) ok();
      else fail();
    } catch (e) {
      fail();
    }
  }

  function wireWrap(wrap) {
    const btn = wrap.querySelector(".vibe-code-copy");
    if (!btn || btn.dataset.bound === "1") return;
    btn.dataset.bound = "1";
    btn.addEventListener("click", function () {
      copyText(textFromWrap(wrap), btn);
    });
  }

  function loadSrc(wrap) {
    const src = wrap.getAttribute("data-vibe-src");
    if (!src) return Promise.resolve();
    const code = wrap.querySelector("pre.vibe-code code") || wrap.querySelector("pre.vibe-code");
    if (!code) return Promise.resolve();
    return fetch(src, { cache: "no-cache" })
      .then(function (res) {
        if (!res.ok) throw new Error(String(res.status));
        return res.text();
      })
      .then(function (text) {
        code.textContent = text.replace(/\r\n/g, "\n");
      })
      .catch(function () {
        code.textContent =
          "# Could not load " +
          src +
          "\n# Open that file from the course site or ask the instructor.";
      });
  }

  document.querySelectorAll(".vibe-code-wrap[data-vibe-copy]").forEach(function (wrap) {
    wireWrap(wrap);
    loadSrc(wrap);
  });
})();
