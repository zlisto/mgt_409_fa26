"""Generate sample New Haven–area commercial lease PDFs for MGT 409 Lecture 2.

Instructor-only helper. Output PDFs are zipped for students; this script is
NOT included in sample_leases.zip.
"""
from __future__ import annotations

import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / "leases"
ZIP_PATH = ROOT / "sample_leases.zip"


@dataclass
class Lease:
    filename: str
    landlord: str
    tenant: str
    address_line: str  # full street + suite
    city_state_zip: str
    space_type: str
    sqft: int | None
    annual_base_rent: float | None
    rent_per_sqft: float | None
    lease_structure: str | None  # Triple Net (NNN) / Gross / Modified Gross
    commencement: str | None  # e.g. January 1, 2024
    expiration: str | None
    security_deposit: float | None
    permitted_use: str
    incomplete: bool = False
    missing_fields: list[str] = field(default_factory=list)
    letterhead_tagline: str = "Commercial Real Estate · New Haven, Connecticut"
    # formal | deal_memo | rent_schedule | broker_cover
    layout: str = "formal"

    @property
    def full_address(self) -> str:
        return f"{self.address_line}, {self.city_state_zip}"


LEASES: list[Lease] = [
    Lease(
        filename="01_harborview_biotech_chapel.pdf",
        landlord="Harborview Realty Partners LLC",
        tenant="Elm City Biotech Labs, Inc.",
        address_line="300 George Street, Suite 420",
        city_state_zip="New Haven, CT 06511",
        space_type="Office / Laboratory",
        sqft=8_450,
        annual_base_rent=380_250.00,
        rent_per_sqft=45.00,
        lease_structure="Triple Net (NNN)",
        commencement="March 1, 2023",
        expiration="February 28, 2028",
        security_deposit=95_062.50,
        permitted_use=(
            "Research and development laboratory operations, related office "
            "use, and ancillary storage of non-hazardous materials, subject "
            "to all applicable laws and building rules."
        ),
        letterhead_tagline="Harborview Realty · Asset Management",
    ),
    Lease(
        filename="02_whitney_corridor_retail.pdf",
        landlord="Whitney Corridor Holdings LLC",
        tenant="Quinnipiac Coffee Roasters LLC",
        address_line="1156 Whitney Avenue, Suite 1",
        city_state_zip="Hamden, CT 06517",
        space_type="Retail",
        sqft=2_200,
        annual_base_rent=72_600.00,
        rent_per_sqft=33.00,
        lease_structure="Modified Gross",
        commencement="June 15, 2022",
        expiration="June 14, 2027",
        security_deposit=12_100.00,
        permitted_use=(
            "Retail sale of coffee, tea, baked goods, and related merchandise; "
            "limited on-premises consumption seating not to exceed twenty (20) seats."
        ),
        letterhead_tagline="Whitney Corridor Holdings · Greater New Haven Retail",
        layout="deal_memo",
    ),
    Lease(
        filename="03_long_wharf_industrial.pdf",
        landlord="Long Wharf Industrial Trust",
        tenant="Shoreline Logistics & Fulfillment Co.",
        address_line="100 Long Wharf Drive, Building B, Suite 12",
        city_state_zip="New Haven, CT 06511",
        space_type="Industrial / Warehouse",
        sqft=24_000,
        annual_base_rent=288_000.00,
        rent_per_sqft=12.00,
        lease_structure="Triple Net (NNN)",
        commencement="October 1, 2021",
        expiration="September 30, 2031",
        security_deposit=72_000.00,
        permitted_use=(
            "Warehousing, light assembly, order fulfillment, and distribution "
            "of consumer goods; truck loading and staging as shown on Exhibit A."
        ),
        letterhead_tagline="Long Wharf Industrial Trust · New Haven Harbor",
    ),
    Lease(
        filename="04_orange_street_professional.pdf",
        landlord="Orange Street Office Partners LP",
        tenant="Mill River Accounting Group PC",
        address_line="59 Elm Street, Suite 300",
        city_state_zip="New Haven, CT 06510",
        space_type="Office",
        sqft=4_100,
        annual_base_rent=143_500.00,
        rent_per_sqft=35.00,
        lease_structure="Gross",
        commencement="January 1, 2024",
        expiration="December 31, 2029",
        security_deposit=23_916.67,
        permitted_use=(
            "General professional office use for certified public accounting "
            "and related advisory services. No retail walk-in traffic."
        ),
        letterhead_tagline="Orange Street Office Partners · Downtown New Haven",
        layout="rent_schedule",
    ),
    Lease(
        filename="05_westville_medical_retail.pdf",
        landlord="Westville Square Properties LLC",
        tenant="Yale-New Haven Area Dental Care PLLC",
        address_line="960 Whalley Avenue, Suite 2B",
        city_state_zip="New Haven, CT 06515",
        space_type="Medical / Retail",
        sqft=1_850,
        annual_base_rent=74_000.00,
        rent_per_sqft=40.00,
        lease_structure="Modified Gross",
        commencement="August 1, 2023",
        expiration="July 31, 2028",
        security_deposit=18_500.00,
        permitted_use=(
            "Outpatient dental practice and related administrative offices, "
            "including patient waiting areas and sterilization rooms."
        ),
        letterhead_tagline="Westville Square Properties · Whalley Corridor",
    ),
    Lease(
        filename="06_science_park_office.pdf",
        landlord="Science Park Redevelopment LLC",
        tenant="Northside Software Systems, Inc.",
        address_line="25 Science Park, Suite 410",
        city_state_zip="New Haven, CT 06511",
        space_type="Office",
        sqft=6_750,
        annual_base_rent=270_000.00,
        rent_per_sqft=40.00,
        lease_structure="Triple Net (NNN)",
        commencement="May 1, 2022",
        expiration="April 30, 2027",
        security_deposit=67_500.00,
        permitted_use=(
            "Software development, customer support, and general administrative "
            "office use. No manufacturing or wet laboratory activity."
        ),
        letterhead_tagline="Science Park Redevelopment · Innovation District",
        layout="broker_cover",
    ),
    Lease(
        filename="07_chapel_west_boutique.pdf",
        landlord="Chapel West Retail Collective LLC",
        tenant="East Rock Outdoor Apparel LLC",
        address_line="910 Chapel Street, Suite A",
        city_state_zip="New Haven, CT 06510",
        space_type="Retail",
        sqft=1_420,
        annual_base_rent=63_900.00,
        rent_per_sqft=45.00,
        lease_structure="Gross",
        commencement="November 1, 2023",
        expiration="October 31, 2026",
        security_deposit=10_650.00,
        permitted_use=(
            "Retail sale of apparel, footwear, and outdoor recreational goods; "
            "occasional in-store promotional events with Landlord prior written consent."
        ),
        letterhead_tagline="Chapel West Retail Collective · Downtown Core",
    ),
    Lease(
        filename="08_milford_flex_space.pdf",
        landlord="Connecticut Shoreline Flex LLC",
        tenant="Amity Precision Components LLC",
        address_line="350 Woodmont Road, Suite 7",
        city_state_zip="Milford, CT 06460",
        space_type="Flex / Light Industrial",
        sqft=11_200,
        annual_base_rent=168_000.00,
        rent_per_sqft=15.00,
        lease_structure="Triple Net (NNN)",
        commencement="February 15, 2024",
        expiration="February 14, 2029",
        security_deposit=42_000.00,
        permitted_use=(
            "Light manufacturing, quality inspection, and related office and "
            "warehouse use for precision metal and polymer components."
        ),
        letterhead_tagline="Connecticut Shoreline Flex · Greater New Haven",
        layout="short_form",
    ),
    # Incomplete: missing Security Deposit and Rent per SqFt
    Lease(
        filename="09_state_street_amendment.pdf",
        landlord="State Street Commercial LLC",
        tenant="New Haven Kitchen Supply Co.",
        address_line="195 State Street, Suite 2",
        city_state_zip="New Haven, CT 06510",
        space_type="Retail / Showroom",
        sqft=3_600,
        annual_base_rent=108_000.00,
        rent_per_sqft=None,
        lease_structure="Modified Gross",
        commencement="April 1, 2021",
        expiration="March 31, 2026",
        security_deposit=None,
        permitted_use=(
            "Retail showroom and wholesale sales of kitchen equipment and "
            "related housewares to trade customers and the general public."
        ),
        incomplete=True,
        missing_fields=["security_deposit", "rent_per_sqft"],
        letterhead_tagline="State Street Commercial · FIRST AMENDMENT (unsigned draft)",
    ),
    # Incomplete: missing Expiration Date and Lease Structure label/value
    Lease(
        filename="10_branford_office_draft.pdf",
        landlord="Branford Harbor Partners LLC",
        tenant="Soundview Maritime Advisors LLC",
        address_line="48 Montowese Street, Suite 210",
        city_state_zip="Branford, CT 06405",
        space_type="Office",
        sqft=2_950,
        annual_base_rent=88_500.00,
        rent_per_sqft=30.00,
        lease_structure=None,
        commencement="September 1, 2024",
        expiration=None,
        security_deposit=14_750.00,
        permitted_use=(
            "Professional office use for maritime consulting and brokerage "
            "services. Client meetings by appointment only."
        ),
        incomplete=True,
        missing_fields=["expiration_date", "lease_structure"],
        letterhead_tagline="Branford Harbor Partners · WORKING DRAFT — terms TBD",
    ),
]


