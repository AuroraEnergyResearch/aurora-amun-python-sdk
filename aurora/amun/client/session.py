from json import encoder
import time
from aurora.amun.client.responses import (
    RegionDetail,
    get_RegionDetail_from_response,
)
from aurora.amun.client.parameters import (
    FlowParameters,
    LoadFactorBaseParameters,
)
from aurora.amun.client.utils import get_single_value_form_list
from typing import Dict, List, Tuple
import requests
import logging
import os
from pathlib import Path
import json
from urllib.parse import urlencode
from aurora.amun.client.utils import AmunJSONEncoder, configure_session_retry, get_v2_url


log = logging.getLogger(__name__)
AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME = "AURORA_API_KEY"
AURORA_API_BASE_URL_ENVIRONMENT_VARIABLE_NAME = "AURORA_API_BASE_URL"
AURORA_API_KEY_FILE_NAME = ".aurora-api-key"
AURORA_AMUN_PRODUCTION_ENDPOINT = "https://api.auroraer.com/amun/v1"


class APISession:
    """Internal class to hold base methods for interacting with the Aurora HTTP API"""

    def __init__(self, base_url=None, token=None):
        self.token = self._get_token(token)
        self.base_url = self._get_base_url(base_url)
        self.session = self._create_session()

    def _get_token(self, token):
        if token is not None:
            log.debug(f"Using token passed as parameter to session constructor")
            return token
        elif AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME in os.environ:
            log.debug(
                f"Using token passed found in environment variable {AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME}"
            )
            return os.environ[AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME]
        else:
            return self._load_token_from_file()

    def _get_base_url(self, base_url):
        if base_url is not None:
            log.debug(
                f"Using baseUrl {base_url} passed as parameter to session constructor"
            )
            return base_url
        elif AURORA_API_BASE_URL_ENVIRONMENT_VARIABLE_NAME in os.environ:
            base_url_override = os.environ[
                AURORA_API_BASE_URL_ENVIRONMENT_VARIABLE_NAME
            ]
            log.debug(
                f"Using base url '{base_url_override}' passed found in environment variable {AURORA_API_BASE_URL_ENVIRONMENT_VARIABLE_NAME}"
            )
            return base_url_override
        else:
            return AURORA_AMUN_PRODUCTION_ENDPOINT

    def _load_token_from_file(self):
        file = Path.joinpath(Path.home(), AURORA_API_KEY_FILE_NAME)
        log.debug(f"Looking for token in '{file}'")
        key_found = []
        if Path.exists(file):
            with open(file, "r") as reader:
                key_found = reader.readlines()
            if len(key_found) == 1:
                return key_found[0]
            else:
                raise RuntimeError(f"Could not parse key from file {file}")
        else:
            raise RuntimeError(
                f"No aurora api key file found '{file}'. Please create the text file '{AURORA_API_KEY_FILE_NAME}' file in your home directory {Path.home()} and add you api token to it."
            )

    def _create_session(self):
        log.debug(f"Creating session with token '**************{self.token[-5:]}'")
        session = session = requests.session()
        session.headers = {
            "Content-Type": "application/json",
            "Private-Token": self.token,
        }
        return session

    def _get_request(self, url, params={}, should_retry=False):
        log.debug(f"GET Request to {url}  with params {params}")

        if should_retry:
            session_to_use = configure_session_retry(self._create_session(), retries=20)
        else:
            session_to_use = self.session

        response = session_to_use.request("GET", url, params=params)
        return self._parse_as_json(response)

    def _del_request(self, url, params={}):
        log.debug(f"DEL Request to {url}  with params {params}")

        response = self.session.request("DELETE", url, params=params)
        if response.status_code == 200:
            return
        elif response.status_code == 401:
            raise RuntimeError(
                f"You are not authorised. Please check you have set the correct api token."
            )
        else:
            raise RuntimeError(f"{response.status_code}  {response.text}")

    def _put_request(self, url, payload):
        log.debug(f"PUT Request to {url} with payload {payload}")
        response = self.session.request(
            "PUT", url, data=json.dumps(payload, cls=AmunJSONEncoder)
        )
        return self._parse_as_json(response)

    def _post_request(self, url, payload):
        log.debug(f"POST Request to {url} with payload {payload}")
        response = self.session.request(
            "POST", url, data=json.dumps(payload, cls=AmunJSONEncoder)
        )
        return self._parse_as_json(response)

    def _parse_as_json(self, response):
        if response.status_code == 200 or response.status_code == 202:
            return response.json()
        elif response.status_code == 401:
            raise RuntimeError(
                f"You are not authorised. Please check you have set the correct api token."
            )
        elif response.status_code == 403:
            raise RuntimeError(
                f"Your token is valid but you do not have the required permissions to perform this operation."
            )
        else:
            raise RuntimeError(f"{response.status_code}  {response.text}")


