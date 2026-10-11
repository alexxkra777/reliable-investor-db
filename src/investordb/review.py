import csv
import hashlib
import json
import random
from pathlib import Path

from investordb.records import FIELD_NAMES, TIER_RANK, iter_targets, primary_source

CLAIM_COLUMNS = [
    "claim_id", "record_id", "record_name", "decision_status", "kind", "field", "stratum",
    "claim", "quote", "url", "tier", "publisher", "published", "other_urls", "stratum_size",
]
MIN_PER_STRATUM = 3


def _money(x) -> str:
    if x is None:
        return "?"
    return f"{x:,.0f}" if float(x).is_integer() else f"{x:,}"


def describe(kind: str, v) -> str:
    if v is None:
        return "unknown"
    if kind in ("sectors", "stages", "geography"):
        return ", ".join(v)
    if kind in ("ticket", "ticket_observed"):
        return f"{_money(v.get('min'))} - {_money(v.get('max'))} {v.get('currency', '')}"
    if kind == "funds":
        return "; ".join(
            f"{fd.get('name')}: {_money(fd.get('size'))} {fd.get('currency') or ''}, "
            f"vintage {fd.get('vintage') or '?'}" for fd in v)
    if kind == "aum":
        s = f"{_money(v.get('amount'))} {v.get('currency', '')}"
        return s + (f" as of {v['as_of']}" if v.get("as_of") else "")
    if kind == "investment":
        s = f"invested in {v.get('company')} on {v.get('date') or 'unknown date'}"
        s += f" ({v.get('date_kind')})"
        rs = v.get("round_size")
        if rs:
            s += f", round {_money(rs.get('amount'))} {rs.get('currency', '')}"
        return s
    return json.dumps(v, ensure_ascii=False)


FIELD_LABELS = {
    "sectors": "Sectors", "stages": "Stages", "geography": "Geography", "ticket": "Ticket size",
    "ticket_observed": "Observed ticket", "funds": "Funds", "aum": "AUM",
}


def _claim(rec, kind, field, stratum, text, sources, cid) -> dict:
    p = primary_source(sources) or {}
    others = list(dict.fromkeys(s.get("url") for s in sources
                                if s is not p and s.get("url") and s.get("url") != p.get("url")))
    return {
        "claim_id": cid, "record_id": rec.get("id"), "record_name": rec.get("name"),
        "decision_status": (rec.get("decision") or {}).get("status", ""),
        "kind": kind, "field": field, "stratum": stratum, "claim": text,
        "quote": p.get("quote", ""), "url": p.get("url", ""), "tier": p.get("tier", ""),
        "publisher": p.get("publisher", ""), "published": p.get("published") or "",
        "other_urls": ";".join(others),
    }


def build_claims(records: list[dict]) -> list[dict]:
    claims = []
    for rec in records:
        status = (rec.get("decision") or {}).get("status")
        if status in ("excluded", "out_of_scope"):
            continue
        rid, name = rec.get("id"), rec.get("name")
        targets = list(iter_targets(rec))
        if status == "included":
            # existence: show the strongest source we have for the record
            all_src = [s for t in targets for s in t.sources]
            all_src.sort(key=lambda s: TIER_RANK.get(s.get("tier"), 9))
            hq = rec.get("hq") or {}
            ids = ", ".join(f"{le.get('id_type')} {le.get('id')}"
                            for le in rec.get("legal_entities") or [])
            text = (f"{name} is a real investor of type '{rec.get('type')}' that still invests"
                    f" (HQ {hq.get('city') or '?'}, {hq.get('country') or '?'}"
                    + (f"; {ids}" if ids else "") + ").")
            extra = [le.get("register_url") for le in rec.get("legal_entities") or []
                     if le.get("register_url")]
            c = _claim(rec, "existence", "", "existence", text, all_src[:1] + all_src[1:4],
                       f"{rid}/existence")
            if rec.get("website"):
                extra.insert(0, rec["website"])
            urls = [*c["other_urls"].split(";"), *extra]
            c["other_urls"] = ";".join(dict.fromkeys(u for u in urls if u and u != c["url"]))
            claims.append(c)
        for t in targets:
            if t.kind == "investment":
                idx = t.key[t.key.index("[") + 1:-1]
                claims.append(_claim(rec, "investment", "", "investment",
                                     f"{name} {describe('investment', t.value)}.", t.sources,
                                     f"{rid}/investment/{idx}"))
            else:
                claims.append(_claim(rec, "field", t.kind, f"field:{t.kind}",
                                     f"{FIELD_LABELS.get(t.kind, t.kind)} of {name}: "
                                     f"{describe(t.kind, t.value)}", t.sources,
                                     f"{rid}/field/{t.kind}"))
    return claims