def _styles(layout: str = "formal"):
    base = getSampleStyleSheet()
    if layout in ("deal_memo", "broker_cover", "short_form"):
        body_font, bold_font = "Helvetica", "Helvetica-Bold"
        italic_font = "Helvetica-Oblique"
        body_size = 9.5
    else:
        body_font, bold_font = "Times-Roman", "Times-Bold"
        italic_font = "Times-Italic"
        body_size = 10
    styles = {
        "letterhead": ParagraphStyle(
            "Letterhead",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=13 if layout != "broker_cover" else 11,
            alignment=TA_CENTER if layout != "broker_cover" else TA_LEFT,
            spaceAfter=2,
        ),
        "tagline": ParagraphStyle(
            "Tagline",
            parent=base["Normal"],
            fontName=italic_font,
            fontSize=9,
            alignment=TA_CENTER if layout != "broker_cover" else TA_LEFT,
            spaceAfter=10,
        ),
        "title": ParagraphStyle(
            "DocTitle",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=12,
            alignment=TA_CENTER,
            spaceBefore=6,
            spaceAfter=12,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName=body_font,
            fontSize=body_size,
            leading=body_size + 3,
            alignment=TA_JUSTIFY if layout == "formal" else TA_LEFT,
            spaceAfter=8,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=10,
            spaceBefore=8,
            spaceAfter=4,
            alignment=TA_LEFT,
        ),
        "field": ParagraphStyle(
            "Field",
            parent=base["Normal"],
            fontName=body_font,
            fontSize=body_size,
            leading=body_size + 3,
            leftIndent=0 if layout in ("deal_memo", "rent_schedule") else 12,
            spaceAfter=3,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName=body_font,
            fontSize=9,
            leading=12,
            alignment=TA_LEFT,
            spaceAfter=2,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName=italic_font,
            fontSize=8,
            alignment=TA_CENTER,
            spaceBefore=16,
        ),
    }
    return styles


