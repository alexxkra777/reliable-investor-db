import math

Z95 = 1.959963984540054


def wilson(k: int, n: int, z: float = Z95) -> tuple[float, float] | None:
    """Wilson score interval for k successes out of n. None when n == 0."""
    if n <= 0:
        return None
    if not 0 <= k <= n:
        raise ValueError(f"k={k} must be within 0..{n}")
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    # at k == 0 or k == n the bound is exactly 0 or 1; don't let float noise say otherwise
    lo = 0.0 if k == 0 else max(0.0, centre - half)
    hi = 1.0 if k == n else min(1.0, centre + half)
    return lo, hi


def rate(k: int, n: int) -> dict:
    ci = wilson(k, n)
    return {
        "k": k, "n": n,
        "value": round(k / n, 4) if n else None,
        "ci95": [round(ci[0], 4), round(ci[1], 4)] if ci else None,
    }
