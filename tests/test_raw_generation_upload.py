import pytest
from datetime import datetime
import logging
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import UploadedGenerationParameters, LoadFactorBaseParameters
from aurora.amun.client.utils import get_json, get_scenario_by_name
from tests.utils import compare_load_factor_from_valuations_and_load_factor



log = logging.getLogger(__name__)


@pytest.fixture
def amun_session():
    return AmunSession()


def test_load_factor_to_valuation(amun_session, snapshot):
    log.info("""Checking that the load factor and valuation APIs
             provide the same result for hourly wind speeds and load factors""")

    # Parameters common to both valuation and load factor
    region = "gbr"
    longitude = 7.774
    latitude = 55.019
    hub_height = 120
    obstacle_height = 0
    generation_array = get_json("tests/test_data/generation.json")["generation"]
    generation_start_time_utc = "2015-12-31T23:00:00.000Z"
    installed_capacity = 288
    granularity_in_mins = 60
    use_reanalysis_correction = False
    use_power_curve_smoothing = False

    # Valuation specific parameters
    scenarios = amun_session.get_scenarios(region)
    scenario_name = "Great Britain Jan 23 (Central)"

    # Load factor specific parameters
    start_time_utc = "2013-01-01T00:00:00.000Z"

    # Run a valuation simulation
    valuation_parameters = {
        "name": f"SDK Wind Farm @ {datetime.now()}",
        "description": "Created by Python SDK test script",
        "longitude": longitude,
        "latitude": latitude,
        "scenarioId": get_scenario_by_name(scenarios, scenario_name)["id"],
        "hubHeight": hub_height,
        "obstacleHeight": obstacle_height,
        "useReanalysisCorrection": use_reanalysis_correction,
        "usePowerCurveSmoothing": use_power_curve_smoothing,
    }
    valuation = amun_session.create_valuation(valuation_parameters)
    amun_session.send_production_for_calibration(
        valuation["id"],
        {
            "generation": generation_array,
            "installedCapacity": installed_capacity,
            "startTime": generation_start_time_utc,
            "granularityInMins": granularity_in_mins,
        }
    )
    hourly_valuation_results = amun_session.get_valuation_results(
        valuation["id"], format="json", should_return_hourly_data=True
    )
    

    # Run a load factor simulation
    flow_parameters = UploadedGenerationParameters(
        uploadedGeneration = generation_array,
        uploadGenerationStartTime = generation_start_time_utc,
        installedCapacity = installed_capacity,
        granularityInMins = granularity_in_mins
    )
    base_parameters = LoadFactorBaseParameters(
        latitude = latitude,
        longitude = longitude,
        startTimeUTC = start_time_utc,
        regionCode = region,
        hubHeight = hub_height,
        obstacleHeight = obstacle_height,
        usePowerCurveSmoothing = use_power_curve_smoothing,
        useReanalysisCorrection = use_reanalysis_correction,
    )
    hourly_load_factor_results = amun_session.run_load_factor_for_parameters(
        flow_parameters, base_parameters, version=2
    )

    compare_load_factor_from_valuations_and_load_factor(hourly_load_factor_results, hourly_valuation_results)

