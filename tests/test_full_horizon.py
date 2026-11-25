"""Live tests for loss templates and full-horizon valuation files.

These hit the real API and are skipped unless AMUN_FULL_HORIZON_TESTS=1 is set. They also need:
- AMUN_LOSS_TEMPLATE_PATH: path to an .xlsx loss template (based on the Amun Loss Template)
- AMUN_FULL_HORIZON_SCENARIO: a non-historic scenario without weather years in AMUN_FULL_HORIZON_REGION
- AMUN_FULL_HORIZON_REGION (optional, defaults to "deu")
"""
import logging
import os
from datetime import datetime

import pytest

from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import get_scenario_by_name, get_single_value_form_list

log = logging.getLogger(__name__)

pytestmark = pytest.mark.skipif(
    os.environ.get("AMUN_FULL_HORIZON_TESTS") != "1",
    reason="Set AMUN_FULL_HORIZON_TESTS=1 to run the live full-horizon tests",
)

FULL_HORIZON_FILES = {
    "site_out_granular.csv",
    "site_out_hourly.csv",
    "central_year_hourly.csv",
    "central_year_granular.csv",
    "loss_schedule.csv",
}


@pytest.fixture
def amun_session():
    return AmunSession()


@pytest.fixture
def template_path():
    return os.environ["AMUN_LOSS_TEMPLATE_PATH"]


def test_upload_list_and_delete_loss_template(amun_session, template_path):
    name = f"SDK test loss template {datetime.now()}"
    loss_template = amun_session.upload_loss_template(template_path, name)
    assert loss_template["name"] == name

    listed_ids = [t["id"] for t in amun_session.get_loss_templates()]
    assert loss_template["id"] in listed_ids

    amun_session.delete_loss_template(loss_template["id"])
    listed_ids = [t["id"] for t in amun_session.get_loss_templates()]
    assert loss_template["id"] not in listed_ids


def test_full_horizon_valuation_files(amun_session, template_path, tmp_path):
    region = os.environ.get("AMUN_FULL_HORIZON_REGION", "deu")
    scenario = get_scenario_by_name(
        amun_session.get_scenarios(region), os.environ["AMUN_FULL_HORIZON_SCENARIO"]
    )
    turbine = get_single_value_form_list(
        filter_function=lambda x: x["name"] == "Siemens SWT-4.0-130",
        results_list=amun_session.get_turbines(),
        error="with name 'Siemens SWT-4.0-130'",
    )
    loss_template = amun_session.upload_loss_template(
        template_path, f"SDK test loss template {datetime.now()}"
    )
    valuation = amun_session.create_valuation(
        {
            "windType": "era5",
            "name": f"SDK test full horizon {datetime.now()}",
            "description": "Created by SDK tests",
            "longitude": "9",
            "latitude": "51",
            "turbineModelId": turbine["id"],
            "numberOfTurbines": 10,
            "hubHeight": 90,
            "roughnessLength": 0.001,
            "scenarioId": scenario["id"],
            "useReanalysisCorrection": False,
            "usePowerCurveSmoothing": True,
            "fullHorizonMode": True,
            "lossSource": "template",
            "lossFileId": loss_template["id"],
        }
    )
    try:
        excel_path = amun_session.get_valuation_results(
            valuation["id"],
            format="excel",
            should_return_hourly_data=False,
            save_to=str(tmp_path / "valuation.xlsx"),
        )
        assert os.path.getsize(excel_path) > 0

        files = amun_session.get_valuation_files(valuation["id"])
        assert {f["name"] for f in files} == FULL_HORIZON_FILES

        paths = amun_session.download_valuation_files(valuation["id"], str(tmp_path))
        assert len(paths) == len(FULL_HORIZON_FILES)
        assert all(os.path.getsize(p) > 0 for p in paths)
    finally:
        amun_session.delete_valuation(valuation["id"])
        amun_session.delete_loss_template(loss_template["id"])
