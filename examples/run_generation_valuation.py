from aurora.amun.client.session import AmunSession

import logging
import logging.handlers
import os
from datetime import datetime
from aurora.amun.client.utils import save_to_json, get_json, get_scenario_by_name

log = logging.getLogger(__name__)

# Sets Up root logging console(INFO) and file (DEBUG) handlers
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


def main():
    setup_file_and_console_loggers("generation_valuation_example.log")
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file HOME/.
    session = AmunSession()

    region = "gbr"
    scenarios = session.get_scenarios(region)

    turbines = session.get_turbines()

    scenario_name = "Aurora Central Weather Years - 2020 April"

    valuation_parameters = {
        "windType": "era5",
        "name": f"SDK Wind Farm {datetime.now()}",
        "description": "Created by Api",
        "longitude": "-1.21",
        "latitude": "59.59",
        "scenarioId": get_scenario_by_name(scenarios, scenario_name)["id"],
    }

    valuation = session.create_valuation(valuation_parameters)

    log.info(f"Created {valuation['id']}")
    save_to_json(f"valuations/valuation_{valuation['id']}.json", valuation)

    # Check the json document for a complete structure of what is required
    # historicCalibration is for weather years
    session.send_calibrated_production(
        valuation["id"], get_json("examples\data\example_calibratedGeneration.json")
    )

    results = session.get_valuation_results(
        valuation["id"], format="json", should_return_hourly_data=False
    )
    log.info(f"Got result for {results['valuation']}")
    save_to_json(f"valuations/valuation_{valuation['id']}_out.json", results)
    log.info(f"Deleting {valuation['id']}")
    session.delete_valuation(valuation["id"])
    log.debug("Done")


if __name__ == "__main__":
    main()
