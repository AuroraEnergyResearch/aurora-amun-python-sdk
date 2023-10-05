from typing import Dict, List

"""
Defines the format of responses returned by the Amun API.
"""


class RegionDetail:
    """The details about a region required to construct valid valuation and load factor requests.

      Args:
          pmfCode (str): The *regionCode* to use when required to look up more details e.g. which scenarios are available. `.AmunSession.get_scenarios`
          defaultWind (str): The dataset used by default in calculations
          availableDatasets (List[str]): A list of datasets that are available for the region.
          era5CorrectionEnabled (bool): Is era5 correction available for the region.
          powerCurveSmoothingEnabled (bool): Is power curve smoothing available for the region.
    """

    def __init__(
        self,
        pmfCode: str,
        defaultWind: str,
        availableDatasets: List[str],
        era5CorrectionEnabled: bool,
        powerCurveSmoothingEnabled: bool,
    ):

        self.pmfCode = pmfCode
        self.defaultWind = defaultWind
        self.availableDatasets = availableDatasets
        self.era5CorrectionEnabled = era5CorrectionEnabled
        self.powerCurveSmoothingEnabled = powerCurveSmoothingEnabled

    def __str__(self):
        return "RegionDetail->" + str(vars(self))


def get_RegionDetail_from_response(resp: Dict) -> RegionDetail:
    return RegionDetail(
        pmfCode=resp["pmfCode"],
        defaultWind=resp["defaultWind"],
        availableDatasets=resp["availableDatasets"],
        era5CorrectionEnabled=resp["era5CorrectionEnabled"],
        powerCurveSmoothingEnabled=resp["powerCurveSmoothingEnabled"],
    )
