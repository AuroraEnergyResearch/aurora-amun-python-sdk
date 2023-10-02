---
title: Get Load Factors
---

### Basic Examples

To run load factor simulation, you will need to first get a turbine using `get_turbine_by_name`. You can then select which flow to use and pass both base and flow parameters. Call `run_load_factor_for_parameters` to generate results. Example below is using ERA5 Built-in Reanalysis dataset.

#### Calculate Load Factors with ERA5 data
```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    BuiltInWindParameters,
    LoadFactorBaseParameters
)

session = AmunSession()
turbine = session.get_turbine_by_name()

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

flow_parameters = BuiltInWindParameters("era5")

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)
```

The same method can be used with any wind type. To see how to use all the types, see [Parameters](/docs/Reference/parameters) For Uploaded Wind, you might want to upload a local JSON file. Use `get_json` from Amun SDK to load local file

#### Calculate Load Factors with custom wind data
```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    UploadedWindParameters,
    LoadFactorBaseParameters
)
from aurora.amun.client.utils import get_json

session = AmunSession()
turbine = session.get_turbine_by_name()

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

speeds = get_json("examples\data\example_windSpeed.json")
flow_parameters = UploadedWindParameters(
    uploadedWindStartTime="2017-01-01T00:00:00.000Z",
    lowHeight=SpeedAtHeight(10, speeds=speeds),
    granularityInMins=60,
)

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)
```

You can also use utils from Amun SDK for some common tasks like saving the response with load factors in a JSON file. For example, you can save a Weibull-based calculation giving it a timestamp, wind type and unique id for reference.

#### Saving response as JSON
```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import (
    WeibullParameters,
    LoadFactorBaseParameters
)
from aurora.amun.client.utils import save_to_json

session = AmunSession()
turbine = session.get_turbine_by_name()

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

flow_parameters = WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6)

load_factors = session.run_load_factor_for_parameters(
    flow_parameters, base_parameters
)

loadFactorRequestId = load_factors["parameters"]["loadFactorRequestId"]
save_to_json(
    f"load_factors_{datetime.now().isoformat().replace(':','_')}_{flow_parameters.windType}_{loadFactorRequestId}.json",
    load_factors
)
```

### Advanced Usage

Alternatively, you could run multiple load factor simulations in bulk using `run_load_factors_for_parameters_batch`.

#### Calculate Load Factors in batch
```python
from aurora.amun.client.parameters import (
    AverageWindSpeedParameters,
    BuiltInWindParameters,
    FlowParameters,
    LoadFactorBaseParameters,
    P50ScalingParameters,
    PowerDensityParameters,
    SpeedAtHeight,
    UploadedWindParameters,
    WeibullParameters,
    P50YieldScalingParameters,
)
from aurora.amun.client.session import AmunSession

session = AmunSession()
turbine = session.get_turbine_by_name()

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

list_of_parameters = [
    BuiltInWindParameters("era5"),
    WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6),
    PowerDensityParameters(measurementHeight=90, averagePowerDensity=400.1),
    AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=6.43),
    P50ScalingParameters(p50GrossProduction=0.4),
    P50YieldScalingParameters(annualProductionInGWHours=200),
    UploadedWindParameters(
        uploadedWindStartTime="2017-01-01T00:00:00.000Z",
        lowHeight=SpeedAtHeight(10, speeds=speeds),
        granularityInMins=60,
    ),
]
results = session.run_load_factors_for_parameters_batch(
    list_of_parameters,
    [base_parameters] * len(list_of_parameters) # This is needed to match every flow parameter with a base parameter
)

for result, params in zip(results, list_of_parameters):
    loadFactorRequestId = result["parameters"]["loadFactorRequestId"]
    save_to_json(
        f"load_factors/load_factors_{datetime.now().isoformat().replace(':','_')}_{params.windType}_{loadFactorRequestId}.json",
        result,
    )
```