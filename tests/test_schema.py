import copy
from datetime import date

import pytest

from investordb.validate import load_validator, validate

TODAY = date(2026, 10, 11)


@pytest.fixture(scope="module")
def validator():
    return load_validator()


def test_fixture_is_valid(records, validator):
    rep = validate(records, validator, today=TODAY)
    assert rep.errors == []
    assert rep.warnings == []


@pytest.mark.parametrize("mutate,needle", [
    (lambda r: r[0]["fields"]["ticket"].update(sources=[]), "should be non-empty"),
    (lambda r: r[0]["fields"].update(sectors={"value": ["x"]}), "'sources' is a required"),
    (lambda r: r[0]["fields"]["ticket"]["value"].update(currency="eur"), "does not match"),
    (lambda r: r[0].update(type="bank"), "is not one of"),
    (lambda r: r[0]["investments"][0]["sources"][0].update(tier="D"), "is not one of"),
    (lambda r: r[0]["investments"][0]["sources"][0].pop("quote"), "'quote' is a required"),
    (lambda r: r[0]["investments"][0].update(date="12.03.2025"), "does not match"),
    (lambda r: r[0]["decision"].update(rules=["X1"]), "does not match"),
    (lambda r: r[0].update(id="Not A Slug"), "does not match"),
])
def test_schema_rejects(records, validator, mutate, needle):
    bad = copy.deepcopy(records)
    mutate(bad)
    errors = validate(bad, validator, today=TODAY).errors
    assert any(needle in e for e in errors), errors


def test_null_fields_are_allowed(records, validator):
    ok = copy.deepcopy(records)
    ok[0]["fields"]["sectors"] = None
    ok[0]["website"] = None
    assert validate(ok, validator, today=TODAY).ok


def test_consistency_checks(records, validator):
    bad = copy.deepcopy(records)
    bad[0]["fields"]["ticket"]["value"].update(min=40_000_000, max=35_000_000)
    bad[0]["investments"][0]["date"] = "2027-01-01"
    bad[0]["investments"][1].update(date="2020-01-01", fund="Example Fund I")
    bad[2]["id"] = "example-ventures"
    errors = "\n".join(validate(bad, validator, today=TODAY).errors)
    assert "min 40000000 > max 35000000" in errors
    assert "max 35000000 EUR > largest fund size 30000000" in errors
    assert "is in the future" in errors
    assert "before vintage 2021" in errors
    assert "duplicate id" in errors


def test_decision_warnings(records, validator):
    bad = copy.deepcopy(records)
    bad[0]["decision"]["rules"] = ["I1", "I3"]
    bad[1]["decision"]["rules"] = []
    warnings = "\n".join(validate(bad, validator, today=TODAY).warnings)
    assert "included but rules miss I2, I4" in warnings
    assert "excluded without an E rule" in warnings


def test_cli_validate(fixtures_dir, tmp_path, capsys):
    from investordb.cli import main

    assert main(["validate", "--records", str(fixtures_dir / "investors.json"),
                 "--today", "2026-10-11"]) == 0
    assert "3 records, 0 errors" in capsys.readouterr().out
    assert main(["validate", "--records", str(tmp_path / "nope.json")]) == 2
