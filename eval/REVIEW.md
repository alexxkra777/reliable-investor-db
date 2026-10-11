# Investor database: evidence review

Reviewed and confirmed by [redacted: name] on 11 October 2026. The assessment was prepared with AI assistance and subsequently reviewed by the project author.

## Review outcome

Of the 60 sampled claims, **58 are supported, subject to the qualifications below; 2 require correction**. The sample covers investor identity, investment activity and descriptive fields for Czech and Slovak investors. It was selected using the existing stratified sampling procedure with seed 7.

The findings apply to the sampled claims. They do not establish the accuracy of every database record or the completeness of the proposed global dataset. Both corrections have been applied to the current dataset. The findings and labels retain the original sample’s results for traceability.

## Required corrections

1. **Inven Capital — financial metric.** The source describes EUR 500 million as total committed capital. It does not establish assets under management. Record the amount under the appropriate capital metric and leave AUM unverified.
2. **Seed Starter / IntellCRE — announcement date.** The announcement supports the investment and the EUR 400,000 amount. The exact date, 17 September 2025, appears only in the URL. Leave the exact day unverified until a dated source corroborates it.

## Qualifications to retain

- **Tensor / Wultra:** the entry dated 3 December 2025 records a transfer of existing shares between Tensor entities. It establishes the registry date and ownership relationship. It does not demonstrate a new cash investment and should not independently satisfy the recent-investment rule.
- **StartupYard:** ICO 22266852 identifies the Batch 15 investment vehicle. The manager and the investment vehicle must remain distinct entities.
- **G-Force:** the commercial register gives a Bratislava address, while the NBS entry gives Trnava. Retain both source references and the discrepancy. A registered office is not sufficient evidence of the operating headquarters.
- **Financial figures:** retain the source date and metric definition. An undated published amount does not establish current AUM. A round’s total size does not establish an individual investor’s ticket.
- **Investment dates:** distinguish announcements, registry entries and transaction closings. Registration and portfolio listings establish identity or ownership; current investment activity requires dated evidence.

## Review approach

The assessment compared the complete source text and investor records. Automated quote matching and earlier model labels were insufficient on their own. Targeted live checks addressed legal identity, group ownership and disputed dates. Most checks used the project’s source cache collected on 11 October 2026; the review did not repeat a live crawl of every source.

Each finding below records the conclusion, supporting sources and any limits on interpretation. The accompanying `review-confirmed-labels.csv` contains the labels and notes confirmed during the author’s review. The detailed notes form part of those conclusions and should be retained when reporting the results.

## Detailed findings

### 1. N1 (Nation 1) — nation-1/field/aum

**Supported — see qualifications.** AUM of N1 (Nation 1): 35,000,000 EUR

The CVCA profile explicitly lists Volume of Funds Managed as EUR 35 million.

