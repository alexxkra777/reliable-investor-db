import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from investordb.records import FIELD_NAMES, parse_date, repo_root

INCLUSION_RULES = {"I1", "I2", "I3", "I4"}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def default_schema_path() -> Path:
    local = Path("schema/investor.schema.json")
    return local if local.exists() else repo_root() / "schema" / "investor.schema.json"


def load_validator(schema_path: str | Path | None = None) -> Draft202012Validator:
    schema = json.loads(Path(schema_path or default_schema_path()).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


def _where(rec: dict, i: int) -> str:
    return rec.get("id") or f"#{i}"


def _deepest(err):
    # oneOf/allOf hide the useful message somewhere inside err.context
    if not err.context:
        return err
    cands = [_deepest(e) for e in err.context]
    return max(cands, key=lambda e: (len(e.absolute_path), e.validator != "type"))


def schema_errors(records, validator: Draft202012Validator) -> list[str]:
    out = []
    for top in sorted(validator.iter_errors(records), key=lambda e: list(e.absolute_path)):
        err = _deepest(top)
        path = list(err.absolute_path)
        where = "/".join(str(p) for p in path) or "(root)"
        if path and isinstance(path[0], int) and isinstance(records[path[0]], dict):
            rid = records[path[0]].get("id")
            if rid:
                where = f"{rid}: " + "/".join(str(p) for p in path[1:])
        out.append(f"schema {where}: {err.message}")
    return out


def consistency(records: list[dict], today: date | None = None) -> Report:
    today = today or date.today()
    rep = Report()
    seen: dict[str, int] = {}
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            continue
        rid = _where(rec, i)
        if rec.get("id") in seen:
            rep.errors.append(f"{rid}: duplicate id (also record #{seen[rec['id']]})")
        else:
            seen[rec.get("id")] = i

        fields = rec.get("fields") or {}
        for name in FIELD_NAMES:
            f = fields.get(name)
            if f is None:
                continue
            if f.get("value") is not None and not f.get("sources"):
                rep.errors.append(f"{rid}: fields.{name} has a value but no sources")

        funds = (fields.get("funds") or {}).get("value") or []
        fund_by_name = {fd.get("name"): fd for fd in funds if isinstance(fd, dict)}
        for fd in funds:
            if fd.get("size") is not None and not fd.get("currency"):
                rep.errors.append(f"{rid}: fund '{fd.get('name')}' has a size but no currency")

        for tname in ("ticket", "ticket_observed"):
            t = (fields.get(tname) or {}).get("value")
            if not t:
                continue
            tmin, tmax, cur = t.get("min"), t.get("max"), t.get("currency")
            if tmin is None and tmax is None:
                rep.errors.append(f"{rid}: {tname} has neither min nor max")
            if not cur:
                rep.errors.append(f"{rid}: {tname} has no currency")
            if tmin is not None and tmax is not None and tmin > tmax:
                rep.errors.append(f"{rid}: {tname} min {tmin} > max {tmax}")
            sized = [fd for fd in funds if fd.get("size") is not None]
            if tname == "ticket" and tmax is not None and sized:
                same = [fd["size"] for fd in sized if fd.get("currency") == cur]
                if same and tmax > max(same):
                    rep.errors.append(
                        f"{rid}: ticket max {tmax} {cur} > largest fund size {max(same)} {cur}")
                elif not same:
                    rep.warnings.append(
                        f"{rid}: ticket currency {cur} differs from fund currencies, not compared")

        aum = (fields.get("aum") or {}).get("value")
        if aum and not aum.get("currency"):
            rep.errors.append(f"{rid}: aum has no currency")

        for j, inv in enumerate(rec.get("investments") or []):
            where = f"{rid}: investments[{j}] ({inv.get('company')})"
            if not inv.get("sources"):
                rep.errors.append(f"{where} has no sources")
            d = parse_date(inv.get("date"))
            if d and d > today:
                rep.errors.append(f"{where} date {d} is in the future")
            rs = inv.get("round_size")
            if rs and not rs.get("currency"):
                rep.errors.append(f"{where} round_size has no currency")
            fname = inv.get("fund")
            if fname:
                fd = fund_by_name.get(fname)
                if fd is None:
                    rep.warnings.append(f"{where} links to unknown fund '{fname}'")
                elif d and fd.get("vintage") and d.year < fd["vintage"]:
                    rep.errors.append(
                        f"{where} date {d} is before vintage {fd['vintage']} of '{fname}'")

        for tgt_sources in _all_sources(rec):
            for s in tgt_sources:
                pub, acc = parse_date(s.get("published")), parse_date(s.get("accessed"))
                if acc and acc > today:
                    rep.errors.append(f"{rid}: source accessed date {acc} is in the future")
                if pub and acc and pub > acc:
                    rep.warnings.append(f"{rid}: source published {pub} after accessed {acc}")

        dec = rec.get("decision") or {}
        rules = set(dec.get("rules") or [])
        status = dec.get("status")
        if status == "included" and INCLUSION_RULES - rules:
            missing = ", ".join(sorted(INCLUSION_RULES - rules))
            rep.warnings.append(f"{rid}: included but rules miss {missing}")
        # an I rule on an excluded record means "failed this inclusion rule"
        if status == "excluded" and not any(r[0] in "EI" for r in rules):
            rep.warnings.append(f"{rid}: excluded without an E rule or a failed I rule")
        if status == "out_of_scope" and "S1" not in rules:
            rep.warnings.append(f"{rid}: out_of_scope without S1")
        if status == "dormant" and "E4" not in rules:
            rep.warnings.append(f"{rid}: dormant without E4")
    return rep


def _all_sources(rec: dict):
    fields = rec.get("fields") or {}
    for name in FIELD_NAMES:
        f = fields.get(name)
        if f:
            yield f.get("sources") or []
    for inv in rec.get("investments") or []:
        yield inv.get("sources") or []


def validate(records, validator=None, today: date | None = None) -> Report:
    validator = validator or load_validator()
    rep = Report(errors=schema_errors(records, validator))
    if isinstance(records, list):
        c = consistency(records, today)
        rep.errors += c.errors
        rep.warnings += c.warnings
    return rep
