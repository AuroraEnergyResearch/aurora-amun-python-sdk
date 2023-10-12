import pytest
import logging
from aurora.amun.client.session import AmunSession
from aurora.amun.client.parameters import AverageWindSpeedParameters, BuiltInWindParameters, LoadFactorBaseParameters


log = logging.getLogger(__name__)


@pytest.fixture
def amun_session():
    return AmunSession()


def test_era5(amun_session):
    log.info("Testing for era5: expect correct successful response with load factors")

    flow_parameters = BuiltInWindParameters("era5")
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
        roughnessLength=0.02,
        usePowerCurveSmoothing=False,
        useReanalysisCorrection=True,
    )
    result = amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters)
    assert isinstance(result, dict)
    assert "parameters" in result
    assert "appliedParams" in result
    assert "typicalHourly" in result
    assert "weatherYearHourly" in result


def test_era5_with_bad_base_parameters(amun_session):
    log.info("Testing for era5: expect error due to unsupported region")

    flow_parameters = BuiltInWindParameters("era5")
    base_parameters = LoadFactorBaseParameters(
        turbineModelId=amun_session.get_turbine_by_name("Siemens SWT-4.0-130")["id"],
        latitude=159.59,
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
        useReanalysisCorrection=True,
    )

    with pytest.raises(Exception) as exception:
        amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters)

    assert isinstance(exception.value, RuntimeError)
    assert "LonLatNotSupported" in str(exception.value)


def test_average_wind_speed_with_bad_flow_parameters(amun_session):
    log.info("Providing negative wind speed causes WOS to return error")

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
        roughnessLength=0.02,
        usePowerCurveSmoothing=False,
        useReanalysisCorrection=True,
    )
    
    result = amun_session.run_load_factor_for_parameters(flow_parameters, base_parameters)

    assert isinstance(result, str)
    assert "Wind speeds below minium value" in result