class AmunSession(APISession):
    """Manage access to the Amun API.

    By default the session will connect to the production Amun API endpoint. This can be overridden by passing the base_url into the constructor
    or by setting the environment variable *AURORA_API_BASE_URL*. This is for internal use only.

    The authentication token is read from the users home directory *$home/.aurora-api-key* e.g. *C:/Users/Joe Bloggs/.aurora-api-key*.
    This can be overridden by passing the token into the constructor or by setting the environment variable *AURORA_API_KEY*.


    Args:
        base_url (string, optional): Override the base url used to contact the Amun API. Defaults to None.
        token (string, optional): Overide the api authentication token used for API access. Defaults to None.
    """

    def __init__(self, base_url=None, token=None):
        super().__init__(base_url, token)

    def get_turbines(self):
        """Get the turbines available to the user.
        
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
        """

        url = f"{self.base_url}/turbines"
        return self._get_request(url)

    def get_turbine_by_name(self, turbine_name):
        """Get a turbine by name."""
        turbines = self.get_turbines()

        return get_single_value_form_list(
            filter_function=lambda x: x["name"] == turbine_name,
            results_list=turbines,
            error=f"with name '{turbine_name}'",
        )

    def get_region_details(
        self, latitude: float, longitude: float
    ) -> List[RegionDetail]:
        """Get a list of supported regions for a given point.

        Args:
            latitude (float): latitude of the point to lookup.
            longitude (float): longitude

        Returns:
            List[RegionDetail]: A list of all the supported regions for the point.
        """

        url = f"{self.base_url}/regions/details"
        params = {"lon": longitude, "lat": latitude}
        region_details = self._get_request(url, params)
        return list(
            map(lambda resp: get_RegionDetail_from_response(resp), region_details)
        )

    def get_scenarios(self, region):
        """Get the scenarios that are available for the specified region. The regions for a given location
           to use can be found be using `.AmunSession.get_region_details`

        Args:
            region (str): The code for the region to lookup scenarios for.

        Returns:
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
        """
        url = f"{self.base_url}/scenarios"
        params = {"region": region}
        scenarios = self._get_request(url, params)
        return scenarios  # list(map(lambda x: scenario_from_dict(x), scenarios))
    

    def get_scenario_by_name(self, region, scenario_name):
        """Get a scenario by name."""
        scenarios = self.get_scenarios(region)
        return get_single_value_form_list(
            filter_function=lambda x: x["name"] == scenario_name
            and x["isRetired"] == False,
            results_list=scenarios,
            error=f"with name '{scenario_name}'",
        )


    def create_valuation(self, valuation):
        url = f"{self.base_url}/valuations"
        return self._put_request(url, valuation)


    def submit_load_factor_calculations(self, load_factor_configurations: List[Dict]) -> List[str]:
        """
        Submits a request to calculate the load factor and wind speeds for a year given
        a start time and a location.
        You can submit a lot of calculations at once and then use the tokens in response
        to check on the status of each calculation.

        See Also:
            `AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            list of load_factor_configurations where each load_factor_configuration is a dictionary of load factor parameters.

        Returns:
            List of tokens where each token is a unique identifier for the calculation. The order of the tokens matches the order of the input parameters.
            * token: unique identifier for the calculation
        """

        # This is a v2 feature
        url = get_v2_url(f"{self.base_url}/loadfactor")

        # Saves the request and a unique token of each calculation/simulation
        tokens = []
        for i, configuration in enumerate(load_factor_configurations):
            creation_response = self._put_request(url, configuration)
            if 'token' in creation_response.keys():
                tokens.append(creation_response['token'])
                log.debug("Submitted a load factor calculation")
            else:
                log.warning(f"Could not create load factor calculation for configuration {i}: {configuration}")
                tokens.append(None)
        return tokens
    

    def get_load_factor_calculation(self, token: str):
        """
        V2 feature.
        Gets the status of a load factor calculation given its token.

        For calculation that is still running:
        - `status` - "Running"

        For a finished calculation:
        - `status` - "Complete"
        - `exiryTime` - Date and time of when the results will be deleted,
        - `results` - load factors

        For errored calculation:
        - `status` - "Errored"
        - `error` - a string explaining the error
        """
        url = get_v2_url(f"{self.base_url}/loadfactor")
        return self._get_request(f'{url}/{token}')


    def track_load_factor_calculation(self, tokens: List[str]) -> List[Dict]:
        """
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
        """
        
        results = [None] * len(tokens)
        leftToRun = tokens.copy()

        while len(leftToRun) > 0:
            time.sleep(10)
            log.info("Checking status...")
            for token in leftToRun:
                i = tokens.index(token)

                # If the token is None then it was not created
                if token is None:
                    leftToRun.remove(token)
                
                response = self.get_load_factor_calculation(token)
                if response['status'] == "Errored":
                    leftToRun.remove(token)
                    results[i] = response['error']
                elif response['status'] == "Complete":
                    leftToRun.remove(token)
                    results[i] = response['result']
        return results
    

    def run_load_factors_in_batch(self, load_factor_configurations: List[Dict]) -> List[Dict]:
        """Perform multiple load factor calculations in parallel.

        See Also:
            `.AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            list of load_factor_configurations where each load_factor_configuration is a dictionary of load factor parameters.

        Returns:
            List of dictionaries of this type. Order of the results matches the order of the input parameters:
            - `parameters` - the parameters used for the calculation
            - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
            - `typicalHourly` - typical hourly load factors
            - `weatherYearHourly` - hourly load factors for the weather year  
        """
        # Step 1: Submit all the calculations/simualations
        tokens = self.submit_load_factor_calculations(load_factor_configurations)
        log.info(f"Submitted {len(tokens)} load factor calculations to perform")

        # Step 2: Wait for each simulation to finish
        results = self.track_load_factor_calculation(tokens)

        return results


    ## Chris never used it and probably never will
    def run_load_factor_calculation(self, load_factor_configuration: Dict):
        """Calculate the load factor and wind speeds for a year given a start time and a location.

        See Also:
           `.AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            load_factor_configuration: A dictionary of load factor parameters.

        Returns:
            Dictionary: A Dictionary with the keys
            - `parameters` - the parameters used for the calculation
            - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
            - `typicalHourly` - typical hourly load factors
            - `weatherYearHourly` - hourly load factors for the weather year  

        """
        url = f"{self.base_url}/loadfactor"
        return self._put_request(url, load_factor_configuration)


    def run_load_factors_for_parameters_batch(
        self, flow_parameters: List[FlowParameters], base_parameters: List[LoadFactorBaseParameters]
    ) -> List[Dict]:
        """Perform multiple load factor calculations in parallel by providing flow parameters and base parameters
            for each calculation.

        See Also:
            `.AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            flow_parameters: The list of parameters specific to the calculation type
                * `aurora.amun.client.parameters.AverageWindSpeedParameters`
                * `aurora.amun.client.parameters.BuiltInWindParameters`
                * `aurora.amun.client.parameters.PowerDensityParameters`
                * `aurora.amun.client.parameters.WeibullParameters`
                * `aurora.amun.client.parameters.UploadedWindParameters`

            base_parameters: List of parameters required for all flows to the calculation type. These are applied to all the flow parameters

        Returns:
            List of dictionaries of this type. Order of the results matches the order of the input parameters:
            - `parameters` - the parameters used for the calculation
            - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
            - `typicalHourly` - typical hourly load factors
            - `weatherYearHourly` - hourly load factors for the weather year 
        """
        assert_message = "The number of flow parameters must match the number of base parameters"
        assert len(flow_parameters) == len(base_parameters), assert_message

        requests = []
        for flow, base in zip(flow_parameters, base_parameters):
            # Create a request by combining the parameters
            request = {}
            request.update(vars(flow))
            request.update(vars(base))
            requests.append(request)
        return self.run_load_factors_in_batch(requests)


    def run_load_factor_for_parameters(
        self, flow_parameters: FlowParameters, base_parameters: LoadFactorBaseParameters
    ):
        """Calculate the load factor and wind speeds for a year given a start time and a location.

        See Also:
            `AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            flow_parameters: The parameters specific to the calculation type
                * `aurora.amun.client.parameters.AverageWindSpeedParameters`
                * `aurora.amun.client.parameters.BuiltInWindParameters`
                * `aurora.amun.client.parameters.PowerDensityParameters`
                * `aurora.amun.client.parameters.WeibullParameters`
                * `aurora.amun.client.parameters.UploadedWindParameters`

            base_parameters (LoadFactorBaseParameters): The parameters required for all flows to the calculation type.

        Returns:
            Dictionary: A Dictionary with the keys
            - `parameters` - the parameters used for the calculation
            - `appliedParams` - smoothing coefficients and other parameters applied to the calculation
            - `typicalHourly` - typical hourly load factors
            - `weatherYearHourly` - hourly load factors for the weather year 
        """

        # Create a request by combining the paramters
        request = {}
        request.update(vars(flow_parameters))
        request.update(vars(base_parameters))
        return self.run_load_factor_calculation(request)

    def get_valuations(self, searchText=None):
        url = f"{self.base_url}/valuations"
        if searchText == None:
            params = {}
        else:
            params = {"searchText": searchText}
        return self._get_request(url, params=params)

    def copy_valuation(self, valuation_id):
        url = f"{self.base_url}/valuations/{valuation_id}/copy"
        return self._post_request(url, {})

    def get_valuation_results(self, valuation_id, format, should_return_hourly_data):
        url = f"{self.base_url}/valuations/{valuation_id}/outputs"
        params = {"format": format}
        if should_return_hourly_data:
            params["hourlyData"] = True
        return self._get_request(url, params=params, should_retry=True)

    def delete_valuation(self, valuation_id):
        """Deletes a valuation from Amun.

        Args:
            valuation_id (string): The id of the valuation to delete.
        """
        url = f"{self.base_url}/valuations/{valuation_id}"
        return self._del_request(url)

    def update_valuation(self, valuation):
        url = (f"{self.base_url}/valuations/{valuation['id']}",)
        return self._post_request(url, valuation)

    def send_production_for_calibration(self, valuation_id, generation):
        url = f"{self.base_url}/valuations/{valuation_id}/rawGeneration"
        return self._post_request(url, generation)

    def send_calibrated_production(self, valuation_id, generation):
        url = f"{self.base_url}/valuations/{valuation_id}/calibratedGeneration"
        return self._post_request(url, generation)

    def get_wind(self, lat, lon, year, dataset):
        """The parameters used for built in wind calculations (*era5*,*merra2*,*newa*).

        Note:
            Not all locations support all wind types and not all locations support Regional Reanalysis Correction.

        Args:
            latitude (float): The latitude of the point (-90 to 90).
            longitude (float): The latitude of the point (-180 to 180).
            year (number):The year to fetch wind data for.
            dataset (str): one of ("Era5","Merra2","NEWA").
        """
        url = f"{self.base_url}/wind/series"
        params = {"lat": lat, "lon": lon, "year": year, "dataset": dataset}
        return self._get_request(url, params=params)

    def get_wind_atlas(
        self, lat, lon, radius, numberOfTurbines, rotorDiameterInMeters, regionCode
    ):
        """The parameters used for built in wind calculations (*era5*,*merra2*,*newa*).

        Note:
            Not all locations are supported.

        Args:
            latitude (float): The latitude of the point (-90 to 90).
            longitude (float): The latitude of the point (-180 to 180).
            radius (int):The radius of the area to average wind speed over 0 to 1000.
            numberOfTurbines (int): If no radius specified this is required to allow the size of the windfarm to be estimated.
            rotorDiameterInMeters (int):The rotor diameter of the turbines used to calculate size of the windfarm from the number of turbines if None a default value is used.

        """
        url = f"{self.base_url}/wind/atlas/{regionCode}/averagewindspeed"
        params = {
            "lat": lat,
            "lon": lon,
            "radius": radius,
            "numberOfTurbines": numberOfTurbines,
            "rotorDiameterInMeters": rotorDiameterInMeters,
        }
        return self._get_request(url, params=params)

    def send_custom_wind(self, valuation_id, wind):
        url = f"{self.base_url}/valuations/{valuation_id}/wind"
        return self._post_request(url, wind)

    def get_windfarms(self, search):
        """Search for windfarms

        Args:
            search (string): Search term to filter by.

        """
        url = f"{self.base_url}/windfarms"
        params = {"search": search}
        return self._get_request(url, params=params)

    def get_windfarm(self, uuid):
        """Get windfarm by uuid

        Args:
            search (uuid): uuid of windfarm to get.

        """
        url = f"{self.base_url}/windfarms/{uuid}"
        return self._get_request(url)
