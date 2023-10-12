---
title: Get a Power Curve for a Turbine
---

You will need to know the exact name of the turbine you want to get the power curve for. To see the list of available turbines in Amun, use [`AmunSession.get_turbines`](/docs/Reference/session#get_turbines).

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")
power_curve = session.get_power_curve(turbine["id"])

# Print the first three points of the power curve
print(power_curve[:3])
```

The output will look like so:

```powershell
[{'speed': 1, 'power': 0}, {'speed': 2, 'power': 0}, {'speed': 3, 'power': 79}]
```