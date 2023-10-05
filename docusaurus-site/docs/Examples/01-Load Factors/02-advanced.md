---
title: Advanced Features
---

There are cases where you could benefit from running multiple load factor simulations in bulk using [`run_load_factors_for_parameters_batch`](/docs/Reference/session#run_load_factors_for_parameters_batch). In cases where you need to produce results for over 100 iterations, it will be faster than using common functions.

### Calculating load factors for all wind types
In this example, you can see how you can run load factor calculation iterating through different wind types

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

### Iterating though parameter values
You can iterate though values to conduct studies. For example, you can submit a large number of requests to see what results different average wind speed values produce

```python
from aurora.amun.client.parameters import AverageWindSpeedParameters
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

list_of_parameters = []
for speedTimes10 in np.arange(10, 150, 1):
    speed = speedTimes10 / 10   # So that we could interate more granularly
    list_of_parameter.append(AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=speed))

results = session.run_load_factors_for_parameters_batch(
    list_of_parameters,
    [base_parameters] * len(list_of_parameters) # This is needed to match every variant of wind speed with a base parameter
)

for result, params in zip(results, list_of_parameters):
    loadFactorRequestId = result["parameters"]["loadFactorRequestId"]
    save_to_json(
        f"load_factors/load_factors_{datetime.now().isoformat().replace(':','_')}_{params.windType}_{loadFactorRequestId}.json",
        result,
    )
```

### Submit calculations and collect results later
For this example, imagine that we want to evaluate load factors in 100 locations within the GBR region. It might take a while to calculate all of them, so we will first submit them at once.

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json, get_json
session = AmunSession()
turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")

# I want to run load factor calculation with the same parameters
# in 100 different locations
def get_configuration(lat: float, lon: float):
    return {
    "windType": "AuroraWindAtlas",
    "turbineModelId": turbine["id"],
    "latitude": lat,
    "longitude": lon,
    "startTimeUTC": "2018-01-01T00:00:00.000Z",
    "regionCode": "GBR",
    "hubHeight": 90,
    "obstacleHeight": 0,
    "numberOfTurbines": 12,
    "roughnessLength": 0.02,
    "usePowerCurveSmoothing": False,
}

# Make a list of coordinates within rectabgular area (50,55) -> (-5,0)
# 0.5 degrees apart
coordinates = []
for lat in range(500, 550, 5):
    for lon in range(-50, 0, 5):
        coordinates.append((lat/10, lon/10))

# Construct configurations
configs = []
for (lat, lon) in coordinates:
    configs.append(get_configuration(lat, lon))

# Submit the calculation requests and save tokens in a separate file to get the results later
tokens = session.submit_load_factor_calculations(configs)
save_to_json("tokens.json", tokens)
```

In some time, you can extract the results using those tokens. The results will be available for 30 days

```python
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json, get_json
session = AmunSession()
tokens = get_json("out/tokens.json")

for token in tokens:
    result = session.get_load_factor_calculation(token)
    lat = result["parameters"]["latitude"]
    lon = result["parameters"]["longitude"]
    save_to_json("load_factor_at({lat},{lon})", result)
```
