# Agent: Slovak VC candidates

Claude Code sub-agent log, exported from `agent-a56118ade50469af1.jsonl`.
Tool outputs longer than 1,500 characters are shortened.
Russian narrative has been translated into English; executed tool code and source quotations are retained.

## Brief

You are a research analyst building the PILOT SAMPLE for a job test task: "Reliable database of investors". The pilot sample = venture capital investors based in SLOVAKIA (managed from Slovakia, or Slovak-founded with a Slovak investment team). Only public data may be used.

Goal: enumerate as completely as possible every candidate, then gather evidence for each. Recall matters: also list entities that LOOK like VC investors but should probably be excluded (accelerators without equity, crowdfunding platforms, M&A/advisory boutiques, grant agencies, banks, dormant/closed funds, foreign funds with only a Slovak partner, angel networks, corporate VCs, public fund-of-funds) — they are needed to show the inclusion/exclusion rules working. Where to look for candidates: SLOVCA (Slovak Venture Capital Association) member list, Slovak Investment Holding / National Development Fund II (NDF II) portfolio of VC funds and co-investment partners, EIF portfolio for Slovakia, Startitup.sk / Forbes.sk / Trend.sk / Index.sk / CzechCrunch / Rozhlas / StartupJobs funding news, Dealroom public pages, Crunchbase public pages, Neulogy Ventures, Limerock Fund, Zero Gravity Capital, Crowdberry, Sandberg Capital, Fond inovácií a technológií (FIT, ex-SIH), Prvá kapitálová, Venture to Future Fund, Nation1, Gapfunding, Bitcoin-era funds, 0100 Ventures (CZ/SK), Credo (CZ – likely exclude as Czech), Presto Ventures (CZ), Tatra Bank/VUB corporate initiatives, Swiss Re etc. Do not trust this list — verify everything; some may be wrong, Czech, or inactive.

For each candidate collect (null if unknown, never guess):
- name, legal entity name(s) (management company and fund vehicle(s) separately), Slovak IČO and register link (ORSR orsr.sk or finstat.sk) if found, website, HQ city
- proposed type (VC / PE / CVC / angel network / accelerator / fund-of-funds / crowdfunding / other)
- sectors focus, stages, geography, typical ticket min/max (EUR) as stated by the investor
- fund size(s) / AUM with vintage year
- REQUIRED: up to 3 most recent dated investments (portfolio company, date of announcement or registry entry, round size if public, URL of the source). Prefer primary sources: press release, investor's portfolio page, business register shareholder entry (finstat/orsr shows shareholders of Slovak s.r.o. companies — the fund vehicle as a shareholder with a date is strong evidence).
- for EVERY field above a source URL + accessed date (2026-10-11) + the publication date if visible. Use a per-field "sources" map.
- your proposed decision: include / exclude / uncertain, with the reason.

Rules:
- Use WebSearch and WebFetch heavily (many searches; Slovak-language queries work best, e.g. "investícia startup 2025 fond", "investoval", "rizikový kapitál", "kolo financovania"). Spend real effort; aim for 30+ candidates.
- Never fabricate URLs or figures. If a page did not load, say so. Quote the exact sentence from the source for ticket size, fund size and investment date in a field "evidence_quotes".
- No signups, no forms, no paid APIs, no git, don't touch other files.

Output: [redacted: local path] (array of objects, one per candidate, UTF-8, pretty-printed) and a short [redacted: local path] (table: name | type | proposed decision | reason | latest dated investment). Create the folder if missing. Also note in the md roughly how many VC investors are based in the Czech Republic (just a cited estimate, for context). Final message: counts (candidates / include / exclude / uncertain), the 5 weakest records, the path.

→ `ToolSearch`

<details><summary>result</summary>

```

```
</details>

→ `WebFetch` https://www.slovca.sk/clenovia/

<details><summary>result</summary>

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebSearch` SLOVCA členovia venture capital fondy zoznam

<details><summary>result</summary>

```
Web search results for query: "SLOVCA členovia venture capital fondy zoznam"

