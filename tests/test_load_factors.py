import pytest
import logging
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import AverageWindSpeedParameters, BuiltInWindParameters, LoadFactorBaseParameters, P50ScalingParameters, WeibullParameters
from tests.utils import create_load_factor_snapshot



log = logging.getLogger(__name__)


@pytest.fixture
def amun_session():
    return AmunSession()


def test_era5(amun_session):
    log.info("Testing for era5: expect correct successful response with load factors")

    flow_parameters = BuiltInWindParameters("era5", True)
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=59.59,
        longitude=0,
        startTimeUTC="2018-01-01T00:00:00.000Z",
        regionCode="GBR",
        hubHeight=90,
        obstacleHeight=0,
        lossesAvailability=0.1,
        lossesWake=0,
        numberOfTurbines=12,
        usePowerCurveSmoothing=False
    )
    result = amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters)
    assert isinstance(result, dict)
    assert "parameters" in result
    assert "appliedParams" in result
    assert "typicalHourly" in result
    assert "weatherYearHourly" in result


def test_era5_with_bad_base_parameters(amun_session):
    log.info("Testing for era5: expect error due to unsupported region")

    flow_parameters = BuiltInWindParameters("era5", True)
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=84,
        longitude=0,
        startTimeUTC="2018-01-01T00:00:00.000Z",
        regionCode="GBR",
        hubHeight=90,
        obstacleHeight=0,
        lossesAvailability=0.1,
        lossesWake=0,
        numberOfTurbines=12,
        usePowerCurveSmoothing=False
    )

    with pytest.raises(Exception) as exception:
        amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters)

    assert isinstance(exception.value, RuntimeError)
    assert "LonLatNotSupported" in str(exception.value)


def test_average_wind_speed_with_bad_flow_parameters(amun_session):
    """
    WOS-level exceptions are handeled differently by 2 API versions:
    - API v1: an exception is raised
    - API v2: an error is recorded in the result object
    For API-level exceptions, an exception is always raised (see test above)
    """
    log.info("Providing negative wind speed causes WOS to return error in the result")

    flow_parameters = AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=-11)
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=59.59,
        longitude=0,
        startTimeUTC="2018-01-01T00:00:00.000Z",
        regionCode="GBR",
        hubHeight=90,
        obstacleHeight=0,
        lossesAvailability=0.1,
        lossesWake=0,
        numberOfTurbines=12,
        usePowerCurveSmoothing=False
    )

    # An exception is raised for API v1
    with pytest.raises(Exception) as exception:
        amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters, version=1)
    assert "Wind speeds below minium value" in str(exception.value)
    
    # No exception is raised for API v2 in this case! This is so that if one load factor
    # calculation fails, the rest can still be calculated. Instead of raising,
    # we record the error in the result object.
    result = amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters, version=2)
    assert isinstance(result, str)
    assert "Wind speeds below minium value" in result


def test_bulk_calculation(amun_session):
    log.info("Requesting to run 5 simulations in bulk: should return a list of 5 valid results")

    list_of_flow_parameters = [
        WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6),
        WeibullParameters(measurementHeight=90, weibullScale=12.5, weibullShape=6),
        WeibullParameters(measurementHeight=90, weibullScale=13, weibullShape=6),
        WeibullParameters(measurementHeight=90, weibullScale=13.5, weibullShape=6),
        WeibullParameters(measurementHeight=90, weibullScale=14, weibullShape=6),
    ]
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=59.59,
        longitude=0,
        startTimeUTC="2018-01-01T00:00:00.000Z",
        regionCode="GBR",
        hubHeight=90,
        obstacleHeight=0,
        lossesAvailability=0.1,
        lossesWake=0,
        numberOfTurbines=12,
        usePowerCurveSmoothing=False
    )

    results = amun_session.run_load_factors_for_parameters_batch(
        list_of_flow_parameters,
        [base_parameters] * len(list_of_flow_parameters) # We must match every flow parameter with a base parameter
    )

    assert isinstance(results, list)
    assert len(results) == len(list_of_flow_parameters)
    assert all(isinstance(result, dict) for result in results)


def test_v1_and_v2_calculations(amun_session, snapshot):
    log.info("""Checking that the the interface for v1 and v2 calculations
             is the same and they return the same results""")
    
    flow_parameters = P50ScalingParameters(p50GrossProduction=0.4)
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=-22.715390,
        longitude=151.303711,
        startTimeUTC="2018-01-01T00:00:00.000Z",
        regionCode="aus_qld",
        hubHeight=90,
        obstacleHeight=0,
        lossesAvailability=0.1,
        lossesWake=0,
        numberOfTurbines=12,
        usePowerCurveSmoothing=False
    )

    # The only thing that changes between usage of v1 and v2 is the version number
    result_v1 = amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters, version=1)
    result_v2 = amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters, version=2)

    # There is data for each hour of the year - that's too much!
    # Summatise the data to make it easier to compare and remove uuids
    result_v1_sumamry = create_load_factor_snapshot(result_v1)
    result_v2_sumamry = create_load_factor_snapshot(result_v2)

    # Results from the two versions should be the same
    snapshot.assert_match(result_v1_sumamry, "result_v1")
    snapshot.assert_match(result_v2_sumamry, "result_v1")


def test_unsupported_version(amun_session):
    log.info("""Must raise an exception if the version is not supported""")
    
    flow_parameters = P50ScalingParameters(p50GrossProduction=0.4)
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=-22.715390,
        longitude=151.303711,
        startTimeUTC="2018-01-01T00:00:00.000Z",
        regionCode="aus_qld",
        hubHeight=90,
        obstacleHeight=0,
        lossesAvailability=0.1,
        lossesWake=0,
        numberOfTurbines=12,
        usePowerCurveSmoothing=False
    )

    with pytest.raises(Exception) as exception:
        amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters, version=3)

    assert isinstance(exception.value, ValueError)
    assert str(exception.value) == "Invalid version number: only versions 1 and 2 are allowed"