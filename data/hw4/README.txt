MGT 409 — Homework 4 data pack
==============================

Download data.zip and unzip it next to your hw4 project folder so you have:

  data/campus_customs.db   SQLite: catalogue, inventory, users
  data/products/           Product images (paths match the catalogue table)

Test user (password is hashed in the DB):
  email:    test@campuscustoms.yale.edu
  password: password

Image paths in the database look like:
  products/basic-hoodie-big-yale.jpg

Your app should serve/read them from data/products/…

Do NOT commit the database or product images to GitHub.
Graders clone your public repo and drop this pack in locally using the same paths.

Use Python’s built-in sqlite3 module to read the .db file.