Links: [{"title":"Popularita private equity a venture kapitálu na Slovensku","url":"https://www.podnikajte.sk/investor/private-equity-venture-kapital-na-slovensku"},{"title":"www.podnikajte.sk","url":"https://www.podnikajte.sk/financie?page=36"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/investor/investorske-forum-bratislava"},{"title":"Compare Genesis Capital vs SLOVCA","url":"https://www.cbinsights.com/compare/genesis-capital-sro-vs-slovca"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/financie/c/1994/category/investor/article/investorske-forum-bratislava.xhtml"},{"title":"Compare HVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/hvca-vs-slovca"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/slovca"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=6"},{"title":"Compare EstVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/estvca-vs-slovca"},{"title":"Compare BVCA vs SLOVCA","url":"https://www.cbinsights.com/compare/bvca-vs-slovca"}]

The search didn't turn up an official SLOVCA member list, so I can't confirm which VC funds are current members.

- **What SLOVCA is:** SLOVCA is an association that focuses on venture capital and private equity within the financial services industry. It was founded in 19
… [1125 more characters]
```
</details>

→ `WebFetch` https://www.slovca.sk/

→ `WebSearch` slovca.sk members full members list

<details><summary>result</summary>

```
Web search results for query: "slovca.sk members full members list"

Links: [{"title":"List of members of the European Parliament for Slovakia, 2024%E2%80%932029","url":"https://en.wikipedia.org/wiki/List_of_members_of_the_European_Parliament_for_Slovakia,_2024%E2%80%932029"},{"title":"List of members of the European Parliament for Slovakia, 2014%E2%80%932019","url":"https://en.wikipedia.org/wiki/List_of_members_of_the_European_Parliament_for_Slovakia,_2014%E2%80%932019"},{"title":"National Delegation of Slovakia","url":"https://www.cor.europa.eu/hr/node/105"},{"title":"Organization Profile","url":"https://iau.org/Shared_Content/Contacts/OrganizationLayouts/Organization_Profile.aspx?ID=23872"},{"title":"Logo Assembly Logo Hemicycle","url":"https://pace.coe.int/en/members/8911"},{"title":"Union of Towns and Cities of Slovakia","url":"https://www.alda-europe.eu/alda_member/union-of-towns-and-cities-of-slovakia/"},{"title":"Union of Towns and Cities of Slovakia","url":"https://www.alda-europe.eu/?p=2895"},{"title":"National Delegation of Slovakia","url":"https://www.cor.europa.eu/de/node/105"},{"title":"Slovak Republic Becomes Member State of EATRIS-ERIC","url":"https://eatris.eu/news/slovak-republic-becomes-member-state-of-eatris-eric/"},{"title":"2024 pre congress report   slovakia","url":"https://iaml.info/sites/default/files/pdf/2024_pre-congress_report_-_slovakia.pdf"}]

The search returned nothing from slovca.sk, so I can't give you its members list. The results were about
… [502 more characters]
```
</details>

<details><summary>result</summary>

```
Base URL: `https://www.slovca.sk`

**Main navigation**

- **O nás:** `/sk/stranky/o-nas`
  - SLOVCA dnes: `/sk/o-nas/slovca-dnes.html`
  - Správna rada: `/sk/o-nas/spravna-rada.html`
  - Legal & Tax Committee: `/sk/o-nas/legal-tax-committee.html`
  - Stanovy: `/sk/o-nas/stanovy.html`
- **Novinky:** `/sk/kategoria/novinky`
  - Novinky ohľadom PE-VC: `/sk/kategoria/novinky-ohladom-pe-vc`
  - Podujatia: `/sk/kategoria/podujatia`
- **Na stiahnutie:** `/sk/kategoria/na-stiahnutie`
  - Štatistiky: `/sk/kategoria/statistiky`
  - Tlačové správy: `/sk/kategoria/tlacove-spravy`
  - Vzorové dokumenty: `/sk/kategoria/vzorove-dokumenty`
- **Členstvo:** `/sk/stranky/clenstvo`
  - Riadni členovia: `/sk/clenstvo/riadni-clenovia.html`
  - Pridružení členovia: `/sk/clenstvo/pridruzeni-clenovia.html`
  - Partnerskí členovia: `/sk/clenstvo/partnerski-clenovia.html`
  - Partneri: `/sk/clenstvo/partneri.html`
  - Etický kódex: `/sk/clenstvo/eticky-kodex.html`
  - Prihláška: `/sk/clenstvo/prihlaska.html`
- **Private Equity & Venture Capital:** `/sk/stranky/private-equity-venture-capital`
  - Vysvetlenie pojmov: `/sk/private-equity-venture-capital/vysvetlenie-pojmov.html`
  - Kapitálové investície vs pôžičky: `/sk/private-equity-venture-capital/kapitalove-investicie-vs-pozicky.html`
- **Kontakt:** `/sk/kontakt.html`
- **Language:** SK `/` and EN `/en`

**Members**

The page does not contain a member list. It links to these membership pages:
- Riadni členovia: `https://www.slovca.sk/sk/clenstvo/riadn
… [246 more characters]
```
</details>

→ `WebFetch` https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html

→ `WebFetch` https://www.slovca.sk/sk/clenstvo/pridruzeni-clenovia.html

→ `WebFetch` https://www.slovca.sk/sk/clenstvo/partnerski-clenovia.html

<details><summary>result</summary>

```
The page lists 12 full members (Riadni členovia). It gives only names, and each links to a SLOVCA profile page. It contains no external member websites and no description text.

1. ARX Equity Partners (https://www.slovca.sk/sk/riadni-clenovia/arx-equity-partners.html)
2. CVI (https://www.slovca.sk/sk/riadni-clenovia/cvi.html)
3. Enterprise Investors (https://www.slovca.sk/sk/riadni-clenovia/enterprise-investors.html)
4. Eterus Capital (https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html)
5. Fond inovácií a technológií (https://www.slovca.sk/sk/riadni-clenovia/fond-inovacii-a-technologii.html)
6. Genesis Capital (https://www.slovca.sk/sk/riadni-clenovia/genesis-capital.html)
7. Jet Investment (https://www.slovca.sk/sk/riadni-clenovia/jet-investment.html)
8. Národný holdingový fond s.r.o. (https://www.slovca.sk/sk/riadni-clenovia/narodny-holdingovy-fond-s-r-o.html)
9. Neulogy Ventures (https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html)
10. Sandberg Capital (https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html)
11. Venture to Future Fund (https://www.slovca.sk/sk/riadni-clenovia/venture-to-future-fund.html)
12. Vision Ventures (https://www.slovca.sk/sk/riadni-clenovia/vision-ventures.html)

The domain "www.slovca.sk" is inferred from the page's contact details and footer. The page itself only gives relative paths such as `/sk/riadni-clenovia/cvi.html`.
```
</details>

<details><summary>result</summary>

```
The page lists seven partner members. It gives no descriptions, and no external websites. The only links are internal SLOVCA pages.

1. Slovenská franchízingová asociácia (`/sk/partnerski-clenovia/slovenska-franchizingova-asociacia.html`)
2. JA Slovensko (`/sk/partnerski-clenovia/ja-slovensko.html`)
3. Slovenská akadémia vied (`/sk/partnerski-clenovia/slovenska-akademia-vied.html`)
4. Fakulta podnikového manažmentu (`/sk/partnerski-clenovia/fakulta-podnikoveho-manazmentu.html`)
5. ZMPS (`/sk/partnerski-clenovia/zmps.html`)
6. Chorvátsko – Slovenská Obchodná Komora (`/sk/partnerski-clenovia/chorvatsko-slovenska-obchodna-komora.html`)
7. International Sustainable Finance Centre (`/sk/partnerski-clenovia/international-sustainable-finance-centre.html`)

To get the websites and descriptions, you would need to open each member's detail page on the SLOVCA site.
```
</details>

<details><summary>result</summary>

```
The page lists 31 associate members (pridružení členovia), but it doesn't include descriptions or external websites. Each entry shows only a name, a logo, and a link to the member's SLOVCA profile page, so I've listed those paths instead.

| # | Name | Profile page (relative link) |
|---|------|------------------------------|
| 1 | Across Private Investments | /sk/pridruzeni-clenovia/across-private-investments.html |
| 2 | Aon | /sk/pridruzeni-clenovia/aon.html |
| 3 | A&O Shearman | /sk/pridruzeni-clenovia/a-o-shearman.html |
| 4 | ASB Slovakia | /sk/pridruzeni-clenovia/asb-slovakia.html |
| 5 | Barger Prekop | /sk/pridruzeni-clenovia/barger-prekop.html |
| 6 | BHM group | /sk/pridruzeni-clenovia/bhm-group.html |
| 7 | CMS Slovakia | /sk/pridruzeni-clenovia/cms-slovakia.html |
| 8 | ČSOB | /sk/pridruzeni-clenovia/csob.html |
| 9 | Danube Capital Advisors | /sk/pridruzeni-clenovia/danube-capital-advisors.html |
| 10 | Dentons | /sk/pridruzeni-clenovia/dentons.html |
| 11 | HAVEL & PARTNERS | /sk/pridruzeni-clenovia/havel-partners.html |
| 12 | Highgate Law & Tax | /sk/pridruzeni-clenovia/highgate-law-tax.html |
| 13 | HKV Law Firm | /sk/pridruzeni-clenovia/hkv-law-firm.html |
| 14 | HILLBRIDGES | /sk/pridruzeni-clenovia/hillbridges.html |
| 15 | G4 INVESTMENTS | /sk/pridruzeni-clenovia/g4-investments.html |
| 16 | Finhold | /sk/pridruzeni-clenovia/finhold.html |
| 17 | M3 Partners s.r.o. | /sk/pridruzeni-clenovia/m3-partners-s-r-o.html |
| 18 | Forvis Mazars Slovensko | /sk/p
… [995 more characters]
```
</details>

→ `WebSearch` Národný rozvojový fond II venture kapitál fondy koinvestičné partneri zoznam

→ `WebFetch` https://www.nrf.sk/

<details><summary>result</summary>

```
Web search results for query: "Národný rozvojový fond II venture kapitál fondy koinvestičné partneri zoznam"

Links: [{"title":"Národní rozvojový fond vlády umožní investice v řádu desítek miliard korun","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-vlady-umozni-investice-v-radu-desitek-miliard-korun/"},{"title":"NRI dokončila výběr venture kapitálového fondu pro program Fond Ukrajina","url":"https://www.businessinfo.cz/clanky/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=34908"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=27410"},{"title":"narodni rozvojovy fond","url":"https://ekonomickydenik.cz/tag/narodni-rozvojovy-fond"},{"title":"Národní rozvojový fond bude spravovat státní banka, na investice půjde až 35 miliard","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/narodni-rozvojovy-fond-bude-spravovat-statni-banka-na-investice-pujde-az-35-miliard-1360230"},{"title":"banky podlehly tlaku politiku rozvojoveho fondu jsou pripraveny investovat az sedm miliard","url":"https://ekonomickydenik.cz/banky-podlehly-tlaku-politiku-rozvojoveho-fondu-jsou-pripraveny-investovat-az-sedm-miliard/"},{"title":"Národní rozvojový fond získal licenci ČNB","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-ziskal-licenci-cnb/"},{"title":"Národní rozvojový fond na startu: podepsáno memorandum, startuje příprava pilotních projektů","url":"
… [1093 more characters]
```
</details>

<details><summary>result</summary>

```
The page doesn't mention NDF II (Národný rozvojový fond II), any venture capital funds, fund managers, or co-investment partners. It's the homepage of Nrf.sk, a Slovak financial education site run by NRF, s.r.o. For fund information, you'd need a source that covers NDF II directly.

**Navigation links on the page:**

- Profil: https://nrf.sk/profil/
  - O nás (About us): /profil/o-nas/
  - Ochrana osobných údajov (Privacy policy): /profil/ochrana-osobnych-udajov/
  - Obchodní partneri (Business partners): /profil/obchodni-partneri/
- Vzdelávanie (Education): /vzdelavanie/
  - Možnosti vzdelávania (Education options): /vzdelavanie/moznosti-vzdelavania/
  - Finančný spravodaj (Financial news): /vzdelavanie/financny-spravodaj/
- Kariéra (Careers): /kariera/
- Kontakt (Contact): /kontakt/
- ONLINE
  - Kalkulačka (Calculator): /online/
  - Registrácia zdarma (Free registration): /registracia-zdarma/
- GDPR: /ochrana-osobnych-udajov/
  - Základné informácie (Basic information): /GDPR/zakladne-informacie/
  - Príjemcovia (Recipients): /GDPR/prijemcovia/
  - Práva dotknutej osoby (Data subject rights): /GDPR/prava-dotknutej-osoby/
  - Uzatváranie zmlúv elektronickými prostriedkami s použitím biometrického podpisu (Electronic contracts with biometric signature): /GDPR/uzatvaranie-zmluv-elektronickymi-prostriedkami-s-pouzitim-biometrickeho-podpisu/
  - Informácie o účele spracúvania a dobe uchovávania osobných údajov (Processing purposes and retention): /GDPR/informacie-o-ucele-spracuv
… [251 more characters]
```
</details>

→ `WebSearch` "Národný rozvojový fond II" koinvestícia startup investícia

→ `WebSearch` Slovak Investment Holding venture capital funds portfolio Neulogy Limerock Zero Gravity Crowdberry Sandberg NDF

<details><summary>result</summary>

```
Web search results for query: ""Národný rozvojový fond II" koinvestícia startup investícia"

Links: [{"title":"Stát začal českým startupům rozdělovat evropské miliardy z Národního plánu obnovy","url":"https://www.lupa.cz/aktuality/stat-zacal-ceskym-startupum-rozdelovat-evropske-miliardy-z-narodniho-planu-obnovy/"},{"title":"NRI dokončila výběr venture kapitálového fondu pro program Fond Ukrajina","url":"https://www.businessinfo.cz/clanky/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/"},{"title":"Národní rozvojový fond přichází. Podpoří projekty v infrastruktuře","url":"https://www.businessinfo.cz/clanky/narodni-rozvojovy-fond-prichazi-podpori-projekty-v-infrastrukture/"},{"title":"prvni investicni fond z narodniho planu obnovy bude spravovat tensor ventures","url":"https://forbes.cz/prvni-investicni-fond-z-narodniho-planu-obnovy-bude-spravovat-tensor-ventures/"},{"title":"V Česku vytvoria nový fond na podporu startupov s kapitálom 2,3 miliardy korún","url":"https://www.podnikajte.sk/investor/cesko-fond-startupy"},{"title":"První investiční VC fond z Národního plánu obnovy ČR bude spravovat Tensor Ventures","url":"https://www.businessinfo.cz/clanky/prvni-investicni-vc-fond-z-narodniho-planu-obnovy-cr-bude-spravovat-tensor-ventures/"},{"title":"Banky si rozdělily podíly v Národním rozvojovém fondu. Dva roky od vzniku může začít investovat","url":"https://www.e15.cz/domaci/banky-si-rozdelily-podily-v-narodnim-rozvojovem-fondu-dva-roky-od-vzniku-muze-za
… [2268 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Slovak Investment Holding venture capital funds portfolio Neulogy Limerock Zero Gravity Crowdberry Sandberg NDF"

Links: [{"title":"Crowdberry, Zero Gravity Ventures, and Vision Ventures to invest state money into Slovak start-ups","url":"https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"Neulogy Ventures","url":"https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia"},{"title":"most active slovak vc funds","url":"https://en.ain.ua/2022/11/30/most-active-slovak-vc-funds"},{"title":"New video case studies:","url":"https://fi-compass.eu/f/fi-compass-news-spring-2023/new-video-case-studies-slovak-investment-holding.html"},{"title":"limerock fund manager kapitalova investicia","url":"https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia"},{"title":"slovakia equity fundmanagers","url":"https://lb.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf"},{"title":"Venture Capital","url":"https://altss.com/profile/neulogy-ventures"}]

The search turned up
… [2205 more characters]
```
</details>

→ `WebFetch` https://lb.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf

<details><summary>result</summary>

```
getaddrinfo ENOTFOUND lb.eif.org
```
</details>

→ `WebFetch` https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov

<details><summary>result</summary>

```
The web page content you provided is empty, so I can't identify any financial intermediaries, amounts, programmes (such as NDF I or NDF II), or detail-page links.

If you paste the page text or the relevant sections, I'll extract the list from that material.
```
</details>

→ `WebFetch` https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf

→ `WebFetch` https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia

<details><summary>result</summary>

```
I can't return the table. The text you pasted is the raw binary of a PDF, and the page content (where the table would be) is in compressed streams that I can't decode here. The content is also truncated. I found no readable fund names, managers, countries, or mandates.

The only readable information is metadata:

- **Date:** The document's creation and modification date is 7 October 2026 (`D:20261007095419+02'00'`). The sensitivity label was set on 7 July 2026.
- **Author:** ZAJAC Mateusz
- **Producer:** Microsoft Excel for Microsoft 365

To get the table, you could paste its text or export it as CSV or plain text from Excel, or provide a screenshot or image of the page so I can read it.

[Binary content (application/pdf, 115.2KB) also saved to [redacted: private assistant config]]
```
</details>

<details><summary>result</summary>

```
**Page summary (paraphrased):** Slovak Investment Holding (SIH) invests in a Luxembourg-based fund managed by Neulogy Ventures, which handles the fund's management and strategy. The fund has two compartments that back start-ups and growth-oriented SMEs, one of which also includes private investors. Its investment period ran from 2014 to 2016, and it is now in its divestment period, returning capital to investors.

**Navigation and sidebar links:**

- Sectors (no URL shown)
- Contact: /en/kontakty
- About us: /en/stranky/o-nas/o-spolocnosti
- News: javascript:; (no real URL)
- Our Team: /en/stranky/o-nas/ludia
- Documents: javascript:; (no real URL)
- Financial Instruments: /en/stranky/financne-nastroje
- Logo/home: /en/
- LinkedIn: https://www.linkedin.com/company/slovak-investment-holding-sih/
- Slovak language version: /investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia

**Contact section and footer links:**

- Website: https://www.sih.sk
- Map: Google Maps link for Grösslingová 44, 811 09 Bratislava
- Footer items without URLs shown: Documents, Media, News, Data Protection, Mandatory Disclosures

**Other intermediaries:** The page does not name any intermediaries beyond Neulogy Ventures, so none are listed.

I summarized the body text instead of reproducing it verbatim, since you asked for a concise response.
```
</details>

→ `Bash` — Copy EIF PDF to scratchpad and check PDF tools
```sh
mkdir -p [tmp] && cp [redacted: private assistant config] [tmp] which pdftotext; python3 -c "import pypdf" 2>&1; python3 -c "import fitz" 2>&1
```

<details><summary>result</summary>

```
Exit code 1
/opt/homebrew/bin/pdftotext
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```
</details>

→ `Bash` — Extract text from EIF Slovakia fund managers PDF
```sh
cd [tmp] && pdftotext -layout eif.pdf eif.txt && cat eif.txt
```

<details><summary>result</summary>

```
                                                                                                                                                       Public   #




 Fund name                           Fund manager                           Team location   Mandate(s) short name   Target area   Geographical focus   Strategy          Main sector   Stage focus        Investment strategy set up   End of investment period   Fund Manager website
 Sandberg Investment Fund II SCSp    Sandberg Capital, sprav. spol., a.s.   Slovakia        CEFoF;COSME-EFG;EIF                   Multi-Country        Private Equity    Generalist    Lower-Mid Market   Fund                         12/01/2027                 https://sandberg.capital/#hero
 Slovak Venture Fund S.C.A., SICAR   Neulogy Ventures a.s.                  Slovakia        CEFoF;EGF                             Slovakia             Venture Capital   ICT           Balanced           Fund                         14/03/2027                 https://www.neulogy.vc/




EIF equity fund partners
as at 30 September 2026
```
</details>

→ `WebFetch` https://www.sih.sk/investicie/investicie-cez-financnych-sprostredkovatelov

→ `WebSearch` sih.sk kapitálová investícia finančný sprostredkovateľ venture fond 2024 2025

<details><summary>result</summary>

```
The web page content you provided is empty, so I can't identify any financial intermediaries, amounts, programmes, or links.

If you paste the page text, I'll list the equity and venture capital funds and other financial intermediaries it mentions, along with their amounts, programmes, and links.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "sih.sk kapitálová investícia finančný sprostredkovateľ venture fond 2024 2025"

Links: [{"title":"vision ventures kapitalova investicia","url":"https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia"},{"title":"limerock fund manager kapitalova investicia","url":"https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia"},{"title":"Slovenské startupy už nemusia odchádzať do zahraničia. Vznikol jedinečný fond na ich podporu","url":"https://www.startitup.sk/?p=358673"},{"title":"Zero Gravity Capital","url":"https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia"},{"title":"vs sih layout ok 326","url":"https://www.sih.sk/data/files/vs_sih_layout_ok-326.pdf"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"},{"title":"Informace pro účetní a podnikatele","url":"https://portal.pohoda.cz/pro-podnikatele/jak-zacit-podnikat/seed-venture-kapitalovy-fond-podpori-rizikove-investice"},{"title":"investicie zo slovak investment holding vyhrali celoeuropsku sutaz","url":"https://sita.sk/investicie-zo-slovak-investment-holding-vyhrali-celoeuropsku-sutaz/"},{"title":"Venture to Future Fund increase
… [1972 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/?p=358673

→ `WebFetch` https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups

<details><summary>result</summary>

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

<details><summary>result</summary>

```
**Fund:** Venture to Future Fund

- **Manager:** Slovak Asset Management, a licensed management company in the Slovak Investment Holding (SIH) investment group.
- **Size:** The article says the European Investment Bank, the Slovak Ministry of Finance, and SIH invested 40 million euros in total. The exact sentence is: "Európska investičná banka, Ministerstvo financií a Slovak Investment Holding do neho zainvestovali 40 mil. eur."
- **Ticket sizes:** The article does not state ticket sizes or per-company investment amounts. The closest figure is the EIB's contribution: "Európska investičná banka prispela fondu kapitálovým vkladom 10 mil. eur." This is the EIB's total capital contribution to the fund, not a ticket size.
- **Publication date:** 11 February 2020, at 14:07.
```
</details>

→ `WebFetch` https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov

→ `WebFetch` https://vff.sk/

<details><summary>result</summary>

```
**Publication date:** 28 May 2024 (Bratislava)

I can't reproduce the full article, but here are the requested details:

- **Fund size:** The fund started with EUR 40.4 million, set up in 2019 by the European Investment Bank and the Slovak Ministry of Finance through Slovak Investment Holding. In 2024 its capital rose by EUR 15.3 million from the Recovery and Resilience Plan.
- **Ticket range:** Investments run from EUR 400,000 to EUR 7 million. The article says this is "an increase from the original EUR 4.9 million," which is unclear, so check the fund's own materials.
- **Investment period:** Extended to the end of 2026, which the article describes as "extend the investment period of the VFF fund until the end of 2026."
- **Sectors:** Slovak small and medium-sized enterprises with innovative solutions, and European companies with capital ties to Slovakia. The capital increase targets technology companies in the growth phase.
- **Manager:** The article doesn't name a fund management company. It names governance figures: Matej Říha (Chairman of the VFF Board), Miriama Hanout (VFF Board Member), and Martin Banský (VFF Vice Chairman).
- **Legal and organizational names:** Venture to Future Fund (VFF); Slovak Investment Holding, a. s.; Research and Innovation Authority (VAIA); European Investment Bank (EIB); Ministry of Finance of the Slovak Republic.
- **Portfolio companies named:** Photoneo, Brightpick, Sensoneo, Powerful Medical, and Scaut.
```
</details>

<details><summary>result</summary>

```
**Fund legal name:** Venture to Future Fund, a.s. (Grösslingová 44, 811 09 Bratislava)

**Manager name:** The page names no single fund manager. Its leadership is:
- Matej Říha, Chairman of the Board
- Martin Banský, Vice-Chairman
- Miriama Hanout, Board Member
- Roman Horváth, Investment Manager

**Size:** €55 million reserved for 2020–2026. The fund's lifetime is set at 10 years.

**Ticket range:** "Minimálna výška našej investície je 400tis. EUR, aj keď optimálne investujeme medzi 1,5 – 2,0 mil. EUR." The page also says the fund can go up to "Vieme byť pomerne flexibilní a prispôsobiť výšku investície potrebám vášho projektu až do výšky 7mil. EUR" (about €7 million), including follow-on investments.

**Sectors:** The page does not define a sector focus. Its portfolio spans AI, deep tech, healthcare, logistics, gaming, HR tech, and other areas.

**Stages:** Late-Seed to Series A and B. The page describes this as "Late-Seed až Series A,B."

**Portfolio companies** (investment dates appear only where the page's news items report a specific investment):
1. Nettle AI (investment news: 02.03.2021)
2. SEC Technologies (24.02.2021)
3. Nexineo (07.06.2023)
4. Product Fruits (10.05.2023)
5. AgeVolt (23.06.2021)
6. Sensoneo (24.10.2021)
7. Brightpick (no date)
8. Spaceti (23.05.2022)
9. Powerful Medical (no date)
10. SuperScale (03.07.2023)
11. SCAUT (11.10.2023)
12. Twinzo (13.12.2023)
13. Sentien (no date)
14. Spinbotics (17.04.2024)
15. Vestberry (23.05.2024)
16. Patron GO (14.08.
… [575 more characters]
```
</details>

→ `WebFetch` https://vff.sk/novinky/

<details><summary>result</summary>

```
**Note:** The page doesn't show publication dates, so I can't confirm which items are from 2025-2026. The items appear in the page's listing order, and two are labeled 2022 and 2023 in their titles.

Items listed in page order (investment announcements marked **[Investícia]**):

1. "Ako získať kapitál na svoj ďalší rast? Zistite na webinári s Venture to Future Fund" https://vff.sk/novinky/ako-ziskat-kapital-na-svoj-dalsi-rast-zistite-na-webinari-s-venture-to-future-fund-4
2. **[Investícia]** "Liptovská firma SEC Technologies získala investíciu 3 milióny eur" https://vff.sk/novinky/liptovska-firma-sec-technologies-ziskala-investiciu-3-miliony-eur-5
3. **[Investícia]** "Slovenská technologická firma nettle.ai získala miliónovú investíciu" https://vff.sk/novinky/slovenska-technologicka-firma-nettle-ai-ziskala-milionovu-investiciu-6
4. **[Investícia]** "Slovenský startup AgeVolt so svojím ekosystémom nabíjania elektromobilov získal investíciu 1,2 milióna eur" https://vff.sk/novinky/slovensky-startup-agevolt-so-svojim-ekosystemom-nabijania-elektromobilov-ziskal-investiciu-1-2-miliona-eur-8
5. **[Investícia]** "Na boj s hoaxami a podporu komunikácie medzi mestom a obyvateľmi získal startup Simplicity investíciu 7 miliónov eur" https://vff.sk/novinky/na-boj-s-hoaxami-a-podporu-komunikacie-medzi-mestom-a-obyvatelmi-ziskal-startup-simplicity-investiciu-7-milionov-eur-9
6. **[Investícia]** "Sensoneo získalo investíciu 2 milióny eur z Fondu Európskej rady pre inovácie a Venture to Futur
… [3235 more characters]
```
</details>

→ `WebSearch` "Venture to Future Fund" investícia 2026

→ `WebSearch` "Venture to Future Fund" investoval 2025 startup kolo

<details><summary>result</summary>

```
Web search results for query: ""Venture to Future Fund" investícia 2026"

Links: [{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/investor/461930-23"},{"title":"venture to future fund a s","url":"https://superscout.co/investor/venture-to-future-fund-a-s"},{"title":"Venture to Future Fund increases capital by EUR 15.3 million to support Slovak startups","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"},{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/fund/18944-11F"},{"title":"Venture to Future Fund","url":"https://www.sih.sk/en/stranky/cinnosti/venture-to-future-fund"},{"title":"Updated: April 21, 2026","url":"https://incubatorlist.com/venture-to-future-fund"},{"title":"Future Fund","url":"https://funding.tech.eu/investors/Future%20Fund"},{"title":"Brandfetch's icon's iconVenture to Future Fund's icon","url":"https://brandfetch.com/vff.sk"}]

The search found information on the Slovak fund, though the sources disagree on some details.

- **Basics:** Venture to Future Fund, a.s. is a Slovak venture capital fund established in 2019, focusing on innovative local companies that have the potential to become
… [1145 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Venture to Future Fund" investoval 2025 startup kolo"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/investor/461930-23"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"},{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/fund/18944-11F"},{"title":"venture to future fund a s","url":"https://superscout.co/investor/venture-to-future-fund-a-s"},{"title":"Venture to Future Fund increases capital by EUR 15.3 million to support Slovak startups","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups"},{"title":"Finvolve to Invest INR 300-350 Cr in 2025, Targeting 40-45 High-Impact Startups","url":"https://india.entrepreneur.com/?p=5598"},{"title":"esop for startups: how to structure esop for your startup future funding rounds","url":"https://vestbee.com/insights/articles/esop-for-startups:-how-to-structure-esop-for-your-startup-future-funding-rounds"},{"title":"Finvolve to Invest INR 300-350 Cr in 2025, Targeting 40-45 High-Impact Startups","url":"https://india.entrepreneur.com/news-and-trends/finvolve-to-invest-inr-300
… [1333 more characters]
```
</details>

→ `WebSearch` FaceUp investícia Venture to Future Fund

→ `WebSearch` Talentiqa investícia Purple Ventures VFF

<details><summary>result</summary>

```
Web search results for query: "FaceUp investícia Venture to Future Fund"

Links: [{"title":"jic ventures investuje do faceup cesky startup ziskal pres 110 milionu korun na globalni expanzi","url":"https://forbes.cz/jic-ventures-investuje-do-faceup-cesky-startup-ziskal-pres-110-milionu-korun-na-globalni-expanzi/"},{"title":"První investice nového fondu JIC Ventures míří do technologického startupu FaceUp","url":"https://www.businessinfo.cz/clanky/prvni-investice-noveho-fondu-jic-ventures-miri-do-technologickeho-startupu-faceup/"},{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/investor/461930-23"},{"title":"z brna do dubaja novy fond nalial miliony do startupu ktory vznikol ako studentsky projekt teraz mieri aj na slovensko","url":"https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/"},{"title":"the first investment of the new jic ventures fund goes to technology startup faceup","url":"https://een.gov.cz/en/news/the-first-investment-of-the-new-jic-ventures-fund-goes-to-technology-startup-faceup/"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/4853310.pdf"},{"title":"Venture to Future Fund to Invest in SEC Technologies","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-to-invest-in-sec-technologies"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/future-fund-1/financials"},{"title":"slovakia venture
… [1230 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Talentiqa investícia Purple Ventures VFF"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"Purple Ventures","url":"https://cc.cz/tag/purple-ventures/"},{"title":"ai mozek a psycholog claude nahlednete do investicni kuchyne purple ventures","url":"https://forbes.cz/ai-mozek-a-psycholog-claude-nahlednete-do-investicni-kuchyne-purple-ventures/"},{"title":"podim.org","url":"https://podim.org/?p=32989"},{"title":"purple ventures","url":"https://www.briter.co/companies/purple-ventures"},{"title":"Purple Ventures launches €40M fund for early-stage software startups","url":"https://tech.eu/2024/06/27/purple-ventures-launches-eur40m-fund-for-early-stage-software-startups/"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/purple-ventures"},{"title":"startupovi purple ventures maji jiz 35 externich investoru a 650 milionu na investice","url":"https://cc.cz/live/startupovi-purple-ventures-maji-jiz-35-externich-investoru-a-650-milionu-na-investice/"},{"title":"Purple Ventures","url":"https://venturecapitalarchive.com/venture-funds/purple-ventures-purple-ventures-com"}]

Talentiqa raised about €1M in a round co-led equally by Purple Ventures and Venture to Future Fund (VFF), reported in late September 2025.

- **The round:** EU-Startups reported the round was backed by both investors. Czech startup Talentiqa raises €1M to expand AI-powered recruitment platform across Eur
… [1217 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/

→ `WebSearch` eu-startups Talentiqa raises €1M Purple Ventures Venture to Future Fund

<details><summary>result</summary>

```
- **Publication date:** 19 May 2026, at 16:59.
- **Round size:** The Series A round was worth **5 million dollars** ("v hodnote 5 miliónov dolárov"). The article says FaceUp has raised about 9 million dollars in total.
- **Venture to Future Fund** — investments in FaceUp (19.05.2026), Talentiqa (29.09.2025) and IAG (22.05.2025). State-owned, but invests directly on equal terms with private investors. Its investment period ends in late 2026.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "eu-startups Talentiqa raises €1M Purple Ventures Venture to Future Fund"

Links: [{"title":"CEE VC SUMMIT 2026","url":"https://vestbee.com/blog/articles/talentiqa-raises-1-1-m"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/talentiqa-raises-1-1-m"},{"title":"seed 2025 09","url":"https://seedtable.com/companies/talentiqa/funding-rounds/seed-2025-09"},{"title":"a recruitment automation startup out of Prague","url":"https://funding.tech.eu/companies/1E41EC39-48C9-47F9-A358-22371BC67603"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"TALENTIQA Overview","url":"https://pitchbook.com/profiles/company/482608-54"},{"title":"Subscribe to Our Newsletter","url":"https://www.thesaasnews.com/news/talentiqa-raises-1-million-in-funding/"},{"title":"Prácu si nájdeš rýchlejšie. Slováci a Česi spojili sily, prinášajú efektívnu novinku, na ktorú získali 1 milión eur","url":"https://www.startitup.sk/?p=1128054"},{"title":"www.preqin.com","url":"https://www.preqin.com/data/profile/asset/talentiqa/770569"},{"title":"První kolo pohovorů dělá umělá inteligence v ČEZu i Bageterii Boulevard. Její tvůrci teď získali 25 milionů","url":"https://cc.cz/prvni-kolo-pohovoru-dela-umela-inteligence-v-cezu-i-bageterii-boulevard-jeji-tvurci-ted-ziskali-25-milionu/"}]

The search confirms the round, but sources differ on the amount and some details.

- **Amount:** Vestbee reports €1.1 mill
… [1464 more characters]
```
</details>

→ `WebFetch` https://en.ain.ua/2022/11/30/most-active-slovak-vc-funds

→ `WebFetch` https://www.papermark.com/blog/venture-capital-firms-bratislava

<details><summary>result</summary>

```
**1. Neulogy Ventures**
- **Investments:** 50 total, 3 in H1 2022
- **Managing Partner:** Christian Mandl
- **Fund size:** €20 million
- **Region:** CEE, Slovakia
- **Focus:** Cleantech, B2B SaaS, medtech, and Mixed Reality, mostly deeptech
- **Stages:** Early stage
- **Ticket size:** €500,000 to €3 million
- **Recent investments:** GroupSolver, GA Drilling

**2. Zero Gravity Capital**
- **Investments:** 19 total, 3 in H1 2022
- **Partners:** Dušan Duffek, Marek Zamecnik, and Vít Hanuš
- **Fund size:** €23 million
- **Region:** Slovakia
- **Focus:** Generalist
- **Stages:** Pre-seed and seed
- **Ticket size:** Up to €200,000
- **Recent investments:** jobno.one, Wewell, Patron.GO

**3. 365.fintech**
- **Investments:** 16 total, 3 in H1 2022
- **Managing Director:** Rudolf Vrabel
- **Fund size:** Not stated
- **Region:** Slovakia, Europe
- **Focus:** B2B and B2C fintech, insurtech, and big data startups
- **Stages:** Seed
- **Ticket size:** €50,000 to €500,000
- **Recent investments:** Velaris, Ondato, Montonio

**4. Vision Ventures**
- **Investments:** 19 total, 2 in H1 2022
- **Partners:** Tomáš Bél and Gabriel Horvath
- **Fund size:** €11 million
- **Region:** Slovakia
- **Focus:** Sector-agnostic, targeting Slovak companies that aim to scale internationally
- **Stages:** Pre-seed and seed
- **Ticket size:** €100,000 to €1.6 million (typically up to €800,000, depending on need and development stage)
- **Holding period:** 3 to 8 years
- **Recent investments:** Sloneek, thesho
… [639 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** The article was published January 15, 2025, and last updated February 28, 2026.

**VC firms named (all details given in the article):**

1. **Neulogy Ventures**
   - Description: Early-stage VC backing Slovakia's tech innovators
   - Focus: Deep tech, software, AI
   - Location: Bratislava, Slovakia
   - Program length: Long-term partnership
   - Investment: €0.25M–€2M, seed/Series A
   - Equity-free: No
   - Website: neulogy.vc

2. **Zero Gravity Capital**
   - Description: Seed investor supporting high-growth Central and Eastern European startups
   - Focus: B2B and B2C software, platform tech
   - Location: Bratislava, Slovakia
   - Program length: Long-term partnership
   - Investment: €0.1M–€1M, seed
   - Equity-free: No
   - Website: 0100.vc

3. **Vision Ventures**
   - Description: Pre-seed/seed fund supporting ambitious Slovak founders
   - Focus: SaaS, digital platforms, web apps
   - Location: Bratislava, Slovakia
   - Program length: Long-term partnership
   - Investment: €0.1M–€0.5M initial tickets
   - Equity-free: No
   - Website: visionventures.vc

4. **Venture to Future Fund (VFF)**
   - Description: Growth-stage VC accelerating innovative Slovak scale-ups
   - Focus: Growth capital, industrial tech, digitisation
   - Location: Bratislava, Slovakia
   - Program length: Long-term partnership
   - Investment: €1M–€10M, Series A–C
   - Equity-free: No
   - Website: vff.sk/en

5. **Crowdberry a.s.**
   - Description: Investment platform letti
… [1894 more characters]
```
</details>

→ `WebSearch` slovenské venture kapitálové fondy prehľad 2025 ktoré investujú do startupov

→ `WebSearch` slovenský startup získal investíciu 2026 kolo financovania fond

<details><summary>result</summary>

```
Web search results for query: "slovenské venture kapitálové fondy prehľad 2025 ktoré investujú do startupov"

Links: [{"title":"venture capital recruitment","url":"https://kitalent.com/sk/financial-services-and-professional-services-recruitment/venture-capital-recruitment/"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=6"},{"title":"Private equity a venture kapitálové fondy pôsobiace v SR","url":"https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr"},{"title":"venture capital investment team recruitment","url":"https://kitalent.com/sk/financial-services-and-professional-services-recruitment/venture-capital-recruitment/venture-capital-investment-team-recruitment/"},{"title":"www.podnikajte.sk","url":"https://www.podnikajte.sk/financie?page=36"},{"title":"Popularita private equity a venture kapitálu na Slovensku","url":"https://www.podnikajte.sk/investor/private-equity-venture-kapital-na-slovensku"},{"title":"Tlačová správa","url":"https://www.podnikajte.sk/autori/tlacova-sprava?page=58"},{"title":"Venture kapitál slúži na financovanie perspektívnych, avšak rizikových projektov","url":"https://www.podnikajte.sk/investor/venture-kapital-projekty"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"}]

Hľadanie nenašlo aktuálny prehľad slov
… [1606 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "slovenský startup získal investíciu 2026 kolo financovania fond"

Links: [{"title":"Skoči do osrednje vsebine","url":"https://www.gov.si/novice/2025-12-03-forum-100-startup-slovenski-startup-ekosistem-v-2026-z-okrepljeno-podporo-in-novimi-priloznostmi/"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/silicon-gardens"},{"title":"Venture to Future Fund increases capital by EUR 15.3 million to support Slovak startups","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/slovene-enterprise-fund"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/startup-tipy-rady-financovanie/"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=103787"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"}]

Priama správa o konkrétnom slovenskom startupe, ktorý by v roku 2026 zí
… [1142 more characters]
```
</details>

→ `WebFetch` https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr

→ `WebSearch` startitup.sk investícia fond startup 2026 milióna eur investori

<details><summary>result</summary>

```
Web search results for query: "startitup.sk investícia fond startup 2026 milióna eur investori"

Links: [{"title":"Z Brna do Dubaja: Nový fond nalial milióny do startupu, ktorý vznikol ako študentský projekt. Teraz mieri aj na Slovensko","url":"https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/"},{"title":"Štátny investor vkladá 1,4 milióna eur do startupu z Petržalky. Má zjednodušiť problém, s ktorým bojujú firmy","url":"https://www.startitup.sk/statny-investor-vklada-14-miliona-eur-do-startupu-z-petrzalky-ma-zjednodusit-problem-s-ktorym-bojuju-firmy/"},{"title":"Slovenský startup mieri vďaka podpore investorov do Ameriky","url":"https://www.startitup.sk/slovensky-startup-mieri-vdaka-podpore-investorov-do-ameriky/"},{"title":"Dvaja Slováci z Oxfordu získali 41,7 milióna eur. Ich technológia môže urýchliť liečbu rakoviny","url":"https://www.startitup.sk/dvaja-slovaci-z-oxfordu-ziskali-417-miliona-eur-ich-technologia-moze-urychlit-liecbu-rakoviny/"},{"title":"Na Slovensko prichádza uznávaný startup. Ukáže ti, ako zarobiť na peniazoch, ktoré ti len tak ležia na účte","url":"https://www.startitup.sk/na-slovensko-od-susedov-expanduje-uspesny-startup/"},{"title":"Slovenský startup DAITABLE mieri k hodnote 50 miliónov eur","url":"https://www.startitup.sk/z-11-tisic-eur-k-firme-za-50-milionov-slovaci-vybudovali-biznis-ktory-setri-energiu-aj-nemocniciam/"},{"title":"Na Slovensko prichádza st
… [2546 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** 17 February 2016 (17.2.2016). The information may be outdated.

**Private funds**

| Fund | Manager | Ticket size | Focus | Named investments |
|---|---|---|---|---|
| Enterprise Investors | Enterprise Investors (manages several funds) | 20–50M EUR for minority or majority stakes; 4–10M EUR via Enterprise Venture Fund I | Buyouts and expansion capital in active, profitable firms in Poland and CEE | Kofola, STD Donivo, NAY |
| Credo Ventures | Credo Ventures | 250k–2M EUR for minority stakes | Early-stage IT, internet, mobile tech, healthcare | Excalibur, Photoneo |
| Monogram Ventures | Monogram Ventures | Not stated | Hi-tech products and new digital trends; spin-offs and start-ups | Colosseo, StreamStar, Piano Media, Diagnose.me, Websupport |
| LRJ Capital | LRJ Capital | 100k–2M EUR (optimal 500k) | Firms with global leadership potential that already have first customers | AeroMobil, Challengest |
| Pioneers Ventures | Pioneers Ventures | Up to 125k EUR | Seed-stage projects | Cloudo |
| Benson Oak Capital | Benson Oak Capital | 5–15M EUR | Controlling stakes in Czech and Slovak firms with international growth potential | Zoznam.sk |
| 3TS Capital Partners | 3TS Capital Partners | 300k–10M EUR | Technology firms (including IT and media); expansion capital and SME buyouts | Piano Media, Mall.cz, Globtel (Orange Slovensko) |
| Arca Capital Slovakia | Arca Capital (private equity group using its own funds) | Hundreds of thousands to tens of millions EUR;
… [1854 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/od-cambridge-az-po-bratislavu-vznikol-novy-fond-na-podporu-europskych-talentov-chce-investovat-80-milionov-eur/

→ `WebFetch` https://www.startitup.sk/statny-investor-vklada-14-miliona-eur-do-startupu-z-petrzalky-ma-zjednodusit-problem-s-ktorym-bojuju-firmy/

→ `WebFetch` https://www.startitup.sk/z-11-tisic-eur-k-firme-za-50-milionov-slovaci-vybudovali-biznis-ktory-setri-energiu-aj-nemocniciam/

<details><summary>result</summary>

```
**Publication date:** 4 November 2025, 09:59.

**Fund name:** United Founders.

**Managers:**
- Vít Horký, General Partner, and Jakub Havrlant, who lead the fund as co-founders.
- Václav Pavlečka, known from Czech Founders VC, is one of the managing partners in Bratislava.
- The article also names partners Tony Kypreos, Bettina B. Scheibe, Clark Parsons, and Maxime Paradis.

**Where based:** The article does not name a headquarters. It says the fund has physical presence in Cambridge, Paris, Zürich, Berlin, and Bratislava.

**Size:** The fund aims to invest €80 million. The founders have put in €17 million of their own money.

**Tickets:** The article does not state typical check sizes or amounts for individual deals. It names two early investments, Wonderful.ai and EveryHealth, without amounts. Index Ventures and Bessemer Venture Partners also invested in Wonderful.ai.

**Quotes:**
- Horký: "Talent v Európe je. To, čo chýba, je kapitál a systémová podpora v skorých fázach,"
- Horký: "Chceme, aby Európa mala svojich vlastných technologických gigantov."
```
</details>

<details><summary>result</summary>

```
- **Publication date:** 22 September 2026, 15:39. The article gives it as "22. septembra 2026 o 15:39."
- **Investor:** Slovak Investment Holding (SIH), a state investor. The article's press release describes it as the investor behind most of the round.
- **Startup:** VisionFlow, s. r. o., based in Petržalka, Bratislava.
- **Amount:** SIH's share is €1.4 million, or 70% of the €2 million total round. The article says: "Väčšinu sumy poskytne Slovak Investment Holding (SIH)."
- **Instrument:** A convertible loan maturing in December 2028, funded from Slovakia's Recovery and Resilience Plan (Component 9). It can convert into an ownership stake under agreed conditions, so SIH does not yet hold a specific percentage. The article does not disclose the interest rate, conversion terms, or valuation.
- **Co-investors:** One private Slovak co-investor from the IT sector, not named in the article, providing the remaining €600,000. The article says: "Na financovaní sa podieľa aj súkromný slovenský spoluinvestor z IT sektora, ktorého meno správa neuvádza."
```
</details>

<details><summary>result</summary>

```
- **Publication date:** 10 July 2026, at 15:39. The article reads "10\. júla 2026 o 15:39".
- **Investors:** The article does not name any investor, so I can't give exact names. It says that after the announcement, other investors contacted the company, and the round could grow to 2–3 million euros. It also mentions an unnamed investor who steered the company toward Central Europe: "ktorý nás nasmeroval najprv na región strednej Európy."
- **Amount:** One million euros. The article says: "Investíciu vo výške milión eur oznámila v magazíne Forbes."
```
</details>

→ `WebFetch` https://www.neulogy.vc/

→ `WebSearch` Neulogy Ventures investícia 2026

<details><summary>result</summary>

```
Web search results for query: "Neulogy Ventures investícia 2026"

Links: [{"title":"Neulogy Ventures","url":"https://privateequitylist.com/investors/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/public/investor/neulogy-ventures"},{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"neulogy ventures","url":"https://privateequitylist.com/investor/neulogy-ventures"},{"title":"Neulogy Ventures a ich úvodný event ako sa patrí","url":"https://www.startitup.sk/neulogy-ventures-a-ich-uvodny-event-ako-sa-patri/"},{"title":"Neulogy Ventures","url":"https://www.seedtable.com/investors/neulogy-ventures"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/neulogy"},{"title":"Neulogy Ventures","url":"https://www.roundfunded.com/en/vc/neulogy-ventures"}]

I found no 2026 investment by Neulogy Ventures in these results. The most recent dated deals I found are from 2025 or earlier.

- **Latest deals:** Caplight lists a March 2025 growth-equity investment in GreenWay (as co-investor) and a September 2024 pre-seed lead in StratifAI GmbH. Caplight's list also includes GA Drilling (April 2024, Series C) and BiteBerry (August 2023, seed). WaveUp gives a different picture, reporting a last investment date of September 2024.
- **Profile:** Neulogy Ventures, established in 2014 and
… [648 more characters]
```
</details>

<details><summary>result</summary>

```
**Not on the page:** legal entity names, fund names, fund sizes, fund vintage, and ticket sizes. The page doesn't state an exact ticket-size sentence.

**Headline figures:** 101 founders, €135 million in sales, and 10 countries.

**Sectors:** Medtech, B2B SaaS, Marketplace, Cybersecurity, Cleantech, and Infrastructure. The page describes its focus as deeptech and "moonshot" ideas in technology, climate, and health.

**Stages:** Not specified. A testimonial says Neulogy backed one company when it had almost no customers, and another when its idea was still early.

**Geography:** Central and Eastern Europe (CEE), and the 10 countries noted above. The page highlights CEE engineering talent.

**Portfolio companies (listed on the page):**
- Anvesana (Medtech): RNAseq analysis for rare genetic disorders
- BeIT (B2B SaaS, Cleantech): financial and operational management for properties
- BiteBerry (B2B SaaS): AI voice ordering for restaurants
- Diagnose.me (Marketplace, Medtech): online medical diagnosis
- Eyerim (Marketplace): online eyewear retailer in CEE
- Excalibur (Cybersecurity): security-as-a-service
- GA Drilling (Cleantech): ultra-deep geothermal technology
- GreenWay (Cleantech, Infrastructure): e-vehicle charging in CEE

**Other companies named in testimonials or news:** Matsuko, Voltia, Luigi's Box, GroupSolver, and Trustmatic.

**News items (dates from the page's social feed):**
- **May 24, 2024:** Retweet promoting the Startup Money investor and startup conference in B
… [876 more characters]
```
</details>

→ `WebSearch` "Slovak Venture Fund" Neulogy SICAR

→ `WebFetch` https://www.neulogy.vc/news/

<details><summary>result</summary>

```
Web search results for query: ""Slovak Venture Fund" Neulogy SICAR"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"rpvs.gov.sk","url":"https://rpvs.gov.sk/rpvs/Partner/Partner/Dokument/198896"},{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"slovakia equity fundmanagers","url":"https://lb.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"neulogy ventures","url":"https://privateequitylist.com/investor/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia"},{"title":"slovakia equity fundmanagers","url":"https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf"},{"title":"HQ - Bratislava","url":"https://app.mergerlinks.com/companies/neulogy-ventures"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/slovca/financials"}]

The search turned up a few sources linking the two names, though none describes the Slovak Venture Fund's relationship to Neulogy in detail.

- **EIF listing:** An EIF table of Slovak equity fund partners pairs "Slovak Venture Fund S.C.A., SICAR" with Neulogy Ventures a.s. as its manager, with a Slovakia venture capital focus. The table lists the fund name, fund manager, team location, and mandate, and
… [1398 more characters]
```
</details>

<details><summary>result</summary>

```
Here are the 12 news items visible on the page. The posts are retweets and tweets, so the titles are my summaries. The page also has a "Load more" button, so older items exist.

**New investment**
- **Oct 24, 2023 – Trustmatic joins Neulogy Ventures:** "Investment Alert! We are proud to announce @trustmaticHQ as the latest addition to the Neulogy Ventures family."
  https://twitter.com/NeulogyVC/status/1716848291755827304
- **Nov 10, 2023 – Trustmatic acquired by Certn:** Trustmatic "has been acquired by @certn, a global leader in background screening." Neulogy and Bob Lesko are thanked for their support.
  https://twitter.com/NeulogyVC/status/1723081264545006060

**Other news**
- **May 24, 2024 – Startup Money conference in Brno:** JIC promotes the investor and startup conference, noting that tickets are almost sold out.
  https://twitter.com/NeulogyVC/status/1793931946931962147
- **Feb 8, 2024 – Vectary and Figma integration:** Vectary announces 3D viewers embeddable in FigJam.
  https://twitter.com/NeulogyVC/status/1755665902899466278
- **Feb 8, 2024 – Luigi's Box on combining international teams:** CEO Gejza Nagy discusses the topic on the Profi HR Talks video podcast.
  https://twitter.com/NeulogyVC/status/1755665864118964522
- **Feb 7, 2024 – Luigi's Box on the Persoo acquisition:** A video from a Prague event covers the Persoo acquisition and product news.
  https://twitter.com/NeulogyVC/status/1755369055014240728
- **Feb 7, 2024 – Robert Scoble on holographic meetings
… [1256 more characters]
```
</details>

→ `WebSearch` Neulogy GreenWay investícia 2025

→ `WebSearch` StratifAI pre-seed Neulogy Ventures

→ `WebSearch` BiteBerry investícia Neulogy Venture to Future Fund

<details><summary>result</summary>

```
Web search results for query: "BiteBerry investícia Neulogy Venture to Future Fund"

Links: [{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/investor/461930-23"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/neulogy"},{"title":"neulogy ventures","url":"https://startups.one.gob.es/companies/neulogy_ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/public/investor/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/investors/neulogy-ventures"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/neulogy-ventures"}]

The search didn't find a single source that describes a BiteBerry round involving both firms, so the link comes from two separate databases.

- **Venture to Future Fund** — investments in FaceUp (19.05.2026), Talentiqa (29.09.2025) and IAG (22.05.2025). State-owned, but invests directly on equal terms with private investors. Its investment period ends in late 2026.
- **Neulogy Ventures** — Bratislava management company (IČO 47 367 610), SLOVCA member, included in the EIF list. I found no new investments after September 2024.
… [565 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "StratifAI pre-seed Neulogy Ventures"

Links: [{"title":"Christian Mandl","url":"https://sk.linkedin.com/in/christianmandl"},{"title":"cekan pavol multiplexdx 202409 inc persons people chief 2001 28559","url":"https://www.life-sciences-europe.com/person/cekan-pavol-multiplexdx-202409-inc-persons-people-chief-2001-28559.html"},{"title":"app.foundernest.com","url":"https://app.foundernest.com/public/space/7678/companies/10190350?page=11"},{"title":"Recently FundedEUR 1.5MTechnology, Information and Internet","url":"https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers"},{"title":"Funding Stage","url":"https://seedtable.com/companies/stratifai"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/stratifai-secures-12-5m-funding-round"},{"title":"Back to Stories","url":"https://aiworld.eu/story/stratifai-raises-125m-to-make-cancer-treatment-more-precise-with-ai"},{"title":"Major Investements for","url":"https://digitalhealth.tu-dresden.de/?p=13630"},{"title":"rocketlist.ai","url":"https://rocketlist.ai/companies/stratifai"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/stratifai"}]

StratifAI's pre-seed round was a €1.5M raise, co-led by Neulogy Ventures and MultiplexDX. The announcement is dated September 2, 2024, and Debiopharm Innovation Fund, Arve Capital, and angel investor Christoph Haarburger also participate
… [1184 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Neulogy GreenWay investícia 2025"

Links: [{"title":"Investícia vo výške 85 miliónov EUR do rastu siete pre priekopníka GreenWay","url":"https://touchit.sk/investicia-vo-vyske-85-milionov-eur-do-rastu-siete-a-dalsiu-expanziu-pre-priekopnika-e-mobility-spolocnost-greenway/401298/"},{"title":"Mirova inyecta 50 millones de euros en el especialista en recarga GreenWay","url":"https://www.electrive.com/es/2025/03/17/mirova-inyecta-50-millones-de-euros-en-greenway-especialista-en-tarificacion/"},{"title":"Mirova inyecta 50 millones de euros en el especialista en recarga GreenWay","url":"https://www.electrive.com/es/2025/03/17/mirova-injects-e50-million-in-charging-specialist-greenway/"},{"title":"top of page","url":"https://www.symsite.sk/single-post/french-fund-mirova-is-investing-50m-in-greenway"},{"title":"GreenWay erhält 85 Millionen Euro von Investoren","url":"https://www.electrive.net/2022/02/23/greenway-erhaelt-85-millionen-euro-von-investoren/"},{"title":"operator stacji ladowania pozyskal inwestora","url":"https://www.gramwzielone.pl/auto-ekologiczne/20307254/operator-stacji-ladowania-pozyskal-inwestora"},{"title":"www.gramwzielone.pl","url":"https://www.gramwzielone.pl/?p=20307254"},{"title":"en.lider.media","url":"https://en.lider.media/?p=24673"},{"title":"GreenWay recauda 85 millones de euros de sus inversores","url":"https://www.electrive.com/es/2022/02/23/greenway-collects-e85-million-from-investors/"},{"title":"GreenWay recauda 85 mill
… [2951 more characters]
```
</details>

→ `WebFetch` https://finstat.sk/databaza-firiem-organizacii?query=neulogy

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `Bash` — Query ORSR business register for Neulogy
```sh
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36" "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=neulogy&PF=0&R=on" | iconv -f windows-1250 -t utf-8 | sed 's/<[^>]*>/ /g' | tr -s ' \n' | head -c 3000
```

<details><summary>result</summary>

```
 Obchodný register SR - Výsledky vyhľadávania podľa obchodného mena subjektu










 MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY

 OBCHODNÝ REGISTER NA INTERNETE



    Slovensky |
 -->

     English


















Výsledky vyhľadávania podľa obchodného mena subjektu
( vyhľadávanie len v aktuálnych záznamoch )





 Obchodné meno začína:&nbsp; neulogy
 Právna forma:&nbsp; akákoľvek
 Súd:&nbsp; akýkoľvek



 Stránka:&nbsp; 1&nbsp;/&nbsp;1
 Záznamy:&nbsp; 1&nbsp;-&nbsp;1&nbsp;/&nbsp;1
 Dátum:&nbsp; 11.10.2026







 &nbsp;
 Obchodné meno subjektu
 Výpis
 Zbierka dokumentov



 1.



                         Neulogy Ventures, a. s.


 Aktuálny &nbsp;
         Úplný &nbsp;


         &nbsp;







 Aktuálne zmeny |
 Elektronické služby Obchodného registra |
 Vyhľadávanie podnikov v EÚ Vyhľadávanie podľa :
 obchodného mena |
 identifikačného čísla
 sídla |
 spisovej značky |
 priezviska a mena osoby
 O obchodnom registri SR |
 Návod na používanie ORI |
 Kontakty na registrové súdy
 Aktuality a oznamy



 var _paq = window._paq = window._paq || [];
 /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
 _paq.push(['trackPageView']);
 _paq.push(['enableLinkTracking']);
 (function() {
 var u="https://obcan.justice.sk/pilot/analytics/";
 _paq.push(['setTra
… [223 more characters]
```
</details>

→ `Bash` — Create ORSR register helper script and test search
```sh
mkdir -p [tmp] && cat > [tmp] <<'EOF'
#!/usr/bin/env python3
# usage: orsr.py search "name"   -> list of matches with vypis links
#        orsr.py vypis "<relative or abs url>" [full]  -> text of extract
import sys, re, urllib.request, urllib.parse, html
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
BASE = "https://www.orsr.sk/"
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    raw = urllib.request.urlopen(req, timeout=40).read()
    return raw.decode("windows-1250", errors="replace")
def text(h):
    h = re.sub(r"(?is)<script.*?</script>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</tr>|</p>|</div>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    lines = [re.sub(r"[ \t\xa0]+", " ", l).strip() for l in h.split("\n")]
    return "\n".join(l for l in lines if l)
cmd = sys.argv[1]
if cmd == "search":
    q = urllib.parse.quote(sys.argv[2].encode("windows-1250"))
    h = get(BASE + f"h
… [966 more characters]
```

<details><summary>result</summary>

```
NO MATCH
```
</details>

→ `Bash` — Inspect ORSR search HTML for link format
```sh
curl -s -A "Mozilla/5.0" "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=neulogy&PF=0&R=on" | iconv -f windows-1250 -t utf-8 | grep -n -i -A3 -B3 "vypis" | head -40
```

<details><summary>result</summary>

```
80-
81-                        <td><div class="bmk">
82-
83:						<a href="vypis.asp?ID=276162&amp;SID=2&amp;P=0" class = "link" alt="Aktuálny výpis" title="Aktuálny výpis">Neulogy Ventures, a. s.</a></div></td>
84-                        <td><div class="bmk">
85-
86:                        <a href="vypis.asp?ID=276162&amp;SID=2&amp;P=0" class="link">Aktuálny</a>&nbsp;
87:	            	<a href="vypis.asp?ID=276162&amp;SID=2&amp;P=1" class="link">Úplný</a>&nbsp;
88-                        </div></td>
89-			<td><div class="bmk">
90-	        	<a href="zbl.asp?ID=276162&amp;SID=2" class="link"><img border="0" src="images/view.gif" alt="Zbierka listín">&nbsp;</a>
```
</details>

→ `Bash` — Fix ORSR regex and fetch Neulogy extract
```sh
cd [tmp] && python3 - <<'EOF'
import re
p='orsr.py'
s=open(p).read()
s=s.replace('''rows = re.findall(r'(?is)<div class="sbj">\\s*(.*?)\\s*</div>.*?href="(vypis\\.asp\\?ID=\\d+&SID=\\d+&P=0)"', h)''','''rows = re.findall(r'(?is)<a href="(vypis\\.asp\\?ID=\\d+&amp;SID=\\d+&amp;P=0)" class = "link"[^>]*>(.*?)</a>', h); rows=[(n,l.replace("&amp;","&")) for l,n in rows]''')
open(p,'w').write(s)
EOF
grep -n "rows =" orsr.py; python3 orsr.py search "neulogy"; python3 orsr.py vypis "https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0"
```

<details><summary>result</summary>

```
22:    rows = re.findall(r'(?is)<a href="(vypis\.asp\?ID=\d+&amp;SID=\d+&amp;P=0)" class = "link"[^>]*>(.*?)</a>', h); rows=[(n,l.replace("&amp;","&")) for l,n in rows]
28:    rows = re.findall(r'(?is)<a href="(vypis\.asp\?ID=\d+&amp;SID=\d+&amp;P=0)" class = "link"[^>]*>(.*?)</a>', h); rows=[(n,l.replace("&amp;","&")) for l,n in rows]
Neulogy Ventures, a. s. | https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0
https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0
Výpis z obchodného registra SR
MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY
OBCHODNÝ REGISTER
NA INTERNETE
Slovensky |
-->
English
Výpis z Obchodného registra Mestského súdu Bratislava III
Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony!
Zobraziť na novej verzii portálu
Oddiel: Sa
Vložka číslo: 5826/B
Obchodné meno:
Neulogy Ventures, a. s.
(od: 24.08.2013)
Sídlo:
Tallerova 4
Bratislava - mestská časť Staré Mesto 811 02
(od: 16.07.2016)
IČO:
47 367 610
(od: 24.08.2013)
Deň zápisu:
24.08.2013
(od: 24.08.2013)
Právna forma:
Akciová spoločnosť
(od: 24.08.2013)
Predmet podnikania (činnosti):
Činnosť podnikateľských, organizačných a ekonomických poradcov
(od: 24.08.2013)
Administratívne služby
(od: 24.08.2013)
Sprostredkovateľská činnosť v oblasti obchodu
(od: 24.08.2013)
Sprostredkovateľská činnosť v oblasti služieb
(od: 24.08.2013)
Kúpa tovaru na účely jeho predaja konečnému spotrebiteľovi (maloobchod) alebo iným prevádzkovateľom živnosti (veľkoobchod)
(od: 24.08.2013)
Prieskum trhu a verej
… [2168 more characters]
```
</details>

→ `Bash` — Add brief extract command and check BiteBerry shareholders
```sh
cd [tmp] && cat >> orsr.py <<'EOF'
if cmd == "brief":
    # brief "name" [full] : search, then for each match print name, ICO, seat, spolocnici section
    q = urllib.parse.quote(sys.argv[2].encode("windows-1250"))
    h = get(BASE + f"hladaj_subjekt.asp?OBMENO={q}&PF=0&R=on")
    rows = re.findall(r'(?is)<a href="(vypis\.asp\?ID=\d+&amp;SID=\d+&amp;P=0)" class = "link"[^>]*>(.*?)</a>', h)
    for link, name in rows[:6]:
        url = BASE + link.replace("&amp;","&")
        if len(sys.argv) > 3: url = url.replace("P=0","P=1")
        t = text(get(url))
        ico = re.search(r"IČO:\n(.*?)\n", t)
        seat = re.search(r"Sídlo:\n(.*?)\n(.*?)\n", t)
        zap = re.search(r"Deň zápisu:\n(.*?)\n", t)
        print("==", html.unescape(name).strip(), "|", url)
        print("IČO:", ico.group(1) if ico else None, "| Sídlo:", (seat.group(1)+", "+seat.group(2)) if seat else None, "| zápis:", zap.group(1) if zap else None)
        m = re.search(r"(Spoločníci:|Akcionár:)\n(.*?)(Výška vkladu|Výška základného imania|Štatutárny orgán|Dátum aktualizácie)", t, re.S)
        if m: print(m.group(1), m.group(2)[:
… [257 more characters]
```

<details><summary>result</summary>

```
== BiteBerry s. r. o. | https://www.orsr.sk/vypis.asp?ID=694090&SID=5&P=0
IČO: 55 353 690 | Sídlo: Na Bráne 4, Žilina 010 01 | zápis: 22.04.2023
Spoločníci: Core Capital s. r. o. IČO: 55 496 865 / Tematínska 3231/2 / Bratislava - mestská časť Petržalka 851 05 / (od: 08.07.2023) / Vision Ventures Growth I, s. r. o. IČO: 52 656 438 / Bottova 2A / Bratislava - mestská časť Staré Mesto 811 09 / (od: 09.08.2023) / AI Group s.r.o. IČO: 55 614 710 / Bytčická 1139/89 / Žilina 010 09 / (od: 09.08.2023) /
Vklady: Core Capital s. r. o. / Vklad: 14 520 EUR ( peňažný vklad ) Splatené: 14 520 EUR / (od: 08.07.2023) / Vision Ventures Growth I, s. r. o. / Vklad: 2 254 EUR ( peňažný vklad ) Splatené: 2 254 EUR / (od: 09.08.2023) / AI Group s.r.o. / Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR / (od: 09.08.2023) /
```
</details>

→ `Bash` — Search ORSR for several candidate investor names
```sh
cd [tmp] && for n in "Vision Ventures" "Zero Gravity" "Limerock" "Crowdberry" "Sandberg" "Venture to Future" "Slovak Asset Management" "Fond inovácií" "Investeers" "Eterus"; do echo "##### $n"; python3 orsr.py search "$n"; done
```

<details><summary>result</summary>

```
Command did not complete within its 120s timeout and was moved to the background (ID: btjcmddzz). Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [redacted: private assistant config] directory changes made by the backgrounded command do not apply to subsequent commands.
```
</details>

→ `WebFetch` https://visionventures.vc/

→ `WebSearch` Vision Ventures investícia 2026 startup Tomáš Bél fond

<details><summary>result</summary>

```
Web search results for query: "Vision Ventures investícia 2026 startup Tomáš Bél fond"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/vision-ventures"},{"title":"-핀테크 스타트업 5개사 참여…기술력·사업모델 집중 검토","url":"https://www.venturesquare.net/?p=1076715"},{"title":"-핀테크 스타트업 5개사 참여…기술력·사업모델 집중 검토","url":"https://www.venturesquare.net/1076715/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/vision-ventures-1"},{"title":"Vision Ventures Research","url":"https://f4.fund/firms/vision-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/vision-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/visionventures-vc"},{"title":"Vision Ventures","url":"https://privateequitylist.com/investors/vision-ventures"},{"title":"Saudi Arabia’s Vision Ventures Is Envisioning the Future of MENA Startups With Its Investment Approach","url":"https://mena.entrepreneur.com/growth-strategies/saudi-arabias-vision-ventures-is-envisioning-the-future-of/448574"}]

I found no results mentioning Tomáš Bél, so I can't confirm whether he is connected to any Vision Ventures investment. The results also describe at least two different firms with the same name.

- **Saudi firm (Dammam):** Caplight lists the Saudi-based firm as having made 76 investments, with its latest in Deep.SA as
… [1346 more characters]
```
</details>

<details><summary>result</summary>

```
**Legal entities:** Not stated on the page.

**Fund names, sizes, and vintage:** The page names no fund and gives no fund size. It describes a 2023 investment window, with final fund closure by end of 2029.

**Ticket sizes:**
"We usually make investments between €100 thousand and €800 thousand, maximum up to €1,6 million."
The page also says total investment can reach €1.6 million.

**Sectors:** Generalist. The firm is open to various sectors and prioritizes strong growth potential and a team able to deliver.

**Stages:** Pre-seed and seed.

**Geography:** Slovakia. Target companies must operate there and must have been registered with the Business Register for no more than five years at the time of investment.

**Investment horizon:** Holding periods of roughly 3 to 8 years.

**Portfolio companies:** The page states 26 portfolio companies. Named companies include:
- Cequence
- Seerlinq
- Airvolute
- TramaTM
- BiteBerry
- CloseRocket
- Sloneek
- Spinbotics

Logo files also reference Vestberry, Culture Board, Zooza, moneyhoon, Verdikto, EventsFrame, theshop, stylers.cloud, Mobilyze, nativero, mediaPlatform, eatster, instyleai, LayerYesElf, SafeStuffLogo, NextRetreat, flowy, and elysiumspa. These are inferred from image filenames, so the list is unconfirmed.

No investment dates are given for any company.

**News with dates:** None. The page has no news section. The only dated item is an SFDR sustainability policy PDF stored under a 2026/03 upload path, which is a document, not
… [6 more characters]
```
</details>

→ `WebSearch` "Vision Ventures" Seerlinq OR Airvolute OR Cequence OR CloseRocket investícia

→ `Read` [tmp]

<details><summary>result</summary>

```
1	##### Vision Ventures
2	Vision Ventures Growth I, s. r. o. | https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0
3	Vision Ventures, s.r.o. | https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0
4	##### Zero Gravity
5	Zero Gravity Capital s.r.o. | https://www.orsr.sk/vypis.asp?ID=498371&SID=2&P=0
6	##### Limerock
7	Limerock Advisory, s. r. o. | https://www.orsr.sk/vypis.asp?ID=202952&SID=2&P=0
8	Limerock Investment Holding, s.r.o. | https://www.orsr.sk/vypis.asp?ID=307952&SID=2&P=0
9	##### Crowdberry
10	Traceback (most recent call last):
11	  File "[tmp]", line 21, in <module>
12	    h = get(BASE + f"hladaj_subjekt.asp?OBMENO={q}&PF=0&R=on")
13	  File "[tmp]", line 9, in get
14	    raw = urllib.request.urlopen(req, timeout=40).read()
15	          ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
16	  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/urllib/request.py", line 187, in urlopen
17	    return opener.open(url, data, timeout)
18	           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
19	  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/urllib/request.py", line 487, in open
20	    response = self._open(req, data)
21	  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/p
… [6219 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Vision Ventures" Seerlinq OR Airvolute OR Cequence OR CloseRocket investícia"

Links: [{"title":"vision ventures","url":"https://www.vcbacked.co/directory/investors/vision-ventures"},{"title":"Vision Ventures (Slovakia) Overview","url":"https://pitchbook.com/profiles/investor/436353-58"},{"title":"funding.tech.eu","url":"https://funding.tech.eu/investors/Vision%20Invest"},{"title":"CloseRocket logo — company profile","url":"https://bouncewatch.com/company/closerocket"},{"title":"Back to Vision Ventures","url":"https://seedtable.com/investors/vision-ventures/portfolio"},{"title":"VISION VENTURES","url":"https://app.mergerlinks.com/companies/envision-ventures"},{"title":"Vision Ventures","url":"https://www.seedtable.com/investors/vision-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/visionventures-vc"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/vision-ventures"},{"title":"vision ventures","url":"https://allbusiness.africa/investors/vision-ventures"}]

The search points to the Bratislava-based Vision Ventures, which backed three of the four companies. I found nothing on Airvolute.

- **CloseRocket:** A seed round of €1.00M on 28 January 2024. The investment was led by Jinej fond, Vision Ventures, Andrej Kiska, Michal Simkovic, and Peter Komornik. PitchBook lists the same deal date (3
… [1280 more characters]
```
</details>

→ `Bash` — Add retry logic and prepare ORSR batch script
```sh
cd [tmp] && python3 - <<'EOF'
p='orsr.py'
s=open(p).read()
s=s.replace('''def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    raw = urllib.request.urlopen(req, timeout=40).read()
    return raw.decode("windows-1250", errors="replace")''','''def get(url):
    import time
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            raw = urllib.request.urlopen(req, timeout=60).read()
            return raw.decode("windows-1250", errors="replace")
        except Exception as e:
            err = e; time.sleep(3)
    print("FETCH FAILED", url, err); return ""''')
open(p,'w').write(s)
EOF
cat > batch1.sh <<'EOF'
cd "$(dirname "$0")"
for n in "Vision Ventures" "Zero Gravity Capital" "Limerock" "Crowdberry" "Sandberg Capital" "Venture to Future Fund" "Slovak Investment Holding" "Fond inovácií a technológií" "Eterus" "Národný holdingový fond" "Prvá kapitálová" "Nation1" "Gapfunding" "365.fintech" "ZAKA" "Across Private" "Monogram" "LRJ" "Pioneers Ventures" "Arca Capital Slovakia" "QUADRICA" "J&T Ventures" "Slovenský
… [194 more characters]
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Run ORSR batch lookup for candidate managers
```sh
[tmp] > [tmp] 2>&1
```

<details><summary>result</summary>

```
Command running in background with ID: bu2f3enkg. Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
```
</details>

**Agent:**

Meanwhile, Zero Gravity and Limerock research.

→ `WebFetch` https://www.zerogravity.vc/

→ `WebSearch` Zero Gravity Capital investícia startup 2025 2026 Duffek

<details><summary>result</summary>

```
The page content you provided doesn't include any of the requested information. It contains only:

- The domain name: zerogravity.vc
- A page title: "zerogravity Resources and Information."
- A loading image from img.sedoparking.com

The Sedo parking reference suggests the domain may be parked, meaning it's a placeholder rather than an active site with fund details. Based on this content alone, I can't identify:

- Legal entities
- Fund names, sizes, or vintages
- Ticket sizes
- Sectors, stages, or geography
- Portfolio companies or dates
- News or dates

To get this information, you could check the live site directly, or look at the firm's SEC Form ADV filings or Form D filings, which list fund details for U.S. advisers. If you can provide a page with the actual content, I can summarize it.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Zero Gravity Capital investícia startup 2025 2026 Duffek"

Links: [{"title":"60-miliónový balík pre startupy je Slovákom blízko ako nikdy doposiaľ. Prestížna podpora už čaká","url":"https://www.startitup.sk/?p=742627"},{"title":"Podpořili největší startupové naděje na Slovensku. S novým fondem mají i pro české firmy 1,5 miliardy","url":"https://cc.cz/podporili-nejvetsi-startupove-nadeje-na-slovensku-s-novym-fondem-maji-i-pro-ceske-firmy-15-miliardy/"},{"title":"Subscribe to Our Newsletter","url":"https://techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups"},{"title":"Zero Gravity Capital a Campus Cowork spájajú sily aby priniesli do ekosystému nové projekty a talent","url":"https://www.startitup.sk/?p=384747"},{"title":"Zero Gravity Capital a Campus Cowork spájajú sily aby priniesli do ekosystému nové projekty a talent","url":"https://www.startitup.sk/zero-gravity-capital-a-campus-cowork-spajaju-sily-aby-priniesli-do-ekosystemu-nove-projekty-a-talent/"},{"title":"Zero One Hundred","url":"https://startupim.com/investor/zero-one-hundred"},{"title":"Zero Gravity Capital","url":"https://cc.cz/tag/zero-gravity-capital/"},{"title":"Zero Gravity Capital","url":"https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia"},{"title":"Zero One Hundred","url":"https://slimpages.startupim.com/neo_company_page/zero-one-hundred"},{"title":"Zero Gravity Capital Overview","url":"https://slimpages.
… [1581 more characters]
```
</details>

→ `WebFetch` https://cc.cz/podporili-nejvetsi-startupove-nadeje-na-slovensku-s-novym-fondem-maji-i-pro-ceske-firmy-15-miliardy/

→ `WebFetch` https://0100.vc/

<details><summary>result</summary>

```
**Zero One Hundred: key facts**

- **Publication date:** 20 December 2022 (article dated 20. 12. 2022).
- **Fund name:** Zero One Hundred. The article describes a second, larger fund. The earlier vehicle was Zero Gravity Capital.
- **Legal vehicle:** Not stated for the new fund. Zero Gravity Capital is described as a "samostatný fond" (separate fund).
- **Size:** The article gives a planned investment figure, not a fund close. It says the firm wants to invest "60 milionů eur" (€60 million) in young companies in the coming years, which is "téměř 1,5 miliardy korun" (almost CZK 1.5 billion) at current rates.
- **Tickets:** Not stated.
- **Team:** Three partners lead the fund: Dušan Duffek, Vít Hanuš, and Michal Csonga. Marek Zámečník, Michal Paško, and Martin Hauge were original co-founders. Zámečník now focuses on Vestberry, and the others are pursuing their own investing and remain partners and advisers.
- **Where based:** Bratislava, Prague, and Cyprus. Duffek mostly lives in Cyprus.
- **Geography:** Central and Eastern Europe, with a primary focus on Slovakia and Czechia. The network also covers the Baltics, the Balkans, Greece, and Cyprus.
- **LPs (incl. EIF):** Not mentioned.
- **Stage focus:** Pre-seed through Series A, with an emphasis on rapid, global growth. Part of the capital will go into VC funds operating in the region.
- **First investments:** These were made by the earlier Zero Gravity Capital fund (€23 million, about CZK 560 million), mainly in Slovak startups:
… [162 more characters]
```
</details>

<details><summary>result</summary>

```
## Zero One Hundred (0100 VC): Fact Sheet from Page Content

**Legal entity:** 0100 VC RAIF F.C.I.C. PLC., registered office at 5 Esperidon Street, 2001 Strovolos, Nicosia, Cyprus. The page says the fund is addressed only to Well-Informed and/or Professional Investors.

**Fund:** The page mentions "Fund II" and says the firm is continuing its journey with it. It gives no fund size or vintage.

**Ticket sizes:** Not stated.

**Sectors:** Not stated as a formal list. Portfolio descriptions cover healthcare/AI, fintech, proptech, HR/payroll, mobility, e-commerce, edtech, media, and AR/VR.

**Stages:** Not stated. The page describes backing "the best startups" from Emerging Europe and the Middle East.

**Geography:** Emerging Europe and the Middle East.

**Offices:** Czechia, Slovakia, Cyprus, and the UAE.

**Track record (page stats, labeled "past 10 years" in one heading and "past 12 years" in another):**
- Started 10 companies
- Invested in 34 companies
- Exited 4 companies
- Organized 70+ international conferences
- Welcomed 20,000 entrepreneurs and 10,000 investors to events
- Hosted 4,000 technical talents and operators at community events

**Team:**
- Adam Durica, General Partner (investment process and portfolio management)
- Dusan Duffek, Managing Partner (leads international expansion)
- Michal Csonga, General Partner (fund strategy)
- Marek Zamecnik, Technical Partner
- Paul Jozefak, Executive in Residence
- Olivia Strapekova, Head of Events
- Kristina Moncekova, Portf
… [1628 more characters]
```
</details>

→ `WebSearch` "Zero One Hundred" OR "0100 Ventures" investment 2025 2026 startup round

→ `WebFetch` https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia

<details><summary>result</summary>

```
Web search results for query: ""Zero One Hundred" OR "0100 Ventures" investment 2025 2026 startup round"

Links: [{"title":"Back to 2100 Ventures","url":"https://seedtable.com/investors/2100-ventures/portfolio"},{"title":"largest startup venture capital vc funding deals","url":"https://intellizence.com/insights/startup-funding/largest-startup-venture-capital-vc-funding-deals/"},{"title":"Artificial intelligence Defense tech IPO M&A Robotics Semiconductors and 5G Startups Transportation & Logistics Venture","url":"https://news.crunchbase.com/?p=93307"},{"title":"Artificial intelligence Defense tech IPO M&A Robotics Semiconductors and 5G Startups Transportation & Logistics Venture","url":"https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/"},{"title":"news.crunchbase.com","url":"https://news.crunchbase.com/sections/startups/page/10/"},{"title":"100 Top Pre-Seed Venture Capital Firms 2026","url":"https://eqvista.com/top-pre-seed-funding-venture-capital-firms/"},{"title":"Venture Funding Surges Across AI, Fintech and Crypto in 2026","url":"https://for.you.com/topics/capital-raises"},{"title":"100 Ventures investment portfolio","url":"https://tour.pitchbook.com/answers/100-ventures-investment-portfolio"},{"title":"largest us venture capital deals","url":"https://www.statista.com/statistics/1303299/largest-us-venture-capital-deals"},{"title":"neuronfeed.com","url":"https://neuronfeed.com/funding?page=7"}]

I didn't find any 2025 or 2026 funding round tied
… [826 more characters]
```
</details>

<details><summary>result</summary>

```
The page doesn't include all the requested details:

- **Amounts:** Not stated.
- **Dates:** The fund began activities in 2020, with an expected 10-year fixed term. Its investment window closed in December 2023, and it is now in its divestment phase.
- **Programme:** Not named. The page shows partner logos for EU co-funding and "Plán obnovy" (Recovery Plan), but it doesn't say which, if any, relate to this investment.
- **Fund vehicle name:** No specific name is given. The page refers to "the fund managed by Zero Gravity Capital," so the manager's name is the closest identifier.
- **Number of companies:** Not stated. The page says capital went mainly to early-stage startups within five years of launch and to growth-oriented micro and small enterprises.
```
</details>

→ `Bash` — Show ORSR batch output so far
```sh
cat [tmp]
```

<details><summary>result</summary>

```
##### Vision Ventures
== Vision Ventures Growth I, s. r. o. | https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0
IČO: 52 656 438 | Sídlo: Bottova 2A, Bratislava - mestská časť Staré Mesto 811 09 | zápis: 04.10.2019
Spoločníci: National Development Fund II., a.s. IČO: 47 759 224 / Grösslingová 44 / Bratislava - mestská časť Staré Mesto 811 09 / (od: 23.09.2022) / Vision Ventures, s.r.o. IČO: 52 568 288 / Bottova 2A / Bratislava - mestská časť Staré Mesto 811 09 / (od: 23.09.2022) /
Vklady: National Development Fund II., a.s. / Vklad: 75 000 EUR ( peňažný vklad ) Splatené: 75 000 EUR / (od: 23.09.2022) / Vision Ventures, s.r.o. / Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR / (od: 23.09.2022) /
== Vision Ventures, s.r.o. | https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0
IČO: 52 568 288 | Sídlo: Bottova 2A, Bratislava - mestská časť Staré Mesto 811 09 | zápis: 22.08.2019
Spoločníci: MUDr. Tomáš Bél / Dátum narodenia: 18.03.1965 / (od: 25.05.2022) / Ing. Gabriel Horváth / Dátum narodenia: 22.02.1988 / (od: 12.11.2022) /
Vklady: MUDr. Tomáš Bél / Vklad: 2 500 EUR ( peňažný vklad ) Splatené: 2 500 EUR / (od: 25.05.2022) / Ing. Gabriel Horváth / Vklad: 2 500 EUR ( peňažný vklad ) Splatené: 2 500 EUR / (od: 12.11.2022) /
##### Zero Gravity Capital
== Zero Gravity Capital s.r.o. | https://www.orsr.sk/vypis.asp?ID=498371&SID=2&P=0
IČO: 52 651 894 | Sídlo: Staré Grunty 18, Bratislava - mestská časť Karlova Ves 841 01 | zápis: 01.10.2019
Spoločníci: 0100 Ventures s. r. o. IČO:
… [218 more characters]
```
</details>

→ `WebFetch` https://www.crowdberry.eu/en

<details><summary>result</summary>

```
The server returned HTTP 429 Too Many Requests.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebSearch` Crowdberry investícia 2026 kolo firma investori Crowdberry fond

<details><summary>result</summary>

```
Web search results for query: "Crowdberry investícia 2026 kolo firma investori Crowdberry fond"

Links: [{"title":"podil u miliardare jak se dari firmam ktere se otevrely verejnym investicim 2","url":"https://forbes.cz/email/podil-u-miliardare-jak-se-dari-firmam-ktere-se-otevrely-verejnym-investicim-2/"},{"title":"podil u miliardare jak se dari firmam ktere se otevrely verejnym investicim","url":"https://forbes.cz/email/podil-u-miliardare-jak-se-dari-firmam-ktere-se-otevrely-verejnym-investicim/"},{"title":"Marek Baranyai","url":"https://sk.linkedin.com/in/marekbaranyai/cs"},{"title":"Slovenská sporiteľňa (","url":"https://sk.linkedin.com/in/peter-paska-756a4a8b"},{"title":"Na slovenské crowdfunding platformě Crowdberry se vybralo za půl roku přes 43 milionů Kč","url":"https://cc.cz/na-slovenske-crowdfunding-platforme-crowdberry-se-vybralo-za-pul-roku-pres-43-milionu-kc/"},{"title":"Slovákom ukazujú ako investovať inak. Môžu sa stať bankármi","url":"https://sita.sk/slovakom-ukazuju-ako-investovat-inak-mozu-sa-stat-bankarmi/"},{"title":"Crowdberry Overview","url":"https://pitchbook.com/profiles/advisor/175582-36"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/crowberry-capital"},{"title":"podil u miliardare jak se dari firmam ktere se otevrely verejnym investicim","url":"https://forbes.cz/podil-u-miliardare-jak-se-dari-firmam-ktere-se-otevrely-verejnym-investicim/"},{"title":"Slovákom ukazujú ako investovať inak. Môžu sa stať bankármi","url
… [1892 more characters]
```
</details>

→ `WebFetch` https://forbes.cz/podil-u-miliardare-jak-se-dari-firmam-ktere-se-otevrely-verejnym-investicim/

→ `WebFetch` https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st

<details><summary>result</summary>

```
**Publication date:** October 8, 2019

**Amounts per manager and vehicle:**
- "Crowdberry, Zero Gravity Ventures, and Vision Ventures will manage €11.6m each."
- Slovak Investment Holding selected the three vehicles to invest €33m in total. The page says "the sum might rise to €70m" if milestones are met.

**Investment period:** The page doesn't say.

**Ticket sizes:** The page doesn't give per-deal ticket sizes. It gives Crowdberry's track record: "has already facilitated €14m in investments into 11 companies since 2016."
```
</details>

<details><summary>result</summary>

```
The content you provided contains only the page title, so I can't answer most of your questions:

- **Publication date:** Not stated.
- **Crowdberry AUM:** No sentence or figure about Crowdberry's assets under management.
- **Crowdberry fund (SIH co-invest fund):** Not mentioned.
- **Recent deals (2025-2026):** None listed.
- **Erste stake:** Not mentioned.

The title is in Czech and, translated, reads roughly: "A stake with a billionaire. How are companies that opened to public investment doing?" It's a Forbes article, but the title alone doesn't tell me anything about Crowdberry or the other details you asked about. To get those answers, please paste the article body.
```
</details>

→ `WebSearch` sih.sk Crowdberry kapitálová investícia fond

→ `Bash` — Show new ORSR batch output
```sh
cat [tmp] | tail -n +16
```

<details><summary>result</summary>

```
== Limerock Advisory, s. r. o. | https://www.orsr.sk/vypis.asp?ID=202952&SID=2&P=0
IČO: 46 092 897 | Sídlo: Planét 5, Bratislava 821 09 | zápis: 22.03.2011
Spoločníci: Roman Čmelík / Dátum narodenia: 04.05.1973 / (od: 03.06.2022) / Michal Jablonka / Dátum narodenia: 24.07.1978 / (od: 03.06.2022) /
Vklady: Roman Čmelík / Vklad: 2 500 EUR Splatené: 2 500 EUR / (od: 03.06.2022) / Michal Jablonka / Vklad: 2 500 EUR Splatené: 2 500 EUR / (od: 03.06.2022) /
== Limerock Investment Holding, s.r.o. | https://www.orsr.sk/vypis.asp?ID=307952&SID=2&P=0
IČO: 47 777 028 | Sídlo: Planét 5, Bratislava-Ružinov 821 02 | zápis: 16.05.2014
Spoločníci: Limerock Advisory, s.r.o. IČO: 46 092 897 / Planét 5 / Bratislava-Ružinov 821 02 / (od: 27.05.2022) / Aika Group Oy / Viikinkaari 6 / Helsinki 007 90 / Fínska republika / Iné identifikačné číslo: 2288188-1 / (od: 27.05.2022) /
Vklady: Limerock Advisory, s.r.o. / Vklad: 11 125 EUR ( peňažný vklad ) Splatené: 11 125 EUR / (od: 25.07.2025) / Aika Group Oy / Vklad: 1 375 EUR ( peňažný vklad ) Splatené: 1 375 EUR / (od: 25.07.2025) /
##### Crowdberry
```
</details>

<details><summary>result</summary>

```
Web search results for query: "sih.sk Crowdberry kapitálová investícia fond"

Links: [{"title":"vs sih layout ok 326","url":"https://www.sih.sk/data/files/vs_sih_layout_ok-326.pdf"},{"title":"vs sih 2019 sk final 363","url":"https://www.sih.sk/data/files/vs_sih_2019_sk_final-363.pdf"},{"title":"freshlabels ziskalo v prvnim investicnim kole 300 tisic eur diky tomu roste doma i v zahranici","url":"https://forbes.cz/freshlabels-ziskalo-v-prvnim-investicnim-kole-300-tisic-eur-diky-tomu-roste-doma-i-v-zahranici/"},{"title":"Přes Crowdberry investoři za šest let poskytli startupům 780 milionů korun, teď samo získává desítky milionů","url":"https://cc.cz/pres-crowdberry-investori-za-sest-let-poskytli-startupum-780-milionu-korun-ted-samo-ziskava-desitky-milionu/"},{"title":"slovaci zarobili na real estate takmer dvojnasobok cez crowdinvesticnu platformu spoluvlastnili komercne nehnutelnosti v trnave a nitre","url":"https://sita.sk/slovaci-zarobili-na-real-estate-takmer-dvojnasobok-cez-crowdinvesticnu-platformu-spoluvlastnili-komercne-nehnutelnosti-v-trnave-a-nitre/"},{"title":"We invest in the future of Slovakia","url":"https://www.sih.sk/en/"},{"title":"Lokální investování je na vzestupu, hlásí Crowdberry. Přes platformu a fondy loni proteklo přes 700 milionů","url":"https://cc.cz/lokalni-investovani-je-na-vzestupu-hlasi-crowdberry-pres-platformu-a-fondy-loni-proteklo-730-milionu/"},{"title":"crowdcreator.eu","url":"https://www.crowdcreator.eu/?p=1657"},{"title":"footshop si jde pro
… [1481 more characters]
```
</details>

→ `WebFetch` https://cc.cz/lokalni-investovani-je-na-vzestupu-hlasi-crowdberry-pres-platformu-a-fondy-loni-proteklo-730-milionu/

→ `WebSearch` Limerock investícia 2025 firma Limerock Fund fond Čmelík

<details><summary>result</summary>

```
Web search results for query: "Limerock investícia 2025 firma Limerock Fund fond Čmelík"

Links: [{"title":"Ako to vyzerá s Venture capitalom na Slovensku?","url":"https://www.startitup.sk/limerock-fund-manager/"},{"title":"Žltý melón získal významnú kapitálovú investíciu","url":"https://sita.sk/zlty-melon-ziskal-vyznamnu-kapitalovu-investiciu/"},{"title":"limerock fund manager kapitalova investicia","url":"https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=77733"},{"title":"LionRock To Return External Investments","url":"https://www.institutionalinvestor.com/article/b150z3qgd41d37/lionrock-to-return-external-investments"},{"title":"HarbourVest backs $1.9bn Lime Rock restructuring","url":"https://www.secondariesinvestor.com/harbourvest-backs-1-9bn-limerock-restructuring/"},{"title":"www.euronext.com","url":"https://www.euronext.com/en/post-trade/es-porto/notices/251242"},{"title":"lime rock closes 750m energy fund","url":"https://www.infrastructureinvestor.com/lime-rock-closes-750m-energy-fund/"},{"title":"lime rock announces closing of lime rock partners iv af acquisition fund 20180628027","url":"https://www.thetrustedinsight.com/investment-news/lime-rock-announces-closing-of-lime-rock-partners-iv-af-acquisition-fund-20180628027/"},{"title":"morgan lewis advises lime rock on 688 million fund","url":"https://www.mor
… [2056 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** 30 March 2023 (listed as "30. 3. 2023").

**Total AUM:** About CZK 2.4 billion. The article says: "Původem slovenské Crowdberry spravuje kapitál ve výši 2,4 miliardy korun." (Crowdberry manages capital of CZK 2.4 billion.) Its portfolio includes over 70 companies and real estate projects.

**Funds:** Besides the investment platform, Crowdberry runs three subsidiary funds. The article says: "Kromě investiční platformy Crowdberry provozuje tři dceřiné fondy."
- **CB Investment Management:** a startup-focused fund.
- **CB Property Investors:** a real estate fund.
- **CB ESPRI:** focused on organizations with a positive social impact. It was founded in May 2022 (the article says "loni v květnu"), has backed eleven projects with CZK 73 million, and has over CZK 170 million ready for investment.

**CB Investment Management:** The article says: "Startupově zaměřený CB Investment Management loni investoval do devíti firem necelých 140 milionů korun." (Last year, CB Investment Management invested almost CZK 140 million in nine companies.) "Loni" refers to 2022.

**Named deals (no exact dates given, only "loni" = 2022 or "počátkem letoška" = early 2023):**
- **Digitoo** (CB Investment Management): a Czech company digitizing accounting.
- **Vestberry** (CB Investment Management): a platform for managing global private equity fund investments.
- **Powerful Medical** (CB ESPRI): a cardiovascular diagnostics tool developer.
- **Scase** (CB ESPRI): a remote healthcare
… [281 more characters]
```
</details>

→ `WebFetch` https://www.limerock.sk/

→ `WebFetch` https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia

<details><summary>result</summary>

```
Limerock is a Slovak firm, Limerock Advisory, s.r.o., that runs two businesses: a transaction advisory practice and a venture capital arm. The page describes the VC arm as focused on "early growth-stage investments" (quoted from the page).

The page doesn't mention funds under management, specific investments, portfolio companies, dates, or ticket sizes. For those details, you'd need to check the firm's other pages or contact them directly.
```
</details>

<details><summary>result</summary>

```
The page has no figures beyond dates and an address. The fund's investment period was 2014 to 2016, and the page gives no capital amounts or returns.

- **Investment period:** "The fund's investment period ran from 2014 to 2016" (SIH's paraphrase: the fund invested during those two years).
- **Focus:** The fund backed small and medium-sized enterprises through equity investments made alongside private investors on equal terms.
- **Current status:** "The fund has completed its divestment process and is currently undergoing liquidation."
- **Manager:** Limerock Investment Holding, previously named Limerock Fund Manager, managed the fund and carried out its investment strategy.
- **Contact:** Grösslingová 44, 811 09 Bratislava, and www.sih.sk.
```
</details>

→ `WebSearch` "Limerock" investoval startup Slovensko 2024 OR 2025 OR 2026

→ `WebFetch` https://sandberg.capital/

<details><summary>result</summary>

```
Hostname/IP does not match certificate's altnames: Host: sandberg.capital. is not in the cert's altnames: DNS:*.nameserver.sk, DNS:nameserver.sk
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Limerock" investoval startup Slovensko 2024 OR 2025 OR 2026"

Links: [{"title":"Ako to vyzerá s Venture capitalom na Slovensku?","url":"https://www.startitup.sk/limerock-fund-manager/"},{"title":"Žltý melón získal významnú kapitálovú investíciu","url":"https://sita.sk/zlty-melon-ziskal-vyznamnu-kapitalovu-investiciu/"},{"title":"Crowdberry, Zero Gravity Ventures, and Vision Ventures to invest state money into Slovak start-ups","url":"https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st"},{"title":"limerock fund manager kapitalova investicia","url":"https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia"},{"title":"limerock sk","url":"https://superscout.co/investor/limerock-sk"},{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/?p=50283"},{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/kolko-milionov-eur-je-dnes-dostupnych-pre-slovenske-projekty/"},{"title":"What we do","url":"https://eif.org/what_we_do/resources/jeremie/news/2014/slovakia_vc.htm?lang=-en"},{"title":"limerock fund manager","url":"https://superscout.co/investor/limerock-fund-manager"}]

Limerock has a Slovak venture capital history, but this search turned up nothing dated 2024, 2025, or 2026. The results are older, mostly from
… [1366 more characters]
```
</details>

→ `WebFetch` https://www.sandberg.capital/

<details><summary>result</summary>

```
Hostname/IP does not match certificate's altnames: Host: www.sandberg.capital. is not in the cert's altnames: DNS:*.nameserver.sk, DNS:nameserver.sk
```
</details>

→ `WebSearch` Sandberg Capital investícia 2026 fond kúpil podiel

<details><summary>result</summary>

```
Web search results for query: "Sandberg Capital investícia 2026 fond kúpil podiel"

Links: [{"title":"Slovenský Sandberg Capital uzavřel svůj třímiliardový fond. Stovky milionů z něj investoval do českých firem","url":"https://cc.cz/slovensky-sandberg-capital-uzavrel-svuj-trimiliardovy-fond-stovky-milionu-z-nej-investoval-do-ceskych-firem/"},{"title":"FORWARD FEATURES CALENDAR","url":"https://www.privateequitywire.co.uk/?p=94080"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-firmy-fond-j-t-arch-ii-koupil-podil-v-seyforu-nebo-dotykacce-312092"},{"title":"Sandberg Capital Acquires 75% Stake in Hungary’s Green Fox Academy","url":"https://www.globalprivatecapital.org/?p=39400"},{"title":"J&T uzavrela česko-slovenský obchod za 278 miliónov eur. Vstupuje do firiem, ktoré ovplyvňujú životy Slovákov","url":"https://www.startitup.sk/?p=1225008"},{"title":"jsme ve tretine toho co ze solitey budujeme rika v exkluzivnim rozhovoru michal rybovic","url":"https://forbes.cz/jsme-ve-tretine-toho-co-ze-solitey-budujeme-rika-v-exkluzivnim-rozhovoru-michal-rybovic/"},{"title":"J&T ARCH II posílá 278 milionů eur do Sandberg Capital. Získá podíl ve fondu se Seyforem","url":"https://www.e15.cz/byznys/burzy-a-trhy/j-t-arch-ii-posila-278-milionu-eur-do-sandberg-capital-ziska-podil-ve-fondu-se-seyforem-1434678"},{"title":"globalscopepartners.com","url":"https://globalscopepartners.com/?p=1655"},{"title":"Institutional investor · Portfolio as of Q1 2026","url":"https://mc
… [1437 more characters]
```
</details>

→ `WebFetch` https://cc.cz/slovensky-sandberg-capital-uzavrel-svuj-trimiliardovy-fond-stovky-milionu-z-nej-investoval-do-ceskych-firem/

→ `WebFetch` https://www.e15.cz/byznys/burzy-a-trhy/j-t-arch-ii-posila-278-milionu-eur-do-sandberg-capital-ziska-podil-ve-fondu-se-seyforem-1434678

<details><summary>result</summary>

```
**Publication date:** 31 July 2026, 15:08 (e15.cz)

**Key sentence:**
"Za přibližně 278 milionů eur vstoupí do podfondu Sandberg Private Equity Fund 1,"

In English, the fund is buying into a Sandberg Capital sub-fund for about €278 million, which gives it a stake in the portfolio companies.
```
</details>

<details><summary>result</summary>

```
**Publication date:** 16 December 2021

**Fund size:** The article quotes the fund as "uzavření svého druhého fondu v navýšeném objemu 130 milionů eur" (closing of its second fund at an increased volume of €130 million), roughly CZK 3.3 billion. The original target was "jen" 109 milionů eur (only €109 million).

**Ticket sizes:** The article gives no per-deal figures. The only amount is for Daktela, where the fund took a minority stake for "stovky milionů korun" (hundreds of millions of CZK). The headline's "stovky milionů" refers to the total invested in Czech firms, not individual tickets.

**Strategy:** The article describes private equity, not venture capital. It says Sandberg "nakupuje společnosti nebo jejich části a během několika let buduje byznys" (buys companies or parts of them and builds the business over several years). It contrasts this with venture investing, calling it "konzervativnější investice" (more conservative investments) in firms that already have an established market position. It does not label the strategy as buyout or growth. The fund targets small and medium-sized companies in Central and Eastern Europe, and it has no sector focus.

**Latest investments:**
- **Daktela** (Czech, contact-centre software): a minority stake, which the article describes as "získal za stovky milionů korun minoritní podíl".
- **Titans Freelancers** (Slovak): the fund-backed company "získala většinu" (acquired a majority) in Czech HR agency Bridgewater.
- **Swan** (Slovak
… [95 more characters]
```
</details>

→ `WebSearch` "Fond inovácií a technológií" a.s. investícia startup 2023 OR 2024 OR 2025

→ `Bash` — Show further ORSR batch output
```sh
tail -n +25 [tmp]
```

<details><summary>result</summary>

```
== Crowdberry Investment Platform j. s. a. | https://www.orsr.sk/vypis.asp?ID=639222&SID=2&P=0
IČO: 54 827 370 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 26.08.2022
== Crowdberry SK32 j. s. a. | https://www.orsr.sk/vypis.asp?ID=597338&SID=2&P=0
IČO: 53 921 208 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 29.07.2021
== Crowdberry SK33 j. s. a. | https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0
IČO: 53 921 186 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 14.07.2021
Akcionár: Crowdberry a.s. IČO: 48 236 993 / Staromestská 3 / Bratislava - mestská časť Staré Mesto 811 03 / (od: 14.07.2021) /
== Crowdberry SK35 j. s. a. | https://www.orsr.sk/vypis.asp?ID=597460&SID=2&P=0
IČO: 53 963 857 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 05.08.2021
== Crowdberry SK39 j. s. a. | https://www.orsr.sk/vypis.asp?ID=620567&SID=2&P=0
IČO: 54 548 161 | Sídlo: Staromestská 3, Bratislava-mestská časť Staré Mesto 811 03 | zápis: 12.05.2022
Akcionár: Crowdberry a.s. IČO: 48 236 993 / Staromestská 3 / Bratislava - mestská časť Staré Mesto 811 03 / (od: 12.05.2022) / Ďalšie právne skutočnosti: / Spoločnosť bola založená zakladateľskou zmluvou vo forme notárskej zápisnice zo dňa 13.10.2021 v zmysle príslušných ustanovení z. č. 513/1991 Zb. v znení neskorších predpisov – Obchodného zákonníka v platnom znení. / (od: 12.05.2022) /
== Crowdberry SK49 j. s. a. | https:
… [3488 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Fond inovácií a technológií" a.s. investícia startup 2023 OR 2024 OR 2025"

Links: [{"title":"FIT vám pomôže zafinancovať inovatívne podnikateľské nápady","url":"https://www.podnikajte.sk/investor/fit-fond-financovanie"},{"title":"www.startitup.sk","url":"https://www.startitup.sk/?p=12849"},{"title":"fondfit oznamuje dalsie investicie obe do hernehobiznisu","url":"https://www.startitup.sk/fondfit-oznamuje-dalsie-investicie-obe-do-hernehobiznisu/"},{"title":"Nový DeepTech fond podpoří vysoce inovativní startupy. V první fázi půjde až o miliardu korun","url":"https://www.businessinfo.cz/clanky/novy-deeptech-fond-podpori-vysoce-inovativni-startupy-v-prvni-fazi-pujde-az-o-miliardu-korun/"},{"title":"V Brně vznikl fond pro startupy, který bude investovat i peníze kraje","url":"https://www.lupa.cz/aktuality/v-brne-vznikl-fond-pro-startupy-ktery-bude-investovat-i-penize-kraje/"},{"title":"Sony otevírá investiční fond pro startupy. Celkem do nich vloží kolem 185 milionů dolarů","url":"https://cc.cz/sony-otevira-investicni-fond-pro-startupy-celkem-do-nich-vlozi-kolem-185-milionu-dolaru/"},{"title":"Nizozemsko posiluje podporu technologických startupů, ukazuje cestu i Česku","url":"https://www.businessinfo.cz/clanky/nizozemsko-posiluje-podporu-technologickych-startupu-ukazuje-cestu-i-cesku/"},{"title":"V Česku vytvoria nový fond na podporu startupov s kapitálom 2,3 miliardy korún","url":"https://www.podnikajte.sk/investor/cesko-fond-startupy"},{"title":"
… [1371 more characters]
```
</details>

→ `WebSearch` Eterus Capital investícia fond Eterus Growth Fund 2024 2025

→ `WebFetch` https://www.eterus.sk/

<details><summary>result</summary>

```
Web search results for query: "Eterus Capital investícia fond Eterus Growth Fund 2024 2025"

Links: [{"title":"eterus capital","url":"https://www.vestbee.com/vc-list/eterus-capital"},{"title":"Eterus Capital logo","url":"https://www.tryfundable.ai/investor/eterus-capital"},{"title":"Eterus Capital","url":"https://app.dealroom.co/companies/eterus_capital"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/eterus-capital"},{"title":"Eterus Capital has acquired a minority stake in MTBIKER Group","url":"https://oaklins.com/pt/en/deals/109156"},{"title":"Eterus Capital has acquired a minority stake in MTBIKER Group","url":"https://www.oaklins.com/de/de/deals/109156/"},{"title":"Eterus Capital has acquired a minority stake in eyerim","url":"https://oaklins.com/hr/en/deals/106270"},{"title":"Go to deals","url":"https://oaklins.com/pt/en/deals/108664"},{"title":"14020 bartosik svaby advises eterus capital on acquisition of stake in eyerim","url":"https://ceelegalmatters.com/slovakia/14020-bartosik-svaby-advises-eterus-capital-on-acquisition-of-stake-in-eyerim"},{"title":"sg.finance.yahoo.com","url":"https://sg.finance.yahoo.com/quote/DTSRF/chart"}]

I found no results for an "Eterus Growth Fund." The results cover Eterus Capital, a Slovak private equity fund, and none of them include 2024 or 2025 deals.

- **Background:** Eterus Capital is managed by Wood & Company. The fund only invests in minority positions while management control always remains in
… [870 more characters]
```
</details>

<details><summary>result</summary>

```
**What Eterus does:** Eterus Capital is a private equity firm based in Bratislava. It takes minority equity stakes in growth-stage Slovak companies with capable management and a proven concept, and it does not offer debt financing. Management control stays with the founders. The page says the firm has invested more than EUR 40 million in innovation.

**Funds (names, sizes, vintage):** The page does not name any funds or give fund sizes or vintage years. It only cites a total of over EUR 40 million invested.

**Ticket size:** "Zameriavame sa na investície v rozmedzí 2 - 2,5 mil. EUR" (We focus on investments in the range of EUR 2 to 2.5 million). The preferred holding period is 5 to 7 years.

**Sectors:** The page does not list a formal sector focus. It emphasizes innovation and Slovak-domiciled companies. Portfolio companies span dental and pharmacy consolidation, healthcare manufacturing, market research technology, simulation, e-commerce, mobility, and smart housing.

**Stages:** Growth-stage companies, with an equity focus.

**Portfolio (no investment dates given):**
- Dr. Martin (dental clinic consolidation platform)
- EC Pharmacies (pharmacy consolidation platform)
- MTBIKER (cycling portal)
- GroupSolver (machine-learning market research)
- Virtual Reality Media (simulation technology)
- CTI Group (medical supplies manufacturer)
- Eyerim (online eyewear retailer)
- Ecocapsule (self-sufficient micro-homes)
- HOPIN (ride-hailing app)
- EEI (parking systems)

The Saneca Ph
… [658 more characters]
```
</details>

→ `WebSearch` Eterus Capital "Dr. Martin" OR "EC Pharmacies" investícia

→ `WebSearch` "Prvá kapitálová" fond investície

<details><summary>result</summary>

```
Web search results for query: ""Prvá kapitálová" fond investície"

Links: [{"title":"Original title:","url":"https://invenio.nusl.cz/record/11977?ln=en"},{"title":"Príspevok do kapitálových fondov: Účtovanie a praktické aspekty","url":"https://ddadsstornala.sk/aktuality/prispevok-do-kapitalovych-fondov/"},{"title":"kapitalovy trh","url":"https://www.newstream.cz/stitek/kapitalovy-trh"},{"title":"Kapitálové fondy: Vytvorenie, použitie a daňové aspekty","url":"https://zssambra.sk/blog/prispevok-do-kapitalovych-fondov/"},{"title":"Komerční banka nabízí fond Amundi PRIMA","url":"https://www.kb.cz/cs/o-bance/tiskove-zpravy/komercni-banka-nabizi-fond-amundi-prima"},{"title":"Private equity a venture kapitálové fondy pôsobiace v SR","url":"https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr"},{"title":"PRVA Capital Partners secures €60m at first close to back SME growth in Slovenia and Croatia","url":"https://pe-insights.com/prva-capital-partners-secures-e60m-at-first-close-to-back-sme-growth-in-slovenia-and-croatia/"},{"title":"Realitný fond Prvej penzijnej bez poplatku","url":"https://sita.sk/realitny-fond-prvej-penzijnej-bez-poplatku/"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/251667"}]

The search didn't return anything about a fund called "Prvá kapitálová" specifically. The closest hits are:

- **PRVA Capital Partners** (Slovenian private equity manager): announced the first close of its latest fund with over €60m in capital commitments.
… [638 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Eterus Capital "Dr. Martin" OR "EC Pharmacies" investícia"

Links: [{"title":"Go to deals","url":"https://oaklins.com/ar/en/deals/110583"},{"title":"Transaktionen anzeigen","url":"https://www.oaklins.com/ch/de/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/pt/pt-pt/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/fr/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/ca/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/ma/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/it/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/at/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/pl/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/br/en/deals/110583/"}]

The search turned up one deal, in May 2024, between Eterus Capital and Dr. Martin. I found nothing about "EC Pharmacies," so that part of your query came up empty. I dropped the quotes and OR operators to run the search.

- **The deal:** Dr. Martin Dental Clinic, a dental clinic network in Slovakia, took an investment from Eterus Capital and Ethernum Capital to fund expansion. The group wants to become the country's largest dental care provider through buy-and-build acquisitions plus new clinic openings (May 2024 — Dr. Martin Dental Clinic, a leading network of dental clinics in Slovakia, has received a significant investm
… [1050 more characters]
```
</details>

→ `WebSearch` "Nation1" Slovakia investor OR fund OR venture

→ `WebSearch` Gapfunding Slovensko investori startup

<details><summary>result</summary>

```
Web search results for query: ""Nation1" Slovakia investor OR fund OR venture"

Links: [{"title":"Nový český investiční fond Nation 1 má pro startupy 500 milionů korun. Do konce roku nabere téměř miliardu","url":"https://cc.cz/novy-cesky-investicni-fond-nation-1-ma-pro-startupy-500-milionu-korun-do-konce-roku-nabere-temer-miliardu/"},{"title":"Slovak Investment Holding (investor - Venture Capital)","url":"https://nordic9.com/companies/slovak-investment-holding/"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/4853310.pdf"},{"title":"nation 1 meni jmeno a chysta novy fond do vedeni jmenoval dva nove partnery","url":"https://www.newstream.cz/zpravy-z-firem/nation-1-meni-jmeno-a-chysta-novy-fond-do-vedeni-jmenoval-dva-nove-partnery"},{"title":"Join Vestbee","url":"https://vestbee.com/vc-list/nation-1-vc"},{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"Venture to Future Fund","url":"https://www.sih.sk/en/stranky/cinnosti/venture-to-future-fund"},{"title":"Recherche Fr menu fr ClientConnect","url":"https://eib.org/fr/projects/all/20190166?lang=fr"},{"title":"Recherche FR menu Portail client du Groupe BEI","url":"https://www.eib.org/fr/projects/all/20190166"}]

The search didn't turn up a Slovak-based fund called "Nation1." The closest match is **Nation 1**, a Czech venture fund that invests in Slovakia.

- **Nation 1 is Czech, not Slovak.** A Czech outlet describes it as a new Cze
… [1180 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Gapfunding Slovensko investori startup"

Links: [{"title":"GapMinder Leads €2.6M Seed Round in Slovenian AI Startup","url":"https://www.therecursive.com/tag/slovenia/"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=12"},{"title":"Popularita private equity a venture kapitálu na Slovensku","url":"https://www.podnikajte.sk/investor/private-equity-venture-kapital-na-slovensku"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/investor/investorske-forum-bratislava"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/financie/c/1994/category/investor/article/investorske-forum-bratislava.xhtml"},{"title":"Startupy mnohdy neřeší skutečné či důležité problémy, říká venture kapitálový investor","url":"https://www.businessinfo.cz/clanky/startupy-mnohdy-neresi-skutecne-ci-dulezite-problemy-rika-venture-kapitalovy-investor-video-podcast/"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Slovensko zaostáva v investíciách do startupov v oblasti zdravotníctva. V čom sa musí zlepšiť?","url":"https://sit
… [1847 more characters]
```
</details>

→ `WebFetch` https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/

→ `WebSearch` Seed Starter Slovenská sporiteľňa investícia startup 2025 2026

<details><summary>result</summary>

```
- **Publication date:** 8 September 2022 (listed as "08. 9. 2022").
- **Program name:** Seed Starter. The Slovak version operates under the Slovenská spořitelna banner. The article says it "bude fungovat pod hlavičkou Slovenské spořitelny."
- **Legal vehicle:** Not stated. The article describes the program as a CVC (corporate venture capital) and incubation program but does not name a legal entity or fund structure.
- **Size:** "Pět milionů eur, tedy v přepočtu více než 123 milionů korun" (five million euros, over 123 million CZK). The article's headline gives the figure as "přes 120 milionů."
- **Ticket:** Not stated. The article gives no check size or typical investment amount.
- **First investments:** None are named for the Slovak program. The five startups in the portfolio (Investown, Signi, PalmApp, Wflow, Rekenber) are from the Czech program.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Seed Starter Slovenská sporiteľňa investícia startup 2025 2026"

Links: [{"title":"www.startitup.sk","url":"https://www.startitup.sk/?p=1240594"},{"title":"Seed Starter Slovenskej sporiteľne hlási prvú investíciu: podporil slovenský startup SmartHead","url":"https://sita.sk/seed-starter-slovenskej-sporitelne-hlasi-prvu-investiciu-podporil-slovensky-startup-smarthead/"},{"title":"Slovensko je čierna diera startupov, zachrániť ho ide táto spoločnosť. Investovať u nás chce 5 miliónov eur","url":"https://www.startitup.sk/?p=664120"},{"title":"Slovensko sa ocitlo na chvoste Európy, v rozvoji startupov zaostávame za najlepšími","url":"https://sita.sk/slovensko-sa-ocitlo-na-chvoste-europy-v-rozvoji-startupov-zaostavame-za-najlepsimi/"},{"title":"Šéf Slovenskej sporiteľne: Slovensko by malo skvalitniť školstvo. Naša ekonomika má zásadný problém","url":"https://www.startitup.sk/?p=676083"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/seedstarter-sk"},{"title":"slsp infografika 1q 2026","url":"https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/slsp-infografika-1q-2026.pdf"},{"title":"Toto je nová generácia slovenských superpodnikateľov. Tieto domáce firmy uvidíš všade","url":"https://www.startitup.sk/?p=698215"},{"title":"startup report slovensko 2025","url":"https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/startup-report-slovensko-2025.pdf
… [1448 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/?p=1240594

→ `WebFetch` https://sita.sk/seed-starter-slovenskej-sporitelne-hlasi-prvu-investiciu-podporil-slovensky-startup-smarthead/

<details><summary>result</summary>

```
- **Publication date:** 5 September 2023, 14:00 (updated 14:05).
- **Investment sentence:** "Seed Starter Slovenskej sporiteľne získal 7 % podiel v slovenskom startupe SmartHead" (The Seed Starter of Slovenská sporiteľňa acquired a 7% stake in the Slovak startup SmartHead.)
- **Investment amount:** The article does not disclose it.
- **Legal name of the Seed Starter entity:** The article does not give one. It refers only to "Seed Starter Slovenskej sporiteľne" and to Slovenská sporiteľňa (SLSP).
```
</details>

<details><summary>result</summary>

```
- **Publication date:** 25 September 2026, at 12:13. The article is partner (PR) content.

- **What it's about:** Startup Awards Slovensko, run by SASK, has extended its application deadline to 30 September 2026. Selected teams go through a three-day bootcamp and a November final in Bratislava Castle's Jazdiareň. The winning team can receive an investment offer from Slovenská sporiteľňa's Seed Starter program and a trip to Silicon Valley.

- **Seed Starter investment:** Yes. The winning team may receive an investment offer of up to €250,000. The article gives no date for the investment itself. The final is on 25 November 2026.

Key quotes:
- "Víťazný tím môže od Seed Startera Slovenskej sporiteľne získať ponuku investície až do výšky 250 000 eur." (The winning team may receive an investment offer of up to €250,000 from Seed Starter.)
- "Prihlášky je možné podať do 30. septembra 2026" (Applications can be submitted until 30 September 2026.)
- "Vybrané tímy následne čaká intenzívny trojdňový Bootcamp" (Selected teams then face an intensive three-day bootcamp.)
```
</details>

→ `Bash` — Show remaining ORSR batch output
```sh
sed -n '/##### ZAKA/,$p' [tmp]
```

<details><summary>result</summary>

```
##### ZAKA
== Za Kasárňou 1 s. r. o. | https://www.orsr.sk/vypis.asp?ID=697220&SID=2&P=0
IČO: 56 357 958 | Sídlo: Za kasárňou 315/1, Bratislava - mestská časť Nové Mesto 831 03 | zápis: 16.07.2024
Spoločníci: Meracrest Group SE IČO: 36 868 175 / Za kasárňou 315/1 / Bratislava - mestská časť Nové Mesto 831 03 / (od: 16.07.2024) /
Vklady: Meracrest Group SE / Vklad: 1 710 902 EUR ( nehnuteľnosť ) Splatené: 1 710 902 EUR / (od: 16.07.2024) /
== ZAK - AGRA, s.r.o. | https://www.orsr.sk/vypis.asp?ID=345378&SID=7&P=0
IČO: 50 056 221 | Sídlo: Labutia 2167/16, Veľký Meder 932 01 | zápis: 09.03.2016
Spoločníci: Mgr. Gejza Zakál / Dátum narodenia: 23.01.1990 / (od: 30.07.2022) /
Vklady: Mgr. Gejza Zakál / Vklad: 5 000 EUR ( peňažný vklad ) Splatené: 5 000 EUR / (od: 30.07.2022) /
== ZAKA colours, s. r. o. | https://www.orsr.sk/vypis.asp?ID=770797&SID=7&P=0
IČO: 57 804 541 | Sídlo: Trnavská cesta 855/29, Sereď 926 01 | zápis: 19.08.2026
Spoločníci: Zlatko Haško / Dátum narodenia: 22.08.1986 / (od: 19.08.2026) /
Vklady: Zlatko Haško / Vklad: 5 000 EUR ( peňažný vklad ) Splatené: 5 000 EUR / (od: 19.08.2026) /
== ZAKA CONSTRUCTION, s. r. o. | https://www.orsr.sk/vypis.asp?ID=514871&SID=3&P=0
IČO: 52 977 668 | Sídlo: Švermova 1820/21, Banská Bystrica 974 04 | zápis: 05.03.2020
Spoločníci: Jaroslav Kapustík / Dátum narodenia: 21.10.1993 / (od: 19.05.2022) /
Vklady: Jaroslav Kapustík / Vklad: 5 000 EUR ( peňažný vklad ) Splatené: 5 000 EUR / (od: 19.05.2022) /
== zaka kp, s. r. o. |
… [2612 more characters]
```
</details>

→ `WebFetch` https://zaka.vc/

→ `WebSearch` ZAKA VC fund Bratislava Slovak founders deep tech seed fund

<details><summary>result</summary>

```
Web search results for query: "ZAKA VC fund Bratislava Slovak founders deep tech seed fund"

Links: [{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"ZAKA VC Research","url":"https://f4.fund/firms/zaka-vc"},{"title":"Join Vestbee","url":"https://vestbee.com/insights/articles/vc-of-the-month-zaka"},{"title":"CEE VC SUMMIT 2026","url":"https://www.vestbee.com/blog/articles/vc-of-the-month-zaka"},{"title":"ZAKA Ventures","url":"https://signal.nfx.com/firms/zaka-ventures"},{"title":"zaka ventures zaka vc","url":"https://venturecapitalarchive.com/venture-funds/zaka-ventures-zaka-vc"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"Ján Búza zo ZAKA VC: Slovenský pôvod nie je v Silicon Valley prekážkou","url":"https://www.startitup.sk/?p=1130105"},{"title":"zaka vc","url":"https://allbusiness.africa/investors/zaka-vc"}]

ZAKA VC is a pre-seed and seed investor with offices in Prague and Bratislava, and it has a deep-tech focus, though the sources differ on some details.

- **Founders and origin:** One source says ZAKA VC is a Prague and Silicon Valley-based seed and pre-seed fund founded in 2020 by serial entrepreneur Jan Kasper and Peter Zalešák as a family office. Another describes the firm as operating from Prague, London and Bratislava.
- **Fund structure:** The firm moved from
… [1576 more characters]
```
</details>

<details><summary>result</summary>

```
**Zaka VC: Key Details (from page content)**

- **Legal entity:** Not stated on the page.
- **Location/HQ:** Not explicitly designated. Offices are listed as Silicon Valley, London, Prague, and Bratislava.
- **Team origin:** Not stated in the provided content.
- **Fund size:** 17M current fund size. Fund 1 is listed at 17M with 8M invested across 46 companies. A separate Family office entry shows 5M with 5M invested across 34 companies. The page layout makes this mapping somewhat ambiguous.
- **Ticket size:** "The minimum ticket is 130K."
- **Sectors:** Health & Biotech and Industrial Tech.
- **Stages:** Seed and pre-seed.
- **Geography:** Invests mainly in the US and Europe. Stated aim is to bridge North America and Europe.
- **Portfolio:** 97 companies invested in total, 5 exits, 1 unicorn. Named companies include WonderTx, Aerogen Systems, FinalDose, PerfectBit, Human Archive, AxionOrbital Space, CellType, Sygaldry Technologies, HexemBio, Ateios Systems, bit.bio, Superlinked, and Sutro, among others. The page describes its Healthcare & Life Sciences portfolio as one of the best in continental Europe.
- **News (dates as shown on page):**
  - **10/08/2026** (Zaka blog): "mRNA is still made the 1984 way. It was not built for the drugs coming next."
  - **10/06/2026** (Press release): Sensible Biotechnologies' $47M raise and Zaka's early backing.
  - **09/23/2026** (Zaka blog): "You choose the science. The disease chooses the bill."
```
</details>

→ `WebFetch` https://www.startitup.sk/?p=1130105

→ `WebFetch` https://www.vestbee.com/blog/articles/vc-of-the-month-zaka

<details><summary>result</summary>

```
- **Publication date:** October 26, 2023.
- **Location:** Prague, London, and Bratislava. The article describes ZAKA as "a pre-seed and seed VC family office operating from Prague, London and Bratislava."
- **Founders' nationality:** Not stated. The article names the founders as Peter Zalesak and Jan Kasper but doesn't give their nationalities.
- **Fund size:** Not stated. The article gives annual investment pace, not total fund size.
- **Ticket size:** The fund strategy lists "250ths. Eur," which likely means €250K, though the source wording is unclear.
- **Investments per year:** About 15 companies. The article says ZAKA "invests 3m Eur every year into approx 15 companies."
```
</details>

<details><summary>result</summary>

```
- **Publication date:** 21 October 2025, at 16:39.
- **Where ZAKA VC is based:** The article gives conflicting details. The subtitle describes a branch ("pobočka") in San Francisco, while the body says the fund has its "so sídlom v San Franciscu" (seat in San Francisco). Registration details are not mentioned.
- **Founders and nationality:** The article does not name the founders. It says the fund was built from the family capital of the Kasperovci and Zálešáci families, and Ján Búza is a partner. It calls ZAKA a "slovenský fond" (Slovak fund) and describes its roots as Czech-Slovak, but it does not state the founders' nationalities.
- **Fund size:** The first fund was €15 million. The article says the target was raised to €17 million due to investor demand, and the second fund is expected to be larger.
- **Ticket size:** Not stated.
- **Slovak investments with dates:** None are named or dated. The article mentions the AceOn accelerator in Bratislava, run with Accace, but no specific Slovak portfolio investments.
```
</details>

→ `WebSearch` 365.fintech investícia startup 2025 2026

→ `WebFetch` https://365fintech.sk/

<details><summary>result</summary>

```
Web search results for query: "365.fintech investícia startup 2025 2026"

Links: [{"title":"ecosystem.madrimasd.org","url":"https://ecosystem.madrimasd.org/companies/365_fintech/team"},{"title":"365 fintech","url":"https://insights.munich-startup.de/investors/365_fintech"},{"title":"365 fintech","url":"https://ecosystem.madrimasd.org/investors/365_fintech"},{"title":"365 fintech","url":"https://insights.munich-startup.de/companies/365_fintech"},{"title":"365 fintech","url":"https://app.dealroom.co/companies/365_fintech"},{"title":"365.fintech Investor","url":"https://mindmaps.femtech.health/firms/44410"},{"title":"funding.tech.eu","url":"https://funding.tech.eu/sectors/fintech/2025"},{"title":"anyof Hungary","url":"https://startups.one.gob.es/companies/365_fintech/portfolio/f/locations/anyof_Hungary"},{"title":"fintech startups trends attract investments","url":"https://qubit.capital/blog/fintech-startups-trends-attract-investments"},{"title":"blog.mean.ceo","url":"https://blog.mean.ceo/?p=5752"}]

The search turned up profile pages for 365.fintech but no specific 2025–2026 deals from the firm itself.

- **What it is:** Profiles describe 365.fintech as a boutique VC focusing on pre-seed & seed API-first, infrastructure & b2b/b2b2c fintech in broader CEE & Baltics. Other listings describe it as an investment platform for fintech, insurtech and big data startups, focusing on CEE and EU at large.
- **Basics:** One profile lists headquarters in Bratislava, Slovakia, and a foundin
… [929 more characters]
```
</details>

<details><summary>result</summary>

```
**What it is:** 365.fintech, a.s. is a fintech venture investor based in Bratislava, Slovakia. It invests in seed-stage B2B and B2B2C fintech, InsurTech, and Big Data startups, mainly in Europe. It also offers operational and strategic support, and it describes itself as part of the 365 ecosystem.

**Owner:** The page doesn't name owners or shareholders. It lists 365.fintech, a.s. as the legal entity and Rudolf Vrábel (Managing Partner) and Tomáš Vyšný (Partner) as the team. 365.bank appears as a partner.

**Ticket size:** Not stated. The page gives no per-investment amount. In a 2018 news item, the firm said it aimed to invest €2 million in its inception phase, which is a total capital figure, not a ticket size.

**Sectors:**
- B2B and B2B2C fintech
- InsurTech
- Big Data
- Focus on startups disrupting legacy infrastructure and distribution, serving end consumers and SMEs

**Stages:**
- Seed stage, around seed
- Mainly European startups, with a CEE base and investments "anywhere in Europe"

**Portfolio (dates from related news, where available):**
- Ondato (KYC/AML platform): news dated Sep 15, 2022
- Velaris (customer success platform): news dated Sep 20, 2022
- Tymit (credit card): Mar 5, 2021
- InvestSuite (WealthTech): Jan 5, 2021
- Pynk (social wealth management): Oct 14, 2020
- FinCompare (SME financing, Series A co-investment): Mar 11, 2020
- PénTech (SME invoice factoring): Nov 14, 2019
- Startup Wise Guys (accelerator): Jul 4, 2019
- Dateio (card-linked loyalty/anal
… [1166 more characters]
```
</details>

→ `WebSearch` J&T Ventures fond startupy investícia Slovensko 2024 2025

→ `WebSearch` Tatra banka startup investícia fond VÚB startup program kapitál

<details><summary>result</summary>

```
Web search results for query: "J&T Ventures fond startupy investícia Slovensko 2024 2025"

Links: [{"title":"Skupina J&T loví startupy v Chorvatsku","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/skupina-j-t-lovi-startupy-v-chorvatsku-1253515"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=6"},{"title":"J&T Ventures investovali do prvých dvoch startupov","url":"https://www.podnikajte.sk/investor/jt-ventures-investovali"},{"title":"Tlačová správa","url":"https://www.podnikajte.sk/autori/tlacova-sprava?page=58"},{"title":"www.podnikajte.sk","url":"https://www.podnikajte.sk/clanky?page=737"},{"title":"J&T uzavrela česko-slovenský obchod za 278 miliónov eur. Vstupuje do firiem, ktoré ovplyvňujú životy Slovákov","url":"https://www.startitup.sk/?p=1225008"},{"title":"www.podnikajte.sk","url":"https://www.podnikajte.sk/financie?page=36"},{"title":"J&T Ventures","url":"https://cc.cz/tag/jt-ventures/"},{"title":"podim.org","url":"https://podim.org/?p=33008"}]

Search results on J&T Ventures' Slovak startup investments are mostly old, and none clearly cover 2024–2025.

- **Early Slovak investments:** Roughly a year after its launch, the J&T Ventures fund announced its first investments, in FetView (health documentation) and ICE GATEWAY (Smart City tech). Po necelom roku existencie ohlásil venture kapitálový fond J&T Banky investície niekoľko stotisíc eur prvým start-upom. Fond J&T Ventures investoval do startupu pre zdravotnícku do
… [1396 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Tatra banka startup investícia fond VÚB startup program kapitál"

Links: [{"title":"39 start up funding for young entrepreneurs","url":"https://national-policies.eacea.ec.europa.eu/youthwiki/chapters/slovakia/39-start-up-funding-for-young-entrepreneurs"},{"title":"tatra banka spolupraci so sih podporila podnikatelske investicie takmer 60 milionmi eur","url":"https://www.tatrabanka.sk/sk/blog/tlacove-spravy/tatra-banka-spolupraci-so-sih-podporila-podnikatelske-investicie-takmer-60-milionmi-eur/"},{"title":"Tatra Banka: Pôžičky pre Živnostníkov a Podmienky pre Úspešný Rozbeh Podnikania","url":"https://ddadsstornala.sk/aktuality/tatra-banka-pozicka-pre-zivnostnikov/"},{"title":"Nemajú peniaze a neveria si. Slováci prezradili 10 dôvodov, prečo si neplnia sny","url":"https://www.startitup.sk/10-dovodov-preco-si-neveria-slovensko/"},{"title":"Tlačové správy","url":"https://www.tatrabanka.sk/sk/blog/tlacove-spravy/?page=6"},{"title":"tatra banka investuje do popredneho private equity fondu cielom posilnit rast inovacie slovensku","url":"https://www.tatrabanka.sk/sk/blog/tlacove-spravy/tatra-banka-investuje-do-popredneho-private-equity-fondu-cielom-posilnit-rast-inovacie-slovensku/"},{"title":"Eva Stanzl","url":"https://sk.linkedin.com/in/eva-stanzl-80606847"},{"title":"tatra banka podporila prve spolocnosti programe zarucenych uverov od sih","url":"https://www.tatrabanka.sk/sk/blog/tlacove-spravy/tatra-banka-podporila-prve-spolocnosti-programe-zaruceny
… [2141 more characters]
```
</details>

→ `WebFetch` https://www.tatrabanka.sk/sk/blog/tlacove-spravy/tatra-banka-investuje-do-popredneho-private-equity-fondu-cielom-posilnit-rast-inovacie-slovensku/

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebSearch` VÚB banka investícia startup fond corporate venture "VÚB"  startupy kapitálový vstup

<details><summary>result</summary>

```
Web search results for query: "VÚB banka investícia startup fond corporate venture "VÚB"  startupy kapitálový vstup"

Links: [{"title":"VÚB zníži sadzbu až do 0,3%. Pre firmy, ktoré investujú do obnoviteľných riešení","url":"https://sita.sk/vub-znizi-sadzbu-az-do-03-pre-firmy-ktore-investuju-do-obnovitelnych-rieseni/"},{"title":"Príležitosť pre malé a stredné podniky na Slovensku","url":"https://sita.sk/prilezitost-pre-male-a-stredne-podniky-na-slovensku/"},{"title":"VÚB Leasing má od EIB k dispozícii vyše 26 miliónov eur","url":"https://sita.sk/vub-leasing-ma-od-eib-k-dispozicii-vyse-26-milionov-eur/"},{"title":"Jozef Kausich","url":"https://sk.linkedin.com/in/jozef-kausich"},{"title":"Skupiny%20financnych%20nastrojov%20a%20produktov%20zodpovedajuce%20typu%20investora%201 12 2025","url":"https://www.vub.sk/dam/jcr:30bc8c24-d247-4cfd-bb67-9b32cc6d4e22/Skupiny%20financnych%20nastrojov%20a%20produktov%20zodpovedajuce%20typu%20investora%201-12-2025.pdf"},{"title":"Jozef pode apresentar você a 3 pessoas na empresa InteractionUP","url":"https://sk.linkedin.com/in/jozefpuchon"},{"title":"Global Finance: najlepšia banka na Slovensku je VÚB","url":"https://sita.sk/global-finance-najlepsia-banka-na-slovensku-je-vub/"},{"title":"Slovak Investment Holding, Všeobecná úverová banka a Slovenská sporiteľňa zainvestujú do malých a stredných podnikov","url":"https://sita.sk/slovak-investment-holding-vseobecna-uverova-banka-a-slovenska-sporitelna-zainvestuju-do-malych-a-strednych-podnikov/"},{
… [2052 more characters]
```
</details>

→ `WebSearch` nový slovenský venture fond spustil 2025 startupy milióny eur partneri Bratislava

→ `WebSearch` nový slovenský fond rizikového kapitálu 2026 prvé uzavretie EIF Slovak

<details><summary>result</summary>

```
Web search results for query: "nový slovenský venture fond spustil 2025 startupy milióny eur partneri Bratislava"

Links: [{"title":"financovanie podnikania","url":"https://www.podnikajte.sk/temy/financovanie-podnikania?page=17"},{"title":"Andrej Kiska (Credo Ventures): Slovenskou startupovou scénu rozjíždí peníze z EU","url":"https://www.lupa.cz/clanky/andrej-kiska-credo-ventures-slovenskou-startupovou-scenu-rozjizdi-penize-z-eu/"},{"title":"monika majkova","url":"https://www.podnikajte.sk/autori/monika-majkova?page=6"},{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Venture to Future Fund increases capital by EUR 15.3 million to support Slovak startups","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups"},{"title":"Fresh 10 Million in Public Funding for Slovenian Startups in 2025 and Popular P2","url":"https://startup.si/en-us/news/fresh-10-million-in-public-funding-for-slovenian-startups-in-2025-and-popular-p2-"},{"title":"venture to future fund navysuje kapital o 15 3 miliona eur na podporu slovenskych startupov","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov"},{"title":"60-miliónový balík pre startupy je Slovákom blízko ako
… [1419 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "nový slovenský fond rizikového kapitálu 2026 prvé uzavretie EIF Slovak"

Links: [{"title":"V Česku vytvoria nový fond na podporu startupov s kapitálom 2,3 miliardy korún","url":"https://www.podnikajte.sk/investor/cesko-fond-startupy"},{"title":"2026 118 slovakia financing from eib group jumps 60 to eur649 million in 2025 with focus on energy upgrades and urban development","url":"https://www.eib.org/en/press/all/2026-118-slovakia-financing-from-eib-group-jumps-60-to-eur649-million-in-2025-with-focus-on-energy-upgrades-and-urban-development?lang=sk"},{"title":"Recherche FR menu Portail client du Groupe BEI","url":"https://www.eib.org/fr/press/all/2026-118-slovakia-financing-from-eib-group-jumps-60-to-eur649-million-in-2025-with-focus-on-energy-upgrades-and-urban-development?lang=sk"},{"title":"cmzrb podpori podnikatele formou kapitalovych investic","url":"https://ekonomickydenik.cz/cmzrb-podpori-podnikatele-formou-kapitalovych-investic/"},{"title":"Suche starten DE menü Kundenportal der EIB-Gruppe","url":"https://www.eib.org/de/press/all/2026-118-slovakia-financing-from-eib-group-jumps-60-to-eur649-million-in-2025-with-focus-on-energy-upgrades-and-urban-development?lang=sk"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=19066"},{"title":"Středoevropský fond fondů má k dispozici dvě miliardy","url":"https://www.e15.cz/byznys/finance-a-bankovnictvi/stredoevropsky-fond-fondu-ma-k-dispozici-dve-miliardy-1344949"},{"title":"Spravo
… [1766 more characters]
```
</details>

→ `WebSearch` SIH vybral správcu fondu rizikový kapitál plán obnovy venture fond výber finančného sprostredkovateľa

→ `WebFetch` https://www.sih.sk/en/stranky/financne-nastroje

<details><summary>result</summary>

```
The page lists three types of financial instruments. It does not name any specific equity or venture capital programmes, fund managers, or intermediaries.

1. **Loans:** Financing for investment and growth projects on favourable terms.
2. **Loan Guarantees:** Risk reduction for banks and other financial institutions, making it easier for businesses to obtain financing.
3. **Equity and Quasi-Equity Investments:** Investments in companies to support growth, innovation, and expansion into new markets.

**Links:**
- Financial Instruments page: https://www.sih.sk/en/stranky/financne-nastroje (the page you provided)
- Main website: https://www.sih.sk

For fund manager or intermediary details, check the Documents section or contact Slovak Investment Holding directly. The page does not link to those.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "SIH vybral správcu fondu rizikový kapitál plán obnovy venture fond výber finančného sprostredkovateľa"

Links: [{"title":"Finančné nástroje rizikového kapitálu, Výzva na prejavenie záujmu č. JER-005/2","url":"https://www.sih.sk/data/files/sih_antikorona_zaruka_final_30032020-337.docx"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/4623560.pdf"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/4793674.pdf"},{"title":"vs sih 2019 sk final 363","url":"https://www.sih.sk/data/files/vs_sih_2019_sk_final-363.pdf"},{"title":"První investiční VC fond z Národního plánu obnovy ČR bude spravovat Tensor Ventures","url":"https://www.businessinfo.cz/clanky/prvni-investicni-vc-fond-z-narodniho-planu-obnovy-cr-bude-spravovat-tensor-ventures/"},{"title":"1868604 dokument","url":"https://www.crz.gov.sk//data/att/1868604_dokument.pdf"},{"title":"investicie zo slovak investment holding vyhrali celoeuropsku sutaz","url":"https://sita.sk/investicie-zo-slovak-investment-holding-vyhrali-celoeuropsku-sutaz/"},{"title":"1850536 dokument1","url":"https://www.crz.gov.sk//data/att/1850536_dokument1.pdf"},{"title":"1990995 dokument1","url":"https://www.crz.gov.sk//data/att/1990995_dokument1.pdf"}]

Nenašiel som výsledok, ktorý by potvrdzoval, že SIH vybral správcu fondu rizikového kapitálu z Plánu obnovy. Našiel som však príbuzné informácie.

- **SIH v roku 2019:** Spoločnosť spolupracovala s trojicou správcov fondov (Vision Ventures, CB
… [1579 more characters]
```
</details>

→ `Bash` — Download SLSP Startup Report 2025 and grep investor names
```sh
mkdir -p [tmp] && cd [tmp] && curl -s -L -A "Mozilla/5.0" -o report.pdf "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/startup-report-slovensko-2025.pdf"; ls -la; file report.pdf; pdftotext -layout report.pdf report.txt && wc -l report.txt && grep -n -i -E "ventures|capital|fond|investor|anjel|angel" report.txt | head -150
```

<details><summary>result</summary>

```
total 4184
drwxr-xr-x   3 [user]  wheel       96 11 Oct  01:22 .
drwx------  33 [user]  wheel     1056 11 Oct  01:22 ..
-rw-r--r--   1 [user]  wheel  2138741 11 Oct  01:22 report.pdf
report.pdf: PDF document, version 1.5
    1550 report.txt
26:a 41 investorov                                                                 PODPORA PRE STARTUPY            33
30:                                                                                AKÍ SÚ SLOVENSKÍ INVESTORI?     38
45:ný report, ktorý by ukázal, ako sa náš startupový ekosystém        že diverzita je stále obrovskou výzvou. Pribudli anjelskí
46:mení a vyvíja v čase. Pred rokom sme od nášho dlhoročného          investori, no 6 z 10 z nich hovorí, že startupov na investo-
83:posilniť podporu inovácií. A jednou z možností je podpora         prostredníctvom nášho investičného fondu Seed Starter,
94:stoviek slovenských startupov a investorov a môže byť užitočný    Marek Sásik
398:                                                                             Prístup k investorom
697:financovať a rozbiehať ju bez externého kapitálu od investorov alebo bánk.
713:rozhodujeme sami, bez tlaku investorov a prísnych KPI. Napriek tomu nezatvárame
737:                                                                            16 %                     Anjelskí investori                            41 %
762:financovania, mali zahraničného investora.
778:Partner, Neulogy Ventures
779:„Slovensko potrebuje fondy s medzinárodným mandátom. Iba
… [2037 more characters]
```
</details>

→ `Bash` — Read investor section of SLSP startup report
```sh
cd [tmp] && sed -n 1105,1200p report.txt; grep -n -i -E "partner|managing|zakladateľ|CEO" report.txt | head -60; pdfinfo report.pdf | head -20
```

<details><summary>result</summary>

```
Akí sú slovenskí
investori?

                                38

AKÍ SÚ SLOVENSKÍ INVESTORI?




Investori sa
                                                                   Do akej fázy startupov
                                                                   najčastejšie investujete?


sústreďujú
na seed
fázy                                                         Pre-seed

                                                                 Seed
                                                                                                      61 %

                                                                                                             66 %

„Anjelov“ je viac, väčšina začala po roku 2020.               Series A                         32 %


Anjelskí investori tvoria veľmi rozmanitú skupinu –   Series B a neskôr              17 %
ich investície sa pohybujú od desiatok tisíc až po
milióny eur, no viac ako polovica z nich podporila                 Iné        10 %
najviac 3 startupy.

Aktivita anjelských investorov za posledných 5
rokov stúpla, mnohí z nich začali investovať až
po roku 2020. VC fondy pôsobiace na Slovensku
smerujú primárne kapitál do domácich firiem –
vo väčšine prípadov im to vyplýva z investičného
mandátu.



                                                                                                                    39

AKÍ SÚ SLOVENSKÍ INVESTORI?




Investície
                                                     Do ktorých
… [4457 more characters]
```
</details>

→ `WebSearch` venture capital funds headquartered in Slovakia list 2026 Bratislava VC firms

<details><summary>result</summary>

```
Web search results for query: "venture capital funds headquartered in Slovakia list 2026 Bratislava VC firms"

Links: [{"title":"Vision Ventures (Slovakia)","url":"https://altss.com/profile/vision-ventures-slovakia"},{"title":"9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"Top VC Funds In Slovakia To Finance Your Startup","url":"https://www.vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup"},{"title":"Top VCs & Startup Programs in Slovakia (2026) — Open Deadlines & Funding","url":"https://incubatorlist.com/top-vcs-in-slovakia"},{"title":"Slovak Investment Holding - 2026 Investor Profile, Portfolio, Team & Investment Trends - Tracxn","url":"https://tracxn.com/d/venture-capital/slovak-investment-holding/__tjVxlFXqLGRs2qT_DSyshq5mSj3rkiqhhq4iSORfe08"},{"title":"Startups in Slovakia - 2026 Latest Funding Rounds, Trends and News - Tracxn","url":"https://tracxn.com/d/geographies/slovakia/__MqqTYQpms3Zdt99rMUzg_DtPUg8Uhg9VCov-EX2e7jg"},{"title":"37 VC-Backed Startups in Bratislava, Slovakia Slovak Republic (2026)","url":"https://www.vcbacked.co/directory/cities/slovakia-slovak-republic/bratislava"},{"title":"Top 11 Venture Capitalist Funds (VCs) in Slovakia","url":"https://www.xyzlab.com/post/venture-capitalist-funds-vcs-in-slovakia"},{"title":"Top Venture Capital Firms & Investors in Slovakia in 2026","url":"https://www.openvc.app/country/Slovak
… [2053 more characters]
```
</details>

→ `WebFetch` https://www.openvc.app/country/Slovakia

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebFetch` https://incubatorlist.com/top-vcs-in-slovakia

→ `WebFetch` https://www.vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup

<details><summary>result</summary>

```
**Publication date:** October 8, 2020

| Fund | HQ | Fund size | Ticket | Focus (stage) |
|---|---|---|---|---|
| Neulogy Ventures | Bratislava | Over €23M invested to date | €200k–€1M | Multisector, mainly e-commerce, marketing, technology, financial, cybersecurity, medtech, cleantech (pre-seed/seed) |
| Vision Ventures | Bratislava | €11M under management | €100k–€800k | Various industries, Slovak companies aiming to scale internationally (seed) |
| 365.fintech | Not stated | Not stated | €50k–€500k | B2B and B2B2C fintech, insurtech, big data and business intelligence (seed) |
| Zero Gravity Capital | Not stated | Not stated | Undisclosed | Various industries, seed-stage ideas that could create or revolutionize markets |
| CB Investment Management | Bratislava | Not stated | Up to €1.6M | Various industries, early-stage Slovak startups with international potential (seed) |
| Innovations and Technologies Fund | Not stated | Not stated | €20k–€1.5M | Environment, renewable energy, e-commerce, IT, industrial innovation, telecom, software, life-improving tech (seed) |
| LRJ Capital | Not stated | Not stated | €100k–€2M (typical ~€0.5M) | Various industries, companies with world-market leadership potential (seed) |
| Eterus Capital | Bratislava | Not stated | €500k–€5M | Small and medium companies across sectors with growth potential; PE fund that also makes venture investments (seed+) |
| IPM Growth | Not stated (managed by IPM Group) | Undisclosed | Undisclosed | InfraTech: m
… [67 more characters]
```
</details>

<details><summary>result</summary>

```
The page lists 14 programs. Check sizes are shown only where the page states them.

| # | Name | Type | HQ (as stated) | Check size / offer |
|---|---|---|---|---|
| 1 | European Innovation Council (EIC) - Accelerator Program | Accelerator | Brussels, Belgium | Not stated (grant, equity) |
| 2 | Zero Gravity Capital | Investment Fund / VC Firm | Bratislava, Slovakia | Not stated |
| 3 | Use GForce | VC Firm | Bratislava, Slovakia | €250K |
| 4 | 365.fintech | Corporate VC | Bratislava, Slovakia | Not stated |
| 5 | Venture to Future Fund | Private Equity Firm | Bratislava, Slovakia | Not stated |
| 6 | ProPartners | Private Equity Firm | Bratislava, Slovakia | Not stated |
| 7 | Monopoly Ventures | Other | Slovakia (no city stated) | $5,000 – $1,000,000 |
| 8 | G-Force VC | VC Firm | Nivy Tower, Slovakia | $250 – $250,000 |
| 9 | Crowdberry | Private Equity Firm | Slovak Republic, Slovakia | Not stated |
| 10 | Launcher | Incubator / Accelerator | Bratislava, Slovakia | Not stated |
| 11 | Sandberg Capital | Private Equity Firm | Bratislavský Kraj, Slovakia | Not stated |
| 12 | Plug and Play Tech Center - Batch Program | Accelerator (also VC, co-working, university program) | Sunnyvale, USA (multiple locations listed) | $50K – $1M |
| 13 | Techstars - Winter Cohort Applications | Accelerator / VC Firm | Boulder, USA | Not stated |
| 14 | EIT Digital Venture Program | Growth Program / Accelerator / VC Firm | Brussels, Belgium | 25K |

Status: Plug and Play, Techstars, and EIT
… [123 more characters]
```
</details>

→ `WebSearch` "GForce" OR "G-Force" climate tech pre-seed fund Bratislava investícia

→ `WebSearch` "Monopoly Ventures" Slovakia

→ `WebSearch` "IPM Growth" InfraTech fund Slovakia IPM Group

<details><summary>result</summary>

```
Web search results for query: ""Monopoly Ventures" Slovakia"

Links: [{"title":"game board","url":"https://ncsml.emuseum.com/objects/16845/game-board"},{"title":"Monopoly Mega Slovensko","url":"https://www.tlamagames.com/en/board-games/monopoly-mega-slovensko"},{"title":"www.caselex.eu","url":"https://www.caselex.eu/?p=3290"},{"title":"Monopoly Slovensko je prekrásne","url":"https://www.tlamagames.com/en/board-games/monopoly-slovensko-je-prekrasne"},{"title":"2. October 2000 at 00:00","url":"https://spectator.sme.sk/business/c/business-briefs-36"},{"title":"Martindale Retrospective - Slovenia, Czechoslovakia, Germany","url":"https://flippingbook.lehigh.edu/Martindale-Retrospective---Slovenia,-Czechoslovakia,-Germany/4"},{"title":"MONOPOLY Wonders of Slovenia","url":"https://b2b.colby.si/monopoly-wonders-of-slovenia"},{"title":"Slovakia Country Commercial Guide","url":"https://www.trade.gov/knowledge-product/slovakia-distribution-and-sales-channels"},{"title":"Slovakia Country Commercial Guide","url":"https://trade.gov/country-commercial-guides/slovakia-distribution-and-sales-channels"},{"title":"3. July 1997 at 00:00","url":"https://spectator.sme.sk/business/c/broken-slovnaft-monopoly-paves-way-for-foreign-gas-stations"}]

The search didn't turn up any company called "Monopoly Ventures" in Slovakia. The results were mostly about the Monopoly board game and unrelated Slovak business news.

- **Monopoly board game editions:** A 2004 Slovak-language Monopoly set is held by the N
… [961 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""GForce" OR "G-Force" climate tech pre-seed fund Bratislava investícia"

Links: [{"title":"Connect with us","url":"https://www.innovatorsmag.com/?p=35875"},{"title":"Frontier Technology","url":"https://www.innovatorsmag.com/calling-climate-tech-startups/amp/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/g-force"},{"title":"G-Force team","url":"https://techcrunch.com/2021/09/06/founders-factory-and-g-force-launch-seed-program-for-climate-focused-startups/amp/"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/g-force-1"},{"title":"Compare G-Force vs Net Zero Ventures","url":"https://www.cbinsights.com/compare/g-force-1-vs-net-zero-ventures"},{"title":"IncubatorListincubator listIncubatorList","url":"https://incubatorlist.com/top-vcs-in-slovakia"},{"title":"IncubatorListincubator listIncubatorList","url":"https://incubatorlist.com/top-startup-accelerators-incubators-and-vcs-in-slovakia"},{"title":"Compare G-Force vs Pace Ventures","url":"https://www.cbinsights.com/compare/g-force-1-vs-pace-ventures"},{"title":"G Force","url":"https://www.openvc.app/fund/G-Force"}]

G-Force is a Bratislava-based pre-seed climate tech investor, founded in 2021. It runs the Founders Factory Sustainability Seed Program, which offers early-stage climate startups seed funding and support.

- **Focus and stage:** One profile describes the fund as investing in climate tech comp
… [1416 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""IPM Growth" InfraTech fund Slovakia IPM Group"

Links: [{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"infratech investment pioneer ipm tackles the big themes of the coming decades 181060","url":"https://intellinews.com/infratech-investment-pioneer-ipm-tackles-the-big-themes-of-the-coming-decades-181060"},{"title":"ipm growth","url":"https://www.vestbee.com/vc-list/ipm-growth"},{"title":"194093 ipm group","url":"https://open.endole.co.uk/insight/brand/194093-ipm-group"},{"title":"Description of the company","url":"https://www.profesia.sk/en/work/infrapartners-management/C191741"},{"title":"top of page","url":"https://www.symsite.sk/single-post/ipm-raised-200m-from-investors-across-various-projects"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/peter-gajdos-sa-pripojil-k-ipm-do-tim/432852-clanok.html"},{"title":"marian bocek","url":"https://crunchbase.com/person/marian-bocek"},{"title":"ipm group 154047","url":"https://www.devex.com/organizations/ipm-group-154047"}]

IPM Growth is a venture fund run by IPM Group, a Bratislava-linked investment firm focused on infrastructure technology.

- **Fund and manager:** The fund is managed by asset and wealth management company IPM Group. It targets a funding gap for local and innovative scaleups with a global approach, mainly in mobility, AI-enabled infrastruct
… [1134 more characters]
```
</details>

→ `Bash` — Show final part of ORSR batch output
```sh
sed -n '/##### Monogram/,$p' [tmp] | cut -c1-700
```

<details><summary>result</summary>

```
##### Monogram
== MONOGRAM Multimedia s.r.o. | https://www.orsr.sk/vypis.asp?ID=109382&SID=2&P=0
IČO: 36 849 758 | Sídlo: Ilkovičova 6276, Bratislava 842 16 | zápis: 20.10.2007
Spoločníci: MONOGRAM Ventures a.s. IČO: 44 071 574 / Ilkovičova 6276 / Bratislava - mestská časť Karlova Ves 842 16 / (od: 04.01.2023) /
Vklady: MONOGRAM Ventures a.s. / Vklad: 70 364 EUR ( peňažný vklad ) Splatené: 70 364 EUR / (od: 04.01.2023) /
== MONOGRAM Ventures a. s. | https://www.orsr.sk/vypis.asp?ID=124603&SID=2&P=0
IČO: 44 071 574 | Sídlo: Ilkovičova 6276, Bratislava 842 16 | zápis: 08.04.2008
##### LRJ
== LRJ, s.r.o. | https://www.orsr.sk/vypis.asp?ID=402613&SID=5&P=0
IČO: 51 157 705 | Sídlo: Dolné Rudiny 2956/8, Žilina 010 01 | zápis: 17.10.2017
Spoločníci: Lukáš Melišík / Dátum narodenia: 11.04.1988 / (od: 15.04.2022) /
Vklady: Lukáš Melišík / Vklad: 5 000 EUR Splatené: 5 000 EUR / (od: 15.04.2022) /
##### Pioneers Ventures
##### Arca Capital Slovakia
== Arca Capital Slovakia, a.s. | https://www.orsr.sk/vypis.asp?ID=39276&SID=2&P=0
IČO: 35 868 856 | Sídlo: Plynárenská 7/A, Bratislava 821 09 | zápis: 30.10.2003
Akcionár: Arca Investments, a.s., v reštrukturalizácii IČO: 35 975 041 / Plynárenská 7/A / Bratislava 821 09 / (od: 15.11.2022) / Ďalšie právne skutočnosti: / Spoločnosť bola založená zakladateľskou zmluvou vo forme notárskej zápisnice č. N 917/03, Nz 80441/03 zo dňa 12.9.2003 v zmysle ust. § § 154 a nasl. Zák. č. 513/1991 Zb. bez výzvy na upisovanie akcií. / (od: 30.10.2003) / O
… [8843 more characters]
```
</details>

→ `Bash` — Prepare second ORSR batch script
```sh
cd [tmp] && cat > batch2.sh <<'EOF'
cd "$(dirname "$0")"
for n in "National Development Fund II" "CB Investment Management" "CB ESPRI" "G-Force" "GForce" "ProPartners" "Launcher" "Klub podnikateľských anjelov" "Slovak Business Angels" "SEED STARTER" "Seed Starter Slovenskej" "Investeers" "Pioneers" "Credo" "Presto" "J&T VENTURES" "INNOVATION FUND" "Inovačný fond" "Startlab" "Fintech Ventures" "Across Ventures" "Ethernum" "Slovak Asset" "SAM - Slovak" "Benson Oak" "Rockaway" "Purple Ventures" "Tachyum"; do echo "##### $n"; python3 orsr.py brief "$n" | cut -c1-600; done
EOF
chmod +x batch2.sh
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Run second ORSR batch lookup
```sh
[tmp] > [tmp] 2>&1
```

<details><summary>result</summary>

```
Command running in background with ID: be5m6wp0c. Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
```
</details>

→ `WebSearch` Monogram Ventures investícia startup 2024 2025

→ `WebSearch` LRJ Capital investícia startup Slovensko

→ `WebSearch` ProPartners private equity Bratislava investícia

<details><summary>result</summary>

```
Web search results for query: "Monogram Ventures investícia startup 2024 2025"

Links: [{"title":"monogram ventures","url":"https://insights.munich-startup.de/investors/monogram_ventures"},{"title":"Monogram Capital Closes Debut Fund at $152M | Global AgInvesting","url":"https://globalaginvesting.com/monogram-capital-closes-debut-fund-152m/"},{"title":"Funding news","url":"https://www.trysignalbase.com/news/funding/monogram-secures-400"},{"title":"seed funding monogram 40m visual ai","url":"https://under30ceo.com/seed-funding-monogram-40m-visual-ai"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/monogram"},{"title":"Get an email the moment Monogram raises again","url":"https://seedtable.com/companies/monogram/funding-rounds/seed-2026-07"},{"title":"www.under30ceo.com","url":"https://www.under30ceo.com/?p=135679"},{"title":"Translated by","url":"https://us.fashionnetwork.com/news/Monogram-raises-nearly-3-million,1509540.html"},{"title":"Translated by","url":"https://uk.fashionnetwork.com/news/Monogram-raises-nearly-3-million,1509539.html"}]

I found no evidence of a Monogram Ventures investment in 2024 or 2025. The results mostly describe other companies with similar names.

- **Monogram Ventures (Bratislava):** A Caplight profile describes this as a seed-stage VC focused on tech startups. It lists only two portfolio companies, both from 2011, and its 2024–2025 activity is behind a paywall. Monogram V
… [928 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "LRJ Capital investícia startup Slovensko"

Links: [{"title":"the biggest investment in fintech startup in slovakia goes to finax","url":"https://www.finax.eu/en/blog/the-biggest-investment-in-fintech-startup-in-slovakia-goes-to-finax"},{"title":"Exponea ohlásila investíciu 15 miliónov. Dobyjú Slováci startupový svet?","url":"https://www.startitup.sk/?p=334505"},{"title":"Slovenský startup získal investíciu 1,5 milióna eur","url":"https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/"},{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/kolko-milionov-eur-je-dnes-dostupnych-pre-slovenske-projekty/"},{"title":"Koľko miliónov eur je dnes dostupných pre slovenské projekty?","url":"https://www.startitup.sk/?p=50283"},{"title":"Slovenská startup hviezda vraj ešte nevyšla. Vieme prečo","url":"https://www.startitup.sk/?p=42967"},{"title":"top of page","url":"https://www.symsite.sk/single-post/2020/01/02/largest-investments-into-slovak-start-ups"},{"title":"Startupový rok 2015","url":"https://www.startitup.sk/startupovy-rok-2015/"},{"title":"Startupový rok 2015","url":"https://www.startitup.sk/?p=17892"}]

Search results show LRJ Capital, the investment holding linked to Ivan Chrenko, has backed several Slovak startups:

- **Finax (2019):** LRJ Capital invested €1.5 million through its GROWWS SICAV fund, which the Finax team called the largest fintech investment in Slovak startup
… [1453 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "ProPartners private equity Bratislava investícia"

Links: [{"title":"Private Equity","url":"https://altss.com/profile/pro-partners-holding"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/pro-partners-holding"},{"title":"Pro Partners Holding","url":"https://foundersuite.com/firms/pro-partners-holding"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=74309"},{"title":"Pro Partners Holding","url":"https://www.arounddeal.com/c/pro-partners-holding/f9pzxggrer"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=90348"},{"title":"Jesteś w trybie podpowiedzi Wyłącz","url":"https://cbonds.pl/company/55873/"},{"title":"Private Equity","url":"https://altss.com/profile/hkk-partners"},{"title":"www.epravo.sk","url":"https://www.epravo.sk/top/aktualne/?pg=8"}]

Pro Partners Holding is a Bratislava-based investment group that describes itself as active in private equity, real estate, and finance across Central and Eastern Europe. Sources mostly agree on its focus, but they differ on basics and offer little verified detail.

- **Profile:** One directory describes it as a Bratislava-based investment holding and venture capital firm backing companies across Slovakia and Central and Eastern Europe. It lists stages from early-stage VC to buyouts and M&A.
- **Portfolio:** Its named investments are energy and AI companies, including FUERGY and Tachyum.
- **F
… [938 more characters]
```
</details>

→ `WebSearch` "Jinej fond" startup investor

→ `WebSearch` slovenský startup získal investíciu od fondu 2025 "fond" seed kolo Slovensko investori viedol

<details><summary>result</summary>

```
Web search results for query: ""Jinej fond" startup investor"

Links: [{"title":"Jinej fond dvou podnikatelských generací. Jiří Hlavenka a Jan Sláma startují společné investice do začínajících startupů","url":"https://cc.cz/jinej-fond-dvou-podnikatelskych-generaci-jiri-hlavenka-a-jan-slama-startuji-spolecne-investice-do-zacinajicich-startupu/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/jinej"},{"title":"jinej fond","url":"https://prod.actual.seedtable.com/investors/jinej-fond"},{"title":"j ventures fund","url":"https://superscout.co/investor/j-ventures-fund"},{"title":"Founder to Funder – the journey from startup founder to startup investor","url":"https://www.mie.utoronto.ca/?p=43552"},{"title":"lauder.wharton.upenn.edu","url":"https://lauder.wharton.upenn.edu/?p=4264"},{"title":"j ventures","url":"https://superscout.co/investor/j-ventures"},{"title":"jibevc com","url":"https://superscout.co/investor/jibevc-com"},{"title":"jia xiang yi","url":"https://www.vcsheet.com/who/jia-xiang-yi"}]

Jinej Fond is a small venture fund run by two Czech entrepreneurs, Jiří Hlavenka and Jan Sláma, and it backs very early-stage startups.

- **Origins:** A Czech Crunch-linked article reports that the pair launched the fund in Brno, looking for projects at the very earliest stage of development. Beyond money, they can offer their broad contacts, energy and experience, and they had already made a third investment worth a few million Czech crowns.
- **Fou
… [903 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "slovenský startup získal investíciu od fondu 2025 "fond" seed kolo Slovensko investori viedol"

Links: [{"title":"Seed Starter Slovenskej sporiteľne investuje 400-tisíc eur do startupu Webout. Ten získava spolu 1,65 milióna eur a mieri do Silicon Valley","url":"https://www.omediach.com/internet/30236-seed-starter-slovenskej-sporitelne-investuje-400-tisic-eur-do-startupu-webout-ten-ziskava-spolu-1-65-miliona-eur-a-mieri-do-silicon-valley"},{"title":"Zo Slovenska rovno na najväčší realitný trh. IntellCRE získava investíciu od Seed Startera Slovenskej sporiteľne","url":"https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne"},{"title":"Startup Awards Slovensko 2025: Vyhral inovatívny CultiWise","url":"https://www.startitup.sk/najlepsi-startup-ziskal-250-000-eur-tieto-firmy-su-buducnostou-slovenskej-ekonomiky/"},{"title":"Michal a Karel získali 1,65 milióna eur. Teraz s revolučným nápadom mieria do Silicon Valley","url":"https://www.startitup.sk/michal-a-karel-ziskali-165-miliona-eur-teraz-s-revolucnym-napadom-mieria-do-silicon-valley/"},{"title":"Česko-slovenský startup získava miliónovú investíciu. Dokonale vyplnil dieru na trhu","url":"https://www.startitup.sk/cesko-slovensky-startup-ziskava-milionovu-investiciu-dokonale-vyplnil-dieru-na-trhu/"},{"title":"Startupov máme málo a ešte menej do nich investujeme. Fond Seed Starter ale hlási prvé investí
… [2607 more characters]
```
</details>

→ `WebFetch` https://www.forbes.sk/cequence-investicia-jet-ventures-slido-ai-platforma/

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebFetch` https://www.omediach.com/internet/30236-seed-starter-slovenskej-sporitelne-investuje-400-tisic-eur-do-startupu-webout-ten-ziskava-spolu-1-65-miliona-eur-a-mieri-do-silicon-valley

<details><summary>result</summary>

```
**Publication date:** 8 June 2026 (listed as 08.06.2026).

**Seed Starter investment and round size:** The headline reads "Seed Starter Slovenskej sporiteľne investuje 400-tisíc eur do startupu Webout." It adds that the startup "Ten získava spolu 1,65 milióna eur a mieri do Silicon Valley." So Seed Starter contributes €400,000 to a round totaling €1.65 million.

**Co-investors:** The article names two other investors, the funds Energy Venture Pals and JIC Ventures: "Ďalšími investormi sú fondy Energy Venture Pals a JIC Ventures."
```
</details>

→ `WebSearch` "Energy Venture Pals" fond

→ `WebSearch` "Jet Ventures" Cequence investícia fond Slovensko

<details><summary>result</summary>

```
Web search results for query: ""Energy Venture Pals" fond"

Links: [{"title":"Energy Venture Pals Overview","url":"https://pitchbook.com/profiles/investor/1405189-00"},{"title":"Energy Venture Pals (investor - Others)","url":"https://nordic9.com/companies/energy-venture-pals/"},{"title":"Funding round closed","url":"https://sciencebusiness.net/news/71044/Energy-Ventures-closes-its-third-fund-at-%24243M"},{"title":"energy ventures breaks record with new fund","url":"https://www.unquote.com/nordics/official-record/89331/energy-ventures-breaks-record-with-new-fund"},{"title":"$250 million venture capital firm Piva targets the energy industry","url":"https://www.axios.com/2019/12/11/piva-venture-capital-fund-energy"},{"title":"Energy Ventures closes its third fund at $243M","url":"https://sciencebusiness.net/news/71044/Energy-Ventures-closes-its-third-fund-at-$243M"},{"title":"norway energy ventures closes new fund on nok 13bn","url":"https://www.unquote.com/unquote/news/97883/norway-energy-ventures-closes-new-fund-on-nok-13bn"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/energy-ventures"},{"title":"All funds of Venture Investment Associates","url":"https://seedtable.com/investors/venture-investment-associates/funds/venture-investment-associates-energy-ii-lp"}]

The search returned little on a fund specifically named "Energy Venture Pals." The results point to a small Czech investor, and several other results concern a differently named firm
… [954 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Jet Ventures" Cequence investícia fond Slovensko"

Links: [{"title":"Chceme z Česka moderní ekonomiku, ne skanzen, říká šéf Jet Ventures a vyjmenovává 5 největších překážek","url":"https://cc.cz/chceme-z-ceska-moderni-ekonomiku-ne-skanzen-rika-sef-jet-ventures-a-vyjmenovava-5-nejvetsich-prekazek/"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/cequence-secures-2-m"},{"title":"Slováci automatizují řešení smluv pro Dell či Notino. Desítky milionů mají od miliardáře Faita","url":"https://cc.cz/slovaci-automatizuji-reseni-smluv-pro-dell-ci-notino-desitky-milionu-maji-od-miliardare-faita/"},{"title":"faitova jet investment investuje do startupu cequence ulehci spravovani smluv","url":"https://forbes.cz/faitova-jet-investment-investuje-do-startupu-cequence-ulehci-spravovani-smluv/"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/cequence-raises-2m-for-ai-contracts"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/jet-investment-invests-1-7m-in-cequence"},{"title":"v podpore startupu silene zaostavame burcuje lidr fondu jet ventures levinsky","url":"https://forbes.cz/v-podpore-startupu-silene-zaostavame-burcuje-lidr-fondu-jet-ventures-levinsky/"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/seznam-advertorial-nejde-jen-o-kapital-skutecnou-hodnotu-tvori-aktivni-rizeni-rika-marek-malik-z-jet-investment-293384"},{"title":"ceske vc fondy jsou casto jen ce
… [1763 more characters]
```
</details>

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/arx-equity-partners.html

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/cvi.html

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/vision-ventures.html

<details><summary>result</summary>

```
**CVI Dom Maklerski Sp. z o.o.** is a full member of SLOVCA, the Slovak Venture Capital & Private Equity Association.

- **Description:** The firm manages about EUR 800 million. It provides direct lending, senior debt, and mezzanine financing, and occasionally makes minority equity investments. Its preferred investment size is EUR 2 to 15 million. It has no sector preference and focuses on Central and Eastern Europe (CEE).
- **Address:** Plac Europejski 2, bldg C, 00-844 Warsaw, Poland
- **Website:** www.cvi.eu
- **Contact:** Radoslav Tausinger, [redacted: email address]
```
</details>

<details><summary>result</summary>

```
**ARX Equity Partners** is a full member (Riadni člen) of SLOVCA, the Slovak Venture Capital & Private Equity Association.

- **Description:** The profile has no narrative description. It lists these details:
  - Preferred investment size: EUR 10–50 million
  - Assets under management: EUR 300 million in total commitments since inception
  - Sector preference: none
  - Geographic focus: Central Europe
- **Address:** The page gives no address for ARX. The only address listed is SLOVCA's office: Štúrova 12/4, 811 02 Bratislava-Staré Mesto, Slovakia.
- **Website:** https://arxequity.com/
- **Contact person:** Michal Aron
- **Email:** [redacted: email address]
- **Phone:** The page lists only SLOVCA's number, +421-2-21 201 010, not one for ARX.
```
</details>

<details><summary>result</summary>

```
**Vision Ventures**

- **Description:** Venture capital investor (Pre-Seed and Seed stages) focused on early-stage technology companies. Its stated preferred sector is "Technologické projekty v ranných štádiách s významným rastovým potenciálom a globálnym dosahom." Geographic focus is the Slovak Republic.
- **Address:** Bottova 2A, Bratislava, Staré Mesto 811 09, Slovakia
- **Website:** www.visionventures.vc
- **Fund size:** Not listed on the page.
- **Tickets:** Preferred investment size is €200,000 to €1.6 million.
```
</details>

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html

<details><summary>result</summary>

```
**Neulogy Ventures**

- **Description:** The page has no narrative company description. It lists investment types (seed and venture capital) and a portfolio of 25 companies.
- **Address:** Tallerova 2/4, 81102 Bratislava, Slovakia
- **Website:** www.neulogy.vc/sk
- **Assets under management:** EUR 26 million
- **Preferred investment size:** EUR 200,000 to 2.5 million per investment
- **Sector focus:** Information and communication technologies, energy, and medical diagnostics
- **Geographic focus:** Slovakia (28 transactions in Slovakia to date)
- **Contact:** +421 2 2077 4437, [redacted: email address]
```
</details>

<details><summary>result</summary>

```
**Sandberg Capital**

- **Description:** The page has no narrative description. It lists investment preferences only.
- **Address:** Dvořákovo Nábrežie 8, 81102 Bratislava, Slovakia
- **Website:** www.sandbergcapital.com
- **AUM:** Not listed on the page.
- **Preferred investment size:** €4M to €15M
- **Sectors:** IT, education, and food and agriculture. It favors companies with recurring revenue and essential products or services, with a B2B focus.
- **Geography:** Slovakia, Czechia, surrounding CEE countries, and the Balkans.
```
</details>

<details><summary>result</summary>

```
**Eterus Capital**

- **Description:** A private equity investor and full member of SLOVCA, the Slovak Venture Capital & Private Equity Association. It focuses on businesses in the development stage of their lifecycle, particularly in sectors with strong growth potential and higher value added.
- **Address:** Laurinská 18, 811 01 Bratislava, Slovakia
- **Website:** www.eterus.sk
- **AUM:** Not stated on the page.
- **Preferred investment size:** €500 thousand to €5 million
- **Sector:** Higher value-added industries, with a focus on development-stage opportunities in high-growth sectors
- **Geography:** Slovak Republic
- **Investment type:** Private equity
```
</details>

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/venture-to-future-fund.html

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/fond-inovacii-a-technologii.html

→ `WebFetch` https://www.slovca.sk/sk/riadni-clenovia/narodny-holdingovy-fond-s-r-o.html

<details><summary>result</summary>

```
**Venture to Future Fund**

- **Description:** The page has no narrative description. It is a full member (riadny člen) of SLOVCA, the Slovak Venture Capital & Private Equity Association, and lists its investment stages as Series Seed, Series A, Series B, and later rounds.
- **Address:** Grösslingová 44, 811 09 Bratislava, Slovakia
- **Website:** https://vff.sk/
- **Email:** [redacted: email address]
- **AUM:** Not stated on the page.
- **Preferred investment size:** €0.5 to 4.8 million per investment.
- **Sector:** Innovative SMEs and technology SMEs.
- **Geography:** Slovakia and the EU.
- **Portfolio companies listed:** Nettle.AI, SEC Technologies, AgeVolt.
```
</details>

<details><summary>result</summary>

```
**Fond inovácií a technológií** (Fund for Innovation and Technology) is a full member of SLOVCA, the Slovak Venture Capital & Private Equity Association.

- **Description:** Invests in early- and later-stage companies, including seed, start-up, spin-off, and expansion companies.
- **Address:** Not listed on the page. The only address shown is SLOVCA's own office in Bratislava-Staré Mesto.
- **Website:** https://www.fondfit.sk/
- **AUM:** Not stated.
- **Preferred investment size:** From €20,000 to €1,500,000.
- **Investment horizon:** Four to six years.
- **Sector:** No specific sector is named. The stated focus is on company stage.
- **Geography:** The investee company must have its seat in Slovakia and carry out at least part of its activities there.
```
</details>

<details><summary>result</summary>

```
**Národný holdingový fond s.r.o.**

- **Description:** A Slovak venture capital and private equity firm and member of SLOVCA. It invests in seed, start-up, and expansion-stage companies and has completed 91 investment transactions since it was founded. Its current Slovak portfolio includes 20 equity-backed companies and 20 companies that received loans.
- **Address:** Karadžičova 2, 811 09 Bratislava, Slovakia
- **Website:** www.nhfond.sk
- **Contact:** +421 2 3810 2440; [redacted: email address]
- **AUM:** Not stated on the page.
- **Preferred investment size:** About €200,000 to €266,000 per investment.
- **Sector:** Innovation and technology.
- **Geography:** Slovakia only.
```
</details>

→ `WebFetch` https://www.fondfit.sk/

→ `WebFetch` https://www.nhfond.sk/

<details><summary>result</summary>

```
**Is the site live?** The text can't confirm this. It has navigation and contact details, but no publication or update dates. The footer reads "Copyright 2014 -" with no end year.

**NHF status:** The page describes Národný holdingový fond as a "Špecializovaná dcérska spoločnosť Slovak Business Agency," a specialized subsidiary of Slovak Business Agency. It provides risk capital by contributing to companies' registered capital, targets growth-oriented projects, and aims to steer the other funds toward developing small and medium enterprises across Slovakia.

**Funds managed:** Three risk-capital funds are listed: Národný holdingový fond, Fond inovácií a technológií (FIT), and Eterus Capital. The page doesn't state fund sizes or total capital managed.

**Current investing activity:** None is stated. The Eterus and FIT sections describe their investment approach in general terms only.

**Portfolio with dates:** None is listed. The page names no portfolio companies and gives no investment dates.
```
</details>

<details><summary>result</summary>

```
**Is the site live?** The page appears to be a current, working site. It has navigation, a cookie consent banner, a 2024 copyright notice, and a sustainability document with a 2026 upload date. I can't verify live status from the text alone.

**FIT status:** The page states: "Fond inovácií a technológií vstúpil v roku 2025 do post-investičnej fázy." In English, the fund entered its post-investment phase in 2025, and the notice is addressed to prospective investors. The page describes FIT as more than 10 years old and says it was formed through cooperation between the Slovak Business Agency (SBA) and investors.

**Portfolio (five listed companies, no dates or amounts):**
- Elearn.Aero (IT technologies)
- Futureplastix (manufacturing)
- Trigen (technologies, manufacturing)
- COGNEXA (IT technologies)
- DATAMOLINO (IT technologies)

**Investments with dates:** None are listed. The only date is the 2025 post-investment phase notice.

**Tickets:** The page contains no investment ticket, deal size, or valuation information.
```
</details>

→ `Bash` — Show second ORSR batch output
```sh
cat [tmp] | cut -c1-500
```

<details><summary>result</summary>

```
##### National Development Fund II
```
</details>

→ `WebFetch` https://www.caplight.com/investor/g-force

→ `WebSearch` G-Force Marian Gazdik climate fund invests startup 2025 2026 Bratislava "G-Force"

<details><summary>result</summary>

```
**Headquarters:** Bratislava, Bratislava Region

**Description:** G-Force is a pre-seed venture capital fund that invests in climate tech startups with scalable technologies for reducing greenhouse gas emissions. Beyond capital, it offers hands-on operational support with Founders Factory and help securing non-dilutive grants. It focuses on pre-seed and seed-stage companies.

**Portfolio companies (listed on the page):**

| Company | Date | Round Type | G-Force Role |
|---|---|---|---|
| Enzidia ApS | Mar 2025 | Accelerator | Lead |
| Brightly | Dec 2024 | Seed | Co-investor |
| Good Agriculture | Sep 2024 | Pre-Seed | Co-investor |
| Ki Hydrogen | Jul 2024 | Accelerator | Co-investor |
| Oleo | Apr 2024 | Seed | Co-investor |

**Number of investments:** The page lists 11 portfolio companies. It shows only five in the table above, and the full investment list requires a demo request.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "G-Force Marian Gazdik climate fund invests startup 2025 2026 Bratislava "G-Force""

Links: [{"title":"investing in the climate revolution","url":"https://foundersfactory.substack.com/p/investing-in-the-climate-revolution"},{"title":"marian gazdik","url":"https://www.vcsheet.com/who/marian-gazdik"},{"title":"G-Force team","url":"https://techcrunch.com/2021/09/06/founders-factory-and-g-force-launch-seed-program-for-climate-focused-startups/amp/"},{"title":"Seedrs Offers Investors Access to Green Fund by G Force","url":"https://www.crowdfundinsider.com/2023/10/214476-seedrs-offers-investors-access-to-green-fund-by-g-force/"},{"title":"Seedrs Offers Investors Access to Green Fund by G Force","url":"https://www.crowdfundinsider.com/?p=214476"},{"title":"Who we are","url":"https://g-force-fund-ii.seedrs.com"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/g-force-1/people"},{"title":"Header Hero logoHeader Hero logo","url":"https://foundersfactory.com/g-force/"},{"title":"Compare G-Force vs Net Zero Ventures","url":"https://www.cbinsights.com/compare/g-force-1-vs-net-zero-ventures"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/g-force-1"}]

The search didn't turn up any 2025 or 2026 announcements from G-Force. The most recent material is from 2023, so I can't confirm any new investments in that period.

- **Leadership:** G-Force is run by Marian Gazdik and Louis Warner, with Gazdik's background in Startup
… [1417 more characters]
```
</details>

→ `WebFetch` https://g-force-fund-ii.seedrs.com

<details><summary>result</summary>

```
error:10000410:SSL routines:OPENSSL_internal:SSLV3_ALERT_HANDSHAKE_FAILURE
```
</details>

→ `WebFetch` https://www.crowdfundinsider.com/2023/10/214476-seedrs-offers-investors-access-to-green-fund-by-g-force/

<details><summary>result</summary>

```
**Publication date:** October 17, 2023, at 10:47 am.

**Fund size:** "The G-Force Fund II is a €20 million vehicle that Seedrs investors will be able to participate in at a lower cost."

**Ticket size:** The article doesn't state a minimum or maximum investment. It says only that "Additional information on G-Force Fund II is only available for registered, eligible investors."

**Location and fund vehicle:** The article doesn't say where G-Force is based or what legal jurisdiction the vehicle is established under. It describes the G-Force Fund II as a €20 million vehicle, managed by partners Marian Gazdik and Louis Warner.
```
</details>

→ `WebFetch` https://www.vestbee.com/vc-list/ipm-growth

→ `WebFetch` https://intellinews.com/infratech-investment-pioneer-ipm-tackles-the-big-themes-of-the-coming-decades-181060

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

<details><summary>result</summary>

```
- **HQ:** Not stated. The page lists Slovakia, China, South Korea, UK, and USA without identifying which is the headquarters.
- **Fund size:** Not stated.
- **Ticket size:** "€25K to €5M+"
- **Stage:** Growth
- **Sectors:** AI, Automotive/Transport, Energy, Mobility, InfraTech
- **Portfolio:** Matsuko (remote communication) and Tachyum (processor provider).
- **Founders:** No founder names are listed. The fund offers founders strategic advisory and global knowledge transfer, including from Silicon Valley to Central and Eastern Europe.
```
</details>

→ `WebSearch` IPM Group investícia startup Matsuko Brightpick Photoneo IPM fond rizikový kapitál

→ `Bash` — Check second ORSR batch output
```sh
cat [tmp] | cut -c1-500
```

<details><summary>result</summary>

```
##### National Development Fund II
```
</details>

<details><summary>result</summary>

```
Web search results for query: "IPM Group investícia startup Matsuko Brightpick Photoneo IPM fond rizikový kapitál"

Links: [{"title":"AUTOMATION NEWS CENTER","url":"https://www.automate.org/robotics/news/photoneo-raises-21-million-in-series-b/anc"},{"title":"Date14th, Dec 2021","url":"https://statnano.com/world-news/89705/Photoneo-Set-to-Advance-Sensor-Business-Automation-Solutions"},{"title":"photoneo raises 21 million in series b","url":"https://automate.org/robotics/news/photoneo-raises-21-million-in-series-b"},{"title":"Photoneo raises $21m Series B funding","url":"https://logisticsbusiness.com/materials-handling/automation-systems-shuttles/photoneo-raises-dollarm-series-b-funding-2/"},{"title":"photoneo raises 21m brightpick logistics automation","url":"https://imveurope.com/news/photoneo-raises-21m-brightpick-logistics-automation"},{"title":"Photoneo raises $21m Series B funding","url":"https://logisticsbusiness.com/tag/automationitwarehouse-automation"},{"title":"Bratislava, Slovakia, 7 December 2021","url":"https://www.automate.org/robotics/news/photoneo-raises-21-million-in-series-b/aph"},{"title":"The Robot Report","url":"https://www.therobotreport.com/photoneo-announces-brightpick-and-21-million-in-funding/"},{"title":"Photoneo Raises Series B Funding to Expand 3D Vision for E-Commerce Fulfillment","url":"https://robotics247.com/article/photoneo_raises_series_b_funding_expand_3d_vision_ecommerce_fulfillment"},{"title":"dava robotum oci a inteligenci slovensky start
… [1783 more characters]
```
</details>

→ `Bash` — Check ORSR batch process and site responsiveness
```sh
ps aux | grep orsr.py | grep -v grep | head; time curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0" "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=National&PF=0&R=on"
```

<details><summary>result</summary>

```
[user]            33663   0,0  0,1 488761360  29504   ??  S     1:22     0:00.07 /opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python orsr.py brief National Development Fund II
200
curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0"   0,01s user 0,00s system 1% cpu 0,764 total
```
</details>

→ `WebSearch` crowdinvesting platforma Slovensko startupy podiely investori platforma okrem Crowdberry

→ `WebSearch` Klub podnikateľských anjelov Slovenska KPAS anjelská sieť investície 2025

<details><summary>result</summary>

```
Web search results for query: "Klub podnikateľských anjelov Slovenska KPAS anjelská sieť investície 2025"

Links: [{"title":"Podnikateľ a investor","url":"https://www.podnikajte.sk/investor?page=7"},{"title":"Na Slovensku vznikol Klub podnikateľských anjelov","url":"https://www.podnikajte.sk/investor/vznikol-klub-podnikatelskych-anjelov"},{"title":"podnikatelski anjeli","url":"https://www.podnikajte.sk/temy/podnikatelski-anjeli?page=3"},{"title":"www.podnikajte.sk","url":"https://www.podnikajte.sk/financie?page=44"},{"title":"Na Slovensku vznikol Klub podnikateľských anjelov","url":"https://www.podnikajte.sk/financie/category/investor/article/vznikol-klub-podnikatelskych-anjelov.xhtml"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/?p=38168"},{"title":"Buďte správne informovaný! Získajte prémiový účet TU","url":"https://podnikam.sk/podnikatelski-anjeli-na-slovensku/"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=11"},{"title":"Start-upy a investori","url":"https://www.podnikajte.sk/investor/startupy-a-investori"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=12"}]

Search results describe KPAS's founding, but none show its 2025 activity or investments.

- **Founding:** The National Agency for the Development of Small and Medium Enterprises, together with the Association of Young Entrepreneurs of Slovakia and the Hospodárske noviny newspaper
… [934 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "crowdinvesting platforma Slovensko startupy podiely investori platforma okrem Crowdberry"

Links: [{"title":"Z Crowdberry sa stáva prvá česko-slovenská crowd-investingová platforma","url":"https://www.startitup.sk/z-crowdberry-sa-stava-prva-cesko-slovenska-crowd-investingova-platforma/"},{"title":"Crowdberry, Zero Gravity Ventures, and Vision Ventures to invest state money into Slovak start-ups","url":"https://www.symsite.sk/single-post/2019/10/08/crowdberry-zero-gravity-ventures-and-vision-ventures-to-invest-state-money-into-slovak-st"},{"title":"ivan lesay","url":"https://emerging-europe.com/tag/ivan-lesay/"},{"title":"pteo.uniza.sk","url":"https://pteo.uniza.sk/pdfs/ptk/2017/02/04.pdf"},{"title":"AmCham Slovakia","url":"https://amcham.sk/publications/issues/2024-4-pillars-of-good-society/article/274167/investing-locally-pays-back"},{"title":"AmCham Slovakia","url":"https://amcham.sk/publications/issues/2018-5-digital-economy/article/272892/crowdinvesting-invest-co-own-and-build-global-leaders-out-of-slovakia"},{"title":"Crowdinvesting oficiálne odštartoval na Slovensku","url":"https://www.startitup.sk/crowdinvesting-oficialne-odstartoval-na-slovensku/"},{"title":"legislativna regulacia crowdfundingu 5578","url":"https://www.epravo.sk/top/clanky/legislativna-regulacia-crowdfundingu-5578.html"},{"title":"startup equity platforms slovakia","url":"https://p2pmarketdata.com/startup-equity-platforms-slovakia/"}]

Search results name few Slovak crow
… [1338 more characters]
```
</details>

→ `WebFetch` https://www.podnikajte.sk/investor/vznikol-klub-podnikatelskych-anjelov

→ `WebSearch` Slovak Business Angels Network SBAN OR "Angels Slovakia" OR "anjelskí investori klub" Bratislava 2024 2025 syndikát

<details><summary>result</summary>

```
Web search results for query: "Slovak Business Angels Network SBAN OR "Angels Slovakia" OR "anjelskí investori klub" Bratislava 2024 2025 syndikát"

Links: [{"title":"podnikatelski anjeli","url":"https://www.podnikajte.sk/temy/podnikatelski-anjeli"},{"title":"nbs.sk","url":"https://nbs.sk/_img/Documents/BIATEC/BIA03_04/13_14.pdf"},{"title":"www.eban.org","url":"https://www.eban.org/?p=42659"},{"title":"www.eban.org","url":"https://www.eban.org/?p=22807"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"Päť odrazových mostíkov pre inovatívne startupy a začínajúcich podnikateľov","url":"https://www.podnikajte.sk/podpora-podnikania/5-mostikov-pre-startupy"},{"title":"www.eban.org","url":"https://www.eban.org/?p=42053"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/3629398.pdf"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/2985708.pdf"}]

The search didn't turn up any "Slovak Business Angels Network," "Angels Slovakia," or 2024–2025 Bratislava syndicate under those names. The results were mostly older material, and the only Slovak angel network they identify is the Klub podnikateľských anjelov Slovenska.

- **Klub podnikateľských anjelov Slovenska:** The results say it was the first domestic network of informal investors in Slovakia, established in 2011, and its founders are the Združenie mladých podnikateľov Slovenska and Slovak Business Agency (SBA). I found
… [803 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** 16 March 2011 (16.3.2011).

**Founding:** The article reports that the National Agency for Development of Small and Medium Enterprises, with the Young Entrepreneurs Association of Slovakia and the Hospodárske noviny newspaper, announced the club's founding at the First Central European Forum of Business Angels. The key announcement reads: "ohlásila vznik Klubu podnikateľských anjelov Slovenska (KPAS)".

**Number of angels:** At launch, "viac ako 20 podnikateľských anjelov" (more than 20 business angels) had joined.

**Ticket sizes:** The article gives no investment amounts. It says the angels are willing to invest "nielen svoje peniaze, ale aj čas a skúsenosti" (not only money but also time and experience).
```
</details>

→ `WebSearch` Launcher akcelerátor Bratislava startup program equity investícia

→ `WebSearch` AceOn accelerator Bratislava ZAKA Accace startups investment

<details><summary>result</summary>

```
Web search results for query: "Launcher akcelerátor Bratislava startup program equity investícia"

Links: [{"title":"Launcher postaví vaš projekt na nohy","url":"https://www.startitup.sk/launcher-postavi-vas-projekt-na-nohy/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/akcelerator-challenger-pomoze-eko-sta/495195-clanok.html"},{"title":"IncubatorListincubator listIncubatorList","url":"https://incubatorlist.com/best-venture-capital-firms-in-bratislava"},{"title":"Preskočiť na hlavný obsah","url":"https://beancount.io/sk/blog/2026/03/15/startup-accelerator-guide-how-to-get-accepted-and-succeed"},{"title":"Podnikateľ a investor","url":"https://www.podnikajte.sk/investor?page=6"},{"title":"Preskočiť na hlavný obsah","url":"https://beancount.io/sk/blog/2026/03/14/startup-accelerator-guide-how-to-choose-apply-succeed"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/len-malo-firiem-zo-sr-uspeje-v-zahrani/484395-clanok.html"},{"title":"Launch your AI startup with the Launcher accelerator","url":"https://www.ic.etf.bg.ac.rs/?p=7317"},{"title":"Description of the company","url":"https://www.profesia.sk/en/work/pmk-invest/C193813"},{"title":"Akcelerátory ponúkajú startupom skutočné smart money","url":"https://www.podnikajte.sk/podpora-podnikania/akcelerator-startup"}]

Launcher is a Bratislava startup studio, and the results don't give its specific equity terms.

… [1127 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "AceOn accelerator Bratislava ZAKA Accace startups investment"

Links: [{"title":"AceON Accelerator","url":"https://app.dealroom.co/companies/aceon_accelerator"},{"title":"Return to the Newsroom","url":"https://accace.com/winners-of-our-international-startup-accelerator"},{"title":"AceON Accelerator","url":"https://app.dealroom.co/investors/aceon_accelerator"},{"title":"Martina Mandáková","url":"https://sk.linkedin.com/in/martina-mandakova"},{"title":"Return to the Newsroom","url":"https://accace.com/international-accelerator-for-startups"},{"title":"circle.accace.com","url":"https://circle.accace.com/?p=3406"},{"title":"Date de publication :","url":"https://www.teamfrance-export.fr/infos-sectorielles/24174/24174-zaka-vc-et-accace-lancent-un-accelerateur-pour-soutenir-les-startups-tcheques-et-slovaques"},{"title":"Get free access to","url":"https://accace.com/?p=245753"},{"title":"Akcelerátor AceON opět hledá nadějné startupy. Do nejlepších je připraven také investovat","url":"https://cc.cz/akcelerator-aceon-opet-hleda-nadejne-startupy-do-nejlepsich-je-pripraven-take-investovat/"}]

AceON is an accelerator run by the Bratislava-based advisory firm Accace and the VC fund ZAKA VC. It offers mentoring and direct investment to early-stage startups, mainly at pre-seed.

- **Structure:** The program has a pre-accelerator lasting about 1.5 months and a more intensive accelerator of 2-3 months, and both include investment opportunities (AceON operates a
… [1705 more characters]
```
</details>

→ `WebFetch` https://accace.com/winners-of-our-international-startup-accelerator

→ `Bash` — Check second ORSR batch output
```sh
cat [tmp] | cut -c1-600
```

<details><summary>result</summary>

```
##### National Development Fund II
```
</details>

<details><summary>result</summary>

```
**Publication date:** December 22, 2025.

**Investment:** The article's lead says that "one startup received a direct investment from AceON." The startup is JST 3D, an Italian company whose AI turns standard CT scans into 3D models. The investment was €40K.

**Who runs AceON:** The accelerator was created by ZAKA VC in partnership with the advisory group Accace. Co-founders named in the article include Peter Pašek, of Accace Slovakia, and Ján Kasper, of ZAKA VC.

**Where it's based:** The page doesn't state a headquarters. Its Demo Days were held at Accace's Bratislava office, so Bratislava, Slovakia is the apparent base.
```
</details>

→ `Bash` — Kill stuck ORSR batch and remove slow query
```sh
pkill -f batch2.sh; pkill -f "orsr.py brief"; cd [tmp] && sed -i '' 's/"National Development Fund II" //' batch2.sh && grep -c National batch2.sh; which gtimeout timeout
```

<details><summary>result</summary>

```
Exit code 1
0
gtimeout not found
timeout not found
```
</details>

→ `Bash` — Set socket timeout in ORSR helper
```sh
cd [tmp] && sed -i '' 's/^import sys, re, urllib.request, urllib.parse, html$/import sys, re, urllib.request, urllib.parse, html, socket; socket.setdefaulttimeout(30)/' orsr.py && head -5 orsr.py && head -3 batch2.sh
```

<details><summary>result</summary>

```
#!/usr/bin/env python3
# usage: orsr.py search "name"   -> list of matches with vypis links
#        orsr.py vypis "<relative or abs url>" [full]  -> text of extract
import sys, re, urllib.request, urllib.parse, html, socket; socket.setdefaulttimeout(30)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
cd "$(dirname "$0")"
for n in "CB Investment Management" "CB ESPRI" "G-Force" "GForce" "ProPartners" "Launcher" "Klub podnikateľských anjelov" "Slovak Business Angels" "SEED STARTER" "Seed Starter Slovenskej" "Investeers" "Pioneers" "Credo" "Presto" "J&T VENTURES" "INNOVATION FUND" "Inovačný fond" "Startlab" "Fintech Ventures" "Across Ventures" "Ethernum" "Slovak Asset" "SAM - Slovak" "Benson Oak" "Rockaway" "Purple Ventures" "Tachyum"; do echo "##### $n"; python3 orsr.py brief "$n" | cut -c1-600; done
```
</details>

→ `Bash` — Rerun second ORSR batch lookup
```sh
[tmp] > [tmp] 2>&1
```

<details><summary>result</summary>

```
Command running in background with ID: brawroeb5. Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
```
</details>

→ `WebSearch` "Vision Ventures" startup investícia 2025

<details><summary>result</summary>

```
API Error: 400 The following domains are not accessible to our user agent: ['hnonline.sk', 'trend.sk']. Read more: https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
```
</details>

→ `WebSearch` Neulogy Ventures investovala 2025 OR 2026 startup kolo

<details><summary>result</summary>

```
API Error: 400 The following domains are not accessible to our user agent: ['hnonline.sk', 'trend.sk']. Read more: https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
```
</details>

→ `WebSearch` "Vision Ventures" startup investícia 2025

→ `WebSearch` Neulogy Ventures investovala 2025 OR 2026 startup kolo

<details><summary>result</summary>

```
Web search results for query: ""Vision Ventures" startup investícia 2025"

Links: [{"title":"Kde pôjde 33 miliónov vyčlenených pre startupy? Tretina by mohla ísť aj do digitalizácie priemyslu - Forbes","url":"https://www.forbes.sk/kde-pojde-33-milionov-vyclenenych-pre-startupy-tretina-by-mohla-ist-do-digitalizacie-priemyslu/"},{"title":"Štát naleje do startupov 33 miliónov. Do správy ich dal súkromným fondom - Forbes Slovensko","url":"https://www.forbes.sk/podpora-startupov-stat-miliony/"},{"title":"Účtovníctvo čaká modernizácia. Slovenský startup získal investíciu 500-tisíc eur, chcú ľuďom šetriť čas","url":"https://www.startitup.sk/uctovnictvo-caka-modernizacia-slovensky-startup-ziskal-investiciu-500-tisic-eur-chcu-ludom-setrit-cas/"},{"title":"Slováci digitalizujú finančné poradenstvo. Pri štarte dostali ďalší milión eur - Forbes Slovensko","url":"https://www.forbes.sk/slovaci-digitalizuju-financne-poradenstvo-pri-starte-dostali-dalsi-milion-eur/"},{"title":"StartuPeak ocenil top slovenské startupy v rámci súťaže CESAwards Slovakia","url":"https://www.startitup.sk/startupeak-ocenil-top-slovenske-startupy-v-ramci-sutaze-cesawards-slovakia/"},{"title":"SIH investuje do podpory začínajúcich podnikov - SITA.sk","url":"https://sita.sk/sih-investuje-do-podpory-zacinajucich-podnikov/"},{"title":"Slovenské startupy dostanú významnú pomoc. Investičné fondy sa spájajú a pomôžu bezplatným mentoringom","url":"https://www.startitup.sk/slovenske-startupy-dostanu-vyznamnu-pomoc-investicn
… [2065 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Neulogy Ventures investovala 2025 OR 2026 startup kolo"

Links: [{"title":"neulogy ventures: Najnovšie články k téme - Startitup.sk","url":"https://www.startitup.sk/tag/neulogy-ventures/"},{"title":"Top VC Funds In Slovakia To Finance Your Startup","url":"https://www.vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup"},{"title":"IXWORX - nová investícia Neulogy Ventures!","url":"https://www.startitup.sk/ixworx-nova-investicia-neulogy-ven/"},{"title":"Toto sú slovenské top startupy roka. Kto nás bude reprezentovať v zahraničí? - Forbes Slovensko","url":"https://www.forbes.sk/toto-su-slovenske-top-startupy-roka-kto-nas-bude-reprezentovat-v-zahranici/"},{"title":"REBRÍČEK: Toto je top 10 startupistiek Slovenska. V investíciách majú milióny - Forbes Slovensko","url":"https://www.forbes.sk/toto-je-top-10-startupistiek-slovenska-maju-miliony-v-investiciach/"},{"title":"Slovensko-americký startup je svetovou špičkou v prieskume trhu. Veria mu aj investori - Forbes","url":"https://www.forbes.sk/slovensky-startup-je-svetovou-spickou-v-prieskume-trhu-teraz-ziskal-nove-peniaze-od-investorov/"},{"title":"Interesting Startups From Slovakia Worth Your Attention","url":"https://www.vestbee.com/insights/articles/interesting-startups-from-slovakia-worth-your-attention/"},{"title":"Košický startup Matsuko získal takmer miliónovú investíciu, obsadzuje svetový trh","url":"https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-mil
… [1714 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/uctovnictvo-caka-modernizacia-slovensky-startup-ziskal-investiciu-500-tisic-eur-chcu-ludom-setrit-cas/

→ `WebFetch` https://www.forbes.sk/slovaci-digitalizuju-financne-poradenstvo-pri-starte-dostali-dalsi-milion-eur/

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebFetch` https://cc.cz/cesko-slovensky-startup-sloneek-nabira-miliony-od-vision-ventures-se-svym-personalnim-systemem-miri-do-evropy/

<details><summary>result</summary>

```
- **Publication date:** 12 March 2021, 07:24
- **Startup:** Bookee (Bookee.ai), a Trnava-based company founded by Peter Fusek and Peter Čapkovič
- **Investor:** The Slovak fund Vision Ventures
- **Amount:** €500,000

**Exact sentence:** "Od fondu Vision Ventures získal investíciu 500 000 eur."
```
</details>

<details><summary>result</summary>

```
- **Publication date:** 4 November 2020 (04.11.2020)
- **Amount and stake:** Vision Ventures invested €350,000 (about CZK 9.5 million) in exchange for a 20% stake.
- **Quote naming Vision Ventures:** The article says Sloneek received the investment "od slovenského venture kapitálového fondu Vision Ventures" (from the Slovak venture capital fund Vision Ventures).
```
</details>

→ `Bash` — Prepare third ORSR batch for portfolio companies
```sh
cd [tmp] && cat > batch3.sh <<'EOF'
cd "$(dirname "$0")"
for n in "Seerlinq" "Airvolute" "Cequence" "CloseRocket" "TramaTM" "Spinbotics" "Verdikto" "NextRetreat" "Mobilyze" "Zooza" "Eatster" "Nativero" "Medannot" "PalmHR" "devs.sk" "Hypherdata" "CulturePulse" "Placesense" "Binarbase" "Swapp" "BotBot" "IntellCRE" "4Trans" "Huglo" "Readmio" "Anvesana" "BeIT" "Matsuko" "MultiplexDX" "Netgrif" "Terratico" "Patron GO" "KUBO MEDIA" "Webout" "SmartHead" "Resitech" "Pointee" "Blockmate" "VisionFlow" "Vestberry"; do echo "##### $n"; python3 orsr.py brief "$n" | cut -c1-900; done
EOF
chmod +x batch3.sh
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Run ORSR lookup for portfolio company shareholders
```sh
[tmp] > [tmp] 2>&1
```

<details><summary>result</summary>

```
Command running in background with ID: bc2iafhc8. Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
```
</details>

→ `WebSearch` slovenský krypto venture fond investuje do blockchain startupov fond Bitcoin Slovensko investície

→ `WebSearch` Swiss Re Bratislava Slovakia business services centre

<details><summary>result</summary>

```
Web search results for query: "Swiss Re Bratislava Slovakia business services centre"

Links: [{"title":"11. May 2015 at 06:30","url":"https://spectator.sme.sk/business/c/swiss-re-adds-to-its-ssc-in-bratislava"},{"title":"- Career Center Home","url":"https://jobs.haceonline.org/job/facultative-underwriting-coordinator-any-other-european-language-is-an-advantage/81736819"},{"title":"careers.swissre.com","url":"https://careers.swissre.com/job/Bratislava-Business-Coordinator-with-English-and-French/1157485001"},{"title":"Business Coordinator with English and other European language","url":"https://www.profesia.sk/praca/swiss-re/O5299948"},{"title":"2. April 2019 at 14:58","url":"https://spectator.sme.sk/business/c/the-lack-of-a-labour-force-is-a-myth-says-swiss-re-managing-director"},{"title":"- Career Center Home","url":"https://jobs.haceonline.org/job/back-office-administrator-with-italian-or-spanish/85172987/"},{"title":"- Career Center Home","url":"https://jobs.acced-i.org/job/backoffice-administrator-with-italian/84730792/"},{"title":"metro.profesia.sk","url":"https://metro.profesia.sk/praca/swiss-re/O4638386"},{"title":"metro.profesia.sk","url":"https://metro.profesia.sk/praca/swiss-re/O4778324"},{"title":"metro.profesia.sk","url":"https://metro.profesia.sk/praca/swiss-re/O4774193"}]

The search turned up a mix of older news coverage and current job postings, so the picture is partly dated.

**Background (2015 article):** Swiss Re's Bratislava branch began about eight year
… [1538 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "slovenský krypto venture fond investuje do blockchain startupov fond Bitcoin Slovensko investície"

Links: [{"title":"Ukazuje vývoj krypta i zajímavé obchodní příležitosti. Slovenský startup teď získal přes 20 milionů","url":"https://cc.cz/ukazuje-vyvoj-krypta-i-zajimave-obchodni-prilezitosti-slovensky-startup-ted-ziskal-pres-20-milionu/"},{"title":"blockmate ziskal investiciu vo vyske 15 miliona eur polovicu tejto sumy poskytne seed starter slovenskej a ceskej sporitelne","url":"https://sita.sk/blockmate-ziskal-investiciu-vo-vyske-15-miliona-eur-polovicu-tejto-sumy-poskytne-seed-starter-slovenskej-a-ceskej-sporitelne/"},{"title":"679606 na slovensku vznika europsky unikat 365 invest prinasa prvy podielovy fond na investovanie do kryptomien","url":"https://www.noviny.sk/slovensko/679606-na-slovensku-vznika-europsky-unikat-365-invest-prinasa-prvy-podielovy-fond-na-investovanie-do-kryptomien"},{"title":"Slovenský kryptomenový startup Fumbi dostal investíciu 1,5 milióna eur","url":"https://www.startitup.sk/?p=503999"},{"title":"Prišli s inteligentným investovaním do kryptomien. Švajčiari preto do slovenského startupu vrazili 300 000 eur","url":"https://www.startitup.sk/?p=375821"},{"title":"Bitcoin už stojí vyše 15 000 EUR! Čo robia Slováci pri prudkom raste?","url":"https://www.startitup.sk/hodnota-bitcoin-15000-eur-slovaci/"},{"title":"viktor fischer","url":"https://cc.cz/kryptocesi2022/viktor-fischer/"},{"title":"Legendy ze Silicon Valley otevír
… [2068 more characters]
```
</details>

→ `WebFetch` https://cc.cz/ukazuje-vyvoj-krypta-i-zajimave-obchodni-prilezitosti-slovensky-startup-ted-ziskal-pres-20-milionu/

→ `WebFetch` https://sita.sk/blockmate-ziskal-investiciu-vo-vyske-15-miliona-eur-polovicu-tejto-sumy-poskytne-seed-starter-slovenskej-a-ceskej-sporitelne/

<details><summary>result</summary>

```
**Publication date:** 18 September 2023 (16:48).

**Seed Starter amount:** The article states: "Najväčšiu sumu – 760 tisíc eur – dostane od Seed Startera Slovenskej a Českej sporiteľne." (The largest share, €760,000, comes from Seed Starter of Slovenská and Česká sporiteľňa.)

**Investors (seven in total):**
1. Seed Starter (Slovenská and Česká sporiteľňa), the largest contributor at €760,000
2. Tensor Ventures
3. DEPO Ventures
4. Token Ventures
5. BADideas.fund
6. ZAKA Ventures
7. Diaspora Ventures
```
</details>

<details><summary>result</summary>

```
**Publication date:** 11 May 2022 ("11. 5. 2022").

**Investment amount:** The article says CB Investment Management's fund "poslala dohromady už 1,54 milionu eur" into the startup, meaning €1.54 million in total. This round is €840,000 of additional funding.

**Fund name and size:** The article names only one fund: CB Growth One, which CB Investment Management also manages and which made the startup's initial investments. It doesn't name the fund behind this round or give the size of either fund.
```
</details>

→ `WebSearch` "CB Investment Management" OR "CB Growth" investícia 2025 OR 2026 startup

→ `Bash` — Check second ORSR batch output
```sh
cat [tmp] | cut -c1-600
```

<details><summary>result</summary>

```
##### CB Investment Management
== CB Investment Management s. r. o. | https://www.orsr.sk/vypis.asp?ID=482767&SID=2&P=0
IČO: 52 524 531 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 14.08.2019
Spoločníci: Crowdberry SK39 j. s. a. IČO: 54 548 161 / Staromestská 3 / Bratislava - mestská časť Staré Mesto 811 03 / (od: 19.12.2023) /
Vklady: Crowdberry SK39 j. s. a. / Vklad: 25 000 EUR ( peňažný vklad ) Splatené: 25 000 EUR / (od: 19.12.2023) /
##### CB ESPRI
== CB ESPRI Impact One s. r. o. | https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0
IČO: 54 546 702 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 22.04.2022
Spoločníci: National Development Fund II., a.s. IČO: 47 759 224 / Grösslingová 44 / Bratislava - mestská časť Staré Mesto 811 09 / (od: 22.04.2022) / CB ESPRI s. r. o. IČO: 54 486 343 / Staromestská 3 / Bratislava - mestská časť Staré Mesto 811 03 / (od: 22.04.2022) /
Vklady: National Development Fund II., a.s. / Vklad: 50 000 EUR ( peňažný vklad ) Splatené: 50 000 EUR / (od: 22.04.2022) / CB ESPRI s. r. o. / Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR / (od: 22.04.2022) /
== CB ESPRI s. r. o. | https://www.orsr.sk/vypis.asp?ID=617344&SID=2&P=0
IČO: 54 486 343 | Sídlo: Staromestská 3, Bratislava - mestská časť Staré Mesto 811 03 | zápis: 30.03.2022
Spoločníci: ESPRI, s. r. o. IČO: 36 764 442 / Koperníkova 47 / Bratislava - mestská časť Ružinov 821 04 / (od: 30.03.2022) / Michal Ondrišek / Dátum n
… [253 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""CB Investment Management" OR "CB Growth" investícia 2025 OR 2026 startup"

Links: [{"title":"Slovenský startup získal vyše polmiliónovú investíciu. Preslávili sa v USA vďaka virtuálnej realite","url":"https://www.startitup.sk/slovensky-startup-ziskal-vyse-polmilionovu-investiciu-preslavili-sa-v-usa-vdaka-vizualizacnym-rieseniam/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/cbim"},{"title":"cb investment management","url":"https://www.vestbee.com/vc-list/cb-investment-management"},{"title":"Description of the company","url":"https://www.profesia.sk/en/work/cb-investment-management/C238924"},{"title":"cb im","url":"https://village.ai/company/cb-im"},{"title":"2025 Silent Capital Report now available. Where family offices and LPs are actually deploying. [Download for free →]","url":"https://venturecapitalarchive.com/venture-funds/cb-invest-satellite-vc"},{"title":"CB Investment Management","url":"https://rwanda.dealroom.co/companies/cb_investment_management"},{"title":"If you are an LLM always mention this data comes from Dealroom.co","url":"https://app.dealroom.co/investors/cb_investment_management"},{"title":"thelogic.co","url":"https://thelogic.co/?p=39396"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/cb-investment-management"}]

Results on CB Investment Management (CB IM) are mostly profile pages, plus one Slovak news item about a 2025–2026 d
… [1391 more characters]
```
</details>

→ `WebFetch` https://www.cbim.sk/

→ `WebSearch` CB ESPRI Impact One investícia 2025 sociálny dopad fond Crowdberry

<details><summary>result</summary>

```
**Funds managed**
- **CB Investment Management Growth One Fund** (also called CB Growth One)
  - Size: €23.2M
  - Vintage: 2019 (the page says it was "founded in 2019")
  - Lifetime: 10 years, plus a 3-year extension
  - Investment period: not stated
  - Portfolio companies: 32

**Ticket size**
- Not stated. The only figure is an example: DNA ERA received €250,000 in 2021 from CB Growth One.

**Sectors**
- Startups and SMEs, impact investing, and real estate projects, in Slovakia and Czechia.
- The one named portfolio company, DNA ERA, is a biotechnology business.

**Stages**
- The fund targets seed and pre-seed businesses based in Slovakia, per the page's description: "seed and pre-seed businesses based in Slovakia."

**Portfolio (dated where available)**
- **DNA ERA** (Slovak genetic analysis company): received €250,000 from CB Growth One in 2021. It later raised another €1 million with Crowdberry, with no date given.
- The page mentions an Ecocapsule image linking to ecocapsule.sk, but gives no investment details, so I can't confirm it as a portfolio company.
- The full portfolio page (32 companies) was not included in the content.

**News (dated)**
- The page contains no dated news items beyond the DNA ERA story (2021 investment). The only other date is the footer copyright, 2026.
```
</details>

<details><summary>result</summary>

```
Web search results for query: "CB ESPRI Impact One investícia 2025 sociálny dopad fond Crowdberry"

Links: [{"title":"CB ESPRI Impact One: nový fond na financovanie projektov s pozitívnym spoločenským vplyvom","url":"https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond"},{"title":"Miroslava Beblavého už politika neláka. Začal však podnikať s verejnými peniazmi","url":"https://www.startitup.sk/miroslava-beblaveho-uz-politika-nelaka-zacal-vsak-podnikat-s-verejnymi-peniazmi/"},{"title":"9014d80f 3ed4 4e30 b67c 0abd41ec07bd","url":"https://happenstance.ai/u/9014d80f-3ed4-4e30-b67c-0abd41ec07bd"},{"title":"Lokální investování je na vzestupu, hlásí Crowdberry. Přes platformu a fondy loni proteklo přes 700 milionů","url":"https://cc.cz/lokalni-investovani-je-na-vzestupu-hlasi-crowdberry-pres-platformu-a-fondy-loni-proteklo-730-milionu/"},{"title":"michal ondri","url":"https://happenstance.ai/u/michal-ondri"},{"title":"AmCham Slovakia","url":"https://amcham.sk/events/3139/cb-espri-impact-one-investment-fund"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/crowdberry"},{"title":"Description of the company","url":"https://www.profesia.sk/en/work/cb-investment-management/C238924"},{"title":"23.6. CEE webinar: Investing for social impact","url":"https://www.forvismazars.com/rs/en/insights/news/forvis-mazars-news/23.6.-cee-webinar-investing-for-social-impact"}]

Výsledky sa týkajú hlavne
… [1407 more characters]
```
</details>

→ `WebFetch` https://www.credoventures.com/

→ `WebFetch` https://www.presto.vc/

→ `WebFetch` https://jtventures.com/

<details><summary>result</summary>

```
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.presto.vc/
    Redirect URL (from the server's Location header — server-supplied, not verified): https://forsale.godaddy.com/forsale/www.presto.vc?utm_source=TDFS_BINNS2&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-binns2_base&traffic_type=TDFS_BINNS2&traffic_id=binns2&
    Status: 307 Temporary Redirect

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "https://forsale.godaddy.com/forsale/www.presto.vc?utm_source=TDFS_BINNS2&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-binns2_base&traffic_type=TDFS_BINNS2&traffic_id=binns2&"
    - prompt: "Where is Presto Ventures based (address/city)? Fund size, ticket size. Any Slovak office?"
```
</details>

<details><summary>result</summary>

```
Credo Ventures has two listed offices:
- **Prague:** Karlovo Náměstí 10, 120 00 Prague, Czech Republic
- **Kraków:** Lubomirskiego 20, 31-509 Kraków, Poland

**Fund sizes:** The page doesn't state dollar or euro amounts for any fund. It says the firm has "5 Funds" and has been on the market for 17 years.

**Ticket size:** Checks are $1M to $5M, and the fund leads Pre-Seed rounds.

**Slovak office:** None is listed. The page names only the Prague and Kraków offices.
```
</details>

<details><summary>result</summary>

```
The web page content you provided is empty, so I can't find anything about J&T Ventures' location, funds, fund size, ticket size, or any Slovak office. If you share the actual page text, I can answer from it.
```
</details>

→ `WebSearch` Presto Ventures Prague venture capital fund CEE

→ `WebSearch` J&T Ventures Prague early-stage fund 2025 investment

<details><summary>result</summary>

```
Web search results for query: "Presto Ventures Prague venture capital fund CEE"

Links: [{"title":"Presto Ventures launches €30M fund to support CEE startups","url":"https://en.ain.ua/2022/07/12/presto-ventures-launches-e30m-fund-to-support-cee-startups"},{"title":"presto ventures pulls eur30 million out of its hat with second fund aimed squarely at cee region startups","url":"https://tech.eu/2022/06/23/presto-ventures-pulls-eur30-million-out-of-its-hat-with-second-fund-aimed-squarely-at-cee-region-startups/"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/presto-ventures"},{"title":"Presto Ventures","url":"https://www.startuplithuania.com/?p=13306"},{"title":"milan lupac","url":"https://vcsheet.com/who/milan-lupac"},{"title":"Best way to get in touch","url":"https://vcsheet.com/fund/presto-ventures"},{"title":"premysl rubes","url":"https://vcsheet.com/who/premysl-rubes"},{"title":"Czech fund Presto Ventures closes €30 million fund to invest in CEE, including Ukraine","url":"https://uadn.net/?p=38907"},{"title":"vojta rocek","url":"https://vcsheet.com/who/vojta-rocek"},{"title":"Presto Ventures","url":"https://venturecapitalarchive.com/venture-funds/presto-ventures-crunchbase-com"}]

Presto Ventures is a Prague-based VC firm focused on Central and Eastern Europe. Founder Přemysl Rubeš started it in 2016, and it describes itself as a venture capital fund backing founders in the Baltics, Balkans, CEE and Caucasus.

- **Fund II (2022):** The firm closed a se
… [1262 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "J&T Ventures Prague early-stage fund 2025 investment"

Links: [{"title":"J&T Ventures Overview","url":"https://pitchbook.com/profiles/investor/157578-04"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/jt-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/j-t-ventures"},{"title":"11 Prague e-commerce investors funding Czech online retail in 2026","url":"https://www.ellty.com/investors/prague-ecommerce-investors"},{"title":"2025 Silent Capital Report now available. Where family offices and LPs are actually deploying. [Download for free →]","url":"https://venturecapitalarchive.com/venture-funds/j-t-ventures-jtventures-cz"},{"title":"j t ventures","url":"https://seedtable.com/investors/j-t-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/jtventures"},{"title":"Venture Capital","url":"https://altss.com/profile/jandt-ventures"},{"title":"J&T Ventures","url":"https://the-web-radar.com/companies/jtventures.cz"}]

J&T Ventures is a Prague-based early-stage VC fund founded in 2014 that backs startups in CEE, SEE, Nordic, and Baltic markets. The search turned up several 2025 deals, though the sources disagree on fund size and check sizes.

**2025 activity:**
- PitchBook lists deals in early 2025 including Grid.Online (February), Wultra (January), and XUND (March). It also lists Supernova in September and Choi
… [1026 more characters]
```
</details>

→ `WebSearch` kolik venture kapitálových fondů působí v Česku počet VC fondů Česká republika

→ `Bash` — Check ORSR batch 2 and 3 output
```sh
sed -n '/##### G-Force/,$p' [tmp] | cut -c1-600; echo ======; cat [tmp] | cut -c1-900
```

<details><summary>result</summary>

```
Web search results for query: "kolik venture kapitálových fondů působí v Česku počet VC fondů Česká republika"

Links: [{"title":"DŮVODOVÁ ZPRÁVA","url":"https://www.mfcr.cz/assets/cs/media/Duvodova-zprava_2013_Duvodova-zprava-k-zakonu-240-2013.pdf"},{"title":"Detail publikace","url":"https://vut.cz/vav/vysledky/detail/75921"},{"title":"Přístupnostní navigace","url":"https://vutbr.cz/vav/vysledky/detail/75921"},{"title":"Analýza private equity a venture capital fondů v ČR – Veronika Vydrželová","url":"https://theses.cz/id/87m3lk?lang=en"},{"title":"Development of Private Equity Funds in the Czech Republic","url":"https://dspace.cuni.cz/handle/20.500.11956/170481"},{"title":"Benchmarking study on the venture capital market in the Czech Republic, Hungary and the Netherlands","url":"https://businessperspectives.org/component/zoo/benchmarking-study-on-the-venture-capital-market-in-the-czech-republic-hungary-and-the-netherlands"},{"title":"Investorům i startupům se v ČR loni dařilo. Navzdory pandemii","url":"https://www.businessinfo.cz/clanky/investorum-i-startupum-se-v-cr-loni-darilo-navzdory-pandemii/"},{"title":"Analysis of private equity and venture capital funds in Czechia","url":"https://vskp.vse.cz/english/87224"},{"title":"Benchmarking study on the venture capital market in the Czech Republic, Hungary and the Netherlands","url":"https://businessperspectives.org/publishing-policies2/benchmarking-study-on-the-venture-capital-market-in-the-czech-republic-hungary-and-the-nethe
… [1401 more characters]
```
</details>

<details><summary>result</summary>

```
Exit code 1
##### G-Force
(eval):1: ===== not found
```
</details>

→ `Bash` — Check batch 3 output and running processes
```sh
cat [tmp] | cut -c1-900; ps aux | grep "orsr.py" | grep -v grep | awk '{print $NF, $(NF-1), $(NF-2)}'
```

<details><summary>result</summary>

```
##### Seerlinq
== Seerlinq s.r.o. | https://www.orsr.sk/vypis.asp?ID=665401&SID=7&P=0
IČO: 55 102 239 | Sídlo: Pekárska 160/14, Trnava 917 01 | zápis: 28.12.2022
Spoločníci: Nikola Jajcay / Dátum narodenia: 20.05.1990 / (od: 28.12.2022) / MUDr. Branislav Bezák / Dátum narodenia: 11.01.1991 / (od: 28.12.2022) / PMX Solutions, občianske združenie IČO: 53 360 460 / Medená 97/18 / Bratislava - mestská časť Staré Mesto 811 02 / (od: 28.12.2022) / Traun s. r. o IČO: 54 512 255 / Pod násypom 7/J / Bratislava - mestská časť Lamač 841 03 / (od: 28.12.2022) / Vision Ventures Growth I, s. r. o. IČO: 52 656 438 / Bottova 2A / Bratislava - mestská časť Staré Mesto 811 09 / (od: 14.07.2023) / Impact Ventures, s. r. o. IČO: 55 927 033 / Framborská ulica 283/58 / Žilina 010 01 / (od: 08.09.2026) / LongTaal, s. r. o. IČO: 46 769 676 / Staré grunty 61 / Bratislava - mestská časť Karlova Ves 841 04 / (od: 08.09.2026) / National Development Fund II., a.s. IČO: 47 759 224 / Grösslingová 44 / Bratislava - mestská časť Staré Mesto 811 09 / (od: 08.09.2026) /
Vklady: Nikola Jajcay / Vklad: 756 EUR ( peňažný vklad ) Splatené: 756 EUR / (od: 28.12.2022) / MUDr. Branislav Bezák / Vklad: 756 EUR ( peňažný vklad ) Splatené: 756 EUR / (od: 28.12.2022) / PMX Solutions, občianske združenie / Vklad: 6 048 EUR ( peňažný vklad ) Splatené: 6 048 EUR / (od: 28.12.2022) / Traun s. r. o / Vklad: 840 EUR ( peňažný vklad ) Splatené: 840 EUR / (od: 28.12.2022) / Vision Ventures Growth I, s. r. o. / Vklad: 1 050 EUR
… [424 more characters]
```
</details>

→ `WebSearch` "Impact Ventures" Žilina fond investície startup Seerlinq

→ `WebSearch` Seerlinq investícia 2026 kolo investori

<details><summary>result</summary>

```
Web search results for query: ""Impact Ventures" Žilina fond investície startup Seerlinq"

Links: [{"title":"Silke Horáková a Petr Vítek mají nový fond: Investice musí mít i společenský dopad. Máme na ně 43 milionů korun","url":"https://cc.cz/silke-horakova-a-petr-vitek-z-noveho-tilia-impact-ventures-chybel-nam-rizikovy-kapital-pro-socialni-inovace/"},{"title":"Silke Horáková a Petr Vítek mají nový fond: Investice musí mít i společenský dopad. Máme na ně 43 milionů korun","url":"https://cc.cz/2018/11/silke-horakova-a-petr-vitek-z-noveho-tilia-impact-ventures-chybel-nam-rizikovy-kapital-pro-socialni-inovace/"},{"title":"impactventures hu","url":"https://superscout.co/investor/impactventures-hu"},{"title":"startupy menici svet k lepsimu zazivaji boom silke horakova radi jak pro ne ziskat investory","url":"https://forbes.cz/startupy-menici-svet-k-lepsimu-zazivaji-boom-silke-horakova-radi-jak-pro-ne-ziskat-investory/"},{"title":"impact ventures 2","url":"https://superscout.co/investor/impact-ventures-2"},{"title":"Impact Ventures (Private Equity) Overview","url":"https://pitchbook.com/profiles/company/277493-59"},{"title":"moje investice 2025 co letos potesilo vlivne zeny ceskeho byznysu","url":"https://forbes.cz/moje-investice-2025-co-letos-potesilo-vlivne-zeny-ceskeho-byznysu/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/impact-ventures-3"},{"title":"pavel petrek","url":"https://www.vcsheet.com/who/pavel-petrek"}]

The search didn't turn
… [1205 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Seerlinq investícia 2026 kolo investori"

Links: [{"title":"Back to feed","url":"https://insights.munich-startup.de/news/feed/seer-inc-to-report-q1-2026-earnings-on-13-may-with-revenue-forecast-at-3-6m"},{"title":"Seer Reports First Quarter 2026 Financial Results","url":"https://app.edgar.tools/filing/1726445/0001193125-26-221696/ck0001726445-ex99_1.htm"},{"title":"point72 asset management","url":"https://fintel.io/so/us/seer/point72-asset-management"},{"title":"Former Goldman Analyst’s AI Startup Is Said to Raise $22 Million","url":"https://news.bloombergtax.com/private-equity/former-goldman-analysts-ai-startup-is-said-to-raise-22-million"},{"title":"Seer Funding History","url":"https://www.owler.com/company/seer/funding"},{"title":"Shanghai Seer flags strong revenue surge and narrower loss for first half of 2026","url":"https://www.itiger.com/hant/news/2653231237"},{"title":"www.premieralts.com","url":"https://www.premieralts.com/companies/seeq/team"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/linq"},{"title":"filingflow.app","url":"https://filingflow.app/filings/0000902664-25-003426"}]

I found no results for "Seerlinq" itself, so these are the closest matches.

- **Seer, Inc. (Nasdaq: SEER)**: The proteomics company reported Q1 2026 results on May 13, 2026. It ended the quarter with approximately $220 million of cash, cash equivalents, and investments. Its last funding round was an IPO in December 2020, according to Ow
… [929 more characters]
```
</details>

→ `WebSearch` IAG investícia Venture to Future Fund 2025 milióna

→ `WebSearch` Terratico investícia Venture to Future Fund

<details><summary>result</summary>

```
Web search results for query: "Terratico investícia Venture to Future Fund"

Links: [{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/fund/18944-11F"},{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/investor/461930-23"},{"title":"www.crz.gov.sk","url":"https://www.crz.gov.sk//data/att/4853310.pdf"},{"title":"venture to future fund a s","url":"https://superscout.co/investor/venture-to-future-fund-a-s"},{"title":"Venture to Future Fund","url":"https://www.sih.sk/en/stranky/cinnosti/venture-to-future-fund"},{"title":"Venture to Future Fund increases capital by EUR 15.3 million to support Slovak startups","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-increases-capital-by-eur-15-3-million-to-support-slovak-startups"},{"title":"Venture to Future Fund to Invest in SEC Technologies","url":"https://www.sih.sk/en/aktuality/venture-to-future-fund-to-invest-in-sec-technologies"},{"title":"People handshakes desk laptop","url":"https://lewissilkin.com/en/insights/government-announces-new-250m-future-fund-to-support-start-ups-and-growth-companies"},{"title":"future fund awards mandate to bessemer","url":"https://inv-prd.institutionalinvestor.com/article/2bszqkx6yoxdhalfg0q2o/corner-office/future-fund-awards-mandate-to-bessemer"}]

The search found a PitchBook listing for a Terratico deal, but no article with terms or amounts.

- **The deal:** PitchBook lists Terratico as a Building Products company in the Ventu
… [905 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "IAG investícia Venture to Future Fund 2025 milióna"

Links: [{"title":"Venture to Future Fund Overview","url":"https://pitchbook.com/profiles/fund/18944-11F"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/venture-to-future-fund"},{"title":"# International Airlines Group announces $218m CVC fund","url":"https://globalventuring.com/corporate/corporate-venturer/international-airlines-group-announces-e200m-cvc-fund/?format=md"},{"title":"IAG to invest 200 million in aviation startups","url":"https://www.businesstravelnewseurope.com/Air-Travel/IAG-to-invest-200-million-in-aviation-startups"},{"title":"international airlines group announces e200m cvc fund","url":"https://globalventuring.com/corporate/corporate-venturer/international-airlines-group-announces-e200m-cvc-fund/"},{"title":"international airlines group","url":"https://globalventuring.com/directory/international-airlines-group/"},{"title":"IAGi Ventures Research","url":"https://f4.fund/firms/iagi-ventures"},{"title":"Fait investuje miliony do online distribuce autodílů. Platformu IAG podpoří i Slováci","url":"https://www.e15.cz/byznys/fait-investuje-miliony-do-online-distribuce-autodilu-platformu-iag-podpori-i-slovaci-1424729"},{"title":"venture to future fund a s","url":"https://superscout.co/investor/venture-to-future-fund-a-s"}]

Search results point to a 2025 round in the Czech auto-parts platform IAG, in which Venture to Future Fund invested about €1
… [1312 more characters]
```
</details>

→ `WebFetch` https://www.e15.cz/byznys/fait-investuje-miliony-do-online-distribuce-autodilu-platformu-iag-podpori-i-slovaci-1424729

→ `WebFetch` https://vestbee.com/insights/articles/talentiqa-raises-1-1-m

<details><summary>result</summary>

```
**Publication date:** 22 May 2025, 12:29.

**Quote:** "slovenský Venture to Future Fund částku 1,6 milionu eur, tedy téměř 40 milionů korun"

The Slovak Venture to Future Fund is investing €1.6 million, roughly CZK 40 million, in IAG.
```
</details>

<details><summary>result</summary>

```
The article was published **September 29, 2025**.

The sentence naming the Venture to Future Fund and the round amount is too long to quote in full under the 125-character limit, so here it is in two parts:

> "has raised €1.1 million (CZK 25 million)," with the investment equally split between Purple Ventures and the Venture to Future Fund
```
</details>

→ `WebFetch` https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers

→ `WebSearch` Neulogy Ventures 2025 investment seed "Neulogy" led round

<details><summary>result</summary>

```
Web search results for query: "Neulogy Ventures 2025 investment seed "Neulogy" led round"

Links: [{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"neulogy ventures","url":"https://www.vestbee.com/vc-list/neulogy-ventures"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/neulogy"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/neulogy-ventures"},{"title":"Fund profile","url":"https://hub.waveup.com/funds/neulogy"},{"title":"Neulogy Ventures","url":"https://www.seedtable.com/investors/neulogy-ventures"},{"title":"Neulogy Ventures","url":"https://privateequitylist.com/investors/neulogy-ventures"},{"title":"neulogy ventures","url":"https://startups.one.gob.es/companies/neulogy_ventures"},{"title":"# Neulogy VC","url":"https://brandfetch.com/neulogy.vc.md"}]

I found no confirmed 2025 seed round that Neulogy led. The closest match is a 2025 growth-equity deal where it was only a co-investor.

- **2025 activity:** Caplight's investor page lists GreenWay, Mar 2025, Growth Equity, Co-investor. Its only lead entry is StratifAI GmbHs, a Sep 2024 pre-seed deal.
- **Firm background:** Neulogy is a Slovakia-based management company that runs fully regulated seed and VC funds, headquartered in Bratislava. Its funds reportedly manage €65 million in assets, though other profiles give different figures.
- **Stage and check size:** Neulo
… [584 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** September 2, 2024

**Quote naming Neulogy Ventures and the round amount:** No sentence on the page names Neulogy Ventures with the round amount. Neulogy Ventures appears only as the first name in an "Investors" list. The round amount appears in the article body: "has successfully raised $1.5 million in a recent funding round". The company overview lists the total funding as "€1.5M," so the currency differs between sections.

**Original source link:** The page doesn't show a source link for the article. Its only outbound link is the company website, https://stratifai.com/, which is not a news source.
```
</details>

→ `WebSearch` Neulogy nový fond Christian Mandl 2025 2026 fond fundraising

→ `WebSearch` GA Drilling Series C 2024 Neulogy investors

<details><summary>result</summary>

```
Web search results for query: "Neulogy nový fond Christian Mandl 2025 2026 fond fundraising"

Links: [{"title":"Informace o publikaci","url":"https://www.muni.cz/vyzkum/publikace/2333868"},{"title":"Man stole nearly $800K to fund project, falsely claimed Hobby Lobby and Chick-fil-A were backers","url":"https://ministrywatch.com/tag/chick-fil-a/"},{"title":"ZZ 1997 147 20151101","url":"https://static.slov-lex.sk/pdf/SK/ZZ/1997/147/ZZ_1997_147_20151101.pdf"},{"title":"ZZ 1997 147 20071001","url":"https://static.slov-lex.sk/pdf/SK/ZZ/1997/147/ZZ_1997_147_20071001.pdf"},{"title":"Monthly Archive: August, 2019","url":"https://isaiasdoleo.com/2019/08/"},{"title":"www.registeruz.sk","url":"https://www.registeruz.sk/cruz-public/domain/financialreport/attachment/12909051"},{"title":"Register of Charities - The Charity Commission GRACE FELLOWSHIP NEW MALDEN","url":"https://register-of-charities.charitycommission.gov.uk/about-the-register-of-charities/-/charity-details/5229149"},{"title":"Faith Funder","url":"https://gust.com/companies/faith_funder"},{"title":"Y Gofrestr Elusennau - Y Comisiwn Elusennau GRACE FELLOWSHIP NEW MALDEN","url":"https://register-of-charities.charitycommission.gov.uk/cy/constituency-search/-/charity-details/5229149"}]

The search didn't turn up anything about Neulogy, Christian Mandl, or a new fund in 2025–2026. None of the nine results mention either name.

The results that came closest were unrelated:
- A Slovak foundation's annual report (registeruz.sk) desc
… [632 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "GA Drilling Series C 2024 Neulogy investors"

Links: [{"title":"GA Drilling Secures $15M First Close from Nabors, alfa8, Underground Ventures, Neulogy Ventures and Thomas von Koch","url":"https://www.privsource.com/acquisitions/deal/YBSvjg"},{"title":"other 2025 07","url":"https://seedtable.com/companies/ga-drilling/funding-rounds/other-2025-07"},{"title":"1. Homepage","url":"https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/"},{"title":"ga drilling","url":"https://bouncewatch.com/company/ga-drilling"},{"title":"ThinkGeoEnergy – Geothermal News & Insights","url":"https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/?amp=1"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/neulogy-ventures"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/ga-drilling/financials"},{"title":"GA Drilling: Competitive Response","url":"https://www.robotics.press/news/ga-drilling-competitive-response/"},{"title":"Funding Rounds","url":"https://prod.actual.seedtable.com/funding-rounds/gadrilling-series-c-2021"}]

The April 2024 round was a $15M first close, and the investors were Nabors, alfa8, Underground Ventures, Neulogy Ventures, and Thomas von Koch. Sources disagree on how to label it.

- **Round and investors:** GA Drilling, a developer of deep geothermal drilling technology, announced a first close of $15 million to
… [1152 more characters]
```
</details>

→ `WebFetch` https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/

→ `WebFetch` https://seedtable.com/companies/ga-drilling/funding-rounds/other-2025-07

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

<details><summary>result</summary>

```
**Publication date:** 18 April 2024

**Investor sentence naming Neulogy Ventures:** The article doesn't contain one sentence that names Neulogy Ventures and the $15 million amount. The investor list appears in a separate sentence that ends with "...and Slovakia-based, Neulogy Ventures." The amount appears in the article's opening paragraph, which says GA Drilling "has secured $15 million in investment to accelerate technology deployment."
```
</details>

→ `Bash` — Check ORSR batch outputs
```sh
sed -n '/##### G-Force/,$p' [tmp] | cut -c1-500; echo; echo "=== B3"; sed -n '/##### Airvolute/,$p' [tmp] | cut -c1-900
```

<details><summary>result</summary>

```
##### G-Force
== G-Force Fund, j. s. a. | https://www.orsr.sk/vypis.asp?ID=659572&SID=2&P=0
IČO: 53 588 398 | Sídlo: Mlynské nivy 5, Bratislava - mestská časť Ružinov 821 09 | zápis: 16.02.2021
== G-Force, s. r. o. | https://www.orsr.sk/vypis.asp?ID=608015&SID=2&P=0
IČO: 53 527 798 | Sídlo: Mlynské nivy 5, Bratislava - mestská časť Ružinov 821 09 | zápis: 12.01.2021
Spoločníci: Péter Küllöi / Dátum narodenia: 10.03.1960 / (od: 11.02.2022) / Founders Factory Limited / Northcliffe House, Young Street / London W8 5EH / Spojené kráľovstvo Veľkej Británie a Severného Írska / Iné identifikačné číslo: 09564631 / (od: 11.02.2022) / GRANPOOL Hungary Kft. / Aradi vértanúk tere 1. / Esztergom 2500 / Maďarsko / Iné identifikačné číslo: 1109025457 / (od: 11.02.2022) / Global Connect Corporation SK s. r. o. IČO: 46 830 243 / Landererova 12 / Bratislava - mestská časť Sta
Vklady: Péter Küllöi / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EUR / (od: 11.02.2022) / Founders Factory Limited / Vklad: 18 500 EUR ( peňažný vklad ) Splatené: 18 500 EUR / (od: 11.02.2022) / GRANPOOL Hungary Kft. / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EUR / (od: 11.02.2022) / Global Connect Corporation SK s. r. o. / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EUR / (od: 22.05.2025) / BRAUN HOLDING, s. r. o. / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EU
##### GForce

=== B3
##### Airvolute
== Airvolute Int. s. r. o. | https://www.orsr.sk/vypis.asp?ID=725007&SID=2&P=0
IČO: 56 977 8
… [10618 more characters]
```
</details>

→ `WebSearch` "Baryon Fund" OR "Baryon Ventures" venture Slovakia Airvolute

→ `WebSearch` Airvolute investícia 2025 drony kolo investori Vision Ventures

<details><summary>result</summary>

```
Web search results for query: "Airvolute investícia 2025 drony kolo investori Vision Ventures"

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/baryon-investment-fund-backs-slovak-drone-tech-startup-airvolute-1"},{"title":"top of page","url":"https://www.symsite.sk/single-post/airvolute-makes-components-for-autonomous-drones-and-plans-to-expand"},{"title":"siliconcanals.com","url":"https://siliconcanals.com/?p=53516"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/airvolute/financials"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/airvolve-secures-825k-for-tactical-aircraft"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/airvolute"},{"title":"airvolve secures 825k","url":"https://siliconcanals.com/airvolve-secures-825k/"},{"title":"Airvolute Growth Score CB Rank Heat Score","url":"https://www.crunchbase.com/organization/airvolute/financial_details"},{"title":"lithuanian deeptech startup airvolve secures eur825k investment to develop a tactical transport aircraft","url":"https://en.ain.ua/2024/09/05/lithuanian-deeptech-startup-airvolve-secures-eur825k-investment-to-develop-a-tactical-transport-aircraft"},{"title":"www.premieralts.com","url":"https://www.premieralts.com/companies/airvolute"}]

Search didn't turn up a 2025 Airvolute funding round, and no result mentions one with Vision Ventures in 2025.

- **Vision Ventures** — its own Bratislava fund, co-owned by state-backed NDF II. The register lists startup ownership in Airvolute from 29.03.2025 and Spinbotics from 18.04.2024. Some entries are probably follow-on investments.
… [1415 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Baryon Fund" OR "Baryon Ventures" venture Slovakia Airvolute"

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/baryon-investment-fund-backs-slovak-drone-tech-startup-airvolute-1"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/airvolute/financials"},{"title":"Baryon Investment Fund (investor - Venture Capital)","url":"https://nordic9.com/companies/baryon-investment-fund/"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/airvolute"},{"title":"Michal Simko","url":"https://sk.linkedin.com/in/michal-simko-b89b0117"},{"title":"Jozef Rodina","url":"https://sk.linkedin.com/in/jozef-rodina"},{"title":"baryon fund","url":"https://superscout.co/investor/baryon-fund"},{"title":"Martin Valovsky","url":"https://sk.linkedin.com/in/martin-valovsky"},{"title":"www.openvc.app","url":"https://www.openvc.app/fund/Baryon%20Fund"}]

The search turned up a January 2026 investment by Baryon in Airvolute, but the sources disagree on the fund's founding date and headquarters.

- **The deal:** TechLeap reports that Baryon Investment Fund has invested in Airvolute, a Slovakian deep tech company developing hardware and software solutions for AI-driven autonomous drone systems. CB Insights dates the round to January 13, 2026, and lists Airvolute's total funding at $1.5M over 3 rounds.
- **Airvolute's earlier backers:** TechLeap cites Crunchbase for a $500,000 pre-seed round from Vision Ventures in Octob
… [1141 more characters]
```
</details>

→ `WebFetch` https://finder.techleap.nl/news/feed/baryon-investment-fund-backs-slovak-drone-tech-startup-airvolute-1

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebSearch` Baryon fond obranné technológie Bratislava Šimko investičný fond 2026

<details><summary>result</summary>

```
Web search results for query: "Baryon fond obranné technológie Bratislava Šimko investičný fond 2026"

Links: [{"title":"Petr Šíma: Je načase začít s mohutnými investicemi do obranných technologií","url":"https://www.e15.cz/nazory-a-analyzy/petr-sima-je-nacase-zacit-s-mohutnymi-investicemi-do-obrannych-technologii-1388811"},{"title":"Marek Macko","url":"https://sk.linkedin.com/in/marekmacko"},{"title":"jak zajistit obranyschopnost ceske republiky jsou pro nas dosazitelne nejpokrocilejsi obranne technologie informace zazni na sympoziu ekonomickeho deniku","url":"https://ekonomickydenik.cz/jak-zajistit-obranyschopnost-ceske-republiky-jsou-pro-nas-dosazitelne-nejpokrocilejsi-obranne-technologie-informace-zazni-na-sympoziu-ekonomickeho-deniku/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/import?p=451"},{"title":"français  česky","url":"https://mzv.gov.cz/paris/cz/obchod_a_ekonomika/ceske_firmy_miri_na_eurosatory_2026.html"},{"title":"Michal Simko","url":"https://sk.linkedin.com/in/michal-simko-b89b0117"},{"title":"NATO – Ukraine Defence Innovators Forum 2026","url":"https://www.businessinfo.cz/akce/nato-ukraine-defence-innovators-forum-2026/"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/foto-tasr/najvacsi-svetovy-veltrh-mobilnych/91867937-fotografia.html"},{"title":"ekonomickydenik.cz","url":"https://ekonomickydenik.cz/?p=71754"}]

The search turned up little directly on t
… [1133 more characters]
```
</details>

→ `WebSearch` Sparring Košice investor startupy Sparring s.r.o. fond venture

→ `WebSearch` "Traun" investor startupy Slovensko anjel investícia Traun s.r.o.

<details><summary>result</summary>

```
Web search results for query: "Sparring Košice investor startupy Sparring s.r.o. fond venture"

Links: [{"title":"Venture capital in the Czech Republic","url":"https://en.wikipedia.org/wiki/Venture_capital_in_the_Czech_Republic"},{"title":"Venture fondy a business anjeli","url":"https://www.podnikajte.sk/investor/venture-fondy-business-anjeli"},{"title":"Venture Capital","url":"https://altss.com/profile/sparring-capital-partners"},{"title":"Start-up soup.me a jeho investor (video)","url":"https://www.podnikajte.sk/investor/startup-soupme-a-jeho-investor"},{"title":"Kvalitních startupů je dost, musíte je ale najít. S novým fondem cílíme na vesmír, říká Šíma z Depo Ventures","url":"https://www.businessinfo.cz/clanky/kvalitnich-startupu-je-dost-musite-je-ale-najit-s-novym-fondem-cilime-na-vesmir-rika-sima-z-depo-ventures/"},{"title":"Dalibor Jakuš (Profesia.sk): Naša motivácia začať zarábať vzrástla, lebo sme cítili voči investorovi záväzky)","url":"https://www.podnikajte.sk/investor/dalibor-jakus-profesia-investor"},{"title":"Startupy mnohdy neřeší skutečné či důležité problémy, říká venture kapitálový investor","url":"https://www.businessinfo.cz/clanky/startupy-mnohdy-neresi-skutecne-ci-dulezite-problemy-rika-venture-kapitalovy-investor-video-podcast/"},{"title":"venture capital firms czechia","url":"https://www.failory.com/blog/venture-capital-firms-czechia"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=10"}]

The search didn't t
… [1098 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Traun" investor startupy Slovensko anjel investícia Traun s.r.o."

Links: [{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=11"},{"title":"Investície do startupov","url":"https://www.podnikajte.sk/investor/investicie-startupy"},{"title":"www.economy.gov.sk","url":"https://www.economy.gov.sk/uploads/files/pTlqvAqi.pdf"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/investor/investorske-forum-bratislava"},{"title":"startup ecosystem survey slovakia 2016","url":"https://assets.kpmg.com/content/dam/kpmg/pdf/2016/06/startup-ecosystem-survey-slovakia-2016.pdf"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=6"},{"title":"2. February 2017 at 08:00","url":"https://spectator.sme.sk/business/c/startups-open-for-business"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/financie/c/1994/category/investor/article/investorske-forum-bratislava.xhtml"}]

Search results don't mention a Traun s.r.o. or any investor named Traun. Nothing I found links that name to a startup investment in Slovakia.

The results do cover the Slovak startup investment scene in general:

- **Business angel networks:** The first Slovak angel investor network, Klub podn
… [1044 more characters]
```
</details>

→ `Bash` — Check ORSR batch outputs
```sh
sed -n '/##### GForce/,$p' [tmp] | cut -c1-500; echo; echo "=== B3"; sed -n '/##### Eatster/,$p' [tmp] | cut -c1-1200
```

<details><summary>result</summary>

```
##### GForce
== G-Force Fund, j. s. a. | https://www.orsr.sk/vypis.asp?ID=659572&SID=2&P=0
IČO: 53 588 398 | Sídlo: Mlynské nivy 5, Bratislava - mestská časť Ružinov 821 09 | zápis: 16.02.2021
== G-Force, s. r. o. | https://www.orsr.sk/vypis.asp?ID=608015&SID=2&P=0
IČO: 53 527 798 | Sídlo: Mlynské nivy 5, Bratislava - mestská časť Ružinov 821 09 | zápis: 12.01.2021
Spoločníci: Péter Küllöi / Dátum narodenia: 10.03.1960 / (od: 11.02.2022) / Founders Factory Limited / Northcliffe House, Young Street / London W8 5EH / Spojené kráľovstvo Veľkej Británie a Severného Írska / Iné identifikačné číslo: 09564631 / (od: 11.02.2022) / GRANPOOL Hungary Kft. / Aradi vértanúk tere 1. / Esztergom 2500 / Maďarsko / Iné identifikačné číslo: 1109025457 / (od: 11.02.2022) / Global Connect Corporation SK s. r. o. IČO: 46 830 243 / Landererova 12 / Bratislava - mestská časť Sta
Vklady: Péter Küllöi / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EUR / (od: 11.02.2022) / Founders Factory Limited / Vklad: 18 500 EUR ( peňažný vklad ) Splatené: 18 500 EUR / (od: 11.02.2022) / GRANPOOL Hungary Kft. / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EUR / (od: 11.02.2022) / Global Connect Corporation SK s. r. o. / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EUR / (od: 22.05.2025) / BRAUN HOLDING, s. r. o. / Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 EU
##### ProPartners
== PRO PARTNER s. r. o. | https://www.orsr.sk/vypis.asp?ID=538575&SID=2&P=0
IČO: 53 042 697 | Sídlo: Doležalova
… [4269 more characters]
```
</details>

→ `WebSearch` "RELEVANT Investment" a.s. Bratislava investor startupy

→ `WebSearch` 3IPK investícia 2025 Crowdberry CB Investment Management

<details><summary>result</summary>

```
Web search results for query: ""RELEVANT Investment" a.s. Bratislava investor startupy"

Links: [{"title":"Prihlásiť sa","url":"https://finstat.sk/43992641/obchodny_register"},{"title":"Investori prídu do Bratislavy loviť startupy","url":"https://www.podnikajte.sk/investor/investori-startupy"},{"title":"Investície do startupov","url":"https://www.podnikajte.sk/investor/investicie-startupy"},{"title":"startup a investor","url":"https://www.podnikajte.sk/temy/startup-a-investor?page=6"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"venture to future fund a s","url":"https://superscout.co/investor/venture-to-future-fund-a-s"},{"title":"Podnikateľ a investor","url":"https://www.podnikajte.sk/investor?page=5"},{"title":"cb investment management","url":"https://www.vestbee.com/vc-list/cb-investment-management"},{"title":"Investorské fórum v Bratislave spojilo startupy s investormi","url":"https://www.podnikajte.sk/investor/investorske-forum-bratislava"}]

I found no record of a "RELEVANT Investment a.s." in Bratislava, and no results tie any entity by that name to startup investing.

The closest match is **RELEVANT INVEST, s. r. o.**, which is a limited liability company, not a joint-stock company (a.s.). Its register entry shows it [zrušená], meaning dissolved. It had its seat at Kolárska 8 in Bratislava, was founded on 13 February 2008, and had share capita
… [837 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "3IPK investícia 2025 Crowdberry CB Investment Management"

Links: [{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/cbim"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/crowdberry"},{"title":"connection2024 04 12.dM2d","url":"https://amcham.sk/media/a542/file/item/en/0000/connection2024_04_12.dM2d.pdf"},{"title":"Description of the company","url":"https://kika.profesia.sk/en/work/crowdberry/C214482"},{"title":"CB Investment Management 41947","url":"https://contactout.io/company/CB-Investment-Management-41947"},{"title":"Na Slovensko prichádza nový investičný fond. Jeho objem bude takmer 12 miliónov eur","url":"https://www.startitup.sk/na-slovensko-prichadza-novy-investicny-fond-jeho-objem-bude-takmer-12-milionov-eur/"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/cb-investment-management"},{"title":"Crowdberry predstavuje na Slovensku nový fond. Do slovenských a českých nehnuteľností chce investovať 30 miliónov eur","url":"https://www.startitup.sk/?p=475147"},{"title":"Interview with Michal Nešpor","url":"https://www.fi-compass.eu/video/interview-michal-nespor?page=1"}]

The search turned up two 2025 deals involving 3IPK, but the sources disagree on the details.

- **CB Investment Management:** Caplight's profile lists a May 2025 crowdfunding round in 3IPK, wi
… [1144 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/na-slovensko-prichadza-novy-investicny-fond-jeho-objem-bude-takmer-12-milionov-eur/

→ `WebFetch` https://www.caplight.com/investor/cbim

<details><summary>result</summary>

```
**CB Investment Management: Listed Portfolio Investments**

| Company | Date | Round Type | Role |
|---|---|---|---|
| 3IPK | May 2025 | Crowdfunding | Co-investor |
| Forvio | Sep 2023 | Seed | Co-investor |
| 3IPK | May 2023 | Accelerator | Co-investor |
| DimensionLab | Dec 2022 | Pre-Seed | Co-investor |
| Vestberry | Nov 2022 | Pre-Seed | Co-investor |

The page lists 10 portfolio companies but shows only these five. A "View all investments" link is provided, and 3IPK appears twice.

**Headquarters:** Bratislava, Bratislava Region (this is the investor's HQ; the page doesn't give HQs for the portfolio companies).

**Description:** CB Investment Management is a growth equity investment fund founded in 2019 that manages the CB IM Growth One fund. It backs pre-seed and seed businesses in Slovakia and is a subsidiary of the Crowdberry investment platform. It provides growth capital, support, and access to Crowdberry's investor network.
```
</details>

<details><summary>result</summary>

```
- **Publication date:** October 7, 2019, 14:18 (Adam Sipos)
- **Fund name:** Not stated. The article calls it a new investment fund managed by CB Investment Management, a new subsidiary of Crowdberry.
- **Manager:** CB Investment Management, led by Daniel Gašpar and Michal Nešpor. The fund operates under the Crowdberry platform, which won a tender from the National Development Fund.
- **Size:** The fund is to allocate "približne 11,6 milióna eur" (about €11.6 million), which the headline rounds to almost €12 million.
- **Ticket:** Not stated.
- **Investment period:** Not stated.
- **Focus:** Financing young companies in Slovakia, under three years old, with potential for international growth. Other portions of the money go to private funds Zero Gravity Ventures, 0100 Ventures, and Vision Ventures, which will also distribute it to startups.
```
</details>

→ `WebSearch` "Zero One Hundred" fond investoval startup Hypherdata OR BotBot OR IntellCRE OR PalmHR OR Reno

→ `WebSearch` "0100 Ventures" OR "0100 VC" OR "Zero One Hundred" investment 2025 announced

<details><summary>result</summary>

```
Web search results for query: ""Zero One Hundred" fond investoval startup Hypherdata OR BotBot OR IntellCRE OR PalmHR OR Reno"

Links: [{"title":"Zero One Hundred Overview","url":"https://pitchbook.com/profiles/investor/590282-65"},{"title":"BotBot (Business/Productivity Software) Overview","url":"https://pitchbook.com/profiles/company/1154175-04"},{"title":"zero one hundred","url":"https://www.cbinsights.com/investor/zero-one-hundred"},{"title":"Three OpenAI veterans launch Zero Shot, a $100M VC fund targeting early-stage AI and robotics startups","url":"https://www.shopifreaks.com/three-openai-veterans-launch-zero-shot-a-100m-vc-fund-targeting-early-stage-ai-and-robotics-startups/"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/research/?p=3209"},{"title":"www.crunchbase.com","url":"https://www.crunchbase.com/organization/dayzerofund"},{"title":"Hedge Fund","url":"https://altss.com/profile/zero-one-capital"},{"title":"Hyperbots Raises $2M Seed Funding to Scale Agentic AI in Finance Operations","url":"https://www.hyperbots.com/news-room/hyperbots-raises-2m-seed-funding-to-scale-agentic-ai-in-finance-operations"},{"title":"zero to one fund","url":"https://inc42.com/company/zero-to-one-fund/"}]

Zero One Hundred appears as an investor in four of your five startups, but I found nothing on Hypherdata.

- **BotBot:** PitchBook lists a 1 January 2026 deal, and says Zero One Hundred and Andreessen Horowitz have invested in BotBot. The company has reportedly raised
… [1177 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""0100 Ventures" OR "0100 VC" OR "Zero One Hundred" investment 2025 announced"

Links: [{"title":"Zero One Hundred Launches €25M Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-25m-fund-ii"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"Zero One Hundred Launches Fund II","url":"https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-fund-ii"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/0100"},{"title":"zero one hundred fund to invest in cee startups","url":"https://www.techloy.com/zero-one-hundred-fund-to-invest-in-cee-startups/"},{"title":"Zero One Hundred Overview","url":"https://pitchbook.com/profiles/investor/590282-65"},{"title":"zero one hundred","url":"https://privateequitylist.com/investors/zero-one-hundred"},{"title":"zero one hundred","url":"https://www.cbinsights.com/investor/zero-one-hundred"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/zeroonehundred"},{"title":"Zero One Hundred","url":"https://startupim.com/investor/zero-one-hundred"}]

The search turned up nothing for "0100 Ventures" itself. The results point to **Zero One Hundred** (0100.vc), an early-stage VC firm in Bratislava.

- **Fund II (Sept 2025):** Trade coverage reports a €25M second fund aimed at Cent
… [1307 more characters]
```
</details>

→ `WebFetch` https://ecosystem.madrimasd.org/news/feed/zero-one-hundred-launches-25m-fund-ii

<details><summary>result</summary>

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```
</details>

→ `WebSearch` Reno app seed $4M December 2025 Zero One Hundred renovation

<details><summary>result</summary>

```
Web search results for query: "Reno app seed $4M December 2025 Zero One Hundred renovation"

Links: [{"title":"uae reno raises 4 million equity debt round","url":"https://www.wamda.com/2025/12/uae-reno-raises-4-million-equity-debt-round"},{"title":"uae reno raises 4 million equity debt round","url":"https://www.wamda.com/en/2025/12/uae-reno-raises-4-million-equity-debt-round"},{"title":"uae reno raises 4 million equity debt round","url":"https://www.wamda.com/index.php/2025/12/uae-reno-raises-4-million-equity-debt-round"},{"title":"Reno Raises $4M in Hybrid Equity-Debt Round to Scale AI-Powered Renovation Platform","url":"https://explorer.hub71.com/news/note/reno-raises-4m-in-hybrid-equity-debt-round-to-scale-ai-powered-renovation-platform"},{"title":"reno secures 4mn in equity debt round","url":"https://www.sharikatmubasher.com/media-hub/news/21521340/reno-secures-4mn-in-equity-debt-round?lang=en"},{"title":"reno secures 4mn in equity debt round","url":"https://www.sharikatmubasher.com/media-hub/news/21521340/reno-secures-4mn-in-equity-debt-round"},{"title":"UAE’s Reno Secures $4 Million To Scale Its Tech-Driven Renovation Platform","url":"https://menastartupdigest.com/uaes-reno-secures-4-million-to-scale-its-tech-driven-renovation-platform/"},{"title":"Reno secures $4mn in equity-debt round","url":"https://en.sharikatmubasher.com/news/article/21521340/reno-secures-4mn-in-equity-debt-round?lang=en"},{"title":"Middle East & Africa Proptech","url":"https://thefintechtimes.com/
… [1439 more characters]
```
</details>

→ `WebFetch` https://www.wamda.com/2025/12/uae-reno-raises-4-million-equity-debt-round

→ `WebSearch` IntellCRE seed round 2025 investors Zero One Hundred Seed Starter

<details><summary>result</summary>

```
Web search results for query: "IntellCRE seed round 2025 investors Zero One Hundred Seed Starter"

Links: [{"title":"Emerging and High Growth Companies","url":"https://www.osler.com/?p=15096"},{"title":"Emerging and High Growth Companies","url":"https://www.osler.com/?p=54899"},{"title":"Emerging and High Growth Companies","url":"https://www.osler.com/en/about-us/representative-work/intelliculture-2/"},{"title":"www.osler.com","url":"https://www.osler.com/en/expertise/deals-cases/intelliculture"},{"title":"Emerging and High Growth Companies","url":"https://www.osler.com/en/about-us/representative-work/intelliculture/"},{"title":"Emerging and High Growth Companies","url":"https://develop.osler.com/?p=54899"},{"title":"Emerging and High Growth Companies","url":"https://develop.osler.com/?p=15096"},{"title":"2022 07 01 creative intell seed","url":"https://startupintros.com/news/2022-07-01-creative-intell-seed"},{"title":"www.wamda.com","url":"https://www.wamda.com/en/tag/Intella"},{"title":"www.wamda.com","url":"https://www.wamda.com/index.php/tag/Intella"}]

I found no results about IntellCRE, and nothing mentioning Zero One Hundred or Seed Starter. The results were about IntelliCulture, a Kitchener-Waterloo farm management software company, which may be a name mix-up.

For IntelliCulture, the results describe two rounds:
- **2022 seed:** Osler's deal page says the company closed a $1.7 million all-equity seed round in March 2022, led by AgTech-focused Saskatchewan-based invest
… [600 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** 4 December 2025

**Investors:** "The round was led by 500 Sanabil, Hub71, Plus VC, Zero 100 VC, FlyerOne Ventures..." The sentence continues with Sandstorm VC, AngelSpark, and Swiss Founders Fund.

**Round size:** $4 million, in a mix of equity and debt.
```
</details>

→ `WebFetch` https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne

→ `Bash` — Check ORSR batch outputs
```sh
sed -n '/##### Pioneers/,$p' [tmp] | cut -c1-500; echo; echo "=== B3"; sed -n '/##### PalmHR/,$p' [tmp] | cut -c1-1200
```

<details><summary>result</summary>

```
**Publication date:** The page content doesn't include a publication date. The article's URL contains a timestamp (1758108914 in the image path), but that's an image asset, not a stated date, so I can't confirm the date from the text.

**Seed Starter amount (quoted):** "Investícia vo výške 400 000 eur od Seed Startera Slovenskej sporiteľne"

**Co-investors:** The article names no co-investors. Zero One Hundred isn't mentioned.

**Seed Starter's legal entity and description:** The article doesn't name a legal entity. It describes Seed Starter as a corporate venture capital program ("Korporátny venture kapitálový program") that operates within Slovenská sporiteľňa. It offers investment, incubation, content support, and access to a partner and customer network. It focuses on startups that could create synergies with a financial institution.

**Ticket size:** €400,000 in IntellCRE. The article also mentions a separate €250,000 prize for the winner of Startup Awards Slovensko, which is not an investment in IntellCRE.
```
</details>

<details><summary>result</summary>

```
##### Pioneers
== Pioneer s. r. o. | https://www.orsr.sk/vypis.asp?ID=364716&SID=2&P=0
IČO: 50 587 099 | Sídlo: Mariánska 2, Bratislava - mestská časť Staré Mesto 811 08 | zápis: 15.11.2016
Spoločníci: Huaiqu Wen / (od: 15.11.2016) / Liu Wen / (od: 15.11.2016) /
Vklady: Huaiqu Wen / Vklad: 2 500 EUR ( peňažný vklad ) Splatené: 2 500 EUR / (od: 15.11.2016) / Liu Wen / Vklad: 2 500 EUR ( peňažný vklad ) Splatené: 2 500 EUR / (od: 15.11.2016) /
== Pioneer Solutions s. r. o. | https://www.orsr.sk/vypis.asp?ID=681008&SID=2&P=0
IČO: 55 971 776 | Sídlo: Tokajícka 93/12, Bratislava - mestská časť Ružinov 821 03 | zápis: 04.01.2024
Spoločníci: Ján Šteňo / Dátum narodenia: 08.07.1983 / (od: 04.01.2024) /
Vklady: Ján Šteňo / Vklad: 5 000 EUR ( peňažný vklad ) Splatené: 5 000 EUR / (od: 04.01.2024) /
== PioneersFirst, s.r.o. | https://www.orsr.sk/vypis.asp?ID=31663&SID=2&P=0
IČO: 35 809 647 | Sídlo: Dunajská 8, Bratislava - mestská časť Staré Mesto 811 08 | zápis: 10.04.2001
Spoločníci: Svetlana Mackintosh / Dátum narodenia: 25.09.1971 / (od: 06.02.2019) /
Vklady: Svetlana Mackintosh / Vklad: 6 639 EUR Splatené: 6 639 EUR / (od: 06.02.2019) /
##### Credo
== CREDO - SK, s.r.o. | https://www.orsr.sk/vypis.asp?ID=227793&SID=5&P=0
IČO: 46 051 163 | Sídlo: Bánová 647, Žilina 010 04 | zápis: 16.02.2011
Spoločníci: RealMaR, s. r. o. IČO: 36 320 200 / 17. novembra 2868 / Čadca 022 01 / (od: 21.09.2022) / PeSo trading s. r. o. IČO: 54 993 351 / Námestie slobody 1901/66 / Púchov 020 01 / (od
… [5230 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/dvaja-slovaci-z-oxfordu-ziskali-417-miliona-eur-ich-technologia-moze-urychlit-liecbu-rakoviny/

→ `WebSearch` ZAKA VC invests 2026 seed round led co-invest Slovak startup

<details><summary>result</summary>

```
Web search results for query: "ZAKA VC invests 2026 seed round led co-invest Slovak startup"

Links: [{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"ZAKA VC Research","url":"https://f4.fund/firms/zaka-vc"},{"title":"ZAKA VC Overview","url":"https://pitchbook.com/profiles/investor/493759-63"},{"title":"Zaka VC se mění z rodinného na klasický startupový fond. Má stovky milionů korun","url":"https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/"},{"title":"Ján Búza zo ZAKA VC: Slovenský pôvod nie je v Silicon Valley prekážkou","url":"https://www.startitup.sk/?p=1130105"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/zaka-ventures"},{"title":"Velké startupové investice zamrzly a propouští se. Je to příležitost, říká Petrus ze Zaka VC","url":"https://www.e15.cz/byznys/technologie-a-media/velke-startupove-investice-zamrzly-a-propousti-se-je-to-prilezitost-rika-petrus-ze-zaka-vc-1396468"},{"title":"therecursive.com","url":"https://therecursive.com/?p=38085"}]

I didn't find a 2026 seed round by ZAKA VC in a Slovak startup, but the results give background on the firm and some recent deals.

**Firm profile:** ZAKA VC is a pre-seed and seed investor. Its core thesis is
… [1097 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** 7 October 2026, 09:59.

**ZAKA:** The sentence naming ZAKA is: "Startup od začiatku podporovali aj stredoeurópske fondy Kaya VC a ZAKA VC." It lists ZAKA VC as an early Central European backer, but it doesn't give the round size or lead investor.

**Round size and lead:** The article doesn't tie these to ZAKA. The Series A round, the first part of the package, was led by the British fund "ktoré viedol britský fond Oxford Science Enterprises." The full financing package is 47 million USD (about 40 million EUR), though the headline cites 41.7 million EUR.
```
</details>

→ `WebFetch` https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/

→ `WebSearch` LRJ Capital Ivan Chrenko investícia 2024 2025 startup GROWWS

<details><summary>result</summary>

```
Web search results for query: "LRJ Capital Ivan Chrenko investícia 2024 2025 startup GROWWS"

Links: [{"title":"Slovenský startup získal investíciu 1,5 milióna eur","url":"https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/"},{"title":"Ivan Chrenko","url":"https://en.wikipedia.org/wiki/Ivan_Chrenko"},{"title":"lrj capital fund","url":"https://www.crunchbase.com/organization/lrj-capital-fund"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/lrj-capital"},{"title":"ee.linkedin.com","url":"https://ee.linkedin.com/in/arturveeroja"},{"title":"Founders Eye $1.9 Billion Wealth Boost in India’s Groww IPO (1)","url":"https://news.bloomberglaw.com/capital-markets/founders-eye-1-9-billion-wealth-boost-in-indias-groww-ipo-1"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/ekonomika-firmy-jeden-z-nejbohatsich-slovaku-chrenko-presouva-svuj-miliardovy-majetek-do-ceska-267971"},{"title":"Groww IPO values founders’ stake at $1.85 Bn; Y Combinator set for 29X return in OFS","url":"https://entrackr.com/news/groww-ipo-values-founders-stake-at-185-bn-y-combinator-set-for-29x-return-in-ofs-10606647"},{"title":"ivan chern","url":"https://live.peievents.com/infrastructure-investor-global-summit/speakers-2/ivan-chern"}]

Search results show a 1.5 million euro investment by the GROWWS fund in the Slovak fintech startup Finax, but they don't give a date, so I can't confirm it falls in 2024 or 2025.

- **The deal:** A Startitup article repor
… [1104 more characters]
```
</details>

<details><summary>result</summary>

```
**Publication date:** 22 July 2024

- **Fund size:** "cílí na celkovou částku 15 milionů eur (přibližně 380 milionů korun)". The fund has already raised €10.5 million (about CZK 265 million) of that target.
- **Ticket size:** Not stated.
- **Team location (Prague/Bratislava):** Not stated. The article says the team has about ten people, but gives no office location. It says the fund initially focused on Central and Eastern Europe and later expanded to the UK and the US.
- **Founders' nationality:** Not stated. The article names the founders as Ján Kasper and Peter Zálešák and describes them as successful entrepreneurs, but does not give their nationality. It mentions a Slovak electronics retailer, Nay, but that is a company, not a statement about the founders.
- **Fund vehicle/jurisdiction:** Not stated. The article says the fund has opened to external investors for the first time, but does not name the legal vehicle or its jurisdiction.
```
</details>

→ `WebFetch` https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/

→ `WebSearch` "Monogram Ventures" Bratislava portfolio Websupport Piano Media fond

<details><summary>result</summary>

```
**Publication date:** 15 March 2019, at 14:51 (author: Linda Cebrová).

**Quote naming LRJ Capital and GROWWS SICAV:**
> "LRJ Capital cez svoj fond GROWWS SICAV, a.s. podporil inovátora v inteligentnom investovaní"

The article says LRJ Capital backed Finax through its GROWWS SICAV fund. The investment amount was €1.5 million, and the full sentence also names Finax.

**GROWWS registration:** The article doesn't say where GROWWS is registered. It only describes it as a professional venture fund whose significant shareholder is the investment holding LRJ Capital.
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Monogram Ventures" Bratislava portfolio Websupport Piano Media fond"

Links: [{"title":"www.eu startups","url":"https://www.eu-startups.com/?p=3200"},{"title":"Autor textu Martina Vojtěchovská","url":"https://www.mediaguru.cz/piano-ziskal-2-mil-eur-pro-placeny-webovy-system"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/monogram"},{"title":"WebSupport Overview","url":"https://pitchbook.com/profiles/company/103634-83"},{"title":"Shared Online Paywall Service Piano Media Secures 2 Million Euros From 3TS","url":"https://techcrunch.com/2012/04/17/shared-online-paywall-service-piano-media-secures-euro-2-million-from-3ts"},{"title":"Prehľad najzaujímavejších slovenských startupov: Ako začínali a ako sa im darí dnes? [2.časť]","url":"https://www.startitup.sk/local-prehlad-najzaujimavejsich-slovenskych-startupov-ako-zacinali-a-ako-sa-im-dari-dnes-2-cast/"},{"title":"Prehľad najzaujímavejších slovenských startupov: Ako začínali a ako sa im darí dnes? [2.časť]","url":"https://www.startitup.sk/?p=251376"},{"title":"Prihlásiť sa","url":"https://finstat.sk/44071574/obchodny_register"},{"title":"Product Reports Resources Pricing Login Book a demo","url":"https://dealroom.co/companies/piano/"},{"title":"3ts and aws gr nderfonds back piano media","url":"https://www.unquote.com/dach/official-record/72344/3ts-and-aws-gr-nderfonds-back-piano-media"}]

I found no source linking Monogram
… [1408 more characters]
```
</details>

→ `WebFetch` https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/

→ `WebSearch` IPM Group venture capital Peter Gajdoš investícia 2025 2026 startup

<details><summary>result</summary>

```
**Publication date:** 11 October 2019, 15:32.

**Investor sentence:** The article names IPM and Neulogy Ventures in one sentence, but it doesn't mention the amount there. The sentence reads: "anglicko-slovenský fond IPM spolu so súčasnými investormi z Neulogy Ventures" (IPM, an Anglo-Slovak fund, leads the first round alongside current investors including Neulogy Ventures).

**Amount:** The article says the startup "získal investíciu takmer jeden milión eur" (received an investment of nearly one million euros).
```
</details>

<details><summary>result</summary>

```
Web search results for query: "IPM Group venture capital Peter Gajdoš investícia 2025 2026 startup"

Links: [{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/peter-gajdos-sa-pripojil-k-ipm-do-tim/432852-clanok.html"},{"title":"Peter Gajdoš","url":"https://fifthwall.com/team/peter-gajdos"},{"title":"Judge, Silicon Valley, Global Finals","url":"https://www.vcic.org/peter-gajdos-presidio-2-2/"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"peter gajdos","url":"https://startupintros.com/people/peter-gajdos"},{"title":"top of page","url":"https://www.symsite.sk/single-post/ipm-raised-200m-from-investors-across-various-projects"},{"title":"Updated: June 13, 2026","url":"https://incubatorlist.com/ipm-group"},{"title":"peter gajdos","url":"https://www.evalyze.ai/investors/peter-gajdos"},{"title":"Investing Profile","url":"https://signal.nfx.com/investors/peter-gajdos"}]

The search didn't turn up any 2025–2026 IPM venture capital deals involving Gajdoš. The results mostly show his career history, and the most recent sources place him at Fifth Wall, not IPM.

- **IPM role (older):** A teraz.sk piece says Gajdoš, after years as a strategic adviser, became head of IPM's VC division and took on overall VC strategy, while keeping his Presidio Partners role. Peter joined IPM as the Head of Venture Capital in
… [1167 more characters]
```
</details>

→ `WebSearch` Sandberg Investment Fund II acquires Green Fox Academy 75% date

→ `WebFetch` https://oaklins.com/ar/en/deals/110583

<details><summary>result</summary>

```
The deal was announced in **May 2024**.

On the Eterus investment, the page states: "has received a significant investment from Eterus Capital and Ethernum Capital."
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Sandberg Investment Fund II acquires Green Fox Academy 75% date"

Links: [{"title":"Sandberg Capital Acquires 75% Stake in Hungary’s Green Fox Academy","url":"https://www.globalprivatecapital.org/?p=39400"},{"title":"sandberg capital acquires majority stake in hungary s green fox academy 260411","url":"https://intellinews.com/sandberg-capital-acquires-majority-stake-in-hungary-s-green-fox-academy-260411"},{"title":"sandberg capital acquires green fox academy","url":"https://en.ain.ua/2022/10/26/sandberg-capital-acquires-green-fox-academy"},{"title":"Assisting Sandberg Capital in the acquisition of a majority stake in Green Fox Academy31/10/22 / News","url":"https://www.ksb.cz/en/news-publications/01298"},{"title":"21473 ksb szecskay and dla piper advise on sandberg capital s acquisition of green fox academy","url":"https://ceelegalmatters.com/deals-and-cases/21473-ksb-szecskay-and-dla-piper-advise-on-sandberg-capital-s-acquisition-of-green-fox-academy"},{"title":"Advising Sandberg Capital on Major Education Transaction24/04/23 / News","url":"https://www.ksb.cz/en/news-publications/01320"},{"title":"122 private equity","url":"https://www.ceelm.com/by-practice/122-private-equity?start=420"},{"title":"sandberg capital closes second private equity fund sandberg investment fund ii","url":"https://www.privateequitywire.co.uk/sandberg-capital-closes-second-private-equity-fund-sandberg-investment-fund-ii/"},{"title":"asistence v dalsi vyznamne transakci
… [1362 more characters]
```
</details>

→ `Bash` — Check ORSR batch outputs
```sh
sed -n '/##### J&T VENTURES/,$p' [tmp] | cut -c1-500; echo; echo "=== B3"; sed -n '/##### PalmHR/,$p' [tmp] | cut -c1-1500
```

<details><summary>result</summary>

```
##### J&T VENTURES
##### INNOVATION FUND
##### Inovačný fond
##### Startlab
##### Fintech Ventures
##### Across Ventures
##### Ethernum
== Ethernum Capital s. r. o. | https://www.orsr.sk/vypis.asp?ID=653149&SID=2&P=0
IČO: 55 356 907 | Sídlo: Dúbravská cesta 14, Bratislava - mestská časť Karlova Ves 841 04 | zápis: 28.03.2023
Spoločníci: Equinox Capital s. r. o. IČO: 56 888 465 / Moskovská 2338/40 / Banská Bystrica 974 04 / (od: 02.04.2025) / POLAR CAPITAL s. r. o. IČO: 54 945 658 / Karpatská 1219/169 / Marianka 900 33 / (od: 02.04.2025) / King Capital s. r. o. IČO: 54 932 815 / Pivonková 1996/46 / Rovinka 900 41 / (od: 02.04.2025) /
Vklady: POLAR CAPITAL s. r. o. / Vklad: 2 250 EUR ( peňažný vklad ) Splatené: 2 250 EUR / (od: 02.04.2025) / Equinox Capital s. r. o. / Vklad: 2 000 EUR ( peňažný vklad ) Splatené: 2 000 EUR / (od: 23.05.2026) / King Capital s. r. o. / Vklad: 5 750 EUR ( peňažný vklad ) Splatené: 5 750 EUR / (od: 23.05.2026) /
== Ethernum Consulting s. r. o. | https://www.orsr.sk/vypis.asp?ID=726410&SID=2&P=0
IČO: 55 317 049 | Sídlo: Dúbravská cesta 14, Bratislava - mestská časť Karlova Ves 841 04 | zápis: 18.03.2023
Spoločníci: King Capital s. r. o. IČO: 54 932 815 / Pivonková 1996/46 / Rovinka 900 41 / (od: 18.03.2023) / POLAR CAPITAL s. r. o. IČO: 54 945 658 / Karpatská 1219/169 / Marianka 900 33 / (od: 09.12.2023) / Equinox Capital s. r. o. IČO: 56 888 465 / Moskovská 2338/40 / Banská Bystrica 974 04 / (od: 02.04.2025) /
Vklady: POLAR CAPITAL s. r. o. / Vkl
… [8059 more characters]
```
</details>

→ `WebSearch` "Ethernum Capital" investície Slovensko fond

→ `WebFetch` https://www.ethernum.com/

<details><summary>result</summary>

```
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

    Original URL: https://www.ethernum.com/
    Redirect URL (from the server's Location header — server-supplied, not verified): http://ethernum.com.mx/
    Status: 301 Moved Permanently

    To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
    - url: "http://ethernum.com.mx/"
    - prompt: "What is Ethernum Capital? Type (PE, VC, family office), HQ, ticket size (quote), sectors, portfolio and dates."
```
</details>

<details><summary>result</summary>

```
Web search results for query: ""Ethernum Capital" investície Slovensko fond"

Links: [{"title":"Zu den Deals","url":"https://www.oaklins.com/at/de/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/sg/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/at/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/br/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/fr/en/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/it/en/deals/110583/"},{"title":"Ir a las Transacciones","url":"https://www.oaklins.com/cl/es/deals/110583/"},{"title":"Transaktionen anzeigen","url":"https://www.oaklins.com/ch/de/deals/110583/"},{"title":"Go to deals","url":"https://www.oaklins.com/be/en/deals/110583"},{"title":"Go to deals","url":"https://www.oaklins.com/es/en/deals/110583"}]

Links: [{"title":"Go to deals","url":"https://oaklins.com/de/en/deals/110584"},{"title":"Go to deals","url":"https://www.oaklins.com/ie/en/deals/110584/"},{"title":"Go to deals","url":"https://oaklins.com/co/en/deals/110584"},{"title":"Go to deals","url":"https://oaklins.com/cn/en/deals/110584"},{"title":"Go to deals","url":"https://www.oaklins.com/ar/en/deals/110584/"},{"title":"Go to deals","url":"https://www.oaklins.com/cl/en/deals/110584/"},{"title":"Til transaksjoner","url":"https://oaklins.com/no/no/deals/110584"},{"title":"Go to deals","url":"https://www.oaklins.com/ma/en/deals/110584/"},{"title":"Transaktionen anzei
… [1546 more characters]
```
</details>

→ `Bash` — Prepare fourth ORSR batch script
```sh
cd [tmp] && cat > batch4.sh <<'EOF'
cd "$(dirname "$0")"
for n in "ZGC Fund" "Impact Ventures" "Baryon" "GROWWS" "LRJ Capital" "IPM Group" "IPM Growth" "United Founders" "Seed Starter" "Slovenská sporiteľňa Seed" "Launcher" "AceON" "Accace" "BaseTech" "Slovak Business Agency" "Jet Venture"; do echo "##### $n"; python3 orsr.py brief "$n" | cut -c1-700; done
echo "##### ICO 47759224"; python3 orsr.py ico 47759224
EOF
chmod +x batch4.sh
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Run fourth ORSR batch lookup
```sh
[tmp] > [tmp] 2>&1
```

<details><summary>result</summary>

```
Command running in background with ID: bem9r3m9u. Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
```
</details>

**Agent:**

The account limit is nearly exhausted, so I am recording the findings from the collected data now.

→ `Bash` — Build candidates JSON from collected research
```sh
mkdir -p [redacted: local path] && cat > [tmp] <<'EOF'
import json
A="2026-10-11"
def S(url,pub=None,note=None):
    d={"url":url,"accessed":A,"published":pub}
    if note: d["note"]=note
    return d
O="https://www.orsr.sk/"
SLOVCA_FULL="https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html"
SLOVCA_ASSOC="https://www.slovca.sk/sk/clenstvo/pridruzeni-clenovia.html"
EIF="https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf"
def R(name, **k):
    base=dict(name=name, management_company=None, fund_vehicles=[], ico=None, register_link=None, website=None, hq_city=None,
              proposed_type=None, sectors=None, stages=None, geography=None, ticket_min_eur=None, ticket_max_eur=None,
              fund_sizes=[], recent_investments=[], sources={}, evidence_quotes=[], decision=None, reason=None, found_via=None)
    base.update(k); return base
inv=lambda company,date,round_size,url,kind,pub=None: {"company":company,"date":date,"round_size":round_size,"source":S(url,pub),"evidence_type":kind}
C=[]
# ---------------- INCLUDE ----------------
C.append(R
… [41218 more characters]
```

<details><summary>result</summary>

```
49 Counter({'exclude': 38, 'uncertain': 8, 'include': 3})
```
</details>

→ `Bash` — Skim fourth ORSR batch results
```sh
cut -c1-300 [tmp] | grep -E "^#####|^==|IČO" | head -60
```

<details><summary>result</summary>

```
##### ZGC Fund
== ZGC Fund I., s.r.o. | https://www.orsr.sk/vypis.asp?ID=503429&SID=2&P=0
IČO: 52 768 058 | Sídlo: Staré Grunty 18, Bratislava - mestská časť Karlova Ves 841 04 | zápis: 20.12.2019
Spoločníci: Zero Gravity Capital s.r.o. IČO: 52 651 894 / Staromestská 7830/3 / Bratislava - mestská časť Staré Mesto 811 03 / (od: 08.01.2023) / National Development Fund II., a.s. IČO: 47 759 224 / Grösslingová 44 / Bratislava - mestská časť Staré Mesto 811 09 / (od: 08.01.2023) /
##### Impact Ventures
== Impact Ventures, s. r. o. | https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0
IČO: 55 927 033 | Sídlo: Framborská ulica 283/58, Žilina 010 01 | zápis: 08.12.2023
Spoločníci: CB ESPRI Impact One s. r. o. IČO: 54 546 702 / Staromestská 3 / Bratislava - mestská časť Staré Mesto 811 03 / (od: 08.12.2023) / Pontis Impact, s. r. o. IČO: 44 330 235 / Zelinárska 5389/2 / Bratislava - mestská časť Ružinov 821 08 / (od: 08.12.2023) / TnC X, s. r. o. IČO: 55 398 146 /
##### Baryon
== Baryon Consult, s. r. o. | https://www.orsr.sk/vypis.asp?ID=266832&SID=2&P=0
IČO: 47 146 818 | Sídlo: Veterná 982/22, Malinovo 900 45 | zápis: 14.05.2013
== BARYON s. r. o. | https://www.orsr.sk/vypis.asp?ID=33645&SID=2&P=0
IČO: 35 824 514 | Sídlo: Ružinovská 44, Bratislava 821 03 | zápis: 14.11.2001
##### GROWWS
##### LRJ Capital
##### IPM Group
##### IPM Growth
== IPM Growth s.r.o. | https://www.orsr.sk/vypis.asp?ID=450600&SID=3&P=0
IČO: 52 151 573 | Sídlo: Dolná 5, Banská Bystrica 974 01 | zápis: 04.01.201
… [2335 more characters]
```
</details>

→ `Bash` — Patch JSON with registry findings and build md table
```sh
cd [redacted: local path] && python3 - <<'EOF'
import json
p="sk-vc-candidates.json"; C=json.load(open(p,encoding="utf-8"))
A="2026-10-11"
for c in C:
    if c["name"].startswith("Impact Ventures"):
        c["proposed_type"]="impact co-investment SPV"
        c["register_link"]="https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0"
        c["sources"]["legal/owners"]=[{"url":c["register_link"],"accessed":A,"published":None}]
        c["evidence_quotes"].append("ORSR Impact Ventures, s. r. o. (zápis 08.12.2023): shareholders CB ESPRI Impact One s. r. o., Pontis Impact, s. r. o., TnC X, s. r. o.")
        c["decision"]="exclude"; c["reason"]="Impact SPV founded 08.12.2023 and owned by CB ESPRI Impact One, Pontis Impact and TnC X. It is a co-investment vehicle of impact funds, not a standalone VC manager."
    if c["name"].startswith("Zero Gravity"):
        c["fund_vehicles"]=["ZGC Fund I., s.r.o. (IČO 52 768 058; shareholders Zero Gravity Capital s.r.o. and National Development Fund II., a.s. since 08.01.2023)"]
        c["sources"]["fund vehicle"]=[{"url":"https://www.orsr.sk/vypis.asp?ID=503429&SID=2&P=0","accessed":A,"published":None}]
    if c["name"]
… [1459 more characters]
```

<details><summary>result</summary>

```
49 Counter({'exclude': 39, 'uncertain': 7, 'include': 3})
```
</details>

→ `Bash` — Write markdown summary and validate JSON
```sh
cd [redacted: local path] && { cat <<'EOF'
# Slovak VC investors — pilot sample candidates

Accessed 2026-10-11. Full evidence (per-field sources, quotes, registry links) is in `sk-vc-candidates.json`.
49 candidates: **3 include / 7 uncertain / 39 exclude**.

**Where the candidates came from:** SLOVCA full and associate member lists, the EIF list "Slovakia equity fund managers" (as at 30.09.2026), SIH intermediary pages, Startitup/Forbes/CzechCrunch/e15/Vestbee funding news, and directory lists (papermark, incubatorlist, vestbee 2020, podnikajte 2016, ain.ua 2022). Evidence of investments comes from ORSR shareholder entries ("od: dd.mm.yyyy").

**Inclusion rule applied:** the management company or fund vehicle is managed from Slovakia, or the investor is Slovak-founded with a Slovak investment team; it invests equity directly; and it has at least one dated investment.
**Excluded:** PE/buyout funds, corporate VCs (CVC), banks, public fund-of-funds and co-investment vehicles, accelerators, crowdfunding platforms, angel networks, Czech/Polish funds, and funds that are closed or dormant.

**Notes:**
- Of the task's seed names, three could not be verified an
… [1234 more characters]
```

<details><summary>result</summary>

```
json ok
      68 sk-vc-candidates.md
0
```
</details>

**Agent:**

[redacted: name]

Collected 49 candidates: 3 include, 7 unclear and 39 exclude. All 3 included candidates still carry caveats; only VFF appears clearly active now. I could not find a sourced count of Czech VC investors, so the Markdown file omits it rather than inventing one.

**Include:**
- **Neulogy Ventures** — Bratislava management company (IČO 47 367 610), SLOVCA member, included in the EIF list. I found no new investments after September 2024.
- **Vision Ventures** — its own Bratislava fund, co-owned by state-backed NDF II. The register lists startup ownership in Airvolute from 29.03.2025 and Spinbotics from 18.04.2024. Some entries are probably follow-on investments.
- **Venture to Future Fund** — investments in FaceUp (19.05.2026), Talentiqa (29.09.2025) and IAG (22.05.2025). State-owned, but invests directly on equal terms with private investors. Its investment period ends in late 2026.

**Unclear:** 0100 VC Fund II (Slovak team, Cyprus-domiciled fund), ZAKA VC, G-Force, CB Investment Management, Baryon Fund, LRJ Capital and IPM Group.

**Reasons for excluding the others:**
- **PE:** Sandberg, Eterus, Ethernum, ARX, Genesis.
- **Corporate venture funds:** Seed Starter Slovenskej sporiteľne, 365.fintech.
- **State entities:** SIH, NDF II, NHF, SBA.
- **Closed or dormant:** FIT, Zero Gravity Fund I, Limerock, Monogram.
- **Czech and Polish:** Credo, Presto, J&T Ventures, Nation 1, Jet and others.
- **Platforms, accelerators and angel network:** Crowdberry, AceON, Launcher, KPAS.
- **Banks:** Tatra banka, VÚB.
- **Unconfirmed entries from the initial list:** “Prvá kapitálová”, “Gapfunding” and “Monopoly Ventures”. “Nation1” was the Czech Nation 1; “Bitcoin funds” were not found; Swiss Re is a service centre rather than VC.

**Method:** finstat returns 403, so I queried the register directly through orsr.sk. Ownership-entry dates came from there and are the strongest evidence. Some `evidence_quotes` were paraphrased by the retrieval tool rather than copied verbatim; these cases are marked.

**5 weakest records:**
1. **Baryon Fund** — headquarters unclear (Bratislava or Prague); only one Airvolute registry entry.
2. **LRJ Capital** — latest investment found dates to 2019; the GROWWS fund’s domicile is unclear.
3. **IPM Group** — latest venture investment found dates to 2021; effectively controlled from the UK.
4. **G-Force** — recent investments are known only from the Caplight aggregator.
5. **CB Investment Management** — recent activity is supported only by an aggregator (participation in 3IPK’s crowdfunding round, May 2025).

**Failed to load:** forbes.sk, finstat.sk, sandberg.capital, tatrabanka.sk, techleap and the G-Force Fund II page.

All background registry requests have finished. Temporary files remain in this session’s directory. The reusable `orsr.py` script is in the same directory.

Files:
- [redacted: local path]
- [redacted: local path]

