"""Build website/data/hw4/csmh.db from the JSON pack files."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "csmh.db"


def main() -> None:
    faq = json.loads((ROOT / "faq.json").read_text(encoding="utf-8"))
    shows_doc = json.loads((ROOT / "shows.json").read_text(encoding="utf-8"))
    tickets_doc = json.loads((ROOT / "sample_tickets.json").read_text(encoding="utf-8"))
    customers = json.loads((ROOT / "customers.json").read_text(encoding="utf-8"))

    confirm_to_user = {}
    for u in customers["users"]:
        for cid in u.get("confirmation_ids") or []:
            confirm_to_user[cid] = u["username"]

    if DB_PATH.exists():
        DB_PATH.unlink()

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.executescript(
        """
        CREATE TABLE meta (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE TABLE users (
            username TEXT PRIMARY KEY,
            display_name TEXT NOT NULL,
            password_salt TEXT NOT NULL,
            password_hash TEXT NOT NULL
        );
        CREATE TABLE shows (
            show_id TEXT PRIMARY KEY,
            artist TEXT NOT NULL,
            support TEXT,
            date TEXT NOT NULL,
            doors_local TEXT,
            show_local TEXT,
            age TEXT,
            notes TEXT
        );
        CREATE TABLE tickets (
            confirmation_id TEXT PRIMARY KEY,
            username TEXT,
            show_id TEXT,
            holder_name TEXT,
            quantity INTEGER,
            status TEXT,
            FOREIGN KEY (username) REFERENCES users(username),
            FOREIGN KEY (show_id) REFERENCES shows(show_id)
        );
        CREATE TABLE faq (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            answer TEXT NOT NULL,
            source_note TEXT,
            category_id TEXT
        );
        CREATE TABLE categories (
            id TEXT PRIMARY KEY,
            label TEXT NOT NULL,
            description TEXT
        );
        CREATE TABLE conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        );
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            screenshot_used INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL,
            FOREIGN KEY (conversation_id) REFERENCES conversations(id)
        );
        """
    )

    meta = {
        "venue": shows_doc.get("venue") or "College Street Music Hall",
        "address": shows_doc.get("address") or "",
        "password_algorithm": customers["algorithm"],
        "password_iterations": str(customers["iterations"]),
        "note": "Course SQLite pack for MGT 409 HW4. Not live venue data.",
    }
    cur.executemany("INSERT INTO meta(key, value) VALUES (?, ?)", list(meta.items()))

    cur.executemany(
        "INSERT INTO users(username, display_name, password_salt, password_hash) VALUES (?, ?, ?, ?)",
        [
            (u["username"], u["display_name"], u["password_salt"], u["password_hash"])
            for u in customers["users"]
        ],
    )
    cur.executemany(
        """INSERT INTO shows(show_id, artist, support, date, doors_local, show_local, age, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        [
            (
                s["show_id"],
                s["artist"],
                s.get("support") or "",
                s["date"],
                s.get("doors_local"),
                s.get("show_local"),
                s.get("age"),
                s.get("notes") or "",
            )
            for s in shows_doc["shows"]
        ],
    )
    cur.executemany(
        """INSERT INTO tickets(confirmation_id, username, show_id, holder_name, quantity, status)
           VALUES (?, ?, ?, ?, ?, ?)""",
        [
            (
                t["confirmation_id"],
                confirm_to_user.get(t["confirmation_id"]),
                t["show_id"],
                t["holder_name"],
                t["quantity"],
                t["status"],
            )
            for t in tickets_doc["tickets"]
        ],
    )
    cur.executemany(
        "INSERT INTO faq(id, title, answer, source_note, category_id) VALUES (?, ?, ?, ?, NULL)",
        [
            (row["id"], row["title"], row["answer"], row.get("source_note") or "")
            for row in faq
        ],
    )
    con.commit()
    con.close()
    print(
        "wrote",
        DB_PATH,
        "users",
        len(customers["users"]),
        "faq",
        len(faq),
        "shows",
        len(shows_doc["shows"]),
        "conversations/messages empty",
    )


if __name__ == "__main__":
    main()