def allocate(sizes: dict[str, int], n: int, floor: int = MIN_PER_STRATUM) -> dict[str, int]:
    """Proportional allocation with a small floor per stratum (largest remainder)."""
    total = sum(sizes.values())
    if total <= n:
        return dict(sizes)
    alloc = {s: min(k, floor) for s, k in sizes.items()}
    if sum(alloc.values()) >= n:
        # not even room for the floor: one each in a fixed order until n runs out
        alloc = dict.fromkeys(sizes, 0)
        left = n
        while left:
            for s in sorted(sizes):
                if left and alloc[s] < sizes[s]:
                    alloc[s] += 1
                    left -= 1
        return alloc
    left = n - sum(alloc.values())
    room = {s: sizes[s] - alloc[s] for s in sizes}
    room_total = sum(room.values())
    quotas = {s: left * room[s] / room_total for s in sizes}
    for s in sizes:
        alloc[s] += int(quotas[s])
    rest = n - sum(alloc.values())
    order = sorted(sizes, key=lambda s: (-(quotas[s] - int(quotas[s])), s))
    for s in order:
        if rest == 0:
            break
        if alloc[s] < sizes[s]:
            alloc[s] += 1
            rest -= 1
    return alloc


def sample_claims(claims: list[dict], n: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    by: dict[str, list[dict]] = {}
    for c in claims:
        by.setdefault(c["stratum"], []).append(c)
    alloc = allocate({s: len(v) for s, v in by.items()}, n)
    picked = []
    for s in sorted(by):
        pool = sorted(by[s], key=lambda c: c["claim_id"])
        for c in rng.sample(pool, alloc[s]):
            picked.append({**c, "stratum_size": len(pool)})
    rng.shuffle(picked)
    return picked


def stratum_order() -> list[str]:
    return ["existence", *(f"field:{f}" for f in FIELD_NAMES), "investment"]


def write_claims_csv(claims: list[dict], path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CLAIM_COLUMNS)
        w.writeheader()
        w.writerows(claims)


def read_claims_csv(path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def render_html(claims: list[dict], seed: int) -> str:
    pack_id = hashlib.sha1("|".join(c["claim_id"] for c in claims).encode()).hexdigest()[:10]
    public = [{k: c[k] for k in ("claim_id", "record_name", "kind", "field", "claim", "quote",
                                 "url", "tier", "publisher", "published", "other_urls")}
              for c in claims]
    data = json.dumps(public, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    return (TEMPLATE.replace("__DATA__", data).replace("__PACK__", pack_id)
            .replace("__COUNT__", str(len(claims))).replace("__SEED__", str(seed)))


def run_review_pack(records: list[dict], n: int, seed: int, html_path, claims_path) -> int:
    claims = build_claims(records)
    if not claims:
        print("no claims to review (no included/dormant/uncertain records with data)")
        return 1
    picked = sample_claims(claims, n, seed)
    write_claims_csv(picked, claims_path)
    p = Path(html_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(render_html(picked, seed), encoding="utf-8")
    counts: dict[str, int] = {}
    for c in picked:
        counts[c["stratum"]] = counts.get(c["stratum"], 0) + 1
    print(f"{len(claims)} claims in total, sampled {len(picked)} (seed {seed}): "
          + ", ".join(f"{s} {counts[s]}" for s in stratum_order() if s in counts))
    print(f"wrote {html_path} and {claims_path}")
    return 0


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Investor claims review</title>
<style>
:root {
  --bg: #f6f7f9; --card: #ffffff; --text: #1c2430; --muted: #5d6877; --line: #dde2e8;
  --accent: #2456c7; --quote: #f1f4f8;
  --ok: #1d7a46; --ok-bg: #e3f4ea; --bad: #b3261e; --bad-bg: #fbe7e6;
  --unk: #8a5a00; --unk-bg: #fdf1d8;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #12161c; --card: #1b2129; --text: #e4e8ee; --muted: #9aa5b3; --line: #2c3540;
    --accent: #7aa2ff; --quote: #222a34;
    --ok: #6fd39b; --ok-bg: #173325; --bad: #ff8a80; --bad-bg: #3a1d1b;
    --unk: #f1c26a; --unk-bg: #3a2f17;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
header { position: sticky; top: 0; z-index: 2; background: var(--card);
  border-bottom: 1px solid var(--line); }
.bar { max-width: 780px; margin: 0 auto; padding: 10px 16px; display: flex; flex-wrap: wrap;
  gap: 8px 12px; align-items: center; }
.bar h1 { font-size: 17px; margin: 0; flex: 1 1 auto; }
.progress { color: var(--muted); font-size: 14px; white-space: nowrap; }
main { max-width: 780px; margin: 0 auto; padding: 16px; }
details.help { background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  padding: 10px 14px; margin-bottom: 16px; font-size: 15px; }
details.help summary { cursor: pointer; font-weight: 600; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  padding: 14px 16px; margin-bottom: 14px; }
.card.correct { border-left: 5px solid var(--ok); }
.card.wrong { border-left: 5px solid var(--bad); }
.card.cant_verify { border-left: 5px solid var(--unk); }
.meta { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; font-size: 13px;
  color: var(--muted); margin-bottom: 6px; }
.badge { border: 1px solid var(--line); border-radius: 999px; padding: 1px 8px; }
.claim { font-size: 17px; font-weight: 600; margin: 4px 0 10px; overflow-wrap: anywhere; }
.quote { background: var(--quote); border-radius: 8px; padding: 10px 12px; margin: 0 0 8px;
  font-style: italic; overflow-wrap: anywhere; }
.src { font-size: 14px; overflow-wrap: anywhere; margin-bottom: 4px; }
.src a { color: var(--accent); }
.others { font-size: 13px; color: var(--muted); overflow-wrap: anywhere; }
.others a { color: var(--muted); }
.actions { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
button, select { font: inherit; font-size: 15px; border-radius: 8px; border: 1px solid var(--line);
  background: var(--card); color: var(--text); padding: 8px 12px; cursor: pointer; }
button:focus-visible, select:focus-visible, textarea:focus-visible, a:focus-visible {
  outline: 2px solid var(--accent); outline-offset: 2px; }
.actions button { flex: 1 1 120px; min-height: 44px; }
button.correct[aria-pressed="true"] {
  background: var(--ok-bg); color: var(--ok); border-color: var(--ok); }
button.wrong[aria-pressed="true"] {
  background: var(--bad-bg); color: var(--bad); border-color: var(--bad); }
button.cant_verify[aria-pressed="true"] {
  background: var(--unk-bg); color: var(--unk); border-color: var(--unk); }
button.primary { background: var(--accent); color: #fff; border-color: var(--accent); }
@media (prefers-color-scheme: dark) { button.primary { color: #0b1020; } }
textarea { width: 100%; margin-top: 10px; min-height: 44px; font: inherit; font-size: 15px;
  padding: 8px 10px; border: 1px solid var(--line); border-radius: 8px; background: var(--bg);
  color: var(--text); resize: vertical; }
.stamp { font-size: 12px; color: var(--muted); margin-top: 4px; min-height: 1em; }
.empty { color: var(--muted); text-align: center; padding: 30px 0; }
.warn { color: var(--bad); font-size: 13px; }
</style>
</head>
<body>
<header>
  <div class="bar">
    <h1>Investor claims review</h1>
    <span class="progress" id="progress"></span>
    <label class="progress" for="filter">Show</label>
    <select id="filter">
      <option value="all">All claims</option>
      <option value="todo">Not reviewed yet</option>
      <option value="correct">Correct</option>
      <option value="wrong">Wrong</option>
      <option value="cant_verify">Can't verify</option>
    </select>
    <button class="primary" id="export" type="button">Export CSV</button>
  </div>
</header>
<main>
  <details class="help" open>
    <summary>How to review</summary>
    <p>Open the source link and check the claim against that page only.</p>
    <ul>
      <li><b>Correct</b>: the page supports the claim as written (value, date, company).</li>
      <li><b>Wrong</b>: the page says something else, or doesn't contain the quote. A true claim
        with a source that doesn't back it is still <b>Wrong</b>.</li>
      <li><b>Can't verify</b>: the page doesn't load, is paywalled, or you can't decide. These
        count against accuracy in the strict metric, so add a short note.</li>
    </ul>
    <p>Answers are kept in this browser. When done, press <b>Export CSV</b> and save the file
      as <code>eval/labels.csv</code>. Pack __PACK__, __COUNT__ claims, seed __SEED__.</p>
    <p class="warn" id="storage-warn" hidden>This browser blocks local storage: answers will be
      lost on reload. Export before closing the page.</p>
  </details>
  <div id="list"></div>
</main>
<script>
(function () {
  "use strict";
  var CLAIMS = __DATA__;
  var KEY = "investordb-review-__PACK__";
  var LABELS = [["correct", "Correct"], ["wrong", "Wrong"], ["cant_verify", "Can't verify"]];
  var state = {};
  var storageOk = true;

  try {
    var raw = window.localStorage.getItem(KEY);
    if (raw) { state = JSON.parse(raw) || {}; }
  } catch (e) { storageOk = false; state = {}; }
  if (!storageOk) { document.getElementById("storage-warn").hidden = false; }

  function save() {
    try { window.localStorage.setItem(KEY, JSON.stringify(state)); }
    catch (e) { document.getElementById("storage-warn").hidden = false; }
  }

  function safeUrl(u) { return /^https?:\/\//i.test(u || "") ? u : null; }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (text !== undefined && text !== null) { n.textContent = text; }
    return n;
  }

  function link(url, text) {
    var ok = safeUrl(url);
    if (!ok) { return el("span", null, url || "(no link)"); }
    var a = el("a", null, text || url);
    a.href = ok; a.target = "_blank"; a.rel = "noopener noreferrer";
    return a;
  }

  function progress() {
    var done = 0;
    CLAIMS.forEach(function (c) { if (state[c.claim_id] && state[c.claim_id].label) { done++; } });
    document.getElementById("progress").textContent = done + " / " + CLAIMS.length + " reviewed";
  }

  function card(c, i) {
    var s = state[c.claim_id] || {};
    var box = el("article", "card" + (s.label ? " " + s.label : ""));
    box.id = "c-" + i;
    var meta = el("div", "meta");
    meta.appendChild(el("span", null, "#" + (i + 1)));
    meta.appendChild(el("span", "badge", c.kind === "field" ? c.field : c.kind));
    if (c.tier) { meta.appendChild(el("span", "badge", "Tier " + c.tier)); }
    meta.appendChild(el("span", null, c.record_name));
    box.appendChild(meta);
    box.appendChild(el("div", "claim", c.claim));
    if (c.quote) { box.appendChild(el("blockquote", "quote", "“" + c.quote + "”")); }
    var src = el("div", "src");
    src.appendChild(document.createTextNode("Source: "));
    src.appendChild(link(c.url));
    var bits = [c.publisher, c.published].filter(Boolean).join(", ");
    if (bits) { src.appendChild(document.createTextNode(" (" + bits + ")")); }
    box.appendChild(src);
    var others = (c.other_urls || "").split(";").filter(Boolean);
    if (others.length) {
      var o = el("div", "others", "Also: ");
      others.forEach(function (u, k) {
        if (k) { o.appendChild(document.createTextNode(" · ")); }
        o.appendChild(link(u));
      });
      box.appendChild(o);
    }
    var actions = el("div", "actions");
    LABELS.forEach(function (pair) {
      var b = el("button", pair[0], pair[1]);
      b.type = "button";
      b.setAttribute("aria-pressed", s.label === pair[0] ? "true" : "false");
      b.addEventListener("click", function () { setLabel(c.claim_id, pair[0]); });
      actions.appendChild(b);
    });
    box.appendChild(actions);
    var note = el("textarea");
    note.placeholder = "Note (optional)";
    note.setAttribute("aria-label", "Note for claim " + (i + 1));
    note.value = s.note || "";
    note.addEventListener("input", function () {
      var cur = state[c.claim_id] || {};
      cur.note = note.value;
      if (cur.label) { cur.reviewed_at = new Date().toISOString(); }
      state[c.claim_id] = cur;
      save();
    });
    box.appendChild(note);
    box.appendChild(el("div", "stamp", s.reviewed_at ? "Reviewed " + s.reviewed_at : ""));
    return box;
  }

  function setLabel(id, label) {
    var cur = state[id] || {};
    cur.label = cur.label === label ? "" : label;  // second click clears
    cur.reviewed_at = cur.label ? new Date().toISOString() : "";
    state[id] = cur;
    save();
    render();
  }

  function render() {
    var f = document.getElementById("filter").value;
    var list = document.getElementById("list");
    var y = window.scrollY;
    list.textContent = "";
    var shown = 0;
    CLAIMS.forEach(function (c, i) {
      var lab = (state[c.claim_id] || {}).label || "";
      if (f === "todo" && lab) { return; }
      if (f !== "all" && f !== "todo" && lab !== f) { return; }
      list.appendChild(card(c, i));
      shown++;
    });
    if (!shown) { list.appendChild(el("p", "empty", "Nothing here.")); }
    progress();
    window.scrollTo(0, y);
  }

  function csvCell(v) {
    v = v === undefined || v === null ? "" : String(v);
    return /[",\n\r]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
  }

  document.getElementById("export").addEventListener("click", function () {
    var rows = [["claim_id", "label", "note", "reviewed_at"]];
    CLAIMS.forEach(function (c) {
      var s = state[c.claim_id];
      if (s && s.label) { rows.push([c.claim_id, s.label, s.note || "", s.reviewed_at || ""]); }
    });
    var text = rows.map(function (r) { return r.map(csvCell).join(","); }).join("\r\n") + "\r\n";
    var blob = new Blob([text], { type: "text/csv;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "labels.csv";
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  });

  document.getElementById("filter").addEventListener("change", render);
  render();
})();
</script>
</body>
</html>
"""
