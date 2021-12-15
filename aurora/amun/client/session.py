from json import encoder
from aurora.amun.client.responses import (
    RegionDetail,
    get_RegionDetail_from_response,
)
from aurora.amun.client.parameters import (
    FlowParameters,
    LoadFactorBaseParameters,
)
from typing import Dict, List
import requests
import logging
import os
from pathlib import Path
import json
from urllib.parse import urlencode
from aurora.amun.client.utils import AmunJSONEncoder, configure_session_retry


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
        if response.status_code == 200:
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

         **Response**:

        .. code-block::

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
                 },........

        """

        url = f"{self.base_url}/turbines"
        return self._get_request(url)

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
           to use can be found be using :meth:`.AmunSession.get_region_details`

        Args:
            region (str): The code for the region to lookup scenarios for.

        Returns:
            List of Scenario details.

        **Response**:

        .. code-block::

                [{
                    'id': 3,
                    'name': '2019 Smart Power Scenario',
                    'description': 'To examine the impact of a smarter power system with more flexible capacity and demand',
                    'region': 'gbr',
                    'S3uri': None,
                    'currency': 'GBP',
                    'currencyYear': 2018,
                    'hasFile': False
                },.....

        """
        url = f"{self.base_url}/scenarios"
        params = {"region": region}
        scenarios = self._get_request(url, params)
        return scenarios  # list(map(lambda x: scenario_from_dict(x), scenarios))

    def create_valuation(self, valuation):
        url = f"{self.base_url}/valuations"
        return self._put_request(url, valuation)

    def run_load_factor_calculation(self, load_factor_configuration: Dict):
        """Calculate the load factor and wind speeds for a year given a start time and a location.

        See Also:
            :meth:`.AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            load_factor_configuration (Dict): A dictionary of load factor parameters.

        Returns:
            Dictionary: A Dictionary with the keys

            * parameters
            * appliedParams
            * typicalHourly
            * weatherYearHourly

        """
        url = f"{self.base_url}/loadfactor"
        return self._put_request(url, load_factor_configuration)

    def run_load_factor_for_parameters(
        self, flow_parameters: FlowParameters, base_parameters: LoadFactorBaseParameters
    ):
        """Calculate the load factor and wind speeds for a year given a start time and a location.

        See Also:
            :meth:`.AmunSession.get_region_details` to get region codes and available datasets for a point

        Args:
            flow_parameters (FlowParameters): The parameters specific to the calculation type

                * :class:`~aurora.amun.client.parameters.AverageWindSpeedParameters`
                * :class:`~aurora.amun.client.parameters.BuiltInWindParameters`
                * :class:`~aurora.amun.client.parameters.PowerDensityParameters`
                * :class:`~aurora.amun.client.parameters.WeibullParameters`
                * :class:`~aurora.amun.client.parameters.UploadedWindParameters`

            base_parameters (LoadFactorBaseParameters): The parameters required for all flows to the calculation type.

        Returns:
            Dictionary: A Dictionary with the keys

                * parameters
                * appliedParams
                * typicalHourly
                * weatherYearHourly
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
            dataset (str): one of ("Era5","Merra2","NEWA")
            year (number):The year to fetch wind data for.
        """
        url = f"{self.base_url}/wind/series"
        params = {"lat": lat, "lon": lon, "year": year, "dataset": dataset}
        return self._get_request(url, params=params)

    def get_wind_atlas(self, lat, lon, year, radius, regionCode):
        """The parameters used for built in wind calculations (*era5*,*merra2*,*newa*).

        Note:
            Not all locations support all wind types and not all locations support Regional Reanalysis Correction.

        Args:
            latitude (float): The latitude of the point (-90 to 90).
            longitude (float): The latitude of the point (-180 to 180).
            dataset (str): one of ("Era5","Merra2","NEWA")
            year (number):The year to fetch wind data for.
        """
        url = f"{self.base_url}/wind/atlas/{regionCode}/averagewindspeed"
        params = {"lat": lat, "lon": lon, "year": year, "radius": radius}
        return self._get_request(url, params=params)

    def send_custom_wind(self, valuation_id, wind):
        url = f"{self.base_url}/valuations/{valuation_id}/wind"
        return self._post_request(url, wind)

    def get_windfarms(self, search):
        """Search for windfarms
        Note:


        Args:
            search (string): Search term to filter by.

        """
        url = f"{self.base_url}/windfarms"
        params = {"search": search}
        return self._get_request(url, params=params)

    def get_windfarm(self, uuid):
        """Get windfarm by uuid
        Note:


        Args:
            search (uuid): uuid of windfarm to get.

        """
        url = f"{self.base_url}/windfarms/{uuid}"
        return self._get_request(url)
