from copy import deepcopy
from functools import reduce


def summarize_hourly_output(hourly_speed_and_load_factors):
    def round_results(result):
        return {
            "dateTime": result["dateTime"],
            "windSpeed": round(result["windSpeed"], 6),
            "loadFactor": round(result["loadFactor"], 6),
        }
    first_day = hourly_speed_and_load_factors[:24]
    last_day = hourly_speed_and_load_factors[-24:]

    return {
        "first day": [round_results(result) for result in first_day],
        "last day": [round_results(result) for result in last_day],
        "count": len(hourly_speed_and_load_factors),
        "load factor sum": reduce(
            lambda a, b: round(a + b["loadFactor"], 6),
            hourly_speed_and_load_factors,
            0
        ),
        "wind speed sum": reduce(
            lambda a, b: round(a + b["windSpeed"], 6),
            hourly_speed_and_load_factors,
            0
        )
    }


def create_load_factor_snapshot(response):
    """
    Converts the output of the load factor API into an object that
    captures the key information for testing purposes
    """
    snapshot = {
        "parameters": deepcopy(response["parameters"]),
        "appliedParams": deepcopy(response["appliedParams"]),
    }
    typical_hourly = deepcopy(response["typicalHourly"])
    weather_year_hourly = deepcopy(response["weatherYearHourly"])

    snapshot["parameters"]["loadFactorRequestId"] = "SNAPSHOT"
    snapshot["typical summary"] = summarize_hourly_output(typical_hourly)
    snapshot["weatherYear summary"] = summarize_hourly_output(weather_year_hourly)

    return snapshot