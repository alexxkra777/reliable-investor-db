# Codex: blind second review

Codex CLI session log (main thread and its helper threads), exported from `rollout-2026-10-11T06-13-07-01a1292a-18a0-7c81-afad-2387d759a56a.jsonl`, `rollout-2026-10-11T06-13-22-01a1292a-5533-7c93-b051-8625925be47b.jsonl`, `rollout-2026-10-11T06-13-26-01a1292a-65ec-72d1-a56d-0b846e07aaa2.jsonl`, `rollout-2026-10-11T06-13-30-01a1292a-75ce-70c3-8b88-3666c485d759.jsonl`.
Tool outputs longer than 1,500 characters are shortened; model reasoning is not stored in readable form by Codex and is left out.

## Thread `2026-10-11T06-13-07`

**Brief / message:**

You are an independent fact-checker. Work in /Users/[redacted]/homeW/ai-dev-test/investor-db, but read ONLY the file eval/second-opinion/input.json (a list of organisations: id, name, country, website). Do NOT open any other file in the repo (no data/, research/, PLAN.md) — your answers must be independent of an earlier assessment.

For each organisation answer, from public web sources you check yourself (use web search and curl):
1. is_investor: "yes" / "no" / "unclear" — does it invest its own or managed capital as equity (or convertible) into private companies, as a core activity? (Crowdfunding platforms, advisers, banks' lending, grant programs = "no".)
2. type: one of vc, pe, cvc, family_office, angel, private_investor, accelerator, fund_of_funds, public_dfi, platform, adviser, other.
3. managed_from: ISO country of the team/manager that makes the investment decisions.
4. latest_investment: the most recent DATED investment you can find: {company, date (YYYY-MM-DD, or YYYY-MM-01 / YYYY-01-01 if only month/year known), date_precision: day|month|year, url, quote}. The quote must be copied verbatim from the raw page text (fetch it with curl and check with grep) — not from a search snippet or a summary. If you can't find any, null.
5. active_36m: "yes" if latest_investment.date >= 2023-10-11, "no" if older, "unclear" if none found.
6. confidence: high / medium / low, and a one-sentence note.

Budget: about 6 searches per organisation; don't get stuck. Write the result to eval/second-opinion/codex.json as a JSON array (same order, include id). Write nothing else, run no git commands, don't mention tools or AI in the file. Print a 5-line English summary at the end (counts per is_investor and active_36m).

**Codex:**

[redacted: name]
Прочитаю только указанный входной файл, независимо проверю организации по публичным источникам и сохраню результат в `eval/second-opinion/codex.json`.


→ `exec`
```
text(await tools.exec_command({cmd:"cat eval/second-opinion/input.json",max_output_tokens:12000}));
text(ALL_TOOLS.filter(x=>/search|browse|curl/.test(x.name+" "+x.description)).map(x=>({name:x.name,description:x.description.slice(0,120)})).slice(0,70));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"51a7cd\",\"wall_time_seconds\":0.000002084,\"exit_code\":0,\"original_token_count\":1403,\"output\":\"[\\n  {\\n    \\\"id\\\": \\\"365-fintech\\\",\\n    \\\"name\\\": \\\"365.fintech\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": \\\"https://365fintech.sk/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"air-ventures\\\",\\n    \\\"name\\\": \\\"Air Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"baryon-fund\\\",\\n    \\\"name\\\": \\\"Baryon Fund\\\",\\n    \\\"country\\\": null,\\n    \\\"website\\\": \\\"https://www.baryon.fund/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"bhm-ventures\\\",\\n    \\\"name\\\": \\\"BHM Ventures (BHM group)\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"cb-investment-management\\\",\\n    \\\"name\\\": \\\"CB Investment Management\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": \\\"https://www.cbim.sk/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"credo-ventures\\\",\\n    \\\"name\\\": \\\"Credo Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.credoventures.com/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"cs-seed-starter\\\",\\n    \\\"name\\\": \\\"ČS Seed Starter\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.see
… [21166 more characters]
```
</details>

→ `spawn_agent`
```
{"task_name":"check_first","fork_turns":"all","message":"gAAAAABqywzi20KugQTJWYMfaSb-L0xenFPl1vVcHvUBKD65AuBR0cwmohrfwzWVSyYErsE5U9jd_bESVHtjUeahuDUFv5RJ-SZYo8xgnqQxx5Ual-U7_Juv6INMJgJyZoH4Juf3bA47jSiQN3E0Vy2YGxWGjcwBnGlAtZPKTEt1Xfedsc-jda-ZElFPZ9kUlk_bLOoGFB_p9_i1j0_SpMVfj9P76xjfGaVGpmS4acp9NHjeOXsN1DNbmgKVX0e7S8c6lQHYM_ufoAZs7vPVw6a7cOUT_vWnrIbTLxmbwexXvrcg76NoBB3x4QVN725r9QKKsHWkENiO99dEYT8XlHCN9iPEmCkrEsCs35mauMsnsy3sTEew77HkkeHHGYO_XBLGEz-qdGc6WnT6zN0BwbMpWhh7IbyDzE9UtE-W7YKFFn7j6ct7iDGC7LCUAQIGmtewrj1WiNvLFsFpjvcFKZFlS0OITkKzYhLmtRzOdLpp1PiV71bHVABsTh2qLJp3KzsCIu-Y_wifRUjHxDxaBOdUeXnlY_s4Wj_UKleEebIsxuXYePFlXmpmXch9XRfkkxi0LEt14cFJwexXRFh60bRlAD7V_M56mI5bdnDjgGmXA1qfd6Pvdb8qk0P7F0Ak5E76cruaYiTYQ3_seAUbewESc6V65tuogZiCbsFvUnOrodOm_o3ctvo82IyzlLk9i7uZZqloKtPbtxI0q2AK5zSwZjtfLxfvI-wsSO54Al3EZ0ysyoH3ZafH1OgzLU4IOJcHccdH15ZoloJ63kJuswh_rxCZhSomf83LDN5QHBvBgA6wI0kAcL_5zTfSWYAmqLqP5lBSgu41aE0OGDae7Xx4SV13lC3e9x-FzIdNzQWIZj9ylqZX4X1SFb4CUcCi9jyO_wPqHdIkNiNniIldfzF06d_qx-hG8TgPkQ-6x_dLLExyRnMHyY6kfi7GJIT-FCOZUTyw981a4kDnScp9-FnxRaBah_L5TQFd37OsN1lheAfP5Rgnq5iq0S-ZS9zKwXqnSopt6CgnkOs7wwZytnY_8FO8tUvByZMu5_V0FIUFsC6zFr5Iyv2YETkf6JkAQjVLLjCn_Ad5T9oHeJbZq6KU6N3tmMuQTg=="}
```

<details><summary>result</summary>

```
{"task_name":"/root/check_first"}
```
</details>

→ `spawn_agent`
```
{"task_name":"check_middle","fork_turns":"all","message":"gAAAAABqywzmIZ-1oVhsvf-GefUxrd2TYH0u6LgaE40tP0BsZYGCZbjKDFuYbQ_Vj0QNfZ9htXV7MX7SVfcUR-Xl3ueFnK9H1EXea5G_ZwbVGCWFoFnnT05ikO-ywzK8PT306uvcY-DTYlgXevY0lJ4_qcedDL4mFT1Iy7Jy8O7gSXzoocU0CPsc0rhIquNX23oaIop_qVd6xbfbX9JZpfZwsxcNrGrs8krzfF8RfErMOhiAgH5LCVgDlc1kPsUtXO8qYWF7y4Lo7bPw9oOnycP9Myod2FaUx8nF2Mq6M_tQtUg1FzPzIbz-x-VxTliA63-yjz-EgMQD4BCq6KW5Snstbf6H-9S8QOZ3irNd198eQz_J5kWz8P5cUi_u0O4BshLifCtBP4mbU-eEKnFJrqfob5azONGw0iihQvxYEw9ZJf2f4DNcEUk2JUhJbC6kQJj7BALyeox6JqK6Iyo81o1e-keWhOdA2XO32CDHY7ql2a3VijIFE14nM9R8XuU56eQvmEFb1OMneZJYMuNCvtVI8_c4WOpGp8UwSy-ifuW9J1pAA-cwgLtJBmlQSrJVO8wgfjGjsbvP-bi64VQzm6JiM2G5aIPyLQ76tDtP7nZRhPslZLFtI9OmwUqfDP47LQUsHCrdwOYNjnBIQhRQZbUaVP0E8epxif12BIVzXoO-_3umYPUXkir34OYb_5fEsC6UtHBAMyS3jePy3p8ktY5TavST4wG_AFfSqCss0JRvi0ma6fccQY6HUAvgZ0jbDqQFx71mwJd066H9ImOXLBcECG5sUUok_v5o8bay8MKDr95LX7rdHto5JAbr7Xgd6-fmybO-ttOB9vCDUT3LvVmxzH7pMvwqsu2qYcOucFGLNbVqWmyhuxcz3bwLSX16TeABGpOEmkiA6pDS8b8iyMbF4zgr4te_g9DltX5BYuzrD_qM3T5sXE_VQVH0zz7dC6Xs0OwYtcxa8irDnknfTfxAsLJRnMtKaHjocU1ap4Lqg-BEsmDBYElepdSwF7Lfau8qHVwl8e4RBey96A3MpZJIuW5XRNbn5AYg3YbhRJGiNu35Go8BsMsxNF9VEJIfkyZMYz0TfESA"}
```

<details><summary>result</summary>

```
{"task_name":"/root/check_middle"}
```
</details>

→ `spawn_agent`
```
{"task_name":"check_last","fork_turns":"all","message":"gAAAAABqywzqFW9WtkNCeUlSS8BWBAAr6FBwFmLfBdC6W9j-ASNHIyz4B2fKpwyddzP08jvjDf4S1Ln4F01t8nUs01USJlySx9KHCG8vyG7-qMxZSKR6EPnl3cwlDIb_HnRDXWHTM_jywATUXpAIXbPotdV2BMXYtAk_gF-Ir7z2mGFqFKZzm0J9xAIXdTI6R_moMd4OHodKH022KsR4os0CdrlaUo6-5HDZycS3ywMQHDttPH7MSgDkGzhaJGoy8ssi_X_atfnfkYAYVKg55o9iz8r_sSGWYgA5gD7rPc6ssXuxum4I5SmSoTV3JkVes_N7bEafvh3YypfcvmQjqVY1oy6f8IlYZeiYmFmscLOyG-rhyuG7nXjEC3FOuE-v6SXc5EWl2Vf3sZty735Qs7fuEgK0j7piLZRDKfW98c8n0KTbepuqYZdrsRv76PQy-ttT-njh56WKOJrSp8FplkFOnDUkpfbARqBjT1xnurV8NnoghTTpIvGlCtEpYrLrd6IHeuzPEklLdogHVWtWtDjNkLxFfIBVRm3hNxYOr93R71sOvBeuB5ot8YOGAhFQoVwErCZf0E8Fwn0Ff1l4V8uTeE0Sxxk5_F4jk3-at5Y3b_Q3XpTiAv_U7baGmxc0euc7qSX2uLnrg-qC9mbiIz83641hfUsiX2RRfh4-mBTWd0djjjFve4X8bLpV9Kyyxzud55oGBrhHGbKQ8LkXzBzkHZlF89A1I1vaElBiNOFPehxogXn6OdmMJJZImEEdE3IsMm-kuNKrLzTZOWDaqvlZ0qNAYPsbSr5pq8K3T68RMPvpLKgQbGNVdOKIj_y8XaOijcotX4yVfOsROkomFFthnrR9yW03lb0aTRVNKChiv-Q5Hg460wbaUHKBW23xXrmPUMIW39Bbp-l1lCAEOI_QD9zsfl-YwQgg0l-uYm6moIU8WMtVoXgTcrZrhrL050OU6s8hlGqiqXwiHCtbZDED4Km4GPQFgewnFjiy2tZwe0x9CDUKhfPTsl1Fxpcxo380qATbaDOOJZHeCpzw836ZkuP9rWfhbVt_OVs0GpB00ygCN71qScg9PN70pP13MmFbPMA3FWez_Dl6aveGMKW-h5ydi7_QLg=="}
```

<details><summary>result</summary>

```
{"task_name":"/root/check_last"}
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Baryon Fund" investment portfolio team'},{q:'"GAIN Ventures" investment Czech'},{q:'"STARTGUIDE" investice startup fond'},{q:'"0100" ventures fund of funds investment team'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "STARTGUIDE – Navádíme na správnou cestu (https://startguide.cz/)\nciteturn1search0 [wordlim: 200] Crawled: 3 weeks ago; ### Jako tým vášnivých nadšenců pro startupy s pevnými podnikatelskými zkušenostmi jsme odhodláni pomáhat startupům k úspěchu prostřednictvím CHYTRÉHO KAPITÁLU.Ve STARTGUIDE přinášíme více než jen kapitál. ... Upřednostňujeme investice do technologických startupů ve střední a východní Evropě, protože věříme, že tento region má silnou základnu talentů a rostoucí technologický ekosystém. ... Jste fond?\n# Podporujeme digitální startupy,aby tvořily hodnotu a přinášely pozitivní změny.\n\nInvestoři podporující digitální startupy v rané fázi v regionu střední a východní Evropy. Přinášíme jedinečnou podporu s praktickým přístupem.\n  * # O nás\n\n## Jsme preferovaným investorem pro startupy a partnery, kteří hledají přidanou hodnotu\n\n### Jako tým vášnivých nadšenců pro startupy s pevnými podnikatelskými zkušenostmi jsme odhodláni pomáhat startupům k úspěchu prostřednictvím CHYTRÉHO KAPITÁLU.Ve STARTGUIDE přinášíme více než jen kapitál. Náš praktický přístup zahrnuje úzkou spolupráci se zakladateli startupů na strategii, produktové vhodnosti pro trh a škálování jejich podnikání k dosažení vedoucí pozice na trhu. Naše investiční filozofie jde nad rámec finančních výnosů a klade důraz na inovace, realizaci a růst.Jsme finančním investorem, ale v
… [32216 more characters]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqywz1xiZT7QDWeJN7jw8CoytP4nN5Uw3UqKucUyMk5A__UKJcxcLfBVKD0neBPOAtJyXVeG3F36vKTfXvGXqvFOZq-VGRRFyQkjxZF-qi_Z5C3WNe_HTZyDNA9FfxQF0HA8zuWJ9xxmnZlzWN0EoRm4tBOIeO6j_rvt456WfyqPztK3YzJ7SSFuByOmP5lTQuF0KHS6f21P-XqO-e0k72G1BEJGs4zlPHT4sBLHw0a7SzD9qqAFwdGoZiZfi3A4dcq_RSU6HLcCoSf_vu0S_2foHv6bnUQ9_8O38B1E8Xey_m6I36j3MjC1QiHY5FyP5YbhStCVBlGoNFD_SBSRL-7lgvCI1zPqvrlvB5MCjqMztbl-uXQa5KovGgo-BjUirjxcqjkNIOp8Xx_tIZEdN8-6WhqPn6GBOQE7acYGUAg46JXFn6cKe8hJEf5M8Y99FbRgn_mKu8ftFOV2fKk_1Rkc-JIpfJYkbaxC7gerc-76nCVtUq-BJe7EuxgZpU85couPdN8AXb6L5BmbEexhx34RW_8LPn_vvqPzbvxhqh6vI4qmQ="}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_last","message":"gAAAAABqywz67eHJ1TIZ4x-p_GImuhMXHwB2NsriNCNaqaH2RZXQx9OLOga7N5waO689q6qa-S6MtThdhqSc2g1BMVsc52KUIXTkvOK9JoNhRjCYZYAlZEJDqN3UpJcvYYbaqSLv-x88XAFASPPEzTv_4ddT6Zd_8R6oR6VJZKWt44zj-mso876cNvKwzJF7xo-41qcXi2qmMDknPvD6IvLUm9kWLR51XfKbpUakOJKYUQfFrYqZKTwgsOxRA0tvryfgneTAkjNiRwhFnbdm9NMooC3SgVnzbztxgh85saz0YrikxIKSUTnkOBQbb5qFnsf9w2IXMXQ_Csr-YLA2PdoXFE4y6qQy1R67zeY18ijxWkQpl8fylS2RnADLMtGF-HQ7JbTT5nZE3f7QxgnPfrCo7zRrQrlfbqlzclt_KghMeSZ0aDp8OsVT6TOysVC7QUoitjBqOwl9cv-h5smyr8b_E4VuPR99bNSiX9dOv8LZRe3zpoon6UhPBwS3smumU_dh95xr6S2Je_JX0Wn5z9wp2_Pv9EqHTXD_UiGy2HR80hvE1I2nkXI="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"IPM Group" investment team Bratislava London managed 2025'},{q:'"Limerock" investície fond tím 2025'},{q:'"LRJ Capital" investment 2025 2026'},{q:'"Monogram Ventures" Slovakia investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "Team | IPM (https://www.ipmgrp.com/team/)\nciteturn11search0 [wordlim: 200] Crawled: 3 days ago; # Team of investment professionals ... #### London ... #### Bratislava ... “IPM” and “IPM Group” are business names of IPM Group Holdings Limited, a Company registered in England and Wales with company number 11719671 and InfraPartners Management s.r.o, a company existing under the laws of Slovakia with ICO 47743034 and DIC 2024080916.\n\n# Team of investment professionals\n\nPlease meet our team below.\n\n  * Read more\n\nFounder & Managing Director Adrian Vycital Co-Founder Marian Bocek Head of Sales Mario Vircik Of Counsel Michal Kilian Head of Finance and Operations Michal Rakay Controller Katarina Marko Paralegal & Compliance Associate Miroslav Baňár Analyst Michal Kozelka Office Manager Barbora Koprdova Operations Manager Viktoria Szaboova\n\n#### London\n\n123 Pall Mall London SE1 9RA United KingdomImage\n\n#### Bratislava\n\nSavoy 2 at Carlton Mostova Street 4 Bratislava I\n\n## Stay in touch\n\n## Bratislava\n\nSavoy 2 at Carlton\nMostova Street 4\nBratislava I\n\nE-MAIL\n\nbusiness@ipmgrp.com\n\n* * *\n\nImage: IPM LLC\n\n“IPM” and “IPM Group” are business names of IPM Group Holdings Limited, a Company registered in England and Wales with company number 11719671 and InfraPartners Management s.r.o, a company existing under the laws of Slovakia with ICO
… [23725 more characters]
```
</details>

→ `send_message`
```
{"target":"check_middle","message":"gAAAAABqyw0H7uW8KO6ncaKCvlXYBhK5gvg43HdAInA86YM8LaWJgM5Rod0KcuyDGmlFHo0FuOWtedlHCIs3WxQqdu0WHUAgLqpCh2ZKrwYWcEW9aMHeC8H8U9LfES2iMddvDo4oj049donw_qgxESFEPfI5sTtcmnYHUNJk7ys7CaVQovKHMSaMU1TXYb1tsvnZ8HvHNx6aATc9IlfELw53NoTsI2Wp0XgBaJEGtewYXygU-fqBxn_HT3bWidodUzm1A4Ux_HV3FsYp2FuGKGL46bvdW30qJ2QgT3Di6CSZ1u4UuNZ2NnZyf5gJAX_e2tkb5w_Y8gE0vIOXeby0HV6yjYos6ASP25ZnPWK6mmDu8STtmn9OS_zhIQbQLQJF27NJYmXtQ5R3ihNi6h6I5Ag5JqLr9bEkTekIOKrZDcLhmQSls45heqmCLdG0pzVzhEZlkzfXM2d8biRWXMSu2-kglUIHgyJRtL_wLUaX5L8mtC-Vo0mbQzhCjC9fnRxiCKJA38QQ534x2fun55_jCxJ67JDMuAAaBlTSEZcdwbO8-RbXutM3nEtUpnSd0YT2T8grgxNGCudjZ-qdTN50YcLlBicHHKRb3dudBnrqgVPHniB63PbAJ-d6VyzeszsngrdB_UFHzUiHMNI2dNE8vsNbDUkxVo9spihWZ_y8o1a_c0TIGqMTopfJcE0BvjtH0EMNIh9INnUz6uOWw2dv29mmQk3ATADdvsi_qL_1g-D1nsfp0pYvYL-W0m4hW0wM-p991PlTk-_MSRph3GO6LHqAK9b91tgDpJc0Fa-tTgonCvjTQanvp0UKvPDbe8sTNWixZ92c4-v8Qfqnqd-N8eZev7h_g4tEW_Zh3B2R7WQkO4dcSzIjkvg="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://www.ipmgrp.com/team/','https://www.limerock.sk/sfdr','https://startguide.cz/en/','https://www.0100.vc/','https://www.baryon.fund/']\nfor u in urls:\n p=subprocess.run(['curl','-L','-sS','--max-time','35',u],capture_output=True,text=True)\n raw=p.stdout\n raw=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>',' ',raw,flags=re.S|re.I)\n txt=html.unescape(re.sub('<[^>]+>','\\n',raw))\n txt=re.sub(r'[ \\t]+',' ',txt)\n lines=[x.strip() for x in txt.splitlines() if x.strip()]\n print(u, 'curl_exit',p.returncode)\n print('\\n'.join(lines)[-16000:])\nPY","max_output_tokens":8500}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"7db89d\",\"wall_time_seconds\":1.99903575,\"exit_code\":0,\"original_token_count\":8375,\"output\":\"https://www.ipmgrp.com/team/ curl_exit 0\\n-->\\nTeam | IPM\\nAbout us\\nInvestments\\nTeam\\nContact\\n×\\nAbout us\\nInvestments\\nTeam\\nContact\\nTeam of investment professionals\\nPlease meet our team below.\\nRead more\\nFounder & Managing Director\\nAdrian Vycital\\nCo-Founder\\nMarian Bocek\\nHead of Sales\\nMario Vircik\\nOf Counsel\\nMichal Kilian\\nHead of Finance and Operations\\nMichal Rakay\\nController\\nKatarina Marko\\nParalegal & Compliance Associate\\nMiroslav Baňár\\nAnalyst\\nMichal Kozelka\\nOffice Manager\\nBarbora Koprdova\\nOperations Manager\\nViktoria Szaboova\\nLondon\\n123 Pall Mall London SE1 9RA United Kingdom\\nBratislava\\nSavoy 2 at Carlton Mostova Street 4 Bratislava I\\nStay in touch\\nBratislava\\nSavoy 2 at Carlton\\nMostova Street 4\\nBratislava I\\nE-MAIL\\nbusiness@ipmgrp.com\\n“IPM” and “IPM Group” are business names of IPM Group Holdings Limited, a Company registered in England and Wales with company number 11719671 and InfraPartners Management s.r.o, a company existing under the laws of Slovakia with ICO 47743034 and DIC 2024080916.\\nCreated by\\nStudio Echt\\nAbout us\\nTeam\\nInvestor\\nProject Developer\\nContact\\nhttps://www.limerock.sk/sfdr curl_exit 0\\n-->\\nSFDR | Limerock Investment Holding
… [32789 more characters]
```
</details>

**Codex:**

[redacted: name]
Проверка идёт по всем 45 организациям. Отдельно проверяю страну управляющей команды и даты сделок: регистрация фонда, привлечение денег в сам фонд и выход из компании не подтверждают новую инвестицию.


→ `exec`
```
text(await tools.web__run({search_query:[{q:'"LRJ Capital" investment latest 2025 2026 Bratislava'},{q:'"Monogram Ventures" investment Streamstar 2015 2016'},{q:'"Baryon" investment drone 2026 2025 fund'},{q:'"Startguide" investment 2026 2025 startup'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "STARTGUIDE – We’ll guide you onto the right path (https://startguide.cz/en/)\nciteturn21search0 [wordlim: 200] Crawled: 3 weeks ago; ### STARTGUIDE's unique approach combines financial investment with strategic mentorship and network access.At STARTGUIDE, we bring more than just capital to the table.Our hands-on approach includes deep collaboration with startup founders on strategy, product-market fit, and scaling their business to achieve market leadership.Our investment philosophy goes beyond financial returns, prioritizing innovation, execution, and growth.We are a financial investor but for selected startups also provide mentoring (up to 160Hour/year). ... Start Guide, s.r.o., Opletalova 1015/55, Nové Město, 110 00 Praha 1\n# We empower digital startups to create value and drive positive change.\n\nEnterprenerues investing in early‑stage digital startups in the CEE region. We are bringing hands‑on unique value.\n  * # About us\n\n## STARTGUIDE is a venture capital fund that invests with a hands‑on approach, bringing added value to investors, startups, and partners.\n\n### STARTGUIDE's unique approach combines financial investment with strategic mentorship and network access.At STARTGUIDE, we bring more than just capital to the table. Our hands-on approach includes deep collaboration with startup founders on strategy, product-market fit, and scaling the
… [31215 more characters]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw0bqGDO0J9TqipiDq98HlL_g9lqEn8Zm8YQ64ncc5oKxR1Wx0zp_65Lu9moSdGNrrK602j63ae4S6vUOexI3tgb-OamCU3Y5fF1924oxN8R0oRtiF_qcjcBjB9QW-jC_OsIbXNJUWIwYPRTxdd8Qi7UvJUeUami81ky7GhvdaIvrKU92HoitVinOw_wUwb537rmMm4_xKEm0gBAZzhBmQClhHGXuHuLtCUe-1OHJ5W7UzKG4Wq55muQzK1fAI6LfVnKp-1jxOb-z8s1E7S81Zy_lT68jueCsfgpcGhFQq3DISd5iJsPL1Jjg-7zdt_oYggbOg9iEuj7Eio9o-aNqoJ2VR245RUGEva9kcVZg7gTW5jOG6UKEEph38l2Y1F_EC9M0b6Tw3WKC0LaAzlUMg-jmJuCmK1jtEoXrhSQov3bF4MWtQYGLlNP7jnaXmvHkW61UElme2SkMnRUwB880P3bDs6qP7XmIapXVyDGXdEdF5kWvUglzGr8X2GYHVf6-x6S"}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"StartGuide" investice startup 2025 2026'},{q:'"STARTGUIDE" invested funding 2024 2025 2026 -site:fundraisingfox.com -site:village.ai'},{q:'"LRJ Capital" "2024"'},{q:'"LRJ Capital" "2025"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "StartGuide Portfolio Investments, StartGuide Funds, StartGuide Exits (https://www.cbinsights.com/investor/startguide)\nciteturn27search0 [wordlim: 200] Crawled: 4 weeks ago; Karla Engliše 3201/6 Smíchov ... ## StartGuide Investments ... Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024. ... 5/31/2024  | Pre-Seed  | Subscribe to see more  | $XXM  | Subscribe to see more  |  | 0\n\n# StartGuide\n\nstartguide.cz\n\n## Are you an investor?\n\nSubmit your portfolio details now to be considered in our investor rankings.\n\nSubmit portfolio details\n\n## Investments\n\n16\n\n## Portfolio Exits\n\n1\n\n## About StartGuide\n\nStartGuide is a Czech incubator. It was founded in 2021 and is based in Praha, Czech Republic.\n\n## Headquarters Location\n\nKarla Engliše 3201/6 Smíchov\n\nPraha, 150 00,\n\nCzech Republic\n\n\n## StartGuide Investments\n\n16 Investments\n\nStartGuide has made 16 investments. Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024.\n\nImage: CBI Logo\n\n### StartGuide Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n11/30/2024  | Pre-Seed  | Airline Pilot Club  | $0.7M  | Yes  |  | \n11/20/2024  | Pre-Seed 
… [28867 more characters]
```
</details>

→ `send_message`
```
{"target":"check_last","message":"gAAAAABqyw0oGxuViUWm3TwbPJJQc2LvwtV7fEMW6znM_JRziVLQiBEvzzpiN2HWEU7WIvdZZx29YLjBs4QXPNqkU6dZsidG6Q79ioSYo0W9obf60xTLTRgi5m59mugAEGSsOGxbHitqraWnm2lD6cmrYcO4QOyITufS3V2hIEz9ZR6eD7xiIfuSMGHZjekCwZVXaBXhZV9lsx7Dybpo8g-QqNSniNWWirA-ecg9XwhAJZUzsklVJIqe4bM5oYFbp8iTsbruK5M0yYX0mGjJ4NyFndwPYaVpkS3IqEXO_MnxyKQ1gs-slcRWAzftlQOrbpTIWk7GKRNxtH836kOBTVNBHuJE_MgR0AYcWfnNHmodp_4jl0LmIcNYVrxM2_WvHehHku4QS_7MB_kAeVo8dklYKTy-YpWvbNTxjm22iNOPfO0Mwkp0-TVQBIGLmP0LCPIRX_-GpMKF2J-7MX2WEDP_xfXeErTSCVw0E74QR-BaHBmNZVK77KpEv5o4ryODoL_372pA7JYNZshLCt2RHIHMeb-yTGZferYKPC7WCVsSeGQ8u9-gYS97zmt2LE7f3B6PdRl5SNkL7PLjN9xf-Azy0gysIUW2mdSnfuY4UBNs6KzsfUaIxgc="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"LRJ Capital" investment'},{q:'"LRJ Capital" headquarters team'},{q:'"Monogram Ventures" "invest" "2016"'},{q:'"Monogram Ventures" "invest" "2018"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Expertná štúdia a stratégia pre rozvoj (https://web.vucke.sk/files/dokumenty/pub/regionalny_rozvoj/phsr/2015/prilohy/priloha_5_expertna_studia_a_strategia_pre_rozvoj_kreativnej_ekonomiky_kosickeho_kraja.pdf)\nciteturn31search12 [wordlim: 200] Published: 2.1 years ago; LRJ Capitalwww.lrjcapital.c ... Investment\nTabuľka č. 2.74: Zoznam investorov \nNÁZOV \nWEB \nPOPIS \nLRJ Capital \nwww.lrjcapital.c\nom \nwww.crowdberr\ny.sk \nInvestujú najmä do firiem s už na trhu prítomným produktom, \nktorý je otestovaný prvými zákazníkmi. Výška investície \nvaríruje od 100k do 1,5 milióna EUR, pričom optimum je na \núrovni okolo 0,5 milióna EUR. Medzi investície patrí napríklad \nAeromobil, slovenský lietajúci automobil, či Challengest, \nslovenská inovatívna HR platforma a poskytovateľ riešení \nv tejto oblasti. Spoločnosť investovala aj do zahraničných \nfiriem, napríklad z Česka, Nemecka, USA a Izraela.  \nCrowdberry \nCrowdfundin\ng \n(Bratislava) \nwww.limerockf\nund.com/sk \nEquity \ncrowdfunding \nplatforma, \nktorá \nspája \nprivátny \ninvestorský klub s dynamickými podnikateľskými nápadmi. \nPrirovnáva sa k private bankingu vo svete startupov. \nCrowdberry nie je spoluinvestorom, ani investorov nezastupuje, \nlen \nspája \nponuku \ninvestícií \nso \nzaujímavými, \npred-\nselektovanými \nprojektami \na firmami. \n------------------------------------------------
… [24651 more characters]
```
</details>

→ `send_message`
```
{"target":"check_middle","message":"gAAAAABqyw0zpX9ktA_3tXL4OoTZoJz7SHxst5hP4HCUsbeBVBmzFXFSSDZmZPDcta3y9ztwICWKS4WcLrDEaGlK9HBwoNNnkKr6ejlPfbNFqKa-91BKTUvpNdCCyzPz8gFFV8DmvcaaBHUZdazy0MFYkOSVdL1UpAvlpmQLlrtATKaZJQ72_Mb8eVasEH9g0QaeqIcuF6DbsE-zXvi0UP8l5WemdPqSlX_gb0c2W1_vLmFj-C-7K3dKSyRtlKrod9zI8W4cH9NR6JwqY-CGBnrkJpd_bpdfpHYeLNzihwOyKzpPeIDnHpsht0mF_m0-ER6A-bLopv0d0ft6PxemwklfZMQ96e_6p4k4LIcZRmkLbPguvFNPlrT6IwnZMwDI7IeKZ0aGIbpHGd1sHOURk8FtVxKVjpoKVnfTKOH54OOH62l3LqWAKz65pEInk57RLH0GGPbQTSD1xSUSZTyL6a1WH_pAXXtj4uquGh0Xq3JSu9WmF9MeZArMyuZHaY8JPAoRWu_CwS_8EiLS6oyNLsGfJfNNDSp7KfmT6ONeCVAQNZG3tprJj-gYq9X4GXCMdkEaPP4n5vG2ASJBbWSEHxGByW_82PF3H8UnPX-gzaPOU5HIhB9aiTgkkDX8DNRc4tPZrvRKAlbnLN4UtlwXT68DCuMKYhuolwar40sSqjN5Lz-CxWY5AMJmnFnGdOjANDD-WQyUT6Sgpheih_Yo-0n7zwDXDcfcMlLWFG_NiehJe0qnueXRXBfsFL1XWmEUscWglh-HMKN3kvb8zMnpb3sOwfcdwQfZAwW0QFAPeTG9__HydCUC_tE="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Air Ventures" investment 2026 2025 Czech'},{q:'"KOOPEO Ventures" investment 2026 2025'},{q:'"G-Force" venture capital managed Bratislava London'},{q:'"RockawayX" equity token investments 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Funds (https://www.rockawayx.com/funds)\nciteturn40search0 [wordlim: 200] Crawled: today; 1.6% ... Building on the success of Fund I, this fund provides capital to early stage companies and protocols in the blockchain ecosystem that offer a high potential return over its investment time horizon.The fund achieves its mandate by pursuing opportunities in the full spectrum of blockchain assets, with a focus on the Solana ecosystem and decentralized finance (DeFi) and infrastructure protocols where RockawayX is a primary liquidity provider or provided custom hardware support. ... Our first venture capital fund, launched in 2021, focussed on companies and projects that would accelerate the nascent blockchain and DeFi ecosystem.It made direct equity and token investments and invested in selected other digital asset funds.\n\n# Proven Track-Record\n\n// Our funds offer investors varied exposure to the fast growing digital asset space.\n\n## RockawayX Liquid Opportunities Fund\n\n[Active]\n\nA fundamentals-driven, directional long/short fund, actively managed to take advantage of crypto market volatility.\nFocus on liquid tokens and listed crypto-related equities. Thesis-driven underwriting, complemented by crypto-native analysis of market structure, liquidity, flows, technicals, and sentiment positioning.\n\n### //Fund type\n\nOpen ended\n\n### //Liquidity\n\nMon
… [30620 more characters]
```
</details>

→ `send_message`
```
{"target":"check_last","message":"gAAAAABqyw1Dw3d_3SLLR-M8nSkjitAYR-Ggx0LlhmLfPsFfnqguyFFDaayUMzHJhqRJbbgwlBjeOgJAkMWkFJW51U378spCqnQ4vbHyTq34V_eAtzjp3TEVpQOyFgse5r4Q6pSNzx2xHQIVL0zRBIRTslLS1Thvaxx0s0EEGc9LGlsTR-m4txGilODhRcSH-5VqlWIjoWVtH2MznSTZqkag0I3h6Yoiq7Tj5uQVRgiaELKNYCV9KFBJiEl6Fok3BfbYGegdx5R4k_dEQv2avWd3xAQGdnVkVYmp7qJ7ZLFlTb1PqcjKMTE9mOTD_Gx_DeBupBlQhpBkZzhgjc2goumWj6OF1hIdqsXUO4MMaTzmTVtNrEr_OO8LUpZYV_lznFHGCnqlHHv3fKQiwlsB-hRNBJMqEvnyr9svC9882xzkBbhrlWlbcHJo3mW5WKt7N0UJz8G48cX_qGYvQaOxyAUVRUjnaDxBkUzGb3I1Y0WBJBojQqqYO8x_dzdRkejss-C1NPaeZJUso4xTa9RgNdZpfWUtt_byRw=="}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw1H029U9jommlb37V8_YDdjNT-71lCujaofwEHhdcaGKgW4Uxsci6MrcfZwbgraPxwrP6-zdhbKuhd1JWd4wl7kj63CbCSvkkMA1mxjh3XzDfqLg6B-4DkBUSc6A7lvOcsLWbsLmHvEwG9EoyHxN9dqqLYBXl4j1TVmI5XYTB2GQHNTAgbYftt7WjpItvEGMFRVY_k_yX8UMnKW9qRmDMHfYhC3MY0daiHHDlNRtfNNmj3r0NFqKihQ6cWM8PKP5VgOg2toRf1Nf4K_cmVo5xUlXPjxlutgNlLeSz2jDlGwCIIXGsu6_GznVj5mJg9kozwKuaQ_6ZvuJ8qzkD2MInUJcduHUeaO9mindeQw4GR-vysg205d304R6s_tRTuwXK1CzSXkMlfZJDSCPhjyd-tFFMRNfU9dEtvk_3l_WyaomPQYtisWflRgmaQsmf7fqVG0VtF5cE8J2o8dfNv82bwvEaVl2QEiU86VV60HG2VxmAhxW7SR8-UlL5ctGq4zlJlsS94b_WvaM9holUdNcavo55iA3KS1aQC_7kStydC36poI4tLR9W1AoVxpWxyK0mo9hHU6YYlU72cDDEhJZaaoOQ=="}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw1QXHohhwzyZl59y9Cbb1NRwrn6S5d_HwJHyG90bdYPAN80OvwET7Kr4UP70SX4SEbudFTiWOfhhwiaGnBrvhGPDK6NkWMP4d3nSQjZzd0nhrM9W3hUKI4WoEyV36C-LfupRaQVpoSxKuLKqJq4AfP6J4iK-dK0qEjlTin8RsuEOI385-5gwkuYT4tFnIYh2t3ZHmW5G9ql5MEoMzXX-CflK9xF2mEhDUFWbrCEuJCramtUn8Sdsv-olUuUpESQQRKYmM2GBrtMk-8iCoNl4jkbOT3kLQUa-u4PtLKJoBrjxjU1_rbqe6lq3Ay-lqMH2p4BkyL4vokYD_kcGmzsw_aPjh2_m4dhTZFVP06Z-wzaJe6Jh1p3CrIyNvi4emrJr-mHhGRDWWsPNEwrLp5UDWEszgmoSs29i7XILsn4VSHRpa5AphEVQ75qbRi7cHxNuOYh4umHhUPTwhhSQxEXocO_s6GMcQP0dnzzynTx8WAh44E="}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_middle","message":"gAAAAABqyw1TZhvMtrsGYuUC7bj1JBudyUHKIi3u0Plj8PHpLMGMtHIXNnXmuaBUYecvzVWiiO0y05KtNvBkoWK24MiViIbA6-qHgRfCBp7uwZQJKy30151VAv-laoVdd354dgmVj5zvuK3JQKHndMmQuKkgLqRABkqUomnytcJky4qHIyrRKWk5zPfKljBUli1Qj6MHlgEwdGQKpPfdhFI4kSQVrpMshZKruiExpDEipXzLjnq-pqIaBWbxxsrQLRrOcxIfNX8lZg--d23MJzdQvbFVtwt93YkNV7Wq_L72Sb2JD-LcleAsj_Zgeq1eR1DTGVsfUtPqk-lsHJC_KvwjMFydchnlBtN_Q2FnOetDHD3kR6jvj7Y="}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_last","message":"gAAAAABqyw1W0XVSvgoRMCyIJFivEmhoK-ELMRlBv9Tta-S7tPn8L6BNY_y-wQZIhznu_RLkNnQwgVkZbx9XqVKukjW2cfzcSP_sjOjh9DLXGmDFFCPL0RlsIsFRqyR47JvnH033mEjQPQnFGiVCo2DO0t3N3czEBmOkEiYEGB7VpLqT6UCabX3NH_buhOPnj1eYJb5BeGs7tnq7DeoEmfWmcT48-gE5-v3q2LWr_ZlrhyqlwCNmZD22iHqdQhyJnIaFAxucDxubIfix536NykYheWQ52g_wuYq7y4u5K1_wVhl3lHOMjIRtw8bm7TzprL_MVI2jBLDBLYa48gyHqLYoK1WqiwoLy-5tFazUXppmhaiQMwHQ7o8="}
```

<details><summary>result</summary>

```

```
</details>

**Codex:**

[redacted: name]
Нашёл несколько неоднозначностей: одноимённые зарубежные организации и старые сделки на страницах с недавней датой обновления. В результат попадут подтверждённые даты; если датированную инвестицию найти не удалось, оставлю `null`.


→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Air Ventures" Czech investment 2025 2026 InsightART'}],response_length:"long"}));
text(await tools.web__run({search_query:[{q:'"365.fintech" investment 2024 2025 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 14118)\nTotal output lines: 1059\n\nInsightART s.r.o., IČO: 03479676 - rejstřík firem - Finmag.cz (https://www.finmag.cz/obchodni-rejstrik/03479676-insightart-s-r-o)\nciteturn50search0 [wordlim: 200] Crawled: 3 days ago; 2016 InsightART s.r.o. zapsáno 25. ... 2025  | Zapsán společník AIR VENTURES s.r.o.\nCo zde najdete\n\nKontaktní údaje\n\nPoslední změny a události\n\nSbírka listin\n\nInformace o podnikání a činnosti\n\nMajetek\n\nPersonální obsazení, vedení\n\nVizualizace vztahů\n\nHodnocení společnosti\n\nSídlo společnosti na mapě\n\nKontaktní údaje\n\nPro tento subjekt neevidujeme žádné kontaktní údaje.\n\nPoslední změny a události InsightART s.r.o. - dle obchodního rejstříku\n\n8. 8. 2026  | Změna adresy: člen statutárního orgánu Jan Sohar\n16. 8. 2025  | Nová listina ve sbírce listin: C 231235/SL26/MSPH účetní závěrka [2024] - předána prostřednictvím správce daně z příjmů k 16.08.2025\n27. 4. 2025  | Zapsán společník AIR VENTURES s.r.o.\n27. 4. 2025  | Vymazán společník AIR VENTURES s.r.o.\n18. 7. 2024  | Nová listina ve sbírce listin: C 231235/SL24/MSPH účetní závěrka [2020] rozvaha\n\nCelá časová osa\n\nSbírka listin společnosti InsightART s.r.o. - Typy listin: účetní závěrka, výroční zpráva, zakladatelské dokumenty.\n\nČíslo listiny  | Vznik listiny  | Typ listiny  | Založeno do SL  | Stránek\n--- |
… [38441 more characters]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw1qv6LGrNvw5_Jy_j8Ic5ovLDCczGFquRT2DPxKxa6JI4smxSojCccc3c7_TUObHNnzZP35801n4DW7Bfjw5IQxq-GvqNytwqwqugpVKOGb2sfL-QF59qpFwbcHRMjFo2t4xf5jp9hwVXpQ2aVLExqdsvzj8MiBh-4Y5gkcj7RXSP02315wFAB-v8Qi1AcDlnJFxtAuOMue0przYrrmc0P47zqYg7knDqcgbTnmN7AO16_vJXKyA2UjBuV4rV2d8ZSZ7mCs5vSj3I0eU_HGPJKVN7i8qLdS9VzbFgjilbHad-z93dndqeAGyZ2iuwYENGvoJtJCJuDMvJrJfm_W6wdC2xXZ6bAoSCOTItyZ9JGM5ZpMRUtuhV0Un8LVge6o5sRpcYjg7jWUqBq9vWvsu45Smm9Mde_UbNmUoJ2Z8QncBX1YEqtKo13Zy59VmM0wl3s_H7vvvCBuGCGdgBvWycFTH4j7DSqK7-vhuK4WxKafbNKy6IZMdzMd5E5XfavaI7XSpuCJpa0Wyix56C5Kf_KR82GhhidU5EGotrhiAk8zn6rxcv3XpMc_8i2x-7MZFBnst0RPPbYmJQmvjy-LVi-B2rzV9-Xg9hrHUT6FELGjkTisr_P6LALiwNYTQJTMDEo9l0Xj-Zi5DabH34ywsFF3eA=="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Air Ventures" "Cross Network" investment'},{q:'"Air Ventures" "investment" "2022" Prague'},{q:'"Air Ventures" "investment" "2023" Czech'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "JANUARY 2020 — ACROSS THE WIRE (https://ceelegalmatters.com/Magazines/ISSUE_CEELM_6.12_free.pdf)\nciteturn54search12 [wordlim: 200] Published: 6.8 years ago; <td>MCL advised Air Ventures, a start-up investment fund, on the acquisition of a 15% stake in Czech mobile provider Cross Network Intelligence from two unnamed individuals. ... <td>ODI advised the Czech Republic’s Ministry of Finance and its state-owned IMOB and PRISKO subsidiaries on the sale of a majority stake in Vipap Videm Krsko, a large Slovenian paper mill and newsprint manufacturer, to Czech-based Ridg Holding.</td>\n<td>Kinstellar, Soltysinski Kawecki &amp; Szlezak, and Cobalt have advised Stada Arzneimittel on the acquisition of Walmart from Mid Europa Partners. White &amp; Case and Weil, Gotshal &amp; Manges advised the sellers on the deal.</td>\n<td>N/A</td>\n<td>Czech Republic; Estonia; Hungary; Latvia; Lithuania; Poland</td>\n</tr>\n<tr>\n<td>22-Nov</td>\n<td>Abraham &amp; Partners; MCL</td>\n<td>MCL advised Air Ventures, a start-up investment fund, on the acquisition of a 15% stake in Czech mobile provider Cross Network Intelligence from two unnamed individuals. The sellers were advised by Abraham &amp; Partners.</td>\n<td>N/A</td>\n<td>Czech Republic; Slovakia</td>\n</tr>\n<tr>\n<td>25-Nov</td>\n<td>ODI Law</td>\n<td>ODI advised the Czech Republic’s Ministry of Finance and its state-o
… [27661 more characters]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw1yciu8fNh3umtJMRHRg119pKJPHNjf3xHkRpLBB4AQhbhHgEh9eacKo1J7_5qEnyKMiQKyXGhBzggM1WY-1y86VBfvw3j8MXvmp1ezREuJK8ZGvZMIiXBenPSKRkPDvqcS-t-UlhvEnptzBrCaSNGaVrGgG7lBaU62G8fB6-yOEJa-1mUrb2CSh7gXrDL2qoLAWBiCn9eYEcT-FZSqT6rM-aTy30e6wrYW4VmyAgBRQuGV-fg23Uj_qH4TBAUL3-tX0GdbVcoTYeKqWDKevCYEhlapXzqS3KDgGxfEPI8iLyQBKzgdWghgYKrQXpqakhw1gd4MH87VrykXARKvZNIHlpbo2BTczhNLZ0pOYI5BLXWl97QQNYCdux9zHHOuLXHtHCsjDyu69hhSuFWkex1A5IeHtSun7w65cHDu0uzG7tXXPHbiA96iti8KKjL22aQZ_iXpEK2o0nnzxY30-RChY7HGPXZ71rv5RnkomJ9ScDUXk5gEySTk23WxD5GQQLpKPRKgCmlLBsW9WxsUiwt4bopJQp4Vlv5TYxolY9AxePb3BDELI_hQoxbikuUMs8g6Ug1nlSPElacnUcoWESkLsw=="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://www.rockawayx.com/insight-categories/news'\np=subprocess.run(['curl','-LsS','--max-time','30',u],capture_output=True,text=True)\nfor href in re.findall('href=\"([^\"]+)\"',p.stdout):\n if 'relayer' in href.lower(): print(href)\nPY","max_output_tokens":1500}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"29de93\",\"wall_time_seconds\":0.141063292,\"exit_code\":0,\"original_token_count\":29,\"output\":\"/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund'\np=subprocess.run(['curl','-LsS','--max-time','30',u],capture_output=True,text=True)\nraw=p.stdout\nfor m in re.finditer('2026|September|August',raw):\n if m.start()<50000: print(raw[max(0,m.start()-80):m.end()+120])\nraw=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>',' ',raw,flags=re.S|re.I)\ntxt=html.unescape(re.sub('<[^>]+>','\\n',raw))\nprint('\\n'.join(x.strip() for x in txt.splitlines() if x.strip())[:18000])\nPY","max_output_tokens":6000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"238772\",\"wall_time_seconds\":0.000003708,\"exit_code\":0,\"original_token_count\":2746,\"output\":\"<!DOCTYPE html><!-- Last Published: Tue Sep 29 2026 16:17:23 GMT+0000 (Coordinated Universal Time) --><html data-wf-domain=\\\"www.rockawayx.com\\\" data-wf-page=\\\"67f7a7ea3c0d75\\n.prod.website-files.com/67ee62af81b95bef343e8255/6a8dcf90ba619368d2f485c0_photo_2026-08-24_10-11-47.jpg\\\" property=\\\"og:image\\\"/><meta content=\\\"RockawayX acquires crypto-focused hedge fund firm, Relayer Capi\\n.prod.website-files.com/67ee62af81b95bef343e8255/6a8dcf90ba619368d2f485c0_photo_2026-08-24_10-11-47.jpg\\\" name=\\\"twitter:image\\\"/><meta property=\\\"og:type\\\" content=\\\"website\\\"/><meta content=\\\"summary_large_imag\\n.prod.website-files.com/67ee62af81b95bef343e8255/6a8dcf90ba619368d2f485c0_photo_2026-08-24_10-11-47.jpg\\\" loading=\\\"lazy\\\"/></div></figure><p>RockawayX, a global digital asset investment platform with approx\\nrong></h2><p>Relayer&#x27;s liquid strategy has delivered strong performance in 2026, delivering an estimated net return of approximately 70% year to date, outperforming an equal-weighted basket of Bitcoi\\n an equal-weighted basket of Bitcoin, Ethereum and Solana by 86% (as of Aug 21, 2026). Performance has been driven by early, high-conviction investments across two of the market’s major themes: AI and the\\n
… [10119 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"GAIN Ventures" Carebot Czech investment 2026'},{q:'"GAIN Ventures" Czech Praha investor'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "Carebot Closes the Largest Investment Round in Its History - Carebot (https://www.carebot.com/news/carebot-closes-the-largest-investment-round-in-its-history)\nciteturn59search0 [wordlim: 200] Published: 2 months ago; Crawled: last month; Aug 3, 2026 ... Carebot has secured an investment of more than €1.5 million, the largest in the company’s history.The round was led by Garage Angels and Electron Capital Partners, with JIC Ventures joining the company alongside existing investors Gain Ventures and Eva Janečková. ... “Carebot has demonstrated that it can successfully implement AI in everyday clinical practice, giving the company a strong opportunity to succeed on a global scale,” says David Zabadal, Investments & Operations at Garage Angels.\n\nCarebot Closes the Largest Investment Round in Its History\n\nAug 3, 2026\n\n### Carebot Closes the Largest Investment Round in Its History\n\nNews\n\nCarebot Closes the Largest Investment Round in Its History\n\nAug 3, 2026\n\n### Carebot Closes the Largest Investment Round in Its History\n\nNews\n\nCarebot Closes the Largest Investment Round in Its History\n\nAug 3, 2026\n\n### Carebot Closes the Largest Investment Round in Its History\n\nImage\n\nCarebot has secured an investment of more than €1.5 million, the largest in the company’s history. The round was led by Garage Angels and Electron Capital Partners, with
… [23242 more characters]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw2MYOGYxy0M9qhWocqChLI3Mblj8bfLsxmIwnwP2c37425zwyIzokLSmqm5o17pxfQX8hE_-opRupjheCB0DR4UZvF74RX2Io9N059BWylRW4Jehtz_fdImMEOL9G4DgLmf2mgKLNbOMXFdTVRW7uL_GhSIx3mj5_SmKh53XnFmxtGKrI_TDlm2Hjw9tbDUZUBLkJJJ51E7szcAYPvrh9ZcOu9dKIEQkiWXfgYWk_fXVSDSb-iJpciQ6vOkdPZvR9RsxsHjZylVC9oJxQU69W8XrMwJFLL0qXnWhWZW1MBqDQ5P7OcdK5DsUlPTKWash7-TS3AkRuKZiS1q4fYkjAhWwxRNtXr1XBeMrC8l1UZzZx8K3l-L2rVKzHFXfV-H9M19kb-5Rqil1YnHc1onFhdXEFkOfnxLzRMDwAIcXdyr9l3tYqlNgJe4xgSX3dT_5QBWHZyBZcMxmFoUfhMEQcHh3Df0E7PvGOS0MR2F777a7Lkrp_y9d4tDJ_HRBK_BYDZkIpKLkIprVmF9ssJOH0lpH_wJ5pkV5SVurw-t_RFiCdOmuYJIG4XFoPUdL0GwmDu6EXYlPlJFmIOEGH0WXJAzk_gVBdG5zqDGoPADfOKYx4PulCaPRR3VNmu_sDiXdZ108XIpZIoBU3uS5DFigzysH4phtB_tDAVKpj4klaXVOLjfvHjoiAD6Na1U_ASXtN-a0aXUcITom4i-w8AMGsc7Do5jy7JCeMaKE6ZuNVzSDsBkXQI9mgtuBSf2UwoynFj-"}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Airline Pilot Club" "StartGuide" investment'},{q:'"CloseRocket" "StartGuide" investment 2024 2025 2026'},{q:'"Nutritionpro" "UP21" 2023 investment'},{q:'"BotBot" "Zero One Hundred" investment 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "StartGuide Portfolio Investments, StartGuide Funds, StartGuide Exits (https://www.cbinsights.com/investor/startguide)\nciteturn63search0 [wordlim: 200] Crawled: 4 weeks ago; ## StartGuide Investments ... Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024.\n\n# StartGuide\n\nstartguide.cz\n\n## Are you an investor?\n\nSubmit your portfolio details now to be considered in our investor rankings.\n\nSubmit portfolio details\n\n## Investments\n\n16\n\n## Portfolio Exits\n\n1\n\n## About StartGuide\n\nStartGuide is a Czech incubator. It was founded in 2021 and is based in Praha, Czech Republic.\n\n## Headquarters Location\n\nKarla Engliše 3201/6 Smíchov\n\nPraha, 150 00,\n\nCzech Republic\n\n\n## StartGuide Investments\n\n16 Investments\n\nStartGuide has made 16 investments. Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024.\n\nImage: CBI Logo\n\n### StartGuide Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n11/30/2024  | Pre-Seed  | Airline Pilot Club  | $0.7M  | Yes  |  | \n11/20/2024  | Pre-Seed  | CloseRocket  | $1M  | Yes  |  | \n8/13/2024  | Seed  | ArtMaster  | $1M  | Yes  |  | 1\n8/1/2024  | Pre-Seed  | Subscribe 
… [27663 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"ArtMaster" "StartGuide" investment 2024'},{q:'"Airline Pilot Club" funding November 2024 Startguide'},{q:'"BotBot" "0100" investment'},{q:'"Nutritionpro" investice "2023" "UP21" -site:cbinsights.com'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "StartGuide Portfolio Investments, StartGuide Funds, StartGuide Exits (https://www.cbinsights.com/investor/startguide)\nciteturn64search0 [wordlim: 200] Crawled: 4 weeks ago; Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024. ... 8/13/2024  | Seed  | ArtMaster  | $1M  | Yes  |  | 1 ... # StartGuide Portfolio Exits\n\n# StartGuide\n\nstartguide.cz\n\n## Are you an investor?\n\nSubmit your portfolio details now to be considered in our investor rankings.\n\nSubmit portfolio details\n\n## Investments\n\n16\n\n## Portfolio Exits\n\n1\n\n## About StartGuide\n\nStartGuide is a Czech incubator. It was founded in 2021 and is based in Praha, Czech Republic.\n\n## Headquarters Location\n\nKarla Engliše 3201/6 Smíchov\n\nPraha, 150 00,\n\nCzech Republic\n\n\n## StartGuide Investments\n\n16 Investments\n\nStartGuide has made 16 investments. Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024.\n\nImage: CBI Logo\n\n### StartGuide Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n11/30/2024  | Pre-Seed  | Airline Pilot Club  | $0.7M  | Yes  |  | \n11/20/2024  | Pre-Seed  | CloseRocket  | $1M  | Yes  |  | \n8/13/2024  | Seed  | ArtMast
… [26442 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'ArtMaster StartGuide investice srpen 2024'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Českou hudebněvýukovou aplikaci podpořili investoři - CzechCrunch (https://cc.cz/pomaha-s-ucenim-na-klavir-ci-kytaru-a-vyuzivaji-ji-v-70-zemich-ceskou-aplikaci-podporili-investori/)\nciteturn65search0 [wordlim: 200] Published: 2.8 years ago; Crawled: 2 months ago; 1. 2024 – 1 min čtení ... Detaily investice shrnujeme níže. ... Jaká je jeho historie: ArtMaster vznikl jako fyzická škola v roce 2018, v roce 2020 se přesunul do onlinu.\n\nStartupy – 02. 1. 2024 – 1 min čtení\n\n# Pomáhá s učením na klavír či kytaru a využívají ji v 70 zemích. Českou aplikaci podpořili investoři\n\nDo ArtMasteru vložila přes jedenáct milionů korun skupina investorů včetně nejvýše postaveného Čecha světového showbyznysu či zakladatele Beat Saberu.\n\nPeter Brejčák\n\nFoto: ArtMaster\n\nZakladatelé ArtMasteru Michal Novák a Radim Vysoký\n\nUložit 0 0Zobrazit komentáře\n\nBudějovický startup ArtMaster staví výukovou platformu, která funguje jako online tržiště, kde i známé osobnosti pomáhají uživatelům naučit se hrát na klavír či akustickou, elektrickou i basovou kytaru. Nějaký z kurzů si pořídilo už přes čtrnáct tisíc zájemců ze sedmdesáti zemí světa. A v oslovování dalších mladé firmě pomohou i noví investoři, kteří do ní vložili přes deset milionů korun. Detaily investice shrnujeme níže.\n\nZainvestovaný startup: ArtMaster\n\nKdo investuje: Český fond N1, německý EQT, BPD Partn
… [24279 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re\nu='https://startguide.cz/en/'\np=subprocess.run(['curl','-LsS','--max-time','30',u],capture_output=True,text=True)\nprint('\\n'.join(sorted(set(re.findall('href=[\"\\x27]([^\"\\x27]+)',p.stdout)))))\nPY","max_output_tokens":1500}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"495b14\",\"wall_time_seconds\":0.016516541,\"exit_code\":0,\"original_token_count\":110,\"output\":\"#\\n#about\\n#contact\\n/\\n/_nuxt/BDw61n7h.js\\n/_nuxt/BcMqlqRe.js\\n/_nuxt/BiNNMZ9q.js\\n/_nuxt/C19QRmIg.js\\n/_nuxt/Footer.DiWGtssM.css\\n/_nuxt/d0TfLoZs.js\\n/_nuxt/jdRToexg.js\\n/_nuxt/v3LzWKjp.js\\n/en/\\n/en/#about\\n/en/#contact\\n/en/#investment\\n/en/_payload.json?_b=84c36fa3-dc9e-4fa0-9c1d-3d0f4176685c\\n/en/sgone/\\n/en/sgone/#references\\n/en/sgtwo/\\n/en/sgtwo/#team\\n/images/favicon.png\\nhttps://www.linkedin.com/company/startguide-cz/\\nmailto:contact@startguide.vc\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"CloseRocket" "Startguide" million'},{q:'"BotBot" funding 2026 seed Zero One Hundred'}],response_length:"long"}));
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://startguide.cz/en/sgone/'\np=subprocess.run(['curl','-LsS','--max-time','30',u],capture_output=True,text=True)\nraw=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>',' ',p.stdout,flags=re.S|re.I)\ntxt=html.unescape(re.sub('<[^>]+>','\\n',raw))\nprint('\\n'.join(x.strip() for x in txt.splitlines() if x.strip())[:18000])\nPY","max_output_tokens":5000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "Zero One Hundred Portfolio Investments, Zero One Hundred Funds, Zero One Hundred Exits (https://www.cbinsights.com/investor/zero-one-hundred)\nciteturn68search0 [wordlim: 200] Crawled: today; Their latest investment was in BotBot as part of their Seed VC on January 01, 2026. ... Zero One Hundred has 2 funds, including Zero One Hundred Fund I.\n\nImage: Zero One Hundred company logo\n\nVenture Capital\n\n# Zero One Hundred\n\n0100.vc\n\n## Investments\n\n41\n\n## Portfolio Exits\n\n1\n\n## Funds\n\n2\n\n## About Zero One Hundred\n\nZero One Hundred is a venture capital firm that focuses on Czech and Slovakian startup investments. It generally invests in early-stage rounds at seed and series A rounds. The company is based in Bratislava, Czech Republic.\n\n## Headquarters Location\n\nCzech Republic\n\n## Latest Zero One Hundred News\n\nPracovat víc za víc peněz? Je jedno, jestli je to podle vás blbost. Český startup chytře oslovil talenty\n\nOct 1, 2025\n\nPracovní hardcore mode Minulý týden tak trochu vybouchl český a slovenský LinkedIn. Nejdřív na něm Juraj Masár ze startupu Better Stack představil pracovní „hardcore mode“ – zaměstnanec se ke konci každého měsíce může dobrovolně přihlásit, že odpracuje 1,5násobek hodin a odměnou za to získá dvojnásobnou kompenzaci. Kdykoliv se pak může z tohoto režimu i odhlásit. ## Zero One Hundred Investments\n\n41 Invest
… [34990 more characters]
```
</details>

→ `send_message`
```
{"target":"check_last","message":"gAAAAABqyw2yGPNjtj_UN5FOsLTyHtLliHz8GJdU8nGDpSkFLBrhdFAwZPSkUJyjkXDNIHBVlGGUH2EEm1yewnD6DYE9uJTKHMKU0RuvQIXG4W5Rdx_kRYXm36G2iVZWRCYdNBbNkAbxphMxiRJ3TVBakOJpX8C-OjQPgWdT3HMlhfwbQjGl4uss0Vj98fQPQfgX8VOkR9QSXmwaEMvT-hrapeYN9rfrpWjMQEsNgOU1YfNKuuEJTwkGSr9oHycUMmIABE3pP7RQJEVfVfJtZU04b4jTf2F-PTbWETiUtXYpqiqvbSYKDTYlcBc940lymEN_eYew2M-nrXcH3IK8hISjxX7rrXQp56w4Qq6Vz9axQyqKa21gWsIzalFcJiJyuNPjh_oXPjAzvkO5NZcsTTbJMCgrg1uqcKpzy8E6P2FxoWtidbxhLVoFydvc8H8HIbZ0--H-KyN8HckxNh196u8P9XdbcuzOekb7ndf268mTpauhTbzjGOsieLTUxDlLI-Kk9hCoG56T-PBVG8Se1JzwQfeMPFV1WYSkG_pWW5f11zbzE6qm2zoSS7U2WW22O1vNhwjffj6q7JmSNTqRQAdql_qInIBE5UHEp86Z1PcxxoJJW9lBZNEXriAniL_vtVl859fYDNkcXUxvYn0OBniSfkb5-y6kvu4zn-8sGjwG5gGtqFOYjMceUABK-cKpiilBN_KDR9B_qS8mmQo7A2dEhZ4ktt-cgZy6B2_bVt9dlJV05uIdvQcdF4KZMqPf9nLj1S2ivZiW68ZiKWpDm2i5TTRBR_WIdpOlo-cn1Pc4HBgusLp391cjUH7p8kW3Qs0kkLBZJttJGL-UA5r38r4GgrxRDe0I_Q6Qizr25Qw2VV8JqUuNaLltFD5LotHwl9_MtKLtd8WLI2sAfOlnNPgCgye8DPj4yEOMiQNETUIJvoRrHLWaEC5E7PQKulFOpQHd6xfAxI0Sz5DSCEluZXn5E81R41a-JJd5hs0EGIp_NDFwM-uGGrpoV8h9r-YM1DqFSzr9mVRtyVjSgmR5T6IhCKKtsSV9SA=="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"CloseRocket" "StartGuide" funding -site:cbinsights.com -site:crunchbase.com -site:teeming.ai -site:failory.com -site:teaserclub.com'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Europe’s leading community of female angel investors LUMUS Investment Collective supported CloseRocket of Katarina Šimková | Startup Kitchen (https://www.linkedin.com/posts/startupkitchenn_europes-leading-community-of-female-angel-activity-7355959140336164865-xUau)\nciteturn72search0 [wordlim: 200] Crawled: 5 months ago; LUMUS joins a distinguished group of supporters, including Peter Komornik, Lucia Pašková, Andrej Kiska, as well as VC funds such as Vision Ventures (VV), Jinej fond, STARTGUIDE VC, and ZAKA VC, who have previously supported CloseRocket.\n\n# Startup Kitchen’s Post\n\nStartup Kitchen\n\n7,575 followers\n\n9mo\n\n⚡ Investment Announcement ⚡ Slovak CloseRocket, founded in 2023 by Kate Simkova, combines an AI-powered sales assistant with a marketplace connecting companies to verified B2B marketers, just raised an investment from LUMUS Investment Collective , one of Europe’s largest female-led angel communities, co-founded by Lucia Cerchlan, Vladimira Cincurova, Terezia Jacovaá and Zuzana Zamborska. LUMUS joins a distinguished group of supporters, including Peter Komornik, Lucia Pašková, Andrej Kiska, as well as VC funds such as Vision Ventures (VV), Jinej fond, STARTGUIDE VC, and ZAKA VC, who have previously supported CloseRocket. More here 👉 https://lnkd.in/ercNnZTh  Matěj Turek, CFA Klaudia Martikánová Martin Búza Marek Tvrz Jozef Tvaroška R
… [29000 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"StartGuide" "Carebot" "2024" investice'},{q:'"StartGuide" "CloseRocket" "2024" investice -site:cbinsights.com -site:crunchbase.com -site:teeming.ai'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Eva Janeckova Portfolio Investments, Eva Janeckova Funds, Eva Janeckova Exits (https://www.cbinsights.com/investor/eva-janeckova)\nciteturn74search0 [wordlim: 200] Crawled: 5 months ago; 3/22/2024  | Seed VC  | Carebot  | $1.3M  | Yes  | BHM Group, Gain Ventures, Karel Bastl, Lukas Kopcaj, Pilulka Lab, Roman Trachta, and StartGuide  | 2\n\n# Eva Janeckova\n\nlinkedin.com/in/eva-janečková-444cz444\n\n## Investments\n\n1\n\n## About Eva Janeckova\n\nEva Janeckova is an angel investor and is based in Alhambra, California.\n\n## Headquarters Location\n\nAlhambra, California,\n\nUnited States\n\n## Eva Janeckova Investments\n\n1 Investments\n\nEva Janeckova has made 1 investments. Their latest investment was in Carebot as part of their Seed VC on March 22, 2024.\n\nImage: CBI Logo\n\n### Eva Janeckova Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n3/22/2024  | Seed VC  | Carebot  | $1.3M  | Yes  | BHM Group, Gain Ventures, Karel Bastl, Lukas Kopcaj, Pilulka Lab, Roman Trachta, and StartGuide  | 2\n\nDate  | 3/22/2024\nRound  | Seed VC\nCompany  | Carebot\nAmount  | $1.3M\nNew?  | Yes\nCo-Investors  | BHM Group, Gain Ventures, Karel Bastl, Lukas Kopcaj, Pilulka Lab, Roman Trachta, and StartGuide\nSources  | 2---
… [24883 more characters]
```
</details>

→ `send_message`
```
{"target":"check_last","message":"gAAAAABqyw3HpjrTImDviglGd1EfLzmwLy18cvztRWswT8LcBlaRj4_lt2rj7B1seA8qNHX4U5Ld1eeUU9NMNhMES-C-O1-tomwLOqcGXM-7ba0l1rLWHFn-0LpAi_YlzOafhoV129jzSjykcQFzmhq8d1LNt_9K2OsHnL2U-JlHk71VrPYL_XvSYigtG_RD4V4mNdOkKb3KQZp2TVz8BGkHrrNgTwOYwpHwYMZCtMXcO9uVTwe3jmZ2XVA9DF3y9JElKYxXh1zo8hyI-wvUvBkEcPSmt5PiahuRVqMK_XB6MLAnKMc9-zts0VwEcpn9t8oBjo80q6LbJVf7458yN1qtQfn_mTVtg5u7pOio-rlN2MoweGepuFG9VNoOl7yZFmkV-QW5tnQ91mZ0xL9LCKAzNXC5VvlWZEz2_X0VyPAHWFJBt9HLDDFr5SncnmVVCYjHL8jpkhJKV5R1fZXKtPDdjCEVS-H3zamJmUApmhIiaidiGKIDQSawnKI7MSEqn5b4JfLguqmYUHUWqP2ZhKV9Td3SYPOwyFv5JYySeAJPeMviBc3bpI__IWFAbYKRUg_F4CpxmVRwoPbXaFV1uZx8VWxXx0h52pyNUi4OIxgfmeLLPJpAPkhfmOOmLIfXnj8FLqXonVYBjNK36imncuJ41Xnq-BJ6IxTuXWmkocSr_VwHxtZ2C72p_fYB33Tl_GADAm_NUB5GlAUbW0XZczimlcXALbdcpyo8nMMEQBazS_BMXq63Q3NwIDKjPt6TtgZxLvLQGlbz2HKnTgTYjq9seiYRE4KlkFAuhbFRa7jrJaP2yVAbmGM4NYdpfChbFKIk4omD-R8ZC12fj7PLQDnpl1eyXHbHoAQJWbXG3mTGen9A9DxctPKePG5QygYaT2MUNYwZMjJIZTtD4ZI2zy7GJaCwuZGZcmRmeT_6RWHx61Zb1TnMDR8="}
```

<details><summary>result</summary>

```

```
</details>

**Codex:**

[redacted: name]
Основные статусы уже определены. Сейчас сверяю цитаты с текстом страниц и проверяю самые свежие сделки; где точный день не указан, отмечу точность до месяца или года.


→ `list_agents`
```
{}
```

<details><summary>result</summary>

```
{"agents":[{"agent_name":"/root","agent_status":"running"},{"agent_name":"/root/check_first","agent_status":"running"},{"agent_name":"/root/check_last","agent_status":"running"},{"agent_name":"/root/check_middle","agent_status":"running"}]}
```
</details>

→ `wait_agent`
```
{"timeout_ms":45000}
```

<details><summary>result</summary>

```
{"message":"Wait completed.","timed_out":false}
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Minerva" "Credo" "October 6" "2026"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "Minerva Humanoids raises $10M for robots that do bomb disposal and rig work (https://thenextweb.com/news/minerva-humanoids-10m-pre-seed-general-catalyst)\nciteturn75search0 [wordlim: 200] Published: 5 days ago; Crawled: today; # Minerva Humanoids raises $10M for robots that do bomb disposal and rig work ... October 6, 2026 - 2:05 pm ... General Catalyst led the round, with Long Journey Ventures and Credo Ventures as co-leads, the company said on Tuesday.\n\n  * Investors and funding\n\n# Minerva Humanoids raises $10M for robots that do bomb disposal and rig work\n\nRoger, a humanoid steered through a VR headset, is built to take on bomb disposal and offshore rig work. Minerva Humanoids starts its first paid pilots this autumn.\n\nOctober 6, 2026 - 2:05 pm\n\nImage: Minerva Humanoids’ Roger robot walking\n\nRoger, the semi-autonomous humanoid robot built by Minerva Humanoids\n\nImage: Image Credits Credit: Minerva Humanoids\n\nMinerva Humanoids has raised about $10M in pre-seed funding to build humanoid robots for dangerous jobs. The San Francisco startup works on oil and gas and public safety. General Catalyst led the round, with Long Journey Ventures and Credo Ventures as co-leads, the company said on Tuesday. Hugging Face, Codecademy, RunwayVC and Compound are among the other backers.\n\nThe money brings Minerva out of stealth. It will start its first pa
… [33854 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://finance.yahoo.com/technology/ai/articles/minerva-humanoids-emerges-stealth-10m-101000013.html','https://lasvegas.newsnetmedia.com/story/484299/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-worlds-most-dangerous-jobs/','https://thenextweb.com/news/minerva-humanoids-10m-pre-seed-general-catalyst']\nfor u in urls:\n p=subprocess.run(['curl','-LsS','--max-time','25',u],capture_output=True,text=True)\n raw=p.stdout\n print(u,'EXIT',p.returncode,'LEN',len(raw))\n for q in ['with Long Journey Ventures and Credo Ventures as co-leads','participation from MVP Ventures, Kaya','General Catalyst led the round']:\n  r=subprocess.run(['grep','-oF',q],input=html.unescape(raw),capture_output=True,text=True)\n  if r.returncode==0: print('GREP OK',r.stdout.strip())\nPY","max_output_tokens":1700}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"a76979\",\"wall_time_seconds\":1.389127708,\"exit_code\":0,\"original_token_count\":182,\"output\":\"https://finance.yahoo.com/technology/ai/articles/minerva-humanoids-emerges-stealth-10m-101000013.html EXIT 0 LEN 23\\nhttps://lasvegas.newsnetmedia.com/story/484299/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-worlds-most-dangerous-jobs/ EXIT 0 LEN 93995\\nGREP OK with Long Journey Ventures and Credo Ventures as co-leads\\nGREP OK participation from MVP Ventures, Kaya\\nhttps://thenextweb.com/news/minerva-humanoids-10m-pre-seed-general-catalyst EXIT 0 LEN 209016\\nGREP OK with Long Journey Ventures and Credo Ventures as co-leads\\nwith Long Journey Ventures and Credo Ventures as co-leads\\nGREP OK General Catalyst led the round\\nGeneral Catalyst led the round\\n\"}"}]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw3fBhIwtQmJH18QtHZBTzcsLLOLEcS8OJwCMB5kOlXKcaVtiEtcMzFUFBtwMPswHN1BULqiy064F22KZFmi-5RbH2DreVCbm7b-njeHzMJlUncgWPHPfsMb8cjMAq-lLSii-iadX3EcMMtyG_Pqy-nMF7XA3Hx_mWLd7OVJl_6f5AUObYA9Qp3readzqJNhR2PWWaC8P-W3af4eqzpW130iM14b4aHRpaH6WjwQxIIxDOQ87_5OwU45lweuKMWgN-JVd9mzmawj-pbZGK-Aim3BQrvgxfxDt4MqyDnD4fZE47rbsGSTukAh153Z1sIrhDltJ42wWBAjRCgL73E-8muuICwSOvL5TWxrbPxZqFyiR0Dx5kTmYLkGrI0vaoX5Tkx1JfQOIk8ghNU44TSQ47xJvz9r09SQkpFx-n04mrTxEkKHGPbVP3sAYn_pxrLDFjMNthystqlloCR8DYAcHZ28Y5uuItc3ciSqncR8mi4nrChQINRK1qBoNLsJ46bPid7xz1-5V65lF7qzOsKN-O6W1zG7KfDZhY5EvXgyB4ZwpDFsMwvEss0-7dGILo5ajjeiw-1kdYNZYs8Vr6-oI9nfh3juja0jsY-82MPlwlyiua-DlO7xgS7HI7lNRQXljf1r2LptKzuoy7vxUr9elX6AmW_lZSkNFl0awHJ8WQU8ee0IylR3-Gpgm2Pkv2eYPoM8"}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_middle","message":"gAAAAABqyw3kQxQ0WCFpW5T2XtWKgk5WYtuzSKTP21zViN_G-kZNZg02LH8jjGYjjb6STZQSPIFeMA-ZaHW-lY400GSOHapqimDRazvecYpQp02GaTGdqW3DyUcUnJRfeu3Othhbq32xTS8OZCiELryquWAMab5vZnbCYVOdKuQPw8-MLALfH_nquhpKx32enYDn6EP1Gdh_cvhgBlBTZdwIV5GnHYM2YMf-Y00OI3QunuNshX_i5-S8cuIxmZ22UeX8IzA8baS90ZTMH9Mgb8LuVxKGveaDtzqjE6EJbU1M75QpU4xKn08V3oZRFq6Vds8wnyAGnwO8BkAhnmzIZ29GDwfduCAN6nfN3fYXmHPYKNuN36bOwCe2THNQvh5tmXgk-P9GqbjRjVOZqz0RqHUX9hCIb3kHoBhg43IWALH2MyfBVhAoCXusDm4pIod4uoQNGQGIj-UE8FuctXONBHrBtAbq9WBra0GHGqUHbb9BxoqAIo55qzcdkInfEnsosoV5z4aNE3WqzDXeueX1MJydVmifEk_yrb9D6qO57IDJ_YtMTpKmnhkiuB8yxtVuyGVbLtPBSCmdUbNwu9PD2sSMjVaEHTFyQ_hrEGkofIIOTHkRVg5qzVHXJ7c-l9XEX5lfAUqyYHQ6pmXOR_aHNpU_FtBeC7uKpGSlF8VIRywfmsKep7MzYIc="}
```

<details><summary>result</summary>

```

```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw3raEBXm2iWxKN4Xbx1oW2SSk13ifQmEyzVnp7-PAtQ0zImG06_f_PEIuSxyqgYLfktquXggeTFSPIPQ-h-JiYAY-Xq5oiwWjFX7SFMJ61uDcdRrE2swB9Bc3jZN6s3JusccbeVbnpR9EJtJ-UKYUSb_hSqUedHxjA50VoRIKC3F26GyAZNXWwInOFLn5h3EuMlvqIgOdpJTk5pqBWualX-WblWyHOZpqMZaK7hBbuo8AtxhkWyI-unwVFWCOlJRPr3u1Max2Zzrx0F8gqlL7wZ459ndHDBA84rMiwKxW-5XYnJWlZkneyasgF7ZaTasectxiUeWE-DJ5U9kou-zgtHdKB7HBwEPKSex2ndwZEdDgnYCONq7ju2dz2tQhV_gN9mHLEKhC6B5jk69OCs-rIbcdkAN6GPAzfuo-EWih8JaC2lRSCQleJXdLw1b3-3HVVQFxs9Tjta1QafKwjSVkNVTLCGG3FkdEh0Ki2L1LiDl-BoGoJhE7_1VqaJ0gWoQnvDILZ2knqrf6bb0f3ZbYuRZbuXQLNQtigOg0whkcvPSJs="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Fond inovácií a technológií" investícia 2020 2021 2022'},{q:'"fondfit" investícia spoločnosti 2022 2023'},{q:'"Fond inovácií a technológií" investícia 2019 2018'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Správa o stave malého a stredného podnikania (https://new.sbagency.sk/wp-content/uploads/2026/02/sprava_o_stave_msp_v_sr_v_roku_2022_print.pdf)\nciteturn77search12 [wordlim: 200] Published: 6 months ago; bolo v kumulatívnom období (od marca 2018 do decembra 2022) podporených 9 MSP.152 ... nasledovné fondy: Fond inovácií a technológií, a. s., Slovenský Rozvojový Fond, a. s., Eterus ... V porovnaní s rokom 2021 bol objem schválených investícií v roku 2022 vyšší o 3 800 000\nspoločností) prostredníctvom špecializovanej dcérskej spoločnosti Národný holdingový fond, \ns. r. o. (do 20. 03. 2014 pod obchodným názvom Fond fondov, s. r. o.). Dlhodobým poslaním \nspoločnosti je usmerňovanie činnosti jednotlivých fondov tak, aby sa stimuloval rozvoj \nsektora MSP na celom území SR, zhodnocoval sa objem finančných prostriedkov \njednotlivých fondov a dosiahnuté zisky sa používali na realizáciu dlhodobého cieľa podpory \nMSP.  \nV roku 2022 boli prostredníctvom spoločnosti Národný holdingový spravované \nnasledovné fondy: Fond inovácií a technológií, a. s., Slovenský Rozvojový Fond, a. s., Eterus \nCapital, a. s..154 \nV sledovanom roku 2022 bola prostredníctvom vyššie uvedených spravovaných fondov \nschválená celková výška investícií v objeme 6 500 000 Eur155 (z Eterus Capital, a. s.). \nV porovnaní s rokom 2021 bol objem schválených investícií v roku 2022 vyšší o 3 8
… [21899 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"G-Force" "Raya" investment 2026'},{q:'"G-Force" "Raya" funding'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "G-Force investor profile | Platvix (https://platvix.com/investors/firm/g-force)\nciteturn78search0 [wordlim: 200] Crawled: 2 weeks ago; G-Force is a pre/seed fund and investment program for mission-driven climate tech startups. ... 2026-09-02 usegforce.com Raya Power Modular, plug-and-play solar and battery pod that delivers backup power and bill…\n\n# G-Force\n\n2026-09-02usegforce.com\n\nPre-seed investorsClimate investors\n\nOverview\n\nWhat they do\n\nG-Force is a pre/seed fund and investment program for mission-driven climate tech startups. The G-Force Sustainability Seed Program is a collaboration between Founders Factory (Henry Lane Fox, Brent Hoberman CBE) and tech leaders: Boris Zeleny (AVG, later sold to AVAST for $1.4bn), Marian Gazdik (Startup Grind), and serial early-stage investors Peter Kulloi & Miklos Kobor.\n\nusegforce.com\n\nWhat they look for\n\nBacking early-stage startups contributing to energy, mobility, and industry transition with the potential for global scale.\n\nusegforce.com\n\nStage\n\nPre-seed, Seed\n\nusegforce.com\n\nSectors\n\nClimate, Deeptech, Food and agriculture, Mobility and logistics\n\nusegforce.com\n\nBased\n\nBratislava, SK\n\nusegforce.com\n\nSources\n\n2026-09-02usegforce.comWe're a pre-seed VC fund focused on Climate/Deep Tech startups.\n\n2026-09-02usegforce.comReach out to us-we'd love to hear from you!\n\n20
… [28828 more characters]
```
</details>

→ `send_message`
```
{"target":"check_first","message":"gAAAAABqyw4D1groYmUQqXj6k_eL97M-VMQWHmRzW78iq3SgbpcksMzf2Qpb1KsIESRiv_mkWnsBtIbeT7nFfD8vSATFA2YV1OubpbuWULJ1ZF28bdKS84YiYEDDpo0SKtBWWB5ShVwURAeyvklVzdM_o_ZJ4L0FJeIXuatUETAhFTI0F4MnQQF8Lp600bIlJCGA-etBTohz-wjELJf-rRXc2VJvhIXjtWsqeSyfyGWLqArJ05m0FaUxIZeOD2gcZPa9aa5UP5P0fIjLAHMWFrpr0yomImdkCuAlhUADzaKcruWbh0kyWQ_NuO8i9m5_3Wbt2ejLgS0PSvQ7UEmukrBZxDRCuw8_sZWjszadExGZpJOP0R8qWHz5X2nBOQdayiqjwoS_A7Ar5K1ESKj5YMD3LvvLZKwlyyd98dPLJURdpxcrvkSHe6Ea6BFFKazUFmEnuMP8AAENncSz_tpfRuWaKWMC6bt2pXGP6dgKvMH-ZO0loWtiSAx6_utnq-3q_QTD8uV4g4srbwCN973OL8Kn6VDkiavziF-2k72ltx6OgF5sq-G-dHRmy0NN3zAcuE9exe9q37HjIMqJCHQ1HOAQS3JGPyRW9xw261gPJDG_lxMQRukf-vJryWCoRLSHhVKgsNtXuDR34lVT837RWVoji5iTR0CqUA=="}
```

<details><summary>result</summary>

```

```
</details>

→ `wait_agent`
```
{"timeout_ms":45000}
```

<details><summary>result</summary>

```
{"message":"Wait completed.","timed_out":false}
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site:startupyard.com "Carebot" investment 2021'},{q:'site:startupyard.com "invested" "2025"'},{q:'site:startupyard.com "investment" "2024" startup'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "The Next Wave Begins: StartupYard Announces Batch 15 - StartupYard (https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/)\nciteturn79search0 [wordlim: 200] Published: 1.1 years ago; Crawled: last month; Since 2011, StartupYard has been the launchpad for some of Central Europe’s most ambitious startups, from Rossum to Gjirafa, Carebot, SwapIn and FeedYou, to name a few. ... For the first time, founders can access an optional €25,000 cash investment alongside the hands-on acceleration StartupYard is known for. ... Whether you’re building applied AI for healthcare, finance, manufacturing, cybersecurity, or something no one has imagined yet, StartupYard is where those bold ideas get traction. ...   * Investor Introductions: StartupYard’s extensive network includes connections to some of the top investors in Europe, offering potential funding opportunities to scale your operations.  * Individual Workshops and Training: Regular workshops focusing on various aspects of business development, including pitch training, financial modeling, and marketing strategies amongst others.\n\n# The Next Wave Begins: StartupYard Announces Batch 15\n\nWhere first-time founders from CEE earn legitimacy and launch bold ideas.\n\nSince 2011, StartupYard has been the launchpad for some of Central Europe’s most ambitious startups, from Rossum to Gjirafa, Careb
… [33156 more characters]
```
</details>

→ `exec`
```
store("last",[
{"id":"rockaway-ventures","is_investor":"yes","type":"vc","managed_from":"CZ","latest_investment":{"company":"Remix","date":"2025-12-19","date_precision":"day","url":"https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-remix-a-technology-platform-for-circular-fashion","quote":"As part of a Series A investment round, the fund is acquiring a 20% stake in the company."},"active_36m":"yes","confidence":"high","note":"The Prague-based venture fund announced a 20% equity investment in Remix."},
{"id":"rockawayx","is_investor":"yes","type":"vc","managed_from":"CZ","latest_investment":{"company":"Relayer Capital","date":"2026-08-25","date_precision":"day","url":"https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund","quote":"today announced the acquisition of Relayer Capital, a digital asset hedge fund founded by Austin Barack."},"active_36m":"yes","confidence":"medium","note":"The latest confirmed transaction is a private-firm acquisition dated August 25 in its official news index, while investment operations span Prague and other international offices."},
{"id":"seed-star
… [6797 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "15 entries retained in memory."}]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Presto Ventures" "Tech Horizons" 2026'},{q:'"Presto Ventures" investment 2026 latest'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Petition of Northrop Grumman to Reopen and Set Aside Decision and Order (https://www.ftc.gov/system/files/ftc_gov/pdf/petition-of-northrop-grumman-to-reopen-and-set-aside-decision-and-order.pdf)\nciteturn80search12 [wordlim: 200] Published: 6 months ago; FEDERAL TRADE COMMISSION | OFFICE OF THE SECRETARY | FILED 03/26/2026 OSCAR NO. ... <td>Presto Tech Horizons</td> ... <td>Presto Ventures</td>\nFEDERAL TRADE COMMISSION | OFFICE OF THE SECRETARY | FILED 03/26/2026 OSCAR NO. 615113 -PAGE Page 254 of 341 * PUBLIC *  \nPublic Version\n\n<table id=\"e1\">\n<tr>\n<th>Name</th>\n<th>All Deals</th>\n<th>Title</th>\n<th>Representing</th>\n<th>Deals</th>\n<th>Phone</th>\n<th>Email</th>\n</tr>\n<tr>\n<td>Donald Trump</td>\n<td>1</td>\n<td>Angel Investor</td>\n<td>Donald Trump</td>\n<td>#6. Later Stage VC (Series C1): Aug 2025, $60.00M, Completed</td>\n<td></td>\n<td></td>\n</tr>\n<tr>\n<td>Joe Voboril</td>\n<td>2</td>\n<td>Partner &amp; Head of Reserach</td>\n<td>1789 Capital</td>\n<td>#6. Later Stage VC (Series C1): Aug 2025, $60.00M, Completed</td>\n<td>+1 (561) 805-3588</td>\n<td>joe@fvrpartners.com</td>\n</tr>\n<tr>\n<td>Matej Luhovy</td>\n<td>3</td>\n<td>Partner</td>\n<td>Presto Tech Horizons</td>\n<td>#6. Later Stage VC (Series C1): Aug 2025, $60.00M, Completed</td>\n<td></td>\n<td>matej@prestotech.com</td>\n</tr>\n<tr>\n<td>Matej Luhovy</td>\n<td>3</td>\n<td>
… [28621 more characters]
```
</details>

→ `followup_task`
```
{"target":"check_middle","message":"gAAAAABqyw5NeVoMWbxDVXkBGcZ79k3lTJ1ac5wp5BOxgei9V0O9ElfFMtfDYjPED-Giqxz360uRyL2ICuBMkGY9Pctjg0TXuoij2mEh1bl5gBaLYkCu9kZrq22PbZgcKNEuTdfI8i3fqCegPsSibdxtwvr23xD7SGVopQe11X9xDWl-rErTfg_K_Oc4EVNkIK7KGODs3Mefr-7YSUxmFX2avlZqUV2QwizCqm5rE2hNW0Dv8IRBrjXtwlg_guDp4AO041rDryJl3hJFItq-oOg2pkETu8tSLV9jh66J1-7daB8qxEYVIlGPjmq6SjjaJ9S1D6oU3IqiBep__L2A1aFyH5LxKDsu5e4CkBR9-MwPbDqIrO7jSn5aD6j1Cz1cUfJD14XBExrbZyQ5IrwAHuqe85AkUmkhSyRNGumv5QmU0ZXZVcTcorb7Hv95vTWfQ3OPb92grIIcfR6MzKVdMm_fb2VsxMOiKnEL5BaIsYvHl5ip8ai3UvflR7ZEJP45yIrdZltxl0ozT38mZ_AJNLi41_r9ZFOH_RtNNeHUqkgfx71YdPT4Bg1bkEwh8WEf7wFUK5PmaAOcgSAVNml6Mquvib6A8YmsVZOG_uUlYbU29AqYh9xqFFgFRnvKdjB_IpAzSCKm1YI3uvJj-EnOVWqMLaMCchd4R7VECUmXdHI9vrR0SnYq8bkRG1ts-bUQT05LvxipUQrl68BUW8HJOFBCWL1Y-LKBISeElw1yrgDYWQhTfb_HJ6MR5fUe3tqnm1Lq_2IPNT7be7NB6SX-Qn9OsrBpZGZXbwcauRmH9ZWWd2-JOu4Ep4GfJidbAeyLIVQSYUnE3_bLiXFgzJUOyzfUt3NtqVg-Hy4bpoOjzuw6THdvCAAxogo="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
store("first",[
{"id":"365-fintech","is_investor":"yes","type":"cvc","managed_from":"SK","latest_investment":{"company":"Ctrl Alt","date":"2023-10-26","date_precision":"day","url":"https://www.gaebler.com/VC-Funding-6AFD2FC7-C9AF-4DA6-AC47-2B1240324F7C-Ctrl-Alt-10-26-2023","quote":"Forward Partners, MiddleGame Ventures and 365.fintech participated in a $2.6 million capital raise for Ctrl Alt."},"active_36m":"yes","confidence":"high","note":"The Bratislava-based 365.bank investment subsidiary makes seed equity investments, and the latest verified transaction is Ctrl Alt's October 2023 funding announcement."},
{"id":"air-ventures","is_investor":"yes","type":"vc","managed_from":"CZ","latest_investment":{"company":"Cross Network Intelligence","date":"2019-10-24","date_precision":"day","url":"https://feedit.cz/2019/10/24/air-ventures-investuje-do-hitech-startupu-cross-network-intelligence-ktery-pomaha-budovat-efektivni-site-mobilnim-operatorum-ve-svete-i-u-nas/","quote":"Ve startupu se zaměřením na síťovou infrastrukturu získává fond Air Ventures 15% podíl."},"active_36m":"no","confidence":"medium","note":"The official site identifies a Prague-based VC, but recent Jiant funding records 
… [15377 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "30 more entries retained in memory."}]
```
</details>

**Codex:**

[redacted: name]
Сверка выявила ещё одну проблему: сделки отдельного фонда Tech Horizons нельзя автоматически приписывать Presto Ventures. Проверяю эту запись перед сохранением итогового JSON.


→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Choice" "Presto Ventures" "2026" funding March'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Presto Ventures Portfolio Investments, Presto Ventures Funds, Presto Ventures Exits (https://www.cbinsights.com/investor/bohemia-venture-capital)\nciteturn82search0 [wordlim: 200] Crawled: today; Their latest investment was in Choice as part of their Series A on March 16, 2026. ... 2/24/2026  | Pre-Seed  | The New Era of Shopping  | $1.4M  | Yes  | Alliance, Andreessen Horowitz, Cory Levy, Davidovs Venture Collective, Evgeny Yurtaev, Greg Tkachenko, Guillaume Roux-Romestaing, hi5 Ventures, Kacper Kielak, Matthieu Tissot, Nicole Buss, Quinn Campbell, Rokubunnoni, Typhon Ventures, Undisclosed Angel Investors, Urvit Goel, and Zituo Chen  | 1 ... 6/23/2022  | Presto Ventures II  |  |  | $31.57M  | 1\n## Presto Ventures Investments\n\n81 Investments\n\nPresto Ventures has made 81 investments. Their latest investment was in Choice as part of their Series A on March 16, 2026.\n\nImage: CBI Logo\n\n### Presto Ventures Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n3/16/2026  | Series A  | Choice  | $7.1M  | No  | Alea Capital Partners, J&T Ventures, Purple Ventures, Reflex Capital, and Smartlink Partners  | 3\n2/24/2026  | Pre-Seed  | The New Era of Shopping  | $1.4M  | Yes  | Alliance, Andreessen Horowitz, Cory L
… [28423 more characters]
```
</details>

→ `exec`
```
text(load("middle").find(x=>x.id==="presto-ventures")); text(load("last").find(x=>x.id==="soulmates-ventures")); text(ALL_TOOLS.filter(x=>/exec_command|web.*run/.test(x.name)));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"id\":\"presto-ventures\",\"is_investor\":\"yes\",\"type\":\"vc\",\"managed_from\":\"CZ\",\"latest_investment\":null,\"active_36m\":\"unclear\",\"confidence\":\"medium\",\"note\":\"Awaiting standalone transaction evidence.\"}"}, {"type": "input_text", "text": "{\"id\":\"soulmates-ventures\",\"is_investor\":\"yes\",\"type\":\"vc\",\"managed_from\":\"CZ\",\"latest_investment\":{\"company\":\"Antiverse\",\"date\":\"2026-03-09\",\"date_precision\":\"day\",\"url\":\"https://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/\",\"quote\":\"This is why we led the $9.3M Series A\"},\"active_36m\":\"yes\",\"confidence\":\"high\",\"note\":\"The Czech venture fund confirms leading Antiverse's Series A, with the date representing publication of its investment announcement.\"}"}, {"type": "input_text", "text": "[{\"name\":\"exec_command\",\"description\":\"Runs a command in a PTY, returning output or a session ID for ongoing interaction.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { exec_command(args: {\\n  // Shell command to execute.\\n  cmd: string;\\n  // User-facing approval question for `require_escalated`; omit otherwise.\\n  justification?: string;\\n  // True runs the shell with -l/-i semantics; false disables them. Defaults to true.\\n  login?: boolean;\\n  // Output token budget. Defaults to 10000 tokens; larger requests may b
… [22905 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://projectstartups.com/startups/choice-choiceqrcom-2026-03-16/','https://tech.eu/2026/09/03/rightcharge-raises-ps500k-to-scale-fleet-ev-charging-payments-across-europe/']\nfor u in urls:\n p=subprocess.run(['curl','-L','-sS','--max-time','30',u],capture_output=True)\n t=html.unescape(re.sub('<[^>]+>',' ',p.stdout.decode(errors='replace')));t=' '.join(t.split())\n print(u)\n for term in ['Presto','2026-03-16','Soulmates','Purple','September 3','Sep 3']:\n  for m in list(re.finditer(term,t))[:4]:print(t[max(0,m.start()-120):m.end()+180])\nPY","max_output_tokens":1800}));
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"c912e9\",\"wall_time_seconds\":0.633291,\"exit_code\":0,\"original_token_count\":506,\"output\":\"https://projectstartups.com/startups/choice-choiceqrcom-2026-03-16/\\nhttps://tech.eu/2026/09/03/rightcharge-raises-ps500k-to-scale-fleet-ev-charging-payments-across-europe/\\nEurope and further develop its platform for managing fleet\\\\r\\\\ncharging payments. The round was led by existing investor Soulmates Ventures,\\\\r\\\\nwith participation from BlackWood Ventures and Purple Ventures.Rightcharge\\\\r\\\\nprovides a platform that brings home and public EV charging payments into a\\\\r\\\\nsingle sy\\nEurope and further develop its platform for managing fleet\\\\r\\\\ncharging payments. The round was led by existing investor Soulmates Ventures,\\\\r\\\\nwith participation from BlackWood Ventures and Purple Ventures.Rightcharge\\\\r\\\\nprovides a platform that brings home and public EV charging payments into a\\\\r\\\\nsingle sy\\nss Europe and further develop its platform for managing fleet charging payments. The round was led by existing investor Soulmates Ventures , with participation from BlackWood Ventures and Purple Ventures . Rightcharge provides a platform that brings home and public EV charging payments into a single system f\\n payments. The round was led by existing investor Soulmates Ventures,\\\\r\\\\nwith participation from Blac
… [868 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Choice Presto Ventures March 16 2026 raised 6 million'},{q:'site.vestbee.com "Choice" "2026" "Presto"'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Presto Ventures Portfolio Investments, Presto Ventures Funds, Presto Ventures Exits (https://www.cbinsights.com/investor/bohemia-venture-capital)\nciteturn83search0 [wordlim: 200] Crawled: today; ## Presto Ventures Investments ... Their latest investment was in Choice as part of their Series A on March 16, 2026. ... 2/24/2026  | Pre-Seed  | The New Era of Shopping  | $1.4M  | Yes  | Alliance, Andreessen Horowitz, Cory Levy, Davidovs Venture Collective, Evgeny Yurtaev, Greg Tkachenko, Guillaume Roux-Romestaing, hi5 Ventures, Kacper Kielak, Matthieu Tissot, Nicole Buss, Quinn Campbell, Rokubunnoni, Typhon Ventures, Undisclosed Angel Investors, Urvit Goel, and Zituo Chen  | 1\n## Presto Ventures Investments\n\n81 Investments\n\nPresto Ventures has made 81 investments. Their latest investment was in Choice as part of their Series A on March 16, 2026.\n\nImage: CBI Logo\n\n### Presto Ventures Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n3/16/2026  | Series A  | Choice  | $7.1M  | No  | Alea Capital Partners, J&T Ventures, Purple Ventures, Reflex Capital, and Smartlink Partners  | 3\n2/24/2026  | Pre-Seed  | The New Era of Shopping  | $1.4M  | Yes  | Alliance, Andreessen Horowitz, Cory Levy, Davidovs Venture C
… [14109 more characters]
```
</details>

**Codex:**

[redacted: name]
Завершаю проверку цитат и дат. Нашёл более свежую сделку Soulmates Ventures; для Presto оставлю только ту, участие в которой подтверждается текстом источника.


→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Presto Ventures" "2025" investment Behavio'},{q:'"Presto Ventures" "2026" investment -site:cbinsights.com -site:caplight.com -site:presto.lv -music -rice -trino -sql'}],response_length:"short"})); 
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://www.vestbee.com/insights/articles/vc-funding-in-cee-report-q1-2026'\nr=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True).stdout.decode(errors='replace');t=' '.join(html.unescape(re.sub('<[^>]+>',' ',r)).split())\nfor m in re.finditer('Choice|Presto',t):print(t[max(0,m.start()-80):m.end()+180])\nPY","max_output_tokens":1500})); 

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "Presto Ventures | News (https://www.prestoventures.com/news)\nciteturn84search0 [wordlim: 200] Crawled: yesterday; Labs of Latvia Investor Showcase: Presto Ventures – investing in defense of Western values ... More money from US investors and rise of defence tech: VCs’ insights on what to expect in 2025 ... Bavovna’s AI-Powered GPRS-Independent Drone Navigation Lands USD 1.7M of Late-Seed Investment ... Agenda podcast by Seznam Zpravy | On venture capital, geopolitics, and resilience tech investing\n\nIN THE\n\nSPOTLIGHT.\n\nFrom time to time, our founders and portfolio companies make waves in the news – here’s a sneak peek. For more updates, check out our LinkedIn page or follow @PrestoVC on X.\n\n25/5/26\n\n#### Presto Ventures\n\nPředstavenstvo společnosti Presto Ventures II a.s., osoba rizikového kapitálu, se sídlem Na příkopě 859/22, Nové Město, 110 00 Praha 1, IČO: 116 78 704, zapsané v obchodním rejstříku vedeném Městským soudem v Praze, sp. zn. B 26527 (dále jen „Společnost“), svolalo řádnou valnou hromadu na 25.6.2026. Na odkazu níźe jsou umístěny pozvánka a další dokumenty pro akcionáře.\n\nView Article\n\n7/2/25\n\n#### Tech Horizons\n\nWhy the future belongs to resilience tech and AI-powered hardware\n\nView Article\n\n20/1/25\n\n#### Outfindo\n\nCzech Outfindo Raises €1.2M to Transform Online Shopping, Led by Eleven Ventures\n\nView Article\n\
… [15618 more characters]
```
</details>

→ `exec`
```
let a=load("middle"); let p=a.find(x=>x.id==="presto-ventures");p.latest_investment={company:"Choice",date:"2026-03-01",date_precision:"month",url:"https://www.vestbee.com/insights/articles/vc-funding-in-cee-report-q1-2026",quote:"Choice raised €6 million from J&T Ventures, Reflex Capital, and Presto Ventures."};p.active_36m="yes";p.confidence="medium";p.note="A CEE funding report names Presto in Choice's March 2026 round, while newer Tech Horizons transactions belong to a separately managed fund.";store("middle",a);
let l=load("last"),s=l.find(x=>x.id==="soulmates-ventures");s.latest_investment={company:"Rightcharge",date:"2026-09-03",date_precision:"day",url:"https://tech.eu/2026/09/03/rightcharge-raises-ps500k-to-scale-fleet-ev-charging-payments-across-europe/",quote:"The round was led by existing investor Soulmates Ventures"};s.note="The Prague-based venture investor led Rightcharge's September 2026 equity funding round.";store("last",l);
let rows=[...load("first"),...load("middle"),...load("last")]; let orbit=rows.find(x=>x.id==="orbit-capital");orbit.latest_investment.quote="new funding from Orbit Capital and Venture to Future Fund";store("all",rows);
text(rows.map(x=>({id:x.
… [110 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "[{\"id\":\"365-fintech\",\"type\":\"cvc\",\"country\":\"SK\",\"investment\":{\"company\":\"Ctrl Alt\",\"date\":\"2023-10-26\",\"date_precision\":\"day\",\"url\":\"https://www.gaebler.com/VC-Funding-6AFD2FC7-C9AF-4DA6-AC47-2B1240324F7C-Ctrl-Alt-10-26-2023\",\"quote\":\"Forward Partners, MiddleGame Ventures and 365.fintech participated in a $2.6 million capital raise for Ctrl Alt.\"},\"confidence\":\"high\",\"note\":\"The Bratislava-based 365.bank investment subsidiary makes seed equity investments, and the latest verified transaction is Ctrl Alt's October 2023 funding announcement.\"},{\"id\":\"air-ventures\",\"type\":\"vc\",\"country\":\"CZ\",\"investment\":{\"company\":\"Cross Network Intelligence\",\"date\":\"2019-10-24\",\"date_precision\":\"day\",\"url\":\"https://feedit.cz/2019/10/24/air-ventures-investuje-do-hitech-startupu-cross-network-intelligence-ktery-pomaha-budovat-efektivni-site-mobilnim-operatorum-ve-svete-i-u-nas/\",\"quote\":\"Ve startupu se zaměřením na síťovou infrastrukturu získává fond Air Ventures 15% podíl.\"},\"confidence\":\"medium\",\"note\":\"The official site identifies a Prague-based VC, but recent Jiant funding records conflate it with an American namesake and no newer verified investment was found.\"},{\"id\":\"baryon-fund\",\"type\":\"vc\",\"country\":\"SK\",\"investment\":{\"company\":\"Airlogix\",\"date\":\"2026-07-21\",\"date
… [22907 more characters]
```
</details>

→ `exec`
```
let j=JSON.stringify(load("all"));let cmd=`python3 - <<'PY'\nimport json,subprocess,concurrent.futures,re,html\nrows=json.loads(${JSON.stringify(j)})\ndef check(x):\n i=x.get('latest_investment')\n if not i:return (x['id'],'NULL')\n p=subprocess.run(['curl','-L','-sS','--max-time','25',i['url']],capture_output=True)\n b=p.stdout\n if b.startswith(b'%PDF'):\n  b=subprocess.run(['pdftotext','-','-'],input=b,capture_output=True).stdout\n raw=b.decode(errors='replace')\n text=' '.join(html.unescape(re.sub('<[^>]+>',' ',raw)).split())\n q=i['quote']\n ok=subprocess.run(['grep','-Fq',q],input=text,text=True).returncode==0\n if not ok:\n  words=q.split(); needle=next((w for w in words if len(w)>7),words[0]); matches=list(re.finditer(re.escape(needle),text)); excerpts=[text[max(0,m.start()-80):m.end()+200] for m in matches[:2]]\n  return (x['id'],'FAIL',len(b),excerpts)\n return (x['id'],'OK')\nwith concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:\n for r in pool.map(check,rows):print(json.dumps(r,ensure_ascii=False))\nPY`;
text(await tools.exec_command({cmd,max_output_tokens:4000,yield_time_ms:1000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"94d9dd\",\"wall_time_seconds\":1.001648542,\"session_id\":96713,\"original_token_count\":0,\"output\":\"\"}"}]
```
</details>

→ `exec`
```
let rows=load("all");text(rows.reduce((a,r)=>{a.investor[r.is_investor]=(a.investor[r.is_investor]||0)+1;a.active[r.active_36m]=(a.active[r.active_36m]||0)+1;return a},{investor:{},active:{}}));let q={};for(let r of rows){let i=r.latest_investment;if(i){let u=i.url.replace(/\/$/,"");q[u]=(q[u]||0)+i.quote.split(/\s+/).length;}}text(Object.entries(q).filter(x=>x[1]>25));text(await tools.write_stdin({session_id:96713,chars:"",yield_time_ms:1000,max_output_tokens:4000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"investor\":{\"yes\":45},\"active\":{\"yes\":37,\"no\":7,\"unclear\":1}}"}, {"type": "input_text", "text": "[]"}, {"type": "input_text", "text": "{\"chunk_id\":\"0fa5cf\",\"wall_time_seconds\":0.000003875,\"exit_code\":0,\"original_token_count\":760,\"output\":\"[\\\"365-fintech\\\", \\\"OK\\\"]\\n[\\\"air-ventures\\\", \\\"OK\\\"]\\n[\\\"baryon-fund\\\", \\\"FAIL\\\", 93309, [\\\"ортфельною компанією Закревська Оля Інвестиції | 21 Липня, 2026 | 1 хв. читання Інвестиційний фонд Baryon Fund повідомив , що український defence-tech стартап Airlogix входить до його портфеля. Інших деталей угоди ані фонд, ані стартап не розкривають. У Baryon прогнозують, що Airlogix може ст\\\", \\\"в український Airlogix своєю портфельною компанією Закревська Оля 1 хв. читання Інвестиційний фонд Baryon Fund повідомив , що український defence-tech стартап Airlogix входить до його портфеля. Інших деталей угоди ані фонд, ані стартап не розкривають. У Baryon прогнозують, що Airlogix може ст\\\"]]\\n[\\\"bhm-ventures\\\", \\\"OK\\\"]\\n[\\\"cb-investment-management\\\", \\\"OK\\\"]\\n[\\\"credo-ventures\\\", \\\"OK\\\"]\\n[\\\"cs-seed-starter\\\", \\\"OK\\\"]\\n[\\\"czech-founders-vc\\\", \\\"FAIL\\\", 75851, [\\\"rce sellers, has raised €1.8 million in funding.\\\\\\\\r\\\\\\\\nThe round was led by Reflex Capital, with participation from Czech Founders VC\\\\\\\\r\\\\\\\\nand Light
… [2271 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nfrom html.parser import HTMLParser\nclass P(HTMLParser):\n def __init__(self):super().__init__();self.s=[];self.skip=0\n def handle_starttag(self,t,a):\n  if t in ['script','style']:self.skip+=1\n def handle_endtag(self,t):\n  if t in ['script','style']:self.skip-=1\n def handle_data(self,d):\n  if not self.skip:self.s.append(d)\nfor u,term in [('https://foundersfactory.com/articles/investing-in-brightly/','We’re excited'),('https://tech.eu/2026/06/09/merchantee-secures-eur18m-for-european-marketplace-expansion/','with participation')]:\n r=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True).stdout.decode();p=P();p.feed(r);t=' '.join(' '.join(p.s).split());pos=t.find(term);print(u,t[pos:pos+330])\nPY","max_output_tokens":1000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"4e4ff8\",\"wall_time_seconds\":0.733556166,\"exit_code\":0,\"original_token_count\":205,\"output\":\"https://foundersfactory.com/articles/investing-in-brightly/ We’re excited to announce our latest G-Force Climate investment — Brightly . The problem Globally, 2.5 billion tons of food goes to waste every year—that’s around one-third of the total food supply. There are numerous reasons for this, ranging from overproduction to selective consumer practices to misinformed consumer behaviour.\\nhttps://tech.eu/2026/06/09/merchantee-secures-eur18m-for-european-marketplace-expansion/ with participation from Czech Founders VC and Lighthouse Ventures . The company plans to use the funding to accelerate product development, expand support for additional e-commerce marketplaces, and support its growth across Europe. Expansion efforts will initially focus on Poland and Germany, with further launches planned in Fr\\n\"}"}]
```
</details>

→ `exec`
```
let rows=load("all");rows.find(x=>x.id==="baryon-fund").latest_investment.quote="український defence-tech стартап Airlogix входить до його портфеля.";rows.find(x=>x.id==="czech-founders-vc").latest_investment.quote="with participation from Czech Founders VC and Lighthouse Ventures";rows.find(x=>x.id==="g-force").latest_investment.quote="We’re excited to announce our latest G-Force Climate investment";store("all",rows);
text(await tools.exec_command({cmd:`python3 - <<'PY'\nimport json,subprocess,re,html\nfrom html.parser import HTMLParser\nrows=json.loads(${JSON.stringify(JSON.stringify(rows.filter(x=>["baryon-fund","czech-founders-vc","g-force"].includes(x.id))))})\nclass Parser(HTMLParser):\n def __init__(self):super().__init__();self.parts=[];self.skip=0\n def handle_starttag(self,t,a):\n  if t in ('style','script'):self.skip+=1\n def handle_endtag(self,t):\n  if t in ('style','script'):self.skip-=1\n def handle_data(self,d):\n  if self.skip==0:self.parts.append(d)\nfor x in rows:\n i=x['latest_investment'];p=Parser();p.feed(subprocess.run(['curl','-LsS','--max-time','25',i['url']],capture_output=True).stdout.decode(errors='replace'));t=' '.join(' '.join(p.parts).split())\n asser
… [149 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"a712ee\",\"wall_time_seconds\":0.87779075,\"exit_code\":0,\"original_token_count\":21,\"output\":\"baryon-fund quote verified\\nczech-founders-vc quote verified\\ng-force quote verified\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site.0100.vc "Cyprus" "team"'},{q:'site.0100.vc "Bratislava" "Csonga"'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Zero One Hundred | Main page (https://www.0100.vc/)\nciteturn85search0 [wordlim: 200] Crawled: 5 days ago; ## In past 10 years our team ... Request more information (investors@0100.vc)Are you an entrepreneur looking for an investment partner? ... ## You can meet us in our offices in Czechia, Slovakia, Cyprus and the UAE.This website and all its content belong exclusively to 0100 VC RAIF F.C.I.C.\n# A venture capital company founded by builders, with a unique ecosystem, backing the best startups from Emerging Europe and the Middle East.\n\n## An entrepreneurial ecosystem which adds value\n\nFuture winners require more than mere capital. We love working with founders side by side, helping their visions come to life. We’re also bringing unmatched value through the companies we have built: leading players in the innovation, technology, and investment sectors.\n\n## In past 10 years our team\n\nIn past\n\n12 years our team\n\nStarted\n\n10 companies\n\nInvested\n\nin 34 companies\n\nExited\n\n4 companies\n\nOrganized\n\n70+ international conferences\n\nWelcomed\n\n20,000 entrepreneurs to our events\n\nBrought\n\n10,000 investors to our events\n\nHosted\n\n4,000 technical talents and operators at our community events\n\nBuilt\n\n1 unique entrepreneurial ecosystem\n\n## Our portfolio\n\nLeading the AI revolution in cardiovascular care Visit website\n\nUnlocking t
… [14356 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,html,re\nu='https://statistiky.sk/firma/57705542'\nb=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True).stdout.decode(errors='replace');t=' '.join(html.unescape(re.sub('<[^>]+>',' ',b)).split());pos=t.find('štatutármi');print(t[pos:pos+240]);print('Bratislava verified:', 'Bratislava' in t and 'Michal Csonga' in t)\nPY","max_output_tokens":250}));let rows=load("all"),r=rows.find(x=>x.id==="zero-one-hundred");r.managed_from="SK";r.note="The Bratislava CEE entity and Slovak investment partners support Slovakia as the decision team's base, with additional Cyprus and UAE operations and conflicting newer BotBot database dates.";store("all",rows);

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"e2ed8f\",\"wall_time_seconds\":0.450896792,\"exit_code\":0,\"original_token_count\":73,\"output\":\"štatutármi sú Adam Ďurica a Michal Csonga . Zdroj: Register právnických osôb ŠÚ SR · zber 8. 10. 2026. Daňové údaje zo zoznamov Finančnej správy SR (CC0). Údaje z registra Registrové údaje firmy Právna forma Spoločnosť s ručením obmedzeným \\nBratislava verified: True\\n\"}"}]
```
</details>

**Codex:**

[redacted: name]
Цитаты проверены по текстам страниц. Сохраняю JSON в исходном порядке: 45 инвесторов, у 37 найдена сделка за последние 36 месяцев, у 7 — только более старая, у одного дата не подтверждена.


→ `exec`
```
text(await tools.exec_command({cmd:`python3 - <<'PY'\nimport json,re,datetime,collections\nrows=json.loads(${JSON.stringify(JSON.stringify(load("all")))})\nwith open('eval/second-opinion/input.json',encoding='utf-8') as f:source=json.load(f)\nassert isinstance(source,list)\nassert [r['id'] for r in rows]==[r['id'] for r in source]\nassert len(rows)==len(set(r['id'] for r in rows))==45\nallowed_types={'vc','pe','cvc','family_office','angel','private_investor','accelerator','fund_of_funds','public_dfi','platform','adviser','other'}\nwords=collections.Counter()\nfor r in rows:\n assert set(r)=={'id','is_investor','type','managed_from','latest_investment','active_36m','confidence','note'},r['id']\n assert r['is_investor'] in {'yes','no','unclear'}\n assert r['type'] in allowed_types\n assert re.fullmatch('[A-Z]{2}',r['managed_from'])\n assert r['confidence'] in {'high','medium','low'}\n assert isinstance(r['note'],str) and r['note']\n i=r['latest_investment']\n if i:\n  assert set(i)=={'company','date','date_precision','url','quote'}\n  d=datetime.date.fromisoformat(i['date']);assert d<=datetime.date(2026,10,11)\n  assert i['date_precision'] in {'day','month','year'}\n  if i['date_prec
… [866 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"69a6f1\",\"wall_time_seconds\":0.000004916,\"exit_code\":0,\"original_token_count\":31,\"output\":\"Saved 45 records to eval/second-opinion/codex.json\\nis_investor: {'yes': 45}\\nactive_36m: {'yes': 37, 'no': 7, 'unclear': 1}\\n\"}"}]
```
</details>

**Codex:**

[redacted: name]
Saved 45 records to eval/second-opinion/codex.json.
is_investor — yes: 45.
is_investor — no: 0; unclear: 0.
active_36m — yes: 37; no: 7.
active_36m — unclear: 1.

## Thread `2026-10-11T06-13-22`

**Brief / message:**

You are an independent fact-checker. Work in /Users/[redacted]/homeW/ai-dev-test/investor-db, but read ONLY the file eval/second-opinion/input.json (a list of organisations: id, name, country, website). Do NOT open any other file in the repo (no data/, research/, PLAN.md) — your answers must be independent of an earlier assessment.

For each organisation answer, from public web sources you check yourself (use web search and curl):
1. is_investor: "yes" / "no" / "unclear" — does it invest its own or managed capital as equity (or convertible) into private companies, as a core activity? (Crowdfunding platforms, advisers, banks' lending, grant programs = "no".)
2. type: one of vc, pe, cvc, family_office, angel, private_investor, accelerator, fund_of_funds, public_dfi, platform, adviser, other.
3. managed_from: ISO country of the team/manager that makes the investment decisions.
4. latest_investment: the most recent DATED investment you can find: {company, date (YYYY-MM-DD, or YYYY-MM-01 / YYYY-01-01 if only month/year known), date_precision: day|month|year, url, quote}. The quote must be copied verbatim from the raw page text (fetch it with curl and check with grep) — not from a search snippet or a summary. If you can't find any, null.
5. active_36m: "yes" if latest_investment.date >= 2023-10-11, "no" if older, "unclear" if none found.
6. confidence: high / medium / low, and a one-sentence note.

Budget: about 6 searches per organisation; don't get stuck. Write the result to eval/second-opinion/codex.json as a JSON array (same order, include id). Write nothing else, run no git commands, don't mention tools or AI in the file. Print a 5-line English summary at the end (counts per is_investor and active_36m).

→ `exec`
```
text(await tools.exec_command({cmd:"cat eval/second-opinion/input.json",max_output_tokens:12000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"5c923a\",\"wall_time_seconds\":0.000005,\"exit_code\":0,\"original_token_count\":1403,\"output\":\"[\\n  {\\n    \\\"id\\\": \\\"365-fintech\\\",\\n    \\\"name\\\": \\\"365.fintech\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": \\\"https://365fintech.sk/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"air-ventures\\\",\\n    \\\"name\\\": \\\"Air Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"baryon-fund\\\",\\n    \\\"name\\\": \\\"Baryon Fund\\\",\\n    \\\"country\\\": null,\\n    \\\"website\\\": \\\"https://www.baryon.fund/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"bhm-ventures\\\",\\n    \\\"name\\\": \\\"BHM Ventures (BHM group)\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"cb-investment-management\\\",\\n    \\\"name\\\": \\\"CB Investment Management\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": \\\"https://www.cbim.sk/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"credo-ventures\\\",\\n    \\\"name\\\": \\\"Credo Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.credoventures.com/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"cs-seed-starter\\\",\\n    \\\"name\\\": \\\"ČS Seed Starter\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.seedst
… [6949 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'365 fintech investment 2025 2026 startup'},{q:'Air Ventures investment 2025 2026 Czech'},{q:'Baryon Fund investment 2025 2026'},{q:'BHM Ventures investment 2025 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 15.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "Axios Pro Rata: Bankroll bifurcation (https://www.axios.com/newsletters/axios-pro-rata-ef74e379-7b84-4591-85a4-2420bb1f47de)\nciteturn5news12 [wordlim: 100] Published: 2 days ago; The 2026 total now stands at $516 billion invested, which is 44% higher than the highest full-year tally (2021) and 61% more than last year's total. ... • Oratomic, a Pasadena, Calif.-based quantum computing startup, raised $475m in Series B funding at a $5.4b valuation from Arch Venture Partners, Spark Capital, Khosla Ventures, Index Ventures, General Catalyst, and Bezos Expeditions. axios.link/47Nsqp7 ... • Trmeric, a San Ramon, Calif.-based agentic enterprise platform, raised $6.5m in seed funding. ... • Agentiq Sports, a NYC-based fintech for fans to indirectly invest in professional athletes' careers, raised $4m led by Defy VC. axios.link/4hP3faD\n--------------------------------------------------------------------------------\n365.fintech — Investor Profile | Nautis (https://www.getnautis.com/investors/365-fintech)\nciteturn5search0 [wordlim: 200] Published: 5 months ago; Crawled: last month; As a VC group operating from Bratislava, Slovakia, which prioritizes pre-seed & seed API-first, infrastructure & b2b/b2b2c fintech investments in the broader CEE & Baltics region, 365.fintech has built a distinct presence in its market. ... With a disciplined investment approach, t
… [30985 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Air Ventures" investment startup latest'},{q:'"Baryon" fund investment startup'},{q:'"BHM Ventures" investment startup'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Invest in Bravery (https://www.investinbravery.com/en)\nciteturn8search0 [wordlim: 200] Crawled: 4 days ago; Line Rindvig, Baryon Fund ... > “We completed our investment round as a result of pitching at Invest in Bravery's pitch showcase.”\n\n# Matching Ukrainian defensetech startups with international investors.\n\n12+\n\nEvents\n\n2,500+\n\nAttendees\n\n300+\n\nStartups\n\n200+\n\nInvestors\n\n30+\n\nCountries\n\n## We bring together leaders from around the world for one purpose: to strengthen Ukrainian defensetech.\n\n## Appreciated by investors, startups, and ecosystem organizations.\n\nImage: Allan Reagan\n\n> “Thoughtful curation resulted in an efficient first look at top emerging defense tech teams. We've closed two investments first seen at an Invest in Bravery pitch showcase!”\n\nAllan Reagan, UAIDFund\n\nImage: Line Rindvig\n\n> “Invest in Bravery has major respect in the ecosystem. For their independence but more importantly, for always connecting Ukrainian defence founders with people who truly want to help and have the resources to do so, always acting with kindness and integrity.”\n\nLine Rindvig, Baryon Fund\n\nImage: Oleksii Teplukhin\n\n> “We completed our investment round as a result of pitching at Invest in Bravery's pitch showcase.”\n\nOleksii Teplukhin, G-Next Intelligence\n\n## We'll post our upcoming events here. Sign up to our maili
… [30614 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Air Ventures" Czech investment'},{q:'"BHM group" ventures investment 2025'},{q:'"CB Investment Management" investment 2025 2026'},{q:'"Credo Ventures" investment 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Air Ventures (https://airventures.eu/)\nciteturn12search0 [wordlim: 200] Crawled: last week; We are an early-stage venture capital firm based in PragueSubmit project now (analyst@airventures.eu) ... Our investment ticket ranges from 200 k EUR to 2 M EUR, depending on the project, stage and valuation. ... LP offices and business network spread around Europe.Prague, Bratislava, London, Berlin, Luxembourg. ... ## Airventures Czech Republic\n\nWE INVEST IF YOU ARE\n\nWe are an early-stage venture capital firm based in Prague\n\nSubmit project now (analyst@airventures.eu)\n\n## We invest in:\n\n1. Startup LegionAIR from Europe\n\nStrong founders with profound knowledge of the industry who/they aim to disrupt and a team standing behind them.\u0003Our core focus stays with where we are based - CEE, Baltics, DACH, UK.\n\nImage\n\n2. Entrepreneurs working HardAIR\n\nStartups proved by market only. We only work with founders ready to be baptised by the fire of competition. Our core focus lies with Late seed or A-round startups scaling up. Ideally your ARR is 300 k EUR+.\n\nImage\n\n3. BoldAIR Late seed or A-round\n\nOur investment ticket ranges from 200 k EUR to 2 M EUR, depending on the project, stage and valuation.\n\nImage\n\n4. Meaningful Innovation SupportAIR\n\nWe are industry agnostic and ready to nurture any meaningful tech innovation - we don't limit oursel
… [31619 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Seed Starter" investment 2026 startup'},{q:'"Czech Founders VC" investment 2026'},{q:'"DEPO Ventures" investment 2026'},{q:'"Fond inovácií a technológií" investícia'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "Czech Founders VC Portfolio Investments, Czech Founders VC Funds, Czech Founders VC Exits (https://www.cbinsights.com/investor/czech-founders-vc)\nciteturn14search0 [wordlim: 200] Crawled: today; Investment details The round was backed by Czech Founders VC , a founder-centric venture capital firm based in Prague, Czech Republic. ... Investment round also backed by Mews angel investor Ory Weihs Maxfusion plans to use the new funding to scale its product, strengthen sales and marketing, and expand adoption among brands and agencies. ... Their latest investment was in Merchantee as part of their Pre-Seed - II on June 09, 2026. ... Czech Founders VC has 4 team members, including current Founder & General Partner, Vit Horky.\n\nNov 27, 2025\n\nWhy Vít Horký Sold His Startup and Came Home to Build a VC\n\nNov 4, 2025\n\nNový fond Jakuba Havrlanta: Dal do něj stovky milionů a spojuje stovku úspěšných podnikatelů\n\nSep 1, 2025\n\nPraha nestačí. Nikde jinde než v San Franciscu úspěch kolem umělé inteligence mít nemůžete\n\nAug 19, 2025\n\nCzech startup Lignufy secures €40,000 investment to digitize timber trade in Europe\n\n## Czech Founders VC Investments\n\n38 Investments\n\nCzech Founders VC has made 38 investments. Their latest investment was in Merchantee as part of their Pre-Seed - II on June 09, 2026.\n\nImage: CBI Logo\n\n### Czech Founders VC Investments 
… [26776 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"DEPO Ventures" investment 2026'}],response_length:"long"}));
text(await tools.web__run({search_query:[{q:'"G-Force" fund investment 2026 Slovakia'},{q:'"GAIN Ventures" Carebot July 2026'},{q:'"i&i Biotech" investment 2026'},{q:'"Impulse Ventures" investment 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 15450)\nTotal output lines: 1033\n\nDEPO Ventures Portfolio Investments, DEPO Ventures Funds, DEPO Ventures Exits (https://www.cbinsights.com/investor/depo-ventures)\nciteturn16search0 [wordlim: 200] Crawled: today; DEPO Ventures is a European venture capital firm focusing on early-stage startups from CEE and the Baltic region. ... Organized by Czech investment group DEPO Ventures , the two-day event will welcome startup investors, founders and members of the wider innovation ecosystem, alongside specialized industry tracks, startup pitches and an extended programme. ... That is why we are giving both topics prominent space this year and creating a place where true technological sovereignty is born,’ Petr Šíma , partner at DEPO Ventures and founder of the Engaged Investments Conference, explains Defense Innovation Meets Frontline Reality The defense track will be organized in collaboration with the Invest in Bravery initiative, which has deep links to Ukraine’s technology and defense ecosystem. ... 4/28/2026  | Pre-Seed  | Tapaya  | $1.17M  | Yes  | BADideas.fund, and Passion Capital  | 2\nThe format reflects the conference’s wider ambition to create practical connections between emerging technologies, founders and capital. In a Nutshell\n\n## DEPO Ventures Investments\n\n118 Investments\n\nDEPO Ventures has
… [38642 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Inven Capital" investment 2026'},{q:'"365.fintech" "Velaris" 2022'},{q:'"Air Ventures" investment 2024 2025 startup'},{q:'"CBIM" investment 2025 startup'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Inven Capital (https://www.invencapital.cz/)\nciteturn18search0 [wordlim: 200] Crawled: today; Inven leads VYTAL’s growth round extension to EUR 14.2m Inven co-leads £11m SeriesA in Ember alongside 2150 and AENU HYDROGRID Raises 8.5M USD Series-A to Digitalize the World’s Largest Source of Renewable Energy Inven’s portfolio company Eliq raises a €10mn financing round Inven and Insight Partners join forces to lead USD 35mn Series C round in WINT, frontrunner in sustainable water management and water risk mitigation Inven Capital raises additional €50 million from the European Investment bank for their new fund, bringing the total committed capital to €500 million Inven’s portfolio company Woltair raises €16.3m to help Europeans heat and power their homes Inven leads $40m Series D round in Isreal based Taranis Inven’s portfolio company Zolar raises €100 million with Inven participating Inven Capital successfully sold its share in the Israeli start-up Driivz, making a multiple return on its initial investment in just three years. tado° raises €38 million and announces a partnership with noventic ... 2026 Public call for share subscription 062026 Subfund C 3.\n## Play\nthe video\n\nSee more who we are!\n\n## Constellation for success\n\nAs a venture capital fund we invest EUR 500m from institutional investors and global corporates in the most innovative startu
… [32048 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"ČS Seed Starter" investice 2026'},{q:'"BHM Ventures" startups'},{q:'"CB Investment Management" Slovak investment latest'},{q:'"G-Force" fund latest investment startup'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "Výroční zpráva 2025 (https://www.csas.cz/static_internet/cs/Redakce/Ostatni/Ostatni_IE/Prilohy/vz-2025-cs.pdf)\nciteturn20search12 [wordlim: 200] Published: 6 months ago; Dividendy se nadále vykazují ve výkazu zisku a ztráty, i když je stanoveno právo Banky přijímat platby, s výjimkou případů, kdy představují spíše návratnost investice než výnos z investice.V roce 2024 Banka navýšila své investice do společnosti ČS NHQ, s.r.o., o 3,1 mld. ... Dne 20. prosince 2024 Banka prodala dceřinou společnost REICO investiční společnost České spořitelny, a.s., společnosti Erste Asset Management GmbH. ... <tr><td>ČS Seed Starter, a.s.</td><td>6,0</td><td>Česká republika</td><td>CZK</td><td>100%</td><td>100%</td><td>318</td></tr>\nplatí, pokud vyřazení vede k sestupnému kroku z dceřiného podniku do přidruženého podniku oceněného pořizovací cenou.\n\nDividendy se nadále vykazují ve výkazu zisku a ztráty, i když je stanoveno právo Banky přijímat platby, s výjimkou případů, kdy představují spíše návratnost investice než výnos z investice.\n\nV roce 2024 Banka navýšila své investice do společnosti ČS NHQ, s.r.o., o 3,1 mld. Kč, do společnosti Dostupné bydlení České spořitelny, a.s., o 1,1 mld. Kč, do společnosti Budějovická Development, s.r.o., o 750 mil. Kč a do společnosti ČS Seed Starter, a.s., o 37,5 mil. Kč. Dne 20. prosince 2024 Banka prodala dceřinou společnost REICO
… [24662 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"BHM" "ventures" "Sharry"'},{q:'"CB Investment Management" "2023" "investícia"'},{q:'"Seed Starter" "2026" "Pointee"'},{q:'"GAIN Ventures" "Carebot" "2026" investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Carebot Closes the Largest Investment Round in Its History - Carebot (https://www.carebot.com/news/carebot-closes-the-largest-investment-round-in-its-history)\nciteturn24search0 [wordlim: 200] Published: 2 months ago; Crawled: last month; Carebot Closes the Largest Investment Round in Its HistoryAug 3, 2026 ... The round was led by Garage Angels and Electron Capital Partners, with JIC Ventures joining the company alongside existing investors Gain Ventures and Eva Janečková.\n\nCarebot Closes the Largest Investment Round in Its History\n\nAug 3, 2026\n\n### Carebot Closes the Largest Investment Round in Its History\n\nNews\n\nCarebot Closes the Largest Investment Round in Its History\n\nAug 3, 2026\n\n### Carebot Closes the Largest Investment Round in Its History\n\nNews\n\nCarebot Closes the Largest Investment Round in Its History\n\nAug 3, 2026\n\n### Carebot Closes the Largest Investment Round in Its History\n\nImage\n\nCarebot has secured an investment of more than €1.5 million, the largest in the company’s history. The round was led by Garage Angels and Electron Capital Partners, with JIC Ventures joining the company alongside existing investors Gain Ventures and Eva Janečková. \n\nThe investment comes at a time of strong commercial growth. Over the past year, Carebot increased its contracted monthly recurring revenue by 750%, and based on already sign
… [22625 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Minerva Humanoids" "Credo" October 6 2026'},{q:'"Merchantee" "2026" "investment"'},{q:'"ArcSpace" "DEPO" "August"'},{q:'"Definic" "Seed Starter" 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Minerva Humanoids Emerges From Stealth With $10M Pre-Seed (https://www.globenewswire.com/news-release/2026/10/06/3375277/0/en/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-world-s-most-dangerous-jobs.html)\nciteturn25search0 [wordlim: 200] Published: 5 days ago; Crawled: 4 days ago; October 06, 2026 06:10 ET  | Source: Minerva Humanoids Minerva Humanoids ... 06, 2026 (GLOBE NEWSWIRE) -- Minerva Humanoids, a robotics company building humanoid robots for the world’s most dangerous jobs in onshore and offshore oil and gas operations and public safety, today announced it has raised approximately $10 million in pre-seed funding led by General Catalyst, with Long Journey Ventures and Credo Ventures as co-leads, and participation from MVP Ventures, Kaya, RunwayVC, Compound, Founders Embassy, Hugging Face, Codecademy, YG, Walter Ventures, Tiny Ventures, Chaotica, and Babylon.\n\n# Minerva Humanoids Emerges From Stealth With $10M Pre-Seed Round Led by General Catalyst to Build Humanoid Robots for the World's Most Dangerous Jobs\n\n## Semi-autonomous humanoid lets trained specialists handle hazardous energy and public safety work from a safe distance with full control\n\nOctober 06, 2026 06:10 ET  | Source: Minerva Humanoids Minerva Humanoids\n\nSAN FRANCISCO, Oct. 06, 2026 (GLOBE NEWSWIRE) --
… [33160 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site:inibio.eu 2026 investment'},{q:'"Impulse Ventures" "Safetica" 2025'},{q:'"Fond inovácií" "investoval" startup'},{q:'"BHM" "Sharry" investice 2024 2025'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Impulse Ventures Portfolio Investments, Impulse Ventures Funds, Impulse Ventures Exits (https://www.cbinsights.com/investor/impulse-ventures)\nciteturn28search0 [wordlim: 200] Crawled: last week; Impulse Ventures is a venture capital investor focused on tech startups in the CE region. ... Their latest investment was in Safetica as part of their Series A on January 24, 2025.\n\nVenture Capital\n\n# Impulse Ventures\n\nimpulseventures.com\n\n## Investments\n\n10\n\n## Portfolio Exits\n\n1\n\n## About Impulse Ventures\n\nImpulse Ventures is a venture capital investor focused on tech startups in the CE region.\n\n## Headquarters Location\n\nLaubova 1729/8\n\nPrague, 130 00,\n\nCzech Republic\n\n## Impulse Ventures Investments\n\n10 Investments\n\nImpulse Ventures has made 10 investments. Their latest investment was in Safetica as part of their Series A on January 24, 2025.\n\nImage: CBI Logo\n\n### Impulse Ventures Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n1/24/2025  | Series A  | Safetica  | $4M  | Yes  | Jakub Mahdal, Michael Poplar - Rostock, Ondrej Smolar, and Ondrej Tomek  | 3\n10/24/2022  | Seed VC - III  | Dataddo  | $2M  | No  |  | 1\n6/23/2022  | Seed VC  | Taikun  |  | Yes  | Gi21 Capital, and N
… [27676 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site:inibio.eu "2026"'},{q:'"HERlab" "G-Force" investment 2024'},{q:'"BHM" "invest" "2026" "Simpleway"'},{q:'"CB Investment Management" "investícia" "2024"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "2024\nVÝROČNÁ SPRÁVA (https://www.sih.sk/data/files/sk_vyrocna-sprava-sih-2024-517.pdf)\nciteturn30search12 [wordlim: 200] Published: 6 months ago; Investícia ... 4 600 000,00 ... CB Investment Management s. r. o.\nSlovakia, a.s., pobočka zahraničnej banky\n \nSlovenská záručná a rozvojová banka, a. s.\n \nČeskoslovenská obchodná banka, a.s.\n \n182 700 504,55 €  \n203 000 560,61 €  \nCEZ FS\n \nČeskoslovenská obchodná banka, a.s. \n(ex OTP Banka Slovensko, a.s.)\nPORTFÓLIOVÁ ZÁRUKA\nPRVEJ STRATY (FLPG) \n- pre MSP s primárnym\nzameraním na\nprevádzkové financovanie\n \nBKS Bank AG, pobočka zahraničnej\nbanky v SR\n \n \nOberbank AG pobočka zahraničnej\nbanky v Slovenskej republike\n \nPoštová banka, a.s.\n \nJ & T BANKA, a.s., pobočka zahraničnej\nbanky\n \n3 401 923,75 €  \n48 598 910,67 €  \nCEZ FS\nUniCredit Bank Czech Republic and\nSlovakia, a.s., pobočka zahraničnej banky\nPORTFÓLIOVÁ ZÁRUKA PRVEJ\nSTRATY (FLPG) \n pre MSP \n \n735 323,32  \n3 313 248,10 \nBoataround.com, a.s.\nCEZ FS\n \n \nSlovenská sporiteľňa, a.s.\n1 658 128,91 €  \n8 290 644,54 €  \n \n \n \n3 100 000,00  \n4 600 000,00 \nAeroMobil R&D, s. r. o. \n \nPORTFÓLIOVÁ ZÁRUKA PRVEJ\nSTRATY (FLPG) \npre MSP v oblasti výskumu, vývoja\na inovácií\n \nGreenWay Infrastructure s.r.o.\n5 000 000,00 \n24 424 000,00 \n \n \n \nSlovenská záručná a rozvojová banka, a. s.\nCEZ FS\n22 282 058,48 € 
… [29862 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\npages=[('365','https://365fintech.sk/','Velaris|2022|Tapline|Bratislava'),('air','https://www.insightart.eu/2024/06/17/investors-from-air-ventures-join-insightart/','invest|2024'),('baryon','https://scroll.media/2026/07/21/baryon-fund-airlogix/','Інвестиційний фонд Baryon|2026'),('credo','https://www.globenewswire.com/news-release/2026/10/06/3375277/0/en/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-world-s-most-dangerous-jobs.html','with Long Journey|October 06'),('gain','https://www.carebot.com/news/carebot-closes-the-largest-investment-round-in-its-history','round was led|Aug 3'),('impulse','https://therecursive.com/czech-safetica-secures-e3-8-investment-to-fuel-expansion-in-the-us/','funding comes from|24 January'),('fit','https://www.teraz.sk/najnovsie/fit-investicia-faktury-spracovanie/73190-clanok.html','FIT\\) zrealizoval|februára 2014'),('bio','https://www.inibio.eu/','2026|Ternary|investment'),('inven','https://www.invencapital.cz/','Wint Raises|2026'),('cb','https://www.cbim.sk/sk','2023|investíciu|B
… [460 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"812864\",\"wall_time_seconds\":0.754503917,\"exit_code\":0,\"original_token_count\":6913,\"output\":\"<stdin>:2: SyntaxWarning: \\\"\\\\)\\\" is an invalid escape sequence. Such sequences will not work in the future. Did you mean \\\"\\\\\\\\)\\\"? A raw string is also an option.\\n365 https://365fintech.sk/\\nVelaris\\nVelaris is a London based platform for customer success management and operations.\\nTapline\\nTapline is a trading platform that enables companies with recurring revenues to receive frictionless, non-dilutive funding.\\nVelaris takes off with €4.7 million to roll out AI-driven customer success \\nSeptember 20, 2022\\n The fresh capital will be used to build a Machine Learning-led layer to Velaris’ platform enabling B2B tech companies to wholly understand their customers, deepen the relationship, and retain...\\nSeptember 15, 2022\\n811 02, Bratislava\\n365.fintech, a.s. © 2022. All Rights Reserved.\\n\\nair https://www.insightart.eu/2024/06/17/investors-from-air-ventures-join-insightart/\\n\\nbaryon https://scroll.media/2026/07/21/baryon-fund-airlogix/\\n{\\\"@context\\\":\\\"https:\\\\/\\\\/schema.org\\\",\\\"@graph\\\":[{\\\"@type\\\":\\\"Article\\\",\\\"@id\\\":\\\"https:\\\\/\\\\/scroll.media\\\\/2026\\\\/07\\\\/21\\\\/baryon-fund-airlogix\\\\/#article\\\",\\\"isPartOf\\\":{\\\"@id\\\":\\\"https:\\\\/\\\\/scroll.media\\\\/
… [32326 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\npages=[('365','https://365fintech.sk/'),('air','https://www.insightart.eu/'),('bio','https://www.inibio.eu/'),('inven','https://www.invencapital.cz/'),('cb','https://www.cbim.sk/sk'),('baryon','https://scroll.media/2026/07/21/baryon-fund-airlogix/')]\ndef go(p):\n raw=subprocess.run(['curl','-LsS','--max-time','25',p[1]],capture_output=True,text=True).stdout\n links=re.findall(r'href=[\"\\']([^\"\\']+)[\"\\']',raw)\n return p[0]+' LINKS\\n'+'\\n'.join(x for x in links if re.search('velaris|tapline|invest|news|post|ternary|wint|insightart|202',x,re.I))[:6000]\nfor r in concurrent.futures.ThreadPoolExecutor(6).map(go,pages):print(r)\nPY","max_output_tokens":9000}));
text(await tools.web__run({search_query:[{q:'"i&i" "Ternary Therapeutics" March 2026'},{q:'"BHM" "Sharry" "investment" 2023'},{q:'"Air Ventures" "InsightART" investors'},{q:'"365.fintech" "Tapline" 2022 2023'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 10723)\nTotal output lines: 645\n\n{\"chunk_id\":\"14d6ad\",\"wall_time_seconds\":0.82089825,\"exit_code\":0,\"original_token_count\":3136,\"output\":\"365 LINKS\\n#news\\n#news\\nhttps://www.velaris.io\\nhttps://www.velaris.io\\nhttps://tapline.io\\nhttps://tapline.io\\nhttp://www.speedinvest.com\\nhttp://www.speedinvest.com\\n/news/velaris-takes-eu47-million-roll-out-ai-driven-customer-success-platform\\n/news/ondato-final-piece-kyc-compliance-puzzle\\n/news/investing-tymit-next-generation-credit-card\\n/news/investsuite-investing-wealthtech-service\\n/news/we-invested-pynk-and-here-why\\n/news/365fintech-participated-fincompares-series-round\\n/news/pentech-sme-invoice-factoring-startup-joins-365fintech-portfolio\\n/news/365fintech-invests-startup-wise-guys\\n/news/365fintech-partners-mkb-fintechlab\\n/news/365fintech-invests-dateio-card-linked-offers-startup\\n/news/365fintech-secured-its-first-large-investments-also-thanks-help-booster-labs-experts-incubation\\n/news/365fintech-closes-partnership-deal-finch-capital-premier-european-fintech-vc\\n/news/365fintech-partnering-speedinvest\\n/news/365fintech-startup-investment-platform-launches-core-component-365-ecosystem\\nair LINKS\\nhttps://insightart.eu/\\nhttps://insightart.eu/wp-content/plugins/bootstrap-for-contact-form-7/assets/dist/css/style.min.css?ve
… [39093 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Ctrl Alt" "365" "2023" funding'},{q:'"Minerva Humanoids" "$10M" October 2026 funding Credo'},{q:'"Merchantee" "Czech Founders" June 2026'},{q:'"Ternary Therapeutics" "i&i" funding March 2026'}],response_length:"long"}));
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\npages=[('seed','https://www.sih.sk/en/aktuality/sih-podporil-definic-slovensku-technologicku-spolocnost-s-globalnymi-ambiciami','participated|18.06'),('inven','https://www.prnewswire.com/news-releases/wint-raises-36-million-in-series-d-funding-to-scale-ai-powered-water-intelligence-globally-302873443.html','2026|Inven Capital|co-led'),('baryon','https://scroll.media/2026/07/21/baryon-fund-airlogix/','Інвестиційний фонд|липня|Липня'),('air','https://middlecap.com/2018/12/18/middlecap-group-ziskala-majoritu-v-startupovom-fonde-air-ventures/','2018|Air Ventures enters'),('depo','https://spacebandits.io/startups/arcspace','closed in August'),('impulse','https://www.finsmes.com/2025/01/safetica-raises-usd4m-in-series-a-funding.html','Impulse|January|Jan'),('fit','https://www.teraz.sk/najnovsie/fit-investicia-faktury-spracovani
… [645 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Minerva Humanoids Emerges From Stealth With $10M Pre-Seed (https://www.globenewswire.com/news-release/2026/10/06/3375277/0/en/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-world-s-most-dangerous-jobs.html)\nciteturn46search0 [wordlim: 200] Published: 5 days ago; Crawled: 4 days ago; October 06, 2026 06:10 ET  | Source: Minerva Humanoids Minerva Humanoids ... 06, 2026 (GLOBE NEWSWIRE) -- Minerva Humanoids, a robotics company building humanoid robots for the world’s most dangerous jobs in onshore and offshore oil and gas operations and public safety, today announced it has raised approximately $10 million in pre-seed funding led by General Catalyst, with Long Journey Ventures and Credo Ventures as co-leads, and participation from MVP Ventures, Kaya, RunwayVC, Compound, Founders Embassy, Hugging Face, Codecademy, YG, Walter Ventures, Tiny Ventures, Chaotica, and Babylon.\n\n# Minerva Humanoids Emerges From Stealth With $10M Pre-Seed Round Led by General Catalyst to Build Humanoid Robots for the World's Most Dangerous Jobs\n\n## Semi-autonomous humanoid lets trained specialists handle hazardous energy and public safety work from a safe distance with full control\n\nOctober 06, 2026 06:10 ET  | Source: Minerva Humanoids Minerva Humanoids\n\nSAN FRANCISCO, Oct. 06, 2026 (GLOBE NEWSWIRE) --
… [28156 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw1WnxbqRJx8d9qzQjOo1S-5NebCBjPCvRROEA7hqppllOA_ias2vHIkGEBshW5KQhQWd8D9e8nxy0R8c7g4tq7n55D4ycN-24jdveThGYXAd-LbtJj4FZcTZmIfbgGh_VbfopnuER7qxMdqO9NnpCrmd4oHb4pNA0dxPz0sOcOyeupQLGMl5YGDzmm7mHevlqIe2HVAa7JgrucVWK4c_Rmv9p9SBxtEP299fJAnhm1uJIpDqpuX48aZk2Cf7ijpmBIL45tH022DJ75svViF9c0dkTa9vfBKiad9wZvcDs-QVR5BZyafHSlJG4asW27jGg55PHbLEiAcnEZcpbnXwlyz_zJPBgGqE86w4SHVw2Z2WK0F7bcMwUAdYtmIuL6dSbfef6p0kLlDPxqN_Skq-ZjRRv684fj1h2JCNMfklewVzSqTTr_qrDCLgfqUWrXDYyOAs0Y-vA9QDlsrhc8-tMmGoYHA_mkGGP-gMQlEu1I97vwsd35-HbQ1cUWABCpC4nOLN12DUGGFaz87WkMrlL9XNkuMhNXZogKw2dRaDU1Dh-XYXDYmrf7BMcZyq4Ajpb05qSpFoCmieDARRlAeC7sb7aNF46BXN-35lPmD-GgPT5PritMQmoQad1wqMDXG4J-E1qCQbT05VxgxrOGdPf8lgbHnPgpExQn9rcrK5885K-4bjtMOV4CiBh2npiRZ-SEl"}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"curl -LsS --max-time 20 https://scroll.media/2026/07/21/baryon-fund-airlogix/ | head -c 200","max_output_tokens":1000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"cc978e\",\"wall_time_seconds\":0.000005417,\"exit_code\":0,\"original_token_count\":68,\"output\":\"<!DOCTYPE html>\\n<html lang=\\\"uk\\\">\\n\\n<head>\\n    <meta charset=\\\"UTF-8\\\">\\n    <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1.0\\\">\\n    <meta name='robots' content='index, follow, max-imagecurl: (56) Failure writing output to destination, passed 43 returned 0\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://scroll.media/2026/07/21/baryon-fund-airlogix/'\nr=subprocess.run(['curl','-LsS',u],capture_output=True,text=True)\ns=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r.stdout,flags=re.S|re.I)\ns=html.unescape(re.sub('<[^>]+>','',s));s=re.sub(r'\\s+',' ',s)\np=subprocess.run(['grep','-oE','.{0,20}Інвестиційний фонд.{0,250}'],input=s,capture_output=True,text=True)\nprint(len(r.stdout),len(s),p.returncode,p.stderr,p.stdout)\nprint(s[s.find('Інвестиційний'):s.find('Інвестиційний')+300])\nPY","max_output_tokens":1000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"6b8908\",\"wall_time_seconds\":0.054415791,\"exit_code\":0,\"original_token_count\":373,\"output\":\"89517 4482 0  026 | 1 хв. читання Інвестиційний фонд Baryon Fund повідомив, що український defence-tech стартап Airlogix входить до його портфеля. Інших деталей угоди ані фонд, ані стартап не розкривають. У Baryon прогнозують, що Airlogix може стати одним із глобальних лідерів у повітряних технологіях\\nа Оля 1 хв. читання Інвестиційний фонд Baryon Fund повідомив, що український defence-tech стартап Airlogix входить до його портфеля. Інших деталей угоди ані фонд, ані стартап не розкривають. У Baryon прогнозують, що Airlogix може стати одним із глобальних лідерів у повітряних технологіях\\n\\nІнвестиційний фонд Baryon Fund повідомив, що український defence-tech стартап Airlogix входить до його портфеля. Інших деталей угоди ані фонд, ані стартап не розкривають. У Baryon прогнозують, що Airlogix може стати одним із глобальних лідерів у повітряних технологіях. Серед переваг стартапу фонд на\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\npages=[('365','https://www.uktech.news/fintech/ctrl-alt-funding-20231024','365.fintech'),('credo','https://traded.co/vc/deal/minerva-humanoids-raises-10-million-in-pre-seed-funding-led-by-general-catalyst/','Credo Ventures'),('seed','https://www.sih.sk/en/aktuality/sih-podporil-definic-slovensku-technologicku-spolocnost-s-globalnymi-ambiciami','participated'),('inven','https://www.prnewswire.com/news-releases/wint-raises-36-million-in-series-d-funding-to-scale-ai-powered-water-intelligence-globally-302873443.html','Inven'),('depo','https://spacebandits.io/startups/arcspace','closed in August'),('impulse','https://www.finsmes.com/2025/01/safetica-raises-usd4m-in-series-a-funding.html','Impulse'),('bio','https://itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues','i&i Biotech'),('air','https://middlecap.com/2018/12/18/middlecap-group-ziskala-majoritu-v-startupovom-fonde-air-ventures/','Air Ventures enters')]\nfor id,u,p in pages:\n r=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True,text=True)\n s=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r.stdout,flags=r
… [347 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 4.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"1a11ed\",\"wall_time_seconds\":3.8764985,\"exit_code\":0,\"original_token_count\":904,\"output\":\"365 https://www.uktech.news/fintech/ctrl-alt-funding-20231024 5548 1 \\nDATES []\\ncredo https://traded.co/vc/deal/minerva-humanoids-raises-10-million-in-pre-seed-funding-led-by-general-catalyst/ 5793 1 \\nDATES []\\nseed https://www.sih.sk/en/aktuality/sih-podporil-definic-slovensku-technologicku-spolocnost-s-globalnymi-ambiciami 844852 0 h J&T Ventures fund and ČS Seed Starter (Česká sporiteľňa), participated in a €2.5 million investment round in the technology company Definic. The capital raised will support the further development of the platform, which helps large enterprises more efficiently select and manage IT vendors, as well as its expansion into\\n\\nDATES ['truments 18.06.2026 SIH supports Defini', 'lava, June 18, 2026 – Slovak Investment']\\ninven https://www.prnewswire.com/news-releases/wint-raises-36-million-in-series-d-funding-to-scale-ai-powered-water-intelligence-globally-302873443.html 210341 0 cle Share toX Share this article Share toX LIP Ventures and Inven Capital lead round as enterprise demand for water risk management accelerates NEW YORK, Sept. 9, 2026 /PRNewswire/ -- Wint, the leading provider of water management solutions for the built environment, today announced it has raised $36 million in Se\\nries D funding co-led
… [2382 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"BHM" "Sharry" funding investment'},{q:'"CB Investment Management" "2023" investment startup latest'},{q:'"G-Force" investment 2025 Brightly'},{q:'"Gain Ventures" Prague team'}],response_length:"long"}));
text(await tools.web__run({search_query:[{q:'"Merchantee" "Czech Founders" June'},{q:'"Cross Network Intelligence" "Air Ventures" 2019'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 15822)\nTotal output lines: 1407\n\nPORTFOLIO - BHM Group (https://www.bhmgroup.eu/portfolio)\nciteturn55search0 [wordlim: 200] Crawled: last week; BHM Renewables se může pochlubit i tím, že ve svém oboru je partnerem největších mezinárodních hráčů a globálních firem. ... Tech Startups Sharry\n\nImage: Czech Republic\n\nRezidenční projekt nadstandardního bydlení Senior Resort Štěpánka z portfolia investiční skupiny BHM group byl v nominován do 25. ročníku soutěže o titul BEST OF REALITY – NEJLEPŠÍ Z REALIT 2023.\n\nUnikátní koncept, založený na best practice z USA a UK, společného bydlení seniorů ve spojení se zdravotnickým servisem, službami, nabídkou volnočasových aktivit a s dosažitelným financováním.\n\n  * Projekt je určen pro klienty v raném seniorském věku nad 50 let, případně pro mladší hendikepované obyvatele.\n  * 184 apartmánů s dispozicemi 1+kk, 2+kk a 3+kk ve vysokém standardu stavebních materiálů, zařizovacích předmětů, s bezbariérovým přístupem a v bezprostřední blízkosti lesoparku Štěpánka v Mladé Boleslavi.\n  * Resort je navržen dle aktuálních trendů kvalitního bydlení s důrazem na dlouhodobou udržitelnost budov i celého areálu.\n  * Projekt 100% vyprodán, úspěšně dokončen a zkolaudován.\n\nTech Startups Sharry\n\nImage: Sharry\n\nTech Startups\n\nImage: Sharry\n\n--------------------------
… [39107 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw17Gyxj2F2BNiILVbyHzazeAE2vsbX31uWhQ2UMt1S8De5FMH8rDgX-AH8i6K2slAa5xLUngj43PUqYyPgCNUIvOMi-E5nzqIZT9FQrbfXO_sxixajDr7wxy-Pbsn3AkLi-PMclnioGHfW7vGF-0A2vJRH_NPxzb0VDZIo7S2fIMdjoX0Ftq6Lw-UfAmoSnT9zs9DQK5CtBjx4Lpvjn31JSLskX7uTojO3C4gZ6QtCfmfN3ZWSfaYOcDHcDkRuWcABWczFlF6akBdAZfsTm826n2OtyIm8rgM8L1Y_XRXq6L8GyM02sWnhTlO0tTYcj5O3y4ERXPbIOJEqFRuScJvV_GfLhnUglKYO9SL0yHqgTGm-hfdGOiQ5pp3pazZPWQcEy_fPNFKwRDdCPL29yQnufS_yOcUk2FYQ1HU162_Dxy3diGwf_PVHQfB8DLh5xHAcaKoiC07_LqIabZEu_xPJ8UKQYG0oos8Np9RRFgmMFPJeul8EB8EMukHirTm4KU4yYu1Bb10CLms3xGbCfNT8plFxeUdtSV6BtIF7rRstOQBJaf_BeaaZgtnf2D4fsd41fa-OoxIBkKv6o_egd6LjHsvI6BgHfSG7oWtSCo3WjB7l0zpanKZF611MxtAZzKFEdHV1kvg9eP47H7WWSFEXpCQ=="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"BHM Ventures" investment'},{q:'"CB Investment Management" latest investment WageNow'},{q:'"GAIN Ventures" Jan Prague venture'},{q:'"G-Force" "Raya Power" investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "G-Force - Portfolio companies (https://www.usegforce.com/portfolio)\nciteturn58search0 [wordlim: 200] Crawled: yesterday; Raya Power Modular, plug-and-play solar and battery pod that delivers backup power and bill savings to the majority of Americans excluded from rooftop solar — renters, low-to-middle income households, and permit-constrained homeowners. ... PowereX AI-powered energy trading platform enabling virtual power plant customer to capitalize on “behind-the-meter” energy market. ... By joining us, you become part of a global community of over 300 founders, thousands of investors, gaining unrivaled access to leading decision makers across industry, government, and academia. ... G-Force, s. r. o., Company ID 53 527 798, is a registered manager entered in the Register of Alternative Investment Fund Managers maintained by the National Bank of Slovakia under registration number 0029.Registration with the National Bank of Slovakia does not constitute approval or endorsement of G-Force’s investment strategy, investments or sustainability claims.\n### Portfolio companies\n\nWe invest in early-stage technology companies developing solutions with the potential to contribute to climate and environmental objectives while building scalable global businesses.\n\nDescriptions of portfolio companies reflect their technologies, business models and intended applic
… [27313 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"GAIN Ventures" "Lukáš"'},{q:'"CB Investment Management" "WageNow" 2023'},{q:'"BHM" "Sharry" "2020"'},{q:'"G-Force" "Raya" funding 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "GAIN Ventures s.r.o. - IČO 05690935 - Obchodní rejstřík na Podnikatel.cz (https://www.podnikatel.cz/rejstrik/gain-ventures-s-r-o-05690935/)\nciteturn60search0 [wordlim: 200] Crawled: 3 months ago; #### Lukáš Uhlík, DiS. ... #### GAIN Private Equity s.r.o.\n## Statutární orgán\n\n### 1 fyzická osoba\n\n#### Lukáš Uhlík, DiS.\n\njednatel\n\nvznik funkce: 9. 1. 2017\n\nŽitná 606/29, Praha, 110 00, Česká republika\n\nDalších 13 vztahů k této osobě\n\n  * člen představenstva\n\n#### Chirurgické obory servis, a.s.\n\nSeydlerova 2451/8, Praha Stodůlky (Praha 13), 158 00\n\n  * jednatel\n\n#### Chirurgické obory Praha s.r.o.\n\nSeydlerova 2451/8, Praha Stodůlky (Praha 13), 158 00\n\n  * jednatel\n\n#### GAIN Private Equity s.r.o.\n\nNa strži 2102/61a, Praha Krč, 140 00\n\n  * jednatel\n\n#### Bojkovice s.r.o.\n\nSvětlov 968, Bojkovice, 687 71\n\n  * jednatel\n\n#### ImunoGen s.r.o.\n\nSluneční náměstí 2588/14, Praha Stodůlky (Praha 13), 158 00\n\n  * jednatel\n\n#### GAIN Solution II, s.r.o.\n\nNa strži 2102/61a, Praha Krč, 140 00\n\n  * jednatel\n\n#### Klinika JL - MR, s.r.o.\n\nV hůrkách 1296/10, Praha Stodůlky (Praha 13), 158 00\n\n  * Jednatel\n\n#### Klinika JL - AS, s.r.o.\n\nV hůrkách 1296/10, Praha Stodůlky (Praha 13), 158 00\n\n  * Jednatel\n\n#### OA ortopedie NJ, s.r.o.\n\nŠenovská 1829, Petřvald, 735 41\n\n  * jednatel\n\n#### Klinika JL - Kardio, s.r
… [24311 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\npages=[('air','https://feedit.cz/2019/10/24/air-ventures-investuje-do-hitech-startupu-cross-network-intelligence-ktery-pomaha-budovat-efektivni-site-mobilnim-operatorum-ve-svete-i-u-nas/','15% podíl'),('cf','https://tech.eu/2026/06/09/merchantee-secures-eur18m-for-european-marketplace-expansion/','Czech Founders'),('365','https://www.gaebler.com/VC-Funding-6AFD2FC7-C9AF-4DA6-AC47-2B1240324F7C-Ctrl-Alt-10-26-2023','365.fintech'),('credo','https://www.globenewswire.com/news-release/2026/10/06/3375277/0/en/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-world-s-most-dangerous-jobs.html','Credo'),('fit','https://www.teraz.sk/najnovsie/fit-investicia-faktury-spracovanie/73190-clanok.html','zrealizoval investíciu'),('gforce','https://www.linkedin.com/posts/usegforce_yeast-climatevc-sustainableinvesting-activity-7197170252332318721-Swwl','latest investment'),('cb','https://www.cbim.sk/sk/ourportfolio','2023')]\nfor id,u,p in pages:\n r=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True,text=True)\n s=re.sub(r'<(script|
… [396 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 4.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"8ef31d\",\"wall_time_seconds\":3.8227154580000002,\"exit_code\":0,\"original_token_count\":1215,\"output\":\"air https://feedit.cz/2019/10/24/air-ventures-investuje-do-hitech-startupu-cross-network-intelligence-ktery-pomaha-budovat-efektivni-site-mobilnim-operatorum-ve-svete-i-u-nas/ 57691 0 se zaměřením na síťovou infrastrukturu získává fond Air Ventures 15% podíl. CNI tak od investorů získalo již více než milion euro. Cross Network Intelligence řeší správu a řízení dokumentace OSS procesů v telekomunikačních a inženýrských sítích. Svým produktem osl\\n\\nDATES ['s 24. 10. 2019 by FeedIT.cz / Tisk', '24. říjen 2019 – Investiční fond A', 'ku v roce 2014 získala první atrak', 'e, v roce 2019 byla jako jedna ze ']\\ncf https://tech.eu/2026/06/09/merchantee-secures-eur18m-for-european-marketplace-expansion/ 75800 0 ng. The round was led by Reflex Capital, with participation from Czech Founders VC and Lighthouse Ventures. The company plans to use the funding to accelerate product development, expand support for additional e-commerce marketplaces, and support its growth across Euro\\n\\nDATES ['it London 2026 --> NOTIFICATIONS S', 'it London 2026 --> Discover More A', 'it London 2026 --> Keep the pulse ', 'ets in Q1 2026 Funding dips, but f', 'c 09 June 2026 Share Facebook Twit', 'served. © 2026 ']\\n365 https://www.gaebler.com/VC-Funding-6AFD2FC7-
… [3505 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"BHM" "Carebot" investice 2024'},{q:'"Fond inovácií a technológií" investícia 2020 2021 2022'},{q:'"WageNow" "investíciu" "2023"'},{q:'"Minerva Humanoids" "Credo" "2026" news'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Správa o stave malého a stredného podnikania (https://new.sbagency.sk/wp-content/uploads/2026/02/sprava_o_stave_msp_v_sr_v_roku_2022_print.pdf)\nciteturn66search12 [wordlim: 200] Published: 6 months ago; bolo v kumulatívnom období (od marca 2018 do decembra 2022) podporených 9 MSP.152 ... nasledovné fondy: Fond inovácií a technológií, a. s., Slovenský Rozvojový Fond, a. s., Eterus ... V porovnaní s rokom 2021 bol objem schválených investícií v roku 2022 vyšší o 3 800 000\nspoločností) prostredníctvom špecializovanej dcérskej spoločnosti Národný holdingový fond, \ns. r. o. (do 20. 03. 2014 pod obchodným názvom Fond fondov, s. r. o.). Dlhodobým poslaním \nspoločnosti je usmerňovanie činnosti jednotlivých fondov tak, aby sa stimuloval rozvoj \nsektora MSP na celom území SR, zhodnocoval sa objem finančných prostriedkov \njednotlivých fondov a dosiahnuté zisky sa používali na realizáciu dlhodobého cieľa podpory \nMSP.  \nV roku 2022 boli prostredníctvom spoločnosti Národný holdingový spravované \nnasledovné fondy: Fond inovácií a technológií, a. s., Slovenský Rozvojový Fond, a. s., Eterus \nCapital, a. s..154 \nV sledovanom roku 2022 bola prostredníctvom vyššie uvedených spravovaných fondov \nschválená celková výška investícií v objeme 6 500 000 Eur155 (z Eterus Capital, a. s.). \nV porovnaní s rokom 2021 bol objem schválených investícií v roku 2022 vyšší o 3 8
… [22865 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"curl -LsS --max-time 20 https://www.slovca.sk/files/attachments/CVCA%20Report%202023%20final.pdf | pdftotext -layout - - | grep -A8 -B3 'CB Investment'","max_output_tokens":3000}));
text(await tools.web__run({search_query:[{q:'"CB Investment Management" "WeWell" investment'},{q:'"Carebot" "BHM" "August" 2025 investment'},{q:'"Minerva Humanoids" "Finsmes" 2026'},{q:'"G-Force" "HERLab" 2024 May investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 11374)\nTotal output lines: 784\n\n{\"chunk_id\":\"f01c13\",\"wall_time_seconds\":0.369770083,\"exit_code\":0,\"original_token_count\":2352,\"output\":\" Buyer                       Country        Company            Period    EV       Stake   Description                                                   Buyer                Country    Company              Period   EV       Stake   Description\\n                                                                         (mEUR)                                                                                                                                       (mEUR)\\n\\n Czech Founders VC, Slovakia                Devs               1 2024    0.5      n/a     Czech Founders VC, Slovakian Zero Gravity Capital, and        CB Investment        Slovakia   Seenode (ex-         2 2023   0.2      n/a     CB Investment Management has invested €0.2 million\\n                                                                                          angel investor Bob Lesko have invested over €0.5 million                                                                                     in Seenode (formerly known as ErlaServers), a robust\\n Zero Gravity Capital                                                                                                                     
… [36490 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Wewell" "1,25" "2023"'},{q:'"Vestberry" "2025" "CB Investment Management"'},{q:'"Carebot" "BHM" "srpna" "2025"'},{q:'"G-Force" "Raya Power" investment 2026 2025 funding'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "G-Force investor profile | Platvix (https://platvix.com/investors/firm/g-force)\nciteturn71search0 [wordlim: 200] Crawled: 2 weeks ago; G-Force is a pre/seed fund and investment program for mission-driven climate tech startups. ... 2026-09-02 usegforce.com Raya Power Modular, plug-and-play solar and battery pod that delivers backup power and bill…\n\n# G-Force\n\n2026-09-02usegforce.com\n\nPre-seed investorsClimate investors\n\nOverview\n\nWhat they do\n\nG-Force is a pre/seed fund and investment program for mission-driven climate tech startups. The G-Force Sustainability Seed Program is a collaboration between Founders Factory (Henry Lane Fox, Brent Hoberman CBE) and tech leaders: Boris Zeleny (AVG, later sold to AVAST for $1.4bn), Marian Gazdik (Startup Grind), and serial early-stage investors Peter Kulloi & Miklos Kobor.\n\nusegforce.com\n\nWhat they look for\n\nBacking early-stage startups contributing to energy, mobility, and industry transition with the potential for global scale.\n\nusegforce.com\n\nStage\n\nPre-seed, Seed\n\nusegforce.com\n\nSectors\n\nClimate, Deeptech, Food and agriculture, Mobility and logistics\n\nusegforce.com\n\nBased\n\nBratislava, SK\n\nusegforce.com\n\nSources\n\n2026-09-02usegforce.comWe're a pre-seed VC fund focused on Climate/Deep Tech startups.\n\n2026-09-02usegforce.comReach out to us-we'd love to hear from you!\n\n20
… [30621 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\npages=[('bhm','https://www.bhmgroup.eu/en/news/blog/bhm-group-in-2025-capital-that-withstands-economic-cycles','full capital'),('cb','https://www.linkedin.com/posts/wewellapp_exciting-news-from-wewell-wewell-has-activity-7138486649600053249-fdHZ','CB Investment'),('gforce','https://www.linkedin.com/posts/usegforce_yeast-climatevc-sustainableinvesting-activity-7197170252332318721-Swwl','datePublished'),('impulse','https://impulseventures.com/','Safetica'),('credo','https://www.credoventures.com/','Minerva'),('cf','https://www.startbase.com/news/merchantee-sammelt-18-millionen-euro-ein-und-automatisiert-den-marktplatzhandel-mit-ki/','Czech Founders')]\nfor id,u,p in pages:\n r=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True,text=True)\n if id=='gforce':s=r.stdout\n else:s=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r.stdout,flags=re.S|re.I);s=html.unescape(re.sub('<[^>]+>','',s));s=re.sub(r'\\s+',' ',s)\n g=subprocess.run(['grep','-oE','.{0,60}'+re.escape(p)+'.{0,300}'],input=s,capture_output=True,text=True)\n print(id,u,len(r.stdout),g.returncode,g.stdout[:1500]);print('DATES',
… [89 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"81d73a\",\"wall_time_seconds\":2.123051709,\"exit_code\":0,\"original_token_count\":308,\"output\":\"bhm https://www.bhmgroup.eu/en/news/blog/bhm-group-in-2025-capital-that-withstands-economic-cycles 29623 2 \\nDATES [' BHM group in 2025: Capital That Withstands Econ', 'S BHM group in 2025: Capital That Withstands Econ', 'Cycles 11. 12. 2025 In a year when the European e', 'rint. The year 2025 demonstrated that a strategy ', 'ding permit in 2025 and moved into the implementa']\\ncb https://www.linkedin.com/posts/wewellapp_exciting-news-from-wewell-wewell-has-activity-7138486649600053249-fdHZ 110366 2 \\nDATES ['ess LinkedIn © 2026 About Accessibility User Agre']\\ngforce https://www.linkedin.com/posts/usegforce_yeast-climatevc-sustainableinvesting-activity-7197170252332318721-Swwl 158919 2 \\nDATES ['center\\\">&copy; 2026</span>']\\nimpulse https://impulseventures.com/ 0 2 \\nDATES []\\ncredo https://www.credoventures.com/ 574506 2 \\nDATES ['9 KrakówPoland©2026 Credo Ventures. Contact(CV.)i', '9 KrakówPoland©2026 Credo Ventures. Contact(CV.)i', 'land16:39, CET©2026 Credo Ventures. Contact(CV.)i', 'land16:39, CET©2026 Credo Ventures. ']\\ncf https://www.startbase.com/news/merchantee-sammelt-18-millionen-euro-ein-und-automatisiert-den-marktplatzhandel-mit-ki/ 29075 2 \\nDATES ['Startbase GmbH 2026 Home Sitemap Geomap Privacy P']\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\npages=[('bhm','https://www.bhmgroup.eu/en/news/blog/bhm-group-in-2025-capital-that-withstands-economic-cycles','full capital'),('cb','https://www.linkedin.com/posts/wewellapp_exciting-news-from-wewell-wewell-has-activity-7138486649600053249-fdHZ','CB Investment'),('gforce','https://www.linkedin.com/posts/usegforce_yeast-climatevc-sustainableinvesting-activity-7197170252332318721-Swwl','datePublished|datetime|latest investment'),('impulse','https://therecursive.com/czech-safetica-secures-e3-8-investment-to-fuel-expansion-in-the-us/','funding comes'),('credo','https://www.globenewswire.com/news-release/2026/10/06/3375277/0/en/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-world-s-most-dangerous-jobs.html?print=1','Credo')]\nfor id,u,p in pages:\n r=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True,text=True)\n s=r.stdout if id=='gforce' else html.unescape(re.sub('<[^>]+>','',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r.stdout,flags=re.S|re.I)));s=re.sub(r'\\s+',' ',s)\n g=subprocess.run(['grep','-oE','.{0,50
… [149 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"c0d7a3\",\"wall_time_seconds\":1.8381462499999999,\"exit_code\":0,\"original_token_count\":781,\"output\":\"bhm https://www.bhmgroup.eu/en/news/blog/bhm-group-in-2025-capital-that-withstands-economic-cycles 29623 0 ostic equipment. Simultaneously, the group made a full capital entry into the Czech startup Carebot, which develops artificial intelligence algorithms for analyzing radiological images. Combining Reinsberg Group's hardware and manufacturing expertise with Carebo\\n\\ncb https://www.linkedin.com/posts/wewellapp_exciting-news-from-wewell-wewell-has-activity-7138486649600053249-fdHZ 110366 0 has secured an investment of €1.25 million led by CB Investment Management with participation from Zero One Hundred and Jakub Borovička, marking a significant… | Wewell LinkedIn respects your privacy LinkedIn and 3rd parties use essential and non-essential cookie\\nhas secured an investment of €1.25 million led by CB Investment Management with participation from Zero One Hundred and Jakub Borovička, marking a significant milestone in our mission to revolutionize skincare. This investment is a big boost for us, enabling the \\n\\ngforce https://www.linkedin.com/posts/usegforce_yeast-climatevc-sustainableinvesting-activity-7197170252332318721-Swwl 158917 0 ners with HERlab! 🌱 We're excited to announce our latest investment in HERLab, a pioneering sta
… [2136 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw3PNj4eXLN1oomlzMk5NMyc9IZqpL9alsHSDT9HrELX1vkjnKZEtDJ0y1GjDdUtboZJZlkmh61SBFn5QTF01qes2t5VnSybjGz-qu5qYJ3aCg65qquQX_be6boo4yCgLAfUvYNubvPhg5zKtzq-p4KBJFZq07XprlHq4gJubBB291a9Z9cV09SThXCW2ho78D_M2EwaG7XJPfHRq0Lr3nADxdHxyX9atcqzlI37Xh5iUlPxAwMWdMCgead_qRugJ1NuqUcMxdv_reFSXmlGvV1_6JnW_HOF8lfUDBLL9WAEJCv5QnjdpXN55N3UGIS3_bTgAB88DSSZt01SJBzaOOHpuhJ-gLA9F7lYbGB9ZJUM_RqlmhH-8fKT8uldoB5_0FKFtjpWJx9Rt7pAF9neMIGXSh7n586098bCGIbedQDs5FwD4NJFUg9de1GtGPVX5sYiFK8Jch_BAzT_nkUEOpmCOB1ClgPXfs7wLQxLTDyxpHT0S6ejydqjqa8_wx-VKyAZhTSQsDJJCD_pI7QxiATfG8Kx-Dc3JwgrPVNwEmrQxUUbX-_ElW6zMbbxY-6dWeuVYHa7u4kmGhhrOpQEG47ZxdJ9gabyzexMjl4d4tuHxxYjlFBnEIbghwgKQSLm94TkEgCHaSWaQSw9yuOmGW5yudEdLUnNFtgUcg46eA2JYDqypwWL-qVx2a_mN95YFS_xQ8UF3vuMR1uNeDvJHVd-LqoTP6dkPojYj9_11VOHtP50T7aeMPvaF37t8ot4XFCUa_J9x2nFkDfoIFNiNHBmIPudTpcm2Lgbl3niI70rG-PyNtmmUrFaqsL2GTJ6lHEa1D5U7DTVangCWDf91-rX06IlvouNWZDYirExpx_LtlarALLjyqj8I3X_6ZYLulRzfETPiRXucoRtRhCdNnTCabBkqPVJrJZrfsbgxwIax0Y="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Safetica" "4M" "Impulse" January 2025 press'},{q:'"Minerva Humanoids" "Credo" October 6 2026 funding -site:globenewswire.com -site:traded.co'}],response_length:"long"}));
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://therecursive.com/czech-safetica-secures-e3-8-investment-to-fuel-expansion-in-the-us/'\nr=subprocess.run(['curl','-LsS',u],capture_output=True,text=True).stdout\ns=html.unescape(re.sub('<[^>]+>','',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S|re.I)));s=re.sub(r'\\s+',' ',s)\ng=subprocess.run(['grep','-oE','.{0,100}(Impulse|24 January).{0,180}'],input=s,capture_output=True,text=True);print(g.returncode,g.stdout)\nu='https://www.linkedin.com/posts/wewellapp_exciting-news-from-wewell-wewell-has-activity-7138486649600053249-fdHZ'\nr=subprocess.run(['curl','-LsS',u],capture_output=True,text=True).stdout\nprint(subprocess.run(['grep','-oE','datePublished.{0,80}'],input=r,capture_output=True,text=True).stdout[:500])\nPY","max_output_tokens":3000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "Safetica Secures $4M Investment to Expand AI-Powered Security (https://safetica.com/resources/press/safetica-secures-4musd-investment-to-accelerate-u-s-expansion-ai-innovation)\nciteturn76search0 [wordlim: 200] Published: 1.6 years ago; Crawled: last month; # Safetica Secures $4M USD Investment to Accelerate U.S. ... San Jose, California — March 17, 2025 – Safetica, a global leader in Intelligent Data Security, has announced a $4 million USD investment to drive its U.S. expansion and enhance AI-powered data security solutions.The investment comes from existing investors, led by Ondřej Tomek (Impulse Capital) and Jakub Mahdal, founder of Safetica in 2007.\n\n# Safetica Secures $4M USD Investment to Accelerate U.S. Expansion & AI Innovation\n\nMar 17, 2025\n\nSan Jose, California — March 17, 2025 – Safetica, a global leader in Intelligent Data Security, has announced a $4 million USD investment to drive its U.S. expansion and enhance AI-powered data security solutions. The investment comes from existing investors, led by Ondřej Tomek (Impulse Capital) and Jakub Mahdal, founder of Safetica in 2007.\n\n \n\n> ”We’re excited to continue growing the business,” says Mirek Kren, CEO of Safetica, who has been spearheading the company’s international strategy since joining a year ago. “This investment is a key stepping stone on our journey to significantly increase 
… [31213 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\npages=[('credo','https://via.ritzau.dk/pressemeddelelse/15210014/minerva-humanoids?publisherId=90446','Credo Ventures'),('impulse','https://en.ain.ua/2025/01/24/safetica-announces-a-4m-investment/','Impulse Ventures'),('gforce','https://foundersfactory.com/articles/investing-in-brightly/','latest G-Force|datePublished|publishDate'),('fit','https://www.fondfit.sk/','2024|2023|invest|portf')]\nfor id,u,p in pages:\n raw=subprocess.run(['curl','-LsS','--max-time','20',u],capture_output=True,text=True).stdout\n s=raw if id=='gforce' else html.unescape(re.sub('<[^>]+>','',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',raw,flags=re.S|re.I)));s=re.sub(r'\\s+',' ',s)\n out=subprocess.run(['grep','-oE','.{0,90}('+p+').{0,200}'],input=s,capture_output=True,text=True).stdout\n print(id,u,len(raw),out[:2200])\nPY","max_output_tokens":5500}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 4.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"a964a4\",\"wall_time_seconds\":4.336811375,\"exit_code\":0,\"original_token_count\":914,\"output\":\"credo https://via.ritzau.dk/pressemeddelelse/15210014/minerva-humanoids?publisherId=90446 152087 y $10 million in pre-seed funding led by General Catalyst, with Long Journey Ventures and Credo Ventures as co-leads, and participation from MVP Ventures, Kaya, RunwayVC, Compound, Founders Embassy, Hugging Face, Codecademy, YG, Walter Ventures, Tiny Ventures, Chaotica, and Babylon. The round brings Min\\n and Sindelfingen, Germany, Minerva is backed by General Catalyst, Long Journey Ventures, Credo Ventures, and additional investors. Learn more at https://www.minervahumanoids.com/.Media ContactMollie Gonzalezminerva-humanoids@bulleitgroup.comA photo accompanying this announcement is available at https:/\\n\\nimpulse https://en.ain.ua/2025/01/24/safetica-announces-a-4m-investment/ 82339 eyword searches. Investment detailsCzech entrepreneur Ondrej Tomek, co-founder and CEO at Impulse Ventures, led the investment round. It was also joined by Jakub Mahdal, founder and former CEO of Safetica, and smaller investors Ondrej Smolář and Michael Poplar-Rostok. Fresh funds are intended to strengthe\\n\\ngforce https://foundersfactory.com/articles/investing-in-brightly/ 181474  5.16.1\\\"/><meta data-react-helmet=\\\"true\\\" name=\\\"description\\\" content=\\
… [2368 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw3svj_BgC7w-c-ZTB4h-6vuFp-_X4Di5h95to8HSt9QgqB_yGfMlyx21eEQNTxhFpz1fShCnbWMgWB9vYXXhF8JP1qE4DNawcMSWix9H_WxpHpg8TKuA2VhtdqTKSruMM-RgGZpDXzgiTbdAPLqN3MrhO78qH7avPfQ06FWKfFotRYxRV9yJ8mlI5xj354R4Ohh7fKISkbDW4y8xO0YEx6Fw3gAo_7h1DhUptuC1kpk173ZIstTc3FwlsCuqToomv_ottn8bdsEoTizhVT97pr8JjGMKjz7v6yDTfvGJSE1ANpCTrhPR8Z2GfDjf29On2x_EBp_dwbb-QgiFFoW3ZaTa4laTT08pjm91riqCcxjQpxXzKmdk_9BJJ4drYGL4oxmguxkFLboc-R88xSsrA3hk8Ul7jqVuoxvqqjxQd2Rrsp3F-j7_VlZJbXqKO-al9ARnce-pGeZX2QVLyoRgK32GENSbNODmF7Q7G4Fzp1pJyz-MgbMp0DSqmL5ejCK7yyg_QwYlAI_40n3YMRYxfuC9cdXbz8-VgbnervRxB843tmbBduPDmkthkZ-UAD88KJNbhjj6p_INIVt9R3gb1idGxcKt9uxjzi5T484o_ZeE5PIkJ7EnYizz_ta_SpyGfmlc0zGF394WeT4HZ5zR7yfP2XJzBOkCtkqNtWmH32X13U="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nfor u,p in [('https://foundersfactory.com/page-data/articles/investing-in-brightly/page-data.json','date|created|202'),('https://www.usegforce.com/','Raya|Canyon|blog|news'),('https://www.fondfit.sk/','supported|podporene|projekty')]:\n s=subprocess.run(['curl','-LsS','--max-time','15',u],capture_output=True,text=True).stdout\n print(u,len(s));print(subprocess.run(['grep','-oE','.{0,30}('+p+').{0,140}'],input=s,capture_output=True,text=True).stdout[:1500])\nPY","max_output_tokens":2500}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"24e28d\",\"wall_time_seconds\":2.56690275,\"exit_code\":0,\"original_token_count\":639,\"output\":\"https://foundersfactory.com/page-data/articles/investing-in-brightly/page-data.json 731294\\nname\\\\\\\":\\\\\\\"Founders Factory\\\\\\\",\\\\\\\"created_at\\\\\\\":\\\\\\\"2023-05-10T16:28:03.478Z\\\\\\\",\\\\\\\"published_at\\\\\\\":\\\\\\\"2024-04-15T13:25:59.344Z\\\\\\\",\\\\\\\"updated_at\\\\\\\":\\\\\\\"2024-04-15T13:25:59.383Z\\\\\\\",\\\\\\\"id\\\\\\\":30570598\\n/founders-factory\\\\\\\",\\\\\\\"sort_by_date\\\\\\\":null,\\\\\\\"position\\\\\\\":-2340,\\\\\\\"tag_list\\\\\\\":[],\\\\\\\"is_startpage\\\\\\\":false,\\\\\\\"parent_id\\\\\\\":305705617,\\\\\\\"meta_data\\\\\\\":null,\\\\\\\"group_id\\\\\\\":\\\\\\\"b3c887f7-5836-45\\n0f\\\\\\\",\\\\\\\"first_published_at\\\\\\\":\\\\\\\"2020-11-27T11:30:12.429Z\\\\\\\",\\\\\\\"release_id\\\\\\\":null,\\\\\\\"lang\\\\\\\":\\\\\\\"default\\\\\\\",\\\\\\\"path\\\\\\\":null,\\\\\\\"alternates\\\\\\\":[],\\\\\\\"default_full_slug\\\\\\\":null,\\\\\\\"translated_slu\\ntors\\\\\\\":[],\\\\\\\"publishedDate\\\\\\\":\\\\\\\"2025-01-09 00:00\\\\\\\",\\\\\\\"collaboratorsLabel\\\\\\\":\\\\\\\"In collaboration with\\\\\\\"},{\\\\\\\"_uid\\\\\\\":\\\\\\\"8adefcbe-d326-4d2f-b9c4-48a8804ce723\\\\\\\",\\\\\\\"richText\\\\\\\":{\\\\\\\"type\\\\\\\":\\nthe avoided methane emissions created by wasted food in
… [2294 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,json,re,html\nu='https://foundersfactory.com/page-data/articles/investing-in-brightly/page-data.json';s=subprocess.run(['curl','-LsS',u],capture_output=True,text=True).stdout\nj=json.loads(s)\ndef walk(o):\n if isinstance(o,dict):\n  for k,v in o.items():\n   if isinstance(v,str) and 'publishedDate' in v:\n    print(k,v[:900])\n   elif k in ('publishedDate','title','full_slug'):print(k,str(v)[:160])\n   if isinstance(v,(dict,list)):walk(v)\n elif isinstance(o,list):\n  for v in o:walk(v)\nwalk(j)\nu='https://foundersfactory.com/articles/investing-in-brightly/'\ns=subprocess.run(['curl','-LsS',u],capture_output=True,text=True).stdout;s=html.unescape(re.sub('<[^>]+>','',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',s,flags=re.S|re.I)));s=re.sub(r'\\s+',' ',s)\nprint(subprocess.run(['grep','-oE','.{0,10}We’re excited.{0,100}'],input=s,capture_output=True,text=True).stdout)\nPY","max_output_tokens":2200}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"8679e9\",\"wall_time_seconds\":0.286734084,\"exit_code\":0,\"original_token_count\":271,\"output\":\"full_slug articles/investing-in-brightly\\ncontent {\\\"_uid\\\":\\\"6417c98a-2019-4b7b-b7ad-67734b25a918\\\",\\\"body\\\":[{\\\"_uid\\\":\\\"ff7f4640-92b5-44df-88a5-eb47e24b535f\\\",\\\"Label\\\":\\\"Investments\\\",\\\"Title\\\":\\\"Investing in Brightly—carbon credits from food recovery\\\",\\\"Backdrop\\\":\\\"#12121280\\\",\\\"HeroImage\\\":\\\"//a.storyblok.com/f/229494/1280x849/ed7a9babda/brightly-food-waste.jpg\\\",\\\"LightText\\\":true,\\\"LogoImage\\\":\\\"\\\",\\\"component\\\":\\\"HeaderHeroImageSection\\\",\\\"HeroImageNew\\\":[{\\\"_uid\\\":\\\"bcfbd59a-1cfa-415c-a9c2-fa7b244bfd19\\\",\\\"image\\\":{\\\"id\\\":18945317,\\\"alt\\\":\\\"\\\",\\\"_uid\\\":\\\"f519e937-8c20-45ad-b85a-b5a2599e359e\\\",\\\"name\\\":\\\"\\\",\\\"focus\\\":\\\"\\\",\\\"title\\\":\\\"\\\",\\\"source\\\":\\\"\\\",\\\"filename\\\":\\\"https://a.storyblok.com/f/229494/1280x849/ed7a9babda/brightly-food-waste.jpg\\\",\\\"copyright\\\":\\\"\\\",\\\"fieldtype\\\":\\\"asset\\\",\\\"meta_data\\\":{},\\\"is_external_url\\\":false},\\\"noBlur\\\":false,\\\"minSize\\\":\\\"400x175\\\",\\\"component\\\":\\\"Image\\\",\\\"mobileImage\\\":{\\\"id\\\":18945317,\\\"alt\\\":\\\"\\\",\\\"name\\\":\\\"\\\",\\\"focus\\\":\\\"\\\",\\\"title\\\":\\\"\\\",\\\"source\\\":\\\"\\\"
… [194 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw4MhT9GyV6VlK3g-6YlYvWNQcyJOqiaagaBSVbedEcMAXJbT79fPqiE4b62l5t0czZmI9Fi-K5iEWmnxhy3oFB0tvFAZG8prVFskE8vkkNw-y47KIEzJ8ufI06O1NoPkKg-cpvWSqubiIvY5sPjAsPjvloUcp-XSUJppO8Lzd8JNiXVf_wPEE27SIvkmPGoWFULRr-LyBITnoiEB4_XWAtM-0ohsJtIDkBOBj2KNNL-7AJKqElggM_dcaQRPfTUpRBzm_-Hk2rUSkb2oAGmBLOOK3g15XwqZSY7qF5nnPaCuEWaz9tE8PVeoDpH-ErhMvUu5fJ9GTzQ4pjO_LZBDUA9ple_xLapGbHKvi4H4EsK53MFnd1jpHU_Zo-LrBCBBj6BLiOVtiyYFQeDRNF2620LW6w8OzKG_i1DVkIkGmGG7pAVQdOiYweFUwOJIqg4Ee7u1WNAkPA0EJggvZ6Cv-6Tm-spXY6cE0od47F3JIv5rwir9VzPcspa9_1mKHx-m_NgA_--TZG7DcuRbGzt7dH961fjMDtsgMHi2hnNiND9EaM2tJjsnkayCk4OudlxvEotKvSpCBOQYnL8D-F8WvGUMRYtaas2EGhMkBCNQzUj_VS7T0LXsu5eHo4wFBdNeJKBUsdxtlMU5mYow9BEU1akwVr-gR4HGuK1z7a8Hexkhnxfxd9DPxwBJltD0qhJHlTLKbOWOtcNxVYgA8eNOpSyqLkP2QMSAy8nFoeMz3nOal3Bz7SMNCD63MQpHRaX7acm6gC-DDFsvQrW-yUC-EtQmXNHwcz6z4UuenKYPgcp5iE="}
```

<details><summary>result</summary>

```

```
</details>

**Codex:**

[redacted: name]
```json
[
  {
    "id": "365-fintech",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Ctrl Alt",
      "date": "2023-10-26",
      "date_precision": "day",
      "url": "https://www.gaebler.com/VC-Funding-6AFD2FC7-C9AF-4DA6-AC47-2B1240324F7C-Ctrl-Alt-10-26-2023",
      "quote": "Forward Partners, MiddleGame Ventures and 365.fintech participated in a $2.6 million capital raise for Ctrl Alt."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Bratislava-based firm makes seed equity investments, and the latest verified transaction is the Ctrl Alt funding announcement in October 2023."
  },
  {
    "id": "air-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Cross Network Intelligence",
      "date": "2019-10-24",
      "date_precision": "day",
      "url": "https://feedit.cz/2019/10/24/air-ventures-investuje-do-hitech-startupu-cross-network-intelligence-ktery-pomaha-budovat-efektivni-site-mobilnim-operatorum-ve-svete-i-u-nas/",
      "quote": "Ve startupu se zaměřením na síťovou infrastrukturu získává fond Air Ventures 15% podíl."
    },
    "active_36m": "no",
    "confidence": "medium",
    "note": "The official site identifies a Prague-based VC, but recent Jiant funding records appear to conflate it with an American namesake and no newer independently verified investment was found."
  },
  {
    "id": "baryon-fund",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Airlogix",
      "date": "2026-07-21",
      "date_precision": "day",
      "url": "https://scroll.media/2026/07/21/baryon-fund-airlogix/",
      "quote": "Інвестиційний фонд Baryon Fund повідомив, що український defence-tech стартап Airlogix входить до його портфеля."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The Slovak founding investment team backs defence startups, while Luxembourg is the fund domicile and the Airlogix announcement does not disclose the transaction closing date."
  },
  {
    "id": "bhm-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Carebot",
      "date": "2025-01-01",
      "date_precision": "year",
      "url": "https://www.bhmgroup.eu/en/news/blog/bhm-group-in-2025-capital-that-withstands-economic-cycles",
      "quote": "Simultaneously, the group made a full capital entry into the Czech startup Carebot"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "BHM's Czech venture arm holds startup equity, and the group's official 2025 review confirms a Carebot capital investment without specifying its exact closing date."
  },
  {
    "id": "cb-investment-management",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Wewell",
      "date": "2023-12-07",
      "date_precision": "day",
      "url": "https://www.linkedin.com/posts/wewellapp_exciting-news-from-wewell-wewell-has-activity-7138486649600053249-fdHZ",
      "quote": "Wewell has secured an investment of €1.25 million led by CB Investment Management"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The Bratislava manager invests through CB Growth One, and Wewell's dated December 2023 announcement verifies activity although newer databases sometimes misattribute portfolio companies' subsequent rounds."
  },
  {
    "id": "credo-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Minerva Humanoids",
      "date": "2026-10-06",
      "date_precision": "day",
      "url": "https://via.ritzau.dk/pressemeddelelse/15210014/minerva-humanoids?publisherId=90446",
      "quote": "with Long Journey Ventures and Credo Ventures as co-leads"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "Credo is an early-stage VC managed from Prague with a Krakow office, and the October 2026 company press release confirms its co-led Minerva pre-seed investment."
  },
  {
    "id": "cs-seed-starter",
    "is_investor": "yes",
    "type": "cvc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Definic",
      "date": "2026-06-18",
      "date_precision": "day",
      "url": "https://www.sih.sk/en/aktuality/sih-podporil-definic-slovensku-technologicku-spolocnost-s-globalnymi-ambiciami",
      "quote": "ČS Seed Starter (Česká sporiteľňa), participated in a €2.5 million investment round in the technology company Definic."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "Česká spořitelna's Prague-based corporate venture subsidiary makes startup equity investments, and SIH's June 2026 announcement explicitly names its participation in Definic."
  },
  {
    "id": "czech-founders-vc",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Merchantee",
      "date": "2026-06-09",
      "date_precision": "day",
      "url": "https://tech.eu/2026/06/09/merchantee-secures-eur18m-for-european-marketplace-expansion/",
      "quote": "The round was led by Reflex Capital, with participation from Czech Founders VC and Lighthouse Ventures."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Prague-based founder-backed fund advertises pre-seed equity tickets and participated in Merchantee's June 2026 financing."
  },
  {
    "id": "depo-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "ArcSpace",
      "date": "2026-08-01",
      "date_precision": "month",
      "url": "https://spacebandits.io/startups/arcspace",
      "quote": "A €2 million seed round closed in August 2026, led by the Czech fund DEPO Ventures"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "DEPO manages Czech early-stage investment funds alongside its angel network, and ArcSpace's reported August 2026 seed is the newest verified deal."
  },
  {
    "id": "fond-inovacii-a-technologii",
    "is_investor": "yes",
    "type": "public_dfi",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Datamolino",
      "date": "2014-02-08",
      "date_precision": "day",
      "url": "https://www.teraz.sk/najnovsie/fit-investicia-faktury-spracovanie/73190-clanok.html",
      "quote": "Fond inovácií a technológií (FIT) zrealizoval investíciu do slovenského start-up projektu Datamolino."
    },
    "active_36m": "no",
    "confidence": "medium",
    "note": "The state-backed Slovak risk-capital fund entered its post-investment phase in 2025, and newer aggregate investment statistics did not identify a dated company transaction beyond Datamolino."
  },
  {
    "id": "g-force",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Brightly",
      "date": "2025-01-09",
      "date_precision": "day",
      "url": "https://foundersfactory.com/articles/investing-in-brightly/",
      "quote": "We’re excited to announce our latest G-Force Climate investment—Brightly."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "G-Force's Slovak registered manager offers cash for minority equity with a Bratislava–London team, and Brightly's January 2025 article is dated in its published page data while newer holdings are undated."
  },
  {
    "id": "gain-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Carebot",
      "date": "2026-08-03",
      "date_precision": "day",
      "url": "https://www.carebot.com/news/carebot-closes-the-largest-investment-round-in-its-history",
      "quote": "with JIC Ventures joining the company alongside existing investors Gain Ventures and Eva Janečková."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "Czech registry records connect Prague-managed GAIN Ventures s.r.o. to Carebot's equity ownership, corroborating the August 2026 announcement despite erroneous California attribution in some databases."
  },
  {
    "id": "ii-biotech-fund",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Ternary Therapeutics",
      "date": "2026-03-17",
      "date_precision": "day",
      "url": "https://itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues",
      "quote": "with participation from Pace Ventures, the i&i Biotech Fund and the UK Innovation & Science Seed Fund"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Luxembourg-domiciled life-science VC has its investment team in Prague and participated in Ternary's March 2026 seed financing."
  },
  {
    "id": "impulse-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Safetica",
      "date": "2025-01-24",
      "date_precision": "day",
      "url": "https://en.ain.ua/2025/01/24/safetica-announces-a-4m-investment/",
      "quote": "Czech entrepreneur Ondrej Tomek, co-founder and CEO at Impulse Ventures, led the investment round."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Prague-based venture investor deploys its own capital, and Safetica's January 2025 financing is the newest verified investment rather than its later Taikun exit."
  },
  {
    "id": "inven-capital",
    "is_investor": "yes",
    "type": "cvc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Wint",
      "date": "2026-09-09",
      "date_precision": "day",
      "url": "https://www.prnewswire.com/news-releases/wint-raises-36-million-in-series-d-funding-to-scale-ai-powered-water-intelligence-globally-302873443.html",
      "quote": "Series D funding co-led by LIP Ventures and Inven Capital."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "ČEZ's Prague-based venture investment manager co-led Wint's $36 million Series D announced in September 2026."
  }
]
```

Отдельный отчёт для родительского агента: 80 поисковых запросов; все 15 приведённых цитат проверены настоящими curl-загрузками и grep. Brightly: дата проверена в `https://foundersfactory.com/page-data/articles/investing-in-brightly/page-data.json`, поле `publishedDate` соответствующей статьи — `2025-01-09 00:00`. Ничего не записывал и другие файлы репозитория не читал. Для GAIN и BHM классификация vc содержит интерпретацию инвестиционного профиля; для FIT `no` означает отсутствие найденной именованной сделки после порога, при этом официальная статистика подтверждает более поздние неназванные инвестиции.

## Thread `2026-10-11T06-13-26`

**Brief / message:**

You are an independent fact-checker. Work in /Users/[redacted]/homeW/ai-dev-test/investor-db, but read ONLY the file eval/second-opinion/input.json (a list of organisations: id, name, country, website). Do NOT open any other file in the repo (no data/, research/, PLAN.md) — your answers must be independent of an earlier assessment.

For each organisation answer, from public web sources you check yourself (use web search and curl):
1. is_investor: "yes" / "no" / "unclear" — does it invest its own or managed capital as equity (or convertible) into private companies, as a core activity? (Crowdfunding platforms, advisers, banks' lending, grant programs = "no".)
2. type: one of vc, pe, cvc, family_office, angel, private_investor, accelerator, fund_of_funds, public_dfi, platform, adviser, other.
3. managed_from: ISO country of the team/manager that makes the investment decisions.
4. latest_investment: the most recent DATED investment you can find: {company, date (YYYY-MM-DD, or YYYY-MM-01 / YYYY-01-01 if only month/year known), date_precision: day|month|year, url, quote}. The quote must be copied verbatim from the raw page text (fetch it with curl and check with grep) — not from a search snippet or a summary. If you can't find any, null.
5. active_36m: "yes" if latest_investment.date >= 2023-10-11, "no" if older, "unclear" if none found.
6. confidence: high / medium / low, and a one-sentence note.

Budget: about 6 searches per organisation; don't get stuck. Write the result to eval/second-opinion/codex.json as a JSON array (same order, include id). Write nothing else, run no git commands, don't mention tools or AI in the file. Print a 5-line English summary at the end (counts per is_investor and active_36m).

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport json\np=json.load(open('eval/second-opinion/input.json'))\nprint(json.dumps(p[15:30],indent=2))\nPY","max_output_tokens":4000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"53b594\",\"wall_time_seconds\":0.000002708,\"exit_code\":0,\"original_token_count\":445,\"output\":\"[\\n  {\\n    \\\"id\\\": \\\"ipm-group\\\",\\n    \\\"name\\\": \\\"IPM Group\\\",\\n    \\\"country\\\": \\\"GB\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"jt-ventures\\\",\\n    \\\"name\\\": \\\"J&T Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.jtventures.cz/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"kaya-vc\\\",\\n    \\\"name\\\": \\\"KAYA VC\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.kaya.vc/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"koopeo-ventures\\\",\\n    \\\"name\\\": \\\"KOOPEO Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"lighthouse-ventures\\\",\\n    \\\"name\\\": \\\"Lighthouse Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://lhv.vc/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"limerock\\\",\\n    \\\"name\\\": \\\"Limerock\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"lrj-capital\\\",\\n    \\\"name\\\": \\\"LRJ Capital\\\",\\n    \\\"country\\\": null,\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"miton\\\",\\n    \\\"name\\\": \\\"Miton\\\",\\n    \\\"country\\\":
… [1384 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'IPM Group latest investment 2026 2025 Slovakia'},{q:'J&T Ventures investment 2026 2025'},{q:'KAYA VC investment 2026 2025'},{q:'KOOPEO Ventures investment 2025 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Kaya VC Portfolio Investments, Kaya VC Funds, Kaya VC Exits (https://www.cbinsights.com/investor/enern)\nciteturn0search0 [wordlim: 200] Crawled: today; ## Latest Kaya VC News ... Their latest investment was in Pencil as part of their Seed VC on June 17, 2026. ... 5/19/2026  | Series A  | Viktor  | $75M  | Yes  | Accel, Alex Bouaziz, Bek Ventures, Cal Henderson, Charlie Songhurst, Daniel Gross, Guillermo Rauch, Harry Stebbings, Inovo, Jack Zhang, Joel Hellermark, Jorn van Dijk, Koen Bok, Lenny Rachitsky, Leonis Capital, Mati Staniszewski, Max Mullen, Nat Friedman, Nico Rosberg, SBS Seed Fund, Shaan Puri, Stewart Butterfield, Tenacity Ventures, Undisclosed Angel Investors, and Victor Riparbelli  | 4\n## Kaya VC Investments\n\n93 Investments\n\nKaya VC has made 93 investments. Their latest investment was in Pencil as part of their Seed VC on June 17, 2026.\n\nImage: CBI Logo\n\n### Kaya VC Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n6/17/2026  | Seed VC  | Pencil  | $7.4M  | Yes  | A16z Speedrun, and Amplify Partners  | 2\n5/19/2026  | Series A  | Viktor  | $75M  | Yes  | Accel, Alex Bouaziz, Bek Ventures, Cal Henderson, Charlie Songhurst, Daniel Gross, Guillermo Rauch, Harry Stebbings, Inovo, Jack Zhang,
… [29255 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"KOOPEO Ventures" investment'},{q:'"IPM Group" investment InoBat funding'},{q:'"Lighthouse Ventures" investment 2026 2025'},{q:'"Limerock" investment Slovakia venture'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "IPM Group and InoBat invest in Wildcat Discovery Technologies together with Flint Hills Resources to disrupt the auto batteries industry in Europe | IPM (https://www.ipmgrp.com/ipm-group-and-inobat-invest-in-wildcat-discovery-technologies-together-with-flint-hills-resources-to-disrupt-the-auto-batteries-industry-in-europe/)\nciteturn3search0 [wordlim: 200] Published: 7.0 years ago; Crawled: last week; Bratislava, Slovakia / San Diego, California (16/10/2019) – IPM Group, in consortium with its portfolio company InoBat and Flint Hills Resources, subsidiary of Koch Industries, invest USD20m Series C financing into Wildcat Discovery Technologies, a global leader in lithium-ion battery research and development. ... Following up on the strategic alliance agreement signed in July this year, IPM Group in consortium with InoBat invested in Wildcat via its newly established investment vehicle, the IPM InoBat Fund, to facilitate the further development of the company’s unique High Throughput Platform, while securing InoBat Auto, a joint venture between Wildcat and InoBat, with regional exclusivity.\n\n# IPM Group and InoBat invest in Wildcat Discovery Technologies together with Flint Hills Resources to disrupt the auto batteries industry in Europe\n\n15th October 2019\n\nThe investment marks an important milestone for the InoBat Auto project, laying the ground for t
… [31565 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"LRJ Capital" investment latest'},{q:'"Miton" investment 2026 2025'},{q:'"Monogram Ventures" investment'},{q:'"Nation 1" investment 2026 2025'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "mitonC Portfolio Investments, mitonC Funds, mitonC Exits (https://www.cbinsights.com/investor/mitonc)\nciteturn6search0 [wordlim: 200] Crawled: last week; Filip Široký (MitonC) o kryptu v 2026: Co je signál a co jen šum? ... Their latest investment was in Legend Trade as part of their Pre-Seed on October 15, 2025. ... 10/15/2025  | Pre-Seed  | Legend Trade  | $1.5M  | Yes  | Big Brain Holdings, Bodhi Ventures, Figment Capital, Global Token Exchange, Kosmos Ventures, Miton, and Undisclosed Investors  | 4\n## mitonC Investments\n\n14 Investments\n\nmitonC has made 14 investments. Their latest investment was in Legend Trade as part of their Pre-Seed on October 15, 2025.\n\nImage: CBI Logo\n\n### mitonC Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n10/15/2025  | Pre-Seed  | Legend Trade  | $1.5M  | Yes  | Big Brain Holdings, Bodhi Ventures, Figment Capital, Global Token Exchange, Kosmos Ventures, Miton, and Undisclosed Investors  | 4\n12/30/2024  | Seed VC  | Accountable  | $2.3M  | Yes  | CMCC Global, Darius Rugys, DCbuilder, M11 Group, Moonhill Capital, and Zee Prime Capital  | 4\n12/20/2024  | Pre-Seed  | Valhalla  | $1.5M  | Yes  | Big Brain Holdings, Calvin Liu, Goncalo Sa, GSR Markets, Hash3, Igor Igamb
… [28839 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"LRJ Capital" venture investment Slovakia'},{q:'"Monogram Ventures" Slovakia investor'},{q:'"Neulogy Ventures" investment latest'},{q:'"Orbit Capital" investment 2026 2025'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "x \nAnalýza prístupu MSP, \nvrátane startupov, k \nmo (https://www.economy.gov.sk/uploads/files/bP0AA1XL.pdf)\nciteturn9search11 [wordlim: 200] Published: 1.7 years ago; LRJ Capital investuje do startupových ... Zisky z investícií LRJ Capital venuje na podporu neziskových organizácií.\n1.5. G4 Investments39 \nSpoločnosť poskytujúca primárne investičné a transakčné poradenstvo a tiež služby \nspojené s hľadaním a správou investícií. G4 Investments združuje úzky okruh investorov zo \nSlovenska a Českej republiky. V súčasnosti svojim klientom spravuje investície v 30 \nprojektoch v hodnote 30 miliónov eur. V rámci svojho podnikania sa sústredí aj na \nposkytovanie pôžičiek, financovanie realitných a developerských projektov a investície do \nstartupov. Jednotlivé investície sa pohybujú v rozmedzí od 200-tisíc eur až do 2 miliónov eur, \npričom majú zvyčajne formu kombinácie vstupu do základného imania spoločnosti, pôžičiek \na projektového financovania. \n \n1.6. LRJ Capital40 \nJe združením súkromných investorov, ktoré podporuje startupový ekosystém na \nSlovensku a v regióne strednej a východnej Európy. LRJ Capital investuje do startupových \nprojektov s vysokým potenciálom rastu, ideálne vo fáze, kedy už majú svoj produkt či službu \nhotový a overený prvými zákazníkmi. Typická výška investície sa pohybuje od 100-tisíc eur \ndo 2 miliónov eur. Zisky z inves
… [27516 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Presto Ventures" investment 2026'},{q:'"Purple Ventures" investment 2026'},{q:'"Reflex Capital" investment 2026'},{q:'"Lighthouse Ventures" Czech investment latest 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "News & Events | Lighthouse Ventures (https://lhv.vc/news-and-events/page/2/)\nciteturn13search0 [wordlim: 200] Crawled: today; As […] 24 June 2026 post Czech News Lighthouse Investment World news Lighthouse Ventures Backs Merchantee in €1.8M Funding Round We are thrilled to announce our investment in Merchantee as part of […] 10 June 2026 post Lighthouse Investment World news Lighthouse Ventures Backs BeatPulse Labs in $1.8M Pre-Seed Round We are thrilled to announce our investment in BeatPulse Labs as part […] 9 June 2026 post Czech News Lighthouse Investment Portfolio News: FaceUp Secures $5 Million Series A to Transform Corporate Compliance We are absolutely thrilled to share that our portfolio company, FaceUp, has […] 21 May 2026 post Czech News OPPORTUNITIES Celebrating Entrepreneurship: LHV joins the Jury at the Sweet & Salty Grand Finale Our partner, Robert Reich, had the pleasure of joining the jury at […] 19 May 2026 post Czech News Lighthouse Investment BIG NEWS: Edmund successfully raises €2.5 million to expand its platform We’re proud to share that Edmund, one of our portfolio companies, has successfully […] 12 April 2026 post Czech News Lighthouse Investment Uncategorized Backed by Us, Recommended by ChatGPT: Spaceti Secures Landmark Contract with NVIDIA!\n\n## Our news and events\n\n  * Show\n  * All\n  * News\n  * Events\n\npost Czech News W
… [32994 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re\nfrom bs4 import BeautifulSoup\nurls=['https://www.ipmgrp.com/news/','https://www.jtventures.cz/','https://www.koopeoventures.com/','https://lhv.vc/news-and-events/','https://www.miton.cz/en/blog/what-happened-fall-winter-2025/','https://n1.rocks/','https://www.neulogy.vc/','https://www.prestoventures.com/news','https://www.purple-ventures.com/']\nfor u in urls:\n r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\n s=BeautifulSoup(r,'html.parser')\n print('\\nURL',u,'LEN',len(r))\n print(s.get_text(' ',strip=True)[:12000])\n print('LINKS',[(a.get_text(' ',strip=True)[:80],a.get('href')) for a in s.find_all('a') if any(x in a.get_text().lower() for x in ['invest','2026','pange','ace','merchan','news','beat','2025'])][:30])\nPY","max_output_tokens":17000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"76a3b3\",\"wall_time_seconds\":0.000003458,\"exit_code\":1,\"original_token_count\":29,\"output\":\"Traceback (most recent call last):\\n  File \\\"<stdin>\\\", line 2, in <module>\\nModuleNotFoundError: No module named 'bs4'\\n\"}"}]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=['https://www.ipmgrp.com/news/','https://www.jtventures.cz/','https://www.koopeoventures.com/','https://lhv.vc/news-and-events/','https://www.miton.cz/en/blog/what-happened-fall-winter-2025/','https://n1.rocks/','https://www.neulogy.vc/','https://www.prestoventures.com/news','https://www.purple-ventures.com/']\ndef f(u):\n r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\n r=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S)\n t=html.unescape(re.sub('<[^>]+>',' ',r));t=re.sub(r'\\s+',' ',t)\n links=re.findall(r'<a\\b[^>]*href=[\\\"\\']([^\\\"\\']+)[\\\"\\'][^>]*>(.*?)</a>',r,re.S)\n return u,len(r),t[:12000],[(a,html.unescape(re.sub('<[^>]+>',' ',b)).strip()[:100]) for a,b in links if any(x in b.lower() for x in ['invest','2026','pange','ace','merchan','news','beat','2025'])][:30]\nfor x in concurrent.futures.ThreadPoolExecutor().map(f,urls):print(x)\nPY","max_output_tokens":17000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 14675)\nTotal output lines: 1\n\n{\"chunk_id\":\"dd0d3b\",\"wall_time_seconds\":1.604036209,\"exit_code\":0,\"original_token_count\":14558,\"output\":\"('https://www.ipmgrp.com/news/', 134836, ' --> News | IPM About us Investments Team Contact × About us Investments Team Contact Newsroom Please see below for all the latest news from IPM. Read more All IPM in the Media All Media IPM Portfolio Press releases Videos 14th June 2022 IPM Group invests in micromobility company Hilo EV 13th June 2022 PALMER AUTOMOTIVE Ltd. joins IPM GROUP to support the development of IPM’s sustainability investment arm 7th December 2021 Photoneo transforms e-commerce order fulfillment, raising a $ 21 million Series B funding 1st December 2021 Wuxi Lead and InoBat Auto partner to provide a turnkey solution for the production of lithium-ion batteries in Europe 16th November 2021 Rio Tinto invests in InoBat 11th October 2021 Our First IPO - ESS Inc. and ACON S2 Acquisition Corp. Announce Closing of Business Combination 25th May 2021 Rio Tinto partners with InoBat to explore innovative lithium battery initiative 7th May 2021 ESS Inc., a Long-Duration Energy Storage Solutions Company, to Become a Publicly Listed Company through Merger with ACON S2 Acquisition Corp. 27th April 2021 InoBat signs first commercial vehicle partnership with lead
… [38813 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"KOOPEO" investment 2025 2026 Kardi'},{q:'"Limerock" investment "2016"'},{q:'"IPM Group" "2025" Brightpick investment'},{q:'"J&T Ventures" Wultra "2026"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "RAPORT SPECJALNY (https://serwis-uslugirozwojowe.parp.gov.pl/storage/publications/pdf/cee_summit_pl_web_31.03_update.pdf)\nciteturn19search12 [wordlim: 200] Published: 7 months ago; Top 10 funduszy VC wg wartości inwestycji w latach 2015-2016 na Węgrzech ... Joint Polish Investment Fund (Hungary) ... Limerock Fund Manager (Slovakia)\nTop 10 funduszy VC wg wartości inwestycji w latach 2015-2016 na Węgrzech\n120 000 000 pln\nPrimus Capital (Hungary)\n91 721 667 pln\nBuran Venture Capital (Hungary)\nSzechenyl Venture Capital Fund (Hungary)\n57 428 000 pln\n6 752 500 pln\nConor Seed Capital Fund (Hungary)\nVenture FIZ  (Hungary)\n6 450 000 pln\n6 192 000 pln\nExperior Venture Fund (Hungary)\nEmem (Hungary)\n4 900 000  pln\n2 570 000 pln\nVew Europe Ventures (Hungary)\nJoint Polish Investment Fund (Hungary)\n2 240 000 pln\nInovo Venture Fund (Hungary)\n1 000 000 pln\n2015\n2016\nTop 10 funduszy VC wg wartości inwestycji w latach 2015-2016 na Słowacji\n27 984 000\nNeulogy Venture (Slovakia)\n6 450 000\nLRJ Capital (Slovakia)\nLimerock Fund Manager (Slovakia)\n1 290 000\nLauncher (Slovakia)\n645 000\n2015\n2016\n54--------------------------------------------------------------------------------\nSFDR | Limerock Investment Holding / JEREMIE Co-Investment Fund (https://www.limerock.sk/sfdr)\nciteturn19search0 [wordlim: 200] Crawled: 4 months ago; ### ​This disclo
… [25620 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"KOOPEO" "Kardi" investment funding'},{q:'"LRJ" "Finax" "2021" investment'},{q:'"Monogram Ventures" investment Streamstar date'},{q:'"N1" "2026" investment site:n1.rocks'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "KOOPEO Ventures (https://www.koopeoventures.com/)\nciteturn22search0 [wordlim: 200] Crawled: last week; Kardi AI ... #### KOOPEO Ventures SE\n\n# Home\n\n  * Image: nahled_video\n\n### Investujeme do inovativních firem\n\n## Naše portfolio\n\n###### O nás\n\n## Benefity investice s Vámi\n\n##### Hledáme příležitosti zejména v začínajících projektech s vysokým potenciálem růstu tržeb a hodnoty společnosti, investujeme do projektů s globálním potenciálem.\n\n###### Naše strategie\n\n## Uplatňujeme potenciál výjimečných lidí s velkým odhodláním.\n\nImage: shutterstock_125230634\n\n###### Naše vize\n\n## Stát se globálním lídrem v počtu úspěšných projektů.\n\nImage: shutterstock_381129667\n\n###### Náš přístup\n\n## Preferujeme konzultativní přístup a zapojování synergií v prodejních a marketingových kanálech, v kontaktech a vztazích.\n\n###### Portfolio\n\n### Portfolio investovaných projektů\n\nAIffinity\n\nLocalazy\n\nKardi AI\n\nSenzoor\n\nRealpad\n\nAgdata\n\nPrecismo\n\nKeyguru\n\nVšechny naše projekty\n\n###### Tým\n\n### Poznejte náš tým\n\n## Petr Špaček\n\n## Libor Daněk\n\n## Vladimír Šťastný\n\n#### Praha\n\nČerná Labuť\nNa Poříčí 25\n110 00 Praha 1\n\n#### Bratislava\n\nSeberíniho 482/1\n821 04 Bratislava\n\n#### Brno\n\nSolniční 243/17\n602 00 Brno\n\n#### KOOPEO Ventures SE\n\nSolniční 243/17\n602 00 Brno\nIČ: 05269113\n\nvedená pod H 564 u Kraj
… [23938 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=['https://n1.rocks/','https://www.neulogy.vc/news/','https://www.miton.cz/en/blog/','https://www.jtventures.cz/blog','https://orbitcapital.com/']\ndef f(u):\n r=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout\n r=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S)\n t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',r)))\n print(u, t[:9000])\n print('LINKS',[(a,html.unescape(re.sub('<[^>]+>',' ',b)).strip()[:80]) for a,b in re.findall(r'<a\\b[^>]*href=[\\\"\\']([^\\\"\\']+)[\\\"\\'][^>]*>(.*?)</a>',r,re.S) if any(x in b.lower() for x in ['invest','2026','2025','news','ace','seed'])][:20])\nlist(concurrent.futures.ThreadPoolExecutor().map(f,urls))\nPY","max_output_tokens":10000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"9755f5\",\"wall_time_seconds\":1.515038042,\"exit_code\":0,\"original_token_count\":6443,\"output\":\"https://www.jtventures.cz/blog  Blog - J&T Ventures Náš přístup Portfolio Tým Blog Kontakt EN English Náš přístup Portfolio Tým Blog Kontakt J&T Ventures, budova J&T Banka Sokolovská 700/113a ( 5. patro ) Praha 8 – Karlín, 186 00 Pošlete pitch deck Blog Portfolio novinky, rozhovory s foundery, komentáře z VC trhu 20/4/2025 Design to code se po letech snění stává skutečností, říká zakladatel Supernovy V jednu chvíli týmu zbývaly jen týdny života, nyní ohlašuje Series A v řádu stovek milionů korun a oznamuje nový produkt, který je naplněním mnohaletého snu. Dlouhou cestu z Ostravy ke kancelářím v Silicon Valley a investorům z Taiwanu popisuje v rozhovoru zakladatel startupu Supernova Jiří Třečák. Napsal 20/4/2025 grid.online přináší lépe zaplacené kurýry, levnější dopravu i méně aut ve městech, říká Ondřej Krátký Zakladatel taxi aplikace Liftago Ondřej Krátký založil spin-off startup grid.online, který v reálném čase propojuje kapacity dopravců s poptávkou logistických a e-commerce společností. Vydělávají na tom obě strany a tým již získal investici 1,5 milionu eur od fondů Reflex Capital, J&T Ventures a Grid Invest. Ondřej Krátký v rozhovoru vysvětluje, jak se rozhodl změnit 100 let starý byznys a jak z logistiky dělá spotový trh. Napsal 3/3/20
… [24131 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Neulogy" "GA Drilling" "2025" funding'},{q:'"KAYA" "Pencil" "2026" funding'},{q:'"N1" "investment" "June 2026"'},{q:'"Purple Ventures" "Fether" funding'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "Proudly announcing a new investment: Fether Labs!🖤 We’re excited to invest €450k in Fether Labs, a deeptech startup founded by researchers from Imperial College London. Fether Labs is developing… | Purple Ventures (https://www.linkedin.com/posts/purple-ventures_proudly-announcing-a-new-investment-fether-activity-7468258551694811136-QtM3)\nciteturn29search0 [wordlim: 200] Crawled: last week; The new funding will help the team launch its first developer kit, expand pilot projects, and move the technology closer to commercial deployment. ... Congrats Fether Labs & Purple Ventures 👏\n\n# Purple Ventures’ Post\n\nPurple Ventures\n\n3,771 followers\n\n3mo\n\nProudly announcing a new investment: Fether Labs!🖤 We’re excited to invest €450k in Fether Labs, a deeptech startup founded by researchers from Imperial College London. Fether Labs is developing a smart wristband that uses unique tendon-sensing technology to translate finger movements into digital commands without cameras or traditional input devices. The technology has the potential to change how people interact with AR/VR, robotics, healthcare, and industrial systems. The new funding will help the team launch its first developer kit, expand pilot projects, and move the technology closer to commercial deployment. Congratulations to the founders and we’re excited for the journey ahead! Read more at Vestbee.\
… [31397 more characters]
```
</details>

→ `exec`
```
await Promise.allSettled([
tools.web__run({search_query:[{q:'Pencil seed 7.4 million KAYA June 2026'}],response_length:"long"}).then(text),
tools.web__run({search_query:[{q:'"Nation 1" investment "2026" startup'}],response_length:"long"}).then(text),
tools.web__run({search_query:[{q:'"Presto" investment "2026" startup funding'}],response_length:"long"}).then(text),
tools.web__run({search_query:[{q:'"Rightcharge" "Purple" "September" "2026"'}],response_length:"long"}).then(text)
]);

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 30462)\nTotal output lines: 2383\n\nSoulmates Ventures Portfolio Investments, Soulmates Ventures Funds, Soulmates Ventures Exits (https://www.cbinsights.com/investor/soulmates-ventures)\nciteturn33search0 [wordlim: 200] Crawled: 2 days ago; Their latest investment was in Rightcharge as part of their Seed VC - IV on September 03, 2026. ... 9/3/2026  | Seed VC - IV  | Rightcharge  | $0.67M  | No  | BlackWood Ventures, and Purple Ventures  | 4\n\nVenture Capital\n\n# Soulmates Ventures\n\nsoulmatesventures.com\n\n## Investments\n\n31\n\n## Portfolio Exits\n\n2\n\n## Funds\n\n1\n\n## About Soulmates Ventures\n\nSoulmates Ventures is a venture capital firm that focuses on investing in sectors such as air, water, energy, mobility, education, healthcare, food and agriculture, and circular economy. iT was founded in 2020 and is based in Parahue 8, Czech Republic.\n\n## Headquarters Location\n\nRohanské nábřeží 693/10 2nd Floor\n\nPrague 8, 186 00,\n\nCzech Republic\n\n## Latest Soulmates Ventures News\n\nRightcharge Raises Growth Funding To Expand Across Europe After 20x ARR Growth\n\nSep 3, 2026\n\nThe financing follows a period of rapid commercial growth for the London-based company, which said annual recurring revenue has increased by more than 20 times over the past year. Rightcharge now supports more than 200 d
… [39099 more characters]
```
</details>

→ `exec`
```
for(const q of ['"Pencil" "KAYA" "June" "2026"','"Nation 1" "2026" funding','"Presto Ventures" investment 2026']) {
const r=await tools.web__run({search_query:[{q}],response_length:"short"}); text(r);
}

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 4.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 10456)\nTotal output lines: 395\n\nJournal of Health Psychology Research (https://www.jstage.jst.go.jp/browse/jhpr/advpub/0/_contents/-char/en)\nciteturn37search0 [wordlim: 200] Published: 4 months ago; Crawled: last month; Takayuki Yokoshima, Daisuke Noguchi, Aguru Ono, Ikuko Kaya ... Published: June 12, 2026 ... This study developed a paper-and-pencil Prosocial Motivation Brief Implicit Association Test for Children (PM-BIAT-C) and examined its reliability and construct validity in elementary school students.\nJournal of Health Psychology Research\n\nOnline ISSN : 2189-8804\nPrint ISSN : 2189-8790\nISSN-L : 2189-8804\n\n\nAdvance online publication\n\nAdvance online publication\n\nAdvance online publication allows users to view and download accepted articles before the production process has been finalised.\n\nDisplaying 1-2 of 2 articles from this issue\n\n  * Development and validation of a brief implicit association test of prosocial motivation for children\n\nTakayuki Yokoshima, Daisuke Noguchi, Aguru Ono, Ikuko Kaya\n\nArticle ID: 251023169\nPublished: June 12, 2026\nAdvance online publication: June 12, 2026\n\nDOIhttps://doi.org/10.11560/jhpr.251023169\n\nJOURNAL RESTRICTED ACCESS ADVANCE PUBLICATION\n\nShow abstract Hide abstract\n\nThis study developed a paper-and-pencil Prosocial Motivation Brief 
… [38566 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=[('ipm','https://www.ipmgrp.com/?post_type=post&p=1862'),('lhv','https://lhv.vc/news/lighthouse-ventures-participates-in-hermetiqs-2-2m-pre-seed-round/'),('miton','https://www.miton.cz/en/blog/miton-is-investing-in-ace-strava-but-for-padel-is-already-used-by-more-than-half-of-czech-players/'),('purple','https://tech.eu/2026/09/03/rightcharge-raises-ps500k-to-scale-fleet-ev-charging-payments-across-europe'),('reflex','https://www.gaebler.com/VC-Investors-575FF626-E6F2-4A1F-B319-4B6870BB85E3-Reflex-Capital'),('lrj','https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/'),('koopeo','https://shizune.co/investors/profile/koopeo-ventures'),('neulogy','https://www.cbinsights.com/investor/neulogy-ventures')]\ndef f(x):\n k,u=x;r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\n raw=r\n r=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S)\n t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',r)))\n print(k,'length',len(raw),'TEXT',t[:6000])\n print('RAW VERIFY',subprocess.run(['grep','-oE','.{0,80}(Hilo|Hermetiq
… [235 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 11159)\nTotal output lines: 1\n\n{\"chunk_id\":\"b33e3f\",\"wall_time_seconds\":2.251297042,\"exit_code\":0,\"original_token_count\":11711,\"output\":\"Warning: truncated output (original token count: 11711)\\nTotal output lines: 67\\n\\nneulogy length 919 TEXT  ERROR: The request could not be satisfied 403 ERROR The request could not be satisfied. Request blocked. We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner. If you provide content to customers through CloudFront, you can find steps to troubleshoot and help prevent this error by reviewing the CloudFront documentation. Generated by cloudfront (CloudFront) Request ID: mzbsJ0WY3yItrvLFE6CBZnCpAcLr9zYTRCqiWc87flXfWy2XqpWhgA== \\nRAW VERIFY \\nmiton length 202651 TEXT  Miton is investing in ACE. \\\"Strava but for padel\\\" is already used by more than half of Czech players. · Blog · Miton Portfolio People How we work AI Careers Blog cz Portfolio People How we work AI Careers Blog cz Miton is investing in ACE. \\\"Strava but for padel\\\" is already used by more than half of Czech players. Michala Gregorová 1. 10. 2026 (Press Release) Padel is the fastest-growing sport in the world. Tomáš Hodboď is a partner at Miton who, as CEO, bu
… [38771 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Pencil startup raises funding kaya amplify 7.4'},{q:'N1 ventures 2026 funding Myriad TrueClaim'},{q:'Zerops Presto Ventures May 2026 investment'},{q:'Sloneek Orbit Capital June 2026 funding'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Zerops Valuation & Funding History | Caplight (https://www.caplight.com/company/zerops)\nciteturn45search0 [wordlim: 200] Crawled: yesterday; Notable investors and investment history ... Zerops's most recent funding round was Seed on May 14, 2026. ... Key investors in Zerops include Presto Ventures, Gi21 Capital.\n--- | --- | --- | --- | --- | --- | ---\n\nFiling documents are not displayed on this public page. Request access to learn about available coverage.\n\nRequest access\n\n## Frequently Asked Questions\n\nCommon questions about Zerops's valuation, stock price, and market status.\n\nIs Zerops a public or private company?\n\nZerops is a private company.\n\nWhat is the current stock price of Zerops?\n\nZerops is a private company with no public stock price. No recent secondary market data is available.\n\nHow much is Zerops worth (valuation)?\n\nValuation information for Zerops is not publicly available.\n\nCan I buy Zerops stock?\n\nZerops shares may be available on secondary markets subject to transfer restrictions. Caplight facilitates secondary market transactions for accredited investors. Visit https://www.caplight.com to learn more.\n\nWhen was Zerops's last funding round?\n\nZerops's most recent funding round was Seed on May 14, 2026.\n\nWho are the main investors in Zerops?\n\nKey investors in Zerops include Presto Ventures, Gi21 Capital.\n\nW
… [14917 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Pencil" "Kaya" funding startup'},{q:'"N1" "TrueClaim" funding'},{q:'"Nation 1" Myriad funding'},{q:'"J&T" "Wultra" 6.8 million'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Kaya VC Portfolio Investments, Kaya VC Funds, Kaya VC Exits (https://www.cbinsights.com/investor/enern)\nciteturn47search0 [wordlim: 200] Crawled: today;  Tehdy zakladatelský tým Kaya investoval do Slevomatu, prvního startupu Tomáše Čupra. ... Czech-Slovak-founded startup TopK secures $5.5M in seed funding to enhance AI-powered search for businesses ... Their latest investment was in Pencil as part of their Seed VC on June 17, 2026.\n## Kaya VC Investments\n\n93 Investments\n\nKaya VC has made 93 investments. Their latest investment was in Pencil as part of their Seed VC on June 17, 2026.\n\nImage: CBI Logo\n\n### Kaya VC Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n6/17/2026  | Seed VC  | Pencil  | $7.4M  | Yes  | A16z Speedrun, and Amplify Partners  | 2\n5/19/2026  | Series A  | Viktor  | $75M  | Yes  | Accel, Alex Bouaziz, Bek Ventures, Cal Henderson, Charlie Songhurst, Daniel Gross, Guillermo Rauch, Harry Stebbings, Inovo, Jack Zhang, Joel Hellermark, Jorn van Dijk, Koen Bok, Lenny Rachitsky, Leonis Capital, Mati Staniszewski, Max Mullen, Nat Friedman, Nico Rosberg, SBS Seed Fund, Shaan Puri, Stewart Butterfield, Tenacity Ventures, Undisclosed Angel Investors, and Victor Riparbelli  | 4\n------------
… [14251 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw1aBqJTCl2pIE4p2wEwgknCRtCmDtO_YwLVGUu6RczbYPvBMTnfOFI1wOBm0rpTqOYDxZ8v8hLAndYaCbIhPD9rY7pbiiwWToejnaDILAUvKDsP53nvkqlkTog7v9ulxAm-5e4Rh8meBDGYGQpRk2OjImM_xp_1BV6ZWMtBpazYVXDw6s1cS07D9_TeCKKwyE2HJHq5F8ZMY7HMcfq857RLxbgwAh7BEIjYKfioRAcuywVB-Xgx2magpWFd_9d60CvFCqfRVHuQDzhtm7tD_AdlqWmbDAwoduZWcxkNpIYAGEmAaRLRmc3SLJryWkKA0rUzGpXWqdmv-1IDhPe8O3RG6r9NedvXIRW6RQ6mKUNU6dOa5-xXe4em2UbA2nTR_bbxUf2LtRENh9O2wwozvUcGu88Vfg-V_AwSsuHIdtjqabhxA_9dpd5K2QFSSEcB53Mg-GSiWjXZaT0HiFN0BGoqbnEDQ6FI6sV2jf77gse9JXDbUTY4WVxeAysvi9aUptw4lYUhQWvuo3lXFU9TsJrj4py8QYy5lO5fkGKvEvSVNLN0Fm-LfcwlwXpMwIw6DcNrYgC8VPdVb9ITzDPBkM7PBCjOSkwsxFyROMUFo4oPXEbYIdo9HE7tgDEprGx5T13VpdOktkaLzdk8ZZOrpLnlICW2bZSv7nqOgYauLfL4zf9iX1RRDonLntTSj-p-Y83jGm6_4maskrX9un85E_EOi0ef8FCNGwW3tKFof4IAp3dS3lYK2iYa17fagIBYWG_RZMKTgl4BzG6Vd7Ja_FMh9dD4cRUaYJRX_XlZnLtbDAW2VOx-z7-LK-biTUvM-cHi1U3LM6Q-9gE7QBQHjo6w_cZeuVxpja0L3RiJXn5X6O74QTMI9byTLxO4C7KqwUIL-vCkKkngvCrb_UK1fSTwWw=="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Merchantee" "Reflex" June 2026'},{q:'"Myriad" "N1" seed September 2025'},{q:'"Pencil" seed Amplify 2026 Tom Krcha'},{q:'"Zerops" "Presto" "2026"'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Merchantee Stock Price, Funding, Valuation, Revenue & Financial Statements (https://www.cbinsights.com/company/merchantee/financials)\nciteturn48search0 [wordlim: 200] Crawled: 3 days ago; Merchantee's latest funding round was a Pre-Seed - II for $2.08M on June 9, 2026. ... Reflex Capital invested in Merchantee's Pre-Seed - II funding round.\n\n# Merchantee\n\nUnclaimed\n\nmerchantee.io\n\n## Total Raised\n\n$2.73M\n\n## Investors Count\n\n4\n\n## Funding, Valuation & Revenue\n\n3 Fundings\n\nMerchantee has raised $2.73M over 3 rounds.\n\nMerchantee's latest funding round was a Pre-Seed - II for $2.08M on June 9, 2026.\n\nDate  | Round  | Amount  | Investors  | Valuation Valuations are submitted by companies, mined from state filings or news, provided by VentureSource, or based on a comparables valuation model.  | Revenue  | Sources\n--- | --- | --- | --- | --- | --- | ---\n6/9/2026  | Pre-Seed - II  | $2.08M  | Reflex Capital, Czech Founders VC, and Lighthouse Ventures  | $XXM  | 0 FY undefined  | 3\n2/1/2024  | Pre-Seed  | $XXM  | Subscribe to see more  | $XXM  | 0 FY undefined  | 10\n | Other Investors  |  | Subscribe to see more  | $XXM  | 0 FY undefined  | 10\n\nDate  | 6/9/2026  | 2/1/2024  | \nRound  | Pre-Seed - II  | Pre-Seed  | Other Investors\nAmount  | $2.08M  | $XXM  | \nInvestors  | Reflex Capital, Czech Founders VC, and Lighthouse Ventures  
… [12634 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=[('kaya','https://shizune.co/investors/profile/kaya-8ed9'),('n1','https://nordic9.com/news/myriad-ai-in-a-78m-seed-round-led-by-category-ventures-and-joined-by-long-journey-10vc-n1-breakwater-caesar-vc-bd-partners-and-preston-werner/'),('jt','https://www.morningstar.com/news/pr-newswire/20260701ln94236/wultra-raises-68-million-in-series-a-funding-to-accelerate-global-expansion-of-post-quantum-digital-identity-solutions'),('reflex','https://startupkitchen.community/agentic-marketplace-intelligence-startup-merchantee-raises-e1-8m-to-expand-across-europe/'),('orbit','https://nordic9.com/news/sloneek-raised-a-6m-seed-extension-led-by-orb/'),('monogram','https://app.dealroom.co/companies/streamstar')]\ndef f(x):\n k,u=x;r=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout\n t=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S);t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',t)))\n matches=[m.group() for m in re.finditer('.{0,150}(?:Theorema|Pencil|2026|2025|2024|Nation 1|N1|J&T Ventures|Reflex Capital|Orbit Capital|MONOGRAM).{0,25
… [73 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"2e5d0e\",\"wall_time_seconds\":0.000002583,\"exit_code\":0,\"original_token_count\":0,\"output\":\"\"}"}]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=[('kaya','https://shizune.co/investors/profile/kaya-8ed9'),('n1','https://nordic9.com/news/myriad-ai-in-a-78m-seed-round-led-by-category-ventures-and-joined-by-long-journey-10vc-n1-breakwater-caesar-vc-bd-partners-and-preston-werner/'),('jt','https://www.morningstar.com/news/pr-newswire/20260701ln94236/wultra-raises-68-million-in-series-a-funding-to-accelerate-global-expansion-of-post-quantum-digital-identity-solutions'),('reflex','https://startupkitchen.community/agentic-marketplace-intelligence-startup-merchantee-raises-e1-8m-to-expand-across-europe/'),('orbit','https://nordic9.com/news/sloneek-raised-a-6m-seed-extension-led-by-orb/'),('monogram','https://app.dealroom.co/companies/streamstar')]\ndef f(x):\n k,u=x;r=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout\n t=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S);t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',t)))\n matches=[m.group() for m in re.finditer('.{0,150}(?:Theorema|Pencil|2026|2025|2024|Nation 1|N1|J&T Ventures|Reflex Capital|Orbit Capital|MONOGRAM).{0,25
… [144 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"e90e5b\",\"wall_time_seconds\":1.099777541,\"exit_code\":0,\"original_token_count\":2941,\"output\":\"('kaya', 326429, ['ccessor of Enern Tech for allthings venture capital, with 40+ investments and latest fund of €90. Show all Total investments: 99 Last investment: Sep 2026 Lead investor: 19% Fund size: $82M Last fund: Jun 2025 Last updated: Oct 2026 For AI agents: llms.txt Industries KAYA invests in Software Internet Health Care Artificial Intelligence E-Commerce Stages KAYA invests in Seed Pre-Seed Series A Venture -', ' is a biocomputing company growing large-scale neuronal tissue, living hardware with memory baked in at the cellular level. $10M / Pre-Seed / Sep 01, 2026 Theorema Theorema.ai is an AI-powered startup that focuses on autonomous R&D agents for science-intensive industries, including innovative materials, biotech, pharmaceuticals, and chemicals. $3.3M / Pre-Seed / Mar 27, 2026 GenPeach AI GenPeach AI de', ' manipulation of digital assets. Their work targets applications in content production, creative workflows, andgenerative AI research. Seed / Jan 01, 2026 Jutro Medical Jutro Medical offers a combination of online and offline primary care — pairing mobile first telemedicine with physical clinic $28.2M / Series A / Dec 16, 2025 Supernova.io Supernova connects to popular design editors and interprets de', 'te their own — for i
… [10467 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nfor u,kw in [('https://shizune.co/investors/profile/kaya-8ed9','biocomputing'),('https://www.prestoventures.com/news','Sensible'),('https://www.limerock.sk/main','Portfolio')]:\n r=subprocess.run(['curl','-Ls',u],capture_output=True,text=True).stdout\n t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n i=t.find(kw);print(u,t[max(0,i-120):i+450])\nPY","max_output_tokens":1000}));
text(await tools.web__run({search_query:[{q:'"KAYA" "biocomputing" 10 million'},{q:'"J&T" "Wultra" site:wultra.com "2026"'},{q:'"Presto Tech Horizons" "October" "2026" Sensible'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"03e97c\",\"wall_time_seconds\":0.348173958,\"exit_code\":0,\"original_token_count\":430,\"output\":\"https://shizune.co/investors/profile/kaya-8ed9 d email See all 7 team members → Investments Company Description Round Links Frontier Computing Frontier Computing is a biocomputing company growing large-scale neuronal tissue, living hardware with memory baked in at the cellular level. $10M / Pre-Seed / Sep 01, 2026 Theorema Theorema.ai is an AI-powered startup that focuses on autonomous R&D agents for science-intensive industries, including innovative materials, biotech, pharmaceuticals, and chemicals. $3.3M / Pre-Seed / Mar 27, 2026 GenPeach AI GenPeach AI develops multimodal AI models for generating and editi\\nhttps://www.prestoventures.com/news  Presto Ventures | News Portfolio Team Founders Horizons News Contact Portfolio Team Founders Horizons News Contact IN THE SPOTLIGHT. From time to time, our founders and portfolio companies make waves in the news – here’s a sneak peek. For more updates, check out our LinkedIn page or follow @PrestoVC on X. 25/5/26 Presto Ventures Představenstvo společnosti Presto Ventures II a.s., osoba rizikového kapitálu, se sídlem Na příkopě 859/22, Nové Měst\\nhttps://www.limerock.sk/main ars in corporate finance , consulting and M&A advisory track record of profitable VC investment dea ls Up Limerock Fund Portfol
… [16840 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=[('jt','https://www.wultra.com/blog/wultra-raises-68-million-eur-in-series-a'),('mono','https://zive.aktuality.sk/clanok/65772/do-websupportu-vstupil-investor-ziskal-15-percentny-podiel/'),('presto','https://startupkitchen.community/agentic-marketplace-intelligence-startup-merchantee-raises-e1-8m-to-expand-across-europe/')]\ndef f(x):\n k,u=x;r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\n t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n if k=='presto':return k,re.findall(r'href=[\\\"\\']([^\\\"\\']*sensible[^\\\"\\']*)',r)\n return k,[m.group() for m in re.finditer('.{0,120}(?:2026|2012|Monogram|J&T Ventures|June|July).{0,200}',t)][:15]\nfor x in concurrent.futures.ThreadPoolExecutor().map(f,urls):print(x)\nPY","max_output_tokens":3000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"3c434f\",\"wall_time_seconds\":1.0859105,\"exit_code\":0,\"original_token_count\":1245,\"output\":\"('jt', ['bal Expansion of Post-Quantum Digital Identity Solutions COMPANY NEWS POST-QUANTUM DIGITAL IDENTITY COMPANY NEWS WULTRA June 29, 2026 Wultra, a provider of post-quantum authentication and digital identity solutions for banks and fintechs, announced the completion of a €6.8 million Series A funding round. The company helps ', ' investor Seventure Partners, followed by ARIADNEXT founders Marc Norlain and Guillaume Despagne and existing investors J&T Ventures and Elevator Ventures. Table of contents TOC Content Items Loads Here The investment round underscores strong investor confidence in Wultra’s vision and its portfolio of post-quantum authentication a', \\\". Two returning investors also joined the funding round, demonstrating their strong confidence in the company's future. J&T Ventures first backed Wultra in 2022 and then again in 2025. “We backed Wultra as the first Investor in 2022, and since then, we have seen consistent growth and the team’s ability to transform security produc\\\", \\\"nd remain highly confident that the company's strongest milestones are still ahead,” said Zuzana Ondrejová , Partner at J&T Ventures. “We see the accelerating need of the global banking industry to deploy post-quantum security solutions already to
… [3668 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Streamstar" "Monogram" "2013"'},{q:'"Limerock" "GEVORKYAN" investment 2016'},{q:'"KOOPEO" "July" "2025"'},{q:'"LRJ Capital" "2020" investment'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "ANNUAL REPORT 2022 (https://www.gevorkyan.eu/wp-content/uploads/2022-Annual-Report_EN.pdf)\nciteturn62search12 [wordlim: 200] Published: 6 months ago; investor companies Jeremie Co-Investment Fund, represented by Limerock Fund Manager, and ... these companies acquired a 3.5% interest in GEVORKYAN, Inc. in 2016\ncompany is issued by TÜV SÜD and focuses on the development of a quality management system \nwith an emphasis on continuous improvement, as well as on the prevention of defects in the supply \nchain.  \nIn order to secure long-term growth in 2016, a decision was taken to accept funding from the \ninvestor companies Jeremie Co-Investment Fund, represented by Limerock Fund Manager, and \nBHS Fund II - Private Equity, in the form of mezzanine financing with a six-year maturity. Each of \nthese companies acquired a 3.5% interest in GEVORKYAN, Inc. in 2016 \nGEVORKYAN, a.s. is the first Slovak SME company to issue public bonds on the Bratislava Stock \nExchange. Securities issued by the company do not have limited transferability. \nThe financial statements for 2022 were audited by Ernst & Young Slovakia, spol. s r.o., license SKAU \nNo. 257. \nIn March 2019, GEVORKYAN, a.s. successfully issued bonds worth € 10 million. The bonds were \npublicly traded on the Prague Stock Exchange. Their purpose was to repay an expensive mezzanine \n---------------------
… [11979 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nspecs=[\n('ipm','https://www.ipmgrp.com/ipm-group-invests-in-micromobility-company-hilo-ev/','today announces that it has invested in Hilo EV'),\n('jt','https://www.wultra.com/blog/wultra-raises-68-million-eur-in-series-a','and existing investors J&T Ventures and Elevator Ventures.'),\n('kaya','https://shizune.co/investors/profile/kaya-8ed9','$10M / Pre-Seed / Sep 01, 2026'),\n('koopeo','https://shizune.co/investors/profile/koopeo-ventures','$638K / Pre-Seed / Jul 17, 2025'),\n('lhv','https://lhv.vc/news/lighthouse-ventures-participates-in-hermetiqs-2-2m-pre-seed-round/','Lighthouse Ventures Participates in Hermetiq’s $2.2M Pre-Seed Round'),\n('limerock','https://www.sih.sk/en/portfolio/gevorkyan-s-r-o','This support is in the form of venture capital and its utilisation started in February 2016.'),\n('lrj','https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/','LRJ Capital cez svoj fond GROWWS SICAV, a.s. podporil inovátora v inteligentnom investovaní, Finax investíciou 1,5 milióna eur.'),\n('miton','https://www.miton.cz/en/blog/miton-is-investing-in-ace-strav
… [2116 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"cf2b3a\",\"wall_time_seconds\":1.771110541,\"exit_code\":0,\"original_token_count\":2740,\"output\":\"('ipm', 'GREP_OK', True, 'quote', 'today announces that it has invested in Hilo EV', 'context', 'raTech, today announces that… Read more Cambridge, UK – 14 June 2022: IPM Group (‘IPM’), the next generation asset manager specialising in InfraTech, today announces that it has invested in Hilo EV (‘Hilo’), the micromobility company reimagining personal transport. Hilo is poised to become the global standard bearer for micromobility and IPM’s investment will support Hilo as it brings its first product, the Hilo e-scooter, to market. Hilo’s advanced electric scooter boasts a variety of innovative features including an oversize front wheel that ', 'dates', ['14 June 2022', '2022-06-14', 'datePublished\\\":\\\"2022-06-14T07:34:42+00:00\\\"', 'datePublished\\\":\\\"2022-06-14T07:34:42+00:00\\\"', '14 June 2022', '14 June 2022', '2026-10-11', '2026-10-11'])\\n('jt', 'GREP_OK', True, 'quote', 'and existing investors J&T Ventures and Elevator Ventures.', 'context', 'r experience. The investment round was backed by lead investor Seventure Partners, followed by ARIADNEXT founders Marc Norlain and Guillaume Despagne and existing investors J&T Ventures and Elevator Ventures. Table of contents TOC Content Items Loads Here The investment round underscores stro
… [9682 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw2o8pfVozMYVeVim0DSwwzVs1949SWMm7OD0I8wI9QoHEV7EeOvgxzVx4JnwNZFCKFkH87LHrC2o-3WiBLLcb_g-oSmr1TGusCwitrTAuE3drGymkhY09MtbJQWg5IZMZnn3nBM-SBt7_mUihPzLdYBh7pfTtEXcxzqR4VTO9jyef2FchZuIEv_I4vL-vkn9ICkkS0MTz8Neixsx28WsdnOGyS2ikRGuSDKnkHfsEBaSgsDk9OqLiHq632zIYZrbFTEbCmeOnKRS1Qdgc-k3zQ3D4k_G-dFJIJ3XweG7bwWkpNnLr06xrPJ7Cth62cbForLqmgcGfqnaERlilG5SCPGICrNs8OtG0rpne1AuXoKso1mN-cMOp8y4w8mymZ9mz6cScdcOLMuB_nii3tjOHa7tJK8PDyGGDZDfeXfMit7Cd0Uu6yJZoXFVb-2baKnX-EOTdK92IUP5TaTcbuPo_vrHhasDYC4G_RGQCHz6uyMidAHh71INP3x-HBy4pOuXWuByl8M63Y6WdMvgxW6j0Rbe9M6HTBOBc2gtwPGwSLQq_TCVtLzzNUJkkcW9XPxQNINRx0eCLXLLimll7AeFoMacllviIfJgzorpBwLbKCcdcA="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=[('limerock','https://gevorkyan.eu/wp-content/uploads/2024_EN_Annual-report-1.pdf'),('lrj','https://www.avantfunds.cz/wp-content/uploads/final-vz-growws-2020.pdf'),('neulogy','https://seedtable.com/companies/ga-drilling/funding-rounds/other-2025-07'),('presto','https://startupkitchen.community/czech-tech-horizons-invests-in-sensible-biotechnologies-47-million-funding-round-to-support-mrna-therapeutics-and-strengthen-europes-resilience-to-biological-threats/')]\ndef f(x):\n k,u=x;r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True).stdout\n if r.startswith(b'%PDF'):\n  r=subprocess.run(['pdftotext','-','-'],input=r,capture_output=True).stdout.decode()\n else:\n  r=r.decode(errors='replace');r=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S);r=html.unescape(re.sub('<[^>]+>',' ',r))\n t=re.sub(r'\\s+',' ',r)\n terms={'limerock':'acquired a 3.5','lrj':'5 176','neulogy':'Neulogy','presto':'Presto'}\n i=t.find(terms[k]);print(k,'LEN',len(t),t[max(0,i-250):i+800])\n print('MATCH',subprocess.run(['grep','-oE','.{0,140}('+terms[k]+').{0,220}'],input=t,capt
… [134 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"ffef19\",\"wall_time_seconds\":0.988970209,\"exit_code\":0,\"original_token_count\":616,\"output\":\"neulogy LEN 60  Just a moment... Enable JavaScript and cookies to continue \\nMATCH \\nlrj LEN 73  404 Not Found Not Found The requested URL was not found on this server. \\nMATCH \\nlimerock LEN 151363 decision was taken to accept funding from the investor companies Jeremie Co-Investment Fund, represented by Limerock Fund Manager, and BHS Fund II - Private Equity, in the form of mezzanine financing with a six-year maturity. Each of these companies acquired a 3.5% interest in GEVORKYAN, Inc. in 2016 GEVORKYAN, a.s. is the first Slovak SME company to issue public bonds on the Bratislava Stock Exchange. Securities issued by the company do not have limited transferability. The financial statements for the year 2024 were audited by Ernst & Young Slovakia, spol. s r.o., license SKAU No. 257. On 16.11.2021 the related company GEVORKYAN CZ, s.r.o. successfully issued bonds worth € 30 million, which are publicly traded on the Prague Stock Exchange and the funds were provided to GEVORKYAN, a.s. in the form of a loan. In 2014, the company employed 190 employees and generated sales of approximately EUR 17 million. Over the next 8 years, thanks mainly to the aforementioned automation, the company has managed to streamline production and reduce j\\nMATCH me
… [1212 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://startupkitchen.community/czech-tech-horizons-invests-in-sensible-biotechnologies-47-million-funding-round-to-support-mrna-therapeutics-and-strengthen-europes-resilience-to-biological-threats/'\nr=subprocess.run(['curl','-Ls',u],capture_output=True,text=True).stdout;t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\nprint(t[900:6500])\nPY","max_output_tokens":2000}));
text(await tools.web__run({search_query:[{q:'"Neulogy" "BiteBerry" 2024 investment'},{q:'"Presto Ventures" "Choice" "2026" round'}],response_length:"short"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"8f4309\",\"wall_time_seconds\":0.994344375,\"exit_code\":0,\"original_token_count\":1409,\"output\":\"hnologies. $47 million funding round to support mRNA therapeutics and strengthen Europe’s resilience to biological threats by Jakob Ulrych October 6, 2026 Tech Horizons, a VC fund investing in technologies that strengthen Western sovereignty, has invested in biotechnology startup Sensible Biotechnologies. The company is developing the first fully integrated cell-based platform of its kind for the design, optimisation and manufacturing of mRNA using living cells. Sensible combines biotechnology, computational modelling and artificial intelligence, paving the way for a new generation of mRNA therapeutics for cancer, genetic disorders and a range of other serious diseases. The company works with global technology leaders, leveraging their computing technologies and AI to reduce one of its mRNA optimisation cycles from 15 days to just one. Beyond enabling the development of next-generation therapeutics, Sensible’s technology is designed to enable local, flexible and resilient mRNA manufacturing. In doing so, it can help strengthen manufacturing capacity in Europe and the United States, while improving the ability to respond rapidly to emerging biological threats. Sensible Biotechnologies has secured a total of $47 million to further develop its in
… [18782 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html,concurrent.futures\nurls=['https://neulogy.vc/portfolio/ga-drilling/','https://neulogy.vc/portfolio/biteberry/','https://www.prestoventures.com/horizons','https://www.gaebler.com/VC-Investors-2E01A655-86BE-4887-BBF5-F8EC7C17E557-Presto-Ventures']\ndef f(u):\n r=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout;t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n return u,[(m.group()) for m in re.finditer('.{0,100}(?:Invested|Tech Horizons|Choice|2026).{0,160}',t)][:8]\nfor x in concurrent.futures.ThreadPoolExecutor().map(f,urls):print(x)\nPY","max_output_tokens":1800}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"8d5a3d\",\"wall_time_seconds\":0.949242208,\"exit_code\":1,\"original_token_count\":875,\"output\":\"('https://neulogy.vc/portfolio/ga-drilling/', ['ing develops technology for ultra-deep geothermal as the only viable large-scale baseload solution. Invested: 2016 Web: gadrilling.com Founder Igor Kočiš CEO at GA Drilling Partner in charge Christian Mandl Managing Partner About GA Drilling , with its patented PLASMA', 'wsletter I agree with the Privacy Policy About us Portfolio News Careers 17 Contact SFDR Disclosure 2026 Neulogy Ventures, All rights reserved. Made by Echt '])\\n('https://neulogy.vc/portfolio/biteberry/', ['ry uses AI to boost restaurant efficiency with a voice ordering system integrated into POS systems. Invested: 2024 Web: biteberry.com Founder Dusan Koutny CEO Partner in charge Jaroslav Luptak Partner About BiteBerry combines food industry experience with AI and autom', 'wsletter I agree with the Privacy Policy About us Portfolio News Careers 17 Contact SFDR Disclosure 2026 Neulogy Ventures, All rights reserved. Made by Echt '])\\n('https://www.prestoventures.com/horizons', [])\\nTraceback (most recent call last):\\n  File \\\"<stdin>\\\", line 6, in <module>\\n  File \\\"/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/concurrent/futures/_base.py\\\", line 645, in result_iterat
… [2379 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nchecks=[('kaya','https://startupkitchen.community/czech-tech-horizons-invests-in-sensible-biotechnologies-47-million-funding-round-to-support-mrna-therapeutics-and-strengthen-europes-resilience-to-biological-threats/','and existing investors Recode Ventures, Isomer Capital, Y Combinator, Backed VC, Kaya VC, Civilization Ventures and BlueYard Capital.'),('neulogy','https://neulogy.vc/portfolio/biteberry/','Invested: 2024'),('n1','https://nordic9.com/news/myriad-ai-in-a-78m-seed-round-led-by-category-ventures-and-joined-by-long-journey-10vc-n1-breakwater-caesar-vc-bd-partners-and-preston-werner/','Round investors: Caesar Business Angels Plug and Play Preston-Werner Ventures Nation 1 VC'),('presto','https://www.gaebler.com/VC-Investors-2E01A655-86BE-4887-BBF5-F8EC7C17E557-Presto-Ventures','Choice')]\nfor k,u,q in checks:\n r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True).stdout.decode(errors='replace');t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n v=subprocess.run(['grep','-oF',q],input=t,capture_output=Tru
… [125 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"557ed7\",\"wall_time_seconds\":2.957871875,\"exit_code\":0,\"original_token_count\":445,\"output\":\"kaya 0 and existing investors Recode Ventures, Isomer Capital, Y Combinator, Backed VC, Kaya VC, Civilization Ventures and BlueYard Capital.\\n\\nuropean Union . Tech Horizons participated in the investment round alongside OTB Ventures, In-Q-Tel and existing investors Recode Ventures, Isomer Capital, Y Combinator, Backed VC, Kaya VC, Civilization Ventures and BlueYard Capital. Investors also include the family office of BioNTech co-founder Christoph Huber and Tim Garnett, former Chief Medical Officer of Eli Lilly . Previous investors includ\\nneulogy 0 Invested: 2024\\n\\nry uses AI to boost restaurant efficiency with a voice ordering system integrated into POS systems. Invested: 2024 Web: biteberry.com Founder Dusan Koutny CEO Partner in charge Jaroslav Luptak Partner About BiteBerry combines food industry experience with AI and automation to create tools for improving restaurant efficiency and profitability. Their primary product is a voice ordering system that a\\nn1 0 Round investors: Caesar Business Angels Plug and Play Preston-Werner Ventures Nation 1 VC\\n\\nnce Legal Services Software Services Total investments received (USD): 9.8m Round value (USD): 7.8m Round investors: Caesar Business Angels Plug and Play Preston-Werner Ventures Nati
… [541 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://www.prestoventures.com/'\nr=subprocess.run(['curl','-Ls',u],capture_output=True,text=True).stdout\nprint(re.findall(r'href=\"([^\"]+)\"[^>]*>[^<]*(?:Horizons)',r));print([x for x in re.findall('href=\"([^\"]+)\"',r) if 'horizon' in x])\nu='https://www.gaebler.com/VC-Investors-2E01A655-86BE-4887-BBF5-F8EC7C17E557-Presto-Ventures'\nr=subprocess.run(['curl','-Ls',u],capture_output=True).stdout.decode(errors='replace');t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',r)));i=t.find('Last Transaction');print(t[i:i+1400])\nPY","max_output_tokens":800}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"53c87c\",\"wall_time_seconds\":0.721236291,\"exit_code\":0,\"original_token_count\":399,\"output\":\"['https://www.prestotech.com/', 'https://www.prestotech.com/', 'https://www.prestotech.com/']\\n['https://therecursive.com/presto-tech-horizons-announces-first-investments-in-ai-and-defense/']\\nLast Transaction 2/25/2026 Transaction History Our records indicate that Presto Ventures invested in the VC transactions listed below. Dollar amounts are for the entire raise, which may include other investors. Company Date Round Amount The New Era of Shopping 2/25/2026 Seed $1,400,000 Firehawk Aerospace 9/25/2025 Series C $60,000,000 Iost 6/10/2025 Undisclosed $21,000,000 MoneySuperMarket 1/10/2025 Series A $20,000,000 GAIB 12/19/2024 Seed $5,000,000 Pibox 11/7/2024 Undisclosed $1,200,000 Jeff App 7/17/2024 Seed $2,000,000 Zerops 6/20/2024 Seed $500,000 Lakmoos 3/5/2024 Seed $275,000 CloudTalk 1/18/2024 Series B $28,000,000 Keboola 12/1/2023 Series A $32,000,000 Getpin 11/27/2023 Seed $400,000 CityPay.io 8/17/2023 Undisclosed $2,174,000 Outfindo 8/11/2023 Seed $982,000 IP Fabric 6/29/2023 Series B $25,000,000 Cruxo 5/8/2023 Undisclosed $877,000 Finmap.online 2/27/2023 Undisclosed $1,063,000 Keboola 11/22/2022 Seed $4,500,000 Trusted Twin 9/22/2022 Seed $1,000,000 Investor Contacts Title Name Email & Social Partner Eduard Kucera Partner Roman Novácek Pa
… [340 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nfor u in ['https://www.prestotech.com/','https://www.prestotech.com/portfolio']:\n r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True).stdout.decode(errors='replace');t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n print(u,t[:1200]);print([(m.group()) for m in re.finditer('.{0,50}(?:Sensible|Presto Ventures|Tech Horizons).{0,150}',t)][:6])\nPY","max_output_tokens":1200}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.2 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"53a298\",\"wall_time_seconds\":1.012880125,\"exit_code\":0,\"original_token_count\":689,\"output\":\"https://www.prestotech.com/  Tech Horizons | Investing in Resilience About Portfolio Pitch Us Team Careers News Contact About Portfolio Pitch Us Team Careers News Contact Investing In Resilience Venture Capital Backed by Industrial Strength Protecting The future Tech Horizons connects frontier technologies, strategic investments, and purpose: to create a safer, more resilient future. Stronger Together 01 Our Unique Edge The best of tech investing meets the best of industrial-technological expertise. A team of seasoned VC professionals joined forces with CSG to back global companies at the forefront of defense, security, and resilience tech . EXCLUSIVE PARTNERSHIP More than 30 years of industrial expertise, connections in defense sectors, and strategic business support for portfolio firms. CSG’s market access, resources, and manufacturing capabilities help overcome barriers that limit other VC players in defense tech . UNPARALLELED NETWORK Our strong reputation and proven track record ensure access to a robust pipeline of relevant startups , extensive deal flow, and an active market presence. Partnerships with 400+ later-stage VCs deliver growth and funding opportunities for portfolio companies. SECTOR FOCUS A\\n[' Tech Horizons | Investing in R
… [1503 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://lasvegas.newsnetmedia.com/story/484299/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-worlds-most-dangerous-jobs/'\nr=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\nq='participation from MVP Ventures, Kaya, RunwayVC, Compound';print('raw grep',subprocess.run(['grep','-oF',q],input=r,capture_output=True,text=True).stdout)\nfor u,q in [('https://startupkitchen.community/czech-tech-horizons-invests-in-sensible-biotechnologies-47-million-funding-round-to-support-mrna-therapeutics-and-strengthen-europes-resilience-to-biological-threats/','has invested in biotechnology startup Sensible Biotechnologies.'),('https://neulogy.vc/portfolio/biteberry/','Invested: 2024')]:\n r=subprocess.run(['curl','-Ls',u],capture_output=True,text=True).stdout;t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n print(q,subprocess.run(['grep','-oF',q],input=t,capture_output=True,text=True).stdout)\nPY","max_output_tokens":700}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"ae2857\",\"wall_time_seconds\":2.408615292,\"exit_code\":0,\"original_token_count\":57,\"output\":\"raw grep participation from MVP Ventures, Kaya, RunwayVC, Compound\\n\\nhas invested in biotechnology startup Sensible Biotechnologies. has invested in biotechnology startup Sensible Biotechnologies.\\n\\nInvested: 2024 Invested: 2024\\n\\n\"}"}]
```
</details>

**Codex:**

[redacted: name]
[
  {
    "id": "ipm-group",
    "is_investor": "yes",
    "type": "pe",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Hilo EV",
      "date": "2022-06-14",
      "date_precision": "day",
      "url": "https://www.ipmgrp.com/ipm-group-invests-in-micromobility-company-hilo-ev/",
      "quote": "today announces that it has invested in Hilo EV"
    },
    "active_36m": "no",
    "confidence": "medium",
    "note": "The growth-equity manager operates from Bratislava and London, with Bratislava its principal published contact, and Hilo EV is the latest dated investment independently verified."
  },
  {
    "id": "jt-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Wultra",
      "date": "2026-06-29",
      "date_precision": "day",
      "url": "https://www.wultra.com/blog/wultra-raises-68-million-eur-in-series-a",
      "quote": "and existing investors J&T Ventures and Elevator Ventures."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Prague-based venture fund is explicitly identified by Wultra as a participant in its dated Series A announcement."
  },
  {
    "id": "kaya-vc",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Minerva Humanoids",
      "date": "2026-10-06",
      "date_precision": "day",
      "url": "https://lasvegas.newsnetmedia.com/story/484299/minerva-humanoids-emerges-from-stealth-with-10m-pre-seed-round-led-by-general-catalyst-to-build-humanoid-robots-for-the-worlds-most-dangerous-jobs/",
      "quote": "participation from MVP Ventures, Kaya, RunwayVC, Compound"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "KAYA is a Prague-based venture manager and the dated funding announcement names it among Minerva's pre-seed investors."
  },
  {
    "id": "koopeo-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "TRIFFT Loyalty Platform",
      "date": "2025-07-17",
      "date_precision": "day",
      "url": "https://shizune.co/investors/profile/koopeo-ventures",
      "quote": "$638K / Pre-Seed / Jul 17, 2025"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "Its official website confirms direct startup investing and Czech operations, while the latest dated TRIFFT investment is documented in a public investor transaction table."
  },
  {
    "id": "lighthouse-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Hermetiq",
      "date": "2026-08-31",
      "date_precision": "day",
      "url": "https://lhv.vc/news/lighthouse-ventures-participates-in-hermetiqs-2-2m-pre-seed-round/",
      "quote": "Lighthouse Ventures Participates in Hermetiq’s $2.2M Pre-Seed Round"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Prague-based fund's own dated announcement confirms its participation in Hermetiq's pre-seed financing."
  },
  {
    "id": "limerock",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "GEVORKYAN",
      "date": "2016-01-01",
      "date_precision": "year",
      "url": "https://gevorkyan.eu/wp-content/uploads/2024_EN_Annual-report-1.pdf",
      "quote": "Each of these companies acquired a 3.5% interest in GEVORKYAN, Inc. in 2016"
    },
    "active_36m": "no",
    "confidence": "high",
    "note": "Limerock manages an equity-investment portfolio from Bratislava, but its official SFDR disclosure states that its legacy fund has made no new investment decisions since November 2016."
  },
  {
    "id": "lrj-capital",
    "is_investor": "yes",
    "type": "private_investor",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Finax",
      "date": "2019-03-15",
      "date_precision": "day",
      "url": "https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/",
      "quote": "LRJ Capital cez svoj fond GROWWS SICAV, a.s. podporil inovátora v inteligentnom investovaní, Finax investíciou 1,5 milióna eur."
    },
    "active_36m": "no",
    "confidence": "medium",
    "note": "Slovak public sources identify a private investment holding investing through GROWWS, and the Finax announcement is the latest dated transaction whose text could be independently verified."
  },
  {
    "id": "miton",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "ACE",
      "date": "2026-10-01",
      "date_precision": "day",
      "url": "https://www.miton.cz/en/blog/miton-is-investing-in-ace-strava-but-for-padel-is-already-used-by-more-than-half-of-czech-players/",
      "quote": "Miton would become an equal partner and, to start with, invest several million crowns."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "Miton's dated announcement describes its equity partnership and initial investment in ACE, with its investment team based in Prague."
  },
  {
    "id": "monogram-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Websupport",
      "date": "2013-05-01",
      "date_precision": "month",
      "url": "https://zive.aktuality.sk/clanok/65772/do-websupportu-vstupil-investor-ziskal-15-percentny-podiel/",
      "quote": "Do slovenskej webhostingovej firmy Websupport začiatkom mája investoval Monogram Ventures."
    },
    "active_36m": "no",
    "confidence": "medium",
    "note": "The Slovak investment firm acquired a 15% Websupport stake in May 2013, while later references to its Streamstar shareholding do not establish a newer investment date."
  },
  {
    "id": "nation-1",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Myriad AI",
      "date": "2025-09-12",
      "date_precision": "day",
      "url": "https://nordic9.com/news/myriad-ai-in-a-78m-seed-round-led-by-category-ventures-and-joined-by-long-journey-10vc-n1-breakwater-caesar-vc-bd-partners-and-preston-werner/",
      "quote": "Round investors: Caesar Business Angels Plug and Play Preston-Werner Ventures Nation 1 VC"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "N1 manages early-stage equity funds with an operating team split between Prague and San Francisco, and the Myriad seed announcement explicitly lists Nation 1 VC."
  },
  {
    "id": "neulogy-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "BiteBerry",
      "date": "2024-01-01",
      "date_precision": "year",
      "url": "https://neulogy.vc/portfolio/biteberry/",
      "quote": "Invested: 2024"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The Slovak manager's own portfolio dates its BiteBerry investment to 2024; a newer GA Drilling database record could not be verified in accessible page text."
  },
  {
    "id": "orbit-capital",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Sloneek",
      "date": "2026-06-08",
      "date_precision": "day",
      "url": "https://nordic9.com/news/sloneek-raised-a-6m-seed-extension-led-by-orb/",
      "quote": "$6 million seed extension led by Orbit Capital and Venture to Future Fund"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "Orbit's Czech manager operates both growth-equity and debt strategies, and Sloneek's dated equity financing was selected rather than subsequent debt transactions."
  },
  {
    "id": "presto-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Sensible Biotechnologies",
      "date": "2026-10-06",
      "date_precision": "day",
      "url": "https://startupkitchen.community/czech-tech-horizons-invests-in-sensible-biotechnologies-47-million-funding-round-to-support-mrna-therapeutics-and-strengthen-europes-resilience-to-biological-threats/",
      "quote": "has invested in biotechnology startup Sensible Biotechnologies."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The transaction is attributed to Tech Horizons, the Presto-associated investment initiative linked from Presto Ventures' official website, rather than its earlier standalone funds."
  },
  {
    "id": "purple-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Rightcharge",
      "date": "2026-09-03",
      "date_precision": "day",
      "url": "https://tech.eu/2026/09/03/rightcharge-raises-ps500k-to-scale-fleet-ev-charging-payments-across-europe",
      "quote": "with participation from BlackWood Ventures and Purple Ventures"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Brno-based venture fund explicitly invests for minority equity stakes and is named in Rightcharge's latest dated funding announcement."
  },
  {
    "id": "reflex-capital",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Merchantee",
      "date": "2026-06-09",
      "date_precision": "day",
      "url": "https://startupkitchen.community/agentic-marketplace-intelligence-startup-merchantee-raises-e1-8m-to-expand-across-europe/",
      "quote": "a €1.8M round led by Reflex Capital, with support from Czech Founders VC and Lighthouse Ventures."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Prague-based venture investor is explicitly named as the lead investor in Merchantee's dated pre-seed round and extension announcement."
  }
]

Все 15 финальных цитат получены через curl и проверены grep; для Limerock — curl → pdftotext → grep. Использовал около 70 поисковых запросов и более 70 загрузок curl, включая проверки классификации, страниц портфолио и повторную проверку финальных цитат. Файлы не записывал, другие файлы репозитория не открывал, git не запускал. Важное ограничение: Presto/Tech Horizons — связанная, но переименованная инициатива; если требуется строго текущий отдельный менеджер Presto Ventures, эту запись лучше заменить подтверждённым standalone раундом, не приписывая ему Tech Horizons автоматически.

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Choice" "Presto Ventures" "March" "2026"'},{q:'"Zerops" "2026" "Presto Ventures" seed funding'}],response_length:"short"}));
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nfor u in ['https://www.caplight.com/company/choiceqr','https://www.caplight.com/company/zerops','https://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/']:\n r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True).stdout.decode(errors='replace');t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n print(u,[(m.group()) for m in re.finditer('.{0,100}(?:Presto Ventures|March 16|May 14|Orbit Capital|June 23).{0,180}',t)][:10])\nPY","max_output_tokens":1600}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Presto Ventures Portfolio Investments, Presto Ventures Funds, Presto Ventures Exits (https://www.cbinsights.com/investor/bohemia-venture-capital)\nciteturn81search0 [wordlim: 200] Crawled: today; Presto Ventures is a venture capital firm focusing on early-stage B2B software startups and online marketplaces. ... Their latest investment was in Choice as part of their Series A on March 16, 2026.\n## Presto Ventures Investments\n\n81 Investments\n\nPresto Ventures has made 81 investments. Their latest investment was in Choice as part of their Series A on March 16, 2026.\n\nImage: CBI Logo\n\n### Presto Ventures Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n3/16/2026  | Series A  | Choice  | $7.1M  | No  | Alea Capital Partners, J&T Ventures, Purple Ventures, Reflex Capital, and Smartlink Partners  | 3\n2/24/2026  | Pre-Seed  | The New Era of Shopping  | $1.4M  | Yes  | Alliance, Andreessen Horowitz, Cory Levy, Davidovs Venture Collective, Evgeny Yurtaev, Greg Tkachenko, Guillaume Roux-Romestaing, hi5 Ventures, Kacper Kielak, Matthieu Tissot, Nicole Buss, Quinn Campbell, Rokubunnoni, Typhon Ventures, Undisclosed Angel Investors, Urvit Goel, and Zituo Chen  | 1\n-------------------------------------------------
… [16502 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nfor u,q in [('https://venture5.com/vc-deals/zerops-raises-2m-seed-round/','with participation from Presto Ventures.'),('https://www.caplight.com/company/zerops','Presto Ventures Seed, Pre Seed'),('https://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/','with $6 million in new funding from Orbit Capital and Venture to Future Fund')]:\n r=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True).stdout.decode(errors='replace');t=re.sub(r'\\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',r,flags=re.S))))\n print(u,'grep',subprocess.run(['grep','-oF',q],input=t,capture_output=True,text=True).stdout);print(re.findall(r'datePublished.{0,80}|2026-06-23|May \\d{1,2}, 2026',r)[:5])\nPY","max_output_tokens":650}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"185dd0\",\"wall_time_seconds\":2.233874583,\"exit_code\":0,\"original_token_count\":154,\"output\":\"https://venture5.com/vc-deals/zerops-raises-2m-seed-round/ grep \\n[]\\nhttps://www.caplight.com/company/zerops grep Presto Ventures Seed, Pre Seed\\n\\n['May 14, 2026', 'May 14, 2026', 'May 15, 2026', 'May 14, 2026', 'May 14, 2026']\\nhttps://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/ grep with $6 million in new funding from Orbit Capital and Venture to Future Fund\\n\\n['2026-06-23', 'datePublished\\\":\\\"2026-06-23T16:02:27+02:00\\\",\\\"dateModified\\\":\\\"2026-08-12T10:37:39+02:00\\\",\\\"inLang', 'datePublished\\\":\\\"2026-06-23T16:02:27+02:00\\\",\\\"dateModified\\\":\\\"2026-08-12T10:37:39+02:00\\\"},{\\\"@typ', '2026-06-23']\\n\"}"}]
```
</details>

**Codex:**

[
  {
    "id": "presto-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Zerops",
      "date": "2026-05-14",
      "date_precision": "day",
      "url": "https://www.caplight.com/company/zerops",
      "quote": "Presto Ventures Seed, Pre Seed"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "Public transaction databases associate Presto with Zerops's May 2026 seed round, although contemporary reporting emphasizes Gi21 and describes Presto's earlier 2024 participation."
  },
  {
    "id": "orbit-capital",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Sloneek",
      "date": "2026-06-23",
      "date_precision": "day",
      "url": "https://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/",
      "quote": "with $6 million in new funding from Orbit Capital and Venture to Future Fund"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The company's dated announcement confirms Orbit's participation in its equity financing, independently of Orbit's separate debt strategy."
  }
]

## Thread `2026-10-11T06-13-30`

**Brief / message:**

You are an independent fact-checker. Work in /Users/[redacted]/homeW/ai-dev-test/investor-db, but read ONLY the file eval/second-opinion/input.json (a list of organisations: id, name, country, website). Do NOT open any other file in the repo (no data/, research/, PLAN.md) — your answers must be independent of an earlier assessment.

For each organisation answer, from public web sources you check yourself (use web search and curl):
1. is_investor: "yes" / "no" / "unclear" — does it invest its own or managed capital as equity (or convertible) into private companies, as a core activity? (Crowdfunding platforms, advisers, banks' lending, grant programs = "no".)
2. type: one of vc, pe, cvc, family_office, angel, private_investor, accelerator, fund_of_funds, public_dfi, platform, adviser, other.
3. managed_from: ISO country of the team/manager that makes the investment decisions.
4. latest_investment: the most recent DATED investment you can find: {company, date (YYYY-MM-DD, or YYYY-MM-01 / YYYY-01-01 if only month/year known), date_precision: day|month|year, url, quote}. The quote must be copied verbatim from the raw page text (fetch it with curl and check with grep) — not from a search snippet or a summary. If you can't find any, null.
5. active_36m: "yes" if latest_investment.date >= 2023-10-11, "no" if older, "unclear" if none found.
6. confidence: high / medium / low, and a one-sentence note.

Budget: about 6 searches per organisation; don't get stuck. Write the result to eval/second-opinion/codex.json as a JSON array (same order, include id). Write nothing else, run no git commands, don't mention tools or AI in the file. Print a 5-line English summary at the end (counts per is_investor and active_36m).

→ `exec`
```
text(await tools.exec_command({cmd:"cat eval/second-opinion/input.json",max_output_tokens:15000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"21c8f7\",\"wall_time_seconds\":0.000004584,\"exit_code\":0,\"original_token_count\":1403,\"output\":\"[\\n  {\\n    \\\"id\\\": \\\"365-fintech\\\",\\n    \\\"name\\\": \\\"365.fintech\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": \\\"https://365fintech.sk/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"air-ventures\\\",\\n    \\\"name\\\": \\\"Air Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"baryon-fund\\\",\\n    \\\"name\\\": \\\"Baryon Fund\\\",\\n    \\\"country\\\": null,\\n    \\\"website\\\": \\\"https://www.baryon.fund/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"bhm-ventures\\\",\\n    \\\"name\\\": \\\"BHM Ventures (BHM group)\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": null\\n  },\\n  {\\n    \\\"id\\\": \\\"cb-investment-management\\\",\\n    \\\"name\\\": \\\"CB Investment Management\\\",\\n    \\\"country\\\": \\\"SK\\\",\\n    \\\"website\\\": \\\"https://www.cbim.sk/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"credo-ventures\\\",\\n    \\\"name\\\": \\\"Credo Ventures\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.credoventures.com/\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"cs-seed-starter\\\",\\n    \\\"name\\\": \\\"ČS Seed Starter\\\",\\n    \\\"country\\\": \\\"CZ\\\",\\n    \\\"website\\\": \\\"https://www.see
… [6952 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Rockaway Ventures investment 2025 2026 latest'},{q:'RockawayX investment 2026 2025 venture'},{q:'Seed Starter Slovenskej sporiteľne investícia 2025 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "RockawayX announces the close of its new $125M crypto venture fund (https://www.rockawayx.com/insights/rockawayx-announces-the-close-of-its-new-125m-crypto-venture-fund)\nciteturn2search0 [wordlim: 200] Published: 1.5 years ago; Crawled: last month; 24 April 2025 – RockawayX, a global $2bn aum digital asset investment firm, today announced the launch of its second early-stage venture capital fund, closed in Q125 at $125 million, following an oversubscribed fundraising period.\n--------------------------------------------------------------------------------\nBratislava, 18. decembra 2025 Tri roky, sedem investícií, milióny v hre: Seed Starter mení slovenské inovácie na globálny biznis | Slovenská sporiteľňa (https://www.slsp.sk/sk/aktuality/2025/12/18/tri-roky-sedem-investicii-miliony-v-hre-seed-starter-meni-slovenske-inovacie-na-globalny-biznis)\nciteturn2search1 [wordlim: 200] Published: 9 months ago; Crawled: 3 weeks ago; Seed Starter Slovenskej sporiteľne za obdobie svojho fungovania potvrdil rolu najaktívnejšieho korporátneho venture kapitálového programu slovenského ekosystému. ... Najnovším a mimoriadne dôležitým projektom je aj Startup Report Slovensko 2025, ktorý Seed Starter a Slovenská sporiteľňa pripravili v spolupráci so SASK. ... Chceme startupy a slovenské inovácie podporovať dlhodobo a už teraz vieme, že rok 2026 bude pre nás rokom ďalšíc
… [26310 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Soulmates Ventures investment 2026 2025 latest'},{q:'Springtide Ventures investment 2026 2025 Czech'},{q:'STARTGUIDE investment venture latest Czech'},{q:'StartupYard investment 2025 2026 startup'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "STARTGUIDE – We’ll guide you onto the right path (https://startguide.cz/en/)\nciteturn4search0 [wordlim: 200] Crawled: 3 weeks ago; ## STARTGUIDE is a venture capital fund that invests with a hands‑on approach, bringing added value to investors, startups, and partners.### STARTGUIDE's unique approach combines financial investment with strategic mentorship and network access.At STARTGUIDE, we bring more than just capital to the table.\n# We empower digital startups to create value and drive positive change.\n\nEnterprenerues investing in early‑stage digital startups in the CEE region. We are bringing hands‑on unique value.\n  * # About us\n\n## STARTGUIDE is a venture capital fund that invests with a hands‑on approach, bringing added value to investors, startups, and partners.\n\n### STARTGUIDE's unique approach combines financial investment with strategic mentorship and network access.At STARTGUIDE, we bring more than just capital to the table. Our hands-on approach includes deep collaboration with startup founders on strategy, product-market fit, and scaling their business to achieve market leadership. Our investment philosophy goes beyond financial returns, prioritizing innovation, execution, and growth.We are a financial investor but for selected startups also provide mentoring (up to 160Hour/year).\n\n#### How?\n\n  * Vision & Strategy\nWe collaborate 
… [32255 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Tensor Ventures investment 2026 2025 latest'},{q:'Tilia Impact Ventures investment 2026 2025'},{q:'UP21 investment 2025 2026 latest'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Tilia Impact Ventures Portfolio Investments, Tilia Impact Ventures Funds, Tilia Impact Ventures Exits (https://www.cbinsights.com/investor/tilia-impact-ventures)\nciteturn7search0 [wordlim: 200] Crawled: today; After one of its 2025 finalists went on to raise €2.7M , Tilia Impact Ventures' flagship summer program is back, but this year opening its doors to even more promising founders across the region. ... 5/19/2026  | Series A  | FaceUp  | $5M  | No  | Fil Rouge Capital, Gi21 Capital, JIC Ventures, Jiri Hlavenka, Reflex Capital, Undisclosed Angel Investors, and Venture to Future Fund  | 5 ... Co-Investors  | Fil Rouge Capital, Gi21 Capital, JIC Ventures, Jiri Hlavenka, Reflex Capital, Undisclosed Angel Investors, and Venture to Future Fund  | Amino Collective, Credo, i&i Biotech Fund, Kaya VC, NAVEC Investment Management, and Undisclosed Angel Investors  | InvestEU, Undisclosed Angel Investors, Undisclosed Private Equity Investors, and Wirtschaftsagentur Wien  | Subscribe to see more  | Subscribe to see more\nThe company, which is developing a new type of electrolyzer for green hydrogen production, is now building a pilot. For impact founders across CEE, Turkey, and Greece, this is one of the few programs that offers direct investor access, charge and equity-free. Applications close July 28 at summer.tilia.vc. Share\n\nJun 17, 2026\n\nCEE Summer of Impac
… [29206 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"UP21" investment startup 2025 2024 2026'},{q:'Venture to Future Fund investment 2026 2025 latest'},{q:'Vision Ventures Slovakia investment 2026 2025 latest'},{q:'Y Soft Ventures investment 2026 2025 latest'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.0 seconds\nOutput:\n"}, {"type": "input_text", "text": "Y Soft Ventures Portfolio Investments, Y Soft Ventures Funds, Y Soft Ventures Exits (https://www.cbinsights.com/investor/y-soft-ventures)\nciteturn10search0 [wordlim: 200] Crawled: last week; Y Soft Ventures is a venture capital firm that invests in B2B technology startups within the hardware and software sectors. ... It is interested in startups that utilize technologies including the Internet of Things, Industry 4.0, Smart Office, Retail 2.0, Smart City, Cyber Security, Big Data & Analytics, and Augmented & Virtual Reality. ... Their latest investment was in Robotwin as part of their Pre-Seed on June 18, 2025. ... 6/18/2025  | Pre-Seed  | Robotwin  | $1.44M  | Yes  | BD Partners, EIT Manufacturing, and Joerg Dr.\n\nCorporate Venture\n\n# Y Soft Ventures\n\nFINANCE | Investment Firms & Funds\n\nysoft.com/ventures\n\n## Investments\n\n7\n\n## About Y Soft Ventures\n\nY Soft Ventures is a venture capital firm that invests in B2B technology startups within the hardware and software sectors. It provides services such as management assistance, financial support, and expertise in sales and marketing. It is interested in startups that utilize technologies including the Internet of Things, Industry 4.0, Smart Office, Retail 2.0, Smart City, Cyber Security, Big Data & Analytics, and Augmented & Virtual Reality. It was founded in 2014 and is based in Brno, Czech Re
… [31844 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Venture to Future Fund" "2026" investment'},{q:'"ZAKA" "2026" "investment" venture'},{q:'"Zero One Hundred" "2026" investment'},{q:'"0100 Ventures" latest investment 2025 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "Zero One Hundred Portfolio Investments, Zero One Hundred Funds, Zero One Hundred Exits (https://www.cbinsights.com/investor/zero-one-hundred)\nciteturn15search0 [wordlim: 200] Crawled: today; Zero One Hundred is a venture capital firm that focuses on Czech and Slovakian startup investments. ... Their latest investment was in BotBot as part of their Seed VC on January 01, 2026.\n## Zero One Hundred Investments\n\n41 Investments\n\nZero One Hundred has made 41 investments. Their latest investment was in BotBot as part of their Seed VC on January 01, 2026.\n\nImage: CBI Logo\n\n### Zero One Hundred Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n1/1/2026  | Seed VC  | BotBot  |  | Yes  |  | 1\n12/4/2025  | Seed VC  | Reno  | $4M  | Yes  | 500 Sanabil Investment, AngelSpark, Flyer One Ventures, Hub71, Plus VC, SandstormVC, and Swiss Founders Fund  | 2\n10/1/2025  | Unattributed VC  | Intellcre  |  | Yes  |  | 1\n3/12/2025  | Seed VC  | Subscribe to see more  | $XXM  | Subscribe to see more  | Subscribe to see more  | 10\n11/19/2024  | Series A - II  | Subscribe to see more  | $XXM  | Subscribe to see more  | Subscribe to see more  | 10\n\nDate  | 1/1/2026  | 12/4/2025  | 10/1/2025  | 3/12/2025  | 11/19/2024\nRo
… [24781 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-remix-a-technology-platform-for-circular-fashion','https://www.slsp.sk/sk/aktuality/2025/12/18/tri-roky-sedem-investicii-miliony-v-hre-seed-starter-meni-slovenske-inovacie-na-globalny-biznis','https://www.soulmatesventures.com/','https://springtide.cz/','https://startguide.cz/en/','https://up21.com/','https://visionventures.vc/','https://0100.vc/','https://zaka.vc/news/']\nfor u in urls:\n p=subprocess.run(['curl','-Ls','--max-time','30',u],capture_output=True,text=True)\n s=html.unescape(re.sub('<[^>]+>',' ',p.stdout));s=re.sub(r'\\s+',' ',s)\n out=subprocess.run(['grep','-oEi','.{0,110}(invest.{0,30}|2026|2025|portfolio|Prague|Bratislava|London).{0,150}'],input=s,capture_output=True,text=True).stdout\n print(u, '\\n',out[:7000])\n if 'soulmates' in u or 'springtide' in u or 'zaka' in u:print('LINKS',re.findall(r'href=[\\\"\\x27]([^\\\"\\x27]+)',p.stdout)[-100:])\nPY","max_output_tokens":15000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 7.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Warning: truncated output (original token count: 15415)\nTotal output lines: 1\n\n{\"chunk_id\":\"3102d9\",\"wall_time_seconds\":7.408599334,\"exit_code\":0,\"original_token_count\":15273,\"output\":\"Warning: truncated output (original token count: 15273)\\nTotal output lines: 176\\n\\nhttps://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-remix-a-technology-platform-for-circular-fashion \\n  Rockaway Ventures invests in Remix, a technology platform for circular fashion – Rockaway Capital Homepage About us Our team Our funds Legal information News Opportunities Contact Invest Invest Our funds \\nrs RockawayQ Our initiatives Rockaway Arts Rockaway Fund Open to new investors Explore Zpět Rockaway Ventures invests in Remix, a technology platform for circular fashion Rockaway Ventures December 19, 2025 • Rockaway PR Prague, December 19th 2025 – Rockaway Ventures is investing in Remix , one \\nof Europe’s largest players in second-hand e-commerce. As part of a Series A investment round, the fund is acquiring a 20% stake in the company. Operating across nine countries and serving a market of 194 million people, the startup is building infrastructure for\\nics platform, and develops advanced AI tools to manage a catalogue of more than one million unique items. The investment will support the further development of this infrastructure, as well as the c
… [40802 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site:rockawayventures.com 2026 invests'},{q:'site:soulmatesventures.com 2026 Antiverse investment'},{q:'"Springtide" "ThreatMark" "2024" investment'},{q:'"STARTGUIDE" investment startup funding'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "STARTGUIDE – We’ll guide you onto the right path (https://startguide.cz/en/)\nciteturn23search0 [wordlim: 200] Crawled: 3 weeks ago; ### STARTGUIDE's unique approach combines financial investment with strategic mentorship and network access.At STARTGUIDE, we bring more than just capital to the table.Our hands-on approach includes deep collaboration with startup founders on strategy, product-market fit, and scaling their business to achieve market leadership. ... We consider investment opportunities up to seed, and provide bridge funding as we believe this allows us to get in on the ground floor of promising startups and support their growth as they progress.\n# We empower digital startups to create value and drive positive change.\n\nEnterprenerues investing in early‑stage digital startups in the CEE region. We are bringing hands‑on unique value.\n  * # About us\n\n## STARTGUIDE is a venture capital fund that invests with a hands‑on approach, bringing added value to investors, startups, and partners.\n\n### STARTGUIDE's unique approach combines financial investment with strategic mentorship and network access.At STARTGUIDE, we bring more than just capital to the table. Our hands-on approach includes deep collaboration with startup founders on strategy, product-market fit, and scaling their business to achieve market leadership. Our investment philosophy go
… [31314 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site:soulmatesventures.com "Antiverse" "2026"'},{q:'"ThreatMark" "$23" "January" "2025"'},{q:'"Startguide" Ringil 2025 2024 investment'},{q:'"UP21" "Nutrition" "investment"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "ThreatMark Secures $23 Million to Advance the Fight Against Fraud (https://www.threatmark.com/newsroom/threatmark-to-advance-the-fight-against-online-fraud/)\nciteturn26search0 [wordlim: 200] Published: 1.8 years ago; Crawled: 3 weeks ago; January 7, 2025 by ThreatMark[London, UK, January 7] ThreatMark, a leading innovator in behavior-based fraud prevention, has successfully closed a $23 million funding round.\n\n# ThreatMark Secures $23 Million to Advance the Fight Against Fraud\n\nJanuary 7, 2025 by ThreatMark\n\n[London, UK, January 7] ThreatMark, a leading innovator in behavior-based fraud prevention, has successfully closed a $23 million funding round.\n\nThe round includes $15 million from Octopus Ventures, one of the largest and most active venture capital investors in the UK and Europe, and Riverside Acceleration Capital (RAC), a US-based growth capital partner to B2B software companies, and an $8 million convertible note from Springtide Ventures Fund. Known for their extensive B2B Software expertise, Octopus Ventures’ and RAC’s equal contributions to the investment round, combined with the continued support from Springtide Ventures Fund, underscore a successful year for ThreatMark and highlights the strong confidence from investors in its mission to combat digital fraud.\n\n## New Partnership to Fuel Innovation\n\nThe $23 million combined investme
… [31817 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://www.soulmatesventures.com/','https://blog.tensor.ventures/archive','https://zaka.vc/news/','https://up21.com/','https://www.springtide.cz/news/','https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/']\nfor u in urls:\n p=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\n print(u)\n if 'up21' in u:print(html.unescape(re.sub('<[^>]+>',' ',p))[-6500:])\n else:\n  links=re.findall(r'href=[\\\"\\x27]([^\\\"\\x27]+)',p)\n  print('\\n'.join(x for x in links if any(w in x.lower() for w in ['antiverse','2026','cnuic','wultra','sensible','edmund','quant','batch-15','investment','newsroom'])))\nPY","max_output_tokens":5000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"ff8cd2\",\"wall_time_seconds\":3.2993274169999998,\"exit_code\":0,\"original_token_count\":1468,\"output\":\"https://www.soulmatesventures.com/\\nhttps://www.soulmatesventures.com/your-cheatsheet-to-greenhack-2026/\\nhttps://www.soulmatesventures.com/rigour-as-strategy-sustainable-investment/\\nhttps://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/\\nhttps://www.soulmatesventures.com/where-venture-capital-meets-sustainability-our-article-9-sfdr-investment-strategy/\\nhttps://www.soulmatesventures.com/soulmates-ventures-leads-investment-in-the-british-edtech-startup-transforming-how-children-engage-with-science-and-technology/\\nhttps://www.soulmatesventures.com/we-have-tripled-our-investment-in-eagronom-we-aim-to-catch-a-unicorn-this-year-says-hynek-sochor/\\nhttps://www.soulmatesventures.com/up-to-60-of-investment-in-climate-tech-flows-into-mobility-yet-this-sector-produces-only-16-of-emissions-industry-is-the-biggest-emitter-with-31/\\nhttps://www.soulmatesventures.com/how-can-investors-improve-their-investment-decisions-based-on-esg-concept/\\nhttps://www.soulmatesventures.com/case/antiverse/\\nhttps://www.soulmatesventures.com/event/prague-climate-week-2026/\\nhttps://www.soulmatesventures.com/event/london-tech-week-2026/\\nhttps://www.soulmatesventures.com/event/swiss-biotech-day-2026/\\nhttps://www.soulmatesventure
… [4759 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Vision Ventures" Slovakia "investment" "2023" December'},{q:'"UP21" investment Spaceflow Nutritionpro 2020'},{q:'"Seed Starter" "Pointee" "2026"'},{q:'"FaceUp" "2026" "Tilia" investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "FaceUp Raises $5M Series A for Ethics & Compliance Platform (https://www.faceup.com/en/blog/series-a)\nciteturn32search0 [wordlim: 200] Published: 4 months ago; Crawled: last month; 2026-05-19 ... The raise also included strong participation from returning investors, Tilia Impact V entures (supported by the InvestEU Fund) and Reflex Capital, alongside a group of angel investors and employees, demonstrating their continued confidence in FaceUp’s growth. ... > “FaceUp’s transition of compliance from a mere checkbox into a proactive, real-time AI system perfectly aligns with our investment thesis at Gi21 Capital.\n\n# FaceUp Raises $5 Million Series A\n\nPublished\n\n2026-05-19\n\nReading time\n\n5 min\n\n\n# FaceUp Raises $5 Million Series A to Turn Compliance from a “Checkbox” into a Real-Time Ethics & Compliance System\n\nTrusted by 3,600+ organizations like Mercedes-Benz and Zendesk, FaceUp helps companies move from reactive reporting to proactive risk prevention\n\nCHARLESTON, S.C. — May 19, 2026 — Companies have spent years treating compliance as a checkbox, something to satisfy regulators after issues arise. That model is changing. FaceUp, a leading secure Ethics & Compliance platform for mid-size and enterprise companies, today announced it has raised $5 million in Series A funding to help organizations surface and resolve issues before they escalate.
… [30618 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/','https://blog.tensor.ventures/p/wultra-raises-68m-to-make-finance','https://zaka.vc/sensible-biotechnologies-raises-47m-why-we-backed-them-early-and-why-its-personal-for-us/','https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/','https://www.threatmark.com/newsroom/threatmark-to-advance-the-fight-against-online-fraud/','https://blog.tensor.ventures/p/portfolio-news-pointee-raises-14m','https://www.faceup.com/en/blog/series-a']\nfor u in urls:\n p=subprocess.run(['curl','-Ls','--max-time','25',u],capture_output=True,text=True).stdout\n p=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',p,flags=re.S)\n s=html.unescape(re.sub('<[^>]+>',' ',p));s=re.sub(r'\\s+',' ',s)\n print(u);print(subprocess.run(['grep','-oEi','.{0,90}(2026|2025|invest.{0,20}|participat.{0,15}|July|March|April).{0,180}'],input=s,capture_output=True,text=True).stdout[:4800])\nPY","max_output_tokens":10000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 4.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"d6ecd7\",\"wall_time_seconds\":4.294814833,\"exit_code\":0,\"original_token_count\":5186,\"output\":\"https://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/\\nive disease targets in medicine.” This is why we led the $9.3M Series A other experienced investors. Antiverse’s technology brings a radical, if not disruptive shift in the entire economics and structure of antibody drug development. The cost and time efficiency is already immense. And this is o\\n of clinical drug development fails and how to improve it? – Acta Pharmaceutica Sinica B, July 2022. https://www.sciencedirect.com/science/article/pii/S2211383522000521 Antiverse and the Cystic Fibrosis Foundation to Identify Nanobodies for ‘Undruggable’ Target – GEN Edge, \\nJanuary 2025. https://journals.sagepub.com/doi/10.1089/genedge.7.1.050?icid=int.sj-full-text.similar-articles.8 Antibody Discovery Market Size to Surpass USD 20.4 BN by 2034 – BioSpace, Januar\\ny 2025. https://www.biospace.com/press-releases/antibody-discovery-market-size-to-surpass-usd-20-4-bn-by-2034-fueled-by-precision-medicine-and-biotech-innovation Share Journal Blog Found\\nhat it actually takes to operate a decade ahead of the market, navigate an uncompromising investor search, and build the visual command center for tomorrow's autonomous \\\"dark factories.\\\" Blog Another Angle: Tatiana Bo
… [19456 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Soulmates" "Antiverse" "March" "2026"'},{q:'"UP21" "invested" "Spaceflow" date'},{q:'"Vision Ventures" "2023" "December" investment Slovakia'},{q:'"Robotwin" "Y Soft" "2025"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "Spaceflow Stock Price, Funding, Valuation, Revenue & Financial Statements (https://www.cbinsights.com/company/spaceflow/financials)\nciteturn42search0 [wordlim: 200] Crawled: last week; Date  | Round  | Amount  | Investors  | Valuation Valuations are submitted by companies, mined from state filings or news, provided by VentureSource, or based on a comparables valuation model. ... Hydda invested in Spaceflow's Acquired funding round. ... 00/00/0000  | 00/00/0000  | UP21  | Subscribe to see more  |  | Incubator/Accelerator  | Czech Republic\nRound  | Acquired  | Incubator/Accelerator  | Series A  | Seed VC  | Seed\nAmount  |  |  | $XXM  | $XXM  | \nInvestors  | Hydda  | Subscribe to see more  | Subscribe to see more  | Subscribe to see more  | Subscribe to see more\nValuation  | $XXM  | $XXM  | $XXM  | $XXM  | $XXM\nRevenue  | 0 FY undefined  | 0 FY undefined  | 0 FY undefined  | 0 FY undefined  | 0 FY undefined\nSources  | 2  | 10  | 10  | 10  | 10\n\n## Spaceflow Investors\n\n5 Investors\n\nSpaceflow has 5 investors. Hydda invested in Spaceflow's Acquired funding round.\n\nFirst funding  | Last Funding  | Investor  | Rounds  | Board Seats  | Type  | Location\n--- | --- | --- | --- | --- | --- | ---\n5/23/2022  | 3/15/2026  | Hydda  | 2 Series A, Acquired (2026)  |  | Holding Company  | Sweden\n00/00/0000  | 00/00/0000  | Future of Mobility Accelerator Prog
… [29235 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'site:visionventures.vc "2023" investment'},{q:'"Vision Ventures" "investment" "BiteBerry" 2023'},{q:'"UP21" Nutritionpro investment 2022 2021'},{q:'"Sloneek" "2026" "Venture to Future Fund"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "Sloneek raises $6 million in new funding | Sloneek (https://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/)\nciteturn43search0 [wordlim: 200] Published: 3 months ago; Crawled: 2 weeks ago; # Sloneek raises $6M to give HR a smarter way to work ... And with $6 million in new funding from Orbit Capital and Venture to Future Fund, we get to close it a lot faster.\n\n# Sloneek raises $6M to give HR a smarter way to work\n\nMilan Rataj\n\n23. 6. 2026 2 min read\n\nImage: Sloneek Investment\n\nA lot of HR work begins with questions that sound simple enough.\n\nCan we afford a new hire? Why is this department suddenly overloaded? Is this team member ready to grow into a bigger role? \n\nGetting to the answer is rarely as simple as the question. The context is often spread across multiple systems, documents, and the kind of company knowledge that never fits neatly into one field. For HR to get the job done, it usually means a lot of going back and forth between people, waiting for replies, and piecing the full picture together by hand.\n\nClosing the gap between a simple question and a hard-to-find answer is exactly what Sloneek is built for. And with $6 million in new funding from Orbit Capital and Venture to Future Fund, we get to close it a lot faster. 🫶\n\n## Here’s what that money actually buys HR teams\n\n### Sloneek Intelligence: Ma
… [26127 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Zero One Hundred" "BotBot" investment'},{q:'"Vision Ventures" "November 10" "2023"'},{q:'"Airline Pilot Club" "Startguide" investment 2024'},{q:'"ZAKA" "FinalDose" investment 2026'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "StartGuide Portfolio Investments, StartGuide Funds, StartGuide Exits (https://www.cbinsights.com/investor/startguide)\nciteturn44search0 [wordlim: 200] Crawled: 4 weeks ago; ## StartGuide Investments ... Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024.\n\n# StartGuide\n\nstartguide.cz\n\n## Are you an investor?\n\nSubmit your portfolio details now to be considered in our investor rankings.\n\nSubmit portfolio details\n\n## Investments\n\n16\n\n## Portfolio Exits\n\n1\n\n## About StartGuide\n\nStartGuide is a Czech incubator. It was founded in 2021 and is based in Praha, Czech Republic.\n\n## Headquarters Location\n\nKarla Engliše 3201/6 Smíchov\n\nPraha, 150 00,\n\nCzech Republic\n\n\n## StartGuide Investments\n\n16 Investments\n\nStartGuide has made 16 investments. Their latest investment was in Airline Pilot Club as part of their Pre-Seed on November 30, 2024.\n\nImage: CBI Logo\n\n### StartGuide Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n11/30/2024  | Pre-Seed  | Airline Pilot Club  | $0.7M  | Yes  |  | \n11/20/2024  | Pre-Seed  | CloseRocket  | $1M  | Yes  |  | \n8/13/2024  | Seed  | ArtMaster  | $1M  | Yes  |  | 1\n8/1/2024  | Pre-Seed  | Subscribe 
… [28198 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nu='https://zaka.vc/news/'\np=subprocess.run(['curl','-Ls',u],capture_output=True,text=True).stdout\nprint([x for x in re.findall(r'href=[\\\"\\x27]([^\\\"\\x27]+)',p) if 'perfectbit' in x])\nurls=['https://blog.tensor.ventures/p/new-investment-cnuic-raises-3m-to','https://www.cbinsights.com/investor/startguide','https://www.cbinsights.com/company/nutritionpro/financials','https://www.cbinsights.com/investor/zero-one-hundred','https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund','https://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/']\nfor u in urls:\n p=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout\n p=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',p,flags=re.S)\n s=html.unescape(re.sub('<[^>]+>',' ',p));s=re.sub(r'\\s+',' ',s)\n print(u); print(subprocess.run(['grep','-oEi','.{0,80}(2026|2025|2023|invest.{0,15}|acquir.{0,15}|January|April|August|November).{0,150}'],input=s,capture_output=True,text=True).stdout[:4000])\nPY","max_output_tokens":8500
… [5 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 2.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"289833\",\"wall_time_seconds\":2.488647792,\"exit_code\":0,\"original_token_count\":1669,\"output\":\"['https://zaka.vc/perfectbit-building-the-verified-data-layer-for-physical-ai/']\\nhttps://blog.tensor.ventures/p/new-investment-cnuic-raises-3m-to\\n 🤗 New Investment: Cnuic Raises $3M to Rethink How Photonic Chips Are Made Tensor Ventures Subscribe Sign in 🤗 New Investment: Cnuic Raises $3M to Rethink How Photonic Chips Are \\nMade Tensor Ventures Apr 28, 2026 1 Share The semiconductor industry has run the same basic playbook for sixty years. Photolithography — the process of etching circuit patterns onto c\\nrlative. The round was oversubscribed — a signal of how seriously the deep tech investment community is taking both the technology and the team behind it. Why This Matters Now The AI infrastructure buildout has made the economics of photonic chips new\\ncessors. Photonic interconnects eliminate that bottleneck. For the hyperscalers investing hundreds of billions in AI compute, the savings from switching to photonic infrastructure at scale are not marginal. They are structural. But the promise of phot\\n computing power.” Martin Drdúl, co-founder of Tensor Ventures, who oversaw the investment alongside Ondřej, adds: “From a deep tech perspective, this is a completely new technology and a major breakthrough that could mean a whole new rol
… [5446 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw1eCrut9uuXVMGo2BhTZru-vJNbcwpsW5L_bIRRmsNjaxpzjXAkkSpfe9fQ69Sl2WcCd9EXF6tzFZrU5B21dtJt-_7rJ7clPa7aVhn6UGOU0TwKYztFFwVvE-10vyeElavBrHR5qp5og3G2IhdVZsADkdRfzRSEBjF2mMzpEuxpPciylYqCMrkcCC6YAtuI9Ij7KViZZD1Bbk852ZkuUVggdAuhl6qEouJGaR21q944UUD-8HFUM5itXiaaa2NsmCt9ZpzAwZP_Qbj8jMuD9PuQuPab34UltwQ5ThYts3ty54elp07Mw9eWi7WZohn9MIRqLz_j-hrOfDrviRPwU6ns_cVaYvtu34LALWq_BtwxL2HR0SM33RCOAr7mawzoNx9pty47a9SHbCu3FklRCtzj5uttUmicLZOsXT604GYrCuB-ZUh22Z5WOa1VCxflhpOp_Ol1c-38bdAEGgvDNvm2_ZCQKoxyCV9NkE_tJMKb9fytdzWIbqa0aJ9l-nQabjPKFONGuzA-7yPLVMcyAlSQA_UFV7RiNGgQUCUk3ktOMWXFuWIb6UTq7j51j8t92op-2q7-r320Y8hbI90_lDeKE7Vt9FXh5MoZmF56g1UHAUnzYDb5FluUFOK7GItlhFxE9PZoMXOWJkR-PpenWlsE-5HcgIqpGzK4WRzsPEb4n3k_UEFOJZTrQ5lY1qSAtjjQreUUmCTAmNaaSyDDVL_7Df_bWiMn8G52IM5ucv_4G7F-Rbm4EYYKOOCzMGnyrlta3mymhxNVVu660fktM02dkXwhj1FcWXkVyARXrRJNMTSZV_0w5OG7NDbx0tcfanLn"}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Startguide" "ArtMaster" "2024"'},{q:'"UP21" "NutritionPro" "2023" investment'},{q:'"Vision Ventures" "Futu" "November" "2023"'},{q:'"Zero One Hundred" "Reno" "December" "2025"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.7 seconds\nOutput:\n"}, {"type": "input_text", "text": "US Angel Investors Portfolio Investments, US Angel Investors Funds, US Angel Investors Exits (https://www.cbinsights.com/investor/us-angel-investors)\nciteturn49search0 [wordlim: 200] Crawled: 3 days ago; Their latest investment was in Nutritionpro as part of their Seed VC - II on June 01, 2023. ... 6/1/2023  | Seed VC - II  | Nutritionpro  | $3M  | Yes  | LEVERAGE, Lighthouse Ventures, Nation 1, and UP21  |\nSecuring funding often takes time and setbacks are common. Giving up too easily can hinder your ability to secure the funding necessary for your startup’s growth.\n\n## US Angel Investors Investments\n\n5 Investments\n\nUS Angel Investors has made 5 investments. Their latest investment was in Nutritionpro as part of their Seed VC - II on June 01, 2023.\n\nImage: CBI Logo\n\n### US Angel Investors Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n6/1/2023  | Seed VC - II  | Nutritionpro  | $3M  | Yes  | LEVERAGE, Lighthouse Ventures, Nation 1, and UP21  | \n10/16/2022  | Angel  | Subscribe to see more  |  | Subscribe to see more  |  | 0\n4/26/2022  | Angel - II  | Subscribe to see more  | $XXM  | Subscribe to see more  |  | 0\n11/25/2021  | Angel  | Subscribe to see more  | $XXM  | Subscribe to see more  
… [26144 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Startguide ArtMaster million funding August 2024'},{q:'"Vision Ventures" "2023" "investícia" November'},{q:'"0100" "BotBot" investment 2026'},{q:'"StartupYard" "Teamsharq" investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "StartupYard — Investment Thesis, Check Size & Team | Fundraising Fox (https://fundraisingfox.com/investors/startupyard)\nciteturn52search0 [wordlim: 200] Crawled: last week;   * 2nd- and 3rd-degree connections: people you know who worked, studied or invested with the StartupYard team ... ## Investment thesis ... Carebot CaseLens DishBoard Fungies Gjirafa InvestBay Neuron Soundware Personeo Retino Rossum Teamsharq Ydoca\n\nCloud Computing Developer Tools SaaS\n\nCo-investorsTETensor Ventures\n\nTEImage\n\nTeskalabsteskalabs.comin𝕏\n\nTeskaLabs develops SIEM, log management, and PKI cybersecurity solutions for enterprise mobile applications.\n\nCybersecurity Enterprise Software IoT London, GB\n\nATAles Teskain\n\nCo-investorsTETechstarsCRCredo VenturesTETechstars London 2016\n\nOther\n\nTracked investments with no reachable website or further public details — typically companies that wound down, renamed, or were absorbed.\n\nCarebot CaseLens DishBoard Fungies Gjirafa InvestBay Neuron Soundware Personeo Retino Rossum Teamsharq Ydoca\n\n## Frequently asked questions\n\nHow many investments has StartupYard made?\n    StartupYard has 17 tracked investments.\n\nWhat stage does StartupYard invest at?\n    StartupYard invests at the Pre-Seed, Seed stages.\n\nWhat sectors does StartupYard focus on?\n    StartupYard focuses on AI & Machine Learning, Cybersecurity, De
… [29060 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"ArtMaster" "StartGuide" funding'},{q:'"CloseRocket" "StartGuide" investment'},{q:'"Vision Ventures" "Futu" investment 2023 November'},{q:'"BotBot" "Zero" investment funding'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "Zero One Hundred Portfolio Investments, Zero One Hundred Funds, Zero One Hundred Exits (https://www.cbinsights.com/investor/zero-one-hundred)\nciteturn53search0 [wordlim: 200] Crawled: today; Zero One Hundred Launches Fund II and Expands Portfolio ... CEE VC Zero One Hundred Signs Agreement to Connect CEE Startups with UAE Investors ... Their latest investment was in BotBot as part of their Seed VC on January 01, 2026.\n## Zero One Hundred Investments\n\n41 Investments\n\nZero One Hundred has made 41 investments. Their latest investment was in BotBot as part of their Seed VC on January 01, 2026.\n\nImage: CBI Logo\n\n### Zero One Hundred Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n1/1/2026  | Seed VC  | BotBot  |  | Yes  |  | 1\n12/4/2025  | Seed VC  | Reno  | $4M  | Yes  | 500 Sanabil Investment, AngelSpark, Flyer One Ventures, Hub71, Plus VC, SandstormVC, and Swiss Founders Fund  | 2\n10/1/2025  | Unattributed VC  | Intellcre  |  | Yes  |  | 1\n3/12/2025  | Seed VC  | Subscribe to see more  | $XXM  | Subscribe to see more  | Subscribe to see more  | 10\n11/19/2024  | Series A - II  | Subscribe to see more  | $XXM  | Subscribe to see more  | Subscribe to see more  | 10\n\nDate  | 1/1/2026  | 12/4/2025 
… [29874 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://zaka.vc/perfectbit-building-the-verified-data-layer-for-physical-ai/','https://www.vcbacked.co/company/cultureboard','https://www.vcbacked.co/company/airline-pilot-club','https://www.vcbacked.co/company/nutritionpro','https://www.0100.vc/','https://www.rockawayx.com/insight-categories/news','https://startupyard.com/meet-caselens-the-ai-specialized-in-complex-disputes/']\nfor u in urls:\n p=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout\n print(u,'DATES',re.findall(r'datePublished.{0,60}',p)[:2])\n p=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',p,flags=re.S)\n s=html.unescape(re.sub('<[^>]+>',' ',p));s=re.sub(r'\\s+',' ',s)\n print(subprocess.run(['grep','-oEi','.{0,70}(2026|2025|2024|2023|invest.{0,12}|funding|acquir.{0,10}|April|December).{0,140}'],input=s,capture_output=True,text=True).stdout[:3500])\nPY","max_output_tokens":7500}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 3.4 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"6d4342\",\"wall_time_seconds\":3.217516708,\"exit_code\":0,\"original_token_count\":2692,\"output\":\"https://zaka.vc/perfectbit-building-the-verified-data-layer-for-physical-ai/ DATES ['datePublished\\\":\\\"2026-08-18T12:31:58+00:00\\\",\\\"dateModified\\\":\\\"2026-08-18T12:', 'datePublished\\\":\\\"2026-08-18T12:31:58+00:00\\\",\\\"dateModified\\\":\\\"2026-08-18T12:']\\nor Physical AI - ZAKA VC Skip to content Home About Team Portfolio Co-Investors News Jobs Contact Submit pitch deck Submit pitch deck Home About Team Portfolio Co-Investors News Jobs Contact E-mail is copied PerfectBit: Building\\n Francisco startup that recently graduated from Y Combinator’s Spring 2026 batch , develops verified multimodal datasets and reinforcement learning environments for frontier AI models. Rather than relying on tradit\\nof AI infrastructure.” Jan Kasper, Managing Partner at ZAKA VC Why we invested PerfectBit combines several characteristics we rarely see together at such an early stage: a technically ambitious problem, a differentiated approach\\narly validation from both customers and the broader AI community. The funding round was oversubscribed and included Y Combinator , alongside angel investors from OpenAI, Anthropic, DeepMind and Meta . Building more ca\\non Valley / London / Prague / Bratislava Home About Team Portfolio Co-Investors News Job
… [9665 more characters]
```
</details>

→ `send_message`
```
{"target":"/root","message":"gAAAAABqyw2GGSFZqtvzXRxHNeggE8bH5CEV-gwfX6Op5-UOLb27edH87fB4CicS62DDXS86RCamsulpcMHhMzbwLupL6GU26sidT_NbRf4HsiyQgQS1SbAYaqlbVFLCRWD5k_dDqnOrNpjPzEM7py1NQ2laMrqJdgBdmzO5tMUNhvDwj027XJ_xwtC8ldhi5-ugMJe4_UI5RYZGLGtQJMMIIEkW1VmVeJrdAZr8Ciw5fzUjj7Uut-wbQs2j-Lhw8kSRkXoJ0RIkXchgCmo5__9hzXpAKkrGgoL3hY5Z9wUJ5Kvr3ePmFZVHeATkI5IsEpB4bwSuK5-aF62kadbhwhHTXhfveGcCxpyuKTMqWbAq-VB7EdioM7igezqaBhd-Fsu881dn4biyDDBmEAbhjB_xvUeygkWfDgD-39YLQioN5dI3pVcf7Laxm_o4qYxsj5j86b_rzw96DURyDY2R1qked2brACNaJnuGgo4SaQ6iWGbbm1YoygmgcTTVRl3fFy3GlQ6lC6hkgLYK0nq67GKWrZ2yhi095u51tNPQHMCPFxOHbhhN1ARBbG2KCBC7eDkPFAoEF022uRgQaXUnXXz-OuBG_m2yQJNCMwd5_iDiWUwc9Z1mjW6vXcTGpCXHLlhQf8O28JLdGnGNHCOK2lFTf_JIbvSFGRYFnAa0tJZ_iyLmGz32B7zAOUU_LQVrhgYTdRM9NHrFVOuca6eL8Da7Iyax1wHdJdEbz8fYDbhlDo0CaTGKfv6MjXMREWtZS7nXN3Jc4X2l1Hdpl2T966p5Bnx-32bR8amfJUtd6TsfTLU-DqCgM6YptKJCGRaopCZZ5VfvLnIC4dS5GQ4rgp0rk883VzQqpxEOOS7HuXkhuB7Bu2Zb7bZw1B8GQMIRz35cReqH32MgwcyENOYDDKGYNwrPFzED1g=="}
```

<details><summary>result</summary>

```

```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Reno" "$4 million" "Zero" December 2025 funding'},{q:'"Cultureboard" "Vision Ventures" investment'},{q:'"Airline Pilot Club" "Start" investment November'},{q:'"ArtMaster" "milion" "2024" investice'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.6 seconds\nOutput:\n"}, {"type": "input_text", "text": "UAE's Reno raises $4 million in equity-debt round - ومضة (https://www.wamda.com/ar/2025/12/uae-reno-raises-4-million-equity-debt-round)\nciteturn61search0 [wordlim: 200] Published: 10 months ago; Crawled: today; News • 04 December, 2025 ...   * UAE-based home renovation tech platform Reno has raised $4 million in equity and debt, led by Sanabil 500, Hub71, Plus VC, Zero 100 VC, FlyerOne Ventures, Sandstorm VC, AngelSpark and Swiss Founders Fund. ... Reno, the region’s leading tech-driven renovation platform, has secured $4 million, in a mix of equity and debt, in funding to scale its mission of building the region’s first end-to-end operating system for renovations.\n\n## UAE's Reno raises $4 million in equity-debt round\n\nNews • 04 December, 2025\n\nImage: UAE's Reno raises $4 million in equity-debt round\n\n  * UAE-based home renovation tech platform Reno has raised $4 million in equity and debt, led by Sanabil 500, Hub71, Plus VC, Zero 100 VC, FlyerOne Ventures, Sandstorm VC, AngelSpark and Swiss Founders Fund.\n  * Founded in 2024 by Marc Michel, Amr Hosny and Farah Karabeg, Reno is the all-in-one, end-to-end interior design and renovation platform for residential and commercial projects.\n  * With this investment, Reno plans to expand its footprint across the GCC, scale its technology capabilities, and continue refining the renovation experience.\n\n
… [30798 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nurls=['https://cc.cz/jsou-mu-jen-dva-roky-ale-mezi-klienty-ma-disney-nike-ci-metu-pomaha-jim-s-firemni-kulturou/','https://www.wamda.com/ar/2025/12/uae-reno-raises-4-million-equity-debt-round','https://www.novalia.cz/blogpost/novalia-zastupovala-robotwin-cesky-startup-ktery-meni-budoucnost-prumyslove-automatizace','https://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/','https://www.spaceflow.io/blog/spaceflow-raises-18m-for-its-scalable-tenant-experience-platform','https://zaka.vc/perfectbit-building-the-verified-data-layer-for-physical-ai/']\nfor u in urls:\n p=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout\n print(u,'DATE',re.findall(r'datePublished.{0,70}',p)[:1])\n p=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',p,flags=re.S)\n s=html.unescape(re.sub('<[^>]+>',' ',p));s=re.sub(r'\\s+',' ',s)\n print(subprocess.run(['grep','-oEi','.{0,30}(2024|2025|Vision Ventures|Zero 100|we invested|UP21|Y Soft Ventures|led the \\$9).{0,210}'],input=s,capture_output=True,text=True).stdout[:2200])\nPY","max_output_tokens":5000}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 4.8 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"a91de8\",\"wall_time_seconds\":4.606932792,\"exit_code\":0,\"original_token_count\":1878,\"output\":\"<stdin>:8: SyntaxWarning: \\\"\\\\$\\\" is an invalid escape sequence. Such sequences will not work in the future. Did you mean \\\"\\\\\\\\$\\\"? A raw string is also an option.\\nhttps://cc.cz/jsou-mu-jen-dva-roky-ale-mezi-klienty-ma-disney-nike-ci-metu-pomaha-jim-s-firemni-kulturou/ DATE ['datePublished\\\":\\\"2024-04-05T13:59:00+02:00\\\",\\\"dateModified\\\":\\\"2024-04-05T13:59:00+02:0']\\n Newsletter Startupy – 05. 4. 2024 – 2 min čtení Jsou mu jen dva roky, ale mezi klienty má Disney, Nike či Metu. Pomáhá jim s firemní kulturou Startup CultureBoard po vstupu na trh rychle oslovil největší globální značky. Od investorů teď získá\\nvestuje: Slovenská společnost Vision Ventures posílá 400 tisíc eur (10 milionů korun) jako navazující částku k takzvanému pre-seed kolu z loňska , kdy tento fond investoval 200 tisíc eur (pět milionů korun). Kolik již startup získal celkem: Dohromady jde \\n3 milionů korun), které kromě Vision Ventures v průběhu času poskytl partner Presto Ventures Vojta Roček , Jinej Fond Jiřího Hlavenky a Jana Slámy a Klára Losert ze startupu Talkbase. Co startup dělá: Vyvíjí soubor modulů pro HR manažery s cílem zlepšovat\\ni (CC+) . Související témata: Vision Ventures CultureBoard Sdílet článek Přejít do diskuze Nejčteněj
… [6172 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'"Ringil" "Startguide" 2023 investment'},{q:'"Startguide" "Airline" "2024" investment'},{q:'"Startguide" "ArtMaster" million'},{q:'"StartGuide" Carebot "2024" investment'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "Karel Bastl Portfolio Investments, Karel Bastl Funds, Karel Bastl Exits (https://www.cbinsights.com/investor/karel-bastl)\nciteturn67search0 [wordlim: 200] Crawled: 3 weeks ago; Their latest investment was in Carebot as part of their Seed VC on March 22, 2024. ... 3/22/2024  | Seed VC  | Carebot  | $1.3M  | Yes  | BHM Group, Eva Janeckova, Gain Ventures, Lukas Kopcaj, Pilulka Lab, Roman Trachta, and StartGuide  | 2\n\nAngel Investor (Individual)\n\n# Karel Bastl\n\n## Investments\n\n1\n\n## About Karel Bastl\n\nKarel Bastl is an angel investor and is based in Prague, Czech Republic.\n\n## Headquarters Location\n\nPrague,\n\nCzech Republic\n\n## Karel Bastl Investments\n\n1 Investments\n\nKarel Bastl has made 1 investments. Their latest investment was in Carebot as part of their Seed VC on March 22, 2024.\n\n### Karel Bastl Investments Activity\n\nImage: investments chart\n\n[Button: View Investments Chart]\n\nDate  | Round  | Company  | Amount  | New?  | Co-Investors  | Sources\n--- | --- | --- | --- | --- | --- | ---\n3/22/2024  | Seed VC  | Carebot  | $1.3M  | Yes  | BHM Group, Eva Janeckova, Gain Ventures, Lukas Kopcaj, Pilulka Lab, Roman Trachta, and StartGuide  | 2\n\nDate  | 3/22/2024\nRound  | Seed VC\nCompany  | Carebot\nAmount  | $1.3M\nNew?  | Yes\nCo-Investors  | BHM Group, Eva Janeckova, Gain Ventures, Lukas Kopcaj, Pilulka Lab, Roman Trachta, 
… [27191 more characters]
```
</details>

→ `exec`
```
text(await tools.web__run({search_query:[{q:'Carebot "2026" "Startguide" investice'},{q:'Carebot "1,5" "Startguide" investice'},{q:'"UP21" "NutritionPro" "2023" "investuje"'}],response_length:"long"}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 1.3 seconds\nOutput:\n"}, {"type": "input_text", "text": "Pár dní v roli GP ve StartGuide VC a už si připisuju zásluhy za investici, kterou vyjednal někdo jiný. Klasický VC move. 😄 Ale vážně — Carebot je přesně ten typ firmy, kvůli kterému jsem do toho… | Lukáš Vácha (https://cz.linkedin.com/posts/luk%C3%A1%C5%A1-v%C3%A1cha-63343b8_p%C3%A1r-dn%C3%AD-v-roli-gp-ve-startguide-vc-a-u%C5%BE-si-activity-7491510920091742209-3LTp)\nciteturn70search0 [wordlim: 200] Crawled: last month; Jsme rádi, že jako jeden z investorů můžeme být součástí příběhu Carebotu, českého healthtech startupu od Matěje Misaře a Daniela Kvaka, který právě uzavřel investiční kolo přes 1,5 milionu eur a k tomu představil nové AI řešení pro mamografii. ... 🙂 #VC #healthtech #AI #investments #startupy #carebot #Startguide #SGTwo\n\n# Příspěvek uživatele Lukáš Vácha\n\nLukáš Vácha\n\nGeneral Partner\n\n1 t.\n\nPár dní v roli GP ve StartGuide VC a už si připisuju zásluhy za investici, kterou vyjednal někdo jiný. Klasický VC move. 😄 Ale vážně — Carebot je přesně ten typ firmy, kvůli kterému jsem do toho šel. AI, která při mamografii pomáhá radiologům odhalit i to, co by jinak přehlédli. Přes 4,5 milionu analyzovaných snímků, nemocnice od Evropy po Vietnam, tržby meziročně +750 %. To se nevidí často. Gratulace celému týmu k dosud největší investici. A jestli v healthtechu stavíte něco podobného — fond SGTwo se právě rozjíždí. Ozvěte se, na kafe se čas v
… [25362 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nitems=[\n('rockaway','https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-remix-a-technology-platform-for-circular-fashion','As part of a Series A investment round, the fund is acquiring a 20% stake in the company.'),\n('rockawayx','https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund','has acquired Relayer Capital'),\n('seedstarter','https://blog.tensor.ventures/p/portfolio-news-pointee-raises-14m','Pointee has closed a $1.4M Seed round led by Tensor Ventures, with Seed Starter České spořitelny and Seed Starter Slovenskej sporiteľne participating.'),\n('soulmates','https://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/','This is why we led the $9.3M Series A'),\n('springtide','https://www.threatmark.com/newsroom/threatmark-to-advance-the-fight-against-online-fraud/','and an $8 million convertible note from Springtide Ventures Fund.'),\n('startguide','https://cc.cz/ceska-umela-inteligence-analyzuje-rentgeny-plic-a-miri-do-evropy-carebot-zaroven-ziskal-investici/','venture kapit
… [1999 more characters]
```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 6.5 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"77f2bf\",\"wall_time_seconds\":6.314990166,\"exit_code\":0,\"original_token_count\":2228,\"output\":\"rockaway PASS As part of a Series A investment round, the fund is acquiring a 20% stake in the company.\\nrockawayx FAIL \\n RockawayX acquires crypto-focused hedge fund firm, Relayer Capital, and launches Liquid Opportunities Fund Home Investments Liquidity Infrastructure Curation Funds Catapult Insights Team RockawayX acquires crypto-focused hedge fund firm, Relayer Capital, and launches Liquid Opportunities Fund News Investments RockawayX, a global digital asset investment platform with approximately $2 billion in assets under management, today announced the acquisition of Relayer Capital, a digital asset hedge fund founded by Austin Barack. Following the transaction, Relayer will become the RockawayX Liquid Opportunities Fund, with Barack joining RockawayX as CIO of the Fund and continuing to lead its investment strategy. The Fund, which is open to new external investors, is a directional long/short hedge fund strategy focused on identifying undervalued liquid tokens and crypto-related equities. The acquisition adds a liquid fundamental strategy to RockawayX’s existing investment platform and expands the firm’s presence in the US, where Barack is based in the New York area. “We have always been disciplined about adding new strategies to Ro
… [7607 more characters]
```
</details>

→ `exec`
```
text(await tools.exec_command({cmd:"python3 - <<'PY'\nimport subprocess,re,html\nitems=[('https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund','today announced the acquisition of Relayer Capital, a digital asset hedge fund founded by Austin Barack.'),('https://blog.tensor.ventures/p/new-investment-cnuic-raises-3m-to','Cnuic has raised $3M in a pre-seed round led by Tensor Ventures and Blank Space Ventures'),('https://cc.cz/2021/06/krabickove-diety-vhodne-i-pro-diabetiky-cesky-nutritionpro-v-praze-rozvezl-uz-250-tisic-jidel-a-nabira-35-milionu-korun/','Karel Janeček a UP21 21,1 % a Lighthouse Ventures 8 %')]\nfor u,q in items:\n p=subprocess.run(['curl','-Ls','--max-time','20',u],capture_output=True,text=True).stdout;p=re.sub(r'<(script|style)\\b[^>]*>.*?</\\1>','',p,flags=re.S);s=html.unescape(re.sub('<[^>]+>',' ',p));s=re.sub(r'\\s+',' ',s)\n r=subprocess.run(['grep','-oF',q],input=s,capture_output=True,text=True);print(u,r.returncode,r.stdout)\nPY","max_output_tokens":1200}));

```

<details><summary>result</summary>

```
[{"type": "input_text", "text": "Script completed\nWall time 0.9 seconds\nOutput:\n"}, {"type": "input_text", "text": "{\"chunk_id\":\"01c6fa\",\"wall_time_seconds\":0.707074875,\"exit_code\":0,\"original_token_count\":152,\"output\":\"https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund 0 today announced the acquisition of Relayer Capital, a digital asset hedge fund founded by Austin Barack.\\n\\nhttps://blog.tensor.ventures/p/new-investment-cnuic-raises-3m-to 0 Cnuic has raised $3M in a pre-seed round led by Tensor Ventures and Blank Space Ventures\\n\\nhttps://cc.cz/2021/06/krabickove-diety-vhodne-i-pro-diabetiky-cesky-nutritionpro-v-praze-rozvezl-uz-250-tisic-jidel-a-nabira-35-milionu-korun/ 0 Karel Janeček a UP21 21,1 % a Lighthouse Ventures 8 %\\n\\n\"}"}]
```
</details>

**Codex:**

[
  {
    "id": "rockaway-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Remix",
      "date": "2025-12-19",
      "date_precision": "day",
      "url": "https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-remix-a-technology-platform-for-circular-fashion",
      "quote": "As part of a Series A investment round, the fund is acquiring a 20% stake in the company."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Prague-based venture fund announced a 20% equity investment in Remix."
  },
  {
    "id": "rockawayx",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Relayer Capital",
      "date": "2026-08-25",
      "date_precision": "day",
      "url": "https://www.rockawayx.com/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund",
      "quote": "today announced the acquisition of Relayer Capital, a digital asset hedge fund founded by Austin Barack."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The latest confirmed transaction is a private-firm acquisition dated August 25 in its official news index, while investment operations span Prague and other international offices."
  },
  {
    "id": "seed-starter-slovenskej-sporitelne",
    "is_investor": "yes",
    "type": "cvc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Pointee",
      "date": "2026-04-21",
      "date_precision": "day",
      "url": "https://blog.tensor.ventures/p/portfolio-news-pointee-raises-14m",
      "quote": "Pointee has closed a $1.4M Seed round led by Tensor Ventures, with Seed Starter České spořitelny and Seed Starter Slovenskej sporiteľne participating."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "Slovenská sporiteľňa's Slovak corporate venture programme participated in Pointee's seed financing."
  },
  {
    "id": "soulmates-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Antiverse",
      "date": "2026-03-09",
      "date_precision": "day",
      "url": "https://www.soulmatesventures.com/making-the-undruggable-druggable-antiverse/",
      "quote": "This is why we led the $9.3M Series A"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Czech sustainable venture fund confirms leading Antiverse's Series A, with the date representing publication of its investment announcement."
  },
  {
    "id": "springtide-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "ThreatMark",
      "date": "2025-01-07",
      "date_precision": "day",
      "url": "https://www.threatmark.com/newsroom/threatmark-to-advance-the-fight-against-online-fraud/",
      "quote": "and an $8 million convertible note from Springtide Ventures Fund."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Czech KKCG-backed fund provided convertible financing to ThreatMark; similarly named US healthcare investors were excluded."
  },
  {
    "id": "startguide",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Carebot",
      "date": "2024-03-22",
      "date_precision": "day",
      "url": "https://cc.cz/ceska-umela-inteligence-analyzuje-rentgeny-plic-a-miri-do-evropy-carebot-zaroven-ziskal-investici/",
      "quote": "venture kapitálová společnost Startguide VC, skupina BHM group Tomáše Krska a Gain Ventures."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "Its official Prague-based VC mandate and Carebot participation are confirmed, but later database-reported deals lacked independently verifiable round-specific evidence."
  },
  {
    "id": "startupyard",
    "is_investor": "yes",
    "type": "accelerator",
    "managed_from": "CZ",
    "latest_investment": null,
    "active_36m": "unclear",
    "confidence": "medium",
    "note": "The Prague accelerator offers cash convertible notes and targets equity, but recent programme admissions do not establish completed dated investments: https://startupyard.com/faq/."
  },
  {
    "id": "tensor-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "Cnuic",
      "date": "2026-04-28",
      "date_precision": "day",
      "url": "https://blog.tensor.ventures/p/new-investment-cnuic-raises-3m-to",
      "quote": "Cnuic has raised $3M in a pre-seed round led by Tensor Ventures and Blank Space Ventures"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Czech deep-tech venture manager confirms co-leading Cnuic's pre-seed round; later portfolio fundraising alone does not prove its participation."
  },
  {
    "id": "tilia-impact-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "FaceUp",
      "date": "2026-05-19",
      "date_precision": "day",
      "url": "https://www.faceup.com/en/blog/series-a",
      "quote": "The raise also included strong participation from returning investors, Tilia Impact V entures (supported by the InvestEU Fund) and Reflex Capital"
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "FaceUp confirms participation by the Prague-based impact venture fund in its Series A."
  },
  {
    "id": "up21",
    "is_investor": "yes",
    "type": "accelerator",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "NutritionPro",
      "date": "2021-06-24",
      "date_precision": "day",
      "url": "https://cc.cz/2021/06/krabickove-diety-vhodne-i-pro-diabetiky-cesky-nutritionpro-v-praze-rozvezl-uz-250-tisic-jidel-a-nabira-35-milionu-korun/",
      "quote": "Karel Janeček a UP21 21,1 % a Lighthouse Ventures 8 %"
    },
    "active_36m": "no",
    "confidence": "medium",
    "note": "The Prague incubator invested for equity; June 2021 is the latest verifiable transaction found, while an uncorroborated June 2023 database entry was excluded."
  },
  {
    "id": "venture-to-future-fund",
    "is_investor": "yes",
    "type": "public_dfi",
    "managed_from": "SK",
    "latest_investment": {
      "company": "Sloneek",
      "date": "2026-06-23",
      "date_precision": "day",
      "url": "https://www.sloneek.com/blog/sloneek-raises-6m-to-give-hr-a-smarter-way-to-work/",
      "quote": "And with $6 million in new funding from Orbit Capital and Venture to Future Fund, we get to close it a lot faster."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "The Bratislava-managed EIB and Slovak-government venture vehicle directly co-invests in companies, and Sloneek confirms its participation."
  },
  {
    "id": "vision-ventures",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "SK",
    "latest_investment": {
      "company": "CultureBoard",
      "date": "2024-04-05",
      "date_precision": "day",
      "url": "https://cc.cz/jsou-mu-jen-dva-roky-ale-mezi-klienty-ma-disney-nike-ci-metu-pomaha-jim-s-firemni-kulturou/",
      "quote": "Slovenská společnost Vision Ventures posílá 400 tisíc eur (10 milionů korun)"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The Slovak VC provided follow-on financing to CultureBoard, although its original fund's investment period has ended."
  },
  {
    "id": "y-soft-ventures",
    "is_investor": "yes",
    "type": "cvc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "RoboTwin",
      "date": "2025-06-23",
      "date_precision": "day",
      "url": "https://www.novalia.cz/blogpost/novalia-zastupovala-robotwin-cesky-startup-ktery-meni-budoucnost-prumyslove-automatizace",
      "quote": "Y Soft Ventures, EIT Manufacturing a investor Jörg Rupp."
    },
    "active_36m": "yes",
    "confidence": "high",
    "note": "Y Soft's Brno-based corporate venture arm participated in RoboTwin's pre-seed financing, confirmed by the company's transaction counsel."
  },
  {
    "id": "zaka-vc",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": "CZ",
    "latest_investment": {
      "company": "PerfectBit",
      "date": "2026-08-18",
      "date_precision": "day",
      "url": "https://zaka.vc/perfectbit-building-the-verified-data-layer-for-physical-ai/",
      "quote": "Why we invested PerfectBit combines several characteristics"
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "The Prague-origin VC explicitly confirms investing in PerfectBit; later Sensible news describes previous investments without confirming participation in its new financing."
  },
  {
    "id": "zero-one-hundred",
    "is_investor": "yes",
    "type": "vc",
    "managed_from": null,
    "latest_investment": {
      "company": "Reno",
      "date": "2025-12-04",
      "date_precision": "day",
      "url": "https://www.wamda.com/ar/2025/12/uae-reno-raises-4-million-equity-debt-round",
      "quote": "The round was led by 500 Sanabil, Hub71, Plus VC, Zero 100 VC, FlyerOne Ventures, Sandstorm VC, AngelSpark and Swiss Founders Fund."
    },
    "active_36m": "yes",
    "confidence": "medium",
    "note": "Direct venture investment is confirmed, but management spans Slovakia and Cyprus and newer BotBot database dates conflict."
  }
]

Verification: 14 final investment quotations checked successfully with curl-fetched page text and literal grep; approximately 65 search queries, no repository writes or git commands. Some retained dates are announcement publication dates, explicitly explained in notes. StartupYard has no completed dated investment established.

