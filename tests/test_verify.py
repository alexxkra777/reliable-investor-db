from investordb.fetch import load_index
from investordb.grade import Checks, grade_record
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
    assert value_status(facts) == "partial"


def test_text_fields_have_no_value_check(example):
    t = next(t for t in iter_targets(example) if t.kind == "sectors")
    assert value_status(value_facts(t, t.sources[0], "anything")) == "n/a"


def test_claim_value_uses_all_verified_quotes(records):
    inv = [t for t in iter_targets(records[0]) if t.kind == "investment"][0]
    names_investor = "the round was led by headline with participation from example ventures"
    has_numbers = "alpha robotics raised 1.5 mil. eur on 12 march 2025"
    src = {"published": None}
    alone = value_status(value_facts(inv, src, names_investor))
    together = value_status(value_facts(inv, src, names_investor + " | " + has_numbers))
    assert alone == "value_not_in_quote"
    assert together == "ok"


def test_unreachable_publication_does_not_support_claim_date(tmp_path):
    quote = "Alpha invested in Company One."
    (tmp_path / "page.txt").write_text(quote)
    rec = {"id": "alpha", "name": "Alpha", "investments": [{
        "company": "Company One", "date": "2026-01-01", "sources": [
            {"url": "https://example.org/live", "quote": quote, "tier": "B"},
            {"url": "https://example.org/missing", "quote": "missing", "tier": "B",
             "published": "2026-01-01"},
        ],
    }]}
    rows = check_records([rec], {"https://example.org/live": {"text_file": "page.txt"}},
                         tmp_path)
    assert rows[0]["quote_status"] == "exact"
    assert rows[1]["quote_status"] == "unreachable"
    assert rows[0]["claim_value_status"] != "ok"


def test_missing_company_fails_claim_even_with_date(tmp_path):
    quote = "Alpha invested on 12 March 2025."
    (tmp_path / "page.txt").write_text(quote)
    rec = {"id": "alpha", "name": "Alpha", "investments": [{
        "company": "Invented Company", "date": "2025-03-12", "sources": [
            {"url": "https://example.org/live", "quote": quote, "tier": "B"},
        ],
    }]}
    rows = check_records([rec], {"https://example.org/live": {"text_file": "page.txt"}},
                         tmp_path)
    assert rows[0]["claim_value_status"] == "partial"


def test_split_sources_support_company_and_date_together(tmp_path):
    texts = ["Alpha invested in Company One.", "The investment was on 12 March 2025."]
    sources, index = [], {}
    for i, text in enumerate(texts):
        (tmp_path / f"page{i}.txt").write_text(text)
        url = f"https://example.org/{i}"
        sources.append({"url": url, "quote": text, "tier": "B"})
        index[url] = {"text_file": f"page{i}.txt"}
    rec = {"id": "alpha", "name": "Alpha", "investments": [{
        "company": "Company One", "date": "2025-03-12", "sources": sources,
    }]}
    rows = check_records([rec], index, tmp_path)
    assert all(r["claim_value_status"] == "ok" for r in rows)
    assert grade_record(rec, Checks(rows))["evidence"]["investments[0]"] == "verified"
