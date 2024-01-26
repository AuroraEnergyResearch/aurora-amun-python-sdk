from enum import Enum
from typing import List

"""
Collection of classes used to define the parameters for a load factor calculation.
"""

class WindType(Enum):
    """The types of wind to use in calculations"""

    #: Amun will use wind speed reanalysis data in the location and calibrate it so that the long-term average wind speed matched the user's projection.
    AverageWindSpeed = "AverageWindSpeed"
    #: Aurora's high-resolution wind speed atlas based on Aurora's data from existing wind farms. Check the region details for availability.
    AuroraWindAtlas = "AuroraWindAtlas"
    #: Hourly simulated production series in the same reference year as Aurora's power market model uploaded by the user. The only adjustment made by Amun to this data will come from price-based economic curtailment.
    CalibratedGeneration = "CalibratedGeneration"
    #: ERA5 reanalysis dataset. Check the region details for availability.
    Era5 = "Era5"
    #: At least one year of hourly metered or modelled production uploaded by the user. Amun will use this data create bespoke power curve that captures the relationship between reanalysis wind speed and observed generation.
    Generation = "Generation"
    #: MERRA-2 reanalysis dataset. Check the region details for availability.
    Merra2 = "Merra2"
    #: NEWA reanalysis dataset. Check the region details for availability.
    NEWA = "NEWA"
    #: Represents the site's long-term P50 production potential as a load factor. Amun will calibrate underlying reanalysis wind speeds to match the long-term P50 load factor.
    P50Scaling = "P50Scaling"
    #: Represents the site's long-term production P50 potential as generation (GWh/year). Amun will calibrate underlying reanalysis wind speeds to match the long-term P50 production.
    P50YieldScaling = "P50YieldScaling"
    #: Power Density is a quantitative measure of wind energy available at a location. Amun will calibrate underlying reanalysis wind speeds to match the average power density.
    PowerDensity = "PowerDensity"
    #: Upload at least one year of hourly modelled or metered wind speed data to calibrate your wind speed profile. Amun will use this data to derive a statistical relationship between uploaded data and the reanalysis wind speed for the same location and time period uploaded.
    UploadedWind = "UploadedWind"
    #: TODO: write description, verify with Charlie or Hudson
    UploadedGeneration = "UploadedGeneration"
    #: Weibull parameters represent the long-term wind speed distribution at the site. Amun will calibrate underlying reanalysis wind speeds distribution to match shape.
    Weibull = "Weibull"


class SpeedAtHeight:
    """The wind speeds at a given height,

    Args:
        height (float): The measurement height (m) of the wind speeds.
        speeds (List[float]): A list of wind speeds in m/s.
    """

    def __init__(self, height: float, speeds: List[float]):
        self.height = height
        self.speeds = speeds

    def to_request_dictionary(self):
        return vars(self)


