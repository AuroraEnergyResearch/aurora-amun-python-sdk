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
    #ddadf72f2fcede1cd7009454ab395a37c0528ecbdcbe277b43f7bef60398d07f
    #e52ff06e4f027e5b765bc423c045a12747983b5559d15d5cfde8f52f5a2d70de
    session = AmunSession("https://api-staging.auroraer.com/amun/v1", "ddadf72f2fcede1cd7009454ab395a37c0528ecbdcbe277b43f7bef60398d07f")
    turbines = session.get_turbines()

    parameters = {
        "windType": "averagewindspeed",
        "measurementHeight": 90,
        "averageWindSpeed": 6.43,
        "baseWindProfile": "era5",
        "turbineModelId": get_turbine_by_name(turbines, "Siemens SWT-4.0-130")["id"],
        "latitude": -27.274161,
        "longitude": 152.863770,
        "startTimeUTC": "2018-01-01T00:00:00.000Z",
        "regionCode": "aus_qld",
        "hubHeight": 90,
        "obstacleHeight": 0,
        "numberOfTurbines": 12,
        "roughnessLength": 0.02,
        "usePowerCurveSmoothing": False,
        "useIntradayCalibration": True,
    }

    load_factors = session.run_load_factor_calculation(parameters)

    loadFactorRequestId = load_factors["parameters"]["loadFactorRequestId"]
    log.info(f"Got result for {loadFactorRequestId}")
    save_to_json(
        f"load_factors/intraday_{datetime.now().isoformat().replace(':','_')}_{loadFactorRequestId}.json",
        load_factors,
    )

if __name__ == "__main__":
    main()
