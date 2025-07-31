---
title: Advanced Features
---

There are cases where you could benefit from running multiple load factor simulations in bulk using [`run_load_factors_for_parameters_batch`](/docs/Reference/session#run_load_factors_for_parameters_batch). In cases where you need to produce results for over 100 iterations, it will be faster than using common functions.

### Calculating load factors for all wind types
In this example, you can see how you can run load factor calculation iterating through different wind types. You can do it by creating a base parameters objects that all the calculations will use (`base_parameters`) and create a list of parameters for individual requests (`list_of_parameters`). After this, you can send all the requests. Be aware that you will need to provide the same number of base parameters and flow parameters because they are paired with each other.

```python
from datetime import datetime
from aurora.amun.client.parameters import (
    AverageWindSpeedParameters,
    BuiltInWindParameters,
    LoadFactorBaseParameters,
    P50ScalingParameters,
    PowerDensityParameters,
    WeibullParameters,
    P50YieldScalingParameters,
)
from aurora.amun.client.session import AmunSession
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
    lossesAvailability=0.1,
    lossesWake=0,
    numberOfTurbines=12,
    usePowerCurveSmoothing=False,
    useReanalysisCorrection=False,
)

list_of_parameters = [
    BuiltInWindParameters("era5"),
    WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6),
    PowerDensityParameters(measurementHeight=90, averagePowerDensity=400.1),
    AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=6.43),
    P50ScalingParameters(p50GrossProduction=0.4),
    P50YieldScalingParameters(annualProductionInGWHours=200)
]

print("Running load factor calculations. This will take a few minutes...")
results = session.run_load_factors_for_parameters_batch(
    list_of_parameters,
    [base_parameters] * len(list_of_parameters) # We must match every flow parameter with a base parameter
)

# Save each result individually pairing it with the request parameters
# (the results come in the same order as the requests)
for result, params in zip(results, list_of_parameters):
    
    # If you want, you can use a unique identifier for each request in the name of your file
    # You can later use this ID to request the results of this specific request again later
    loadFactorRequestId = result["parameters"]["loadFactorRequestId"]

    timestamp = datetime.now().isoformat().replace(':','_')
    save_to_json(
        f"load_factors/load_factors_{timestamp}_{params.windType}_{loadFactorRequestId}.json",
        result,
    )
```

You will see 6 result files in the `out/load_factors/` directory. This approach will be faster than using [`AmunSession.run_load_factors_for_parameters`](/docs/Reference/session#run_load_factor_for_parameters) in a for-loop

### Iterating though parameter values
You can iterate though values to conduct studies. For example, you can submit a large number of requests to see what results different average wind speed values produce

```python
from aurora.amun.client.parameters import AverageWindSpeedParameters, LoadFactorBaseParameters
from aurora.amun.client.session import AmunSession
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
    lossesAvailability=0.1,
    lossesWake=0,
    numberOfTurbines=12,
    usePowerCurveSmoothing=False,
    useReanalysisCorrection=False,
)

# Wind speeds from 1.0 to 15.0 m/s in 0.1 m/s increments
variants = []
for speedTimes10 in range(10, 150, 1):
    speed = speedTimes10 / 10   # So that we could iterate more granularly
    variants.append(AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=speed))

print("Running load factor calculations. This will take a few minutes...")
results = session.run_load_factors_for_parameters_batch(
    variants,
    [base_parameters] * len(variants) # This is needed to match every variant of wind speed with a base parameter
)

for result, variant in zip(results, variants):
    save_to_json(
        f"load_factors/load_factors_for_avg_wind_speed_{variant.averageWindSpeed}.json",
        result,
    )
```

At the time this example was written, it took 29 minutes to run these 100 calculations.