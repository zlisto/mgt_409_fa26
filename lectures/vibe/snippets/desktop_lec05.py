"""Native window: real Chromium on the left, Dash chat on the right."""

from __future__ import annotations

import sys
import threading
import time
import urllib.error
import urllib.request

from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QAction
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

CHAT_URL = "http://127.0.0.1:8050/"
WINDOW_TITLE = "Browser agent"
HOME_HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  html, body { height: 100%; margin: 0; background: #f5f5f5; color: #222;
    font-family: system-ui, sans-serif; }
  .box { min-height: 100%; display: flex; align-items: center; justify-content: center;
    text-align: center; padding: 40px; box-sizing: border-box; }
  h1 { margin: 0 0 12px; font-size: 1.5rem; }
  p { max-width: 460px; line-height: 1.5; color: #444; }
</style></head>
<body><div class="box"><div>
  <h1>This is a real browser</h1>
  <p>Type any website or PDF URL in the bar above.
  Ask the chat on the right; it can screenshot when your question needs what’s on screen.</p>
</div></div></body></html>
"""


class SameTabPage(QWebEnginePage):
    """Open target=_blank links in this same pane instead of a new window."""

    def createWindow(self, _wintype):
        return self


class BrowserPane(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.view = QWebEngineView()
        page = SameTabPage(self.view)
        self.view.setPage(page)
        settings = self.view.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        if hasattr(QWebEngineSettings.WebAttribute, "PdfViewerEnabled"):
            settings.setAttribute(QWebEngineSettings.WebAttribute.PdfViewerEnabled, True)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Type any website or PDF URL…")
        self.url_bar.returnPressed.connect(self.go)

        back = QPushButton("←")
        forward = QPushButton("→")
        reload_btn = QPushButton("Reload")
        go_btn = QPushButton("Go")
        open_btn = QPushButton("Open file")
        back.clicked.connect(self.view.back)
        forward.clicked.connect(self.view.forward)
        reload_btn.clicked.connect(self.view.reload)
        go_btn.clicked.connect(self.go)
        open_btn.clicked.connect(self.open_file)

        chrome = QHBoxLayout()
        chrome.setContentsMargins(8, 8, 8, 8)
        chrome.setSpacing(6)
        for widget in (back, forward, reload_btn, self.url_bar, go_btn, open_btn):
            chrome.addWidget(widget)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        chrome_host = QWidget()
        chrome_host.setObjectName("chrome")
        chrome_host.setLayout(chrome)
        layout.addWidget(chrome_host)
        layout.addWidget(self.view, 1)

        self.view.urlChanged.connect(self._sync_url)
        self.view.setHtml(HOME_HTML, QUrl("https://browser-agent.local/home"))

    def go(self) -> None:
        text = self.url_bar.text().strip()
        if not text:
            return
        if text.startswith("file://") or "://" in text:
            url = QUrl(text)
        elif text.startswith("\\\\") or (len(text) > 2 and text[1] == ":"):
            url = QUrl.fromLocalFile(text)
        else:
            url = QUrl("https://" + text)
        self.view.setUrl(url)

    def open_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open page or PDF",
            "",
            "Web and PDF (*.pdf *.html *.htm);;All files (*.*)",
        )
        if path:
            self.view.setUrl(QUrl.fromLocalFile(path))

    def _sync_url(self, url: QUrl) -> None:
        shown = url.toString()
        if shown.startswith("https://browser-agent.local/"):
            return
        self.url_bar.setText(shown)


class DesktopWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(1500, 900)

        browser = BrowserPane()
        chat = QWebEngineView()
        chat.setUrl(QUrl(CHAT_URL))

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setObjectName("app-split")
        splitter.setHandleWidth(6)
        splitter.setChildrenCollapsible(False)
        browser.setMinimumWidth(420)
        chat.setMinimumWidth(320)
        splitter.addWidget(browser)
        splitter.addWidget(chat)
        splitter.setSizes([980, 520])
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)
        self.setCentralWidget(splitter)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        self.addAction(quit_action)


def _wait_for_dash(url: str = CHAT_URL, timeout_s: float = 20) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        try:
            urllib.request.urlopen(url, timeout=0.6)
            return
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(0.2)
    raise RuntimeError(f"Dash chat did not start at {url}")


def run_desktop() -> None:
    from app import app as dash_app

    def _serve() -> None:
        dash_app.run(host="127.0.0.1", port=8050, debug=False, use_reloader=False)

    threading.Thread(target=_serve, name="dash-server", daemon=True).start()
    _wait_for_dash()

    qt = QApplication(sys.argv)
    window = DesktopWindow()
    window.show()
    sys.exit(qt.exec())
