from investordb.fetch import load_index
from investordb.records import iter_targets
from investordb.verify import check_records, value_facts, value_status


def test_verify_against_fixture_cache(records, fixtures_dir):
    cache = fixtures_dir / "cache"
    rows = check_records(records, load_index(cache), cache)
    by = {(r["record_id"], r["target"]): r for r in rows}
    assert len(rows) == 7
    assert by[("example-ventures", "fields.ticket")]["quote_status"] == "exact"
    assert by[("example-ventures", "fields.ticket")]["value_status"] == "ok"
    assert by[("example-ventures", "fields.funds")]["fetch_used"] == "wayback"
    assert by[("example-ventures", "investments[0]")]["value_detail"] == (
        "date=2025-03-12:ok; round=1500000:ok")
    assert by[("demo-capital", "investments[0]")]["quote_status"] == "unreachable"


def test_value_not_in_quote(example):
    t = next(t for t in iter_targets(example) if t.kind == "ticket")
    src = t.sources[0]
    facts = value_facts(t, src, "our tickets are small")
    assert value_status(facts) == "value_not_in_quote"
    facts = value_facts(t, src, "tickets from 200000 eur")
    assert value_status(facts) == "partial"


def test_investment_date_from_published_date(example):
    t = next(t for t in iter_targets(example) if t.kind == "investment")
    src = dict(t.sources[0], published="2025-03-12")
    facts = value_facts(t, src, "we invested 1.5 mil. eur in alpha robotics")
    assert ("date=2025-03-12", "published") in facts
    assert value_status(facts) == "ok"


def test_text_fields_have_no_value_check(example):
    t = next(t for t in iter_targets(example) if t.kind == "sectors")
    assert value_status(value_facts(t, t.sources[0], "anything")) == "n/a"
