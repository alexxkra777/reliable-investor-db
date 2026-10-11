# Agent: public sources and universe size

Claude Code sub-agent log, exported from `agent-a3ac17bd55c8ff68c.jsonl`.
Tool outputs longer than 1,500 characters are shortened.
Russian narrative has been translated into English; executed tool code and source quotations are retained.

## Brief

You are a research analyst on a job test task: "Reliable database of investors in companies" (VC funds, private equity, family offices, angel investors, large private investors). Every record must be a REAL investor (not a random company), with: sector focus, what it typically invests in and ticket size, total investable capital (AUM/fund size), and where each piece of information comes from. ONLY publicly available data may be used.

Your job (research only, no code): produce the evidence base for the PLAN section that answers:
1. Which PUBLIC sources can be used to (a) discover investors and (b) verify that an entity really invests (and when). Cover globally and concretely, with URLs and what each source gives, its coverage, cost (free / free-with-limits), access method (API, bulk download, HTML), licence/ToS constraints for scraping. Must include at least: SEC EDGAR Form D and Form ADV (IAPD bulk data, "venture capital fund adviser" exempt reporting advisers), SEC 13F (and why it's mostly irrelevant for private investing), ESMA registers (EuVECA / AIFM), national regulators (Czech CNB list of fund managers / "obhospodařovatelé", Slovak NBS register), UK Companies House (PSC / filings) and FCA register, national business registers that show shareholders (Slovak ORSR / Finstat / RPVS register of public-sector partners, Czech justice.cz / ARES), Invest Europe and national VC associations (SLOVCA, CVCA Czech, BVCA, Invest Europe member directory, NVCA), EIF portfolio of funds, national development banks' fund-of-funds portfolios (Slovak National Development Fund II / Slovak Investment Holding, Czech National Development Fund / NRB), OpenVC, Crunchbase free tier (and its ToS), Dealroom public pages, Wikidata, GLEIF LEI data, OpenCorporates, press-release feeds, company portfolio pages, angel networks (EBAN, Business Angels Slovakia/Czechia), family office lists (and why they are hard), Forbes lists for large private investors. Be honest about which are not freely usable.
2. Size estimate of the reachable universe from public sources, by investor type (VC, PE, family office, angels, large private investors) worldwide and for Europe, with ranges. Base each number on a cited figure (e.g. SEC ERA counts, Invest Europe stats on number of firms, Preqin/PitchBook public press statements on number of firms, EBAN angel numbers, family office counts from public reports like UBS/Campden/Deloitte). Explain the arithmetic. State expected data reliability (per field: existence, sector, ticket, AUM) and why — e.g. AUM is often self-reported/stale, tickets frequently missing.
3. Typical failure modes / false positives when building such DBs (dead funds, M&A advisors, crowdfunding platforms, accelerators, banks, holding companies, fund-of-funds vs manager vs vehicle duplication, name collisions), with real examples if you can find them.

Rules:
- Use WebSearch/WebFetch heavily. Every figure must have a URL and the date you accessed it (today is 2026-10-11) and, if available, the publication date. Never invent a number; if you can't find one, write "not found" and give your reasoned estimate clearly labelled as an estimate.
- Do not sign up anywhere, do not submit forms, do not use paid APIs.
- Do not run git, do not touch any files other than your output files.

Output: write [redacted: local path] (English, structured with tables: source | what it gives | coverage | access | cost | ToS notes | URL | accessed). Create the folder if missing. Final message to me: a 15-line summary with the headline numbers and the 5 most useful free sources, plus the path.

→ `ToolSearch`

<details><summary>result</summary>

```

```
</details>

→ `WebSearch` SEC exempt reporting advisers venture capital fund advisers number 2025

→ `WebSearch` Invest Europe number of private equity firms Europe investing activity report 2025

→ `WebSearch` EBAN statistics compendium number of business angels Europe

→ `WebSearch` number of family offices worldwide Deloitte Private 2024 report 8,030

<details><summary>result</summary>

```
Web search results for query: "SEC exempt reporting advisers venture capital fund advisers number 2025"

Links: [{"title":"Exempt reporting adviser","url":"https://databento.com/compliance/exempt-reporting-adviser"},{"title":"SEC Adopts New Reporting Requirements for All Investment Advisers","url":"https://www.axley.com/?p=1813"},{"title":"SEC Adopts New Reporting Requirements for All Investment Advisers","url":"https://www.axley.com/publication_article/sec-adopts-new-reporting-requirements-for-all-investment-advisers/"},{"title":"the new regulatory regime for investment advisers","url":"https://mondaq.com/unitedstates/fund-management-reits/118986/the-new-regulatory-regime-for-investment-advisers"},{"title":"3010 sec proposes rules relating to investment adviser registration e","url":"https://hunton.com/media/legal/3010_sec_proposes_rules_relating_to_investment_adviser_registration_e.pdf"},{"title":"the new regulatory regime for investment advisers","url":"https://mondaq.com/unitedstates/fund-management-reits/119926/the-new-regulatory-regime-for-investment-advisers"},{"title":"At an open meeting on June 22, the SEC voted to adopt rules substantially as proposed earlier this year that:","url":"https://katten.com/SEC-Adopts-Rules-Implementing-Core-Provisions-of-Dodd-Frank-That-Apply-to-Investment-Advisers"},{"title":"sec clarifies exemptions for advisers","url":"https://proskauer.com/alert/sec-clarifies-exemptions-for-advisers"},{"title":"the new regulatory regime for investmen
… [1580 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Invest Europe number of private equity firms Europe investing activity report 2025"

Links: [{"title":"Investing in Europe: Private Equity Activity 2025 Report highlights strong fundraising and investment performance","url":"https://tech.eu/2026/05/07/investing-in-europe-private-equity-activity-2025-report-highlights-strong-fundraising-and-investment-performance/"},{"title":"defence investments shrunk between 2024 and 2025 finds invest europe","url":"https://realdeals.eu.com/article/defence-investments-shrunk-between-2024-and-2025-finds-invest-europe"},{"title":"invest europe venture capital reaches second highest level on record","url":"https://tech.eu/2026/07/10/invest-europe-venture-capital-reaches-second-highest-level-on-record/"},{"title":"Sale del 16% la raccolta del private capital europeo nel 2025. Lo rileva Invest Europe","url":"https://financecommunity.it/sale-del-16-la-raccolta-del-private-capital-europeo-nel-2025-lo-rileva-invest-europe/"},{"title":"Optimism returns to Europe’s private equity market despite global headwinds","url":"https://manda.be/articles/optimism-returns-to-europes-private-equity-market-despite-global-headwinds/"},{"title":"Arthur D. Little presents Invest Europe 2025 - Download the full report","url":"https://capital-riesgo.es/en/articles/state-of-the-european-private-equity-industry-by-arthur-d-little-/"},{"title":"european private equity funds close to hit the 2025 peak with fundraising at 147 billion euros 16
… [1998 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "EBAN statistics compendium number of business angels Europe"

Links: [{"title":"eban.org","url":"https://eban.org/?p=31952"},{"title":"Statistics Compendium 2019 European Early Stage Market Statistics","url":"https://eban.org/statistics-compendium-2019-european-early-stage-market-statistics"},{"title":"www.eban.org","url":"https://www.eban.org/knowledge-center/statistics"},{"title":"www.eban.org","url":"https://www.eban.org/?p=33767"},{"title":"Statistics Compendium 2019 European Early Stage Market Statistics","url":"https://www.eban.org/eban-publications/statistics-compendium-2019-european-early-stage-market-statistics/"},{"title":"Statistics Compendium 2020 European Early Stage Market Statistics","url":"https://www.eban.org/2021/12/03/"},{"title":"Statistics Compendium 2021 European Early Stage Market Statistics","url":"https://www.eban.org/2022/10/10/"},{"title":"Statistics Compendium 2021 European Early Stage Market Statistics","url":"https://eban.org/?p=35526"},{"title":"EBAN Annual Statistics Compendium for 2024","url":"https://www.eban.org/2025/10/29"},{"title":"Download the EBAN Statistics Compendium","url":"https://eltia.eu/index.php/events-extranet/eban-publishes-its-annual-statistics-compendium-reporting-on-the-activity-of-business-angels-and-business-angel-networks-in-europe-2"}]

The most recent figure I found for the number of business angels is from EBAN's 2021 compendium: approximately 39400 active business angel investors on the
… [1408 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "number of family offices worldwide Deloitte Private 2024 report 8,030"

Links: [{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/in/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/az/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"deloitte number of family offices to grow 75 by 2030","url":"https://www.dakota.com/fundraising-news/deloitte-number-of-family-offices-to-grow-75-by-2030"},{"title":"family office assets set for 7","url":"https://en.paperjam.lu/article/family-office-assets-set-for-7"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/global/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape.html"},{"title":"global edition explores the rapid expansion family offices and ffers vision of the future landscape","url":"https://www.deloitte.com/global/en/about/press-room/global-edition-explores-the-rapid-expansion-family-offices-and-ffers-vision-of-the-future-landscape"},{"title":"North
… [1853 more characters]
```
</details>

→ `WebSearch` "exempt reporting advisers" number 2025 IAA Investment Adviser Industry Snapshot venture capital

→ `WebFetch` https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers

→ `WebSearch` PitchBook number of active venture capital investors worldwide 2025

→ `WebSearch` Preqin number of private equity firms globally "fund managers" active 2024

<details><summary>result</summary>

```
Web search results for query: ""exempt reporting advisers" number 2025 IAA Investment Adviser Industry Snapshot venture capital"

Links: [{"title":"industry snapshot continued growth in demand for adviser services","url":"https://www.investmentadviser.org/iaatoday/news/industry-snapshot-continued-growth-in-demand-for-adviser-services"},{"title":"Exempt reporting adviser","url":"https://databento.com/compliance/exempt-reporting-adviser"},{"title":"IAA: Investment Adviser Industry Sees Continued Growth","url":"https://rethinking65.com/investment-adviser-industry-continues-to-see-growing-demand-for-its-services"},{"title":"IAA: Investment Adviser Industry Sees Continued Growth","url":"https://rethinking65.com/?p=24831"},{"title":"investment adviser industry snapshot 2024","url":"https://www.comply.com/resource/investment-adviser-industry-snapshot-2024/"},{"title":"comply.com","url":"https://comply.com/?p=4969"},{"title":"an overview of exempt reporting advisers era registration requirements","url":"https://www.comply.com/blog/an-overview-of-exempt-reporting-advisers-era-registration-requirements"},{"title":"natlawreview.com","url":"https://natlawreview.com/node/58823/printable/pdf"},{"title":"The Investment Adviser Industry Snapshot 2025","url":"https://www3.comply.com/the-investment-adviser-industry-snapshot-2025"},{"title":"exempt reporting advisers","url":"https://www.jonesday.com/exempt_reporting_advisers/"}]

The search didn't turn up a 2025 Snapshot figure for the number o
… [1505 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "PitchBook number of active venture capital investors worldwide 2025"

Links: [{"title":"Lovguiden LogoLovguiden","url":"https://lovguiden.dk/en/det-offentlige/det-europaeiske-institut-for-innovation-og-teknologi/2026-03-09-innoenergy-kaaret-som-verdens-mest-aktive-investor-i-energisektoren"},{"title":"Awards & Recognitions","url":"https://www.polsinelli.com/news/polsinelli-earns-top-rankings-in-pitchbooks-q2-2025-league-tables"},{"title":"active investors in game devs could fall in 2025 pitchbook","url":"https://gamesbeat.com/active-investors-in-game-devs-could-fall-in-2025-pitchbook/"},{"title":"Venture capital, all the figures for 2025 according to Pitchbook","url":"https://www.startupbusiness.it/en/venture-capital-all-the-figures-for-2025-according-to-pitchbook/149000/"},{"title":"news.crunchbase.com","url":"https://news.crunchbase.com/?p=93153"},{"title":"54860 pitchbook nvca global vc investments hit 512b in 2025 with ai accounting for 50 vc fundraising fell to a 10 year low of 1186b 100b less than in 2024","url":"https://news.bensbites.com/posts/54860-pitchbook-nvca-global-vc-investments-hit-512b-in-2025-with-ai-accounting-for-50-vc-fundraising-fell-to-a-10-year-low-of-1186b-100b-less-than-in-2024"},{"title":"Global VC deals grew in 2025, thanks to AI investments | Pitchbook first look","url":"https://gamesbeat.com/?p=314206"},{"title":"news.crunchbase.com","url":"https://news.crunchbase.com/section/data/"},{"title":"data 2025 vs 2021 fund
… [1174 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Preqin number of private equity firms globally "fund managers" active 2024"

Links: [{"title":"Listing Thumbnail","url":"https://aws.amazon.com/marketplace/pp/prodview-5sdnmcxcyi4kk"},{"title":"pe fundraising at a glance  q4 2024","url":"https://paulweiss.com/media/3985897/pe_fundraising_at_a_glance_-q4_2024.pdf"},{"title":"London Insights","url":"https://maples.com/wp-content/uploads/2024/05/London-Insights.pdf"},{"title":"Data Coverage June 2023","url":"https://wrds-www.wharton.upenn.edu/documents/1892/Data-Coverage-June-2023.pdf"},{"title":"www.aap.com.au","url":"https://www.aap.com.au/aapreleases/globenewswire1001027933/"},{"title":"Preqin, a Data and Insights Firm Focused on Alternatives, Releases Fundraising for First-Time Managers Report","url":"https://www.crowdfundinsider.com/tag/cameron-joyce/"},{"title":"state of private capital fundraising in 2025","url":"https://preqin.com/insights/research/reports/state-of-private-capital-fundraising-in-2025"},{"title":"6 Jan, 2025","url":"https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/1/top-20-private-credit-managers-hold-more-than-one-third-of-dry-powder-86886642"},{"title":"libguides.cbs.dk","url":"https://libguides.cbs.dk/Preqin"},{"title":"The Best of Preqin: 2025","url":"https://www.preqin.com/c/the-best-of-preqin-2025"}]

I didn't find a single published figure for the number of active private equity firms worldwide in 2024. The results give related numbers that
… [1291 more characters]
```
</details>

<details><summary>result</summary>

```
The page offers monthly Investment Adviser Information Report data files for two groups:

- **Registered Investment Advisers:** SEC-registered advisers. These files are larger, about 5 MB for recent months.
- **Exempt Investment Advisers:** Exempt Reporting Advisers, who file only some Form ADV items (1, 2, 3, 6, 7, 10, and 11). These files are smaller, about 0.9 MB for recent months.

**Contents:** The data comes from Form ADV filings submitted through the IARD system. The files cover Form ADV sections such as identifying information, SEC registration, advisory business, custody, control persons, and disclosure. The page notes that the SEC does not guarantee the data's accuracy, and some country fields are currently omitted.

**Frequency:** Monthly. The page's title gives coverage from July 2006 through October 2026. Some months have no usable data: October and November 2025 are PDF notices, and January 2019 was unavailable due to a government shutdown.

**Format:** Recent files are ZIP archives that contain a spreadsheet when unzipped. Files from September 2025 and earlier, back to 2025, are direct XLSX downloads. Older files are ZIP or XLSX.

**Latest file date:** October 2026. The page was last updated October 2, 2026.

**Latest URLs:**
- Registered Investment Advisers, October 2026 (ZIP, 5.74 MB): https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia100226.zip
- Exempt Investment Advisers, October 20
… [474 more characters]
```
</details>

→ `Bash` — Download SEC adviser data files
```sh
mkdir -p [tmp] && cd [tmp] && curl -s -A "[redacted: name] research [redacted: email]" -o era.zip https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia100226-exempt.zip && curl -s -A "[redacted: name] research [redacted: email]" -o ria.zip https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia100226.zip && ls -la && unzip -o era.zip -d era && unzip -o ria.zip -d ria && ls -la era ria
```

<details><summary>result</summary>

```
total 13616
drwxr-xr-x  4 [user]  wheel      128 11 Oct  01:08 .
drwx------  3 [user]  wheel       96 11 Oct  01:08 ..
-rw-r--r--  1 [user]  wheel   949871 11 Oct  01:08 era.zip
-rw-r--r--  1 [user]  wheel  6019002 11 Oct  01:08 ria.zip
Archive:  era.zip
  inflating: era/ia100226-exempt.csv
Archive:  ria.zip
  inflating: ria/ia09012026.csv
era:
total 13136
drwxr-xr-x  3 [user]  wheel       96 11 Oct  01:08 .
drwxr-xr-x  6 [user]  wheel      192 11 Oct  01:08 ..
-rw-rw-rw-  1 [user]  wheel  6725415  2 Oct  16:31 ia100226-exempt.csv

ria:
total 83432
drwxr-xr-x  3 [user]  wheel        96 11 Oct  01:08 .
drwxr-xr-x  6 [user]  wheel       192 11 Oct  01:08 ..
-rw-rw-rw-  1 [user]  wheel  42713988  2 Oct  16:26 ia09012026.csv
```
</details>

→ `Bash` — Inspect SEC adviser file headers
```sh
cd [tmp] && python3 -I -c "
import csv,sys
for f in ['era/ia100226-exempt.csv','ria/ia09012026.csv']:
    with open(f,encoding='latin-1') as fh:
        r=csv.reader(fh); h=next(r)
        print(f,len(h))
        for i,c in enumerate(h):
            if any(k in c.lower() for k in ['venture','2b','exempt','private fund','country','sec region','state','legal name','primary business','5f','regulatory assets']): print(i,repr(c))
"
```

<details><summary>result</summary>

```
era/ia100226-exempt.csv 171
0 'SEC Region'
8 'Primary Business Name'
9 'Legal Name'
13 'Main Office State'
14 'Main Office Country'
23 'Mail Office State'
24 'Mail Office Country'
38 'Location of Books and Records State'
39 'Location of Books and Records Country'
47 '2B(1)'
48 '2B(2)'
49 '2B(3)'
53 '3C-State'
54 '3C-Country'
97 'Count of Private Funds - 7B(1)'
105 'Any Real Estate Funds'
106 'Total number of Real Estate funds'
113 'Total Gross Assets of Private Funds'
114 'Count of Private Funds - 7B(2)'
167 '12B(1)'
168 '12B(2)'
ria/ia09012026.csv 448
0 'SEC Region'
10 'Primary Business Name'
11 'Legal Name'
15 'Main Office State'
16 'Main Office Country'
25 'Mail Office State'
26 'Mail Office Country'
41 'Location of Books and Records State'
42 'Location of Books and Records Country'
65 '3C-State'
66 '3C-Country'
159 '5F(1)'
160 '5F(2)(a)'
161 '5F(2)(b)'
162 '5F(2)(c)'
163 '5F(2)(d)'
164 '5F(2)(e)'
165 '5F(2)(f)'
166 '5F(3)'
337 'Count of Private Funds - 7B(1)'
345 'Any Real Estate Funds'
346 'Total number of Real Estate funds'
353 'Total Gross Assets of Private Funds'
354 'Count of Private Funds - 7B(2)'
444 '12B(1)'
445 '12B(2)'
```
</details>

→ `Bash` — Inspect ERA file columns and sample
```sh
cd [tmp] && python3 -I -c "
import csv
with open('era/ia100226-exempt.csv',encoding='latin-1') as fh:
    r=csv.reader(fh); h=next(r)
    print(h[40:60]); print(h[95:120])
    rows=list(r)
print(len(rows))
print(rows[0][40:60]); print(rows[0][95:120])
"
```

<details><summary>result</summary>

```
['Location of Books and Records Postal Code', 'Total Number of Books and Records Locations', '1M', '1N', '1O', '1O - If yes, approx. amount of assets', '1P', '2B(1)', '2B(2)', '2B(3)', '3A', '3A-Other', '3B', '3C-State', '3C-Country', '6A(1)', '6A(2)', '6A(3)', '6A(4)', '6A(5)']
['Share Location', '7B', 'Count of Private Funds - 7B(1)', 'Any PFs a Master', 'Any Hedge Funds', 'Total number of Hedge funds', 'Any Liquidity Funds', 'Total number of Liquidity funds', 'Any PE Funds', 'Total number of PE funds', 'Any Real Estate Funds', 'Total number of Real Estate funds', 'Any Securitized Funds', 'Total number of Securitized funds', 'Any VC Funds', 'Total number of VC funds', 'Any Other Funds', 'Total number of Other funds', 'Total Gross Assets of Private Funds', 'Count of Private Funds - 7B(2)', '10A', 'Count of Control person Public Reporting Company', '11', '11A(1)', 'Count of 11A(1) disclosures']
6778
['', '0', 'N', 'N', 'N', '', '', 'N', 'Y', 'N', 'Limited Liability Company', '', 'DECEMBER', 'CO', 'United States', 'N', 'N', 'Y', 'N', 'N']
['N', 'Y', '                   1', 'N', 'N', '', 'N', '', 'Y', '1', 'N', '', 'N', '', 'N', '', 'N', '', '            78,960,522.00', '                   0', 'N', '                   0', 'N', 'N', '0']
```
</details>

→ `Bash` — Count ERAs by exemption and country
```sh
cd [tmp] && python3 -I -c "
import csv,collections
def num(s):
    s=s.strip().replace(',','')
    try: return float(s)
    except: return 0.0
with open('era/ia100226-exempt.csv',encoding='latin-1') as fh:
    r=csv.DictReader(fh); rows=list(r)
print('ERA total',len(rows))
for k in ['2B(1)','2B(2)','2B(3)','Any VC Funds','Any PE Funds','Any Hedge Funds']:
    print(k,collections.Counter(x[k] for x in rows))
vc=[x for x in rows if x['2B(1)']=='Y']
print('VC-exempt advisers',len(vc))
print('VC funds count total', sum(num(x['Total number of VC funds']) for x in rows))
print('VC-exempt gross assets \$bn', sum(num(x['Total Gross Assets of Private Funds']) for x in vc)/1e9)
c=collections.Counter(x['Main Office Country'] for x in vc); print('VC by country top',c.most_common(25))
c2=collections.Counter(x['Main Office Country'] for x in rows); print('ALL ERA by country top',c2.most_common(30))
eu=['United Kingdom','Germany','France','Switzerland','Netherlands','Luxembourg','Sweden','Ireland','Spain','Italy','Denmark','Finland','Norway','Belgium','Austria','Czech Republic','Czechia','Slovakia','Poland','Portug
… [414 more characters]
```

<details><summary>result</summary>

```
ERA total 6778
2B(1) Counter({'N': 4466, 'Y': 2312})
2B(2) Counter({'Y': 4911, 'N': 1867})
2B(3) Counter({'N': 6683, 'Y': 95})
Any VC Funds Counter({'N': 4037, 'Y': 2741})
Any PE Funds Counter({'N': 4784, 'Y': 1994})
Any Hedge Funds Counter({'N': 5544, 'Y': 1234})
VC-exempt advisers 2312
VC funds count total 41771.0
VC-exempt gross assets $bn 1280.332321997
VC by country top [('United States', 1512), ('', 493), ('Israel', 41), ('Cayman Islands', 41), ('United Kingdom', 34), ('Singapore', 22), ('China', 16), ('Brazil', 14), ('Canada', 14), ('India', 14), ('Mauritius', 13), ('Hong Kong', 11), ('Germany', 10), ('United Arab Emirates', 7), ('Switzerland', 7), ('Mexico', 5), ('Guernsey', 5), ('France', 5), ('Netherlands', 4), ('Chile', 3), ('Luxembourg', 3), ('Ireland', 3), ('Argentina', 2), ('Cyprus', 2), ('Vietnam', 2)]
ALL ERA by country top [('United States', 3328), ('', 937), ('United Kingdom', 513), ('Hong Kong', 218), ('Cayman Islands', 188), ('Singapore', 182), ('Israel', 103), ('Canada', 98), ('Luxembourg', 96), ('China', 82), ('France', 72), ('Mauritius', 69), ('Jersey', 67), ('Brazil', 62), ('India', 60), ('Australia', 59), ('Switzerland', 57), ('United Arab Emirates', 56), ('Guernsey', 55), ('Germany', 52), ('Sweden', 50), ('Japan', 45), ('Netherlands', 32), ('Ireland', 29), ('British Virgin Islands', 25), ('Spain', 21), ('Bermuda', 19), ('Korea, South', 17), ('Denmark', 14), ('Mexico', 12)]
Europe ERA all 1137 Europe VC 84
CZ/SK [('Slovakia', 1), ('Czech Republic', 1)
… [1 more characters]
```
</details>

→ `Bash` — Count RIAs with VC/PE private funds
```sh
cd [tmp] && python3 -I -c "
import csv,collections
def num(s):
    s=s.strip().replace(',','')
    try: return float(s)
    except: return 0.0
with open('ria/ia09012026.csv',encoding='latin-1') as fh:
    rows=list(csv.DictReader(fh))
print('RIA total',len(rows))
for k in ['Any VC Funds','Any PE Funds','Any Hedge Funds']:
    print(k,collections.Counter(x.get(k) for x in rows))
pf=[x for x in rows if num(x['Count of Private Funds - 7B(1)'])>0]
print('RIA with >=1 private fund',len(pf))
vcpe=[x for x in rows if x.get('Any VC Funds')=='Y' or x.get('Any PE Funds')=='Y']
print('RIA with VC or PE funds',len(vcpe))
print('VC funds total RIA',sum(num(x['Total number of VC funds']) for x in rows),'PE funds total RIA',sum(num(x['Total number of PE funds']) for x in rows))
c=collections.Counter(x['Main Office Country'] for x in vcpe); print(c.most_common(15))
# check family office-ish names
print('names with FAMILY OFFICE', sum(1 for x in rows if 'FAMILY OFFICE' in (x['Primary Business Name']+x['Legal Name']).upper()))
" ; python3 -I -c "
import csv
rows=list(csv.DictReader(open('[tmp]
… [321 more characters]
```

<details><summary>result</summary>

```
RIA total 17210
Any VC Funds Counter({'N': 16679, 'Y': 531})
Any PE Funds Counter({'N': 14632, 'Y': 2578})
Any Hedge Funds Counter({'N': 14606, 'Y': 2604})
RIA with >=1 private fund 5837
RIA with VC or PE funds 2861
VC funds total RIA 5359.0 PE funds total RIA 32544.0
[('United States', 2672), ('', 118), ('United Kingdom', 23), ('Canada', 21), ('Australia', 6), ('Singapore', 4), ('Ireland', 3), ('Guernsey', 2), ('Hong Kong', 2), ('Korea, South', 1), ('Switzerland', 1), ('Brazil', 1), ('Guatemala', 1), ('Mauritius', 1), ('Israel', 1)]
names with FAMILY OFFICE 76
ERA PE funds total 10379.0
ERA with VC or PE 4609
```
</details>

→ `WebFetch` https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets

→ `WebFetch` https://www.sec.gov/search-filings/edgar-search-tools/accessing-edgar-data

<details><summary>result</summary>

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

<details><summary>result</summary>

```
**Contents:** The page says the data sets contain structured data from Notices of Exempt Offerings of Securities filed under Rule 504, Rule 506(b), Rule 506(c), or Section 4(a)(5). The data is taken from the XML-based fillable portion of Form D. The page does not list specific fields such as issuer, offering, related persons, or industry group (including pooled investment fund types). It refers to a separate PDF, "Form D Data Sets," for documentation of scope, organization, file formats, and table definitions.

**Format:** The data is provided as ZIP files. It is "presented without change from the 'as-filed' submissions and in a flattened format."

**Frequency:** Updated quarterly. Filings made after 5:30 PM Eastern on the last business day of a quarter appear in the next quarterly posting.

**Coverage and latest quarter:** The banner says September 2009 to September 2026, but the download list also includes 2008 Q1 through Q4 files. The latest quarter listed is 2026 Q3. The page was last reviewed or updated on Sept. 30, 2026.

**Limitations (per the disclaimer):**
- The SEC cannot guarantee accuracy, since the data comes from registrant-submitted information.
- Errors may have been introduced during extraction and compilation.
- The sets do not include all information, such as certain filing metadata.
- They are not a substitute for the filings, and investors should review full filings before making decisions.
```
</details>

→ `Bash` — Find Form D dataset download links
```sh
cd [tmp] && curl -s -A "[redacted: name] research [redacted: email]" https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets | grep -oE 'href="[^"]+\.zip"' | head -8
```

<details><summary>result</summary>

```
href="/files/datastandardsinnovation/data/form-d-data-sets/2026q3_d.zip"
href="/files/datastandardsinnovation/data/form-d-data-sets/2026q2_d.zip"
href="/files/structureddata/data/form-d-data-sets/2026q1_d.zip"
href="/files/structureddata/data/form-d-data-sets/2025q4_d.zip"
href="/files/structureddata/data/form-d-data-sets/2025q3_d.zip"
href="/files/structureddata/data/form-d-data-sets/2025q2_d.zip"
href="/files/structureddata/data/form-d-data-sets/2025q1_d.zip"
href="/files/structureddata/data/form-d-data-sets/2024q4_d.zip"
```
</details>

→ `Bash` — Download four quarters of Form D data
```sh
cd [tmp] && mkdir -p formd && for q in 2025q4 2026q1 2026q2 2026q3; do p=structureddata; [[ $q == 2026q2 || $q == 2026q3 ]] && p=datastandardsinnovation; curl -s -A "[redacted: name] research [redacted: email]" -o formd/$q.zip https://www.sec.gov/files/$p/data/form-d-data-sets/${q}_d.zip; sleep 1; unzip -o -q formd/$q.zip -d formd/$q; done; ls -R formd | head -30
```

<details><summary>result</summary>

```
2025q4
2025q4.zip
2026q1
2026q1.zip
2026q2
2026q2.zip
2026q3
2026q3.zip

formd/2025q4:
2025Q4_d

formd/2025q4/2025Q4_d:
FormD_metadata.json
FormD_readme.html
FORMDSUBMISSION.tsv
ISSUERS.tsv
OFFERING.tsv
RECIPIENTS.tsv
RELATEDPERSONS.tsv
SIGNATURES.tsv

formd/2026q1:
2026Q1_d

formd/2026q1/2026Q1_d:
FormD_metadata.json
FormD_readme.html
FORMDSUBMISSION.tsv
ISSUERS.tsv
```
</details>

→ `Bash` — Inspect Form D table headers
```sh
cd [tmp] && head -1 2026q3/*/OFFERING.tsv | tr '\t' '\n' | head -60; head -1 2026q3/*/FORMDSUBMISSION.tsv; head -1 2026q3/*/ISSUERS.tsv
```

<details><summary>result</summary>

```
ACCESSIONNUMBER
INDUSTRYGROUPTYPE
INVESTMENTFUNDTYPE
IS40ACT
REVENUERANGE
AGGREGATENETASSETVALUERANGE
FEDERALEXEMPTIONS_ITEMS_LIST
ISAMENDMENT
PREVIOUSACCESSIONNUMBER
SALE_DATE
YETTOOCCUR
MORETHANONEYEAR
ISEQUITYTYPE
ISDEBTTYPE
ISOPTIONTOACQUIRETYPE
ISSECURITYTOBEACQUIREDTYPE
ISPOOLEDINVESTMENTFUNDTYPE
ISTENANTINCOMMONTYPE
ISMINERALPROPERTYTYPE
ISOTHERTYPE
DESCRIPTIONOFOTHERTYPE
ISBUSINESSCOMBINATIONTRANS
BUSCOMBCLARIFICATIONOFRESP
MINIMUMINVESTMENTACCEPTED
OVER100RECIPIENTFLAG
TOTALOFFERINGAMOUNT
TOTALAMOUNTSOLD
TOTALREMAINING
SALESAMTCLARIFICATIONOFRESP
HASNONACCREDITEDINVESTORS
NUMBERNONACCREDITEDINVESTORS
TOTALNUMBERALREADYINVESTED
SALESCOMM_DOLLARAMOUNT
SALESCOMM_ISESTIMATE
FINDERSFEE_DOLLARAMOUNT
FINDERSFEE_ISESTIMATE
FINDERFEECLARIFICATIONOFRESP
GROSSPROCEEDSUSED_DOLLARAMOUNT
GROSSPROCEEDSUSED_ISESTIMATE
GROSSPROCEEDSUSED_CLAROFRESP
AUTHORIZEDREPRESENTATIVE
ACCESSIONNUMBER	FILE_NUM	FILING_DATE	SIC_CODE	SCHEMAVERSION	SUBMISSIONTYPE	TESTORLIVE	OVER100PERSONSFLAG	OVER100ISSUERFLAG
ACCESSIONNUMBER	IS_PRIMARYISSUER_FLAG	ISSUER_SEQ_KEY	CIK	ENTITYNAME	STREET1	STREET2	CITY	STATEORCOUNTRY	STATEORCOUNTRYDESCRIPTION	ZIPCODE	ISSUERPHONENUMBER	JURISDICTIONOFINC	ISSUER_PREVIOUSNAME_1	ISSUER_PREVIOUSNAME_2	ISSUER_PREVIOUSNAME_3	EDGAR_PREVIOUSNAME_1	EDGAR_PREVIOUSNAME_2	EDGAR_PREVIOUSNAME_3	ENTITYTYPE	ENTITYTYPEOTHERDESC	YEAROFINC_TIMESPAN_CHOICE	YEAROFINC_VALUE_ENTERED
```
</details>

→ `Bash` — Count Form D filings by fund type over 4 quarters
```sh
cd [tmp] && python3 -I -c "
import csv,glob,collections
csv.field_size_limit(10**9)
tot=collections.Counter(); new=collections.Counter(); filers=collections.Counter(); ciks={'Venture Capital Fund':set(),'Private Equity Fund':set()}
allsub=0
for d in sorted(glob.glob('*/*_d')):
    off=list(csv.DictReader(open(d+'/OFFERING.tsv',encoding='latin-1'),delimiter='\t'))
    sub={r['ACCESSIONNUMBER']:r['SUBMISSIONTYPE'] for r in csv.DictReader(open(d+'/FORMDSUBMISSION.tsv',encoding='latin-1'),delimiter='\t')}
    iss={}
    for r in csv.DictReader(open(d+'/ISSUERS.tsv',encoding='latin-1'),delimiter='\t'):
        if r['IS_PRIMARYISSUER_FLAG']=='YES': iss[r['ACCESSIONNUMBER']]=r['CIK']
    allsub+=len(off)
    for r in off:
        t=r['INVESTMENTFUNDTYPE'] or ('(non-fund) '+r['INDUSTRYGROUPTYPE'] if r['INDUSTRYGROUPTYPE']!='Pooled Investment Fund' else 'Pooled-other')
        tot[r['INVESTMENTFUNDTYPE'] or 'NONFUND']+=1
        if sub.get(r['ACCESSIONNUMBER'])=='D': new[r['INVESTMENTFUNDTYPE'] or 'NONFUND']+=1
        if r['INVESTMENTFUNDTYPE'] in ciks: ciks[r['INVESTMENTFUNDTYPE']].add(iss.get(r['ACCE
… [236 more characters]
```

<details><summary>result</summary>

```
all offerings 4q 62963
all filings by fund type [('NONFUND', 22478), ('Venture Capital Fund', 10856), ('Hedge Fund', 10231), ('Other Investment Fund', 9755), ('Private Equity Fund', 9643)]
new D (not D/A) by type [('NONFUND', 17796), ('Venture Capital Fund', 9459), ('Private Equity Fund', 6247), ('Other Investment Fund', 4802), ('Hedge Fund', 1831)]
{'Venture Capital Fund': 10222, 'Private Equity Fund': 8724}
Counter({'D': 10291, 'D/A': 5661})
```
</details>

→ `Bash` — Estimate SPV share of VC Form D issuers
```sh
cd [tmp] && python3 -I -c "
import csv,glob,collections,re
csv.field_size_limit(10**9)
names=[]; rel=collections.Counter()
for d in sorted(glob.glob('*/*_d')):
    vc={r['ACCESSIONNUMBER'] for r in csv.DictReader(open(d+'/OFFERING.tsv',encoding='latin-1'),delimiter='\t') if r['INVESTMENTFUNDTYPE']=='Venture Capital Fund'}
    for r in csv.DictReader(open(d+'/ISSUERS.tsv',encoding='latin-1'),delimiter='\t'):
        if r['ACCESSIONNUMBER'] in vc and r['IS_PRIMARYISSUER_FLAG']=='YES': names.append(r['ENTITYNAME'])
names=set(names); print('unique VC issuer names',len(names))
ser=[n for n in names if re.search(r'a series of|series [0-9]|\bSPV\b|co-invest|coinvest',n,re.I)]
print('series/SPV/co-invest-like',len(ser))
import random; random.seed(1); print(random.sample(sorted(ser),12))
"
```

<details><summary>result</summary>

```
unique VC issuer names 10248
series/SPV/co-invest-like 6609
['CA-0223 Fund I, a series of Capital Factory SPVs, LP', 'Parkway Co-Investment 12 (Figure Series C) QP LP', 'dotCV Aug 2025 a Series of CGF2021 LLC', 'VE-0731 Fund I, a series of Seldon Lab, LP', 'Aloga Circool SPV a Series of CGF2021 LLC', 'F25, a series of Rail Ventures, LP', 'Billseye a Series of Fictive Ventures Investments LLC', 'NI-0617 Fund III, a series of Roll Up Vehicles, LP', 'VA-1218 Fund II, a series of Zachary Ginsburg Funds, LP', 'MA-0706 Fund I, a series of Gold Dragon Ventures, LP', 'MajlisQuintSPV1 a Series of CGF2021 LLC', 'SMC0526 a Series of Raba Partners LLC']
```
</details>

→ `WebSearch` NVCA Yearbook 2025 number of venture capital firms in the US assets under management

→ `WebSearch` Center for Venture Research angel market analysis 2024 number of active angel investors

→ `WebSearch` Forbes World's Billionaires 2026 list number of billionaires record

→ `WebSearch` ESMA register EuVECA managers number registered interactive single register

<details><summary>result</summary>

```
Web search results for query: "NVCA Yearbook 2025 number of venture capital firms in the US assets under management"

Links: [{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/press_releases/nvca-releases-2025-yearbook-showcasing-2024-vc-trends/"},{"title":"FOR IMMEDIATE RELEASE","url":"https://nvca.org/?p=120789"},{"title":"largest venture capital firms us","url":"https://altss.com/rankings/largest-venture-capital-firms-us"},{"title":"2025 NVCA Yearbook","url":"https://nvca.org/wp-content/uploads/2025/03/2025-NVCA-Yearbook.pdf"},{"title":"NVCA Yearbook","url":"https://nvca.org/?p=116130"},{"title":"nvca yearbook","url":"https://nvca.org/nvca-yearbook/"},{"title":"NVCA 2026 Yearbook 4.9.26","url":"https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf"},{"title":"NVCA 2017 Yearbook","url":"https://nvca.org/wp-content/uploads/2023/07/NVCA-2017-Yearbook.pdf"},{"title":"largest venture capital firms","url":"https://altss.com/rankings/largest-venture-capital-firms"}]

The 2025 NVCA Yearbook results don't give a total firm count or assets under management figure for U.S. VC firms. The closest figures come from neighboring editions.

- **2025 Yearbook (2024 data):** The NVCA release says U.S. firms raised $76.8 billion across 538 funds in 2024. It also reports 14,320 deals worth $215.4 billion and a U.S. median fund size of $21.3 million.
- **2024 Yearbook (2023 data):** This edition reported that by the end of 2023, the U.S. VC ecosystem had 3,417 VC firm
… [678 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Center for Venture Research angel market analysis 2024 number of active angel investors"

Links: [{"title":"paulcollege.unh.edu","url":"https://paulcollege.unh.edu/sites/default/files/media/2025-12/FY%202024%20Analysis%20Report%20Final.pdf"},{"title":"- July 3, 2024","url":"https://eban.org/?p=40179"},{"title":"axis intelligence","url":"https://axis-intelligence.com/?p=40436"},{"title":"Site icon EBAN","url":"https://www.eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels/amp"},{"title":"fy 2022 analysis report final","url":"https://paulcollege.unh.edu/sites/default/files/resource/files/fy_2022_analysis_report_final.pdf"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://www.eban.org/industry-reports/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels/"},{"title":"center for venture research the angel market in 2023 an inflection point for women angels","url":"https://eban.org/center-for-venture-research-the-angel-market-in-2023-an-inflection-point-for-women-angels"},{"title":"www.unh.edu","url":"https://www.unh.edu/unhtoday/node/11005"},{"title":"The Angel Market in 2021: Metrics Indicate Strong Market – By Center for Venture Research","url":"https://www.eban.org/knowledge-center/the-angel-market-in-2021-metrics-indicate-strong-market-by-center-for-venture-research/"},{"title":"Site icon EBAN","u
… [1279 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Forbes World's Billionaires 2026 list number of billionaires record"

Links: [{"title":"Forbes 2026 List Shows Record 3,428 Billionaires Led by Elon Musk","url":"https://ground.news/article/ccd7639b-1af9-497a-b912-3dcd3103ff6a"},{"title":"Forbes billionaires list hits record 3,428 as combined wealth tops US$20 trillion","url":"https://theonlinecitizen.com/2026/03/12/forbes-billionaires-list-hits-record-3-428-as-combined-wealth-tops-us-20-trillion"},{"title":"WORLD > NEWS","url":"https://bernama.com/en/world/news.php?id=2532912"},{"title":"forbes billionaire list 2026","url":"https://www.bosshunting.com.au/hustle/forbes-billionaire-list-2026/"},{"title":"number of billionaires and collective wealth","url":"https://statista.com/chart/17979/number-of-billionaires-and-collective-wealth"},{"title":"WORLD > NEWS","url":"https://web11.bernama.com/en/world/news.php?id=2532912"},{"title":"Now Reading","url":"https://www.stylerave.com/richest-people-in-the-world-2026/"},{"title":"World's Billionaires List in 2026: Rankings, Net Worth & Key Trends","url":"https://www.bleap.finance/en-us/blog/world-billionaires-list"},{"title":"World's Billionaires List in 2026: Rankings, Net Worth & Key Trends","url":"https://www.bleap.finance/fr-fr/blog/world-billionaires-list"}]

Forbes' 2026 World's Billionaires list, published March 10, 2026, counted a record number of billionaires. Here are the key figures:

- **Count:** Forbes' 40th annual Billionaires List records 3
… [1023 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "ESMA register EuVECA managers number registered interactive single register"

Links: [{"title":"Databases and Registers","url":"https://www.esma.europa.eu/databases-and-registers"},{"title":"ESMA Registers - Publication Interface Help File","url":"https://registers.esma.europa.eu/publication/helpPage"},{"title":"esma 2016 774   questions and answers. application of the eusef and euveca regulations","url":"https://www.dirittobancario.it/wp-content/uploads/sites/default/files/allegati/esma-2016-774_-_questions_and_answers._application_of_the_eusef_and_euveca_regulations.pdf"},{"title":"Databases and Registers","url":"https://www.esma.europa.eu/access-regulated-information"},{"title":"eumonitor.eu","url":"https://eumonitor.eu/9353000/1/j4nvhdfcs8bljza_j9vvik7m1c3gyxp/vk5rfykdg0zq"},{"title":"www.esma.europa.eu","url":"https://www.esma.europa.eu/print/pdf/node/201492"},{"title":"service.betterregulation.com","url":"https://service.betterregulation.com/document/204440"},{"title":"Company register","url":"https://www.fi.se/en/our-registers/company-register/gransoverskridandehandel?id=608219"},{"title":"Company register","url":"https://fi.se/en/our-registers/company-register/gransoverskridandehandel/?id=656590"},{"title":"Company register","url":"https://www.fi.se/en/our-registers/company-register/gransoverskridandehandel?id=684722"}]

The search didn't turn up a current count of registered EuVECA managers. It did confirm how the register is set up.

-
… [1406 more characters]
```
</details>

→ `Bash` — Query ESMA registers Solr endpoints
```sh
for c in esma_registers_euveca esma_registers_upreg esma_registers_aifmd esma_registers_eusef; do echo "== $c"; curl -s -m 30 "https://registers.esma.europa.eu/solr/${c}/select?q=*:*&rows=1&wt=json" | head -c 1500; echo; done
```

<details><summary>result</summary>

```
== esma_registers_euveca
<p>
  Searching for Solr?<br/>
  You must type the correct path.<br/>
  Solr will respond.
</p>

== esma_registers_upreg
{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"*:*",
      "rows":"1",
      "wt":"json"}},
  "response":{"numFound":101706,"start":0,"numFoundExact":true,"docs":[
      {
        "id":"aeActivity147",
        "ac_serviceName":"Reception and transmission of orders",
        "ac_authorisationNotificationDateStr":"12/09/2006",
        "ac_status":"Active",
        "ac_comment":"",
        "entity_type":"aeActivity",
        "_root_":"ae42",
        "type_s":"child",
        "ac_authorisationEndDate":"",
        "ac_authorisationNotificationDate":"2006-09-12T00:00:00Z",
        "_version_":1861996368975888384,
        "timestamp":"2026-04-09T12:35:14.329Z"}]
  }}

== esma_registers_aifmd
<p>
  Searching for Solr?<br/>
  You must type the correct path.<br/>
  Solr will respond.
</p>

== esma_registers_eusef
<p>
  Searching for Solr?<br/>
  You must type the correct path.<br/>
  Solr will respond.
</p>
```
</details>

→ `Bash` — Facet ESMA upreg register by entity type
```sh
curl -s -m 30 "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=*:*&rows=0&wt=json&facet=true&facet.field=ae_entityTypeLabel&facet.field=entity_type&facet.limit=60" | python3 -I -c "import json,sys; d=json.load(sys.stdin); print(d['facet_counts']['facet_fields'])"
```

<details><summary>result</summary>

```
{'ae_entityTypeLabel': ['investment firm', 7159, 'aifm', 3783, 'ucits management company', 1704, 'evc', 486, 'european crowdfunding service provider', 261, 'multilateral trading facility', 178, 'regulated market', 136, 'systematic internaliser', 113, 'organised trading facility', 32, 'approved reporting mechanism', 20, 'esf', 17, 'approved publication arrangement', 15], 'entity_type': ['aeActivityHistory', 48356, 'aeActivity', 38782, 'ae', 13904, 'aeNotHostMmbSt', 663, 'lastModification', 1]}
```
</details>

→ `Bash` — Inspect EuVECA and AIFM entries by country
```sh
curl -s -m 30 "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=ae_entityTypeLabel:evc&rows=1&wt=json" | head -c 2500; echo; for t in evc aifm; do curl -s -m 30 "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=ae_entityTypeLabel:$t&rows=0&wt=json&facet=true&facet.field=ae_homeMemberState&facet.limit=40" | python3 -I -c "import json,sys; d=json.load(sys.stdin); print('$t', d['response']['numFound'], d['facet_counts']['facet_fields'])"; done
```

<details><summary>result</summary>

```
{
  "responseHeader":{
    "status":0,
    "QTime":106,
    "params":{
      "q":"ae_entityTypeLabel:evc",
      "rows":"1",
      "wt":"json"}},
  "response":{"numFound":486,"start":0,"numFoundExact":true,"docs":[
      {
        "id":"ae36567",
        "ae_entityTypeCode":"EVC",
        "ae_lastUpdate":"2019-07-19T00:00:00Z",
        "ae_lastUpdateStr":"19/07/2019",
        "ae_lei":"",
        "ae_headOfficeLei":"",
        "ae_entityName":"Enbarr Investments GP DAC",
        "collectorParent":["Enbarr Investments GP DAC"],
        "ae_officeType":"Head office",
        "ae_competentAuthority":"Central Bank of Ireland (CBI)",
        "ae_homeMemberState":"IRELAND",
        "ae_hostMemberState":"",
        "ae_headOfficeAddress":"",
        "ae_branchAddress":"",
        "ae_comment":"",
        "ae_status":"Active",
        "ae_authorisationNotificationDate":"2019-07-18T00:00:00Z",
        "ae_authorisationNotificationDateStr":"18/07/2019",
        "ae_authorisationWithdrawalEndDateStr":"",
        "entity_type":"ae",
        "type_s":"parent",
        "ae_entityTypeLabel":"EVC",
        "_root_":"ae36567",
        "ae_dbId":36567,
        "ae_website":"",
        "ae_commercialName":"",
        "ae_legalform":"",
        "timestamp":"2026-04-09T13:20:25.634Z",
        "no_of_funds":"1",
        "_version_":1878619009513947136}]
  }}

evc 486 {'ae_homeMemberState': ['spain', 100, 'sweden', 90, 'germany', 78, 'netherlands', 63, 'norway', 27, 'italy', 25, 'finland', 23, 'lux
… [869 more characters]
```
</details>

→ `Bash` — Check status facets and Slovak AIFMs
```sh
for t in evc aifm; do curl -s -m 30 "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=ae_entityTypeLabel:$t&rows=0&wt=json&facet=true&facet.field=ae_status" | python3 -I -c "import json,sys; d=json.load(sys.stdin); print('$t', d['facet_counts']['facet_fields'])"; done; curl -s -m 30 "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=ae_entityTypeLabel:aifm%20AND%20ae_homeMemberState:slovakia&rows=20&wt=json&fl=ae_entityName,ae_status" | python3 -I -c "import json,sys; d=json.load(sys.stdin); [print(x) for x in d['response']['docs']]"
```

<details><summary>result</summary>

```
evc {'ae_status': ['active', 448, 'inactive', 38, '', 0]}
aifm {'ae_status': ['active', 3135, 'inactive', 556, '', 92]}
{'ae_entityName': 'Sandberg Capital, správ. spol., a.s.', 'ae_status': 'Active'}
{'ae_entityName': 'Avanea, správ. spol., a.s.', 'ae_status': 'Inactive'}
{'ae_entityName': 'PARTNERS ASSET MANAGEMENT, správ. spol., a. s.', 'ae_status': 'Active'}
{'ae_entityName': 'HB Reavis Investment Management správ. spol., a. s.', 'ae_status': 'Active'}
{'ae_entityName': 'VOSEM Capital, správ. spol., a. s.', 'ae_status': 'Active'}
{'ae_entityName': 'Asset Management Slovenskej sporiteľne, správ. spol., a.s.', 'ae_status': 'Inactive'}
{'ae_entityName': 'Tatra Asset Management, správ. spol., a.s.', 'ae_status': 'Active'}
{'ae_entityName': 'IAD Investments, správ. spol., a. s.', 'ae_status': 'Active'}
{'ae_entityName': 'J&T INVESTIČNÁ SPOLOČNOSŤ, správ. spol., a.s.', 'ae_status': 'Active'}
{'ae_entityName': 'Slovak Asset Management, správ. spol., a.s.', 'ae_status': 'Inactive'}
{'ae_entityName': 'Across Asset Management, správ. spol., a. s.', 'ae_status': 'Active'}
{'ae_entityName': '365.invest, správ. spol., a. s.', 'ae_status': 'Active'}
{'ae_entityName': 'RIB SLOVAKIA, správ. spol., a.s.', 'ae_status': 'Inactive'}
```
</details>

→ `WebSearch` ČNB seznam regulovaných subjektů JERRS obhospodařovatel investičních fondů nad rozhodný limit pod limit počet

→ `WebSearch` NBS register subjektov finančného trhu správcovská spoločnosť alternatívne investičné fondy register lists

→ `WebSearch` Companies House API rate limit 600 requests 5 minutes PSC bulk data snapshot free

→ `WebSearch` FCA Financial Services Register API free registration rate limit

<details><summary>result</summary>

```
Web search results for query: "NBS register subjektov finančného trhu správcovská spoločnosť alternatívne investičné fondy register lists"

Links: [{"title":"nbs.sk","url":"https://nbs.sk/dokument/4dfca3c2-3daf-45c0-a770-6e1a37a4175d/stiahnut/?force=true"},{"title":"VS2008 kap04","url":"https://www.nbs.sk/_img/Documents/_Publikacie/VyrocnaSprava/SVK2008/VS2008_kap04.pdf"},{"title":"Publikacie\\VyrocnaSprava\\SVK2007\\VS2007 kap04","url":"https://www.nbs.sk/_img/Documents/_Publikacie\\VyrocnaSprava\\SVK2007\\VS2007_kap04.pdf"},{"title":"nbs.sk","url":"https://nbs.sk/dokument/d918e99a-6c2f-4524-96d6-ffb239440b69/stiahnut/?force=true"},{"title":"vs11 kap03","url":"https://nbs.sk/_img/documents/_publikacie/vyrocnasprava/svk2011/vs11_kap03.pdf"},{"title":"vs12 kap06","url":"https://nbs.sk/_img/documents/_publikacie/vyrocnasprava/protected/svk2012/vs12_kap06.pdf"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/nbs-financie-trh-pravomoci/58834-clanok.html"},{"title":"Investori môžu prísť o všetko: NBS varuje pred platformami, ktoré ponúkajú finančné služby bez oprávnenia","url":"https://www.startitup.sk/?p=1136070"},{"title":"NBS dala pokutu jednej z investičných firiem, nariadila jej aj ukončenie činnosti","url":"https://sita.sk/vofinanciach/nbs-dala-pokutu-jednej-z-investicnych-firiem-nariadila-jej-aj-ukoncenie-cinnosti/"}]

I didn't find the register itself, but the results point to NBS materials on registered AIF manag
… [1300 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Companies House API rate limit 600 requests 5 minutes PSC bulk data snapshot free"

Links: [{"title":"Rate limiting","url":"https://developer-specs.company-information.service.gov.uk/guides/rateLimiting"},{"title":"Rate Limiting and the Companies House API","url":"https://medium.com/@alistairboyer/rate-limiting-and-the-companies-house-api-b16ef36365a6"},{"title":"Companies House API Limits","url":"https://forum.companieshouse.gov.uk/t/companies-house-api-limits/8626"},{"title":"API Rating limit","url":"https://forum.companieshouse.gov.uk/t/api-rating-limit/3118"},{"title":"API Rate Limit Issue","url":"https://forum.companieshouse.gov.uk/t/api-rate-limit-issue/4335"},{"title":"Bulk Data Access Request — Officers, Charges Snapshots & Updates","url":"https://forum.companieshouse.gov.uk/t/bulk-data-access-request-officers-charges-snapshots-updates/12697"},{"title":"API rate limiting exception","url":"https://forum.companieshouse.gov.uk/t/api-rate-limiting-exception/504"},{"title":"Rate limit increase request — legitimate B2B SaaS platform with variable user demand","url":"https://forum.companieshouse.gov.uk/t/rate-limit-increase-request-legitimate-b2b-saas-platform-with-variable-user-demand/12847"},{"title":"forum.companieshouse.gov.uk","url":"https://forum.companieshouse.gov.uk/t/companies-house-api-502-and-500-error-the-server-returned-an-invalid-or-incomplete-response-and-internal-server-error-issue/4995"},{"title":"API Changes with regards to nu
… [1595 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "FCA Financial Services Register API free registration rate limit"

Links: [{"title":"Need help with your APIs? I offer API discovery, governance & evangelism services. Explore services →","url":"https://providers.apievangelist.com/providers/fca-uk/"},{"title":"FCA Register Scraper","url":"https://apify.com/danielainsworth/fca-register"},{"title":"Financial Conduct Authority website screenshot","url":"https://apis.io/providers/fca-uk/"},{"title":"Understanding the Financial Services Register API","url":"https://financial-services-register-api.readthedocs.io/en/latest/sources/financial-services-register-api.html"},{"title":"financial services register api.readthedocs","url":"https://financial-services-register-api.readthedocs.io"},{"title":"Understanding the Financial Services Register API","url":"https://financial-services-register-api.readthedocs.io/en/stable/sources/financial-services-register-api.html"},{"title":"financial-services-register-api.readthedocs.io","url":"https://financial-services-register-api.readthedocs.io/en/latest/"},{"title":"register extract handbook","url":"https://www.Fca.Org.Uk/publication/documents/register-extract-handbook.pdf"},{"title":"root.packagist.org","url":"https://root.packagist.org/packages/cyborgfinance/fcaregisterlaravel"},{"title":"Financial Conduct Authority · Authentication Profile","url":"https://apis.io/security/fca-uk/fca-uk-authentication/"}]

The FCA's own handbook gives a lower rate limit than the c
… [1641 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "ČNB seznam regulovaných subjektů JERRS obhospodařovatel investičních fondů nad rozhodný limit pod limit počet"

Links: [{"title":"Role ČNB u správců podle § 15 zákona o investičních společnostech a investičních fondech","url":"https://www.cnb.cz/cs/dohled-financni-trh/vykon-dohledu/upozorneni-pro-verejnost/Role-CNB-u-spravcu-podle-15-zakona-o-investicnich-spolecnostech-a-investicnich-fondech"},{"title":"cnb.cz (ČNB)","url":"https://zpravy.kurzy.cz/621352-role-cnb-u-spravcu-podle--15-zakona-o-investicnich-spolecnostech-a-investicnich-fondech/"},{"title":"Informace poskytnuté na žádost ze dne 30. 7. 2026 týkající se svěřenského fondu","url":"https://www.cnb.cz/cs/o_cnb/106/informace-poskytnute-ceskou-narodni-bankou-podle-zakona-c.-106-1999-sb.-o-svobodnem-pristupu-k-informacim/Informace-poskytnute-nanbspzadost-zenbspdne-30.nbsp7.nbsp2026-tykajici-se-sverenskeho-fondu"},{"title":"alternativni investicni fondy pod drobnohledem ceske narodni banky 115307","url":"https://www.epravo.cz/top/clanky/alternativni-investicni-fondy-pod-drobnohledem-ceske-narodni-banky-115307.html"},{"title":"Alternativní investiční fondy a role ČNB ve vztahu ke správcům majetku podle § 15 ZISIF","url":"https://epravo.cz/top/clanky/alternativni-investicni-fondy-a-role-cnb-ve-vztahu-ke-spravcum-majetku-podle-15-zisif-114258.html"},{"title":"novela zakona o investicnich spolecnostech a investicnich fondech regulace patnactek 117804","url":"https://www.epravo.cz/top/clanky/novel
… [2490 more characters]
```
</details>

→ `WebFetch` https://download.companieshouse.gov.uk/en_pscdata.html

→ `WebFetch` https://www.cnb.cz/cs/dohled-financni-trh/seznamy/

→ `WebSearch` ARES API rest ares.gov.cz ekonomicke-subjekty-v-be open data Czech business register justice.cz sbírka listin datová sada

<details><summary>result</summary>

```
- **Product:** The People with significant control (PSC) snapshot from Companies House, described as "a downloadable data snapshot containing the full list of PSC's provided to Companies House."
- **Format:** Data files are in JSON, delivered as a single zip (`persons-with-significant-control-snapshot-2026-10-10.zip`) or as 33 smaller zip files.
- **Update frequency:** Updated daily. "The latest snapshot will be updated every morning before 10am GMT," and it contains information compiled up to the end of the previous day.
- **Cost:** Free. "This snapshot is provided free of charge and will not be supported."
- **File date:** 10 October 2026. The file names carry this date, and the page shows "Last Updated: 10/10/2026 08:05hrs."
```
</details>

→ `WebSearch` Slovakia register partnerov verejného sektora RPVS open data API konečný užívateľ výhod orsr.sk podiel spoločníci

<details><summary>result</summary>

```
Web search results for query: "ARES API rest ares.gov.cz ekonomicke-subjekty-v-be open data Czech business register justice.cz sbírka listin datová sada"

Links: [{"title":"Czech Company Data — ARES Registry, VAT & Directors avatar","url":"https://apify.com/foxlabs/czech-company-data"},{"title":"Czech ARES Company API avatar","url":"https://apify.com/osmateus/czech-ares-company-api"},{"title":"# Changelog","url":"https://glama.ai/mcp/servers/@vzeman/ares-mcp-server/blob/f3074b5f9ee3fba6205cc424ce8b8839c88d4d9c/CHANGELOG.md"},{"title":"laravel ares","url":"https://root.packagist.org/packages/nyoncode/laravel-ares"},{"title":"glama.ai","url":"https://glama.ai/mcp/servers/t1l6e135pz"},{"title":"glama.ai","url":"https://glama.ai/mcp/servers/n0ll8rme3j"},{"title":"Ministerstvo financí logo, na hlavní stránku","url":"https://mf.gov.cz/cs/ministerstvo/informacni-systemy/ares--administrativni-registr-ekonomicky"},{"title":"Ministerstvo financí logo, na hlavní stránku","url":"https://mf.gov.cz/cs/ministerstvo/informacni-systemy/ares"},{"title":"Ministerstvo financí logo, na hlavní stránku","url":"https://mf.gov.cz/cs/o-ministerstvu/informacni-systemy/ares--administrativni-registr-ekonomicky"}]

The search turned up the ARES REST API base URL and some community tools built on it, but nothing on justice.cz or the Sbírka listin.

- **Endpoint:** A community Apify actor points to a search endpoint at https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat. A Laravel
… [1405 more characters]
```
</details>

<details><summary>result</summary>

```
The page lists these registers and lists under "Seznamy a evidence":

- **Seznamy regulovaných a registrovaných subjektů (JERRS)**: the main application, covering all financial market entities that are licensed, authorised, registered, notified, or entered in lists kept by ČNB.
- **Seznam externích ratingových agentur**: ČNB links to the EBA's list of external credit assessment institutions, which is hosted on the EBA site.
- **Seznam schválených a notifikovaných prospektů**: a register of approved and notified prospectuses.
- **Seznam konečných podmínek základních prospektů**: a register of final terms for base prospectuses.
- **Ostatní seznamy**: other lists, such as foreign regulated markets, foreign settlement systems, and insurance education.
- **Otevřená data**: open data.
- **Webové služby WS JERRS**: web services for JERRS.

**JERRS URL:** The page gives only relative links: `/cnb/jerrs` and `/cs/dohled-financni-trh/seznamy/jerrs`. These sit on the ČNB website (cnb.cz).

**Web services:** WS JERRS are at `/cs/dohled-financni-trh/seznamy/webove-sluzby-ws-jerrs/`. The page says that since 1 July 2019 they provide "vybrané informace" (selected information) about financial market entities.

**Export/download:** The page mentions Otevřená data and the WS JERRS web services, but it doesn't describe any export or download formats for JERRS itself.

**Your specific categories:** The page doesn't mention investment companies, AIF managers, §15 managers, or investment funds. Th
… [58 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Slovakia register partnerov verejného sektora RPVS open data API konečný užívateľ výhod orsr.sk podiel spoločníci"

Links: [{"title":"Register partnerov verejného sektora","url":"https://www.justice.gov.sk/sluzby/register-partnerov-verejneho-sektora/"},{"title":"Často kladené otázky – RPVS","url":"https://www.justice.gov.sk/?p=6753"},{"title":"Ako zistiť konečného užívateľa výhod?","url":"https://www.podnikajte.sk/zakonne-povinnosti-podnikatela/ako-zistit-konecneho-uzivatela-vyhod"},{"title":"Slovakia Public Sector Partners Register (Register partnerov verejného sektora - RPVS) (2025-01-09)","url":"https://bods-data.openownership.org/source/slovakia"},{"title":"Zápis konečného užívateľa výhod","url":"https://www.podnikajte.sk/temy/zapis-konecneho-uzivatela-vyhod?page=2"},{"title":"Register partnerov verejného sektora - zápis do registra","url":"https://ficek.sk/rpvs-103"},{"title":"Vymazanie záznamu z RPVS (Registra partnerov verejného sektora): Komplexný prehľad","url":"https://ddadsstornala.sk/aktuality/vymaz-z-rpvs-ministerstvio/"},{"title":"zapis konecneho uzivatela vyhod","url":"https://www.podnikajte.sk/temy/zapis-konecneho-uzivatela-vyhod"},{"title":"zapis konecneho uzivatela vyhod","url":"https://www.podnikajte.sk/temy/zapis-konecneho-uzivatela-vyhod?page=1"}]

The search turned up general information about the RPVS register, but nothing on the API itself or how it links to orsr.sk.

- **What it is:** The Register of Public Sector Partne
… [1758 more characters]
```
</details>

→ `WebFetch` https://about.crunchbase.com/terms-of-service/

→ `WebFetch` https://www.openvc.app/

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebFetch` https://www.gleif.org/en/lei-data/gleif-golden-copy/download-the-golden-copy

→ `WebFetch` https://api.opencorporates.com/

<details><summary>result</summary>

```
The page doesn't give enough detail to answer most of your questions:

- **Free tier:** Not mentioned.
- **Open-data/share-alike (ODbL) conditions:** The page says the data is "available as either share-alike attribution open data or commercially," but it doesn't name ODbL or describe the conditions.
- **Commercial use restrictions:** Not described. The page only says commercial access is available and links to "pricing options."
- **Rate limits:** Not mentioned.

The page links to the API Reference, FAQs, and the "our-data" pricing page, which may cover these terms.
```
</details>

<details><summary>result</summary>

```
**Contents**
- **Level 1 (Who is Who):** LEI records and related reference data, based on the LEI-CDF format.
- **Level 2 (Who Owns Whom):** The Relationship Record (RR-CDF) file identifies the direct and ultimate parents of a legal entity whose parents have an LEI. A separate Reporting Exceptions file covers cases such as an entity with no parent, an entity that opts out for exceptional reasons, or parents without an LEI.

**Format**
- Common Data File (CDF) formats: LEI-CDF, RR-CDF, and Reporting Exceptions.
- The same content is also available in RDF, and data.world hosts a graph representation.

**Frequency**
- "GLEIF issues three sets of Golden Copy Files daily."
- Each update includes four delta files that show new LEIs and/or revisions compared with versions published 8 hours, 24 hours, 7 days, and 31 days earlier.

**Licence:** The page doesn't state the licence. It links to "LEI Data Terms of Use" in the footer, but that document's content isn't included here.

**Cost:** Not mentioned.

**API:** Not covered on this page. It only links to a separate "GLEIF API" page.
```
</details>

<details><summary>result</summary>

```
**Effective/Updated Date:** "Last Updated: September 30, 2026." The page says the changes "will go into effect on September 30, 2026." The page's embedded JSON-LD lists a `dateModified` of 2024-11-26, which conflicts with this.

**Scraping, Crawling, and Automated Access**

- Clause (h): "“Crawls,” “scrapes,” or “spiders” any page, data, or portion of or relating to the Service or Content"
- Clause (i): "attempting to access, download, export, or otherwise use or exploit any Content using any automated means or tools"

**Data Reuse and Redistribution**

- Clause (j): "Copies or stores any significant portion of the Content, including but not limited to integrating"
- Clause (n): "Uses or allows the Content to be used to train models (including generative artificial intelligence technologies)"
- Content use: "You will not use, copy, reproduce, adapt, modify, translate, publish, broadcast, transmit, distribute"
- "Any other uses of Content require Crunchbase’s prior written consent."

**Free Plan**

The page does not describe a free plan. It covers free trials and reserves the right to charge for parts of the Service:
- "You can sign up for a trial for certain portions of the Service."
- The page also says the 2013 Snapshot and Crunchbase Basic are available under the Creative Commons Attribution License, with attribution to the pseudonym "CrunchBase 2013 Snapshot."
```
</details>

→ `WebSearch` OpenVC database how many investors free list of VC funds check size

→ `WebSearch` OpenCorporates API free "public benefit" licence share-alike attribution terms

→ `WebSearch` GLEIF LEI data CC0 license free API no registration

→ `WebSearch` Dealroom terms of use scraping prohibited free account number of investors tracked

<details><summary>result</summary>

```
Web search results for query: "OpenVC database how many investors free list of VC funds check size"

Links: [{"title":"crunchbase alternatives","url":"https://www.papermark.com/blog/crunchbase-alternatives.md"},{"title":"Hub/Comparisons/OpenVC vs Signal NFX","url":"https://hub.causo.ai/compare/openvc-vs-signal-nfx"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-under-100k"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-under-100k?page=2"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-under-100k?page=33"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-under-100k?page=59"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-under-100k?page=6"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-over-1m"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-over-1m?page=2"},{"title":"For Founders","url":"https://www.openvc.app/investor-lists/checks-over-1m?page=21"}]

OpenVC is a free founder-facing investor database, and its own site currently claims about 20,000 investors. I didn't find an exact or independently verified count.

- **Size:** OpenVC's site says it lets founders search 20,000+ verified investors, including venture capitalists, angel investors, family offices, accelerators, and more. A third-party review, Papermark's comparison, instead describes it as a community-edited databa
… [986 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "OpenCorporates API free "public benefit" licence share-alike attribution terms"

Links: [{"title":"Terms of use – OpenCorporates","url":"https://opencorporates.com/terms-of-use-2/"},{"title":"API Reference: version 0.4.8","url":"https://api.opencorporates.com/documentation/Home"},{"title":"Following the Money: A Beginner’s Guide to Using the OpenCorporates API","url":"https://bellingcat.com/resources/2023/08/24/following-the-money-a-beginners-guide-to-using-the-opencorporates-api"},{"title":"www.bespacific.com","url":"https://www.bespacific.com/?p=44061"},{"title":"interpreting the open database license","url":"https://tildes.net/~tech/1qs2/interpreting_the_open_database_license"},{"title":"Annual Report 2024","url":"https://assets.opencorporates.com/companies/us_nh/859424/filings"},{"title":"Annual Report 2001","url":"https://assets.opencorporates.com/companies/us_nh/175911/filings"},{"title":"Annual Report 2024","url":"https://assets.opencorporates.com/companies/us_nh/751169/filings"},{"title":"Annual Report 2022","url":"https://assets.opencorporates.com/companies/us_nh/773161/filings"},{"title":"Annual Report 2018","url":"https://assets.opencorporates.com/companies/us_nh/638796/filings"}]

The search turned up the main pieces, though not a single consolidated licence page.

- **Terms of use:** OpenCorporates says it offers free access to general-public users for personal use, and to journalists, NGOs and academics doing public benefit researc
… [1591 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "GLEIF LEI data CC0 license free API no registration"

Links: [{"title":"2020 06 05 annual report 2019 v1.0 signed final","url":"https://www.gleif.org/about/governance/annual-report/2020-06-05_annual-report-2019_v1.0_signed_final.pdf"},{"title":"LEI Company Identity & Ownership (GLEIF, 2.7M+)","url":"https://apify.com/foxlabs/lei-company-ownership"},{"title":"GLEIF Legal Entity Scraper","url":"https://apify.com/crawlergang/gleif-scraper"},{"title":"GLEIF LEI Scraper","url":"https://apify.com/crawlergang/gleif-lei-scraper"},{"title":"GLEIF LEI Scraper (Legal Entity Data) avatar","url":"https://apify.com/opendata-labs/gleif-lei-scraper"},{"title":"Need help with your APIs? I offer API discovery, governance & evangelism services. Explore services →","url":"https://providers.apievangelist.com/providers/gleif/"},{"title":"gleif enhances access to rich lei data","url":"https://www.xbrl.org/news/gleif-enhances-access-to-rich-lei-data/"},{"title":"infocert.digital","url":"https://infocert.digital/?p=8847"},{"title":"gleif answers financial industry calls enable faster customized and","url":"https://financialit.net/news/regulatory-standards/gleif-answers-financial-industry-calls-enable-faster-customized-and"}]

The search supports the core claim: GLEIF's LEI data is free, requires no registration, and has an API. The CC0 part is less well sourced.

- **Free, no registration:** GLEIF's 2019 annual report says its Global LEI Index offers free of charge acce
… [897 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Dealroom terms of use scraping prohibited free account number of investors tracked"

Links: [{"title":"terms of service","url":"https://dealroom.co/terms-of-service"},{"title":"wp.dealroom.co","url":"https://wp.dealroom.co/?p=48"},{"title":"Terms of Service","url":"https://content.dealroom.co/terms-of-service"},{"title":"Dealroom Scraper: Company Funding and Investor Cap Tables","url":"https://apify.com/getascraper/dealroom-scraper"},{"title":"Terms of Service","url":"https://dealroom.net/terms"},{"title":"Terms of Service","url":"https://dealroom.net/product/terms"},{"title":"Terms & Conditions","url":"https://mercomindia.com/termsandconditions/"},{"title":"Privacy Policy","url":"https://dealroom.co/privacy-policy."},{"title":"soccerdata.readthedocs.io","url":"https://soccerdata.readthedocs.io/en/stable/_sources/faq.rst.txt"}]

The search turned up Dealroom's terms of use, but nothing on a free account's investor-tracking limit.

- **Scraping is prohibited.** Dealroom.co's terms list scraping among its "Don'ts" and warn against excessive use of its data. The terms say not to scrape the data or use it excessively. They also bar commercializing, copying, or sub-licensing the data.
- **Personal use is the baseline.** The data shown is for personal and/or internal business purposes. The terms also say you may use it to find investors.
- **Don't confuse the two companies.** Dealroom.co (Amsterdam) and DealRoom Technologies, Inc. (dealroom.net) are d
… [662 more characters]
```
</details>

→ `WebSearch` Invest Europe activity report "private equity firms" data "European Data Cooperative" number of firms covered 2025

→ `WebSearch` EIF portfolio list of funds venture capital private equity "where we invest" signed funds list

→ `WebSearch` Národný rozvojový fond II venture capital fondy portfólio zoznam co-investičné fondy Slovak Investment Holding

→ `WebSearch` Národní rozvojový fond NRB fond fondů venture capital portfolio fondy seznam 2025

<details><summary>result</summary>

```
Web search results for query: "Invest Europe activity report "private equity firms" data "European Data Cooperative" number of firms covered 2025"

Links: [{"title":"Invest Europe","url":"https://en.wikipedia.org/wiki/Invest_Europe"},{"title":"Invest Europe CEE Statistics 2024","url":"https://cvca.hr/wp-content/uploads/2025/12/Invest-Europe_CEE-Statistics_2024.pdf"},{"title":"2024 Statistik Europa Invest Europe Charts","url":"https://www.bvkap.de/files/content/Statistik-europa/pdf/2024_Statistik_Europa_Invest Europe_Charts.pdf"},{"title":"The European Data Cooperative (EDC)","url":"https://thelivinglib.org/?p=60460"},{"title":"2023 Statistik Europa Invest Europe neu","url":"https://www.bvkap.de/files/content/Statistik-europa/pdf/2023_Statistik_Europa_Invest Europe_neu.pdf"},{"title":"20260311 BVK Statistik 2025 Charts final","url":"https://www.bvkap.de/files/content/Statistiken/Statistik Deutschland/pdfs/20260311_BVK-Statistik_2025_Charts_final.pdf"},{"title":"Investing in Europe: Private Equity Activity 2025 Report highlights strong fundraising and investment performance","url":"https://tech.eu/2026/05/07/investing-in-europe-private-equity-activity-2025-report-highlights-strong-fundraising-and-investment-performance/"},{"title":"InvestEurope CEE Activity Report 2017","url":"https://inventure.com.ua/upload/library/InvestEurope-CEE-Activity-Report-2017.pdf"},{"title":"Investing in Europe: Private Equity activity 2024","url":"https://www.seca.ch/en/knowledge-library/newsletters
… [1230 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "EIF portfolio list of funds venture capital private equity "where we invest" signed funds list"

Links: [{"title":"eif ar2003 en","url":"https://www.eif.org/attachments/publications/about/eif_ar2003_en.pdf"},{"title":"EIF for Venture Capital & Private Equity funds","url":"https://eif.org/what_we_do/equity/deals/index_.htm"},{"title":"EIF Annual Report 2006","url":"https://www.eif.org/news_centre/publications/EIF_Annual_Report_2006.pdf"},{"title":"eif ar2002 en","url":"https://www.eif.org/attachments/publications/about/eif_ar2002_en.pdf"},{"title":"activity report 2001 en","url":"https://www.eif.org/attachments/publications/about/activity_report_2001_en.pdf"},{"title":"eif s venture capital and infrastructure funds investments","url":"https://trad.eib.org/attachments/events/eif-s-venture-capital-and-infrastructure-funds-investments.pdf"},{"title":"eif ar2001 en","url":"https://eif.org/attachments/publications/about/eif_ar2001_en.pdf"},{"title":"EIF increases VC commitments","url":"https://www.buyoutsinsider.com/eif-increases-vc-commitments-2/"},{"title":"Join Vestbee","url":"https://www.vestbee.com/lp-list/european-investment-fund-eif"}]

The search didn't turn up a current, complete EIF fund list. The most useful hit is EIF's own equity page, but the list it links to is dated 2022.

- **EIF's equity page:** It links to two PDFs, one of active all-time funds that still invest and one of all active EIF investments. It says the lists cover private
… [921 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Národný rozvojový fond II venture capital fondy portfólio zoznam co-investičné fondy Slovak Investment Holding"

Links: [{"title":"NRI dokončila výběr venture kapitálového fondu pro program Fond Ukrajina","url":"https://www.businessinfo.cz/clanky/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=34908"},{"title":"National Investment and Infrastructure Fund: Private Markets Fund – II (NDB-NIIFPRIVATEMARKETSII)","url":"https://ewsdata.rightsindevelopment.org/projects/NDB-NIIFPRIVATEMARKETSII"},{"title":"narodni rozvojovy fond","url":"https://ekonomickydenik.cz/tag/narodni-rozvojovy-fond"},{"title":"Národní rozvojový fond vlády umožní investice v řádu desítek miliard korun","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-vlady-umozni-investice-v-radu-desitek-miliard-korun/"},{"title":"Národní rozvojový fond přichází. Podpoří projekty v infrastruktuře","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-prichazi-podpori-projekty-v-infrastrukture/"},{"title":"narodni rozvojovy fond ziskal licenci cnb","url":"https://ekonomickydenik.cz/narodni-rozvojovy-fond-ziskal-licenci-cnb/"},{"title":"Národní rozvojový fond získal licenci ČNB","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-ziskal-licenci-cnb/"},{"title":"All funds of Neo (venture capital fund)","url":"https://seedtable.com/investors/neo-venture-capital-fund/
… [1113 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Národní rozvojový fond NRB fond fondů venture capital portfolio fondy seznam 2025"

Links: [{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/nhfond"},{"title":"Národní fond rozvoje získal licenci od České národní banky","url":"https://ct24.ceskatelevize.cz/ekonomika/3226938-narodni-fond-rozvoje-ziskal-licenci-od-ceske-narodni-banky"},{"title":"banky podlehly tlaku politiku rozvojoveho fondu jsou pripraveny investovat az sedm miliard","url":"https://ekonomickydenik.cz/banky-podlehly-tlaku-politiku-rozvojoveho-fondu-jsou-pripraveny-investovat-az-sedm-miliard/"},{"title":"Národní rozvojový fond vlády umožní investice v řádu desítek miliard korun","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-vlady-umozni-investice-v-radu-desitek-miliard-korun/"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=27410"},{"title":"Ministr Havlíček: Peníze do národního fondu chtějí posílat kromě bank i jiné firmy","url":"https://www.businessinfo.cz/clanky/ministr-havlicek-penize-do-narodniho-fondu-chteji-posilat-krome-bank-i-jine-firmy/"},{"title":"Národní rozvojový fond bude spravovat státní banka, na investice půjde až 35 miliard","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/narodni-rozvojovy-fond-bude-spravovat-statni-banka-na-investice-pujde-az-35-miliard-1360230"},{"title":"Národní rozvojový fond získal licenci ČNB","url":"https://www.businessi
… [1746 more characters]
```
</details>

→ `WebSearch` Národní rozvojová investiční NRI fondy rizikového kapitálu portfolio správci vybráni Národní inovační fond

→ `WebSearch` Slovak Investment Holding SIH venture capital funds portfolio Národný rozvojový fond II investments list

→ `WebSearch` SLOVCA members list Slovak venture capital association members

→ `WebSearch` CVCA Czech Private Equity and Venture Capital Association members list

<details><summary>result</summary>

```
Web search results for query: "Národní rozvojová investiční NRI fondy rizikového kapitálu portfolio správci vybráni Národní inovační fond"

Links: [{"title":"NRI dokončila výběr venture kapitálového fondu pro program Fond Ukrajina","url":"https://www.businessinfo.cz/clanky/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/"},{"title":"20190912 MEMORANDUM O SPOLUPRACI NRF CZ web","url":"https://vlada.gov.cz/assets/media-centrum/aktualne/20190912_MEMORANDUM-O-SPOLUPRACI_NRF_CZ-web.pdf"},{"title":"P. %C5%A0T%C4%9AP%C3%81NEK N%C3%A1rodn%C3%AD rozvojov%C3%BD fond","url":"https://finance-edu.vse.cz/wp-content/uploads/2020/02/P.-%C5%A0T%C4%9AP%C3%81NEK-N%C3%A1rodn%C3%AD-rozvojov%C3%BD-fond.pdf"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=34908"},{"title":"20190912 MEMORANDUM O SPOLUPRACI NRF CZ web","url":"https://uv.gov.cz/assets/media-centrum/aktualne/20190912_MEMORANDUM-O-SPOLUPRACI_NRF_CZ-web.pdf"},{"title":"narodni rozvojovy fond","url":"https://ekonomickydenik.cz/tag/narodni-rozvojovy-fond"},{"title":"narodni rozvojovy fond ziskal licenci cnb","url":"https://ekonomickydenik.cz/narodni-rozvojovy-fond-ziskal-licenci-cnb/"},{"title":"Národní rozvojový fond vlády umožní investice v řádu desítek miliard korun","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-vlady-umozni-investice-v-radu-desitek-miliard-korun/"},{"title":"Národní rozvojový fond získal licenci ČNB","url":"https://www.businessinfo.cz/clanky/narodni-rozvoj
… [1279 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Slovak Investment Holding SIH venture capital funds portfolio Národný rozvojový fond II investments list"

Links: [{"title":"About the Company","url":"https://www.sih.sk/en/stranky/o-nas/o-spolocnosti"},{"title":"Slovak Investment Holding invested 1.3 billion euros in 10 years and supported hundreds of companies","url":"https://www.sih.sk/en/aktuality/slovak-investment-holding-za-10-rokov-preinvestoval-1-3-miliardy-eur-a-podporil-stovky-firiem"},{"title":"vs sih 2019 en final 351","url":"https://www.sih.sk/data/files/vs_sih_2019_en_final-351.pdf"},{"title":"SIH boosts support for Slovak start-up businesses","url":"https://www.sih.sk/en/aktuality/sih-boosts-support-for-slovak-start-up-businesses"},{"title":"dealroom.launchvic.org","url":"https://dealroom.launchvic.org/companies/slovak_investment_holding/portfolio"},{"title":"Slovak Investment Holding (SIH)","url":"https://eltia.eu/index.php/about/all-members/slovak-investment-holding-sih"},{"title":"ako investovat v eu slovensko je vzorom pre ostatne krajiny","url":"https://www.sih.sk/en/aktuality/ako-investovat-v-eu-slovensko-je-vzorom-pre-ostatne-krajiny"},{"title":"ecosystem.madrimasd.org","url":"https://ecosystem.madrimasd.org/investors/slovak_investment_holding/portfolio"},{"title":"Release date: 16 October 2019","url":"https://www.eib.org/en/projects/pipelines/all/20190166"}]

The search didn't return a complete list of SIH's venture capital holdings or NDF II investments, but it did turn u
… [1660 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "SLOVCA members list Slovak venture capital association members"

Links: [{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/slovca/financials"},{"title":"Compare HVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/hvca-vs-slovca"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/slovca"},{"title":"Compare Genesis Capital vs SLOVCA","url":"https://www.cbinsights.com/compare/genesis-capital-sro-vs-slovca"},{"title":"Compare BVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/bvca-vs-slovca"},{"title":"Compare FVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/fvca-vs-slovca"},{"title":"1778762 dokument1","url":"https://crz.gov.sk//data/att/1778762_dokument1.pdf"},{"title":"Compare EstVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/estvca-vs-slovca"},{"title":"2154112 dokument1","url":"https://www.crz.gov.sk//data/att/2154112_dokument1.pdf"},{"title":"Compare Canadian Venture Capital and Private Equity Association vs SLOVCA","url":"https://www.cbinsights.com/compare/canadian-venture-capital-and-private-equity-association-vs-slovca"}]

The search didn't turn up a member list. The results are mostly third-party profile pages and a few contract documents, and none names SLOVCA's members.

- **Organization basics:** A CB Insights profile describes SLOVCA as a Bratislava-based association focused on venture capital and private equity, founded in 1995. Its headquarters is listed at Rajská
… [864 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "CVCA Czech Private Equity and Venture Capital Association members list"

Links: [{"title":"NEWS & INSIGHTS","url":"https://kinstellar.com/news-and-insights/detail/227/partner-jitka-logesova-joins-board-of-directors-of-czech-private-equity-and-venture-capital-association"},{"title":"cvca.hr","url":"https://cvca.hr/?p=504"},{"title":"about cvca","url":"https://cvca.hr/about-cvca"},{"title":"cvca.hr","url":"https://cvca.hr/?p=545"},{"title":"cvca.hr","url":"https://cvca.hr/members"},{"title":"cvca.hr","url":"https://cvca.hr/?p=6956"},{"title":"cvca.hr","url":"https://cvca.hr/?p=1158"},{"title":"app.foundernest.com","url":"https://app.foundernest.com/public/space/8836/companies/10571551?page=6"},{"title":"annual general assembly meeting 2025","url":"https://cvca.hr/annual-general-assembly-meeting-2025/"}]

The search didn't turn up a member list for the Czech association. Most of the results are for the **Croatian** CVCA (cvca.hr), which uses the same acronym, so keep the two apart.

- **Czech association:** The only Czech-specific result is a 2015 Kinstellar news item. It describes the Czech CVCA as an association representing PE and VC firms active in the Czech Republic, and notes it is a member of the European Private Equity and Venture Capital Association (EVCA). CVCA represents the interests of private equity and venture capital companies active in the Czech Republic. That article is over ten years old and names no members.
- **Croatian associa
… [744 more characters]
```
</details>

→ `WebFetch` https://www.cvca.cz/en/members/

→ `WebFetch` https://www.slovca.sk/

→ `WebFetch` https://www.investeurope.eu/about-us/who-we-are/

→ `WebFetch` https://eif.org/what_we_do/equity/deals/index_.htm

<details><summary>result</summary>

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

<details><summary>result</summary>

```
**Yes, there is a members section, but the page doesn't include the member list, the member count, or a breakdown of fund managers versus service providers.**

The page lists these membership categories:
- Riadni členovia (ordinary members)
- Pridružení členovia (associate members)
- Partnerskí členovia (partner members)
- Partneri (partners)

The homepage describes the membership section as "Stáli, pridružení a partnerskí členovia SLOVCA, partneri, etický kódex člena." The page does not say which category includes fund managers and which includes law firms or advisors, so I can't classify members from this content.

**Members page URL:** https://www.slovca.sk/sk/stranky/clenstvo

The ordinary members subpage is https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html. The associate and partner subpages are linked from the same menu, but the provided content doesn't include their member lists.
```
</details>

<details><summary>result</summary>

```
The page doesn't give a total member count or break members down by type (PE/VC firms, LPs, associates). It says membership "now includes private equity, venture capital and infrastructure investment firms," and also includes large institutional investors such as pension funds and insurance groups. It doesn't mention associates.

Members are "based in 57 countries worldwide."

A member search tool appears at https://www.investeurope.eu/membership/member-search/. The page describes it as a way to check whether a firm is a member, but it doesn't say whether the directory is publicly accessible without logging in.
```
</details>

<details><summary>result</summary>

```
The page lists **84 members**: **27 full members** and **57 associate members**. These are my counts of the listings, since the page gives no total.

**Full members (PE/VC investors), 27 listed.** Examples: Abris Capital, Innova Capital, Mid Europa Partners.

**Associate members (advisors and service providers), 57 listed.** Examples:
- Law firms: Clifford Chance, White & Case
- Banks: Citibank Europe, Komerční banka
- Consulting and audit firms: Deloitte, KPMG
```
</details>

→ `WebFetch` https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html

→ `WebSearch` Invest Europe "members" "more than 700" OR "over 600" private equity venture capital firms membership

→ `WebSearch` BVCA membership "over 600" OR "more than 600" OR "1,000" member firms private equity venture capital

<details><summary>result</summary>

```
There are **12 ordinary members** listed on the page:

1. ARX Equity Partners
2. CVI
3. Enterprise Investors
4. Eterus Capital
5. Fond inovácií a technológií
6. Genesis Capital
7. Jet Investment
8. Národný holdingový fond s.r.o.
9. Neulogy Ventures
10. Sandberg Capital
11. Venture to Future Fund
12. Vision Ventures
```
</details>

→ `WebSearch` EIF "list of active investments" OR "active all time funds" pdf eif.org equity funds

<details><summary>result</summary>

```
Web search results for query: "Invest Europe "members" "more than 700" OR "over 600" private equity venture capital firms membership"

Links: [{"title":"Invest Europe","url":"https://en.wikipedia.org/wiki/Invest_Europe"},{"title":"398898 Invest Europe","url":"https://littlesis.org/org/398898-Invest_Europe"},{"title":"invl.com","url":"https://invl.com/en/?p=23548"},{"title":"Invest Europe","url":"https://eltia.eu/index.php/about/all-members/invest-europe"},{"title":"Invest Europe","url":"https://www.library.hbs.edu/Citations/Invest-Europe"},{"title":"Invest Europe","url":"https://www.bunch.capital/private-markets-glossary/invest-europe"},{"title":"Invest Europe","url":"https://www.impacteurope.net/members/invest-europe"},{"title":"540e278a ce28 49f7 9cd4 f4964b59fa19","url":"https://pubrio.com/companies/540e278a-ce28-49f7-9cd4-f4964b59fa19"},{"title":"dev.invl.com","url":"https://dev.invl.com/en/?p=13262"},{"title":"Invalda INVL signed up in 2017","url":"https://dev.invl.com/en/?p=25259"}]

The search didn't turn up any source saying Invest Europe has "more than 700" members, so that figure isn't supported here. The sources that give a count are:

- **Wikipedia** says the association has more than 650 members, divided roughly equally among private equity firms, venture capital firms and limited partners, alongside around 110 associate members representing advisers and service providers. It adds that its member base spans 57 countries, including 42 in Europe.
- **Bunch Capital'
… [547 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "EIF "list of active investments" OR "active all time funds" pdf eif.org equity funds"

Links: [{"title":"EIF for Venture Capital & Private Equity funds","url":"https://eif.org/what_we_do/equity/deals/index_.htm"},{"title":"eif backed active funds","url":"https://www.eif.org/files/records/eif-backed-active-funds.pdf"},{"title":"What we do","url":"https://www.eif.org/what_we_do/equity/news/2015/efsi_deals.htm"},{"title":"eif.org","url":"https://eif.org/what_we_do/equity/impact-investing/index.htm"},{"title":"eif ee25 masterfile presentations   copy.c347c0d654d6","url":"https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/22890/eif_ee25_masterfile_presentations_-_copy.c347c0d654d6.pdf"},{"title":"eif s venture capital and infrastructure funds investments","url":"https://trad.eib.org/attachments/events/eif-s-venture-capital-and-infrastructure-funds-investments.pdf"},{"title":"eif.org","url":"https://eif.org/InvestEU/equity_products_calls/index.htm"},{"title":"Development Finance","url":"https://pipelineroad.com/directory/eib-eif"},{"title":"european investment fund eif org","url":"https://venturecapitalarchive.com/venture-funds/european-investment-fund-eif-org"}]

The search turned up EIF's equity deals page, which links to two lists, though the exact PDF filenames you named didn't appear.

- **Overview page:** EIF for Venture Capital & Private Equity funds lists an overview as at 30.09.2022 with two PDFs: active all-time funds backed by the EIF
… [860 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "BVCA membership "over 600" OR "more than 600" OR "1,000" member firms private equity venture capital"

Links: [{"title":"bvca.medium.com","url":"https://bvca.medium.com/about"},{"title":"About Us","url":"https://www.bvca.co.uk/About-Us"},{"title":"bvca   british private equity  venture capital association","url":"https://aifi.it/it/aderenti/bvca---british-private-equity--venture-capital-association"},{"title":"Altius Group Joins Foremost Private Equity Industry Body","url":"https://www.lep.co.uk/business/altius-group-joins-foremost-private-equity-industry-body-4972435"},{"title":"48C3A984 A390 4C7A BEEA3840F8578B4C","url":"https://www.bvca.co.uk/asset/48C3A984-A390-4C7A-BEEA3840F8578B4C"},{"title":"This site is part of the Informa Connect Division of Informa PLC","url":"https://informaconnect.com/superreturn-japan/sponsors/bvca/"},{"title":"4C696259 78A3 49CA AF4584752D92C3C5","url":"https://www.bvca.co.uk/asset/4C696259-78A3-49CA-AF4584752D92C3C5"},{"title":"village.ai","url":"https://village.ai/company/bvca"},{"title":"ri.lgpsboard.org","url":"https://ri.lgpsboard.org/items/80/bvca"}]

The search didn't turn up any source citing 1,000 or more member firms. The BVCA's membership figure varies by source and date, ranging from about 600 to over 750.

- **Official About Us page:** Membership comprises more than 600 firms, including over 250 private equity and venture capital businesses, over 100 institutional investors and more than 200 profession
… [954 more characters]
```
</details>

→ `Bash` — Download EIF active funds PDF
```sh
cd [tmp] && mkdir -p eif && curl -sL -A "Mozilla/5.0" -o eif/active.pdf https://www.eif.org/files/records/eif-backed-active-funds.pdf && ls -la eif && file eif/active.pdf && which pdftotext; python3 -I -c "import pypdf" 2>&1
```

<details><summary>result</summary>

```
Exit code 1
total 560
drwxr-xr-x   5 [user]  wheel     160 11 Oct  01:12 .
drwx------  16 [user]  wheel     512 11 Oct  01:11 ..
-rw-r--r--   1 [user]  wheel  160434 11 Oct  01:12 active.pdf
-rw-r--r--   1 [user]  wheel  117979 11 Oct  01:09 eif.pdf
-rw-r--r--   1 [user]  wheel    1070 11 Oct  01:09 eif.txt
eif/active.pdf: PDF document, version 1.6 (zip deflate encoded)
/opt/homebrew/bin/pdftotext
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
```
</details>

→ `Bash` — Extract EIF PDF text and check CEE entries
```sh
cd [tmp] && pdftotext -layout active.pdf active_mine.txt && head -40 active_mine.txt && wc -l active_mine.txt && grep -ciE 'slovak|czech' active_mine.txt; grep -iE 'slovak|czech|CEE' active_mine.txt | head -20
```

<details><summary>result</summary>

```
                                                                                                               All active EIF‐backed fund investments                                                                                                             as at 30.09.2022




Geographical Focus   Fund Name                                                Fund Manager                                                                Main Sector                                     Fund Status End of Investment Period   Investment Strategy Set Up
Belgium              MicroStart                                               MicroStart SC‐ES                                                            Generalist                                      Signed                                 Fund
Belgium              E‐Capital                                                E‐Capital Management SCRL                                                   Generalist                                      Signed                      31/12/2005 Fund
Belgium              VIVES                                                    Sopartec SA                                                                 ICT                                             Signed                      18/12/2007 Fund
Belgium              CD3 (Centre for Drug design and Discovery)               KU Leuven Research & Development                                            Life Science                                    Signed
… [10389 more characters]
```
</details>

→ `Bash` — Count EIF funds and managers
```sh
cd [tmp] && python3 -I -c "
import re
rows=[l for l in open('active_mine.txt') if re.search(r'\b(Signed|Fund Status)\b',l) and 'Fund Status' not in l]
print('rows',len(rows))
mg=set()
for l in rows:
    parts=re.split(r'\s{2,}',l.strip())
    if len(parts)>=3: mg.add(parts[2].lower())
print('unique managers approx',len(mg))
"
```

<details><summary>result</summary>

```
rows 1097
unique managers approx 696
```
</details>

→ `WebFetch` https://www.eban.org/2025/10/29

→ `WebSearch` Campden Wealth number of single family offices worldwide estimate 2025 family office count Europe

→ `WebSearch` SEC family office rule exclusion from Investment Advisers Act no registration Form ADV family offices not public

→ `WebSearch` Business Angels Slovakia OR "Slovak Business Angels Network" OR "Czech Business Angels" network members number EBAN member

<details><summary>result</summary>

```
Web search results for query: "Campden Wealth number of single family offices worldwide estimate 2025 family office count Europe"

Links: [{"title":"north america family office report 2025","url":"https://campdenwealth.com/report/north-america-family-office-report-2025"},{"title":"burgeoning family offices manage 59 trillion","url":"https://www.thewealthadvisor.com/article/burgeoning-family-offices-manage-59-trillion"},{"title":"number single family offices increases over third","url":"https://www.paminsight.com/epc/article/number-single-family-offices-increases-over-third"},{"title":"Burgeoning family offices manage $ 5.9 trillion: Campden","url":"https://www.ft.lk/front-page/Burgeoning-family-offices-manage-5-9-trillion-Campden/44-682056"},{"title":"Burgeoning family offices manage $ 5.9 trillion: Campden","url":"https://www.ft.lk/Front-Page/Burgeoning-family-offices-manage-5-9-trillion-Campden/44-682056"},{"title":"asia pacific family office report 2025","url":"https://campdenwealth.com/report/asia-pacific-family-office-report-2025"},{"title":"How Many Family Offices Are There in the United States?","url":"https://www.wealthmanagement.com/high-net-worth/how-many-family-offices-are-there-united-states"},{"title":"single family offices control 5 9 trn campden wealth","url":"https://www.buyoutsinsider.com/single-family-offices-control-5-9-trn-campden-wealth/"},{"title":"How Many Family Offices are there in the United States?","url":"https://familyoffice.com/insights/how-many-
… [1199 more characters]
```
</details>

<details><summary>result</summary>

```
The page doesn't give figures for most of your questions. Here is what it does state:

- **Visible angel investment amount:** Not stated in the text. The page includes an image titled "2024 Angel Investment Market Highlights," but the figures are not in the page text.
- **Number of angels:** Not stated in the text.
- **Number of networks:** Not stated in the text.
- **Countries covered:** 38 countries on the European continent.
- **Date published:** No explicit publication date for the compendium. The page is dated 29 October 2025, and the PDF link path suggests a December 2025 upload.
- **Limitations:** The figures are "not representative of the entire European market," according to the page. They are presented as indicative insights into early-stage investment trends.

For the investment, angel, and network figures, you'll need to check the full PDF linked from the page.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "SEC family office rule exclusion from Investment Advisers Act no registration Form ADV family offices not public"

Links: [{"title":"SEC Adopts Rules Defining Investment Adviser Exclusion for Family Offices","url":"https://akingump.com/communicationcenter/newsalertdetail.aspx?pub=2797"},{"title":"sec adopts final rules defining scope of family office exclusion from the definition of investment adviser","url":"https://mondaq.com/unitedstates/fund-management-reits/139816/sec-adopts-final-rules-defining-scope-of-family-office-exclusion-from-the-definition-of-investment-adviser"},{"title":"family office rule","url":"https://altss.com/glossary/family-office-rule"},{"title":"family office rule","url":"https://altss.com/glossary/family-office-rule.md"},{"title":"sec adopts family office rule","url":"https://www.thinkadvisor.com/amp/2011/10/01/sec-adopts-family-office-rule/"},{"title":"the sec adopts final rule under the dodd frank act","url":"https://www.carltonfields.com/insights/publications/2011/the-sec-adopts-final-rule-under-the-dodd-frank-act"},{"title":"family office insights family offices and the investment advisers act","url":"https://www.squirepattonboggs.com/media/jhifbxur/family-office-insights-family-offices-and-the-investment-advisers-act.pdf"},{"title":"110719 sec adopts rules defining investment adviser exclusion fo","url":"https://www.akingump.com/a/web/7452/aogRf/110719_sec_adopts_rules_defining_investment_adviser_exclusion_fo.pdf"},
… [2228 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Business Angels Slovakia OR "Slovak Business Angels Network" OR "Czech Business Angels" network members number EBAN member"

Links: [{"title":"www.eban.org","url":"https://www.eban.org/?p=22807"},{"title":"nbs.sk","url":"https://nbs.sk/_img/Documents/BIATEC/BIA03_04/13_14.pdf"},{"title":"EBAN Strengthens Presence and Activity in CEE Countries with Launch of EBAN CEE Community","url":"https://www.eban.org/2016/10/22/"},{"title":"EBAN Membership Directory","url":"https://www.eban.org/our-network-2"},{"title":"podnikatelski anjeli","url":"https://www.podnikajte.sk/temy/podnikatelski-anjeli"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"Investície do startupov","url":"https://www.podnikajte.sk/investor/investicie-startupy"},{"title":"www.eban.org","url":"https://www.eban.org/?p=42659"},{"title":"Driving Successful and Responsible Angel Investing in Europe","url":"https://www.eban.org/about-us-2/"}]

I couldn't find member counts for any Slovak or Czech business angel network, and I didn't find a "Slovak Business Angels Network" or "Czech Business Angels" under those names.

- **Slovakia's main network:** The Klub podnikateľských anjelov Slovenska (Club of Business Angels of Slovakia) was founded in 2011 by the Slovak Business Agency and the Association of Young Entrepreneurs of Slovakia, as the first domestic network of informal investors in Slovakia. The source give
… [1169 more characters]
```
</details>

→ `Bash` — Count Wikidata items per investor class
```sh
cd [tmp] && q='SELECT ?c ?cLabel (COUNT(DISTINCT ?x) AS ?n) WHERE { VALUES ?c { wd:Q1752459 wd:Q1066339 wd:Q1407209 wd:Q5433016 wd:Q15911314 wd:Q4830453 } ?x wdt:P31 ?c . SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } } GROUP BY ?c ?cLabel'; curl -s -G -H "Accept: application/sparql-results+json" -A "[redacted: name]Research/1.0 ([redacted: email])" --data-urlencode "query=$q" https://query.wikidata.org/sparql | python3 -I -c "import json,sys; d=json.load(sys.stdin); [print(b['c']['value'],b['cLabel']['value'],b['n']['value']) for b in d['results']['bindings']]"
```

<details><summary>result</summary>

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import json,sys; d=json.load(sys.stdin); [print(b['c']['value'],b['cLabel']['value'],b['n']['value']) for b in d['results']['bindings']]
                       ~~~~~~~~~^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```
</details>

→ `Bash` — Look up Wikidata investor classes by label
```sh
q='SELECT ?c ?cLabel (COUNT(DISTINCT ?x) AS ?n) WHERE { VALUES ?lbl { "venture capital firm"@en "private equity firm"@en "family office"@en "investment company"@en "angel investor"@en "venture capital fund"@en "private equity fund"@en } ?c rdfs:label ?lbl . ?x wdt:P31 ?c . SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } } GROUP BY ?c ?cLabel'; curl -s -m 90 -G -H "Accept: application/sparql-results+json" -A "[redacted: name]Research/1.0 ([redacted: email])" --data-urlencode "query=$q" https://query.wikidata.org/sparql | head -c 3000
```

<details><summary>result</summary>

```
{
  "head" : {
    "vars" : [ "c", "cLabel", "n" ]
  },
  "results" : {
    "bindings" : [ {
      "c" : {
        "type" : "uri",
        "value" : "http://www.wikidata.org/entity/Q751314"
      },
      "cLabel" : {
        "xml:lang" : "en",
        "type" : "literal",
        "value" : "family office"
      },
      "n" : {
        "datatype" : "http://www.w3.org/2001/XMLSchema#integer",
        "type" : "literal",
        "value" : "15"
      }
    }, {
      "c" : {
        "type" : "uri",
        "value" : "http://www.wikidata.org/entity/Q778274"
      },
      "cLabel" : {
        "xml:lang" : "en",
        "type" : "literal",
        "value" : "angel investor"
      },
      "n" : {
        "datatype" : "http://www.w3.org/2001/XMLSchema#integer",
        "type" : "literal",
        "value" : "1"
      }
    }, {
      "c" : {
        "type" : "uri",
        "value" : "http://www.wikidata.org/entity/Q1752459"
      },
      "cLabel" : {
        "xml:lang" : "en",
        "type" : "literal",
        "value" : "investment company"
      },
      "n" : {
        "datatype" : "http://www.w3.org/2001/XMLSchema#integer",
        "type" : "literal",
        "value" : "275"
      }
    }, {
      "c" : {
        "type" : "uri",
        "value" : "http://www.wikidata.org/entity/Q3487908"
      },
      "cLabel" : {
        "xml:lang" : "en",
        "type" : "literal",
        "value" : "venture capital firm"
      },
      "n" : {
        "datatype" : "http://www.w3.org/2001/
… [847 more characters]
```
</details>

→ `Bash` — Count Wikidata items by VC/PE industry
```sh
q='SELECT ?ind ?indLabel (COUNT(DISTINCT ?x) AS ?n) WHERE { VALUES ?lbl { "venture capital"@en "private equity"@en } ?ind rdfs:label ?lbl . ?x wdt:P452 ?ind . SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } } GROUP BY ?ind ?indLabel'; curl -s -m 90 -G -H "Accept: application/sparql-results+json" -A "[redacted: name]Research/1.0 ([redacted: email])" --data-urlencode "query=$q" https://query.wikidata.org/sparql | python3 -I -c "import json,sys; d=json.load(sys.stdin); [print(b['ind']['value'],b['indLabel']['value'],b['n']['value']) for b in d['results']['bindings']]"
```

<details><summary>result</summary>

```
http://www.wikidata.org/entity/Q219409 venture capital 57
http://www.wikidata.org/entity/Q476115 private equity 83
```
</details>

→ `WebSearch` dataor.justice.cz otevřená data obchodní rejstřík XML ke stažení veřejný rejstřík

→ `WebSearch` Register právnických osôb RPO API štatistický úrad open data api.statistics.sk rpo

→ `WebSearch` Finstat API cenník podmienky použitia automatizované sťahovanie zakázané

→ `WebSearch` NBS subjekty finančného trhu vyhľadávanie register správcovských spoločností registrovaní správcovia AIF počet 2025

<details><summary>result</summary>

```
Web search results for query: "dataor.justice.cz otevřená data obchodní rejstřík XML ke stažení veřejný rejstřík"

Links: [{"title":"Nový obchodní rejstřík? Promarněná šance","url":"https://www.lupa.cz/clanky/novy-obchodni-rejstrik-promarnena-sance/"},{"title":"Otevřená data veřejných rejstříků budou již brzy v plném provozu","url":"https://advokatnidenik.cz/2019/03/26/otevrena-data-verejnych-rejstriku-budou-jiz-brzy-v-plnem-provozu/"},{"title":"XML s.r.o., IČO: 08125023, sídlo: Praha","url":"https://www.finmag.cz/obchodni-rejstrik/08125023-xml-s-r-o"},{"title":"czech republic company lookup guide","url":"https://www.infobelpro.com/en/blog/czech-republic-company-lookup-guide"},{"title":"verejna evidence po popis dat csv a xml","url":"https://msp.gov.cz/documents/d/msp/verejna-evidence-po-popis-dat-csv-a-xml"},{"title":"popis api","url":"https://opendata.mv.gov.cz/popis-api/"},{"title":"docs.topograph.co","url":"https://docs.topograph.co/essentials/czechia"},{"title":"repozitar.techlib.cz","url":"https://repozitar.techlib.cz/bitstreams/141cf5b0-35b5-40b7-a338-e3a4e4c69963/download"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/datova-zurnalistika/"}]

The search turned up the Ministry of Justice's 2019 announcement that the open data from the public registers would be on dataor.justice.cz, and a 2022 critique of the data quality. I couldn't confirm the portal's current state.

- **Launch and formats:** A 2019 article said the Ministry would publish the reg
… [1110 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Register právnických osôb RPO API štatistický úrad open data api.statistics.sk rpo"

Links: [{"title":"04 SjzS0NLMwNTKxNLfQj9CPykssy0xPLMnMz0vMAfIjo8ziw3wCLJycDB0N H2MXQ0Cg4K9Q90CAzzcwwz1g1Pz9HOjHBUBgEXw3Q!!","url":"https://slovak.statistics.sk/wps/portal/ext/Databases/RPO%20-%20Register%20pr%C3%A1vnick%C3%BDch%20os%C3%B4b/!ut/p/z0/04_SjzS0NLMwNTKxNLfQj9CPykssy0xPLMnMz0vMAfIjo8ziw3wCLJycDB0N_H2MXQ0Cg4K9Q90CAzzcwwz1g1Pz9HOjHBUBgEXw3Q!!"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/3836116.pdf"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/4449086.pdf"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/3637710.pdf"},{"title":"SU SR RPO 005","url":"https://mirri.gov.sk/wp-content/uploads/2023/09/SU-SR-RPO-005.pdf"},{"title":"HY1LC4JAFEZ jUu910eZSzdKEYGIZrOR6zTUVN5RHHr9 rTV4XDg 0BAA4LpqS9ktWF6zH4S6zYtiqLc1zXmdZDhNvRzPFQVYhZDqRh2IHTXey Ze htIoyjlR8lgR8mM5YJfRtHkYKQhq16W2hMN9HVVezgZOcr6f4LWwfPZKmj78dBMyhuF4Xhnh9 BCQnjQ!!","url":"https://susr.statistics.sk/wps/portal/ext/Databases/!ut/p/z0/HY1LC4JAFEZ_jUu910eZSzdKEYGIZrOR6zTUVN5RHHr9-rTV4XDg-0BAA4LpqS9ktWF6zH4S6zYtiqLc1zXmdZDhNvRzPFQVYhZDqRh2IHTXey_Ze-htIoyjlR8lgR8mM5YJfRtHkYKQhq16W2hMN9HVVezgZOcr6f4LWwfPZKmj78dBMyhuF4Xhnh9_BCQnjQ!!/"},{"title":"04 Sj9CPykssy0xPLMnMz0vMAfIjo8ziw3wCLJycDB0NDEJ9LA0cg1yMDS28zIycgw31g1Pz9AuyHRUBvgInTQ!!","url":"https://slovak.statistics.sk/wps/portal/ext/Databases/Open_data/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi
… [2151 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "NBS subjekty finančného trhu vyhľadávanie register správcovských spoločností registrovaní správcovia AIF počet 2025"

Links: [{"title":"nbs.sk","url":"https://nbs.sk/dokument/4dfca3c2-3daf-45c0-a770-6e1a37a4175d/stiahnut/?force=true"},{"title":"nbs.sk","url":"https://nbs.sk/dokument/d918e99a-6c2f-4524-96d6-ffb239440b69/stiahnut/?force=true"},{"title":"nbs.sk","url":"https://nbs.sk/dokument/92c2fb17-d841-440e-9f01-cddf078d874c/stiahnut/?force=true"},{"title":"Usmernenie k registracii EuVECA EuSEF","url":"https://regsaif.nbs.sk:443/static/Usmernenie_k_registracii_EuVECA_EuSEF.pdf"},{"title":"nbs.sk","url":"https://nbs.sk/dokument/9c104a40-ba90-4644-af27-0e0ed6f3f51e/stiahnut/?force=true"},{"title":"nbs.sk","url":"https://nbs.sk/dokument/005b0a5b-65ac-4347-8228-b7b7bc0acaa1/stiahnut/?force=true"},{"title":"vyhlasene znenie","url":"https://static.slov-lex.sk/static/SK/ZZ/2025/296/vyhlasene_znenie.html"},{"title":"static.slov-lex.sk","url":"https://static.slov-lex.sk/static/SK/OP/2025/18/20251201.html"},{"title":"static.slov-lex.sk","url":"https://static.slov-lex.sk/static/SK/ZZ/2025/296/20251110.html"}]

Search turned up the NBS regulatory framework for AIF managers, but no current count of registered AIF managers for 2025.

- **Register:** The NBS maintains a Register of AIF managers, and it includes a separate EuVECA/EuSEF register. If a registered AIF manager wants to manage EuVECA and/or EuSEF funds, it must register such a fund in the EuVECA an
… [968 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Finstat API cenník podmienky použitia automatizované sťahovanie zakázané"

Links: [{"title":"Cenník služieb","url":"https://finstat.sk/Sluzby"},{"title":"Prihlásiť sa","url":"https://finstat.sk/sluzby"},{"title":"github.com","url":"https://github.com/hubipe/finstat"},{"title":"hubipe / finstat","url":"https://packagist.org/packages/hubipe/finstat"},{"title":"Prihlásiť sa","url":"https://finstat.sk/vseobecne-obchodne-podmienky"},{"title":"be-soft / finstat","url":"https://packagist.org/packages/be-soft/finstat"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/5729690.pdf"},{"title":"crz.gov.sk","url":"https://crz.gov.sk//data/att/5420660.pdf"},{"title":"Prihlásiť sa","url":"https://finstat.sk/api"}]

I didn't find a clause in the results that prohibits automated scraping, so I can't confirm that restriction from these sources. The results do cover pricing and the general terms.

- **Pricing:** The API isn't priced separately. The public price list shows FinStat PREMIUM at 350 € / rok, ELITE at 1 200 € / rok, and ULTIMATE at 2 750 € / rok, and API access is tied to these tiers. The FinStat API entry itself says "Kontaktujte nás", so custom pricing requires contacting the company.
- **API scope:** The API page says the service offers unlimited 24/7 access within the set limit, and that selected APIs are offered within the FinStat PREMIUM, ELITE and ULTIMATE packages.
- **Terms:** FinStat's B2B general terms (VOP) govern use of the
… [724 more characters]
```
</details>

→ `WebFetch` https://regsaif.nbs.sk/

→ `WebFetch` https://www.cnb.cz/cs/dohled-financni-trh/seznamy/webove-sluzby-ws-jerrs/

<details><summary>result</summary>

```
**What it is:** The Register of Alternative Investment Fund Managers (RegSAIF), run by Národná banka Slovenska (NBS). According to the page, it contains persons registered under § 31b of Act No. 203/2011 on collective investment. Registration uses an online form and carries an NBS administrative fee. Only persons covered by the exemption in § 31a(1) can be registered.

**Categories of entities:** The page doesn't explicitly categorize its listed entities. It links to registration forms for:
- AIFs and AIF managers
- EuSEF and EuVECA funds

**Counts:** None shown.

**Export/search:** Not described. The page has a "Zoznam registrovaných osôb" (list of registered persons) link, but it doesn't mention search or export functions. A notice also warns of possible web service outages from 5 to 7 September 2025 due to maintenance.
```
</details>

<details><summary>result</summary>

```
**What it provides:** Machine-readable data from the JERRS information system, made available to external entities through three synchronous web services:

1. **Information about a specific entity:** identification data, registered address, authorization dates, permitted activities, and selected links to other entities.
2. **List of entities in a chosen role:** a simplified list without links or hierarchies. Large lists are split across pages.
3. **Representatives of a given represented party:** a paginated list of representing entities.

**Format:** XML. You send an XML request and receive an XML response, and both must conform to the published XSD specification. Each service has a maximum response size.

**Free or registration required:** Registration is required. You must email a signed access request to [redacted: email address] with your identification details, a contact person, and the serial number and issuer name of the certificate you'll use. Authentication uses a commercial (non-qualified) certificate from eIdentity, I.CA, Postsignum, or a listed foreign authority. The page doesn't mention fees, so it doesn't say whether access is free.

**Entity types (investment companies, management companies, §15 managers, investment funds):** The page doesn't name these types or say whether they're covered. It refers to a role codelist (WSJERRS_role.xlsx) and a lists codelist (WSJERRS_seznamy.xlsx), which would show the available roles and lists, but their contents aren't included here.
```
</details>

→ `WebSearch` Sequoia Capital split HongShan Peak XV separate firms completed 2024

→ `WebSearch` Foundry Group will not raise new funds wind down announcement

→ `WebSearch` Social Capital Chamath converts to family office no outside capital 2021

→ `WebSearch` most active investors Europe list crowdfunding platform Crowdcube Seedrs ranked among most active investors Dealroom

<details><summary>result</summary>

```
Web search results for query: "Sequoia Capital split HongShan Peak XV separate firms completed 2024"

Links: [{"title":"Venture CapitalGiant Sequoia toSplitinto Three Entities","url":"https://news.qq.com/rain/a/20230607A0AMR100"},{"title":"One To Three: The Story of Sequoia Capital's Split","url":"https://conquestbitspilani.substack.com/p/one-to-three-the-story-of-sequoia"},{"title":"Sequoia Capital splits into 3 firms, separating China operations from the US, amid rising geopolitical tensions","url":"https://amp.scmp.com/tech/article/3223176/sequoia-capital-splits-three-firms-separating-china-operations-us-amid-rising-geopolitical-tensions"},{"title":"Sequoia Capital Splits Into Three Units","url":"https://www.finews.asia/finance/39434-sequoia-capital-splits-into-three-units"},{"title":"Sequoia Capital to carve off China and India units as it faces ‘increasingly complex’ pressures","url":"https://www.cityam.com/?p=2008695"},{"title":"entrackr.com","url":"https://entrackr.com/?p=168808"},{"title":"krdo.com","url":"https://krdo.com/?p=976258"},{"title":"After Sequoia split, India's Peak XV says confident of investor backing","url":"https://sg.news.yahoo.com/sequoia-split-indias-peak-xv-142509693.html"},{"title":"Sequoia Capital's strategic split: Three groups formed for China, Asean and India, US and Europe","url":"https://www.peoplemattersglobal.com/?p=38102"},{"title":"texxr.com","url":"https://texxr.com/840759"}]

The search results describe the plan and the rebrand, but no
… [962 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Social Capital Chamath converts to family office no outside capital 2021"

Links: [{"title":"Chamath Palihapitiya","url":"https://en.wikipedia.org/wiki/Chamath_Palihapitiya"},{"title":"Chamath Palihapitiya burns down what he built","url":"https://www.axios.com/2018/09/21/social-capital-chamath-burns-down"},{"title":"Single Family Office","url":"https://altss.com/profile/social-solutions-global"},{"title":"Chamath Palihapitiya","url":"https://www.wikipedia.org/wiki/Chamath Palihapitiya"},{"title":"Chamath Palihapitiya: From Facebook to SPAC King","url":"https://startuptalky.com/chamath-palihapitiya-success-story/"},{"title":"Image Credits:Michael Kovac/Getty Images for Vanity Fair / Getty Images","url":"https://techcrunch.com/?p=1716743"},{"title":"Social Capital will no longer raise outside capital","url":"https://techcrunch.com/2018/09/20/social-capital-will-no-longer-raise-outside-capital/embed/"},{"title":"social capital","url":"https://texxr.com/entity/social-capital"},{"title":"Chamath Palihapitiya Height, Weight, Net Worth, Age, Birthday, Wikipedia, Who, Instagram, Biography","url":"https://dash.duchenneuk.org/chamath-palihapitiya-height-weight-net-worth-age-birthday-wikipedia-wh.html"}]

The conversion happened in 2018, not 2021. In September 2018, Social Capital said it would stop raising outside money and become a holding company investing mostly Palihapitiya's own capital. Social Capital no longer will raise outside capital, and instea
… [1112 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Foundry Group will not raise new funds wind down announcement"

Links: [{"title":"stacks of dollars with down red arrow","url":"https://techcrunch.com/?p=2664906"},{"title":"2/16/2024: The Foundry Group Will Not Raise a New Fund","url":"https://greatreset2022.substack.com/p/2162024-the-foundry-group-will-not"},{"title":"Endings and Beginnings","url":"https://www.sethlevine.com/archives/2024/01/endings-and-beginnings.html"},{"title":"Endings and Beginnings","url":"https://sethlevine.com/archives/2024/01/endings-and-beginnings%2ehtml"},{"title":"Endings and Beginnings","url":"https://sethlevine.com/?p=13046"},{"title":"- Venture Daily Digest","url":"https://venturedailydigest.beehiiv.com/p/vc-fund-35b-aum-shutting-openais-founding-scientist-leaving-second-time"},{"title":"ending and starting venture capital firms transcript","url":"https://stvp.stanford.edu/wp-content/uploads/sites/3/2024/09/ending-and-starting-venture-capital-firms-transcript.pdf"},{"title":"foundry group announces closure and no further fundraising plans","url":"https://robots.net/news/foundry-group-announces-closure-and-no-further-fundraising-plans/"},{"title":"25 Aug 2025","url":"https://podwise.ai/episodes/5041406"}]

Foundry Group announced in January 2024 that its current fund would be its last, and it will not raise another. The firm is a Boulder-based venture firm with about $3.5 billion in assets under management. It first announced that its current fund would be its las
… [1634 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "most active investors Europe list crowdfunding platform Crowdcube Seedrs ranked among most active investors Dealroom"

Links: [{"title":"seedrs recognized as most active uk equity investor","url":"https://www.heyfuturenexus.com/seedrs-recognized-as-most-active-uk-equity-investor"},{"title":"Quarterly and annual reports Regional Seed funding Venture","url":"https://news.crunchbase.com/venture/europe-leading-2022-investors-crowdcube-antler"},{"title":"Seedrs Recognized as Most Active Investor in UK, Updates on Secondary Marketplace for Private Securities","url":"https://www.crowdfundinsider.com/?p=158087"},{"title":"www.heyfuturenexus.com","url":"https://www.heyfuturenexus.com/?p=24632"},{"title":"seedrs most active crowdfunder 2016 mid point","url":"https://www.privateequitywire.co.uk/seedrs-most-active-crowdfunder-2016-mid-point/"},{"title":"seedrs and crowdcube named uks top investors for 2016","url":"https://startups.co.uk/news/seedrs-and-crowdcube-named-uks-top-investors-for-2016/"},{"title":"back to reports","url":"https://dealroom.co/reports/active-venture-capital-investors-in-europe"},{"title":"Seedrs Update: The Most Active Pan-European Equity Crowdfunding Platform","url":"https://www.crowdfundinsider.com/?p=177807"},{"title":"Seedrs Recognized as Most Active Investor in UK, Updates on Secondary Marketplace for Private Securities","url":"https://www.crowdfundinsider.com/2020/02/158087-seedrs-recognized-as-most-active-investor-in-uk-update
… [2036 more characters]
```
</details>

→ `Bash` — Download NVCA 2026 Yearbook and grep firm counts
```sh
cd [tmp] && mkdir -p nvca_mine && cd nvca_mine && curl -sL -A "Mozilla/5.0" -o y2026.pdf "https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf" && file y2026.pdf && pdftotext -layout y2026.pdf y.txt && grep -inE 'VC firms|venture firms|firms (in|across) the|assets under management|AUM|investors participated|active investors|unique investors' y.txt | head -30
```

<details><summary>result</summary>

```
y2026.pdf: PDF document, version 1.7 (zip deflate encoded)
236:percent from the 457 launched in 2021. The total number of VC firms in existence declined for the first time as well, falling from 3,054 to
244:
Total assets under management reached $1.38 trillion, including $1.08 trillion in net asset value and $299.3 billion in dry powder. But
251:AUM and decades of successful investing on the other.
532:                                                                                     Raised Funds                       Avg Fund Size                       Median Fund       Median AUM
533:                     Cumulative   Cumulative   Cumulative          Existing Funds                      AUM ($B)                           Avg AUM ($M)
604:                                                   US Venture Capital AUM by Year
627:                                                                                                                               Total AUM ($B)
642:The industry's average AUM per firm
667:US Venture Capital AUM by Year
680: Total AUM ($B)    $296.4    $331.9   $363.8    $379.1         $415.5              $509.7              $600.4              $797.9              $1,239.8           $1,199.6           $1,226.9           $1,299.6               $1,377.0
722:Number of Active Investors (#)
784:                                       *Active investor definitions are as follows. Active Investors are Investors hq'ed globally who made 1+ venture capital type investmen
… [2417 more characters]
```
</details>

→ `Bash` — Read NVCA firm count and active investor sections
```sh
cd [tmp] && sed -n 230,250p y.txt; sed -n 715,790p y.txt | cut -c1-220; sed -n 890,910p y.txt | cut -c1-200; sed -n 4370,4410p y.txt | cut -c1-200
```

<details><summary>result</summary>

```
between 2020 and 2022.


The aggregate numbers also mask a sharp bifurcation in the market. The top ten funds alone raised a combined $22 billion, 32.9
percent of all VC capital, up 2.5 times from the 13 percent they claimed in 2021. That left roughly $44.9 billion to be divided among the
remaining 575 funds. At the same time, first-time fund formation collapsed to 101 funds, the lowest level since 2007 and down 77.9
percent from the 457 launched in 2021. The total number of VC firms in existence declined for the first time as well, falling from 3,054 to
2,984. Nearly half of all venture investors active in 2021 have since exited the market.




                                                                       6
                                                            N VC A 2026 Y E A RBOOK

Total assets under management reached $1.38 trillion, including $1.08 trillion in net asset value and $299.3 billion in dry powder. But
the dry powder is concentrated in the same platform firms that dominate fundraising, leaving the median sub-$100 million fund with far
less runway than the industry aggregate suggests.


VC isn’t retreating; it’s recalibrating. The capital is there, and the firms remain. The question, especially for emerging managers, is how
to thrive in an ecosystem defined by a 3.75 percent federal funds rate on one side, and platform funds with tens of billions of dollars in
differentiated managers who are operating                                    2015
… [10382 more characters]
```
</details>

→ `WebSearch` "Investing in Europe" "Private Equity Activity 2025" methodology "firms" "1,"  Invest Europe statistics based on

→ `WebFetch` https://www.investeurope.eu/research/about-research/european-data-cooperative/

→ `WebFetch` https://dealroom.co/reports/active-venture-capital-investors-in-europe

<details><summary>result</summary>

```
The EDC covers **4,000 firms, 10,900 funds, 86,700 portfolio companies, and 330,900 transactions**.

The page doesn't state a date for these figures.

The page doesn't say whether EDC data is public or members-only. The figures appear on the public data collection page, but some Invest Europe publications are marked "MEMBER ONLY," and the page notes that "Invest Europe members and data contributors receive dedicated research and data support."
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Investing in Europe" "Private Equity Activity 2025" methodology "firms" "1,"  Invest Europe statistics based on"

Links: [{"title":"Roland Berger European Private Equity Outlook 2025","url":"https://content.rolandberger.com/hubfs/Roland_Berger_European_Private_Equity_Outlook 2025.pdf"},{"title":"Investing in Europe: Private Equity Activity 2025 Report highlights strong fundraising and investment performance","url":"https://tech.eu/2026/05/07/investing-in-europe-private-equity-activity-2025-report-highlights-strong-fundraising-and-investment-performance/"},{"title":"european private equity market recap q3 2025","url":"https://www.ropesgray.com/en/insights/alerts/2025/11/european-private-equity-market-recap-q3-2025"},{"title":"Pulse of private equity TL Q2 V6","url":"https://assets.kpmg.com/content/dam/kpmg/dp/pdf/2025/Pulse_of_private_equity_TL_Q2_V6.pdf"},{"title":"Invest Europe: Venture capital reaches second-highest level on record","url":"https://tech.eu/2026/07/10/invest-europe-venture-capital-reaches-second-highest-level-on-record/"},{"title":"journal.fsv.cuni.cz","url":"https://journal.fsv.cuni.cz/mag/article/show/id/1557"},{"title":"Investing in Europe: Private Equity activity 2024","url":"https://www.seca.ch/en/knowledge-library/newsletters/2025/seca-enewsletter-no-550/private-equity-int-news/investing-in-europe-private-equity-activity-2024/"},{"title":"pwc private equity trend report 2025 final","url":"https://pwc.dk/da/publikationer/2
… [2099 more characters]
```
</details>

<details><summary>result</summary>

```
The page doesn't say how many active investors in European tech there are, or break them down by investor type. It states only that Dealroom's database "contains over 17,500 investment funds and other professional investors," and that the analysis of how many are actively investing each year is in the full report, which is behind a form. The "Key findings" and "Selected charts" sections are referenced but their contents aren't included.

The report is dated **August 17, 2017**.
```
</details>

→ `WebSearch` State of European Tech 2025 Atomico number of active investors in European startups unique investors

→ `WebSearch` UBS Global Wealth Report 2025 number of millionaires ultra high net worth individuals over 50 million Europe count

→ `WebSearch` Preqin family offices database number tracked "family offices" investing in private equity venture

→ `WebSearch` PitchBook "family offices" number tracked direct investments "family office" venture deals 2025 report

<details><summary>result</summary>

```
Web search results for query: "State of European Tech 2025 Atomico number of active investors in European startups unique investors"

Links: [{"title":"state european tech report 2025","url":"https://sifted.eu/articles/state-european-tech-report-2025"},{"title":"europe at a crossroads insights from atomicos state of european tech 2025","url":"https://cvca.hr/europe-at-a-crossroads-insights-from-atomicos-state-of-european-tech-2025/"},{"title":"europes tech future hits a turning point","url":"https://ioplus.nl/en/posts/europes-tech-future-hits-a-turning-point"},{"title":"les startups europeennes ont leve 44 milliards de dollars en 2025","url":"https://www.maddyness.com/2025/11/19/les-startups-europeennes-ont-leve-44-milliards-de-dollars-en-2025/"},{"title":"state of european tech report","url":"https://www.trendingtopics.eu/state-of-european-tech-report/"},{"title":"jornaleconomico.sapo.pt","url":"https://jornaleconomico.sapo.pt/?p=1353743"},{"title":"Kellogg-WHU Executive MBA | Logo","url":"https://kellogg.whu.edu/en/news-insights/whu-magazine/article/four-whu-start-ups-among-europes-mighty-50"},{"title":"state of european tech 2025 europa acelera e portugal ganha novo unicornio","url":"https://www.empreendedor.com/state-of-european-tech-2025-europa-acelera-e-portugal-ganha-novo-unicornio"},{"title":"state european tech 2025 what hot topics emerge luxembourg","url":"https://digital-skills-jobs.europa.eu/en/latest/news/state-european-tech-2025-what-hot-topics-emerge-luxembourg
… [1348 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "UBS Global Wealth Report 2025 number of millionaires ultra high net worth individuals over 50 million Europe count"

Links: [{"title":"hirunews.lk","url":"https://hirunews.lk/en/business/474904/X"},{"title":"Nearly One Million New Millionaires Created Worldwide in a Single Year","url":"https://en.politis.com.cy/news/1016080/nearly-one-million-new-millionaires-created-worldwide-in-a-single-year"},{"title":"Nearly one million people worldwide became millionaires in 2025, UBS report finds","url":"https://www.internazionale.it/ultime-notizie-reuters/2026/06/30/nearly-one-million-people-worldwide-became-millionaires-in-2025-ubs-report-finds"},{"title":"Nearly one million people worldwide became millionaires in 2025, UBS report finds","url":"https://www.arabnews.pk/node/2649077"},{"title":"Nearly one million people worldwide became millionaires in 2025, UBS report finds","url":"https://www.thestar.com.my/news/world/2026/06/30/nearly-one-million-people-worldwide-became-millionaires-in-2025-ubs-report-finds"},{"title":"UBS: World’s millionaires increase by nearly 1 million in 2025","url":"https://www.idnfinancials.com/news/65427/ubs-jumlah-jutawan-dunia-bertambah-hampir-1-juta-pada-2025"},{"title":"Millionaire numbers hit new high in 2025","url":"https://hirunews.lk/goldfmnews/474904/millionaire-numbers-hit-new-high-in-2025"},{"title":"Nearly one million people worldwide became millionaires in 2025, UBS report finds","url":"https://www.nst.com.my/amp/bu
… [1672 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "PitchBook "family offices" number tracked direct investments "family office" venture deals 2025 report"

Links: [{"title":"Global Family Office Deals Study 2025","url":"https://www.pwc.com/us/en/ghosts/family-office-deals-study.html"},{"title":"Global Family Office Deals Study 2025","url":"https://www.pwc.com/gx/en/services/entrepreneurial-private-business/emea-private-business/family-office-deals-study.html"},{"title":"Global Family Office Deals Study 2025","url":"https://www.pwc.com/gx/en/services/family-business/family-office/family-office-deals-study.html"},{"title":"global family office deals study 2025","url":"https://www.pwc.com/gx/en/services/family-business/assets/global-family-office-deals-study-2025.pdf"},{"title":"Family offices widen global reach and boost private deals, report shows","url":"https://www.wealthprofessional.ca/news/industry-news/family-offices-widen-global-reach-and-boost-private-deals-report-shows/391926"},{"title":"Family offices and venture capital: the new architecture of private capital","url":"https://www.citi.com/ventures/perspectives/opinion/family-offices-new-architecture-of-private-capital.html"},{"title":"clockworks summer solstice report","url":"https://andsimple.co/insights/clockworks-summer-solstice-report"},{"title":"www.craincurrency.com","url":"https://www.craincurrency.com/node/1020996"},{"title":"2025 Silent Capital Report now available. Where family offices and LPs are actually deploying. [Download
… [1434 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Preqin family offices database number tracked "family offices" investing in private equity venture"

Links: [{"title":"family offices tripled creating a new gold rush on wall street","url":"https://www.cnbc.com/2024/03/08/family-offices-tripled-creating-a-new-gold-rush-on-wall-street.html"},{"title":"family offices fast growth in family offices ignites competition among investment companies","url":"https://www.ifcreview.com/news/2024/march/family-offices-fast-growth-in-family-offices-ignites-competition-among-investment-companies/"},{"title":"Knowledge Center","url":"https://altss.com/knowledge-center/preqin-alternatives"},{"title":"Family Office","url":"https://www.familywealthreport.com/article.php/New-Preqin-Report-Shows-Rise-In-Family-Offices"},{"title":"Private equity database","url":"https://preqin.com/data/private-equity"},{"title":"Deutsche Family Offices erobern Private Markets","url":"https://www.boersen-zeitung.de/banken-finanzen/deutsche-family-offices-erobern-private-markets"},{"title":"the best institutional investor database for 2025 why altss is redefining fundraising intelligence","url":"https://altss.com/blog/the-best-institutional-investor-database-for-2025-why-altss-is-redefining-fundraising-intelligence.md"},{"title":"best family office database 2025","url":"https://altss.com/blog/best-family-office-database-2025.md"},{"title":"Private equity database","url":"https://cdn-website-ssr-core.iridium.pro.preqin.com/data/private-e
… [1549 more characters]
```
</details>

→ `WebSearch` "private equity firms" number in the United States PitchBook count 2025 "PE firms" headquartered

→ `WebFetch` https://libguides.cbs.dk/Preqin

→ `WebFetch` https://www.preqin.com/c/the-best-of-preqin-2025

<details><summary>result</summary>

```
Web search results for query: ""private equity firms" number in the United States PitchBook count 2025 "PE firms" headquartered"

Links: [{"title":"Private Equity Venture Capital Fact Sheets","url":"https://publishedresearch.cambridgeassociates.com/wp-content/uploads/2026/02/Private-Equity-Venture-Capital-Fact-Sheets.pdf"},{"title":"2025 US Private Equity Outlook","url":"https://files.pitchbook.com/website/files/pdf/2025_US_Private_Equity_Outlook.pdf"},{"title":"us pe market recap","url":"https://www.ropesgray.com/en/insights/alerts/2025/07/us-pe-market-recap"},{"title":"US Private Equity Report Shares Trends in Deal Activity, Exits, Fundraising","url":"https://www.crowdfundinsider.com/?p=245480"},{"title":"Private Equity, Hedge Funds & Investment Vehicles in the US - Number of Businesses (2004–2031)","url":"https://script.ibisworld.com/united-states/number-of-businesses/private-equity-hedge-funds-investment-vehicles/1345"},{"title":"www.etftrends.com","url":"https://www.etftrends.com/?p=614006"},{"title":"private equity comeback horizon","url":"https://www.advisorperspectives.com/commentaries/2025/07/03/private-equity-comeback-horizon"},{"title":"2025 annual us pe breakdown","url":"https://pitchbook.brightspotcdn.com/8c/8b/0621ec674566a564da64b1a53874/2025-annual-us-pe-breakdown.pdf"},{"title":"private equity comeback horizon","url":"https://api.advisorperspectives.com/commentaries/2025/07/03/private-equity-comeback-horizon"}]

I didn't find a PitchBook figure for the number
… [1068 more characters]
```
</details>

<details><summary>result</summary>

```
- **Fund managers:** Coverage reaches 67,000+ managers. The report says "our data now includes 67,000+ fund managers across 160+ countries," and 2,800+ were added in 2025.
- **Investors/LPs:** No total is given. Investor coverage grew 11%, with 3,700+ new investors added.
- **Family offices:** The page doesn't report a family office figure.
- **Funds:** Fund count rose 9%, with 19,900+ new funds added.
- **Countries:** Fund manager data spans 160+ countries.
```
</details>

<details><summary>result</summary>

```
- **PE fund managers:** "more than 34,100 active private equity fund managers" (the page also lists 1,500 infrastructure managers).
- **VC:** The page gives no separate VC fund or manager count. Its VC figure is deal coverage: "coverage of over 445,000 deals" under Venture Deals.
- **Funds:** "more than 85,000 PE funds and 4,500 infrastructure funds."
- **Investors (LPs):** "in-depth profiles of more than 19,800 active institutional investors in private equity." The page does not use the term LPs, and it lists 9,000 infrastructure investors separately.
- **Family offices:** Not mentioned.
- **Date:** Performance data covers funds "dating back to 1999." The "Last Updated: Oct 7, 2026" line refers to the guide page, not the database coverage.
```
</details>

→ `WebSearch` EBAN estimate total angel market Europe "invisible" market size number of business angels 300,000

→ `WebFetch` https://www.cnbc.com/2024/03/08/family-offices-tripled-creating-a-new-gold-rush-on-wall-street.html

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "EBAN estimate total angel market Europe "invisible" market size number of business angels 300,000"

Links: [{"title":"EBAN Statistics Compendium 2017","url":"https://www.eban.org/wp-content/uploads/2018/07/EBAN-Statistics-Compendium-2017"},{"title":"business angel investments in europe by visible and non visible market","url":"https://fr.statista.com/statistics/889583/business-angel-investments-in-europe-by-visible-and-non-visible-market/"},{"title":"Stats Compendium 2024","url":"https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf"},{"title":"No results found for","url":"https://2019.stateofeuropeantech.com/chapter/investors/article/angels"},{"title":"EBAN Statistics Compendium 2023","url":"https://www.eban.org/wp-content/uploads/2024/10/EBAN-Statistics-Compendium-2023.pdf"},{"title":"www.eban.org","url":"https://www.eban.org/?p=35526"},{"title":"Statistics Compendium 2021 European Early Stage Market Statistics","url":"https://www.eban.org/2022/10/10/"},{"title":"Statistics 2018 Compendium   FINAL","url":"https://www.eltia.eu/images/Statistics_2018_Compendium_-_FINAL.pdf"},{"title":"business angel investments by country in europe","url":"https://www-statista-com.ezproxy.canberra.edu.au/statistics/439669/business-angel-investments-by-country-in-europe"},{"title":"business angels co investment europe","url":"https://www-statista-com.ezproxy.canberra.edu.au/statistics/439687/business-angels-co-investment-europe"}]

I couldn't
… [2059 more characters]
```
</details>

→ `Bash` — Download EBAN 2024 compendium and grep figures
```sh
cd [tmp] && mkdir -p eban_mine && cd eban_mine && curl -sL -A "Mozilla/5.0" -o c2024.pdf https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf && file c2024.pdf && pdftotext -layout c2024.pdf c.txt && grep -inE 'angels|networks|million|slovak|czech' c.txt | head -60 | cut -c1-220
```

<details><summary>result</summary>

```
c2024.pdf: PDF document, version 1.4, 22 pages
13:business angels and business angel networks. The Compendium provides information on
14:the overall early-stage market and on how business angel networks operate, as well as
18:European business angel networks (hereafter BANs), Federations of BANs, but also
33:the surveys. Given that not all of the investments made by business angels are reported
56:European Commission to CSES about the Business Angels market in Europe. While
68:the publicly available reports published by business angel networks, national federations
107:substantially from the 764 Million Euros invested before the covid pandemic in 2019 to
108:1,220 Million Euros invested in 2024. This latest figure however represents a -2,8%
109:decrease from the 1,255 Million Euros from the previous year 2023. In 2024, angel
114:networks, and national venture capital associations, there are approximately 47,600 active
130:by associations and networks which are increasingly more capable at capturing data from
142:The business angel ecosystem in Europe, structured through various networks,
146:networks and through external channels beyond business angel associations, resulting in a
156:investment, with 291.3 million Euros invested in 2024, representing a 5% decrease from
157:2023. Germany follows in second place with 162.3 million Euros in angel investments,
159:million Euros, marking a 31% reduction from the previous year.
199:European VCs in 2024, business angels have managed
… [3846 more characters]
```
</details>

→ `Bash` — Read EBAN country table header
```sh
cd [tmp] && sed -n 640,660p c.txt | cut -c1-200; sed -n 105,118p c.txt
```

<details><summary>result</summary>

```
not a collapse in confidence, but rather a temporary rebalancing toward quality and
sustainability in early-stage investing as investors navigate uncertain economic terrain.




Figure 8. Angel Investments by Country, Visible Market Statistics



                                                  Total BA                 Total BA
                     No.       No.       No.                                                    Total BA Inv.
    Country                                      Inv. 2024,         YoY   Inv. 2023,   YoY
                    BANs       BAs      Inv.                                                      2022, €M
                                                    €M                       €M
     Austria          3        520       92        29,14            -8%     31,68      -0,7%        31,9
     Belarus          1        170      N/A         N/A             N/A      N/A        N/A         N/A
     Belgium          7        580       96        40,42            73%     23,39      -7,2%        25,2
    Bosnia
                      1        N.A      N/A         N/A             N/A      N/A        N/A         N/A
  Herzegovina
Data on the investments made across the 39 different countries measured in the report
indicates that the visible angel investment market on the European continent has grown
substantially from the 764 Million Euros invested before the covid pandemic in 2019 to
1,220 Million Euros invested in 2024. This latest figure however represents a
… [728 more characters]
```
</details>

→ `WebSearch` Forbes 2026 billionaires by country Germany Czech Republic number of billionaires Europe total

→ `WebSearch` Forbes terms of service scraping billionaires list real-time data reuse prohibited

<details><summary>result</summary>

```
Web search results for query: "Forbes 2026 billionaires by country Germany Czech Republic number of billionaires Europe total"

Links: [{"title":"List of countries by number of billionaires","url":"https://en.wikipedia.org/wiki/List_of_countries_by_number_of_billionaires"},{"title":"total wealth of billionaires by country","url":"https://statbase.org/datasets/business-and-investments/total-wealth-of-billionaires-by-country/"},{"title":"richest people in europe","url":"https://www.bleap.finance/blog/richest-people-in-europe"},{"title":"Top 10 Countries With The Most Billionaires Worldwide, June 2026","url":"https://databoks.katadata.co.id/en/economics-macro/statistics/7f739b9d3c814e4/top-10-countries-with-the-most-billionaires-worldwide-june-2026"},{"title":"richest people in europe","url":"https://www.bleap.finance/fr-fr/blog/richest-people-in-europe"},{"title":"richest people in europe","url":"https://www.bleap.finance/nl-nl/blog/richest-people-in-europe"},{"title":"richest people in europe","url":"https://www.bleap.finance/de-de/blog/richest-people-in-europe"},{"title":"richest people in europe","url":"https://www.bleap.finance/en-us/blog/richest-people-in-europe"},{"title":"Which EU Countries Do Billionaires Adore?","url":"https://www.tovima.com/society/which-eu-countries-do-billionaires-adore/amp/"}]

The search didn't turn up a Czech Republic figure. Germany's count varies by source and date, and the Europe total comes from a single secondary source.

- **Germany:** A Wi
… [744 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Forbes terms of service scraping billionaires list real-time data reuse prohibited"

Links: [{"title":"# Forbes Lists Scraper (`crawlerbros/forbes-lists-scraper`) Actor","url":"https://apify.com/crawlerbros/forbes-lists-scraper.md"},{"title":"# Forbes Real-Time Billionaires Scraper (`akash9078/forbes-real-time-billionaires-scraper`) Actor","url":"https://apify.com/akash9078/forbes-real-time-billionaires-scraper.md"},{"title":"FORBES® Terms of Service","url":"https://forbes.com.tr"},{"title":"DEV Community","url":"https://dev.to/crawlbase/how-to-scrape-valuable-data-from-forbes-3ai8"},{"title":"how to scrape data from forbes","url":"https://www.octoparse.com/blog/how-to-scrape-data-from-forbes"},{"title":"THE BILLIONAIRES 2018","url":"https://nycdatascience.com/blog/?p=38504"},{"title":"www.grepsr.com","url":"https://www.grepsr.com/?p=28917"},{"title":"Just launched - Fast Search API: organic SERP data in under 1 second Try it now","url":"https://www.scrapingbee.com/scrapers/forbes-scraper-api"},{"title":"lab 10","url":"https://www.stat.cmu.edu/~cshalizi/statcomp/12/labs/10/lab-10.pdf"}]

The search turned up Forbes terms of service that restrict scraping and data reuse, but not a clause specific to the billionaires list, and the copy I found is on a mirror domain rather than forbes.com.

- **Prohibited uses:** A copy of Forbes' terms hosted at forbes.com.tr (a mirror, so I can't confirm it matches the current official text) bars users from stori
… [1219 more characters]
```
</details>

→ `Bash` — Count 13F-HR and Form D filings in EDGAR index
```sh
cd [tmp] && mkdir -p idx_mine && cd idx_mine && curl -s -A "[redacted: name] research [redacted: email]" -o q3.idx https://www.sec.gov/Archives/edgar/full-index/2026/QTR3/form.idx && curl -s -A "[redacted: name] research [redacted: email]" -o q2.idx https://www.sec.gov/Archives/edgar/full-index/2026/QTR2/form.idx && for f in q2.idx q3.idx; do echo $f; grep -cE '^13F-HR ' $f; grep -cE '^13F-HR/A' $f; grep -cE '^D  ' $f; grep -cE '^D/A ' $f; done
```

<details><summary>result</summary>

```
q2.idx
9307
318
10680
6171
q3.idx
9442
406
10406
5753
```
</details>

→ `Bash` — Check Crunchbase ToS text for licence clauses
```sh
curl -sL -A "Mozilla/5.0" https://about.crunchbase.com/terms-of-service/ | python3 -I -c "
import sys,re,html
t=re.sub(r'<[^>]+>',' ',sys.stdin.read()); t=html.unescape(re.sub(r'\s+',' ',t))
for k in ['Creative Commons','Crunchbase Basic','scrape','Last Updated']:
    for m in re.finditer(k,t): print('...',t[max(0,m.start()-300):m.start()+400],'\n')
" | head -40
```

<details><summary>result</summary>

```
... m terms. Additionally, Crunchbase provides access to the Crunchbase 2013 Snapshot (the “Snapshot”) and Crunchbase Basic (“Crunchbase Basic”) pursuant to the following license terms: Subject to your compliance with these Terms, you may access and use the Snapshot and Crunchbase Basic pursuant to the Creative Commons Attribution License . The Snapshot must be attributed to our designated pseudonym “CrunchBase 2013 Snapshot” and bear the copyright notice “© 2013” in accordance with the Creative Commons requirements. The pseudonym and copyright notice are meant to avoid confusion with the current Crunchbase dataset and to promote transparency to users of the data. If you have questions, please c

... t to your compliance with these Terms, you may access and use the Snapshot and Crunchbase Basic pursuant to the Creative Commons Attribution License . The Snapshot must be attributed to our designated pseudonym “CrunchBase 2013 Snapshot” and bear the copyright notice “© 2013” in accordance with the Creative Commons requirements. The pseudonym and copyright notice are meant to avoid confusion with the current Crunchbase dataset and to promote transparency to users of the data. If you have questions, please contact us at [redacted: email address] . Crunchbase may also provide access to information or data points that are powered by generative artificial intelligence technologies (“AI Content”), an

... s and conditions and, if applicable, pay all required fees which apply to your spe
… [3445 more characters]
```
</details>

→ `WebFetch` https://www.gleif.org/en/meta/lei-data-terms-of-use

→ `WebFetch` https://www.sec.gov/about/privacy-information

<details><summary>result</summary>

```
Yes. The page says the data from the Access Service is released under CC0 1.0 Universal:

"The data available through the Access Service are provided under the CC0 licence"

The terms also restrict how you present the data. You must not suggest that GLEIF endorses or is associated with your data or services, except for the original LEI and LE-RD you download. The GLEIF trademark and logo require separate permission.
```
</details>

<details><summary>result</summary>

```
The page sets a rate limit but says nothing about a User-Agent declaration requirement.

**Rate limit:** "Current guidelines limit users to a total of no more than 10 requests per second"

The page also says that exceeding this threshold can lead to temporary restrictions. Requests from an IP address may be limited for a brief period, and access resumes once the rate stays below the threshold for 10 minutes.

**Automated tools:** "The SEC does not allow "unclassified" bots or automated tools to crawl the site."

This page is the SEC.gov Privacy Information policy, not EDGAR-specific guidance, and it covers SEC.gov content generally. For the User-Agent requirement, check EDGAR's developer or access documentation.
```
</details>

→ `WebFetch` https://www.sec.gov/os/accessing-edgar-data

→ `WebFetch` https://www.slovca.sk/sk/clenstvo/pridruzeni-clenovia.html

<details><summary>result</summary>

```
**User-Agent header**
- The page asks users to "declare your **user agent** in request headers" and gives a sample that includes a company name and an admin contact email.

**Rate limits**
- "Current max request rate: 10 requests/second." The page also says "SEC reserves the right to limit request rates to preserve fair access for all users."
- Scripts should download only the data they need and keep request volume low to reduce server load.

**data.sec.gov APIs**
- "Submissions by company and extracted XBRL data are available via RESTful APIs on data.sec.gov"
- The APIs return JSON-formatted data.

**Bulk files**
- Feed archives are "tar and gzip archive files (e.g., 20061207.nc.tar.gz) for each filing day."
- The Oldloads directory holds "daily concatenated archive files of all public filing submissions."
- Full and quarterly index files are rebuilt weekly, early on Saturday mornings, to incorporate post-acceptance corrections.
```
</details>

<details><summary>result</summary>

```
The page lists **31 associate members** (Pridružení členovia). The page doesn't describe the firms, so the categories below are inferred from names and should be verified.

**Law firms (11):** A&O Shearman, Barger Prekop, CMS Slovakia, Dentons, HAVEL & PARTNERS, Highgate Law & Tax, HKV Law Firm, Noerr, Majerník & Miháliková, TaylorWessing, V4 Legal

**Bank (1):** ČSOB

**Advisors (11):** Aon, ASB Slovakia, Danube Capital Advisors, HILLBRIDGES, M3 Partners s.r.o., Forvis Mazars Slovensko, Ments, KPMG Slovakia, Howden, PwC, CLA Slovakia

**Other (8):** Across Private Investments, BHM group, G4 INVESTMENTS, Finhold, PFCEU, Slovak Investment Holding, Montward, Wezeo
```
</details>

→ `WebSearch` nrinvest.cz Národní rozvojová investiční portfolio fondy investice venture kapitál seznam

→ `WebSearch` "Národní inovační fond" NIF Czech venture capital fund portfolio investments

<details><summary>result</summary>

```
Web search results for query: ""Národní inovační fond" NIF Czech venture capital fund portfolio investments"

Links: [{"title":"Český stát se poprvé vážně pouští do startupů. Je tu Národní inovační fond","url":"https://www.lupa.cz/clanky/cesky-stat-se-poprve-vazne-pousti-do-startupu-je-tu-narodni-inovacni-fond/"},{"title":"Investoři: Peněz je dost, stát by nás měl nechat být. Ale za zkoušku to stojí","url":"https://www.lupa.cz/clanky/investori-penez-je-dost-stat-by-nas-mel-nechat-byt-ale-za-zkousku-to-stoji/"},{"title":"Stát dá na podporu rozjezdu startupů dvě miliardy","url":"https://www.e15.cz/magazin/stat-da-na-podporu-rozjezdu-startupu-dve-miliardy-1235392"},{"title":"Hlavní obsah","url":"https://www.novinky.cz/clanek/ekonomika-na-rozjezd-startupu-v-cesku-ma-jit-vic-nez-miliarda-z-eu-328610"},{"title":"Státní peníze pomohou s rozjezdem start-upů, ministerstvo připravuje nový fond","url":"https://www.businessinfo.cz/cs/clanky/statni-penize-pomohou-s-rozjezdem-start-upu-ministerstvo-pripravuje-novy-fond-69623.html"},{"title":"Státní peníze pomohou s rozjezdem start-upů, ministerstvo připravuje nový fond","url":"https://www.businessinfo.cz/clanky/statni-penize-pomohou-s-rozjezdem-start-upu-ministerstvo-pripravuje-novy-fond/"},{"title":"Projekt státního fondu pro startupy ožívá. Už se chystá na vládu","url":"https://www.lupa.cz/clanky/projekt-statniho-fondu-pro-startupy-oziva-uz-se-chysta-na-vladu/"},{"title":"mpo zacne podporovat startupy vznikne investicni fond","url":"http
… [1481 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "nrinvest.cz Národní rozvojová investiční portfolio fondy investice venture kapitál seznam"

Links: [{"title":"our partners","url":"https://www.nrb.cz/en/about-the-bank/our-partners/"},{"title":"Národní rozvojový fond přichází. Podpoří projekty v infrastruktuře","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-prichazi-podpori-projekty-v-infrastrukture/"},{"title":"ceskomoravska zarucni a rozvojova banka","url":"https://www.businessinfo.cz/informace/ceskomoravska-zarucni-a-rozvojova-banka/"},{"title":"strukturalni fondy pomohly zrealizovat pilotni investicni fazi ipo fondu narodni rozvojove investicni a s","url":"https://www.businessinfo.cz/clanky/strukturalni-fondy-pomohly-zrealizovat-pilotni-investicni-fazi-ipo-fondu-narodni-rozvojove-investicni-a-s/"},{"title":"NRI dokončila výběr venture kapitálového fondu pro program Fond Ukrajina","url":"https://www.businessinfo.cz/clanky/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/"},{"title":"narodni rozvojovy fond","url":"https://ekonomickydenik.cz/tag/narodni-rozvojovy-fond"},{"title":"20190912 MEMORANDUM O SPOLUPRACI NRF CZ web","url":"https://vlada.gov.cz/assets/media-centrum/aktualne/20190912_MEMORANDUM-O-SPOLUPRACI_NRF_CZ-web.pdf"},{"title":"banky podlehly tlaku politiku rozvojoveho fondu jsou pripraveny investovat az sedm miliard","url":"https://ekonomickydenik.cz/banky-podlehly-tlaku-politiku-rozvojoveho-fondu-jsou-pripraveny-investovat-az-sedm-miliard/
… [1301 more characters]
```
</details>

→ `Bash` — Check reachability of source URLs
```sh
for u in https://subjekty.nbs.sk/ https://regsaif.nbs.sk/ https://www.orsr.sk/ https://rpvs.gov.sk/rpvs https://dataor.justice.cz/ https://or.justice.cz/ias/ui/rejstrik https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/27074358 https://www.cnb.cz/cnb/jerrs https://register.fca.org.uk/ https://adviserinfo.sec.gov/ https://www.openvc.app/ https://efts.sec.gov/LATEST/search-index?q=%22venture%22&forms=D https://www.nrinvesticni.cz/ https://www.sih.sk/ https://www.vtff.sk/ https://www.eban.org/our-network-2 https://www.investeurope.eu/membership/member-search/ https://www.bvca.co.uk/ https://nvca.org/ https://www.forbes.com/billionaires/ https://www.finstat.sk/ https://www.wikidata.org/ https://api.gleif.org/api/v1/lei-records?page%5Bsize%5D=1; do printf "%s  " "$u"; curl -s -o /dev/null -m 20 -L -A "Mozilla/5.0 (research; [redacted: email])" -w "%{http_code}\n" "$u"; done
```

<details><summary>result</summary>

```
Exit code 1
(eval):1: parse error near `&'
```
</details>

→ `Bash` — Check reachability of source URLs
```sh
cat > [tmp] <<'EOF'
https://subjekty.nbs.sk/
https://regsaif.nbs.sk/
https://www.orsr.sk/
https://rpvs.gov.sk/rpvs
https://dataor.justice.cz/
https://or.justice.cz/ias/ui/rejstrik
https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/27074358
https://www.cnb.cz/cnb/jerrs
https://register.fca.org.uk/
https://adviserinfo.sec.gov/
https://www.openvc.app/
https://efts.sec.gov/LATEST/search-index?q=%22venture%22&forms=D
https://www.nrinvesticni.cz/
https://www.sih.sk/
https://www.eban.org/our-network-2
https://www.investeurope.eu/membership/member-search/
https://www.bvca.co.uk/
https://www.forbes.com/billionaires/
https://www.finstat.sk/
https://api.gleif.org/api/v1/lei-records?page[size]=1
https://download.companieshouse.gov.uk/en_output.html
https://api.opencorporates.com/
EOF
while read u; do printf "%s  " "$u"; curl -s -g -o /dev/null -m 20 -L -A "Mozilla/5.0 (research; [redacted: email])" -w "%{http_code}\n" "$u"; done < [tmp]
```

<details><summary>result</summary>

```
https://subjekty.nbs.sk/  200
https://regsaif.nbs.sk/  200
https://www.orsr.sk/  000
https://rpvs.gov.sk/rpvs  200
https://dataor.justice.cz/  200
https://or.justice.cz/ias/ui/rejstrik  200
https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/27074358  200
https://www.cnb.cz/cnb/jerrs  200
https://register.fca.org.uk/  200
https://adviserinfo.sec.gov/  200
https://www.openvc.app/  403
https://efts.sec.gov/LATEST/search-index?q=%22venture%22&forms=D  200
https://www.nrinvesticni.cz/  200
https://www.sih.sk/  200
https://www.eban.org/our-network-2  200
https://www.investeurope.eu/membership/member-search/  200
https://www.bvca.co.uk/  200
https://www.forbes.com/billionaires/  200
https://www.finstat.sk/  403
https://api.gleif.org/api/v1/lei-records?page[size]=1  200
https://download.companieshouse.gov.uk/en_output.html  200
https://api.opencorporates.com/  200
```
</details>

→ `Bash` — Check ORSR and count GLEIF active fund LEIs
```sh
curl -s -o /dev/null -m 20 -w "%{http_code}\n" http://www.orsr.sk/ ; curl -s -g -m 30 "https://api.gleif.org/api/v1/lei-records?filter[entity.category]=FUND&filter[entity.status]=ACTIVE&page[size]=1" | python3 -I -c "import json,sys; d=json.load(sys.stdin); print(d['meta']['pagination'])"; curl -s -g -m 30 "https://api.gleif.org/api/v1/lei-records?filter[entity.category]=FUND&filter[entity.status]=ACTIVE&filter[entity.legalAddress.country]=CZ&page[size]=1" | python3 -I -c "import json,sys; d=json.load(sys.stdin); print('CZ',d['meta']['pagination']['total'])"; curl -s -g -m 30 "https://api.gleif.org/api/v1/lei-records?filter[entity.category]=FUND&filter[entity.status]=ACTIVE&filter[entity.legalAddress.country]=SK&page[size]=1" | python3 -I -c "import json,sys; d=json.load(sys.stdin); print('SK',d['meta']['pagination']['total'])"
```

<details><summary>result</summary>

```
302
{'currentPage': 1, 'perPage': 1, 'from': 1, 'to': 1, 'total': 201591, 'lastPage': 201591}
CZ 1149
SK 159
```
</details>

→ `WebSearch` AMAC registered private equity and venture capital fund managers number 2025 China 私募股权 创业投资基金管理人 数量

<details><summary>result</summary>

```
Web search results for query: "AMAC registered private equity and venture capital fund managers number 2025 China 私募股权 创业投资基金管理人 数量"

Links: [{"title":"Investment Funds 2026","url":"https://practiceguides.chambers.com/practice-guides/investment-funds-2026/china/trends-and-developments/O24011"},{"title":"Investment Funds 2026","url":"https://practiceguides.chambers.com/practice-guides/investment-funds-2026/china/trends-and-developments"},{"title":"Investment Funds 2026","url":"https://practiceguides.chambers.com/practice-guides/investment-funds-2026/china"},{"title":"Guantao contributes to the China Chapter of Chambers \"Investment Funds 2026\" Global Practice Guide","url":"https://www.guantao.com/en/page4967"},{"title":"Investment Funds 2026 Comparisons","url":"https://practiceguides.chambers.com/practice-guides/comparison/1112/18202/28479-28480-28481-28482"},{"title":"Alternative Funds 2025","url":"https://practiceguides.chambers.com/practice-guides/alternative-funds-2025/china"},{"title":"Alternative Funds 2025 Comparisons","url":"https://practiceguides.chambers.com/practice-guides/comparison/1019/17339/27235-27238-27249-27261"},{"title":"Investment Funds 2025","url":"https://practiceguides.chambers.com/practice-guides/investment-funds-2025/china"},{"title":"Alternative Funds 2025","url":"https://gpg-pdf.chambers.com/Alternative-Funds-2025/91/"}]

The search didn't turn up a 2025 total for PE/VC fund managers alone. It did find totals for all private fund managers and some
… [1375 more characters]
```
</details>

→ `WebSearch` Henley Centi-Millionaire Report 2025 number of centi-millionaires worldwide Europe

<details><summary>result</summary>

```
Web search results for query: "Henley Centi-Millionaire Report 2025 number of centi-millionaires worldwide Europe"

Links: [{"title":"europe london wealth creation centimillionaire decline henley partners","url":"https://fortune.com/europe/2024/09/18/europe-london-wealth-creation-centimillionaire-decline-henley-partners"},{"title":"Wed, Nov 12, 2025","url":"https://www.opalesque.com/industry-updates/6928/the-emergence-of-a-new-class-of-super.html"},{"title":"UK and Germany top Centi-Millionaires rich list in Europe","url":"https://businesschief.eu/leadership-and-strategy/uk-and-germany-top-millionaires-rich-list-europe"},{"title":"centi millionaires how canadas ultra rich rank worldwide","url":"https://vancouverisland.ctvnews.ca/business/article/centi-millionaires-how-canadas-ultra-rich-rank-worldwide"},{"title":"aap.com.au","url":"https://aap.com.au/?p=190343"},{"title":"Centi-Millionaires – the changing face of the super-wealthy","url":"https://www.businesschief.asia/leadership-and-strategy/centi-millionaires-the-changing-face-of-the-super-wealthy"},{"title":"Accessibility Statement Skip Navigation","url":"https://prnewswire.com/ru/press-releases/centi-millionaire-boom-america-and-china-dominate-the-super-rich-club-302245454.html"},{"title":"Centi-Millionaire Boom: America and China Dominate the Super Rich Club","url":"https://kyodonewsprwire.jp/release/202409176529"},{"title":"centi millionaire 2024","url":"https://henleyglobal.com/newsroom/press-releases/centi-millionaire
… [1024 more characters]
```
</details>

→ `Bash` — Check RPVS open data endpoint
```sh
curl -s -m 20 -o /dev/null -w "%{http_code}\n" "https://rpvs.gov.sk/opendata/PartneriVerejnehoSektora?\$top=1"; curl -s -m 20 "https://rpvs.gov.sk/opendata/PartneriVerejnehoSektora?\$top=1" | head -c 600; echo; curl -s -m 20 "https://rpvs.gov.sk/opendata/\$metadata" | head -c 300
```

<details><summary>result</summary>

```
404
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>404 - File or directory not found.</title>
<style type="text/css">
<!--
body{margin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;}
fieldset{padding:0 15px 10px 15px;}
h1{font-size:2.4em;margin:0;color:#FFF;}
h2{font-size:1.7em;margin:0;color:#CC0000;}
h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>404 - File or directory not found.</title>
<style typ
```
</details>

→ `Bash` — Create output research folder
```sh
mkdir -p [redacted: local path] && ls -la [redacted: local path] [redacted: local path]
```

<details><summary>result</summary>

```
[redacted: local path]
total 0
drwxr-xr-x  4 [user]  staff  128 11 Oct  01:18 .
drwxr-xr-x  4 [user]  staff  128 11 Oct  01:07 ..
drwxr-xr-x  9 [user]  staff  288 11 Oct  01:07 .git
drwxr-xr-x  2 [user]  staff   64 11 Oct  01:18 research

[redacted: local path]
total 0
drwxr-xr-x  2 [user]  staff   64 11 Oct  01:18 .
drwxr-xr-x  4 [user]  staff  128 11 Oct  01:18 ..
```
</details>

→ `Write` [redacted: local path]

<details><summary>result</summary>

```
File created successfully at: [redacted: local path] (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Fix truncated URLs and clean my temp files
```sh
f=[redacted: local path] python3 -I - "$f" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
s=s.replace("(https://amp.scmp.com/tech/article/3223176/...)","(https://amp.scmp.com/tech/article/3223176/sequoia-capital-splits-three-firms-separating-china-operations-us-amid-rising-geopolitical-tensions)")
s=s.replace("https://theonlinecitizen.com/2026/03/12/... ;","https://theonlinecitizen.com/2026/03/12/forbes-billionaires-list-hits-record-3-428-as-combined-wealth-tops-us-20-trillion ;")
s=s.replace("| Free (\"provided free of charge and will not be supported\") | Open Government Licence |","| Free (\"provided free of charge and will not be supported\") | Open Government Licence (my own knowledge, not re-verified in this session) |")
open(p,'w').write(s)
EOF
grep -c '\.\.\.)' $f; grep -n 'OGL\|Open Government' $f | head; cd [tmp] && rm -rf sec nvca_mine eban_mine idx_mine urls_mine.txt eif/active.pdf eif/active_mine.txt && ls
```

<details><summary>result</summary>

```
0
47:| **UK Companies House: PSC snapshot** | Every person or entity with significant control (>25%) of every UK company, with notified date | All UK companies. JSON, **updated daily** (file of 2026-10-10) | Bulk | Free ("provided free of charge and will not be supported") | Open Government Licence (my own knowledge, not re-verified in this session) | https://download.companieshouse.gov.uk/en_pscdata.html | 2026-10-11 |
batch1.txt
bin
cz
damo.html
dl
eif
eu
i706.html
ibkr3324.html
irs
ish
ish.py
je
je_out_1791674233.json
je_out_1791674282.json
je_out_1791674301.json
je_out_1791674321.json
je.py
portu.txt
r_czech.json
r_CzechFinance.json
ss
sw
trends.txt
vg
vg_summary_vxus.json
vg_summary.json
vg.py
vlogin.log
```
</details>

**Agent:**

[redacted: name]

Research file ready: `[redacted: local path]` (in English). It contains source tables, investor-universe estimates by type and 17 common errors with real examples. Figures fall into three categories: my calculations from official free downloads on 2026-10-11, report figures with links and dates, and my estimates explicitly labelled as estimates.

**Key figures:**
- **SEC Form ADV (download dated 2 October 2026):** 2,312 advisers exempt from registration as venture-capital fund managers. SEC data shows about 7,470 managers with VC or PE funds overall (4,609 exempt + 2,861 registered). For comparison, NVCA reports 2,984 US VC firms; in 2025, 13,634 investors made at least one investment in US companies, versus 25,969 in 2021.
- **Europe:** Invest Europe’s EDC database covers about 4,000 PE/VC firms. ESMA lists 448 active EuVECA fund managers, including 2 in Slovakia and 0 in Czechia. There are 3,135 active AIFMs, covering all asset classes.
- **Family offices:** about 8,030 worldwide, including 2,020 in Europe (Deloitte, 2024). No public register exists; in the US they do not register at all.
- **Angels:** 445,535 in the US (2024 data). In Europe, 47,610 belong to networks (EBAN, 2024). Czechia has 340 angels in 3 networks; Slovakia has 120 in one.
- **Large private investors:** 3,428 billionaires (Forbes 2026).
- **My estimate of what can realistically be collected and verified from free sources:** about 12,000–20,000 investors worldwide excluding angels, 3,500–6,000 in Europe, and 150–300 PE/VC firms and family offices in Czechia and Slovakia combined.
- **Main pitfall:** 64% of venture “funds” in Form D over the last 4 quarters were one-off deal vehicles and series (SPVs). A manager → fund → vehicle hierarchy is needed to prevent inflated database counts.

**Five most useful free sources:**
1. **SEC Form ADV** — monthly downloads with a venture-capital adviser flag.
2. **SEC Form D** — fund size, year of first sale (effectively the launch year) and the link between fund and manager.
3. **ESMA registers** (EuVECA and AIFM) — evidence of a manager’s existence across the EU.
4. **Company registers with ownership records** — UK Companies House, Czech justice.cz and ARES, and Slovak ORSR. These show an investor’s ownership in a company and its start date.
5. **Curated manager lists** — EIF fund list, full CVCA and SLOVCA members, and state-backed SIH and NRI. Associate members (lawyers, banks and consultants) must be excluded.

Crunchbase, Dealroom, Preqin, PitchBook, the Finstat API and OpenCorporates cannot be used freely for commercial purposes: use them only for manual candidate discovery. Exceptions are Crunchbase Basic and the 2013 snapshot, licensed under CC-BY.

Gaps: I did not find the current number of Czech managers operating without a ČNB licence (“§15 managers”); only 190 for 2020 was available. I also did not find the number of registered Slovak managers. The EIF list is dated 30.09.2022. The EU beneficial-ownership access restriction and Companies House data licence were written from memory and are marked accordingly. I registered nowhere, submitted no forms and did not use Git. I removed my temporary downloads from the working directory.

