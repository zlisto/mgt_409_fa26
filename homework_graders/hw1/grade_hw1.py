#!/usr/bin/env python3
"""
HW1 autograder — Investor Due Diligence Extractor

Usage:
  python grade_hw1.py --submission path/to/hw1/ --pdf path/to/test.pdf --config path/to/config.json

Config JSON (example keys):
  {
    "numeric_fields": {
      "total_revenue_usd": 1250000000,
      "net_income_usd": 87000000
    },
    "numeric_tolerance_pct": 2.0,
    "must_be_null": ["yoy_revenue_growth_pct"],
    "risk_factor_min_count": 3,
    "company_name_contains": "Acme"
  }

Fill numeric_fields and must_be_null after you finalize the test PDFs.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    jsonschema = None

BASE_FIELDS = {
    "company_name": str,
    "fiscal_period": str,
    "total_revenue_usd": (int, float, type(None)),
    "net_income_usd": (int, float, type(None)),
    "yoy_revenue_growth_pct": (int, float, type(None)),
    "risk_factors": list,
    "management_outlook_one_sentence": str,
    "fields_not_found": list,
    "computed_metric": dict,
}

REQUIRED_PATHS = [
    "README.md",
    "extract.py",
    "requirements.txt",
    "schema.json",
    "prompts/pdf_extract.txt",
    "memo.md",
    "sample_output/public_extract.json",
]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def check_submission_layout(submission: Path) -> tuple[int, list[str]]:
    score = 10
    notes: list[str] = []
    for rel in REQUIRED_PATHS:
        if not (submission / rel).is_file():
            score -= 2
            notes.append(f"MISSING: {rel}")
    extract_py = submission / "extract.py"
    if not extract_py.is_file():
        notes.append("extract.py not found — cannot run CLI")
    return max(score, 0), notes


def run_extract(submission: Path, pdf: Path, out: Path) -> tuple[bool, str]:
    cmd = [sys.executable, str(submission / "extract.py"), "--pdf", str(pdf), "--out", str(out)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180, cwd=submission)
    except subprocess.TimeoutExpired:
        return False, "extract.py timed out after 180s"
    if result.returncode != 0:
        return False, f"extract.py exit {result.returncode}\n{result.stderr[:500]}"
    return True, ""


def type_ok(value, expected) -> bool:
    if isinstance(expected, tuple):
        return isinstance(value, expected)
    return isinstance(value, expected)


def check_base_fields(data: dict) -> tuple[int, list[str]]:
    score = 10
    notes: list[str] = []
    for key, typ in BASE_FIELDS.items():
        if key not in data:
            score -= 2
            notes.append(f"Missing base field: {key}")
            continue
        if not type_ok(data[key], typ):
            score -= 1
            notes.append(f"Wrong type for {key}: {type(data[key]).__name__}")
    if isinstance(data.get("risk_factors"), list) and len(data["risk_factors"]) < 3:
        score -= 2
        notes.append("risk_factors must have at least 3 items")
    cm = data.get("computed_metric")
    if isinstance(cm, dict):
        for k in ("name", "value", "formula"):
            if k not in cm:
                score -= 1
                notes.append(f"computed_metric missing {k}")
    else:
        score -= 2
    return max(score, 0), notes


def within_tolerance(actual, expected, tol_pct: float) -> bool:
    if actual is None or expected is None:
        return actual is None and expected is None
    if expected == 0:
        return abs(actual) <= tol_pct / 100.0
    return abs(actual - expected) / abs(expected) * 100 <= tol_pct


def check_numerics(data: dict, config: dict) -> tuple[int, list[str]]:
    score = 15
    notes: list[str] = []
    tol = config.get("numeric_tolerance_pct", 2.0)
    for field, expected in config.get("numeric_fields", {}).items():
        actual = data.get(field)
        if not within_tolerance(actual, expected, tol):
            score -= 5
            notes.append(f"{field}: expected ~{expected}, got {actual}")
    return max(score, 0), notes


def check_must_be_null(data: dict, config: dict) -> tuple[int, list[str]]:
    score = 10
    notes: list[str] = []
    not_found = set(data.get("fields_not_found") or [])
    for field in config.get("must_be_null", []):
        val = data.get(field)
        if val is not None:
            score -= 5
            notes.append(f"HALLUCINATION: {field} should be null, got {val}")
        if field not in not_found:
            score -= 2
            notes.append(f"{field} should be listed in fields_not_found")
    return max(score, 0), notes


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]{4,}", text.lower()))


def check_risk_grounding(data: dict, pdf_text: str, min_count: int = 3) -> tuple[int, list[str]]:
    score = 10
    notes: list[str] = []
    risks = data.get("risk_factors") or []
    if len(risks) < min_count:
        return 0, [f"Need {min_count} risk_factors"]
    pdf_tokens = tokenize(pdf_text)
    grounded = 0
    for r in risks:
        rt = tokenize(str(r))
        if rt & pdf_tokens:
            grounded += 1
    if grounded < min_count:
        score -= 5
        notes.append(f"Only {grounded}/{len(risks)} risk factors overlap PDF text")
    return score, notes


def extract_pdf_text(pdf: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    try:
        reader = PdfReader(str(pdf))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        return ""


def validate_schema(data: dict, schema_path: Path) -> tuple[bool, str]:
    if jsonschema is None:
        return True, "jsonschema not installed — skipped"
    schema = load_json(schema_path)
    try:
        jsonschema.validate(data, schema)
        return True, ""
    except jsonschema.ValidationError as e:
        return False, str(e.message)[:200]


def main() -> int:
    parser = argparse.ArgumentParser(description="Grade HW1 submission")
    parser.add_argument("--submission", required=True, help="Path to unzipped hw1/ folder")
    parser.add_argument("--pdf", required=True, help="Test PDF path")
    parser.add_argument("--config", required=True, help="Grader config JSON")
    parser.add_argument("--skip-run", action="store_true", help="Use existing JSON in --out instead of running extract.py")
    parser.add_argument("--out", default="", help="JSON output path (temp if running extract)")
    args = parser.parse_args()

    submission = Path(args.submission).resolve()
    pdf = Path(args.pdf).resolve()
    config = load_json(Path(args.config))

    total = 0
    all_notes: list[str] = []

    s, n = check_submission_layout(submission)
    total += s
    all_notes.extend(n)
    print(f"Layout: {s}/10")

    out_path = Path(args.out) if args.out else submission / "_grader_output.json"
    if not args.skip_run:
        ok, err = run_extract(submission, pdf, out_path)
        if not ok:
            print(f"RUN FAILED: {err}")
            print(f"TOTAL (partial): {total}/100")
            return 1
    if not out_path.is_file():
        print("No output JSON found")
        return 1

    data = load_json(out_path)
    schema_ok, schema_msg = validate_schema(data, submission / "schema.json")
    schema_score = 10 if schema_ok else 4
    if not schema_ok:
        all_notes.append(f"schema validation: {schema_msg}")
    total += schema_score
    print(f"Schema: {schema_score}/10")

    s, n = check_base_fields(data)
    total += s
    all_notes.extend(n)
    print(f"Base fields: {s}/10")

    # Public/hidden PDF tests — scale to 25 or 30 depending on config weight
    pdf_weight = config.get("pdf_test_points", 25)
    s_num, n_num = check_numerics(data, config)
    s_null, n_null = check_must_be_null(data, config)
    pdf_text = extract_pdf_text(pdf)
    s_risk, n_risk = check_risk_grounding(data, pdf_text, config.get("risk_factor_min_count", 3))

    raw_pdf = s_num + s_null + s_risk  # max ~35 internally
    pdf_score = min(pdf_weight, int(raw_pdf * pdf_weight / 35))
    total += pdf_score
    all_notes.extend(n_num + n_null + n_risk)
    print(f"PDF tests: {pdf_score}/{pdf_weight}")

    # computed_metric sanity
    cm_score = 5
    cm = data.get("computed_metric") or {}
    rev, ni = data.get("total_revenue_usd"), data.get("net_income_usd")
    if cm.get("name") and "margin" in cm.get("name", "").lower():
        if rev and ni is not None and cm.get("value") is not None:
            expected = ni / rev if rev else None
            if expected and cm["value"] is not None:
                if not within_tolerance(cm["value"], expected * 100 if cm["value"] > 1 else expected, 5):
                    cm_score -= 3
                    all_notes.append("computed_metric value inconsistent with formula")
    total += cm_score
    print(f"Computed metric: {cm_score}/5")

    print(f"\nAUTO TOTAL (memo 10 pts graded separately): {total}/90")
    if all_notes:
        print("\nNotes:")
        for note in all_notes:
            print(f"  - {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
