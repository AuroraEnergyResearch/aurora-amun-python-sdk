---
title: Advanced Features
---

There are cases where you could benefit from running multiple load factor simulations in bulk using [`run_load_factors_for_parameters_batch`](/docs/Reference/session#run_load_factors_for_parameters_batch). In cases where you need to produce results for over 100 iterations, it will be faster than using common functions.

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