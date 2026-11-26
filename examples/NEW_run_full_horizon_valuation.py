"""Step 2: create a full-horizon valuation that uses a loss template for time-varying losses.

The valuation is only created here; it is calculated when its outputs are first requested
(step 3, download_valuation_outputs.py). It is not deleted.
"""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import (
    create_full_horizon_valuation,
    load_local_env,
    setup_file_and_console_loggers,
    download_valuation_outputs,
    download_full_horizon_files,
)

# --- EDIT ME -----------------------------------------------------------------
LOSS_FILE_ID = "903eafd6-f466-4536-813a-d7e140561be4"
REGION = "deu"
# Must be a non-historic scenario without weather years, covering whole months within 01/2019-12/2070
SCENARIO_NAME = "Germany Q3 26 (Central)"
HOURLY_DATA = False
# -----------------------------------------------------------------------------


def main():
    load_local_env()
    setup_file_and_console_loggers("run_full_horizon_valuation.log")
    session = AmunSession()
    valuation = create_full_horizon_valuation(session, LOSS_FILE_ID, REGION, SCENARIO_NAME)
    download_valuation_outputs(session, valuation["id"], HOURLY_DATA)
    download_full_horizon_files(session, valuation["id"])


if __name__ == "__main__":
    main()
