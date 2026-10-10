import pytest

from investordb.stats import rate, wilson


@pytest.mark.parametrize("k,n,lo,hi", [
    (0, 10, 0.0, 0.2775),
    (10, 10, 0.7225, 1.0),
    (5, 10, 0.2366, 0.7634),
    (81, 100, 0.7222, 0.8749),
    (1, 1, 0.2065, 1.0),
])
def test_wilson_known_values(k, n, lo, hi):
    a, b = wilson(k, n)
    assert a == pytest.approx(lo, abs=1e-4)
    assert b == pytest.approx(hi, abs=1e-4)


def test_wilson_bounds_and_edge_cases():
    assert wilson(0, 0) is None
    with pytest.raises(ValueError):
        wilson(3, 2)
    for n in (1, 7, 60):
        for k in range(n + 1):
            lo, hi = wilson(k, n)
            assert 0.0 <= lo <= k / n <= hi <= 1.0


def test_rate():
    assert rate(3, 4)["value"] == 0.75
    assert rate(0, 0) == {"k": 0, "n": 0, "value": None, "ci95": None}
