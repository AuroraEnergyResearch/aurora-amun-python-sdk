import requests
import logging
import os
from pathlib import Path
import json
from aurora.amun.client.utils import configure_session_retry


log = logging.getLogger(__name__)
AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME = "AURORA_API_KEY"
AURORA_API_BASE_URL_ENVIRONMENT_VARIABLE_NAME = "AURORA_API_BASE_URL"
AURORA_API_KEY_FILE_NAME = ".aurora-api-key"
AURORA_AMUN_PRODUCTION_ENDPOINT = "https://api.auroraer.com/amun/v1"


class APISession:
    """Internal class to hold base methods for interacting with an Aurora HTTP API
    """

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
        response = self.session.request("PUT", url, json=payload)
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
    """Create a session to interact with the Amun API.

    :param base_url: The base url to use to contact the amun API. Defaults to the production endpoint. 
    :param token: The authentication token to interact with the mun API. If omitted will try to find environment based key See below. 
    :type base_url: string (optional)
    :type token: string (optional)


    """

    def __init__(self, base_url=None, token=None):
        super().__init__(base_url, token)

    def get_turbines(self):
        payload = {}
        url = f"{self.base_url}/turbines"
        return self._get_request(url)

    def get_scenarios(self, region):
        payload = {}
        url = f"{self.base_url}/scenarios"
        params = {"region": region}
        return self._get_request(url, params)

    def create_valuation(self, valuation):
        url = f"{self.base_url}/valuations"
        return self._put_request(url, valuation)

    def run_load_factor_calculation(self, load_factor_configuration):
        """
        :param load_factor_configuration: The base url to use to contact the amun API. Defaults to the production endpoint. 
        :type load_factor_configuration: dictionary of run configuration parameters


        """
        url = f"{self.base_url}/loadfactor"
        return self._put_request(url, load_factor_configuration)

    def get_valuations(self):
        url = f"{self.base_url}/valuations"
        return self._get_request(url)

    def get_valuation_results(self, valuation_id, format, should_return_hourly_data):
        """
        valuation_id:int
        Id of the valuation to get the results for
        format: 'json','gzip','excel' 
        If gzip is chosen the response will be unzipped before returning
        should_return_hourly_data: boolean 
        Should the response include hourly data? Only available internally.
        """
        url = f"{self.base_url}/valuations/{valuation_id}/outputs"
        params = {"format": format}
        if should_return_hourly_data:
            params["hourlyData"] = True
        return self._get_request(url, params=params, should_retry=True)

    def delete_valuation(self, valuation_id):
        url = f"{self.base_url}/valuations/{valuation_id}"
        return self._del_request(url)
