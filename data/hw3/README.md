# MGT 409 Homework 3 — Campus Customs inventory pack

Course data for **Homework 3: Campus Customs Product Search**.

## What’s in this pack

| Path | Contents |
|------|----------|
| `inventory.json` | Curated catalog of **20** Yale Bulldog Blue t-shirts/tops (SKU, name, price, colors, sizes, synthetic `qty_by_size`, product image path, source URL) |
| `products/*.jpg` | One product image per SKU (20 images) |
| `media/` | Customer video / stills for the video-search problems (see note below) |

## Important notes

- **Venue story:** Campus Customs (Yale merch). Images and list prices come from the public collection at [yalebulldogblue.com](https://yalebulldogblue.com/collections/clothing-t-shirts-tops) for teaching. This is **not** an official partnership and **not** live store inventory.
- **`qty_by_size` is synthetic** for the course. Do not treat it as real stock.
- **Customer media:** Drop your visit video/stills into `media/` (or use the files your instructor posts there). Typical filenames: `customer_ask.mp4`, `not_in_catalog.jpg`. If `media/` is still empty when you start, ask your instructor—do not scrape additional store pages for the assignment.

## Suggested layout after you unzip

```
hw3_data/
├── README.md
├── inventory.json
├── products/
│   └── *.jpg
└── media/
    ├── customer_ask.mp4      (instructor / visit capture)
    └── not_in_catalog.jpg    (optional; item not in this catalog)
```
