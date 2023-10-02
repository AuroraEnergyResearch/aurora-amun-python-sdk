---
sidebar_label: parameters
title: parameters
---

## WindType Objects

```python
class WindType(Enum)
```

The types of wind to use in calculations

#### Era5

Uses the raw reanalysis dataset Era5. Check the region details endpoint for dataset availability.

#### UploadedWind

Uses the wind speeds uploaded by the user.

#### Generation

Uses generation data uploaded by the user.

#### Merra2

Uses the raw reanalysis dataset Merra2. Check the region details endpoint for dataset availability.

#### Weibull

Uses Weibull shape and scale parametes to estimate the wind speeds.

#### NEWA

Uses the raw reanalysis dataset NEWA. Check the region details endpoint for dataset availability.

#### P50Scaling

Uses P50 load factor parameter which represents the long-term production potential of this site.

#### PowerDensity

Uses power density of the site at a specific height to estimate the wind speeds.

#### AverageWindSpeed

Uses the average wind speed of the site at a specific height to estimate the wind speeds.

#### CalibratedGeneration

Uses the calibrated generation data uploaded by the user.

#### AuroraWindAtlas

Uses the reanalysis dataset calibrated using the AmunWindAtlas. Check the region details endpoint for dataset availability.

#### P50YieldScaling

Uses expectde annual production in GWh to estimate the wind speeds.

## SpeedAtHeight Objects

```python
class SpeedAtHeight()
```

The wind speeds at a given height,

**Arguments**:

- `height` _float_ - The measurement height (m) of the wind speeds.
  speeds (List[float]):A list of wind speeds in m/s.

## LoadFactorBaseParameters Objects

```python
class LoadFactorBaseParameters()
```

Parameters for all wind types.

**Notes**:

  Not all regions/locations support Multi-Turbine Power Curve Smoothing.
  

**Arguments**:

- `turbineModelId` _int_ - The Id of the Turbine to use in the calculation as returned from :meth:`.AmunSession.get_turbines`.
- `latitude` _float_ - The latitude of the point (-90 to 90).
- `longitude` _float_ - The latitude of the point (-180 to 180).
  
- `startTimeUTC` _str_ - The time in UTC that the calcution should start from. This must be in the form &#x27;*2016-07-28T00:00:00.000Z*&#x27; .
- `regionCode` _str_ - The code for the region used to set region specific parameters.
- `hubHeight` _float_ - Given in meters (m).
- `obstacleHeight` _float_ - Given in meters (m).
- `numberOfTurbines` _int_ - The number of turbines in the site.
- `roughnessLength` _float, optional_ - Static roughness. If not given, will be derived from reanalysis data. Defaults to None.
  usePowerCurveSmoothing (bool, optional):Should Default Multi-Turbine Power Curve Smoothing be used in the calculation if true then a region specific scale factor is used. If None then no smoothing is applied Defaults to None.
  useReanalysisCorrection(bool, optional):Should Reanalysis Correctionbe used only valid for ERA5, Defaults to False.
- `.AmunSession.get_turbines`0 _float_ - The value to use for smoothing. This will override any region specific values. This has no effect unless *usePowerCurveSmoothing* is true.
  lossesWake (float) default 0: The percentage to apply for wake loss. (0 &lt;= lossesWake &lt; 1)
  lossesAvailability (float) default 0: Percentage for external losses.  (0 &lt;= lossesAvailability &lt; 1)
  lossesElectrical (float) default 0: Percentage for external losses.  (0 &lt;= lossesElectrical &lt; 1)
  lossesTurbinePerformance (float) default 0: Percentage for external losses.  (0 &lt;= lossesTurbinePerformance &lt; 1)
  lossesEnvironmental (float) default 0: Percentage for external losses.  (0 &lt;= lossesEnvironmental &lt; 1)
  lossesOtherCurtailment (float) default 0: Percentage for external losses.  (0 &lt;= lossesOtherCurtailment &lt; 1)

## FlowParameters Objects

```python
class FlowParameters()
```

Base class for a flow. Internal Use only.

**Arguments**:

- `windType` _WindType_ - All flows must define a unique windtype as defined by the Amun http API.

## BuiltInWindParameters Objects

```python
class BuiltInWindParameters(FlowParameters)
```

The parameters used for built in wind calculations.

**Notes**:

  Not all locations support all wind types and not all locations support Regional Reanalysis Correction.
  

**Arguments**:

- `windType` _WindType_ - one of (WindType.Era5,WindType.Merra2,WindType.NEWA)
  useReanalysisCorrection (bool, optional):Should Regional Reanalysis Correction be enabled. If true then a location
  specific *reanalysisScaleCorrectionDelta* is used. Defaults to None.
- `reanalysisScaleCorrectionDelta` _float, optional_ - Override the location specific *reanalysisScaleCorrectionDelta*.
  This has no effect if *reanalysisScaleCorrectionDelta* is false. Defaults to None.

## WeibullParameters Objects

```python
class WeibullParameters(FlowParameters)
```

The parameters required for a *Weibull* calculation.

**Arguments**:

- `weibullShape` _float_ - The long term shape parameter from your wind report
- `weibullScale` _float_ - The long term scale parameter from your wind report
- `measurementHeight` _float_ - The height at which the measurements were taken (m)

## AverageWindSpeedParameters Objects

```python
class AverageWindSpeedParameters(FlowParameters)
```

The parameters required for a *AverageWindSpeed* calculation.

**Arguments**:

- `averageWindSpeed` _float_ - The average wind speed of your site to use as calibration (m/s)
- `measurementHeight` _float_ - The height at which the measurements were taken (m)

## PowerDensityParameters Objects

```python
class PowerDensityParameters(FlowParameters)
```

The parameters required for a *PowerDensity* calculation.

**Arguments**:

- `averagePowerDensity` _float_ - The average power density of your site to use as calibration (W/m2)
- `measurementHeight` _float_ - The height at which the measurements were taken (m)

## P50ScalingParameters Objects

```python
class P50ScalingParameters(FlowParameters)
```

The parameters required for a *P50Scaling* calculation.

**Arguments**:

- `p50GrossProduction` _float, 0 &lt; p50GrossProduction &lt; 1_ - the P50 load factor which represents the long-term production potential of this site,
  typically from an energy assessment report, will be used to calibrate the underlying reanalysis wind speed,
  such that the long-term production potential used in Amun-based valuations are the same.

## P50YieldScalingParameters Objects

```python
class P50YieldScalingParameters(FlowParameters)
```

The parameters required for a *P50YieldScaling* calculation.

**Arguments**:

- `annualProductionInGWHours` _float, 0 &lt; annualProductionInGWHours &lt; 1000000_ - the production expected by the site in a year in Gigawatt Hours.

## UploadedWindParameters Objects

```python
class UploadedWindParameters(FlowParameters)
```

The parameters required to run a custom (uploaded) load factor calculation.  If *highHeight*
is specified it must be the same length as the *lowHeight* and be measured at a greater height.
The speeds upload should be hourly measurements starting at *uploadedWindStartTime* and span at least 1 year.

**Arguments**:

- `uploadedWindStartTime` _str_ - The time in UTC that the wind speeds upload start from. This must be in the form &#x27;*2016-07-28T00:00:00.000Z*&#x27; .
- `lowHeight` _SpeedAtHeight_ - The height and speed for the low height wind speed to upload.
- `highHeight` _SpeedAtHeight, optional_ - The height and speed for the high height wind speed to upload. Defaults to None.