[Primary source](https://cvca.cz/en/nation1-2/)

### 2. BHM Ventures (BHM group) — bhm-ventures/field/existence

**Supported — see qualifications.** existence of BHM Ventures (BHM group): ["portfolio_page"]

The BHM tech-startups portfolio names Carebot, CloudTalk, GoRamp and multiple other holdings; this supports portfolio_page, not recent investment activity.

[Primary source](https://www.bhmgroup.eu/portfolio?industry=tech-startups)

### 3. Vision Ventures — vision-ventures/field/ticket

**Supported — see qualifications.** Ticket size of Vision Ventures: 100,000 - 1,600,000 EUR

The investor homepage states usual EUR 100k-800k tickets with an absolute maximum of EUR 1.6m; stored limits preserve the absolute range. New investment period ended in 2023.

[Primary source](https://visionventures.vc/)

### 4. Inven Capital — inven-capital/field/aum

**Not supported as written.** AUM of Inven Capital: 500,000,000 EUR

The homepage calls EUR 500m capital invested from institutional investors and later total committed capital. It does not identify this as manager AUM; PLAN distinguishes fund commitments from AUM.

[Primary source](https://www.invencapital.cz/)

### 5. StartupYard — startupyard/existence

**Supported — see qualifications.** StartupYard is a real investor of type 'accelerator' that still invests (HQ Praha, CZ; ICO 22266852).

The SmartGuide register identifies StartupYard Batch 15, ICO 22266852, as shareholder from 20 Aug 2026; accelerator page offers convertible-note investment. Live ARES confirms Prague address and the ICO. ICO belongs to a batch vehicle, not the accelerator manager.

[Primary source](https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1018928&typ=UPLNY) · [Additional source 1](https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/) · [Additional source 2](https://startupyard.com/) · [Additional source 3](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22266852)

### 6. J&T Ventures — jt-ventures/investment/0

**Supported — see qualifications.** J&T Ventures invested in Supernova on 2025-09-30 (announced), round 9,200,000 USD.

The Tech.eu article names J&T among participants in the USD 9.2m Series A and displays 30 September 2025. Investor blog has a different April article, which does not independently support this round.

[Primary source](https://www.jtventures.cz/blog) · [Additional source 1](https://tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-vibe-coding-to-enterprise-product-teams/)

### 7. CB Investment Management — cb-investment-management/field/funds

**Supported — see qualifications.** Funds of CB Investment Management: CB Growth ONE: 23,200,000 EUR, vintage 2019

The CBIM homepage names Growth One, EUR 23.2m fund size and 2019 founded; supports fund name, size and vintage.

[Primary source](https://www.cbim.sk/)

### 8. CB Investment Management — cb-investment-management/field/existence

**Supported — see qualifications.** existence of CB Investment Management: ["regulator_register", "fund_of_funds_commitment"]

The NBS page identifies registered alternative-fund manager, ICO 52524531; SIH page explicitly states its commitment to the CBIM-managed fund. SIH also says the fund is divesting.

[Primary source](https://subjekty.nbs.sk/sk/entity/5483/) · [Additional source 1](https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/cb-investment-management-kapitalova-investicia)

### 9. Seed Starter Slovenskej sporiteľne — seed-starter-slovenskej-sporitelne/investment/1

**Not supported as written.** Seed Starter Slovenskej sporiteľne invested in IntellCRE on 2025-09-17 (announced).

The cached and freshly fetched investor announcement confirms IntellCRE and EUR 400k, but does not state 17 September 2025. Raw HTML has no datePublished or explicit matching date; day is inferred only from URL, so exact announcement date is not independently supported.

[Primary source](https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne)

### 10. Miton — miton/existence

**Supported — see qualifications.** Miton is a real investor of type 'vc' that still invests (HQ Praha, CZ; ICO 25417967).

The homepage and portfolio show repeated venture investments; ACE release dated 1 Oct 2026 confirms current investing. Live ARES confirms MITON CZ, ICO 25417967, at the same Prague address.

[Primary source](https://www.miton.cz/) · [Additional source 1](https://www.miton.cz/portfolio) · [Additional source 2](https://www.miton.cz/blog/miton-investuje-do-ace-stravu-pro-padel-uz-pouziva-vice-nez-polovina-ceskych-hracu/) · [Additional source 3](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/25417967)

### 11. Neulogy Ventures — neulogy-ventures/field/sectors

**Supported — see qualifications.** Sectors of Neulogy Ventures: ICT, energy, medical diagnostics

The SLOVCA profile explicitly lists information and communication technologies, energy and medical diagnostics.

[Primary source](https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html)

### 12. Tensor Ventures — tensor-ventures/investment/0

**Supported — see qualifications.** Tensor Ventures invested in Wultra on 2025-12-03 (registry_entry).

The Wultra historical register records Tensor Co-Investment Fund entering on 3 Dec 2025, so registry_entry date is supported. The same two shares were previously held by Tensor Warehouse and transferred unchanged: do not interpret this as a new cash investment on that date.

[Primary source](https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=883583&typ=UPLNY)

### 13. Venture to Future Fund — venture-to-future-fund/investment/0

**Supported — see qualifications.** Venture to Future Fund invested in FaceUp on 2026-05-19 (announced), round 5,000,000 USD.

The article dated 19 May 2026 reports a USD 5m FaceUp Series A with Venture to Future Fund participation. This is secondary evidence, correctly Tier C; date is announcement, not verified closing.

[Primary source](https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/)

### 14. Czech Founders VC — czech-founders-vc/field/ticket

**Supported — see qualifications.** Ticket size of Czech Founders VC: 50,000 - 350,000 EUR

The investor homepage states pre-seed tickets typically EUR 50-350k.

[Primary source](https://czechfounders.vc/)

### 15. ZAKA VC — zaka-vc/field/stages

**Supported — see qualifications.** Stages of ZAKA VC: pre-seed, seed

The ZAKA homepage identifies the investor as a seed and pre-seed VC fund.

[Primary source](https://www.zaka.vc/)

### 16. Vision Ventures — vision-ventures/field/existence

**Supported — see qualifications.** existence of Vision Ventures: ["regulator_register", "fund_of_funds_commitment", "association_full_member"]

The NBS page names Vision Ventures and registered fund-manager status; SIH page states commitment; SLOVCA ordinary-member list includes it. These prove existence categories, not current new-deal activity.

[Primary source](https://subjekty.nbs.sk/sk/entity/5484/) · [Additional source 1](https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia) · [Additional source 2](https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html)

### 17. J&T Ventures — jt-ventures/field/ticket

**Supported — see qualifications.** Ticket size of J&T Ventures: 300,000 - 3,000,000 EUR

The J&T homepage states investment size EUR 300k-3m.

[Primary source](https://www.jtventures.cz/)

### 18. ZAKA VC — zaka-vc/field/existence

**Supported — see qualifications.** existence of ZAKA VC: ["portfolio_page"]

The ZAKA portfolio is titled global investment activity and names many portfolio companies, including the four quoted.

[Primary source](https://zaka.vc/portfolio/)

### 19. Vision Ventures — vision-ventures/field/geography

**Supported — see qualifications.** Geography of Vision Ventures: SK

The Vision Ventures homepage explicitly restricts investments to companies based and operating in Slovakia.

[Primary source](https://visionventures.vc/)

### 20. Vision Ventures — vision-ventures/investment/0

**Supported — see qualifications.** Vision Ventures invested in Airvolute s.r.o. (follow-on) on 2026-01-09 (registry_entry).

The current and historical Airvolute registers show Vision Ventures Growth I paid-in contribution increased from EUR 2500 until 8 Jan 2026 to EUR 3290 from 9 Jan 2026. This supports the labelled follow-on registry entry; date is registration, not proven cash-transfer date.

[Primary source](https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=0) · [Additional source 1](https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=1)

### 21. Vision Ventures — vision-ventures/investment/2

**Supported — see qualifications.** Vision Ventures invested in Seerlinq s.r.o. on 2023-07-14 (registry_entry).

The Seerlinq register names the company, Vision Ventures Growth I and EUR 1050 paid-in contribution from 14 July 2023. Date correctly labelled registry_entry.

[Primary source](https://www.orsr.sk/vypis.asp?ID=665401&SID=7&P=0)

### 22. Credo Ventures — credo-ventures/investment/1

**Supported — see qualifications.** Credo Ventures invested in Upheal on 2025-01-25 (announced), round 10,000,000 USD.

The Upheal page names Credo participation and USD 10m; its displayed date was refreshed to 9 Oct 2026. The Credo newsroom independently preserves the same announcement dated 25 Jan 2025, supporting stored announcement date.

[Primary source](https://www.upheal.io/blog/upheal-secures-10m-to-help-reduce-clinician-burnout-and-improve-client-outcomes-with-their-ai-powered-platform) · [Additional source 1](https://www.credoventures.com/newsroom)

### 23. Tilia Impact Ventures — tilia-impact-ventures/field/geography

**Supported — see qualifications.** Geography of Tilia Impact Ventures: CZ, CEE

The Tilia homepage states Czech and CEE founders; this describes founder origin and regional focus, not an exclusive company-domicile restriction.

[Primary source](https://www.tilia.vc/)

### 24. Credo Ventures — credo-ventures/field/geography

**Supported — see qualifications.** Geography of Credo Ventures: CEE, CEE diaspora

The Credo homepage explicitly says CEE and its global diaspora; geography is founder origin, not legal headquarters.

[Primary source](https://www.credoventures.com/)

### 25. DEPO Ventures — depo-ventures/field/stages

**Supported — see qualifications.** Stages of DEPO Ventures: inception, pre-seed

The DEPO homepage explicitly lists Stage: Inception & Pre-seed.

[Primary source](https://www.depoventures.com/)

### 26. Tilia Impact Ventures — tilia-impact-ventures/field/ticket

**Supported — see qualifications.** Ticket size of Tilia Impact Ventures: 300,000 - 1,200,000 EUR

The Tilia homepage explicitly lists EUR 0.3-1.2m initial ticket; the number is an initial-ticket range.

[Primary source](https://www.tilia.vc/)

### 27. Neulogy Ventures — neulogy-ventures/field/funds

**Supported — see qualifications.** Funds of Neulogy Ventures: Slovak Venture Fund S.C.A., SICAR: ? , vintage ?

The EIF partner PDF names Slovak Venture Fund S.C.A., SICAR and Neulogy Ventures as manager. No amount or vintage is claimed; unknowns are retained.

[Primary source](https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf)

### 28. J&T Ventures — jt-ventures/field/geography

**Supported — see qualifications.** Geography of J&T Ventures: CEE, SEE, Baltics

The J&T homepage explicitly lists CEE, SEE and Baltics as investment region.

[Primary source](https://www.jtventures.cz/)

### 29. Neulogy Ventures — neulogy-ventures/existence

**Supported — see qualifications.** Neulogy Ventures is a real investor of type 'vc' that still invests (HQ Bratislava, SK; ICO 47367610, company_number B185175).

The EIF PDF confirms manager and venture-capital strategy; MultiplexDX register records its fund and B185175 with paid-in contribution from 17 Jan 2026. Live manager register confirms ICO 47367610 and Bratislava. SIH-backed older compartments are divesting, while EIF partner table lists investment end in March 2027.

[Primary source](https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf) · [Additional source 1](https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia) · [Additional source 2](https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=0) · [Additional source 3](https://www.neulogy.vc/) · [Additional source 4](https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0)

### 30. RockawayX — rockawayx/field/stages

**Supported — see qualifications.** Stages of RockawayX: early stage

The RockawayX homepage explicitly says it invests in early-stage projects. This alone does not establish equity-only VC activity; the record remains uncertain.

[Primary source](https://rockawayx.com/)

### 31. G-Force — g-force/existence

**Supported — see qualifications.** G-Force is a real investor of type 'accelerator' that still invests (HQ Bratislava, SK; ICO 53527798, ICO 53588398).

Official NBS entry confirms the manager and fund. The live commercial register confirms manager ICO 53527798 and Bratislava registered office; NBS instead shows Trnava, a source discrepancy to retain. The archived Founders Factory announcement explicitly names the G-Force investment in Enzidia on 11 March 2025. Registered office is used as a proxy for HQ; it is not independently established as the operating headquarters.

[Primary source](https://subjekty.nbs.sk/sk/entity/5492/) · [Additional source 1](https://foundersfactory.com/g-force/) · [Additional source 2](https://www.orsr.sk/vypis.asp?ID=608015&SID=2&P=0) · [Additional source 3](https://www.orsr.sk/vypis.asp?ID=659572&SID=2&P=0)

### 32. Vision Ventures — vision-ventures/investment/1

**Supported — see qualifications.** Vision Ventures invested in BiteBerry s. r. o. on 2023-08-09 (registry_entry).

The BiteBerry register names Vision Ventures Growth I and paid-in contribution from 9 August 2023. The company was subsequently renamed. This is a registry-entry date, not an independently confirmed closing date.

[Primary source](https://www.orsr.sk/vypis.asp?ID=694090&SID=5&P=0)

### 33. Venture to Future Fund — venture-to-future-fund/investment/2

**Supported — see qualifications.** Venture to Future Fund invested in Talentiqa on 2025-09-29 (announced), round 1,100,000 EUR.

The Vestbee announcement dated 29 September 2025 names Talentiqa, VFF and Purple Ventures in the EUR 1.1m round. Amount is the total round, not VFF’s individual ticket.

[Primary source](https://vestbee.com/insights/articles/talentiqa-raises-1-1-m)

### 34. Credo Ventures — credo-ventures/field/aum

**Supported — see qualifications.** AUM of Credo Ventures: 170,000,000 EUR

CVCA profile explicitly states EUR 170m volume of funds managed. The profile has no financial as-of date; do not represent the figure as current 2026 AUM.

[Primary source](https://cvca.cz/en/credo-ventures-2/)

### 35. Tensor Ventures — tensor-ventures/field/ticket

**Supported — see qualifications.** Ticket size of Tensor Ventures: 250,000 - 1,000,000 EUR

The CVCA profile gives EUR 250k–1m investment size. This is the published range, not a measured distribution of completed tickets.

[Primary source](https://cvca.cz/en/tensor-ventures/)

### 36. Zero One Hundred (0100 Ventures) — zero-one-hundred/field/existence

**Supported — see qualifications.** existence of Zero One Hundred (0100 Ventures): ["regulator_register", "fund_of_funds_commitment"]

NBS identifies Zero Gravity Capital and SIH confirms its fund commitment. A live commercial-register check independently links Zero Gravity Capital to its sole shareholder 0100 Ventures (ICO 50209728). These support group-level existence; SIH’s older fund is divesting.

[Primary source](https://subjekty.nbs.sk/sk/entity/5486/) · [Additional source 1](https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia)

### 37. Zero One Hundred (0100 Ventures) — zero-one-hundred/field/geography

**Supported — see qualifications.** Geography of Zero One Hundred (0100 Ventures): Emerging Europe, Middle East

The investor website explicitly identifies Emerging Europe and the Middle East as its investment focus.

[Primary source](https://0100.vc/)

### 38. Inven Capital — inven-capital/field/sectors

**Supported — see qualifications.** Sectors of Inven Capital: climate tech

The investor homepage explicitly describes its climate-technology investment focus.

[Primary source](https://www.invencapital.cz/)

### 39. J&T Ventures — jt-ventures/field/aum

**Supported — see qualifications.** AUM of J&T Ventures: 120,000,000 EUR

The J&T homepage states EUR 120m in assets. The source does not provide a financial as-of date.

[Primary source](https://www.jtventures.cz/)

### 40. Credo Ventures — credo-ventures/existence

**Supported — see qualifications.** Credo Ventures is a real investor of type 'vc' that still invests (HQ Praha, CZ; ICO 28538137).

The CVCA profile and investor homepage support venture-investor identity. Live ARES confirms Credo Ventures a.s., ICO 28538137, and Prague registered office. The separately reviewed Supernova announcement supports activity within the 36-month window. Registered office is a proxy for HQ.

[Primary source](https://cvca.cz/en/credo-ventures-2/) · [Additional source 1](https://www.credoventures.com/) · [Additional source 2](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/28538137)

### 41. Vision Ventures — vision-ventures/field/stages

**Supported — see qualifications.** Stages of Vision Ventures: pre-seed, seed

The Vision homepage states pre-seed and seed focus. Its initial investment period ended in 2023; stage focus does not itself demonstrate current new-deal activity.

[Primary source](https://visionventures.vc/)

### 42. DEPO Ventures — depo-ventures/field/funds

**Supported — see qualifications.** Funds of DEPO Ventures: DEPO Ventures One SCSp: ? , vintage ?

Official NRI page identifies DEPO Ventures One SCSp as a selected financial intermediary. The claim leaves size and vintage unknown.

[Primary source](https://www.nrinvesticni.cz/)

### 43. Soulmates Ventures — soulmates-ventures/field/sectors

**Supported — see qualifications.** Sectors of Soulmates Ventures: air, water, energy, mobility, education, healthcare, food and agriculture, circular economy

The Soulmates homepage lists the claimed sustainability-related sectors. These are stated focus areas rather than exhaustive portfolio classifications.

[Primary source](https://www.soulmates.ventures/)

### 44. Venture to Future Fund — venture-to-future-fund/field/funds

**Supported — see qualifications.** Funds of Venture to Future Fund: Venture to Future Fund: 55,000,000 EUR, vintage ?

The VFF homepage identifies EUR 55m allocated for investment during 2020–2026. This supports the amount as investable capital; it is not NAV or current AUM.

[Primary source](https://vff.sk/) · [Additional source 1](https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov)

### 45. Baryon Fund — baryon-fund/field/sectors

**Supported — see qualifications.** Sectors of Baryon Fund: defence tech

The Baryon homepage explicitly identifies defence technology as its sector focus.

[Primary source](https://baryon.fund/)

### 46. Venture to Future Fund — venture-to-future-fund/field/sectors

**Supported — see qualifications.** Sectors of Venture to Future Fund: innovative SMEs, technology SMEs

The SLOVCA profile identifies innovative SMEs and technology-oriented SMEs. These are broad strategy descriptions, not mutually exclusive sectors.

[Primary source](https://www.slovca.sk/sk/riadni-clenovia/venture-to-future-fund.html)

### 47. J&T Ventures — jt-ventures/investment/2

**Supported — see qualifications.** J&T Ventures invested in Finlay on 2025-03-03 (announced), round 300,000 EUR.

J&T blog lists the Finlay announcement on 3 March 2025; the related interview describes the EUR 300k pre-seed round with J&T and DEPO participation. Announcement date is not a verified closing date.

[Primary source](https://www.jtventures.cz/blog) · [Additional source 1](https://www.jtventures.cz/blog/investice-do-naboroveho-startupu-finlay)

### 48. KAYA VC — kaya-vc/field/stages

**Supported — see qualifications.** Stages of KAYA VC: pre-seed, seed

The KAYA homepage describes pre-seed and seed rounds. Later-stage follow-ons are not ruled out by this initial-stage focus.

[Primary source](https://www.kaya.vc/)

### 49. Czech Founders VC — czech-founders-vc/existence

**Supported — see qualifications.** Czech Founders VC is a real investor of type 'vc' that still invests (HQ Praha, CZ; ICO 17051835).

The Edmund registry records Czech Founders Ventures, ICO 17051835, entering as shareholder on 25 March 2026 with a concurrent capital change. This supports legal identity, Prague registered address and recent investment activity.

[Primary source](https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1199826&typ=UPLNY) · [Additional source 1](https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1096675&typ=UPLNY) · [Additional source 2](https://czechfounders.vc/) · [Additional source 3](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/17051835)

### 50. Credo Ventures — credo-ventures/investment/0

**Supported — see qualifications.** Credo Ventures invested in Supernova on 2025-09-30 (announced), round 9,200,000 USD.

Credo newsroom and Tech.eu article both identify the 30 September 2025 Supernova USD 9.2m round; Tech.eu explicitly lists Credo among participating investors.

[Primary source](https://www.credoventures.com/newsroom) · [Additional source 1](https://tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-vibe-coding-to-enterprise-product-teams/)

### 51. Reflex Capital — reflex-capital/investment/0

**Supported — see qualifications.** Reflex Capital invested in Ranketta on 2026-10-07 (registry_entry).

The Ranketta register identifies Reflex 3 entering on 7 October 2026 with a preferred share and a concurrent capital increase. The claim correctly uses registry_entry, not transaction closing.

[Primary source](https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1288906&typ=UPLNY)

### 52. Fond inovácií a technológií — fond-inovacii-a-technologii/field/ticket

**Supported — see qualifications.** Ticket size of Fond inovácií a technológií: 20,000 - 1,500,000 EUR

The SLOVCA profile states EUR 20k–1.5m ticket range. The record is dormant; this is the published historical mandate, not evidence of present deployment.

[Primary source](https://www.slovca.sk/sk/riadni-clenovia/fond-inovacii-a-technologii.html)

### 53. Limerock — limerock/field/existence

**Supported — see qualifications.** existence of Limerock: ["regulator_register", "fund_of_funds_commitment"]

The NBS entry confirms the renamed Limerock entity and registered-manager status; SIH page confirms its fund commitment. The SIH-backed fund is divesting, so existence does not establish current new investments.

[Primary source](https://subjekty.nbs.sk/sk/entity/308293/) · [Additional source 1](https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia)

### 54. Czech Founders VC — czech-founders-vc/investment/1

**Supported — see qualifications.** Czech Founders VC invested in SharpGrid on 2023-08-30 (registry_entry).

The historical SharpGrid registry records Czech Founders Ventures entering on 30 August 2023 alongside new preferred shares and a capital increase. A later address/name update is not counted as another deal.

[Primary source](https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1096675&typ=UPLNY)

### 55. Venture to Future Fund — venture-to-future-fund/field/existence

**Supported — see qualifications.** existence of Venture to Future Fund: ["regulator_register", "association_full_member"]

The NBS entry confirms the registered alternative fund and manager; the SLOVCA member page supports association membership. These are existence categories rather than activity measures.

[Primary source](https://subjekty.nbs.sk/sk/entity/5190/) · [Additional source 1](https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html)

### 56. Tensor Ventures — tensor-ventures/field/funds

**Supported — see qualifications.** Funds of Tensor Ventures: Tensor Ventures Fund I SCSp: ? , vintage ?; Tensor Co-Investment Fund SCSp: ? , vintage ?

The EIF list identifies Tensor Co-Investment Fund SCSp and Tensor Advisory; Tensor’s own site identifies Tensor Ventures Fund I SCSp. Size and vintage are correctly left unknown.

[Primary source](https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf) · [Additional source 1](https://tensor.ventures/)

### 57. Czech Founders VC — czech-founders-vc/field/geography

**Supported — see qualifications.** Geography of Czech Founders VC: CEE

The investor homepage explicitly states its CEE regional focus.

[Primary source](https://czechfounders.vc/)

### 58. Neulogy Ventures — neulogy-ventures/investment/2

**Supported — see qualifications.** Neulogy Ventures invested in Trustmatic on 2023-10-24 (announced).

The Neulogy news page embeds the Trustmatic investment announcement with a 24 October 2023 timestamp. This supports announcement date, not independently verified closing.

[Primary source](https://neulogy.vc/news/)

### 59. Orbit Capital — orbit-capital/field/stages

**Supported — see qualifications.** Stages of Orbit Capital: growth

The CVCA profile identifies growth equity and venture debt. The stored growth stage is supported, but does not mean every investment is equity.

[Primary source](https://cvca.cz/en/orbit-capital-2/)

### 60. ZAKA VC — zaka-vc/field/sectors

**Supported — see qualifications.** Sectors of ZAKA VC: health & biotech, industrial tech

The ZAKA homepage explicitly identifies Health & Biotech and Industrial Tech as focus verticals.

[Primary source](https://www.zaka.vc/)
