from aurora.amun.client.parameters import SpeedAtHeight
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from pathlib import Path
import os
import json

log = logging.getLogger(__name__)


def get_single_value_form_list(filter_function, results_list, error):
    search_result = list(filter(filter_function, results_list))
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) == 0:
        raise RuntimeError(f"Did not find any results:{error}")
    else:
        raise RuntimeError(f"Found multiple results:{error}")


# https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#module-urllib3.util.retry
# This is a sub class of the Retry util from the requests package that allows the Max wait time between
# requests to be configured and to log warnings if any connection issues occur.
class RetryWithLogger(Retry):
    def __init__(self, backoff_max=Retry.BACKOFF_MAX, *args, **kwargs):
        super(RetryWithLogger, self).__init__(*args, **kwargs)
        self.BACKOFF_MAX = backoff_max

    def new(self, **kw):
        return super(RetryWithLogger, self).new(backoff_max=self.BACKOFF_MAX, **kw)

    def increment(self, method, url, *args, **kwargs):
        incremented_value = super(RetryWithLogger, self).increment(
            method, url, *args, **kwargs
        )
        response = kwargs["response"]
        log.debug(
            'Trying "%s" gave "%s:%s" attempt %s  with  %s remaining waiting for %ss.',
            url,
            response.status,
            response.reason,
            len(incremented_value.history) + 1,
            incremented_value.total,
            incremented_value.get_backoff_time(),
        )
        return incremented_value


# Configurable retry session that can be used generically
def configure_session_retry(
    session,
    retries=3,
    backoff_factor=5,
    status_forcelist=[504],
    back_off_max=10,
):
    retry = RetryWithLogger(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        backoff_max=back_off_max,
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


class AmunJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SpeedAtHeight):
            return obj.to_request_dictionary()
        return json.JSONEncoder.default(self, obj)


def save_to_json(file_name, object):
    output_dir = Path("out")
    file = Path.joinpath(output_dir, file_name)
    os.makedirs(file.parent, exist_ok=True)

    log.info(f"Saving to {file}")
    with open(file, "w") as writer:
        json.dump(object, writer, indent=4)


def get_json(file):
    with open(file, "r") as reader:
        data = json.load(reader)
    return data


def get_scenario_by_name(scenarios, scenario_name: str):
    return get_single_value_form_list(
        filter_function=lambda x: x["name"] == scenario_name
        and x["isRetired"] == False,
        results_list=scenarios,
        error=f"with name '{scenario_name}'",
    )