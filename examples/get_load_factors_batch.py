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

# Submitting a batch of load factor calculations
# via run_load_factors_for_parameters_batch
def main():
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
        usePowerCurveSmoothing=False
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
        loadFactorRequestId = result["parameters"]["loadFactorRequestId"]

        timestamp = datetime.now().isoformat().replace(':','_')
        save_to_json(
            f"load_factors/load_factors_{timestamp}_{params.windType}_{loadFactorRequestId}.json",
            result,
        )

if __name__ == "__main__":
    main()