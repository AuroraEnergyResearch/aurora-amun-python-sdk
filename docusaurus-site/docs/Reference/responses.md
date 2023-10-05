---
sidebar_label: responses
title: responses
---

## RegionDetail Objects

```python
class RegionDetail()
```

The details about a region required to construct valid valuation and load factor requests.

**Arguments**:

- `pmfCode` _str_ - The *regionCode* to use when required to look up more details e.g. which scenarios are available. `.AmunSession.get_scenarios`
- `defaultWind` _str_ - The dataset used by default in calculations
- `availableDatasets` _List[str]_ - A list of datasets that are available for the region.
- `era5CorrectionEnabled` _bool_ - Is era5 correction available for the region.
- `powerCurveSmoothingEnabled` _bool_ - Is power curve smoothing available for the region.

