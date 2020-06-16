from aurora_amun_sdk.amun import AmunSession
from aurora_amun_sdk.valuations import Valuations, WindType, Wind_Valuation

import logging
import logging.handlers
import os
from datetime import datetime
from aurora_amun_sdk.utils import save_to_json

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


if __name__ == "__main__":
    setup_file_and_console_loggers("create_valuation_example.log")
    log.setLevel(logging.DEBUG)  # Set Level for main logging in this file
    # Set Level for Amun SDK
    logging.getLogger("aurora_amun_sdk").setLevel(logging.DEBUG)

    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file HOME/.
    session = AmunSession()

    scenarios = session.get_scenarios("gbr")
    log.info(f"Scenarios {list(map(lambda x: x['name'],scenarios))}")
    valuations = Valuations(session)

    scenario_name = "Aurora Central weather years - 2020 April"
    region = "gbr"
    valuation = valuations.create_wind_valuation(
        Wind_Valuation(
            windType=WindType.era5,
            name=f"SDK Wind Farm {datetime.now()}",
            description="Created by Api",
            longitude="-1.21",
            latitude="59.59",
            turbine_model_name="Siemens SWT-4.0-130",
            numberOfTurbines=10,
            hubHeight=80,
            obstacleHeight=0,
            wakeLoss=0.1,
            roughnessLength=0.001,
        ),
        scenario_name=scenario_name,
        region=region,
    )
    log.info(f"Created {valuation['id']}")
    save_to_json(f"valuation_{valuation['id']}.json", valuation)

    results = session.get_valuation_results(valuation["id"])
    log.info(results["valuation"])
    save_to_json(f"valuation_results_{valuation['id']}.json", results)
    log.debug("Done")
