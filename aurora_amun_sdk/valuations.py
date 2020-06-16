from aurora_amun_sdk.amun import AmunSession
from aurora_amun_sdk.utils import get_single_value_form_list
from enum import Enum


class WindType(Enum):
    era5 = 0
    uploadedwind = 1
    uploadedgeneration = 2
    merra2 = 3
    weibull = 4
    newa = 5
    p50scaling = 6
    powerdensity = 7
    AverageWindSpeed = 8


class Valuation:
    def __init__(self, windType: WindType, name, description, longitude, latitude):
        self.windType: WindType = windType
        self.name = name
        self.description = description
        self.longitude = longitude
        self.latitude = latitude


class Wind_Valuation(Valuation):
    def __init__(
        self,
        windType: WindType,
        name,
        description,
        longitude,
        latitude,
        turbine_model_name,
        numberOfTurbines,
        hubHeight,
        obstacleHeight,
        wakeLoss,
        roughnessLength,
    ):
        super().__init__(windType, name, description, longitude, latitude)
        self.turbine_model_name = turbine_model_name
        self.numberOfTurbines = numberOfTurbines
        self.hubHeight = hubHeight
        self.obstacleHeight = obstacleHeight
        self.wakeLoss = wakeLoss
        self.roughnessLength = roughnessLength


class Valuations:
    def __init__(self, session: AmunSession):
        self.session = session

    def create_wind_valuation(self, valuation: Wind_Valuation, scenario_name, region):
        valuation = {
            "name": valuation.name,
            "description": valuation.description,
            "longitude": valuation.longitude,
            "latitude": valuation.latitude,
            "turbineModelId": self.get_turbine_by_name(valuation.turbine_model_name)[
                "id"
            ],
            "numberOfTurbines": valuation.numberOfTurbines,
            "hubHeight": valuation.hubHeight,
            "obstacleHeight": valuation.obstacleHeight,
            "wakeLoss": valuation.wakeLoss,
            "roughnessLength": valuation.roughnessLength,
            "scenarioId": self.get_scenario_by_name(scenario_name, region)["id"],
            "windType": valuation.windType.name,
        }

        return self.session.create_valuation(valuation)

    def get_scenario_by_name(self, scenario_name, region):
        scenarios = self.session.get_scenarios(region)
        return get_single_value_form_list(
            filter_function=lambda x: x["name"] == scenario_name,
            results_list=scenarios,
            error=f"with name '{scenario_name}' in region '{region}'",
        )

    def get_turbine_by_name(self, turbine_name):
        turbines = self.session.get_turbines()
        return get_single_value_form_list(
            filter_function=lambda x: x["name"] == turbine_name,
            results_list=turbines,
            error=f"with name '{turbine_name}'",
        )

    def get_valuation(self, id):
        pass

    def get_valuation_result(self, id):
        pass

    def download_valuation_result_as_excel(self, id, filepath):
        pass
