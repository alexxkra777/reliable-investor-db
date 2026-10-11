import copy

import pytest

from investordb.fetch import load_index
from investordb.grade import Checks, flat_row, grade_record
from investordb.verify import check_records


def rows_for(records, fixtures_dir):
    cache = fixtures_dir / "cache"
    return check_records(records, load_index(cache), cache)


def test_grade_a_with_verified_tier_a(records, fixtures_dir):
    g = grade_record(records[0], Checks(rows_for(records, fixtures_dir)))
    assert g["confidence"] == "A"
    assert g["last_investment_date"] == "2025-03-12"
    assert g["evidence"]["fields.ticket"] == "verified"


def test_missing_quote_does_not_count(records, fixtures_dir):
    rows = rows_for(records, fixtures_dir)
    # pretend the Tier A pages no longer contain the quotes
    for r in rows:
        if r["tier"] == "A":
            r["quote_status"] = "missing"
    g = grade_record(records[0], Checks(rows))
    assert g["existence_tier_a"] is False
    assert g["confidence"] == "C"  # only 1 company with Tier B, no Tier A
    assert g["evidence"]["fields.funds"] == "unsupported"


def test_value_not_in_quote_does_not_count(records, fixtures_dir):
    rows = rows_for(records, fixtures_dir)
    for r in rows:
        if r["target"] == "fields.funds":
            r["value_status"] = r["claim_value_status"] = "value_not_in_quote"
    g = grade_record(records[0], Checks(rows))
    # The other Tier A quote lacks the company name, so it cannot rescue this claim.
    assert g["confidence"] == "C"
    assert g["evidence"]["fields.funds"] == "unsupported"


def test_grade_b_needs_three_portfolio_companies(records):
    rec = copy.deepcopy(records[0])
    rec["fields"]["funds"] = None
    for inv in rec["investments"]:
        for s in inv["sources"]:
            s["tier"] = "B"
    checks = Checks(None)  # ignore verification
    assert grade_record(rec, checks)["confidence"] == "C"
    third = copy.deepcopy(rec["investments"][0])
    third["company"] = "Gamma Robotics"
    rec["investments"].append(third)
    g = grade_record(rec, checks)
    assert g["confidence"] == "B" and g["portfolio_count"] == 3


def test_tier_c_only_is_c(records):
    g = grade_record(records[2], Checks(None))
    assert g["confidence"] == "C"
    assert g["dated_investment_tier"] == "C"
    assert g["evidence"]["investments[0]"] == "unverified"


def test_stale_verification_row_is_ignored(records, fixtures_dir):
    rows = rows_for(records, fixtures_dir)
    for r in rows:
        r["url"] = "https://example.com/moved"
    assert grade_record(records[0], Checks(rows))["confidence"] == "C"


def test_flat_row(records, fixtures_dir):
    rec = records[0]
    g = grade_record(rec, Checks(rows_for(records, fixtures_dir)))
    row = flat_row(rec, g)
    assert row["sectors"] == "software;deeptech"
    assert row["ticket_min"] == "200000" and row["ticket_currency"] == "EUR"
    assert row["funds_source"] == "https://example.org/fof/portfolio"
    assert row["last_investment_source"] == "https://example.com/news/alpha"
    assert row["legal_entities"] == "ICO:12345678"
    assert row["confidence"] == "A"


def test_split_claim_counts_when_quotes_together_carry_the_values(records, fixtures_dir):
    rows = rows_for(records, fixtures_dir)
    for r in rows:
        if r["target"] == "fields.funds":
            # this one source alone lacks the number, but the claim as a whole is backed
            r["value_status"], r["claim_value_status"] = "value_not_in_quote", "ok"
    g = grade_record(records[0], Checks(rows))
    assert g["evidence"]["fields.funds"] != "unsupported"


def test_partial_claim_is_not_verified(records, fixtures_dir):
    rows = rows_for(records, fixtures_dir)
    for row in rows:
        if row["target"] == "investments[0]":
            row["claim_value_status"] = "partial"
    grade = grade_record(records[0], Checks(rows))
    assert grade["evidence"]["investments[0]"] == "unsupported"
    assert grade["last_investment_date"] != "2025-03-12"


@pytest.mark.parametrize("change", ["value", "quote", "tier", "other_source"])
def test_same_url_with_changed_evidence_is_not_reused(records, fixtures_dir, change):
    rows = rows_for(records, fixtures_dir)
    rec = copy.deepcopy(records[0])
    funds = rec["fields"]["funds"]
    if change == "value":
        funds["value"][0]["size"] = 999_000_000
    elif change == "quote":
        funds["sources"][0]["quote"] = "A different statement on the same page."
    elif change == "tier":
        funds["sources"][0]["tier"] = "A" if funds["sources"][0]["tier"] != "A" else "B"
    else:
        funds["sources"].append(dict(funds["sources"][0], url="https://example.org/new"))
    assert grade_record(rec, Checks(rows))["evidence"]["fields.funds"] == "unsupported"
