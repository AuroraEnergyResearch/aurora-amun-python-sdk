---
title: Get Turbines
---

To see the list of available turbines in Amun, use [`AmunSession.get_turbines`](/docs/Reference/session#get_turbines)

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
turbines = session.get_turbines()
print("Number of available turbines:", len(turbines))
print(turbines[:2])
```

The output will look like so:

```powershell
Number of available turbines: 947
[{'id': 1006, 'manufacturer': 'Hypothetical', 'name': ' 16MW 320SP 166HH', 'ratedCapacity': 16, 'rotorDiameter': 250, 'minHubHeight': 149, 'maxHubHeight': 166, 'cutInSpeed': 4, 'cutOutSpeed': 25, 'specSource': 'custom', 'type': 'custom'}, {'id': 1011, 'manufacturer': 'Hypothetical', 'name': ' 16MW GE', 'ratedCapacity': 16, 'rotorDiameter': 254, 'minHubHeight': 152, 'maxHubHeight': 152, 'cutInSpeed': 3, 'cutOutSpeed': 28, 'specSource': 'custom', 'type': 'custom'}]
```

You could also get a turbine by name. This is especially useful when you run valuations or load factor calculations

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")
```