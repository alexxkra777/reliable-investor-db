import json
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

FIELD_NAMES = ("sectors", "stages", "geography", "ticket", "ticket_observed", "funds", "aum",
               "existence")
TIER_RANK = {"A": 0, "B": 1, "C": 2}


class DataError(Exception):
    pass


@dataclass
class Target:
    """One sourced thing inside a record: a field or an investment."""

    key: str  # "fields.ticket" or "investments[3]"
    kind: str  # field name or "investment"
    value: Any
    sources: list[dict]
    label: str = ""


def load_records(path: str | Path) -> list[dict]:
    p = Path(path)
    if not p.exists():
        raise DataError(f"records file not found: {p}")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise DataError(f"{p} is not valid JSON: {e}") from e
    if not isinstance(data, list):
        raise DataError(f"{p} must contain a JSON array of records")
    return data


def iter_targets(rec: dict) -> Iterator[Target]:
    fields = rec.get("fields") or {}
    for name in FIELD_NAMES:
        f = fields.get(name)
        if not f:
            continue
        yield Target(f"fields.{name}", name, f.get("value"), f.get("sources") or [], name)
    for i, inv in enumerate(rec.get("investments") or []):
        yield Target(f"investments[{i}]", "investment", inv, inv.get("sources") or [],
                     inv.get("company", ""))


def parse_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def best_tier(sources: list[dict]) -> str | None:
    tiers = [s.get("tier") for s in sources if s.get("tier") in TIER_RANK]
    return min(tiers, key=TIER_RANK.__getitem__) if tiers else None


def primary_source(sources: list[dict]) -> dict | None:
    if not sources:
        return None
    return min(sources, key=lambda s: TIER_RANK.get(s.get("tier"), 9))


def repo_root() -> Path:
    # src/investordb/records.py -> repo root
    return Path(__file__).resolve().parents[2]
