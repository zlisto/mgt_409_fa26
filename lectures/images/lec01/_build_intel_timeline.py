"""Build curated OpenAI vs Anthropic intelligence timeline JSON for lec01."""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

SRC = (
    "https://raw.githubusercontent.com/oolong-tea-2026/"
    "artificial-analysis-leaderboards/main/data/2026-07-10/llms.json"
)
OUT = Path(__file__).with_name("intelligence_timeline.json")

PICKS = [
    ("openai", "GPT-3.5 Turbo", "2022-11-30"),
    ("openai", "GPT-4", "2023-03-14"),
    ("openai", "GPT-4 Turbo", "2023-11-06"),
    ("openai", "GPT-4o (May '24)", "2024-05-13"),
    ("openai", "o1-preview", "2024-09-12"),
    ("openai", "o1", "2024-12-05"),
    ("openai", "o3", "2025-04-16"),
    ("openai", "o3-pro", "2025-06-10"),
    ("openai", "GPT-5 (high)", "2025-08-07"),
    ("openai", "GPT-5.1 (high)", "2025-11-13"),
    ("openai", "GPT-5.2 (xhigh)", "2025-12-11"),
    ("openai", "GPT-5.4 (xhigh)", "2026-03-05"),
    ("openai", "GPT-5.5 (xhigh)", "2026-04-23"),
    ("openai", "GPT-5.6 Sol (max)", "2026-07-09"),
    ("anthropic", "Claude Instant", "2023-03-14"),
    ("anthropic", "Claude 2.0", "2023-07-11"),
    ("anthropic", "Claude 3 Opus", "2024-03-04"),
    ("anthropic", "Claude 3.5 Sonnet (June '24)", "2024-06-21"),
    ("anthropic", "Claude 3.7 Sonnet (Reasoning)", "2025-02-24"),
    ("anthropic", "Claude 4 Opus (Reasoning)", "2025-05-22"),
    ("anthropic", "Claude 4.1 Opus (Reasoning)", "2025-08-05"),
    ("anthropic", "Claude Opus 4.5 (Reasoning)", "2025-11-24"),
    ("anthropic", "Claude Opus 4.6 (Adaptive Reasoning, Max Effort)", "2026-02-05"),
    ("anthropic", "Claude Opus 4.7 (Adaptive Reasoning, Max Effort)", "2026-04-16"),
    ("anthropic", "Claude Opus 4.8 (Adaptive Reasoning, Max Effort)", "2026-05-28"),
    ("anthropic", "Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)", "2026-06-09"),
]

STRIP = [
    " (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)",
    " (Adaptive Reasoning, Max Effort)",
    " (Reasoning)",
    " (high)",
    " (xhigh)",
    " (max)",
]


def short_label(name: str) -> str:
    label = name
    for s in STRIP:
        label = label.replace(s, "")
    return label


def main() -> None:
    data = json.loads(urllib.request.urlopen(SRC, timeout=60).read())
    by_name = {(m["creator"]["slug"], m["name"]): m for m in data["models"]}
    out: dict[str, list] = {"openai": [], "anthropic": [], "source": SRC, "note": (
        "Artificial Analysis Intelligence Index from public leaderboard snapshot "
        "2026-07-10, plus Claude Opus 5 / GPT-5.6 Sol from Aug 2026 public AA board. "
        "Index composition changes over time; use for relative progress, not exact apples-to-apples."
    )}
    for creator, name, date in PICKS:
        m = by_name.get((creator, name))
        if not m:
            raise SystemExit(f"missing {creator} {name}")
        idx = round(float(m["evaluations"]["artificial_analysis_intelligence_index"]), 1)
        out[creator].append({"t": date, "y": idx, "label": short_label(name)})

    # Aug 2026 public Artificial Analysis board (post-snapshot releases / refresh)
    out["anthropic"].append({"t": "2026-07-24", "y": 63.0, "label": "Claude Opus 5"})
    for p in out["openai"]:
        if p["label"].startswith("GPT-5.6 Sol"):
            p["y"] = 60.9
            p["label"] = "GPT-5.6 Sol"

    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"wrote {OUT} openai={len(out['openai'])} anthropic={len(out['anthropic'])}")


if __name__ == "__main__":
    main()
