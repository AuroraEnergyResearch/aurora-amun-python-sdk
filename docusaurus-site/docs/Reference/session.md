---
sidebar_label: session
title: session
---

## APISession Objects

```python
class APISession()
```

Internal class to hold base methods for interacting with the Aurora HTTP API

## AmunSession Objects

```python
class AmunSession(APISession)
```

Manage access to the Amun API.

By default the session will connect to the production Amun API endpoint. This can be overridden by passing the base_url into the constructor
or by setting the environment variable *AURORA_API_BASE_URL*. This is for internal use only.

The authentication token is read from the users home directory *$home/.aurora-api-key* e.g. *C:/Users/Joe Bloggs/.aurora-api-key*.
This can be overridden by passing the token into the constructor or by setting the environment variable *AURORA_API_KEY*.


**Arguments**:

- `base_url` _string, optional_ - Override the base url used to contact the Amun API. Defaults to None.
- `token` _string, optional_ - Overide the api authentication token used for API access. Defaults to None.

#### get\_turbines

```python
def get_turbines()
```

Get the turbines available to the user.

**Response example**:
```json
    [{
        'id': 29,
        'manufacturer': 'EWT Directwind',
        'name': 'EWT Directwind 2000/96',
        'ratedCapacity': 2,
        'rotorDiameter': 96,
        'minHubHeight': None,
        'maxHubHeight': None,
        'cutInSpeed': 3.5,
        'cutOutSpeed': 25,
        'specSource': 'https://www.thewindpower.net/turbine_en_879_ewt_directwind-2000-96.php',
        'type': 'public',
        },
            ...
```

#### get\_turbine\_by\_name

```python
def get_turbine_by_name(turbine_name)
```

Get turbine information by name.

**Returns**:

  A dictionary with the turbine information. If not found, raises an error.
  
  **Response example**:
```json
    {
        'id': 29,
        'manufacturer': 'EWT Directwind',
        'name': 'EWT Directwind 2000/96',
        'ratedCapacity': 2,
        'rotorDiameter': 96,
        'minHubHeight': None,
        'maxHubHeight': None,
        'cutInSpeed': 3.5,
        'cutOutSpeed': 25,
        'specSource': 'https://www.thewindpower.net/turbine_en_879_ewt_directwind-2000-96.php',
        'type': 'public',
    }
```

#### get\_power\_curve

```python
def get_power_curve(turbine_id)
```

Get the power curve for a turbine.

**Arguments**:

- `turbine_id` _int_ - The id of the turbine. To get ID (with additional info), refer to `AmunSession.get_turbines`
  or `AmunSession.get_turbine_by_name`
  

**Returns**:

  List of dictionaries with these fields:
  - `speed` - wind speed in m/s
  - `power` - generated power in kW

#### get\_region\_details

```python
def get_region_details(latitude: float,
                       longitude: float) -> List[RegionDetail]
```

Get a list of supported regions for a given point.

**Arguments**:

- `latitude` _float_ - latitude of the point to lookup.
- `longitude` _float_ - longitude
  

**Returns**:

- `List[RegionDetail]` - A list of all the supported regions for the point.

#### get\_scenarios

```python
def get_scenarios(region)
```

Get the scenarios that are available for the specified region. The regions for a given location
to use can be found be using `.AmunSession.get_region_details`

**Arguments**:

- `region` _str_ - The code for the region to lookup scenarios for.
  

**Returns**:

  List of Scenario details.
  
  **Response example**:
  
```json
        [{
            'id': 3,
            'name': '2019 Smart Power Scenario',
            'description': 'To examine the impact of a smarter power system with more flexible capacity and demand',
            'region': 'gbr',
            'S3uri': None,
            'currency': 'GBP',
            'currencyYear': 2018,
            'hasFile': False
        },
        ...
```

#### get\_scenario\_by\_name

```python
def get_scenario_by_name(region, scenario_name)
```

Get a scenario by name

**Arguments**:

- `region` _str_ - The code for the region to lookup scenarios for. Use `AmunSession.get_region_details` to get the region code for a point.
- `scenario_name` _str_ - The name of the scenario to get. Please ensure the name is spelled correctly.
  

**Returns**:

  An object with infomation about the scenario. If not found, raises an error.
  
  **Response example**:
  
```json
    {
        'id': 3,
        'name': '2019 Smart Power Scenario',
        'description': 'To examine the impact of a smarter power system with more flexible capacity and demand',
        'region': 'gbr',
        'S3uri': None,
        'currency': 'GBP',
        'currencyYear': 2018,
        'hasFile': False
    }
```

#### create\_valuation

```python
def create_valuation(valuation)
```

Creates a valuation in Amun.

