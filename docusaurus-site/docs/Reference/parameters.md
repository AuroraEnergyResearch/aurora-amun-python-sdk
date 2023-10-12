---
sidebar_label: parameters
title: parameters
---

## WindType Objects

```python
class WindType(Enum)
```

The types of wind to use in calculations

#### AverageWindSpeed

Amun will use wind speed reanalysis data in the location and calibrate it so that the long-term average wind speed matched the user&#x27;s projection.

#### AuroraWindAtlas

Aurora&#x27;s high-resolution wind speed atlas based on Aurora&#x27;s data from existing wind farms. Check the region details for availability.

#### CalibratedGeneration

Hourly simulated production series in the same reference year as Aurora&#x27;s power market model uploaded by the user. The only adjustment made by Amun to this data will come from price-based economic curtailment.

#### Era5

ERA5 reanalysis dataset. Check the region details for availability.

#### Generation

At least one year of hourly metered or modelled production uploaded by the user. Amun will use this data create bespoke power curve that captures the relationship between reanalysis wind speed and observed generation.

#### Merra2

MERRA-2 reanalysis dataset. Check the region details for availability.

#### NEWA

NEWA reanalysis dataset. Check the region details for availability.

#### P50Scaling

Represents the site&#x27;s long-term P50 production potential as a load factor. Amun will calibrate underlying reanalysis wind speeds to match the long-term P50 load factor.

#### P50YieldScaling

Represents the site&#x27;s long-term production P50 potential as generation (GWh/year). Amun will calibrate underlying reanalysis wind speeds to match the long-term P50 production.

#### PowerDensity

Power Density is a quantitative measure of wind energy available at a location. Amun will calibrate underlying reanalysis wind speeds to match the average power density.

#### UploadedWind

Upload at least one year of hourly modelled or metered wind speed data to calibrate your wind speed profile. Amun will use this data to derive a statistical relationship between uploaded data and the reanalysis wind speed for the same location and time period uploaded.

#### Weibull

Weibull parameters represent the long-term wind speed distribution at the site. Amun will calibrate underlying reanalysis wind speeds distribution to match shape.

## SpeedAtHeight Objects

```python
class SpeedAtHeight()
```

The wind speeds at a given height,

**Arguments**:

- `height` _float_ - The measurement height (m) of the wind speeds.
- `speeds` _List[float]_ - A list of wind speeds in m/s.

## LoadFactorBaseParameters Objects

```python
class LoadFactorBaseParameters()
```

Parameters for all wind types.

**Notes**:

  Not all regions/locations support Multi-Turbine Power Curve Smoothing.
  

**Arguments**:

  - **turbineModelId** (int): The Id of the Turbine to use in the calculation as returned from `.AmunSession.get_turbines`.
  - **latitude** (float): The latitude of the point (-90 to 90).
  - **longitude** (float): The latitude of the point (-180 to 180).
  - **startTimeUTC** (str): The time in UTC that the calcution should start from. This must be in the form &#x27;*2016-07-28T00:00:00.000Z*&#x27; .
  - **regionCode** (str): The code for the region used to set region specific parameters.
  - **hubHeight** (float): Given in meters (m).
  - **obstacleHeight** (float): Given in meters (m).
  - **numberOfTurbines** (int): The number of turbines in the site.
  - **roughnessLength** (float, optional): Static roughness. If not given, will be derived from reanalysis data. Defaults to None.
  - **usePowerCurveSmoothing** (bool, optional): Should Default Multi-Turbine Power Curve Smoothing be used in the calculation if true then a region specific scale factor is used. If None then no smoothing is applied Defaults to None.
  - **useReanalysisCorrection** (bool, optional): Should Reanalysis Correctionbe used only valid for ERA5, Defaults to False.
  - **smoothingCoefficient** (float): The value to use for smoothing. This will override any region specific values. This has no effect unless *usePowerCurveSmoothing* is true.
  - **lossesWake** (float, default 0): The percentage to apply for wake loss. (0 &lt;= lossesWake &lt; 1)
  - **lossesAvailability** (float, default 0): Percentage for external losses.  (0 &lt;= lossesAvailability &lt; 1)
  - **lossesElectrical** (float, default 0): Percentage for external losses.  (0 &lt;= lossesElectrical &lt; 1)
  - **lossesTurbinePerformance** (float, default 0): Percentage for external losses.  (0 &lt;= lossesTurbinePerformance &lt; 1)
  - **lossesEnvironmental** (float, default 0): Percentage for external losses.  (0 &lt;= lossesEnvironmental &lt; 1)
  - **lossesOtherCurtailment** (float, default 0): Percentage for external losses.  (0 &lt;= lossesOtherCurtailment &lt; 1)

## FlowParameters Objects

```python
class FlowParameters()
```

Base class for a flow. Internal Use only.

**Arguments**:

- `windType` _WindType_ - All flows must define a unique windtype as defined by the Amun http API.

## AverageWindSpeedParameters Objects

```python
class AverageWindSpeedParameters(FlowParameters)
```

The parameters required for a *AverageWindSpeed* calculation.

**Arguments**:

- `averageWindSpeed` _float_ - The average wind speed of your site to use as calibration (m/s)
- `measurementHeight` _float_ - The height at which the measurements were taken (m)

## BuiltInWindParameters Objects

```python
class BuiltInWindParameters(FlowParameters)
```

The parameters used for built in wind calculations.

**Notes**:

  Not all locations support all wind types and not all locations support Regional Reanalysis Correction.
  

**Arguments**:

- `windType` _WindType_ - AuroraWindAtlas, Era5, Merra2, or NEWA
- `useReanalysisCorrection` _bool, optional_ - Should Regional Reanalysis Correction be enabled.
  If true then a location specific *reanalysisScaleCorrectionDelta* is used. Defaults to None.
- `reanalysisScaleCorrectionDelta` _float, optional_ - Override the location specific
  *reanalysisScaleCorrectionDelta*. This has no effect if *reanalysisScaleCorrectionDelta* is false. Defaults to None.

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

## PowerDensityParameters Objects

```python
class PowerDensityParameters(FlowParameters)
```

The parameters required for a *PowerDensity* calculation.

**Arguments**:

- `averagePowerDensity` _float_ - The average power density of your site to use as calibration (W/m2)
- `measurementHeight` _float_ - The height at which the measurements were taken (m)

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

## WeibullParameters Objects

```python
class WeibullParameters(FlowParameters)
```

The parameters required for a *Weibull* calculation.

**Arguments**:

- `weibullShape` _float_ - The long term shape parameter from your wind report
- `weibullScale` _float_ - The long term scale parameter from your wind report
- `measurementHeight` _float_ - The height at which the measurements were taken (m)

