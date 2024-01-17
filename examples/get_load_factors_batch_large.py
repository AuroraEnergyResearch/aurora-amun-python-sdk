import os
import logging
import logging.handlers
from datetime import datetime
import time
from aurora.amun.client.parameters import (
    AverageWindSpeedParameters,
    LoadFactorBaseParameters,
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
    consoleHandler.setLevel(logging.DEBUG)
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

def request_simulations(number: int, batch: bool, version: int):
    session = AmunSession("https://api-staging.auroraer.com/amun/v1", "36630c69063314ef248db53b11e848530b625dd2f1aa6c76798ad5abf062299d")
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

    start_time = time.time()

    if batch:
        variants = []
        for _ in range(0, number):
            variants.append(AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=12))

        session.run_load_factors_for_parameters_batch(
            variants,
            [base_parameters] * len(variants) # This is needed to match every variant of wind speed with a base parameter
        )
    else:
        for _ in range(0, number):
            flow_parameters = AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=12)
            session.run_load_factor_for_parameters(
                flow_parameters, base_parameters, version
            )
    
    end_time = time.time()
    print(f"Finished running {number} sims using APIv{version} in {'batch' if batch else 'sequence'} in: {end_time - start_time} seconds")


# Submitting a batch of load factor calculations
# via run_load_factors_for_parameters_batch
def main():
    setup_file_and_console_loggers("get_load_factors_batch_large.log")
    request_simulations(number=100, batch=False, version=1)

if __name__ == "__main__":
    main()