# Aurora Amun SDK

## This is under development and not for general use.

## Installing

```powershell
pip install git+https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk
```

In order to use the Amun API a user token is required. This token can be added to the file `HOME/.aurora-api-key` for example `C:\Users\Joe Bloggs\.aurora-api-key` or set as the environment variable `AURORA_API_KEY`.

Once the key is set up the `AmunSession` object can be created to access the api

```python
from aurora.amun.client.session import AmunSession
session  = AmunSession()
turbines  = session.get_turbines()
print(turbines[0])
```
