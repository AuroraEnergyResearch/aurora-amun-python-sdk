"""Step 3: download the classic valuation outputs (JSON and Excel databook) to out/<valuation id>/classic/.

Requesting outputs runs the valuation if it has not been calculated yet.
"""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import (
    download_valuation_outputs,
    load_local_env,
    setup_file_and_console_loggers,
)

# --- EDIT ME -----------------------------------------------------------------
VALUATION_ID = 0  # id from run_full_horizon_valuation.py
HOURLY_DATA = False  # requires the hourly data permission
# -----------------------------------------------------------------------------


def main():
    load_local_env()
    setup_file_and_console_loggers("download_valuation_outputs.log")
    session = AmunSession()
    download_valuation_outputs(session, VALUATION_ID, HOURLY_DATA)


if __name__ == "__main__":
    main()