Expects a dictionary of with these fields:
- **name** (str)
- **description** (str)
- **longitude** (str)
- **latitude** (str)
- **windType** (str) - One of &quot;era5&quot;, &quot;merra2&quot;, &quot;weibull&quot;, &quot;newa&quot;, &quot;p50scaling&quot;, &quot;powerdensity&quot;, &quot;averagewindspeed&quot;, &quot;aurorawindatlas&quot;, &quot;p50yieldscaling&quot;. Not applicable for uploaded data.
- **scenarioId** (string) to get the id of the scenario you want to use, check `AmunSession.get_scenario_by_name` or `AmunSession.get_scenarios`
- **turbineModelId** (int): The Id of the Turbine to use in the calculation as returned from `.AmunSession.get_turbines`.
- **numberOfTurbines** (int): The number of turbines in the site.
- **hubHeight** (float): Given in meters (m).
- **useReanalysisCorrection** - if True, will use regional reanalysis correction if it is available for the location
- **usePowerCurveSmoothing** - if True, will use regional reanalysis correction if it is available for the location
- **roughnessLength** (float, optional): Static roughness. If not given, will be derived from reanalysis data
- **curtailmentThreshold** (float, optional): Defaults to 0
- **lossesWake** (float, optional): The percentage to apply for wake loss. (0 &lt;= lossesWake &lt; 1)
- **lossesAvailability** (float, optional): Percentage for external losses. (0 &lt;= lossesAvailability &lt; 1)
- **lossesElectrical** (float, optional): Percentage for external losses. (0 &lt;= lossesElectrical &lt; 1)
- **lossesTurbinePerformance** (float, optional): Percentage for external losses. (0 &lt;= lossesTurbinePerformance &lt; 1)
- **lossesEnvironmental** (float, optional): Percentage for external losses. (0 &lt;= lossesEnvironmental &lt; 1)
- **lossesOtherCurtailment** (float, optional): Percentage for external losses. (0 &lt;= lossesOtherCurtailment &lt; 1)

Additional parameters that are specific to a wind type will be required. Please look at the parameters section of SDK Reference documentation and
see Amun SDK Examples to see how to create a valuation for your use case.

**Returns**:

  A dictionary with the valuation information. Additionally provides a unique valuation id that should be used to run it and get results. Please see `AmunSession.get_valuation_results` for more details.

#### submit\_load\_factor\_calculations

```python
def submit_load_factor_calculations(
        load_factor_configurations: List[Dict]) -> List[str]
```

Submits a request to calculate the load factor and wind speeds for a year given
a start time and a location.
You can submit a lot of calculations at once and then use the tokens in response
to check on the status of each calculation.

**See Also**:

  `AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

  list of load_factor_configurations where each load_factor_configuration is a dictionary of load factor parameters.
  

**Returns**:

  List of tokens where each token is a unique identifier for the calculation. The order of the tokens matches the order of the input parameters.
  * token: unique identifier for the calculation

#### get\_load\_factor\_calculation

```python
def get_load_factor_calculation(token: str)
```

V2 feature.
Gets the status of a load factor calculation given its token.

For calculation that is still running:
- `status` - &quot;Running&quot;

For a finished calculation:
- `status` - &quot;Complete&quot;
- `exiryTime` - Date and time of when the results will be deleted,
- `results` - load factors

For errored calculation:
- `status` - &quot;Errored&quot;
- `error` - a string explaining the error

#### track\_load\_factor\_calculation

```python
def track_load_factor_calculation(tokens: List[str]) -> List[Dict]
```

V2 feature
Tracks the status of a load factor calculation/simulation given their token and
returns the results of the simulations as soon as they finish running.

Accepts a list of tokens of calculations and returns a list of results.
The order of the results matches the order of the input parameters.
Depending on the status of the calculation the result will have different keys:

For finished calculations:
- `parameters` - the parameters used for the calculation
- `appliedParams` - smoothing coefficients and other parameters applied to the calculation
- `typicalHourly` - typical hourly load factors
- `weatherYearHourly` - hourly load factors for the weather year  

For errored calculations:
- `error` - a string explaining the error  

For calcualtions that failed to be submitted:
- `None`

#### run\_load\_factors\_in\_batch

```python
def run_load_factors_in_batch(
        load_factor_configurations: List[Dict]) -> List[Dict]
```

Perform multiple load factor calculations in parallel.

**See Also**:

  `.AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

  list of load_factor_configurations where each load_factor_configuration is a dictionary of load factor parameters.
  

**Returns**:

  List of dictionaries of this type. Order of the results matches the order of the input parameters:
  - `parameters` - the parameters used for the calculation
  - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
  - `typicalHourly` - typical hourly load factors
  - `weatherYearHourly` - hourly load factors for the weather year

#### run\_load\_factor\_calculation

```python
def run_load_factor_calculation(load_factor_configuration: Dict,
                                version=1) -> Dict
```

Calculate the load factor and wind speeds for a year given a start time and a location.

