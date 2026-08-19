# MGT 409 Homework 4 — College Street Music Hall

Course data for **Homework 4: College Street Music Hall guest site**.

This is a class project using paraphrased public information. It is **not** an official venue document and **not** a partnership. **Do not** email, call, or otherwise contact the venue (or hotel partners).

Public site (context only): https://collegestreetmusichall.com/

## Use the SQLite file

Copy **`csmh.db`** into your project’s `backend/` folder. The running app should read and write this file (login, signup, FAQ, shows, tickets, chats). JSON files below are the same seed content, for inspection only.

## Tables in `csmh.db`

| Table | What’s in it |
|-------|----------------|
| `users` | Guest accounts: `username`, `display_name`, `password_salt`, `password_hash`. No plaintext passwords. Seeded with four demo users; your app also **inserts** new signups here. |
| `faq` | Policy entries (`id`, `title`, `answer`, `source_note`). `category_id` starts empty — fill in Problem 2. |
| `categories` | Empty until your categorize script writes rows. |
| `shows` | Sample calendar. |
| `tickets` | Fictional `CSMH-DEMO-*` confirmations, linked to `username`. |
| `conversations` | One row per chat thread (`username`, `title`, timestamps). Starts empty. |
| `messages` | Turns in a thread (`conversation_id`, `role`, `content`, `screenshot_used`, timestamp). Starts empty. |
| `meta` | `venue`, `address`, `password_algorithm`, `password_iterations`. |

## Other files

| File | Contents |
|------|----------|
| `faq.json` / `faq.md` | Same FAQ as the `faq` table |
| `shows.json` | Same shows as the `shows` table |
| `sample_tickets.json` | Same tickets as the `tickets` table |
| `customers.json` | Same users/hashes as the `users` table |

Policies on the live site may have changed. Graders score grounding against **this pack**.

## Demo logins (course-only)

Plaintext passwords are **not** in the database. Use these to test login:

- `alex.rivera` / `Boola2026!`
- `jordan.lee` / `NightOut!`
- `sam.patel` / `LcdNight1`
- `guest.walker` / `Showtime!`

Hashes are PBKDF2-HMAC-SHA256 (`meta.password_algorithm`, `meta.password_iterations`, per-user salt + hash). Lookup means hash what the guest typed and compare; do not store or return plaintext passwords.
