import csv
import json
import re

from investordb.evaluate import human_metrics, read_labels, recall, run_eval
from investordb.review import allocate, build_claims, render_html, sample_claims


def test_claims_skip_excluded_records(records):
    claims = build_claims(records)
    assert not any(c["record_id"] == "sample-crowd" for c in claims)
    kinds = {c["claim_id"]: c["kind"] for c in claims}
    assert kinds["example-ventures/existence"] == "existence"
    assert kinds["example-ventures/field/ticket"] == "field"
    assert kinds["demo-capital/investment/0"] == "investment"
    # dormant records get no existence claim (inclusion precision is about included ones)
    assert "demo-capital/existence" not in kinds


def test_allocate_proportional_with_floor():
    sizes = {"existence": 50, "field:ticket": 10, "field:aum": 2, "investment": 200}
    alloc = allocate(sizes, 60)
    assert sum(alloc.values()) == 60
    assert alloc["field:aum"] == 2  # whole stratum, it's below the floor
    assert alloc["field:ticket"] >= 3
    assert alloc["investment"] > alloc["existence"] > alloc["field:ticket"]
    assert all(alloc[s] <= sizes[s] for s in sizes)


def test_allocate_small_population_takes_all():
    assert allocate({"a": 2, "b": 3}, 60) == {"a": 2, "b": 3}


def test_sampling_is_deterministic(records):
    claims = build_claims(records)
    a = [c["claim_id"] for c in sample_claims(claims, 5, seed=7)]
    b = [c["claim_id"] for c in sample_claims(claims, 5, seed=7)]
    assert a == b and len(a) == 5


def test_html_is_self_contained(records):
    claims = sample_claims(build_claims(records), 60, 7)
    claims[0]["quote"] = "</script><script>alert(1)</script>"
    html = render_html(claims, 7)
    assert html.count("</script>") == 1  # only the real closing tag
    assert not re.search(r"""(src|href)=["']https?://""", html)
    assert "localStorage" in html and "labels.csv" in html
    assert 'name="viewport"' in html


def write_csv(path, header, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def test_metrics_from_labels(records, tmp_path):
    claims = sample_claims(build_claims(records), 60, 7)
    labels_path = tmp_path / "labels.csv"
    write_csv(labels_path, ["claim_id", "label", "note", "reviewed_at"], [
        ["example-ventures/existence", "correct", "", ""],
        ["example-ventures/field/ticket", "correct", "", ""],
        ["example-ventures/field/sectors", "wrong", "", ""],
        ["example-ventures/investment/0", "correct", "", ""],
        ["demo-capital/investment/0", "cant_verify", "404", ""],
        ["example-ventures/field/funds", "maybe", "", ""],
    ])
    labels, problems = read_labels(labels_path)
    assert problems == ["example-ventures/field/funds: unknown label 'maybe'"]
    m = human_metrics(claims, labels)
    assert m["inclusion_precision"]["correct"] == 1
    assert m["investment_date_accuracy"]["strict"]["value"] == 0.5
    assert m["investment_date_accuracy"]["lenient"]["value"] == 1.0
    assert m["overall_claim_accuracy"]["labelled"] == 5
    assert m["field_accuracy"]["sectors"]["correct"] == 0


def test_recall_matches_aliases_and_legal_names(records, fixtures_dir):
    r = recall(records, fixtures_dir / "reference")["example-association"]
    assert (r["k"], r["n"]) == (2, 3)
    assert r["missing"] == ["Missing Partners"]


def test_eval_without_labels_says_so(records, fixtures_dir, tmp_path):
    rc = run_eval(fixtures_dir / "investors.json", tmp_path / "claims.csv",
                  tmp_path / "labels.csv", fixtures_dir / "reference",
                  tmp_path / "none.csv", tmp_path / "none.csv", tmp_path / "none.json",
                  tmp_path / "ACCURACY.md", tmp_path / "metrics.json")
    assert rc == 0
    md = (tmp_path / "ACCURACY.md").read_text()
    assert "No review labels found" in md
    metrics = json.loads((tmp_path / "metrics.json").read_text())
    assert metrics["human"] is None
    assert metrics["recall"]["example-association"]["k"] == 2


def test_model_review_is_reported_apart_and_compared(records, fixtures_dir, tmp_path):
    from investordb.review import write_claims_csv

    claims = sample_claims(build_claims(records), 60, 7)
    claims_path = tmp_path / "claims.csv"
    write_claims_csv(claims, claims_path)
    ids = [c["claim_id"] for c in claims][:2]
    write_csv(tmp_path / "labels.csv", ["claim_id", "label", "note", "reviewed_at"],
              [[ids[0], "correct", "", ""], [ids[1], "wrong", "", ""]])
    write_csv(tmp_path / "labels-model.csv", ["claim_id", "label", "note", "reviewed_at"],
              [[ids[0], "correct", "", ""], [ids[1], "correct", "", ""]])
    run_eval(fixtures_dir / "investors.json", claims_path, tmp_path / "labels.csv",
             fixtures_dir / "reference", tmp_path / "none.csv", tmp_path / "none.csv",
             tmp_path / "none.json", tmp_path / "ACCURACY.md", tmp_path / "metrics.json",
             tmp_path / "labels-model.csv")
    md = (tmp_path / "ACCURACY.md").read_text()
    assert "## Human review" in md and "## Model review" in md
    m = json.loads((tmp_path / "metrics.json").read_text())
    assert (m["reviewer_agreement"]["k"], m["reviewer_agreement"]["n"]) == (1, 2)
    assert m["reviewer_agreement"]["disagreements"] == [ids[1]]
