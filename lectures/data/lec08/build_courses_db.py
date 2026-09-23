"""Build lec08 data.zip: SQLite courses table from lec07 yale_som_classes.json."""
from __future__ import annotations

import json
import sqlite3
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEC07_JSON = ROOT.parent / "lec07" / "yale_som_classes.json"
DB_PATH = ROOT / "yale_som.db"
ZIP_PATH = ROOT / "data.zip"

# Map JSON keys → friendly column names
COLUMNS = [
    ("course_id", "Course ID"),
    ("course_number", "Course Number"),
    ("course_title", "Course Title"),
    ("course_category", "Course Category"),
    ("course_type", "Course Type"),
    ("course_session", "Course Session"),
    ("course_description", "Course Description"),
    ("faculty_1", "Faculty 1"),
    ("faculty_1_email", "Faculty 1 Email"),
    ("faculty_bio", "faculty_bio"),
    ("daytimes", "Daytimes"),
    ("timings_day", "Timings Day"),
    ("timings_start", "Timings StartTime"),
    ("timings_end", "Timings EndTime"),
    ("room", "Room"),
    ("section", "Section"),
    ("units", "Units"),
    ("term_code", "TermCode"),
    ("syllabus", "Syllabus"),
    ("old_syllabus", "Old Syllabus"),
]


def main() -> None:
    rows = json.loads(LEC07_JSON.read_text(encoding="utf-8"))
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    col_defs = ", ".join(f"{name} TEXT" for name, _ in COLUMNS)
    cur.execute(
        f"""
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {col_defs}
        )
        """
    )
    placeholders = ", ".join("?" for _ in COLUMNS)
    col_names = ", ".join(name for name, _ in COLUMNS)
    for row in rows:
        values = [str(row.get(src, "") or "").strip() for _, src in COLUMNS]
        cur.execute(
            f"INSERT INTO courses ({col_names}) VALUES ({placeholders})",
            values,
        )
    con.commit()
    n = cur.execute("SELECT COUNT(*) FROM courses").fetchone()[0]
    con.close()
    print(f"wrote {DB_PATH} with {n} courses")

    # Zip as data/yale_som.db so unzip next to project gives data/yale_som.db
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(DB_PATH, arcname="data/yale_som.db")
    print(f"wrote {ZIP_PATH}")


if __name__ == "__main__":
    main()
