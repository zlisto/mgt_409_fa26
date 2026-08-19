# Practice decision scenario: Warehouse WMS vendor shortlist

**Role:** Ops lead at Harbor Collective (practice business)  
**Goal:** Recommend one warehouse management system (WMS) for a 20,000 sq ft regional DC.

## Options (use only these facts)

| Vendor | Annual license (USD) | Go-live (weeks) | API maturity | Notes |
|--------|----------------------|-----------------|--------------|-------|
| StackBay WMS | 48,000 | 10 | Strong REST + webhooks | Best integrator docs |
| ParcelOps | 36,000 | 6 | Limited REST | Fastest go-live; weak analytics |
| AtlasShelf | 62,000 | 14 | GraphQL + REST | Strong analytics; longest ramp |

## Constraints

1. Budget ceiling: **$50,000 / year** license (implementation labor is separate and out of scope).
2. Must go live in **≤ 12 weeks**.
3. Prefer strong API maturity when other constraints are met.

## Required output shape

Return JSON with:

- `matrix`: array of rows `{ "vendor", "annual_license_usd", "go_live_weeks", "meets_budget", "meets_timeline", "api_note", "score_1_to_5" }`
- `recommendation`: one vendor name
- `executive_summary`: ≤ 80 words explaining the tradeoff
- `rejected`: array of `{ "vendor", "reason" }` for options not chosen