def _money(amount: float) -> str:
    return f"${amount:,.2f}"


def _parties_line(lease: Lease) -> str:
    return (
        f"<b>Landlord Name:</b> {lease.landlord}<br/>"
        f"<b>Tenant Name:</b> {lease.tenant}"
    )


def _field_blocks(lease: Lease, styles) -> list:
    """Shared field lines — labels must match verify_sample_leases.py."""
    blocks = []
    blocks.append(Paragraph(f"<b>Full Street Address:</b> {lease.full_address}", styles["field"]))
    blocks.append(Paragraph(f"<b>Space Type:</b> {lease.space_type}", styles["field"]))
    if lease.sqft is not None:
        blocks.append(
            Paragraph(f"<b>Rentable Square Footage:</b> {lease.sqft:,} sqft", styles["field"])
        )
    if lease.annual_base_rent is not None:
        blocks.append(
            Paragraph(
                f"<b>Annual Base Rent:</b> {_money(lease.annual_base_rent)}",
                styles["field"],
            )
        )
    if lease.rent_per_sqft is not None:
        blocks.append(
            Paragraph(
                f"<b>Rent per SqFt:</b> {_money(lease.rent_per_sqft)} /sqft",
                styles["field"],
            )
        )
    elif "rent_per_sqft" in lease.missing_fields:
        blocks.append(
            Paragraph(
                "<i>[Unit rent rate not stated in this draft — to be confirmed by Landlord.]</i>",
                styles["field"],
            )
        )
    if lease.lease_structure is not None:
        blocks.append(
            Paragraph(f"<b>Lease Structure:</b> {lease.lease_structure}", styles["field"])
        )
    elif "lease_structure" in lease.missing_fields:
        blocks.append(
            Paragraph(
                "<i>[Expense structure blank / under negotiation — Gross vs. NNN TBD.]</i>",
                styles["field"],
            )
        )
    if lease.commencement is not None:
        blocks.append(
            Paragraph(f"<b>Commencement Date:</b> {lease.commencement}", styles["field"])
        )
    if lease.expiration is not None:
        blocks.append(
            Paragraph(f"<b>Expiration Date:</b> {lease.expiration}", styles["field"])
        )
    elif "expiration_date" in lease.missing_fields:
        blocks.append(
            Paragraph(
                "<i>[Term end date intentionally omitted / term length not yet agreed.]</i>",
                styles["field"],
            )
        )
    if lease.security_deposit is not None:
        blocks.append(
            Paragraph(f"<b>Security Deposit:</b> {_money(lease.security_deposit)}", styles["field"])
        )
    elif "security_deposit" in lease.missing_fields:
        blocks.append(
            Paragraph(
                "<i>[Deposit amount not specified in this amendment package.]</i>",
                styles["field"],
            )
        )
    blocks.append(
        Paragraph(
            f"<b>Permitted Use / Business Description:</b> {lease.permitted_use}",
            styles["field"],
        )
    )
    return blocks


