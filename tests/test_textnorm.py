from datetime import date

import pytest

from investordb.textnorm import (
    date_match,
    match_quote,
    name_key,
    normalize,
    number_in,
    numbers_in,
)


def test_normalize_strips_slovak_diacritics_and_case():
    assert normalize("Spoločník: ŽILINA, Ľubomír, Ďurčo, Šťastný") == (
        "spolocnik: zilina, lubomir, durco, stastny"
    )


def test_normalize_unifies_spaces_quotes_and_dashes():
    raw = "„Fond“ – ‘seed’ stage —\tfinal\n\nround"
    assert normalize(raw) == "\"fond\" - 'seed' stage - final round"


@pytest.mark.parametrize("raw", ["1 500 000", "1 500 000", "1.500.000", "1,500,000",
                                 "1 500 000"])
def test_normalize_thousand_separators(raw):
    assert normalize(f"round of {raw} eur") == "round of 1500000 eur"


def test_normalize_decimal_comma():
    assert normalize("1,5 mil. €") == "1.5 mil. €"


def test_normalize_leaves_dates_alone():
    assert normalize("12.03.2025") == "12.03.2025"
    assert normalize("12. 3. 2025") == "12. 3. 2025"


@pytest.mark.parametrize("text,value", [
    ("1,5 mil. eur", 1_500_000),
    ("€2M", 2_000_000),
    ("EUR 30m", 30_000_000),
    ("30 miliónov eur", 30_000_000),
    ("200k", 200_000),
    ("€200 000", 200_000),
    ("$1.5bn", 1_500_000_000),
    ("2,5 mld. Kč", 2_500_000_000),
    ("50 tis. eur", 50_000),
])
def test_numbers_with_scale_words(text, value):
    assert number_in(value, normalize(text))


def test_number_not_found():
    assert not number_in(3_000_000, normalize("tickets up to 2 mil. eur"))
    assert numbers_in(normalize("nothing here")) == []


def test_exact_match_despite_nbsp_and_diacritics():
    page = "Úvod\nDňa 12. marca 2025 sme investovali 1,5 mil. eur do Alpha Robotics.\n"
    quote = "Dna 12. marca 2025 sme investovali 1,5 mil. eur do Alpha Robotics."
    assert match_quote(quote, page) == ("exact", 1.0)


def test_exact_match_across_number_formats():
    page = "We closed a 1,500,000 EUR round."
    assert match_quote("We closed a 1 500 000 EUR round.", page)[0] == "exact"


def test_fuzzy_match_small_edit():
    page = "Intro. Our first tickets range from €200 000 to €2 million for seed rounds. Bye."
    status, sim = match_quote("Our first tickets range from €200 000 to €2 million for seed round",
                              page)
    assert status == "exact"  # a prefix is still a substring
    status, sim = match_quote("Our initial tickets range from €200 000 to €2 million for seed",
                              page)
    assert status == "fuzzy" and 0.85 <= sim < 1


def test_fuzzy_with_changed_numbers_is_missing():
    page = "Our first tickets range from €200 000 to €2 million for seed rounds."
    quote = "Our first tickets range from €250 000 to €3 million for seed rounds."
    status, sim = match_quote(quote, page)
    assert status == "missing" and sim >= 0.85


def test_missing_and_unreachable():
    assert match_quote("Completely different sentence.", "Some page about cats.")[0] == "missing"
    assert match_quote("anything", None) == ("unreachable", 0.0)
    assert match_quote("anything", "")[0] == "unreachable"


@pytest.mark.parametrize("text,expected", [
    ("Dňa 12. marca 2025 sme investovali", "full"),
    ("dne 12. března 2025", "full"),
    ("zapísaný 12.03.2025", "full"),
    ("on March 12, 2025", "full"),
    ("on 12 March 2025", "full"),
    ("published 2025-03-12", "full"),
    ("v marci 2025", "month"),
    ("in March 2025", "month"),
    ("v březnu 2025 / brezna 2025", "month"),
    ("03/2025", "month"),
    ("in 2025", "year"),
    ("in 2024", ""),
])
def test_date_match(text, expected):
    assert date_match(date(2025, 3, 12), normalize(text)) == expected


def test_czech_june_july_not_confused():
    t = normalize("1. července 2024")
    assert date_match(date(2024, 7, 1), t) == "full"
    assert date_match(date(2024, 6, 1), t) == "year"


@pytest.mark.parametrize("a,b", [
    ("Neulogy Ventures a.s.", "NEULOGY VENTURES"),
    ("Zero Gravity Capital, s. r. o.", "Zero Gravity Capital"),
    ("Limerock Fund Manager, správ. spol., a.s.", "Limerock Fund Manager"),
])
def test_name_key(a, b):
    assert name_key(a) == name_key(b)


def test_small_number_words_before_scale():
    assert number_in(5_000_000, normalize("Pět milionů eur si připravila Slovenská spořitelna"))
    assert number_in(3_000_000, normalize("investovali tri milióny eur"))
    assert not number_in(5, normalize("pět let"))
