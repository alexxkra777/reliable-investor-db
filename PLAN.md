# Plan: a reliable database of investors

The point of this database is trust. A record is only worth something if a reader can click
through to a public page and see for themselves that the entity invests, in what, how much,
and since when. So the plan is built around evidence first and coverage second.

Research behind the numbers below: [`research/sources-and-universe.md`](research/sources-and-universe.md).

---

## 1. What counts as an investor

**Unit of a record = the investing organisation (manager), or a person investing in their own name.**
Not the fund vehicle, not the SPV, not the brand. A manager with five funds is one record with
five funds attached. This matters a lot: 64 % of "venture capital fund" issuers in the last
four quarters of SEC Form D filings are one-deal SPVs or series vehicles. Counting vehicles
would triple the database with noise.

### Types

| Type | Definition used here |
|---|---|
| `vc` | Manages third-party or own capital and takes minority equity / convertible stakes in young private companies (pre-seed to growth). |
| `pe` | Buyout, growth or mezzanine investor in established private companies, usually majority or significant minority stakes. |
| `cvc` | Investment arm of a corporation (banks and insurers included) that puts balance-sheet money into third-party startups. A bank's lending is E3; a bank's startup equity program is `cvc`. |
| `family_office` | Single or multi-family office that makes **direct** investments into private companies (not only allocates to funds or manages a portfolio of listed securities). |
| `angel` | Natural person investing own money into startups, with a **public investor persona** (self-published profile, or named in at least two deal announcements). |
| `private_investor` | High-net-worth individual or their holding company with repeated direct investments in private companies. |
| `accelerator` | Program that takes equity in exchange for capital + program. Kept, but tagged, so it never pollutes ticket statistics. |
| `fund_of_funds` / `public_dfi` | Invests mainly into other funds, or a state-owned development investor. Kept in a separate list: very useful for **verification** (their portfolios name real managers), not a target investor by default. |

### Inclusion rules (all must hold)

| ID | Rule |
|---|---|
| **I1 Identity** | The entity resolves to one legal entity with a registry identifier (IČO, company number, LEI, SEC CRD/CIK) or, for a person, a stable public profile. |
| **I2 Investing is a core activity** | At least one of: a regulatory licence / registration as a fund manager (SEC ADV, ESMA AIFM/EuVECA, ČNB, NBS); full (not associate) membership of a VC/PE association; a fund-of-funds commitment (EIF, SIH, NRB) to its fund; or a self-published portfolio of ≥3 companies. |
| **I3 Proven, recent investing** | At least **one dated investment within the last 36 months**, shown by a Tier A or Tier B source (see 3.1). 36 months because CEE funds often make only 2–5 deals a year and investment periods run 4–5 years; anything shorter would wrongly drop live small funds. |
| **I4 Investor, not intermediary** | Its own capital (or capital it manages) goes into the company. |

### Exclusion rules (any one excludes)

