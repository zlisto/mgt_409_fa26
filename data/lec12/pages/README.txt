Lecture 12 — Scraper Trap pages
================================

Four fictional company webpages for the in-class prompt injection lab.

  maple_street_bakery.html       clean page (the control)
  maple_street_bakery_trap.html  same bakery + hidden 0px text that says the shop closed
  northwind_bikes.html           white-on-white text with zero-width characters + a fake recall
  harbor_dental.html             HTML comment + display:none block that tries to send your notes out

Open each page in a browser first. You will only see the normal website.
Your agent sees everything.

All companies are made up. The attacker URL uses the reserved .example domain,
and your fetch_url tool must only record URLs, never send real requests.
