"""Step 1: upload an Excel loss template (based on the Amun Loss Template)."""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import (
    generate_loss_file_name,
    load_local_env,
    setup_file_and_console_loggers,
    upload_loss_file,
)

# --- EDIT ME -----------------------------------------------------------------
LOSS_FILE_PATH = "examples/data/Amun Loss Template.xlsx"
LOSS_FILE_NAME = generate_loss_file_name()  # must be unique among your templates
# -----------------------------------------------------------------------------


def main():
    load_local_env()
    setup_file_and_console_loggers("upload_loss_template.log")
    session = AmunSession()
    upload_loss_file(session, LOSS_FILE_PATH, LOSS_FILE_NAME)


if __name__ == "__main__":
    main()