| ID | Excluded | Why / how detected |
|---|---|---|
| **E1** | Crowdfunding / investment platforms (Crowdberry's platform, Crowdcube, Seedrs, Republic) | They route other people's money. Negative list = ESMA ECSP register (261 providers). If the platform also runs a fund, the **fund manager** can be included separately. |
| **E2** | Advisers: M&A boutiques, law firms, auditors, banks' corporate finance | Associate members of CVCA (57 of 84) and SLOVCA (31) are exactly this. NACE 69.10/69.20/70.22/64.19 filter + manual check. |
| **E3** | Lenders only (banks, leasing, venture debt funds without equity) | Debt is not equity investing. Venture debt that takes warrants → `vc` with a flag. |
| **E4** | Dormant: no dated investment in 36 months | Kept in a `dormant` list with `last_evidence_date`, so it can be re-activated. |
| **E5** | Announced but never launched funds | Needs a first close or first investment, not a press release about plans (example: the Czech Národní inovační fond was cancelled before investing). |
| **E6** | Grant agencies, subsidy programs, competitions | No equity. |
| **E7** | Pure listed-equity managers, hedge funds, retail asset managers | No private-company investing. ESMA AIFM register mixes them in (e.g. Tatra Asset Management, IAD Investments in SK). |
| **E8** | Single-business holding groups | Buying operating companies for their own group (strategic M&A) is not third-party investing. Included as `private_investor` only if they invest repeatedly in unrelated startups. |
| **E9** | Fund vehicles, SPVs, compartments | Rolled up to their manager (rule "unit of record"). |
| **E10** | Angels without a public investor persona | GDPR: names of private individuals are personal data. We only keep people who present themselves publicly as investors. |

On an excluded record the `rules` list names the rule that decided it: an E rule, or an I rule
that the entity failed (e.g. `I2` = investing isn't shown to be a core activity).

**Pilot scope (S1).** The pilot covers one slice of the database, so a real investor that falls outside
that slice (a PE firm in a VC pilot, a foreign manager, a state fund-of-funds) gets status
`out_of_scope` with rule `S1` instead of `excluded`. They are valid records for the full database,
and they are kept out of the precision numbers so the pilot doesn't look better or worse than it is.

Edge cases are decided in [`data/sample/parts/sk-decisions.md`](data/sample/parts/sk-decisions.md) and [`cz-decisions.md`](data/sample/parts/cz-decisions.md) with the rule ID that
decided each one, so the rules are testable rather than vibes.

---

## 2. Data model

```
Investor (manager or person)  1 ─── n  Fund  1 ─── n  Vehicle
   │
   ├── n  Investment (portfolio company, date, round, evidence)
   └── every field = { value, source_url, source_type, tier, published, accessed, quote }
```

- **Every value carries its own provenance.** Not "sources: [5 links]" at the bottom of a row, but
  the exact URL and an exact quote for that one field. A reviewer can check any single number
  in under a minute.
- `quote` is a verbatim sentence from the source. It is what makes automated checking possible (3.2).
- Money is stored as amount + currency + `as_of`. Fund size and AUM are different fields:
  `fund_size` (one fund's commitments) vs `aum` (manager total as stated). They are not added up
  silently, because their definitions differ.
- `ticket_min/ticket_max` = what the investor says on its own site, or what the fund-of-funds
  terms say; derived ticket estimates from round sizes are stored separately as `ticket_observed`.
- `confidence` is computed per record from the evidence tiers (3.3), not set by hand.

Schema: [`schema/investor.schema.json`](schema/investor.schema.json).

---

## 3. How authenticity and classification are verified

### 3.1 Evidence tiers

| Tier | Sources | Proves |
|---|---|---|
| **A — legal filings** | Regulators (SEC ADV/Form D, ESMA, ČNB, NBS), business registers with shareholder entries (ORSR, justice.cz, Companies House), fund-of-funds commitments from EIF/SIH/NRB | That the entity exists as a manager / that it owns a stake in company X since date Y |
| **B — first-party statements** | The investor's own site (portfolio, thesis, ticket), its press releases, the portfolio company's announcement | Investment happened and when; stated sectors and tickets |
| **C — secondary** | Media (Forbes, Trend, Startitup, CzechCrunch), Dealroom/Crunchbase public pages | Discovery and corroboration only. A C-only fact is marked `unverified`. |

### 3.2 Automated checks (run on every record, every refresh)

1. **Quote check.** Re-fetch every `source_url` and confirm the stored `quote` actually appears on
   the page (normalised whitespace and diacritics). This catches the main failure of LLM-assisted
   extraction: a plausible number with a real-looking link that says something else.
2. **Link health.** HTTP status, redirects to a homepage, and a Wayback snapshot as fallback.
3. **Recency.** `last_investment_date` within 36 months, else `dormant`.
4. **Identity.** Registry ID present and the registered name matches; foreign HQ flagged.
5. **Consistency.** ticket_min ≤ ticket_max ≤ fund_size; fund vintage ≤ investment dates; currency present.
6. **Negative lists.** ECSP platforms, association associate members, NACE codes of advisers.

### 3.3 Confidence grade

- **A**: existence proven by Tier A **and** a dated investment proven by Tier A or B.
- **B**: existence by Tier B (own portfolio of ≥3 companies) and a dated investment by Tier B.
- **C**: anything relying on Tier C. Not published as verified.

### 3.4 Independent re-verification

A second reviewer, with no access to the first pass's answers, gets only the investor name and
has to answer the same questions from scratch. Disagreements go to a human. In this pilot the
second reviewer was a different model family from the extractor, so their errors are less
correlated (details in the README).

### 3.5 Human review and the accuracy measurement

- **Inclusion precision**: share of included records that a human confirms are real, active investors of the stated type.
- **Field accuracy**: for each field (sector, stage, ticket, fund size/AUM, last investment), the share of values a human confirms against the cited source. A value with a broken or non-supporting source counts as wrong, even if it happens to be true, because the database promises provenance.
- **Recall** (where a reference list exists): share of reference entities (SLOVCA ordinary members, SIH/NDF II portfolio managers, ESMA EuVECA for SK) that ended up included or explicitly excluded with a rule.
- Report with 95 % Wilson intervals, because pilot samples are small.

---

## 4. Who can be covered, how many, how reliable

Short version (full arithmetic in the research file):

| Type | Worldwide, reachable with public evidence | Europe | Main free sources |
|---|---|---|---|
| VC managers | 5,000–7,000 | 1,500–2,200 | SEC ADV (2,312 VC-exempt advisers + 531 RIAs with VC funds), ESMA (448 EuVECA), EIF list (~700 managers), associations, press |
| PE managers | 4,000–6,000 | 1,000–1,800 | SEC ADV/Form D, ESMA AIFM (filtered), associations |
| Family offices (direct investing) | 800–2,000 of ~8,000 | 250–600 of ~2,000 | Press releases of direct deals, registry shareholder entries; no register exists |
| Large private investors | 1,500–3,000 | 400–900 | Rich lists (manual seeding only), holding company registries |
| Angels (public persona) | 15,000–40,000 | 4,000–10,000 | Press, self-published profiles; network member lists are not public |

**Headline:** about **12,000–20,000 verified organisations** worldwide, plus up to 15–40k named
angels if they are in scope. For CZ+SK about 150–300 PE/VC/FO entities.

**Expected reliability by field** (before human review):

| Field | Expected | Why |
|---|---|---|
| Is a real investor | ≥ 90 % precision with Tier A, lower for website-only records | Filings are legal documents; websites outlive funds |
| Still active | Medium, decays 10–20 % a year | Nearly half of 2021's active US investors stopped investing by 2025 (NVCA) |
| Sector / stage | Medium | Self-declared, coarse ("tech", "generalist") |
| Ticket size | Low–medium, missing for ~40–60 % | PE and family offices rarely publish it |
| Fund size / AUM | Low–medium | Mixed definitions, often stale, cumulative across funds |

---

## 5. Pilot

**Scope: venture capital investors managed from Slovakia.** Why Slovakia:
- the market is small enough to enumerate completely, so recall can be measured, not only precision;
- it has good reference lists (SLOVCA ordinary members, the state SIH / NDF II fund-of-funds portfolio, ESMA EuVECA, NBS);
- shareholder data in ORSR gives Tier A proof of investments for Slovak s.r.o. targets;
- it is the reviewer's home market, so errors are easy to spot.

**Change during the pilot:** Slovakia alone produced only 7 included VCs after full enumeration —
far too few to measure field accuracy with any confidence — so the pilot was extended to VCs managed
from Czechia (CVCA full members, EIF Czech managers, NRI, press). One record per manager across both
countries; duplicates were merged by the country the manager sits in (`scripts/merge_parts.py`).

Pilot outputs: [`data/sample/`](data/sample/) (records with per-field sources), [`eval/ACCURACY.md`](eval/ACCURACY.md), and the scale-up cost estimate in [`docs/COST.md`](docs/COST.md).

## 6. Risks and how they are handled

| Risk | Handling |
|---|---|
| GDPR (angels, family members behind family offices) | Only public investor personas; legitimate-interest assessment; Art. 14 notice and opt-out before any commercial use. |
| Terms of service of commercial databases | Crunchbase, Dealroom, PitchBook, Forbes, Finstat API are used only to **discover** names manually. Every stored fact points to a free primary source. |
| Staleness | `as_of` on every value; monthly refresh of filings, quarterly re-check of activity; dormant after 36 months. |
| Name collisions and rebrands | Matching on registry IDs, `former_names`, `successor_of`. |