class LoadFactorBaseParameters:
    """Parameters for all wind types.

    Note:
        Not all regions/locations support Multi-Turbine Power Curve Smoothing.

    Args:
        - **turbineModelId** (int): The Id of the Turbine to use in the calculation as returned from `.AmunSession.get_turbines`.
        - **latitude** (float): The latitude of the point (-90 to 90).
        - **longitude** (float): The latitude of the point (-180 to 180).
        - **startTimeUTC** (str): The time in UTC that the calcution should start from. This must be in the form '*2016-07-28T00:00:00.000Z*' .
        - **regionCode** (str): The code for the region used to set region specific parameters.
        - **hubHeight** (float): Given in meters (m).
        - **obstacleHeight** (float): Given in meters (m).
        - **numberOfTurbines** (int): The number of turbines in the site.
        - **roughnessLength** (float, optional): Static roughness. If not given, will be derived from reanalysis data. Defaults to None.
        - **usePowerCurveSmoothing** (bool, optional): Should Default Multi-Turbine Power Curve Smoothing be used in the calculation if true then a region specific scale factor is used. If None then no smoothing is applied Defaults to None.
        - **useReanalysisCorrection** (bool, optional): Should Reanalysis Correctionbe used only valid for ERA5, Defaults to False.
        - **smoothingCoefficient** (float): The value to use for smoothing. This will override any region specific values. This has no effect unless *usePowerCurveSmoothing* is true.
        - **lossesWake** (float, default 0): The percentage to apply for wake loss. (0 <= lossesWake < 1)
        - **lossesAvailability** (float, default 0): Percentage for external losses.  (0 <= lossesAvailability < 1)
        - **lossesElectrical** (float, default 0): Percentage for external losses.  (0 <= lossesElectrical < 1)
        - **lossesTurbinePerformance** (float, default 0): Percentage for external losses.  (0 <= lossesTurbinePerformance < 1)
        - **lossesEnvironmental** (float, default 0): Percentage for external losses.  (0 <= lossesEnvironmental < 1)
        - **lossesOtherCurtailment** (float, default 0): Percentage for external losses.  (0 <= lossesOtherCurtailment < 1)
    """

    def __init__(
        self,
        turbineModelId: int,
        latitude: float,
        longitude: float,
        startTimeUTC: str,
        regionCode: str,
        hubHeight: float,
        obstacleHeight: float,
        numberOfTurbines: int,
        roughnessLength: float = None,
        usePowerCurveSmoothing: bool = None,
        useReanalysisCorrection: bool = False,
        smoothingCoefficient: float = None,
        lossesWake: float = 0.0,
        lossesAvailability: float = 0.0,
        lossesElectrical: float = 0.0,
        lossesTurbinePerformance: float = 0.0,
        lossesEnvironmental: float = 0.0,
        lossesOtherCurtailment: float = 0.0,
    ):
        self.turbineModelId = turbineModelId
        self.latitude = latitude
        self.longitude = longitude
        self.smoothingCoefficient = smoothingCoefficient
        self.startTimeUTC = startTimeUTC
        self.regionCode = regionCode
        self.hubHeight = hubHeight
        self.obstacleHeight = obstacleHeight

        self.numberOfTurbines = numberOfTurbines
        self.roughnessLength = roughnessLength
        self.usePowerCurveSmoothing = usePowerCurveSmoothing
        self.useReanalysisCorrection = useReanalysisCorrection

        self.lossesWake = lossesWake
        self.lossesAvailability = lossesAvailability
        self.lossesElectrical = lossesElectrical
        self.lossesTurbinePerformance = lossesTurbinePerformance
        self.lossesEnvironmental = lossesEnvironmental
        self.lossesOtherCurtailment = lossesOtherCurtailment


class FlowParameters:
    """Base class for a flow. Internal Use only.

    Args:
        windType (WindType): All flows must define a unique windtype as defined by the Amun http API.
    """

    def __init__(self, windType: WindType):
        self.windType = windType


class AverageWindSpeedParameters(FlowParameters):
    """The parameters required for a *AverageWindSpeed* calculation.

    Args:
        averageWindSpeed (float): The average wind speed of your site to use as calibration (m/s)
        measurementHeight (float): The height at which the measurements were taken (m)
    """

    def __init__(self, averageWindSpeed: float, measurementHeight: float):
        super().__init__(WindType.AverageWindSpeed)
        self.averageWindSpeed = averageWindSpeed
        self.measurementHeight = measurementHeight


class BuiltInWindParameters(FlowParameters):
    """The parameters used for built in wind calculations.

    Note:
        Not all locations support all wind types and not all locations support Regional Reanalysis Correction.

    Args:
        windType (WindType): AuroraWindAtlas, Era5, Merra2, or NEWA
        useReanalysisCorrection (bool, optional): Should Regional Reanalysis Correction be enabled.
            If true then a location specific *reanalysisScaleCorrectionDelta* is used. Defaults to None.
        reanalysisScaleCorrectionDelta (float, optional): Override the location specific
            *reanalysisScaleCorrectionDelta*. This has no effect if *reanalysisScaleCorrectionDelta* is false. Defaults to None.
    """

    def __init__(
        self,
        windType: WindType,
        useReanalysisCorrection: bool = None,
        reanalysisScaleCorrectionDelta: float = None,
    ):
        super().__init__(windType)
        self.useReanalysisCorrection = useReanalysisCorrection
        self.reanalysisScaleCorrectionDelta = reanalysisScaleCorrectionDelta


