"""Step 4: download the additional full-horizon files from WOS to out/<valuation id>/full_horizon/.

The valuation must already have been calculated (run download_valuation_outputs.py first).
"""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import (
    download_full_horizon_files,
    load_local_env,
    setup_file_and_console_loggers,
)

# --- EDIT ME -----------------------------------------------------------------
VALUATION_ID = 0  # id from run_full_horizon_valuation.py
# -----------------------------------------------------------------------------


def main():
    load_local_env()
    setup_file_and_console_loggers("download_full_horizon_files.log")
    session = AmunSession()
    download_full_horizon_files(session, VALUATION_ID)


if __name__ == "__main__":
    main()
