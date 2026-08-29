"""Verify lec02 sample lease PDFs extract as selectable text with expected fields.

Run after build_sample_leases.py. Asserts 8 complete leases contain all required
labels/values and 2 incomplete leases omit the intended fields.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / "leases"

# Import lease definitions from the builder (same folder).
sys.path.insert(0, str(ROOT))
from build_sample_leases import LEASES  # noqa: E402

REQUIRED_LABELS_COMPLETE = [
    "Tenant Name:",
    "Landlord Name:",
    "Full Street Address:",
    "Space Type:",
    "Rentable Square Footage:",
    "Annual Base Rent:",
    "Rent per SqFt:",
    "Lease Structure:",
    "Commencement Date:",
    "Expiration Date:",
    "Security Deposit:",
    "Permitted Use / Business Description:",
]


def extract_text(path: Path) -> str:
    chunks: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            chunks.append(t)
    return "\n".join(chunks)


def assert_contains(text: str, needle: str, context: str) -> None:
    if needle not in text:
        raise AssertionError(f"{context}: missing expected text {needle!r}")


def assert_missing(text: str, needle: str, context: str) -> None:
    if needle in text:
        raise AssertionError(f"{context}: expected to omit {needle!r} but found it")


def verify_one(lease) -> None:
    path = PDF_DIR / lease.filename
    if not path.exists():
        raise FileNotFoundError(path)
    text = extract_text(path)
    if len(text.strip()) < 200:
        raise AssertionError(f"{lease.filename}: extracted text too short ({len(text)} chars)")

    # Always present identity / premises / use
    assert_contains(text, "Tenant Name:", lease.filename)
    assert_contains(text, lease.tenant, lease.filename)
    assert_contains(text, "Landlord Name:", lease.filename)
    assert_contains(text, lease.landlord, lease.filename)
    assert_contains(text, "Full Street Address:", lease.filename)
    assert_contains(text, lease.address_line, lease.filename)
    assert_contains(text, lease.city_state_zip, lease.filename)
    assert_contains(text, "Space Type:", lease.filename)
    assert_contains(text, lease.space_type, lease.filename)
    assert_contains(text, "Permitted Use / Business Description:", lease.filename)

    if lease.incomplete:
        if "security_deposit" in lease.missing_fields:
            assert_missing(text, "Security Deposit:", lease.filename)
            assert_contains(text, "Deposit amount not specified", lease.filename)
        if "rent_per_sqft" in lease.missing_fields:
            assert_missing(text, "Rent per SqFt:", lease.filename)
            assert_contains(text, "Unit rent rate not stated", lease.filename)
        if "expiration_date" in lease.missing_fields:
            assert_missing(text, "Expiration Date:", lease.filename)
            assert_contains(text, "Term end date intentionally omitted", lease.filename)
        if "lease_structure" in lease.missing_fields:
            assert_missing(text, "Lease Structure:", lease.filename)
            assert_contains(text, "Expense structure blank", lease.filename)
    else:
        for label in REQUIRED_LABELS_COMPLETE:
            assert_contains(text, label, lease.filename)
        assert lease.sqft is not None
        assert_contains(text, f"{lease.sqft:,} sqft", lease.filename)
        assert lease.annual_base_rent is not None
        assert_contains(text, f"${lease.annual_base_rent:,.2f}", lease.filename)
        assert lease.rent_per_sqft is not None
        assert_contains(text, f"${lease.rent_per_sqft:,.2f} /sqft", lease.filename)
        assert lease.lease_structure is not None
        assert_contains(text, lease.lease_structure, lease.filename)
        assert lease.commencement is not None
        assert_contains(text, lease.commencement, lease.filename)
        assert lease.expiration is not None
        assert_contains(text, lease.expiration, lease.filename)
        assert lease.security_deposit is not None
        assert_contains(text, f"${lease.security_deposit:,.2f}", lease.filename)


def main() -> None:
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if len(pdfs) != 10:
        raise AssertionError(f"Expected 10 PDFs in {PDF_DIR}, found {len(pdfs)}")

    complete = [L for L in LEASES if not L.incomplete]
    incomplete = [L for L in LEASES if L.incomplete]
    if len(complete) != 8 or len(incomplete) != 2:
        raise AssertionError("Expected 8 complete and 2 incomplete lease definitions")

    for lease in LEASES:
        verify_one(lease)
        status = "INCOMPLETE" if lease.incomplete else "OK"
        print(f"PASS [{status}] {lease.filename}")

    print("\n=== Verification summary ===")
    print(f"{'#':<3} {'Tenant':<42} {'Status'}")
    print("-" * 80)
    for i, lease in enumerate(LEASES, 1):
        if lease.incomplete:
            status = f"incomplete - missing {', '.join(lease.missing_fields)}"
        else:
            status = "complete"
        print(f"{i:<3} {lease.tenant[:41]:<42} {status}")

    print("\nAll verification checks passed.")


if __name__ == "__main__":
    main()
