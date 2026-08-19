"""Build HW3 inventory pack from Yale Bulldog Blue public collection JSON."""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "products"
IMG.mkdir(parents=True, exist_ok=True)

SIZES = ["XS", "S", "M", "L", "XL", "XXL"]


def fake_qty(sku: str, size: str) -> int:
    h = sum(ord(c) for c in (sku + size))
    if h % 7 == 0:
        return 0
    return 1 + (h % 8)


def main() -> None:
    products: list[dict] = []
    seen: set[str] = set()
    for page in range(1, 6):
        url = (
            "https://yalebulldogblue.com/collections/clothing-t-shirts-tops/"
            f"products.json?page={page}&limit=24"
        )
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        for pr in data.get("products", []):
            handle = pr.get("handle")
            if not handle or handle in seen:
                continue
            seen.add(handle)
            pid = str(pr.get("id"))
            title = pr.get("title") or handle
            variants = pr.get("variants") or []
            prices = [float(v.get("price")) for v in variants if v.get("price") is not None]
            price = min(prices) if prices else None
            colors: set[str] = set()
            sizes: set[str] = set()
            for v in variants:
                for key in ("option1", "option2", "option3"):
                    val = v.get(key)
                    if not val or val == "Default Title":
                        continue
                    up = val.upper().replace("2XL", "XXL")
                    if up in SIZES or up in {"3XL", "4XL"}:
                        sizes.add(up if up in SIZES else up)
                    else:
                        colors.add(val)
            if not sizes:
                sizes = set(SIZES[:4])
            if not colors:
                colors = {"Navy"}
            images = pr.get("images") or []
            img_url = images[0].get("src") if images else None
            if not img_url and pr.get("image"):
                img_url = pr["image"].get("src")
            slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", handle)[:80]
            local_name = f"{slug}.jpg"
            local_path = IMG / local_name
            if img_url and not local_path.exists():
                try:
                    req = urllib.request.Request(
                        img_url, headers={"User-Agent": "MGT409-course-pack/1.0"}
                    )
                    with urllib.request.urlopen(req, timeout=60) as ir:
                        local_path.write_bytes(ir.read())
                    time.sleep(0.12)
                except Exception as e:
                    print("IMG FAIL", handle, e)
                    local_name = None
            elif not img_url:
                local_name = None
            qty = {s: fake_qty(pid, s) for s in sorted(sizes)}
            tags = pr.get("tags")
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]
            products.append(
                {
                    "sku": f"YBB-{pid[-6:]}",
                    "handle": handle,
                    "name": title,
                    "price_usd": price,
                    "colors": sorted(colors),
                    "sizes": sorted(sizes, key=lambda s: SIZES.index(s) if s in SIZES else 99),
                    "qty_by_size": qty,
                    "image": f"products/{local_name}" if local_name else None,
                    "source_url": f"https://yalebulldogblue.com/products/{handle}",
                    "vendor": pr.get("vendor"),
                    "product_type": pr.get("product_type"),
                    "tags": tags or [],
                }
            )
            print(f"page {page}: {title} (${price})")

    inventory = {
        "store": "Campus Customs / Yale Bulldog Blue",
        "store_url": "https://yalebulldogblue.com/",
        "collection_url": "https://yalebulldogblue.com/collections/clothing-t-shirts-tops",
        "note": (
            "Course inventory pack for MGT 409 Homework 3. Prices and images from the public "
            "t-shirt collection for teaching. qty_by_size is synthetic course stock, not live "
            "store inventory. Not an official partnership."
        ),
        "products": products,
    }
    (ROOT / "inventory.json").write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    print("TOTAL", len(products), "images", len(list(IMG.glob("*.jpg"))))


if __name__ == "__main__":
    main()
