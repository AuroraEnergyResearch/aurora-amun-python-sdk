---
title: Common Examples
---

Amun SDK provides an array of options on how to calculate load factors for a location. Examples below will be using [`AmunSession.run_load_factor_for_parameters`](/docs/Reference/session#run_load_factor_for_parameters) that expects two parts: [base parameters](/docs/Reference/parameters#loadfactorbaseparameters-objects) and one of the flow parameters:
- [`AverageWindSpeedParameters`](/docs/Reference/parameters#averagewindspeedparameters-objects)
- [`BuiltInWindParameters`](/docs/Reference/parameters#builtinwindparameters-objects)
- [`PowerDensityParameters`](/docs/Reference/parameters#powerdensityparameters-objects)
- [`P50ScalingParameters`](/docs/Reference/parameters#p50scalingparameters-objects)
- [`P50YieldScalingParameters`](/docs/Reference/parameters#p50yieldscalingparameters-objects)
- [`UploadedWindParameters`](/docs/Reference/parameters#uploadedwindparameters-objects)
- [`WeibullParameters`](/docs/Reference/parameters#weibullparameters-objects)

And to read more information about each wind/power type, refer to the [WindType Objects](/docs/Reference/parameters#windtype-objects) section of SDK Reference.

You can find more examples with code in [Amun Python SDK repository](https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk) inside the `examples/` folder.

### Calculate Load Factors with Amun Wind Atlas
To use `AmunSession.run_load_factor_for_parameters`, select an available turbine that is available in Amun and set base parameters. See [SDK Reference](/docs/Reference/parameters#loadfactorbaseparameters-objects) for explanations on what each parameter means.  

Built-in dataset is a good choice of wind type to use if no site-specific data is available. To use a built-in datase, use [`aurora.amun.client.parameters.BuiltInWindParameters(WindType)`](/docs/Reference/parameters#builtinwindparameters-objects). You can pass types like `AuroraWindAtlas`, `Era5`, `Merra2`, or `NEWA`. But check whether the wind type is supported by the [region](/docs/Examples/Regions/get-region-details).  

In our case, the region support Amun Wind Atlas, which is the most accurate version of built-in wind data available in Amun

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    BuiltInWindParameters,
    LoadFactorBaseParameters
)

session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")

base_parameters = LoadFactorBaseParameters(
    turbineModelId=turbine["id"],
    latitude=59.59,
    longitude=0,
    startTimeUTC="2018-01-01T00:00:00.000Z",
    regionCode="GBR",
    hubHeight=90,
    obstacleHeight=0,
    lossesAvailability=0.1,
    lossesWake=0,
    numberOfTurbines=12,
    roughnessLength=0.02,
    usePowerCurveSmoothing=False,
    useReanalysisCorrection=True,
)

flow_parameters = BuiltInWindParameters("AuroraWindAtlas")

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)

# Print out the wind type and first 5 hourly load factors
print("Example load factors for wind type:", load_factors["parameters"]["windType"])
print(load_factors["weatherYearHourly"][:5])
```

Expected output (truncated)
```powershell
Example load factors for wind type: era5
[{'dateTime': '2018-01-01T00:00Z', 'windSpeed': 8.344985289917028, 'loadFactor': 0.5179}, {'dateTime': '2018-01-01T01:00Z', 'windSpeed': 7.460143358993289, 'loadFactor': 0.3753}, {'dateTime': '2018-01-01T02:00Z', 'windSpeed': 7.143849120158415, 'loadFactor': 0.327}, {'dateTime': '2018-01-01T03:00Z', 'windSpeed': 8.058062729353766, 'loadFactor': 0.4678}, {'dateTime': '2018-01-01T04:00Z', 'windSpeed': 8.742962986200617, 'loadFactor': 0.5874}]
```

### Calculate Load Factors with Custom Wind Data
The same code template can be used with other wind types. But for [Uploaded Wind](/docs/Reference/parameters#uploadedwindparameters-objects), for example, you might want to import a local JSON file with wind speeds. Use `get_json` from Amun SDK utilities to load local file

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    UploadedWindParameters,
    LoadFactorBaseParameters
)
from aurora.amun.client.utils import get_json

session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")

base_parameters = LoadFactorBaseParameters(
    turbineModelId=turbine["id"],
    latitude=59.59,
    longitude=0,
    startTimeUTC="2018-01-01T00:00:00.000Z",
    regionCode="GBR",
    hubHeight=90,
    obstacleHeight=0,
    lossesAvailability=0.1,
    lossesWake=0,
    numberOfTurbines=12,
    roughnessLength=0.02,
    usePowerCurveSmoothing=False,
    useReanalysisCorrection=False,
)

# Provide the path to your file
# In our example, the file looks like {"speeds":[10.888, 11.59, ...]}
# and contains 8760 values - for each hour in a year 2017
speeds = get_json("examples\data\example_windSpeed.json")["speeds"]

flow_parameters = UploadedWindParameters(
    uploadedWindStartTime="2017-01-01T00:00:00.000Z",
    lowHeight=SpeedAtHeight(10, speeds=speeds),
    granularityInMins=60,
)

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)

# Print out the wind type and first 5 hourly load factors
print("Example load factors for wind type:", load_factors["parameters"]["windType"])
print(load_factors["weatherYearHourly"][:5])
```

```powershell
Example load factors for wind type: UploadedWind
[{'dateTime': '2017-01-01T00:00Z', 'windSpeed': 12.476777004018876, 'loadFactor': 0.8987}, {'dateTime': '2017-01-01T01:00Z', 'windSpeed': 13.354024977064322, 'loadFactor': 0.9}, {'dateTime': '2017-01-01T02:00Z', 'windSpeed': 12.738090910135982, 'loadFactor': 0.8994}, {'dateTime': '2017-01-01T03:00Z', 'windSpeed': 12.914630833546354, 'loadFactor': 0.8998}, {'dateTime': '2017-01-01T04:00Z', 'windSpeed': 12.017396341735259, 'loadFactor': 0.8976}]
```

### Calculate Load Factors with P50 scaling + Save to JSON
You might want to save the load factors in a file. And for that you could use one of the Amun SDK utils. For example, you can save a [P50 scaling](/docs/Reference/parameters#p50scalingparameters-objects) calculation giving it a timestamp, wind type and unique id for reference.

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    WeibullParameters,
    LoadFactorBaseParameters
)
from aurora.amun.client.utils import save_to_json

session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")

base_parameters = LoadFactorBaseParameters(
    turbineModelId=turbine["id"],
    latitude=59.59,
    longitude=0,
    startTimeUTC="2018-01-01T00:00:00.000Z",
    regionCode="GBR",
    hubHeight=90,
    obstacleHeight=0,
    lossesAvailability=0.1,
    lossesWake=0,
    numberOfTurbines=12,
    roughnessLength=0.02,
    usePowerCurveSmoothing=False,
    useReanalysisCorrection=False,
)

flow_parameters = P50ScalingParameters(p50GrossProduction=0.6)

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)

loadFactorRequestId = load_factors["parameters"]["loadFactorRequestId"]
save_to_json(
    f"load_factors_{datetime.now().isoformat().replace(':','_')}_{flow_parameters.windType}_{loadFactorRequestId}.json",
    load_factors
)
```

You will find the output in the new directoty called 'out' (will be created in the same folder where you run the script from). And the output file's name will look like this: `load_factors_2023-10-03T10_43_21.083658_WindType.P50Scaling_e33fcdf0-5e98-47ee-b7df-424d75809e66.json`.

### Calculate Load Factors from Average Wind Speed
Average Wind Speed is another type of calibration Amun SDK has available. See [wind type overview](/docs/Reference/parameters#averagewindspeed) for context, and [parameters documentation](/docs/Reference/parameters#averagewindspeedparameters-objects) to see which values need to be provided

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    WeibullParameters,
    LoadFactorBaseParameters
)
from aurora.amun.client.utils import save_to_json

session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")

base_parameters = LoadFactorBaseParameters(
    turbineModelId=turbine["id"],
    latitude=59.59,
    longitude=0,
    startTimeUTC="2018-01-01T00:00:00.000Z",
    regionCode="GBR",
    hubHeight=90,
    obstacleHeight=0,
    lossesAvailability=0.1,
    lossesWake=0,
    numberOfTurbines=12,
    roughnessLength=0.02,
    usePowerCurveSmoothing=False,
    useReanalysisCorrection=False,
)

flow_parameters = AverageWindSpeedParameters(averageWindSpeed=10, measurementHeight=40)

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)

loadFactorRequestId = load_factors["parameters"]["loadFactorRequestId"]
```