def _structure_blurb(lease: Lease, styles) -> list:
    out = []
    if lease.lease_structure and "NNN" in lease.lease_structure:
        out.append(
            Paragraph(
                "Under this Triple Net (NNN) Lease, Tenant shall pay its proportionate share of "
                "real estate taxes, building insurance, and common area maintenance (CAM).",
                styles["body"],
            )
        )
    elif lease.lease_structure == "Gross":
        out.append(
            Paragraph(
                "Under this Gross Lease, Base Rent is inclusive of Landlord’s share of taxes, "
                "insurance, and standard CAM for the Building, except as otherwise provided.",
                styles["body"],
            )
        )
    elif lease.lease_structure == "Modified Gross":
        out.append(
            Paragraph(
                "Under this Modified Gross Lease, Landlord and Tenant share certain operating "
                "expenses as set forth in Exhibit B (expense stop and exclusions).",
                styles["body"],
            )
        )
    elif "lease_structure" in lease.missing_fields:
        out.append(
            Paragraph(
                "Operating expense allocation between Landlord and Tenant has not been finalized "
                "in this working draft.",
                styles["body"],
            )
        )
    return out


def _footer_bits(lease: Lease, styles) -> list:
    return [
        Spacer(1, 14),
        Paragraph(
            f"Landlord: {lease.landlord} ________________________ Date: __________",
            styles["field"],
        ),
        Paragraph(
            f"Tenant: {lease.tenant} ________________________ Date: __________",
            styles["field"],
        ),
        Paragraph(
            "Sample teaching document — Yale SOM MGT 409 · fictional parties and terms",
            styles["footer"],
        ),
    ]


def _build_formal(lease: Lease, styles) -> list:
    story = []
    story.append(Paragraph(lease.landlord.upper(), styles["letterhead"]))
    story.append(Paragraph(lease.letterhead_tagline, styles["tagline"]))
    story.append(
        Paragraph(
            "COMMERCIAL LEASE AGREEMENT"
            + (" (PARTIAL / DRAFT)" if lease.incomplete else ""),
            styles["title"],
        )
    )
    story.append(
        Paragraph(
            f"This Commercial Lease Agreement (the “Lease”) is entered into by and between "
            f"<b>Landlord Name:</b> {lease.landlord} (“Landlord”) and "
            f"<b>Tenant Name:</b> {lease.tenant} (“Tenant”).",
            styles["body"],
        )
    )
    story.append(Paragraph("1. Premises", styles["section"]))
    story.extend(_field_blocks(lease, styles)[:3])  # address, space, sqft
    story.append(
        Paragraph(
            "Landlord hereby leases to Tenant the Premises described above, together with "
            "reasonable non-exclusive use of common areas, subject to the terms of this Lease.",
            styles["body"],
        )
    )
    story.append(Paragraph("2. Rent and Lease Structure", styles["section"]))
    rest = _field_blocks(lease, styles)
    skip = 2 + (1 if lease.sqft is not None else 0)
    story.extend(rest[skip:])
    story.extend(_structure_blurb(lease, styles))
    story.append(Paragraph("3. Miscellaneous", styles["section"]))
    story.append(
        Paragraph(
            "This Lease constitutes the entire agreement of the parties with respect to the "
            "Premises and supersedes all prior negotiations. Governing law: State of Connecticut.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "IN WITNESS WHEREOF, Landlord and Tenant have executed this Lease as of the "
            "Commencement Date (or the date of the last signature below).",
            styles["body"],
        )
    )
    story.extend(_footer_bits(lease, styles))
    return story


