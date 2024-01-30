
from aurora.amun.client.parameters import LoadFactorBaseParameters, UploadedGenerationParameters
from aurora.amun.client.session import AmunSession
import logging

from aurora.amun.client.utils import get_json, save_to_json


log = logging.getLogger(__name__)



def main():
    # setup_file_and_console_loggers("generation_valuation_example.log")
    # Calling with no token in constructor will load one from an environment variable if provided
    session = AmunSession()

    # Setting the initial variables used for the load factor.
    region = "gbr"
    longitude = 7.774
    latitude = 55.019
    hub_height = 120
    obstacle_height = 0
    generation_array = get_json("tests/test_data/generation.json")["generation"]
    # When did the collection of the data start?
    generation_start_time_utc = "2015-12-31T23:00:00.000Z"
    # When do you want the returned data to start?
    start_time_utc = "2013-01-01T00:00:00.000Z"
    installed_capacity = 288
    granularity_in_mins = 60
    use_reanalysis_correction = False
    use_power_curve_smoothing = False
 
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

    loadfactor = session.run_load_factor_for_parameters(flow_parameters, base_parameters, version=1)

    log.info(f"Got result for {loadfactor}")
    save_to_json(f"loadfactor/loadfactor_{loadfactor['params']['loadFactorRequestId']}.json", loadfactor)
    log.debug("Done")


if __name__ == "__main__":
    main()