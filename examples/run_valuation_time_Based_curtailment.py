from aurora.amun.client.session import AmunSession

import logging
import logging.handlers
import os
from datetime import datetime
from aurora.amun.client.utils import get_single_value_form_list, save_to_json

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

    #


def get_scenario_by_name(scenarios, scenario_name: str):
    return get_single_value_form_list(
        filter_function=lambda x: x["name"] == scenario_name,
        results_list=scenarios,
        error=f"with name '{scenario_name}'",
    )


def get_turbine_by_name(turbines, turbine_name):
    return get_single_value_form_list(
        filter_function=lambda x: x["name"] == turbine_name,
        results_list=turbines,
        error=f"with name '{turbine_name}'",
    )


def main():
    setup_file_and_console_loggers("run_valuation_time_Based_curtailment.log")
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file HOME/.
    session = AmunSession()

    region = "gbr"
    scenarios = session.get_scenarios(region)

    turbines = session.get_turbines()

    #  scenario_name = "Aurora Central Weather Years - 2020 April"
    scenario_name = "Aurora Central - 2020 October"
    valuation_parameters = {
        "windType": "era5",
        "name": f"SDK Wind Farm {datetime.now()}",
        "description": "Created by Api",
        "longitude": "-1.21",
        "latitude": "59.59",
        "turbineModelId": get_turbine_by_name(turbines, "Siemens SWT-4.0-130")["id"],
        "numberOfTurbines": 10,
        "hubHeight": 90,
        "obstacleHeight": 0,
        "roughnessLength": 0.001,
        "scenarioId": get_scenario_by_name(scenarios, scenario_name)["id"],
        # Optional
        # "lossesWake": 0.2,
        # "lossesAvailability": 0.02,
        # "lossesElectrical": 0.01,
        # "lossesTurbinePerformance": 0.1,
        # "lossesEnvironmental": 0.05,
        # "lossesOtherCurtailment": 0.0,
        "timeBasedCurtailmentThresholds": [
            {"threshold": 10, "timeValidFrom": "2024-01-01T00:00:00.000Z",},
            {"threshold": 20, "timeValidFrom": "2028-01-01T00:00:00.000Z",},
            {"threshold": 40, "timeValidFrom": "2032-01-01T00:00:00.000Z",},
            {"threshold": 60, "timeValidFrom": "2036-01-01T00:00:00.000Z",},
            {"threshold": 80, "timeValidFrom": "2040-01-01T00:00:00.000Z",},
            {"threshold": 100, "timeValidFrom": "2044-01-01T00:00:00.000Z",},
            {"threshold": 120, "timeValidFrom": "2048-01-01T00:00:00.000Z",},
        ],
    }

    valuation = session.create_valuation(valuation_parameters)

    log.info(f"Created {valuation['id']}")
    save_to_json(f"valuations/valuation_{valuation['id']}.json", valuation)

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
