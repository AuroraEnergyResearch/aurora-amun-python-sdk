---
title: Get Scenarios
---

To see the list of available scenarios in Amun, use [`AmunSession.get_scenarios`](/docs/Reference/session#get_scenarios). Scenarios are regional, hence you need to provide a region you want to get scenarios for. List of region codes you could use:
- aus_nsw
- aus_qld
- aus_saa
- aus_tas
- aus_vic
- bgr
- deu
- erc_hou
- erc_nor
- erc_sou
- erc_wes
- esp
- fra
- gbr
- grc
- irx
- ita_cal
- ita_cnor
- ita_csud
- ita_nor
- ita_sar
- ita_sic
- ita_sud
- nld
- nod_dk1
- nod_dk2
- nod_fi
- nod_no1
- nod_no2
- nod_no3
- nod_no4
- nod_no5
- nod_se1
- nod_se2
- nod_se3
- nod_se4
- np15
- pjm_ae
- pjm_aep
- pjm_ap
- pjm_atsi
- pjm_bge
- pjm_ce
- pjm_day
- pjm_deok
- pjm_dlco
- pjm_dom
- pjm_dpl
- pjm_ekpc
- pjm_jcpl
- pjm_me
- pjm_ovec
- pjm_peco
- pjm_pep
- pjm_pn
- pjm_ppl
- pjm_pseg
- pjm_reco
- pol
- prt
- rou
- sp15
- zp26

**Note that you will get the scenarios in the region only if you are subscribed to a region**

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
scenarios = session.get_scenarios("gbr")
print("Number of scenarios:", len(scenarios))
print(scenarios[:2])
```

The output will look like so:

```powershell
Number of scenarios: 130
[{'id': 3, 'name': '2019 Smart Power Scenario', 'description': 'To examine the impact of a smarter power system with more flexible capacity and demand', 'isRetired': True, 'region': 'gbr', 'S3uri': None, 'currency': 'GBP', 'currencyYear': 2018, 'publicationDate': '2020-01-09T17:02:05.000Z', 'type': 'legacy', 'scenarioVersion': 0, 'hash': 'a5da31ed-f72d-424e-9d41-a81873269dbc', 'hasFile': False}, {'id': 4, 'name': 'Aurora Central - 2019 April', 'description': "Aurora's long-term central price forecast, published in April 2019.", 'isRetired': False, 'region': 'gbr', 'S3uri': None, 'currency': 'GBP', 'currencyYear': 2018, 'publicationDate': '2019-04-09T17:02:05.000Z', 'type': 'legacy', 'scenarioVersion': 0, 'hash': 'ca648771-380f-4b49-96ce-3d1f3ae809eb', 'hasFile': False}]
```

You could also get a scenario by name. This is especially useful when you run valuations or load factor calculations

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
scenario = session.get_scenario_by_name("gbr", "Aurora Central - April 2022")
```