**See Also**:

  `.AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

- `load_factor_configuration` - A dictionary of load factor parameters.
- `version` _defaults to 1_ - Version of the API to use for calculations (1 or 2).
  

**Returns**:

  A Dictionary with the keys
  - `parameters` - the parameters used for the calculation
  - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
  - `typicalHourly` - typical hourly load factors
  - `weatherYearHourly` - hourly load factors for the weather year

#### run\_load\_factors\_for\_parameters\_batch

```python
def run_load_factors_for_parameters_batch(
        flow_parameters: List[FlowParameters],
        base_parameters: List[LoadFactorBaseParameters]) -> List[Dict]
```

Perform multiple load factor calculations in parallel by providing flow parameters and base parameters
for each calculation.

**See Also**:

  `.AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

- `flow_parameters` - The list of parameters specific to the calculation type
  * `aurora.amun.client.parameters.AverageWindSpeedParameters`
  * `aurora.amun.client.parameters.BuiltInWindParameters`
  * `aurora.amun.client.parameters.PowerDensityParameters`
  * `aurora.amun.client.parameters.WeibullParameters`
  * `aurora.amun.client.parameters.UploadedWindParameters`
  
- `base_parameters` - List of parameters required for all flows to the calculation type. These are applied to all the flow parameters
  

**Returns**:

  List of dictionaries of this type. Order of the results matches the order of the input parameters:
  - `parameters` - the parameters used for the calculation
  - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
  - `flow_parameters`0 - typical hourly load factors
  - `flow_parameters`1 - hourly load factors for the weather year

#### run\_load\_factor\_for\_parameters

```python
def run_load_factor_for_parameters(flow_parameters: FlowParameters,
                                   base_parameters: LoadFactorBaseParameters,
                                   version=1)
```

Calculate the load factor and wind speeds for a year given a start time and a location.

**See Also**:

  `AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

- `flow_parameters` - The parameters specific to the calculation type
  - `aurora.amun.client.parameters.AverageWindSpeedParameters`
  - `aurora.amun.client.parameters.BuiltInWindParameters`
  - `aurora.amun.client.parameters.PowerDensityParameters`
  - `aurora.amun.client.parameters.WeibullParameters`
  - `aurora.amun.client.parameters.UploadedWindParameters`
  
- `base_parameters` _LoadFactorBaseParameters_ - The parameters required for all flows to the calculation type.
- `version` _defaults to 1_ - Version of the API to use for calculations (1 or 2).
  

**Returns**:

  A Dictionary with the keys
  - **parameters** - the parameters used for the calculation
  - **appliedParams** - smoothing coefficients and other parameters applied to the calculation
  - **typicalHourly** - typical hourly load factors
  - **weatherYearHourly** - hourly load factors for the weather year

#### get\_valuation\_results

```python
def get_valuation_results(valuation_id, format, should_return_hourly_data)
```

Gets the results of a valuation

**Arguments**:

- `valuation_id` _number_ - The id of the valuation to get the results for.
- `format` _string_ - The format of the results. One of (&quot;json&quot;,&quot;xlsx&quot;)
- `should_return_hourly_data` _bool_ - Set to true to return the hourly data for the valuation.

#### delete\_valuation

```python
def delete_valuation(valuation_id)
```

Deletes a valuation from Amun.

**Arguments**:

- `valuation_id` _string_ - The id of the valuation to delete.

#### get\_wind

```python
def get_wind(lat, lon, year, dataset)
```

The parameters used for built in wind calculations (*era5*,*merra2*,*newa*).

**Notes**:

  Not all locations support all wind types and not all locations support Regional Reanalysis Correction.
  

**Arguments**:

- `latitude` _float_ - The latitude of the point (-90 to 90).
- `longitude` _float_ - The latitude of the point (-180 to 180).
  year (number):The year to fetch wind data for.
- `dataset` _str_ - one of (&quot;Era5&quot;,&quot;Merra2&quot;,&quot;NEWA&quot;).

#### get\_wind\_atlas

```python
def get_wind_atlas(lat, lon, radius, numberOfTurbines, rotorDiameterInMeters,
                   regionCode)
```

The parameters used for built in wind calculations (*era5*,*merra2*,*newa*).

**Notes**:

  Not all locations are supported.
  

**Arguments**:

- `latitude` _float_ - The latitude of the point (-90 to 90).
- `longitude` _float_ - The latitude of the point (-180 to 180).
  radius (int):The radius of the area to average wind speed over 0 to 1000.
- `numberOfTurbines` _int_ - If no radius specified this is required to allow the size of the windfarm to be estimated.
  rotorDiameterInMeters (int):The rotor diameter of the turbines used to calculate size of the windfarm from the number of turbines if None a default value is used.

#### get\_windfarms

```python
def get_windfarms(search)
```

Search for windfarms

**Arguments**:

- `search` _string_ - Search term to filter by.

#### get\_windfarm

```python
def get_windfarm(uuid)
```

Get windfarm by uuid

**Arguments**:

- `search` _uuid_ - uuid of windfarm to get.

