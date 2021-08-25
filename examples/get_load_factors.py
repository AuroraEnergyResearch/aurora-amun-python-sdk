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


def run_request_and_save(
    session, flow_parameters: FlowParameters, base_parameters: LoadFactorBaseParameters
):
    log.info(f"getting for {flow_parameters.windType}")

    load_factors = session.run_load_factor_for_parameters(
        flow_parameters, base_parameters
    )

    loadFactorRequestId = load_factors["parameters"]["loadFactorRequestId"]
    log.info(f"Got result for {loadFactorRequestId}")
    save_to_json(
        f"load_factors/load_factors_{datetime.now().isoformat().replace(':','_')}_{flow_parameters.windType}_{loadFactorRequestId}.json",
        load_factors,
    )


def main():
    setup_file_and_console_loggers("get_load_factors_example.log")
    log.info(f"Starting")
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file HOME/.
    session = AmunSession()
    turbines = session.get_turbines()

    base_parameters = LoadFactorBaseParameters(
        turbineModelId=get_turbine_by_name(turbines, "Siemens SWT-4.0-130")["id"],
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
    )

    run_request_and_save(session, BuiltInWindParameters("era5"), base_parameters)

    run_request_and_save(
        session,
        WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6),
        base_parameters,
    )
    run_request_and_save(
        session,
        PowerDensityParameters(measurementHeight=90, averagePowerDensity=400.1),
        base_parameters,
    )
    run_request_and_save(
        session,
        AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=6.43),
        base_parameters,
    )
    run_request_and_save(
        session, P50ScalingParameters(p50GrossProduction=0.4), base_parameters,
    )
    run_request_and_save(
        session,
        P50YieldScalingParameters(annualProductionInGwHours=2000),
        base_parameters,
    )
    speeds = get_json("examples\data\example_windSpeed.json")["speeds"]
    run_request_and_save(
        session,
        UploadedWindParameters(
            uploadedWindStartTime="2017-01-01T00:00:00.000Z",
            lowHeight=SpeedAtHeight(10, speeds=speeds),
        ),
        base_parameters,
    )


if __name__ == "__main__":
    main()
