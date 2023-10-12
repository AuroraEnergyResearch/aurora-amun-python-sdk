---
title: Common Examples
---

Here you will see common usage of Amun SDK for creating valuations. Each section will cover an example for a different [wind type](/docs/Reference/parameters#windtype-objects) and provide some tips like how to configure losses, delete a valuation, etc.  

You can find more examples with code in [Amun Python SDK repository](https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk) inside the `examples/` folder.

:::caution
Valuations SDK has been built to support "reasonable" level of usage for now, but will not support scripts that produce very large numbers (1000s) of valuations automatically. If you are interested in using Amun SDK for such purposes, get in touch with Aurora.
:::

### Run Valuation with Amun Wind Atlas + Losses
Running a valuation involves multiple steps. Firstly, you need to create parameters and get information about scenario and turbine you want to use. Make sure the names are spelled correctly. Secondly, you will need to create a valuation. After it's successfully created, you will be able to see it in your Amun profile on our website. And lastly, the valuation needs to be launched using the `AmunSession.get_valuation_results` function.  

Optionally, you can add losses to the valuation parameters.

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json
from datetime import datetime

session = AmunSession()
    
scenario = session.get_scenario_by_name("gbr", "Aurora Central - April 2022")
turbine = session.get_turbine_by_name("Alstom Eco 110")

valuation_parameters = {
    "name": f"SDK Wind Farm {datetime.now()}",
    "description": "Created by Api",
    "longitude": -1.009191,
    "latitude": 52.308479,
    "windType": "AuroraWindAtlas",
    "scenarioId": scenario["id"],
    "turbineModelId": turbine["id"],
    "numberOfTurbines": 10,
    "hubHeight": 80,
    "obstacleHeight": 0,
    "roughnessLength": 0.001,
    "useReanalysisCorrection": False,
    "usePowerCurveSmoothing": True,
    # Optional
    "lossesWake": 0.2,
    "lossesAvailability": 0.02,
    "lossesElectrical": 0.01,
    "lossesTurbinePerformance": 0.1,
    "lossesEnvironmental": 0.05,
    "lossesOtherCurtailment": 0.0,
}

valuation = session.create_valuation(valuation_parameters)
save_to_json(f"valuations/valuation_{valuation['id']}.json", valuation)

results = session.get_valuation_results(
    valuation["id"], format="json", should_return_hourly_data=False
)
save_to_json(f"valuations/valuation_{valuation['id']}_out.json", results)
```

### Run Average Wind Speed Valuation + Specific Parameters
The same method is used for all other power types. For example, Average Wind Speed calibration. You will need to provide additional parameters that are relevant for this wind type: `averageWindSpeed` and `measurementHeight`. Refer to SDK Reference to see list of additional required parameters. For example, see the "Arguments" section of [AverageWindSpeedParameters](/docs/Reference/parameters#averagewindspeedparameters-objects)

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json
from datetime import datetime

session = AmunSession()
    
scenario = session.get_scenario_by_name("gbr", "Aurora Central - April 2022")
turbine = session.get_turbine_by_name("Alstom Eco 110")

valuation_parameters = {
    "name": f"SDK Wind Farm {datetime.now()}",
    "description": "Created by Api",
    "longitude": -1.009191,
    "latitude": 52.308479,
    "windType": "averagewindspeed",
    "averageWindSpeed": 7.5,
    "measurementHeight": 100,
    "scenarioId": scenario["id"],
    "turbineModelId": turbine["id"],
    "numberOfTurbines": 10,
    "hubHeight": 80,
    "obstacleHeight": 0,
    "roughnessLength": 0.001,
    "useReanalysisCorrection": False,
    "usePowerCurveSmoothing": True
}

valuation = session.create_valuation(valuation_parameters)
save_to_json(f"valuations/valuation_{valuation['id']}.json", valuation)

results = session.get_valuation_results(
    valuation["id"], format="json", should_return_hourly_data=False
)
save_to_json(f"valuations/valuation_{valuation['id']}_out.json", results)
```

### Run P50 load factor + Delete Valuation
AmunSession also allows you to detele a valuation with [`AmunSession.delete_valuation`](/docs/Reference/session#delete_valuation). This could be useful for cleaning up after experiments and when the valuation is unlikely to be used later. For example, you can create a valution with P50 load factor estimation and remove the valuation after saving the results in JSON.

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json
from datetime import datetime

session = AmunSession()
    
scenario = session.get_scenario_by_name("gbr", "Aurora Central - April 2022")
turbine = session.get_turbine_by_name("Alstom Eco 110")

valuation_parameters = {
    "name": f"SDK Wind Farm {datetime.now()}",
    "description": "Created by Api",
    "longitude": -1.009191,
    "latitude": 52.308479,
    "windType": "p50scaling",
    "p50GrossProduction": 0.6,
    "scenarioId": scenario["id"],
    "turbineModelId": turbine["id"],
    "numberOfTurbines": 10,
    "hubHeight": 80,
    "obstacleHeight": 0,
    "roughnessLength": 0.001,
    "useReanalysisCorrection": False,
    "usePowerCurveSmoothing": True
}

valuation = session.create_valuation(valuation_parameters)
save_to_json(f"valuations/valuation_{valuation['id']}.json", valuation)

results = session.get_valuation_results(
    valuation["id"], format="json", should_return_hourly_data=False
)
save_to_json(f"valuations/valuation_{valuation['id']}_out.json", results)

session.delete_valuation(valuation["id"])
```

### Run Valuation using Time Series Generation
Sometimes you will need to provide sizeable data to Amun SDK. In these cases, it is convenient to use one of the utils of Amun SDK: `get_json`. Below is an example for Time Series Generation upload. The process includes an extra step of uploading the generation data to Amun before running valuation.

Make sure that the format of the data is correct and that the generation values have been produced in the location that you pass in valuation parameters. If there is a large discrepancy between the generation values and the long-term reanalysis data in that location Amun API will throw and error.

Because the generation data has already been provided, it is not necessary to specify a turbine.

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json, get_json
from datetime import datetime

session = AmunSession()
    
scenario = session.get_scenario_by_name("gbr", "Aurora Central - April 2022")
turbine = session.get_turbine_by_name("Alstom Eco 110")

valuation_parameters = {
    "name": f"SDK Wind Farm {datetime.now()}",
    "description": "Created by Api",
    "longitude": -0.23,
    "latitude": 52.93,
    "scenarioId": scenario["id"],
    "hubHeight": 59,
    "obstacleHeight": 0,
    "useReanalysisCorrection": False,
    "usePowerCurveSmoothing": False,
}

valuation = session.create_valuation(valuation_parameters)
save_to_json(f"valuations/valuation_{valuation['id']}.json", valuation)

# Check the json document for a complete structure of what is required
generation_json = get_json("examples\data\example_generation_request.json")

# Specify data's granularity in minutes
generation_json["granularityInMins"] = 60

session.send_production_for_calibration(valuation["id"], generation_json)

results = session.get_valuation_results(
    valuation["id"], format="json", should_return_hourly_data=False
)
save_to_json(f"valuations/valuation_{valuation['id']}_out.json", results)
```