def _build_deal_memo(lease: Lease, styles) -> list:
    """Broker-style one-pager: KEY BUSINESS TERMS box, then short prose."""
    story = []
    story.append(Paragraph("CONFIDENTIAL — LEASE DEAL MEMO", styles["letterhead"]))
    story.append(Paragraph(lease.letterhead_tagline, styles["tagline"]))
    story.append(Paragraph("KEY BUSINESS TERMS (EXECUTED SUMMARY)", styles["title"]))
    story.append(Paragraph(_parties_line(lease), styles["field"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("ECONOMICS & PREMISES", styles["section"]))
    story.extend(_field_blocks(lease, styles))
    story.extend(_structure_blurb(lease, styles))
    story.append(Paragraph("NOTES", styles["section"]))
    story.append(
        Paragraph(
            "This deal memo summarizes the executed commercial lease for asset-management "
            "intake. Full legal form is on file with Landlord’s counsel. Governing law: Connecticut.",
            styles["body"],
        )
    )
    story.extend(_footer_bits(lease, styles))
    return story


def _build_rent_schedule(lease: Lease, styles) -> list:
    """Office lease with Schedule A rent table look (still plain paragraphs for extractability)."""
    story = []
    story.append(Paragraph(lease.landlord.upper(), styles["letterhead"]))
    story.append(Paragraph("OFFICE LEASE — SCHEDULE A (RENT & PREMISES)", styles["title"]))
    story.append(
        Paragraph(
            f"Parties: <b>Landlord Name:</b> {lease.landlord}; "
            f"<b>Tenant Name:</b> {lease.tenant}.",
            styles["body"],
        )
    )
    story.append(Paragraph("SCHEDULE A — BASIC LEASE INFORMATION", styles["section"]))
    story.append(
        Paragraph(
            "<i>The following Basic Lease Information is incorporated into the Lease. "
            "If any conflict arises, the body of the Lease controls except for dollar amounts below.</i>",
            styles["body"],
        )
    )
    # Present as labeled rows (table-like)
    for p in _field_blocks(lease, styles):
        story.append(p)
        story.append(Spacer(1, 2))
    story.extend(_structure_blurb(lease, styles))
    story.append(Paragraph("INCORPORATION", styles["section"]))
    story.append(
        Paragraph(
            "Tenant acknowledges receipt of the Lease and this Schedule A. Notices to the "
            "addresses above. Governing law: State of Connecticut.",
            styles["body"],
        )
    )
    story.extend(_footer_bits(lease, styles))
    return story


def _build_broker_cover(lease: Lease, styles) -> list:
    """Looks like a leasing-agent cover sheet / email printout."""
    story = []
    story.append(Paragraph("NEW HAVEN LEASING DESK — EXECUTED LEASE COVER SHEET", styles["letterhead"]))
    story.append(Paragraph(lease.letterhead_tagline, styles["tagline"]))
    story.append(Paragraph("<b>FROM:</b> Asset Management / Lease Admin", styles["meta"]))
    story.append(Paragraph("<b>TO:</b> Portfolio file · New Haven CRE book", styles["meta"]))
    story.append(
        Paragraph(
            f"<b>RE:</b> Fully executed lease — {lease.tenant} @ {lease.address_line}",
            styles["meta"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(Paragraph("PARTY IDENTIFICATION", styles["section"]))
    story.append(Paragraph(_parties_line(lease), styles["field"]))
    story.append(Paragraph("EXTRACTED LEASE FACTS (FOR CRM / DASHBOARD)", styles["section"]))
    story.extend(_field_blocks(lease, styles))
    story.extend(_structure_blurb(lease, styles))
    story.append(
        Paragraph(
            "Please upload these facts to the portfolio system. Do not redistribute outside the firm.",
            styles["body"],
        )
    )
    story.extend(_footer_bits(lease, styles))
    return story


def _build_short_form(lease: Lease, styles) -> list:
    """Compact industrial short-form lease — different section titles, same field labels."""
    story = []
    story.append(Paragraph(lease.landlord.upper(), styles["letterhead"]))
    story.append(Paragraph(lease.letterhead_tagline, styles["tagline"]))
    story.append(Paragraph("SHORT-FORM COMMERCIAL LEASE", styles["title"]))
    story.append(
        Paragraph(
            f"<b>Landlord Name:</b> {lease.landlord}<br/>"
            f"<b>Tenant Name:</b> {lease.tenant}<br/>"
            "The parties agree to the following short-form terms. Additional riders, if any, are attached.",
            styles["body"],
        )
    )
    story.append(Paragraph("A. LOCATION & USE", styles["section"]))
    blocks = _field_blocks(lease, styles)
    # address, space, sqft, ... use is last
    story.extend(blocks[:3])
    story.append(blocks[-1])  # permitted use early
    story.append(Paragraph("B. MONEY TERMS", styles["section"]))
    story.extend(blocks[3:-1])  # rent through deposit
    story.extend(_structure_blurb(lease, styles))
    story.append(Paragraph("C. ACCEPTANCE", styles["section"]))
    story.append(
        Paragraph(
            "Tenant accepts the Premises “as is” except for latent structural defects. "
            "Governing law: Connecticut. Counterparts permitted.",
            styles["body"],
        )
    )
    story.extend(_footer_bits(lease, styles))
    return story


def build_pdf(lease: Lease, path: Path) -> None:
    styles = _styles(lease.layout)
    margins = {
        "formal": (0.85, 0.85, 0.7, 0.7),
        "deal_memo": (0.7, 0.7, 0.6, 0.6),
        "rent_schedule": (0.75, 0.75, 0.65, 0.65),
        "broker_cover": (0.65, 0.65, 0.55, 0.55),
        "short_form": (0.8, 0.8, 0.65, 0.65),
    }
    lm, rm, tm, bm = margins.get(lease.layout, margins["formal"])
    doc = SimpleDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=lm * inch,
        rightMargin=rm * inch,
        topMargin=tm * inch,
        bottomMargin=bm * inch,
        title=f"Commercial Lease — {lease.tenant}",
        author=lease.landlord,
    )
    builders = {
        "formal": _build_formal,
        "deal_memo": _build_deal_memo,
        "rent_schedule": _build_rent_schedule,
        "broker_cover": _build_broker_cover,
        "short_form": _build_short_form,
    }
    story = builders.get(lease.layout, _build_formal)(lease, styles)
    doc.build(story)


def generate_all() -> list[Path]:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for lease in LEASES:
        out = PDF_DIR / lease.filename
        build_pdf(lease, out)
        paths.append(out)
        print(f"Wrote {out.name}")
    return paths


def write_zip(pdf_paths: list[Path]) -> Path:
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in pdf_paths:
            # Flat folder of PDFs inside the zip for easy student extraction
            zf.write(p, arcname=f"sample_leases/{p.name}")
    print(f"Wrote {ZIP_PATH}")
    return ZIP_PATH


def print_summary() -> None:
    print("\n=== Lease summary ===")
    print(f"{'#':<3} {'Tenant':<42} {'Address':<48} {'Status'}")
    print("-" * 120)
    for i, lease in enumerate(LEASES, 1):
        status = (
            f"INCOMPLETE (missing: {', '.join(lease.missing_fields)})"
            if lease.incomplete
            else "complete"
        )
        print(
            f"{i:<3} {lease.tenant[:41]:<42} {lease.full_address[:47]:<48} {status}"
        )


def main() -> None:
    paths = generate_all()
    write_zip(paths)
    print_summary()


if __name__ == "__main__":
    main()
