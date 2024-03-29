from copy import deepcopy
from functools import reduce


def summarize_hourly_output(hourly_speed_and_load_factors):
    """
    Extracts enough information from hourly speed and load factor 
    output to help capture correctness of the results.
    """
    hourly_load_factor = [result["loadFactor"] for result in hourly_speed_and_load_factors]
    hourly_wind_speed = [result["windSpeed"] for result in hourly_speed_and_load_factors]

    stats = {
        "total hours": len(hourly_speed_and_load_factors),
        "load factor sum": sum(hourly_load_factor),
        "load factor max": max(hourly_load_factor),
        "load factor min": min(hourly_load_factor),
        "wind speed sum": sum(hourly_wind_speed),
        "wind speed max": max(hourly_wind_speed),
        "wind speed min": min(hourly_wind_speed),
    }

    return {
        "first day": hourly_speed_and_load_factors[:24],
        "last day": hourly_speed_and_load_factors[-24:],
        "statistics": stats,
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

def compare_load_factor_from_valuations_and_load_factor(loadFactorResponse, valuationResponse):
    """
    Compares the output of the load factor API and the valuation API
    """
    
    load_hourly = loadFactorResponse['typicalHourly']
    valuation_hourly = valuationResponse['forecast']['hourly']

    valuation_formatted = {item['dateTime']: item for item in valuation_hourly}

    inconsistencies = {}
    inconsistencies_wind = {}

    for item in load_hourly:
        if item['loadFactor'] != valuation_formatted[item['dateTime']]['loadFactor']:
            inconsistencies[item['dateTime']] = valuation_formatted[item['dateTime']]['loadFactor'] - item['loadFactor']
        if item['windSpeed'] != valuation_formatted[item['dateTime']]['windSpeed']:
            inconsistencies_wind[item['dateTime']] = valuation_formatted[item['dateTime']]['windSpeed'] - item['windSpeed']

    assert inconsistencies.__len__() == 0
    assert inconsistencies_wind.__len__() == 0