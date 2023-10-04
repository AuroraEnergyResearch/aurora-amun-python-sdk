---
title: Add Custom Turbine
---

You can upload a turbine to Amun providing an Excel workbook with required information. You can get a template for the workbook from [Amun](https://eos.auroraer.com/dragonfly/amun) in the Turbine section of a New Valuation form.

```python
import requests
from aurora.amun.client.session import AmunSession

# Calling AmunSession() with no token in constructor will load one from an environment variable if provided
# or a file HOME/.
session = AmunSession()

filePath = "examples\data\Turbine_upload_api_example.xlsx"
files = {"name": ("Turbine_upload_api_example.xlsx", open(filePath, "rb"))}

headers = {
    "Private-Token": session.token,
}
req = requests.put(url=f"{session.base_url}/turbines", files=files, headers=headers)
```