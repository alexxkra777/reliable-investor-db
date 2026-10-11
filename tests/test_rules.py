import copy
from datetime import date

import pytest

from investordb.rules import (
    agreement,
    decide,
    load_negative_list,
    months_back,
    months_between,
)

REF = date(2026, 10, 11)


def with_last_investment(rec: dict, d: str, tier: str = "B") -> dict:
    rec = copy.deepcopy(rec)
    inv = copy.deepcopy(rec["investments"][0])
    inv["date"] = d
    inv["sources"][0]["tier"] = tier
    rec["investments"] = [inv]
    return rec


def test_months_back_clamps_month_end():
    assert months_back(date(2026, 10, 11), 36) == date(2023, 10, 11)
    assert months_back(date(2028, 2, 29), 36) == date(2025, 2, 28)
    assert months_back(date(2026, 5, 31), 1) == date(2026, 4, 30)
    assert months_between(date(2023, 10, 11), REF) == 36
    assert months_between(date(2023, 10, 12), REF) == 35


def test_recency_boundary(example):
    # exactly 36 months back still counts as recent
    on_edge = with_last_investment(example, "2023-10-11")
    assert decide(on_edge, {}, REF).status == "included"
    # one day older is dormant
    too_old = with_last_investment(example, "2023-10-10")
    d = decide(too_old, {}, REF)
    assert d.status == "dormant" and d.rules == ["E4"]


def test_window_is_configurable(example):
    rec = with_last_investment(example, "2024-10-10")
    assert decide(rec, {}, REF, window_months=24).status == "dormant"
    assert decide(rec, {}, REF, window_months=36).status == "included"


def test_recent_tier_c_only_is_uncertain(example):
    rec = with_last_investment(example, "2026-01-05", tier="C")
    d = decide(rec, {}, REF)
    assert d.status == "uncertain" and "I3?" in d.rules


def test_no_investments_is_uncertain(example):
    example["investments"] = []
    assert decide(example, {}, REF).status == "uncertain"


def test_platform_type_is_excluded(records):
    d = decide(records[1], {}, REF)
    assert d.status == "excluded" and d.rules == ["E1"]


def test_platform_on_negative_list_is_excluded(example, fixtures_dir, tmp_path):
    neg = tmp_path / "negative.csv"
    neg.write_text("name,reason,rule\nCrowdberry,platform,E1\n", encoding="utf-8")
    example["name"] = "Crowdberry"
    d = decide(example, load_negative_list(neg), REF)
    assert d.status == "excluded" and d.rules == ["E1"]
    # the fund manager with a different name is not caught by the platform entry
    example["name"] = "Crowdberry Fund Management"
    example["aliases"] = []
    assert decide(example, load_negative_list(neg), REF).status == "included"


def test_repo_negative_list_has_the_big_platforms():
    neg = load_negative_list("data/negative_list.csv")
    assert {"crowdcube", "seedrs", "republic", "crowdberry"} <= set(neg)
    assert all(row["rule"] == "E1" for row in neg.values())


def test_missing_identity_is_uncertain(example):
    example["legal_entities"] = []
    d = decide(example, {}, REF)
    assert d.status == "uncertain" and "I1?" in d.rules


@pytest.mark.parametrize("stored,computed,expected", [
    ({"status": "included", "rules": []}, "included", "agree"),
    ({"status": "included", "rules": []}, "dormant", "DISAGREE"),
    ({"status": "excluded", "rules": ["E7"]}, "included", "human_only"),
])
def test_agreement(example, stored, computed, expected):
    example["decision"] = stored
    d = decide(example, {}, REF)
    d.status = computed
    assert agreement(example, d) == expected


def test_existence_evidence_satisfies_core_activity(example):
    rec = with_last_investment(example, "2026-01-05")
    rec["fields"]["funds"] = None  # drop the Tier A fund-of-funds source
    d = decide(rec, {}, REF)
    assert d.status == "uncertain" and "I2?" in d.rules
    rec["fields"]["existence"] = {"value": ["association_full_member"], "sources": [
        {"url": "https://example.org/members", "tier": "B", "publisher": "Example VC Association",
         "published": None, "accessed": "2026-10-11", "quote": "Full members: Example Ventures"}]}
    assert decide(rec, {}, REF).status == "included"
    # a Tier C mention isn't enough
    rec["fields"]["existence"]["sources"][0]["tier"] = "C"
    assert decide(rec, {}, REF).status == "uncertain"
