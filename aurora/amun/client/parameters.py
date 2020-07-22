class LoadFactorBaseParameters:
    """Parameters for all wind types.

        Note:
            Not all regions/locations support Multi-Turbine Power Curve Smoothing.

        Args:
            turbineModelId (int): The Id of the Turbine to use in the calculation as returned from :meth:`.AmunSession.get_turbines`.
            latitude (float): The latitude of the point (-90 to 90).
            longitude (float): The latitude of the point (-180 to 180).

            startTimeUTC (str): The time in UTC that the calcution should start from. This must be in the form '*2016-07-28T00:00:00.000Z*' .
            regionCode (str): The code for the region used to set region specific parameters.
            hubHeight (float): Given in meters (m).
            obstacleHeight (float): Given in meters (m).
            wakeLoss (float): Static roughness. If not given, will be derived from reanalysis data,
            numberOfTurbines (int): 
            roughnessLength (float, optional): Static roughness. If not given, will be derived from reanalysis data. Defaults to None.
            usePowerCurveSmoothing (bool, optional):Should Default Multi-Turbine Power Curve Smoothing be used in the calculation if true then a region specific scale factor is used. If None then no smoothing is applied Defaults to None.
            smoothingCoefficient (float): The value to use for smoothing. This will override any region specific values. This has no effect unless *usePowerCurveSmoothing* is true.
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
        wakeLoss: float,
        numberOfTurbines: int,
        roughnessLength: float = None,
        usePowerCurveSmoothing: bool = None,
        smoothingCoefficient: float = None,
    ):
        self.turbineModelId = turbineModelId
        self.latitude = latitude
        self.longitude = longitude
        self.smoothingCoefficient = smoothingCoefficient
        self.startTimeUTC = startTimeUTC
        self.regionCode = regionCode
        self.hubHeight = hubHeight
        self.obstacleHeight = obstacleHeight
        self.wakeLoss = wakeLoss
        self.numberOfTurbines = numberOfTurbines
        self.roughnessLength = roughnessLength
        self.usePowerCurveSmoothing = usePowerCurveSmoothing


class FlowParameters:
    """Base class for a flow. Internal Use only. 

        Args:
            windType (str): All flows must define a unique windtype as defined by the Amun http API.
    """

    def __init__(self, windType: str):

        self.windType = windType


class BuiltInWindParameters(FlowParameters):
    """The parameters used for built in wind calculations (*era5*,*merra2*,*newa*). 

        Note:
            Not all locations support all wind types and not all locations support Regional Reanalysis Correction.

        Args:
            windType (str): one of ("era5","merra2","newa")
            useReanalysisCorrection (bool, optional):Should Regional Reanalysis Correction be enabled. If true then a location 
            specific *reanalysisScaleCorrectionDelta* is used. Defaults to None.
            reanalysisScaleCorrectionDelta (float, optional): Override the location specific *reanalysisScaleCorrectionDelta*. 
            This has no effect if *reanalysisScaleCorrectionDelta* is false. Defaults to None.
    """

    def __init__(
        self,
        windType: str,
        useReanalysisCorrection: bool = None,
        reanalysisScaleCorrectionDelta: float = None,
    ):
        super().__init__(windType)
        self.useReanalysisCorrection = useReanalysisCorrection
        self.reanalysisScaleCorrectionDelta = reanalysisScaleCorrectionDelta


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

        super().__init__("weibull")
        self.weibullShape = weibullShape
        self.weibullScale = weibullScale
        self.measurementHeight = measurementHeight


class AverageWindSpeedParameters(FlowParameters):
    """The parameters required for a *AverageWindSpeed* calculation.

        Args:
            averageWindSpeed (float): The average wind speed of your site to use as calibration (m/s)
            measurementHeight (float): The height at which the measurements were taken (m)
    """

    def __init__(self, averageWindSpeed: float, measurementHeight: float):

        super().__init__("averageWindSpeed")
        self.averageWindSpeed = averageWindSpeed
        self.measurementHeight = measurementHeight


class PowerDensityParameters(FlowParameters):
    """The parameters required for a *PowerDensity* calculation.

        Args:
            averagePowerDensity (float): The average power density of your site to use as calibration (W/m2)
            measurementHeight (float): The height at which the measurements were taken (m)
    """

    def __init__(self, averagePowerDensity: float, measurementHeight: float):

        super().__init__("PowerDensity")
        self.averagePowerDensity = averagePowerDensity
        self.measurementHeight = measurementHeight

