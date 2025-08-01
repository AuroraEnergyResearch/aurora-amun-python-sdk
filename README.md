# Aurora Amun SDK

A Python SDK for interacting with Amun.

## Installation

Minimum Python version required is 3.8.

```powershell
pip install git+https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk
```

In order to use the Amun API a user token is required and can be created in [EOS setting](https://eos.auroraer.com/dragonfly/settings). This token can be added to the file `HOME/.aurora-api-key` for example `C:\Users\Joe Bloggs\.aurora-api-key` or set as the environment variable `AURORA_API_KEY`.

Once the key is set up the `AmunSession` object can be created to access the api. Examples of methods available can be found in [examples](examples).

See [aurora-amun-python-sdk-docs](https://auroraenergyresearch.github.io/aurora-amun-python-sdk-docs/) for full SDK documentation.

```python
from aurora.amun.client.session import AmunSession
session  = AmunSession()
turbines  = session.get_turbines()
print(turbines[0])
```

You can find documentation website at [auroraenergyresearch.github.io/aurora-amun-python-sdk/](https://auroraenergyresearch.github.io/aurora-amun-python-sdk/)