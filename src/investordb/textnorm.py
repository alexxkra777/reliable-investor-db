import re
import unicodedata
from datetime import date
from difflib import SequenceMatcher

FUZZY_THRESHOLD = 0.85

_CHAR_MAP = {
    **{ord(c): "'" for c in "‘’‚‛′`´"},
    **{ord(c): '"' for c in "“”„‟″«»"},
    **{ord(c): "-" for c in "‐‑‒–—―−"},
    **{ord(c): " " for c in "          "
       "  　\t\r\n\f\v"},
    **{ord(c): None for c in "​‌‍﻿­"},
    # letters that NFKD leaves alone
    ord("ł"): "l", ord("Ł"): "L", ord("đ"): "d", ord("Đ"): "D", ord("ø"): "o", ord("Ø"): "O",
}

# 1 500 000 / 1.500.000 / 1,500,000 / 1'500'000 -> 1500000 (same separator throughout)
_THOUSANDS = re.compile(r"(?<!\d)(\d{1,3})((?:([ .,'])\d{3})(?:\3\d{3})*)(?![\d])")
# 1,5 -> 1.5 (decimal comma, one or two digits after it)
_DEC_COMMA = re.compile(r"(?<=\d),(\d{1,2})(?!\d)")
_WS = re.compile(r"\s+")
_DIGITS = re.compile(r"\d+(?:\.\d+)?")


def _join_thousands(m: re.Match) -> str:
    return m.group(1) + m.group(2).replace(m.group(3), "")


