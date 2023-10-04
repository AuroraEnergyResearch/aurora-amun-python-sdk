---
title: Get Region Details
---

You can get more details about the location that you want to request using [`AmunSession.get_region_details`](/docs/Reference/session#get_region_details). Depending on location, there can be 1, 0 or 1+ regions.

You can use this method to see which reanalysis data sets are available to use in that region(s).

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
regions = session.get_region_details(latitude=51.753081, longitude=-1.250017)
print(len(regions), "regions found")
print(regions[0])
```

Output:

```powershell
1 regions found
RegionDetail->{'pmfCode': 'gbr', 'defaultWind': 'Era5', 'availableDatasets': ['Era5', 'NEWA', 'AuroraWindAtlas'], 'era5CorrectionEnabled': True, 'powerCurveSmoothingEnabled': True}
```

