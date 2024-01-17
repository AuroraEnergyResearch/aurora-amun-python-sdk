import os
import logging
import logging.handlers
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

log = logging.getLogger(__name__)


# Sets Up root loging console(INFO) and file (DEBUG) handlers
def setup_file_and_console_loggers(fileName):
    os.makedirs("logs", exist_ok=True)
    rotFileHandler = logging.handlers.RotatingFileHandler(
        f"logs/{fileName}", "a", 30 * 1024 * 1024, 10
    )
    f = logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    rotFileHandler.setFormatter(f)
    rotFileHandler.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    )
    logger = logging.getLogger()
    logger.addHandler(rotFileHandler)
    logger.addHandler(consoleHandler)
    log.setLevel(logging.DEBUG)  # Set Level for main logging in this file
    # Set Level for Amun SDK
    logging.getLogger("aurora.amun").setLevel(logging.DEBUG)

    #

# Submitting a batch of load factor calculations
# via run_load_factors_for_parameters_batch
def main():
    setup_file_and_console_loggers("get_load_factors_batch_example.log")
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