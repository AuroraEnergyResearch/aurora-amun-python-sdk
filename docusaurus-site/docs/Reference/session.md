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

Get a turbine by name.

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

Get a scenario by name.

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
- `status` - &quot;Running&quot;
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
def run_load_factor_calculation(load_factor_configuration: Dict)
```

Calculate the load factor and wind speeds for a year given a start time and a location.

**See Also**:

  `.AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

- `load_factor_configuration` - A dictionary of load factor parameters.
  

**Returns**:

- `Dictionary` - A Dictionary with the keys
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
                                   base_parameters: LoadFactorBaseParameters)
```

Calculate the load factor and wind speeds for a year given a start time and a location.

**See Also**:

  `AmunSession.get_region_details` to get region codes and available datasets for a point
  

**Arguments**:

- `flow_parameters` - The parameters specific to the calculation type
  * `aurora.amun.client.parameters.AverageWindSpeedParameters`
  * `aurora.amun.client.parameters.BuiltInWindParameters`
  * `aurora.amun.client.parameters.PowerDensityParameters`
  * `aurora.amun.client.parameters.WeibullParameters`
  * `aurora.amun.client.parameters.UploadedWindParameters`
  
- `base_parameters` _LoadFactorBaseParameters_ - The parameters required for all flows to the calculation type.
  

**Returns**:

- `Dictionary` - A Dictionary with the keys
  - `parameters` - the parameters used for the calculation
  - `flow_parameters`0 - smoothing coefficients and other parameters applied to the calculation
  - `flow_parameters`1 - typical hourly load factors
  - `flow_parameters`2 - hourly load factors for the weather year

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

