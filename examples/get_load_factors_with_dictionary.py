from aurora.amun.client.session import AmunSession

import logging
import logging.handlers
import os
from datetime import datetime
from aurora.amun.client.utils import get_single_value_form_list, save_to_json, get_json

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


def get_turbine_by_name(turbines, turbine_name):
    return get_single_value_form_list(
        filter_function=lambda x: x["name"] == turbine_name,
        results_list=turbines,
        error=f"with name '{turbine_name}'",
    )


def main():
    setup_file_and_console_loggers("get_load_factors_example.log")
    log.info(f"Starting")
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file HOME/.
    session = AmunSession()
    turbines = session.get_turbines()

    windType = "AuroraWindAtlas"

    parameters = {
        "windType": windType,
        "turbineModelId": get_turbine_by_name(turbines, "Siemens SWT-4.0-130")["id"],
        "latitude": 59.59,
        "longitude": 0,
        "startTimeUTC": "2018-01-01T00:00:00.000Z",
        "regionCode": "GBR",
        "hubHeight": 90,
        "obstacleHeight": 0,
        "numberOfTurbines": 12,
        "roughnessLength": 0.02,
        "usePowerCurveSmoothing": False,
        # Optional
        # "lossesWake": 0.2,
        # "lossesAvailability": 0.02,
        # "lossesElectrical": 0.01,
        # "lossesTurbinePerformance": 0.1,
        # "lossesEnvironmental": 0.05,
        # "lossesOtherCurtailment": 0.0,
    }

    log.info(f"getting for {windType}")

    load_factors = session.run_load_factor_calculation(parameters)

    loadFactorRequestId = load_factors["parameters"]["loadFactorRequestId"]
    log.info(f"Got result for {loadFactorRequestId}")
    save_to_json(
        f"load_factors/load_factors_{datetime.now().isoformat().replace(':','_')}_{windType}_{loadFactorRequestId}.json",
        load_factors,
    )


if __name__ == "__main__":
    main()
