---
sidebar_position: 1
sidebar_label: Installation
title: Installation
description: Getting the SDK installed and authenticated
---

# Installation

1. Install the package from the git repository

```bash
pip install git+https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk
```

2. In order to use the Amun API a user token is required and can be created in [EOS setting](https://eos.auroraer.com/dragonfly/settings). Add your Aurora API key to the file $home/.aurora-api-key. for example `C:\Users\Joe Bloggs\.aurora-api-key` or set as the environment variable `AURORA_API_KEY`. 

3. Once the key is set up the `AmunSession` object can be created to access the API. Examples of methods available can be found in [AmunSession](/docs/Reference/session) for details on usage.

```python
from aurora.amun.client.session import AmunSession
session  = AmunSession()
result  = session.get_scenarios("gbr")
print(res[0])
```