class P50ScalingParameters(FlowParameters):
    """The parameters required for a *P50Scaling* calculation.

    Args:
        p50GrossProduction (float, 0 < p50GrossProduction < 1):  the P50 load factor which represents the long-term production potential of this site,
            typically from an energy assessment report, will be used to calibrate the underlying reanalysis wind speed,
            such that the long-term production potential used in Amun-based valuations are the same.
    """

    def __init__(self, p50GrossProduction: float):
        super().__init__(WindType.P50Scaling)
        self.p50GrossProduction = p50GrossProduction


class P50YieldScalingParameters(FlowParameters):
    """The parameters required for a *P50YieldScaling* calculation.

    Args:
        annualProductionInGWHours (float, 0 < annualProductionInGWHours < 1000000):  the production expected by the site in a year in Gigawatt Hours.
    """

    def __init__(self, annualProductionInGWHours: float):
        super().__init__(WindType.P50YieldScaling)
        self.annualProductionInGWHours = annualProductionInGWHours


class PowerDensityParameters(FlowParameters):
    """The parameters required for a *PowerDensity* calculation.

    Args:
        averagePowerDensity (float): The average power density of your site to use as calibration (W/m2)
        measurementHeight (float): The height at which the measurements were taken (m)
    """

    def __init__(self, averagePowerDensity: float, measurementHeight: float):
        super().__init__(WindType.PowerDensity)
        self.averagePowerDensity = averagePowerDensity
        self.measurementHeight = measurementHeight


class UploadedWindParameters(FlowParameters):
    """The parameters required to run a custom (uploaded) load factor calculation.  If *highHeight*
    is specified it must be the same length as the *lowHeight* and be measured at a greater height.
    The speeds upload should be hourly measurements starting at *uploadedWindStartTime* and span at least 1 year.

    Args:
        uploadedWindStartTime (str): The time in UTC that the wind speeds upload start from. This must be in the form '*2016-07-28T00:00:00.000Z*' .
        lowHeight (SpeedAtHeight): The height and speed for the low height wind speed to upload.
        highHeight (SpeedAtHeight, optional): The height and speed for the high height wind speed to upload. Defaults to None.
    """

    def __init__(
        self,
        uploadedWindStartTime: str,
        lowHeight: SpeedAtHeight,
        highHeight: SpeedAtHeight = None,
        granularityInMins: int = 60,
    ):
        super().__init__(WindType.UploadedWind)
        self.uploadedWindStartTime = uploadedWindStartTime
        self.lowHeight = lowHeight
        self.highHeight = highHeight
        self.granularityInMins = granularityInMins


class WeibullParameters(FlowParameters):
    """The parameters required for a *Weibull* calculation.

    Args:
        weibullShape (float): The long term shape parameter from your wind report
        weibullScale (float): The long term scale parameter from your wind report
        measurementHeight (float): The height at which the measurements were taken (m)
    """

    def __init__(
        self, weibullShape: float, weibullScale: float, measurementHeight: float
    ):
        super().__init__(WindType.Weibull)
        self.weibullShape = weibullShape
        self.weibullScale = weibullScale
        self.measurementHeight = measurementHeight


class UploadedGenerationParameters(FlowParameters):
    """
    TODO: Add docs
    """

    def __init__(
        self,
        uploadGenerationStartTime: str,
        uploadedGeneration: List[float],
        installedCapacity: int,
        granularityInMins: int = 60,
    ):
        super().__init__(WindType.UploadedGeneration)
        self.uploadGenerationStartTime = uploadGenerationStartTime
        self.uploadedGeneration = uploadedGeneration
        self.installedCapacity = installedCapacity
        self.granularityInMins = granularityInMins