def strip_diacritics(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def normalize(text: str) -> str:
    s = text.translate(_CHAR_MAP)
    s = strip_diacritics(s).translate(_CHAR_MAP).casefold()
    s = _WS.sub(" ", s).strip()
    s = _THOUSANDS.sub(_join_thousands, s)
    s = _DEC_COMMA.sub(r".\1", s)
    return s


def best_fuzzy(quote: str, text: str, max_anchors: int = 4,
               max_hits: int = 40) -> tuple[float, str]:
    """Best similarity of the (normalised) quote against windows of the (normalised) text.

    Windows are placed around occurrences of the quote's longest tokens, so we never
    slide over the whole page.
    """
    if not quote or not text:
        return 0.0, ""
    tokens = quote.split(" ")
    anchors = sorted(set(t for t in tokens if len(t) >= 3), key=len, reverse=True)[:max_anchors]
    if not anchors:
        anchors = tokens[:1]
    n = len(quote)
    best, best_window = 0.0, ""
    seen: set[int] = set()
    for a in anchors:
        q_off = quote.find(a)
        start = 0
        for _ in range(max_hits):
            i = text.find(a, start)
            if i < 0:
                break
            start = i + 1
            ws = max(0, i - q_off)
            if ws in seen:
                continue
            seen.add(ws)
            for size in (n, int(n * 1.1) + 1, max(1, int(n * 0.9))):
                window = text[ws:ws + size]
                sm = SequenceMatcher(None, quote, window, autojunk=False)
                if sm.real_quick_ratio() <= best or sm.quick_ratio() <= best:
                    continue
                r = sm.ratio()
                if r > best:
                    # keep a bit of slack so numbers at the edges are not cut in half
                    best, best_window = r, text[max(0, ws - 10):ws + int(n * 1.2) + 10]
            if best >= 0.999:
                return best, best_window
    return best, best_window


def match_quote(quote: str, text: str | None, norm_text: str | None = None) -> tuple[str, float]:
    """Return (status, similarity). Status: exact | fuzzy | missing | unreachable."""
    if text is None and norm_text is None:
        return "unreachable", 0.0
    nt = norm_text if norm_text is not None else normalize(text)
    if not nt:
        return "unreachable", 0.0
    nq = normalize(quote)
    if nq and nq in nt:
        return "exact", 1.0
    score, window = best_fuzzy(nq, nt)
    if score < FUZZY_THRESHOLD:
        return "missing", round(score, 3)
    # a near-identical sentence with different numbers is exactly the failure we hunt for
    page_nums = set(_DIGITS.findall(window))
    if any(n not in page_nums for n in _DIGITS.findall(nq)):
        return "missing", round(score, 3)
    return "fuzzy", round(score, 3)


# --- numbers -------------------------------------------------------------------

_MULT = [
    (r"thousand\w*|tisic\w*|tis\.?|k", 1e3),
    (r"million\w*|milion\w*|mil\.?|mio\.?|mn|m", 1e6),
    (r"billion\w*|miliard\w*|mld\.?|bn|b", 1e9),
]
_NUM = re.compile(
    r"(?<![\d.])(\d+(?:\.\d+)?)\s?(?:(?:eur|usd|czk|gbp|chf|€|\$|£)\s?)?("
    + "|".join(f"(?:{p})" for p, _ in _MULT) + r")?(?![a-z0-9])"
)


def _mult(word: str | None) -> float:
    if not word:
        return 1.0
    for pat, m in _MULT:
        if re.fullmatch(pat, word):
            return m
    return 1.0


def numbers_in(text: str) -> list[float]:
    """Numbers in already-normalised text, with scale words applied (1.5 mil. -> 1500000)."""
    out = []
    for m in _NUM.finditer(text):
        base = float(m.group(1))
        out.append(base)
        mult = _mult(m.group(2))
        if mult != 1.0:
            out.append(base * mult)
    return out


def number_in(value: float, text: str, rel_tol: float = 0.01) -> bool:
    tol = max(0.5, rel_tol * abs(value))
    return any(abs(x - value) <= tol for x in numbers_in(text))


# --- dates ---------------------------------------------------------------------

# month names after normalize() (no diacritics, casefolded): English, Slovak, Czech
MONTHS = {
    1: ["january", "jan", "januar", "januara", "leden", "ledna"],
    2: ["february", "feb", "februar", "februara", "unor", "unora"],
    3: ["march", "mar", "marec", "marca", "brezen", "brezna"],
    4: ["april", "apr", "aprila", "duben", "dubna"],
    5: ["may", "maj", "maja", "kveten", "kvetna"],
    6: ["june", "jun", "juna", "cerven", "cervna"],
    7: ["july", "jul", "jula", "cervenec", "cervence"],
    8: ["august", "aug", "augusta", "srpen", "srpna"],
    9: ["september", "sep", "sept", "septembra", "zari"],
    10: ["october", "oct", "oktober", "oktobra", "rijen", "rijna"],
    11: ["november", "nov", "novembra", "listopad", "listopadu"],
    12: ["december", "dec", "decembra", "prosinec", "prosince"],
}


def _names(m: int) -> str:
    return "(?:" + "|".join(sorted(MONTHS[m], key=len, reverse=True)) + r")\.?"


def date_match(d: date, text: str) -> str:
    """How well a date shows up in normalised text: 'full', 'month', 'year' or ''."""
    y, m, day = d.year, d.month, d.day
    dd, mm = rf"0?{day}", rf"0?{m}"
    names = _names(m)
    full = [
        rf"\b{y}-{m:02d}-{day:02d}\b",
        rf"\b{dd}\s?\.\s?{mm}\s?\.\s?{y}\b",
        rf"\b{dd}\s?/\s?{mm}\s?/\s?{y}\b",
        rf"\b{mm}\s?/\s?{dd}\s?/\s?{y}\b",
        rf"\b{dd}(?:st|nd|rd|th)?\.?\s{names}\s?,?\s{y}\b",
        rf"\b{names}\s{dd}(?:st|nd|rd|th)?\s?,?\s{y}\b",
    ]
    if any(re.search(p, text) for p in full):
        return "full"
    month = [
        rf"\b{names}\s?,?\s{y}\b",
        rf"\b{mm}\s?[./]\s?{y}\b",
        rf"\b{y}-{m:02d}\b",
    ]
    if any(re.search(p, text) for p in month):
        return "month"
    if re.search(rf"\b{y}\b", text):
        return "year"
    return ""
