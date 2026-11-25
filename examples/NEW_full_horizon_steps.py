"""Shared steps for the full-horizon / loss template examples.

The runnable scripts are:
- upload_loss_template.py
- list_loss_templates.py
- run_full_horizon_valuation.py
- download_valuation_outputs.py
- download_full_horizon_files.py
- full_horizon_loss_template_e2e.py (chains all of the above)

Run them from the repository root, e.g. `python examples/upload_loss_template.py`.
The API base URL and token are picked up from AURORA_API_BASE_URL / AURORA_API_KEY
(or ~/.aurora-api-key), as for every other example. For convenience they are also read
from the gitignored file examples/.env.local (see examples/.env.local.example).
"""
import logging
import logging.handlers
import os
from datetime import datetime

from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import get_scenario_by_name, get_single_value_form_list

log = logging.getLogger(__name__)

OUT_DIR = "out"
LOCAL_ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local")


def load_local_env(path=LOCAL_ENV_FILE):
    """Load KEY=VALUE lines from a gitignored env file into os.environ (real env vars win)."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def setup_file_and_console_loggers(file_name):
    os.makedirs("logs", exist_ok=True)
    rot_file_handler = logging.handlers.RotatingFileHandler(
        f"logs/{file_name}", "a", 30 * 1024 * 1024, 10
    )
    rot_file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    )
    rot_file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    )
    logger = logging.getLogger()
    logger.addHandler(rot_file_handler)
    logger.addHandler(console_handler)
    log.setLevel(logging.DEBUG)
    logging.getLogger("aurora.amun").setLevel(logging.DEBUG)


def default_template_name():
    return f"SDK-uploaded loss template {datetime.now():%Y-%m-%d %H-%M-%S}"


def upload_loss_template(session: AmunSession, template_path, template_name):
    loss_template = session.upload_loss_template(template_path, template_name)
    log.info(
        f"Uploaded loss template '{loss_template['name']}' with id {loss_template['id']}"
    )
    return loss_template


def create_full_horizon_valuation(
    session: AmunSession, loss_template_id, region, scenario_name
):
    scenario = get_scenario_by_name(session.get_scenarios(region), scenario_name)
    turbine = get_single_value_form_list(
        filter_function=lambda x: x["name"] == "Siemens SWT-4.0-130",
        results_list=session.get_turbines(),
        error="with name 'Siemens SWT-4.0-130'",
    )

    valuation_parameters = {
        "windType": "era5",
        "name": f"SDK Full Horizon Wind Farm {datetime.now()}",
        "description": "Full-horizon valuation with a loss template, created by the SDK",
        "longitude": "9",
        "latitude": "51",
        "turbineModelId": turbine["id"],
        "numberOfTurbines": 10,
        "hubHeight": 90,
        "obstacleHeight": 0,
        "roughnessLength": 0.001,
        "scenarioId": scenario["id"],
        "useReanalysisCorrection": False,
        "usePowerCurveSmoothing": True,
        # New: time-varying losses from a loss template over the full horizon
        "fullHorizonMode": True,
        "lossSource": "template",
        "lossFileId": loss_template_id,
    }

    valuation = session.create_valuation(valuation_parameters)
    log.info(f"Created full-horizon valuation {valuation['id']}")
    return valuation


def download_valuation_outputs(session: AmunSession, valuation_id, hourly_data=False):
    """Downloads the classic outputs (JSON and Excel databook). Runs the valuation if needed."""
    out_dir = os.path.join(OUT_DIR, str(valuation_id), "classic")
    json_path = session.get_valuation_results(
        valuation_id,
        format="json",
        should_return_hourly_data=hourly_data,
        save_to=os.path.join(out_dir, f"valuation_{valuation_id}.json"),
    )
    log.info(f"Saved JSON outputs to '{json_path}'")
    excel_path = session.get_valuation_results(
        valuation_id,
        format="excel",
        should_return_hourly_data=hourly_data,
        save_to=os.path.join(out_dir, f"valuation_{valuation_id}.xlsx"),
    )
    log.info(f"Saved Excel databook to '{excel_path}'")
    return [json_path, excel_path]


def download_full_horizon_files(session: AmunSession, valuation_id):
    """Downloads the additional full-horizon files from the wind output model (WOS)."""
    out_dir = os.path.join(OUT_DIR, str(valuation_id), "full_horizon")
    paths = session.download_valuation_files(valuation_id, out_dir)
    for path in paths:
        log.info(f"Saved '{path}'")
    return paths
