import logging
from datetime import datetime

from aurora.amun.client.parameters import (
    AverageWindSpeedParameters,
    BuiltInWindParameters,
    LoadFactorBaseParameters,
    P50ScalingParameters,
    PowerDensityParameters,
    SpeedAtHeight,
    UploadedWindParameters,
    WeibullParameters,
    P50YieldScalingParameters,
)
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json, get_json

log = logging.getLogger(__name__)

# Submitting a batch of load factor calculations
# via run_load_factors_for_parameters_batch
def main():

    log.info(f"Starting")
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

    list_of_parameters = [
        BuiltInWindParameters("era5"),
        WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6),
        PowerDensityParameters(measurementHeight=90, averagePowerDensity=400.1),
        AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=6.43),
        P50ScalingParameters(p50GrossProduction=0.4),
        P50YieldScalingParameters(annualProductionInGWHours=200),
        UploadedWindParameters(
            uploadedWindStartTime="2017-01-01T00:00:00.000Z",
            lowHeight=SpeedAtHeight(10, speeds=get_json("examples\data\example_windSpeed.json")["speeds"]),
            granularityInMins=60,
        ),
    ]
    results = session.run_load_factors_for_parameters_batch(
        list_of_parameters, [base_parameters] * len(list_of_parameters)
    )

    for result, params in zip(results, list_of_parameters):
        loadFactorRequestId = result["parameters"]["loadFactorRequestId"]
        log.info(f"Got result for {loadFactorRequestId}")
        save_to_json(
            f"load_factors/load_factors_{datetime.now().isoformat().replace(':','_')}_{params.windType}_{loadFactorRequestId}.json",
            result,
        )


# More advanced example
# Submitting a batch of load factor calculations in stages
# via submit_load_factor_calculations
def submit_batch():
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

    # Make a list of coordinates
    coordinates = []
    for lat in range(500, 550, 5):
        for lon in range(-50, 0, 5):
            coordinates.append((lat/10, lon/10))
    
    # Construct configurations
    configs = []
    for (lat, lon) in coordinates:
        configs.append(get_configuration(lat, lon))
    
    print(coordinates)
    print(f"Submitting {len(configs)} configurations to run. First two:")
    print(configs[:2])

    # For future reference, you could save the tokens to a file to get the results later
    tokens = session.submit_load_factor_calculations(configs[:2])
    print(tokens)

    save_to_json("tokens.json", tokens)


# Get results for the calculations submitted in the previous example
def get_results_from_tokens():
    session = AmunSession()
    tokens = get_json("out/tokens.json")

    for token in tokens:
        result = session.get_load_factor_calculation(token)
        print(result)


if __name__ == "__main__":
    # main()
    # submit_batch()
    # get_results_from_tokens()