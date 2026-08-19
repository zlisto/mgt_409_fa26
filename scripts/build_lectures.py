#!/usr/bin/env python3
"""Build slide and vibe HTML from lecture_data_part1/2."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_lectures import slide_html, vibe_html, SLIDES_DIR, VIBE_DIR
from lecture_data_part1 import DECK as DECK1
from lecture_data_part2 import DECK as DECK2

ALL = {**DECK1, **DECK2}


def main():
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    VIBE_DIR.mkdir(parents=True, exist_ok=True)
    for n in sorted(ALL.keys()):
        data = ALL[n]
        slides_path = SLIDES_DIR / f"lec{n:02d}-slides.html"
        vibe_path = VIBE_DIR / f"lec{n:02d}-vibe.html"
        slides_path.write_text(slide_html(n, data["title"], data["slides"]), encoding="utf-8")
        v = data["vibe"]
        vibe_path.write_text(
            vibe_html(n, data["title"], v["goal"], v.get("zip"), v["steps"]),
            encoding="utf-8",
        )
        print(f"Wrote lec{n:02d} ({len(data['slides'])} slides, {len(v['steps'])} vibe steps)")
    print("Skipped lec01 (hand-maintained)")


if __name__ == "__main__":
    main()
