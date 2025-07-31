---
title: Get Region Details
---

You can get more details about the location that you want to request using [`AmunSession.get_region_details`](/docs/Reference/session#get_region_details). Depending on location, there can be 1, 0 or 1+ regions.

You can use this method to see which reanalysis data sets are available to use in that region(s) or what the code of the region is.

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

To see what each of the output fields means, see [`RegionalDetail` object format](/docs/Reference/responses#regiondetail-objects)

Here is an example where multiple regions overlap at the point

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
regions = session.get_region_details(latitude=50.757310, longitude=1.225665)
print(len(regions), "regions found")
print(regions[0])
print(regions[1])
```

Output:

```powershell
2 regions found
RegionDetail->{'pmfCode': 'fra', 'defaultWind': 'Era5', 'availableDatasets': ['Era5', 'NEWA', 'AuroraWindAtlas'], 'era5CorrectionEnabled': False, 'powerCurveSmoothingEnabled': False}
RegionDetail->{'pmfCode': 'gbr', 'defaultWind': 'Era5', 'availableDatasets': ['Era5', 'NEWA', 'AuroraWindAtlas'], 'era5CorrectionEnabled': True, 'powerCurveSmoothingEnabled': True}
```

Calling `get_region_details` is also useful when you want to know the region code that should be passed to the [`get_scenarios`](/docs/Reference/session#get_scenarios) method. Since you will need to access relevant scenarios when running the valuations, it is common usage example

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
regions = session.get_region_details(latitude=50.757310, longitude=1.225665)

# Just to check how many regions are available at this location
print(len(regions), "regions found")
for region in regions:
    print(region)

# You can extract available scenarios for a region of interest
region_code = regions[0].pmfCode
scenarios = session.get_scenarios(region_code)
```

Output will look something like this:

```powershell
2 regions found
RegionDetail->{'pmfCode': 'fra', 'defaultWind': 'Era5', 'availableDatasets': ['Era5', 'NEWA', 'AuroraWindAtlas'], 'era5CorrectionEnabled': False, 'powerCurveSmoothingEnabled': False}
RegionDetail->{'pmfCode': 'gbr', 'defaultWind': 'Era5', 'availableDatasets': ['Era5', 'NEWA', 'AuroraWindAtlas'], 'era5CorrectionEnabled': True, 'powerCurveSmoothingEnabled': True}
```