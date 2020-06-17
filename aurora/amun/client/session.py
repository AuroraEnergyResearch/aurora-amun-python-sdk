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


class AmunSession:
    def __init__(self, baseUrl=None, token=None):
        self.token = self.__get_token(token)
        self.base_url = self.__get_base_url(baseUrl)
        self.session = self.__create_session()

    def __get_token(self, token):
        if token is not None:
            log.debug(f"Using token passed as parameter to session constructor")
            return token
        elif AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME in os.environ:
            log.debug(
                f"Using token passed found in environment variable {AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME}"
            )
            return os.environ[AURORA_API_KEY_ENVIRONMENT_VARIABLE_NAME]
        else:
            return self.__load_token_from_file()

    def __get_base_url(self, base_url):
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

    def __load_token_from_file(self):
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
                f"No aurora api key file found '{file}' please create this file and add you api token to it."
            )

    def __create_session(self):
        log.debug(f"Creating session with token '**************{self.token[-5:]}'")
        session = session = requests.session()
        session.headers = {
            "Content-Type": "application/json",
            "Private-Token": self.token,
        }
        return session

    def __get_request(self, url, params={}, should_retry=False):
        log.debug(f"GET Request to {url}  with params {params}")

        if should_retry:
            session_to_use = configure_session_retry(
                self.__create_session(), retries=20
            )
        else:
            session_to_use = self.session

        response = session_to_use.request("GET", url, params=params)
        return self.__parse_as_json(response)

    def __del_request(self, url, params={}):
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

    def __put_request(self, url, payload):
        log.debug(f"PUT Request to {url} with payload {payload}")
        response = self.session.request("PUT", url, json=payload)
        return self.__parse_as_json(response)

    def __parse_as_json(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise RuntimeError(
                f"You are not authorised. Please check you have set the correct api token."
            )
        else:
            raise RuntimeError(f"{response.status_code}  {response.text}")

    def get_turbines(self):
        payload = {}
        url = f"{self.base_url}/turbines"
        return self.__get_request(url)

    def get_scenarios(self, region):
        payload = {}
        url = f"{self.base_url}/scenarios"
        params = {"region": region}
        return self.__get_request(url, params)

    def create_valuation(self, valuation):
        url = f"{self.base_url}/valuations"
        return self.__put_request(url, valuation)

    def get_valuation_results(self, valuation_id, format, should_return_hourly_data):

        url = f"{self.base_url}/valuations/{valuation_id}/outputs"
        params = {"format": format}
        if should_return_hourly_data:
            params["hourlyData"] = True
        return self.__get_request(url, params=params, should_retry=True)

    def delete_valuation(self, valuation_id):
        url = f"{self.base_url}/valuations/{valuation_id}"
        return self.__del_request(url)
