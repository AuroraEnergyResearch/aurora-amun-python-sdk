"""Step 1: upload an Excel loss template (based on the Amun Loss Template)."""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import (
    default_template_name,
    load_local_env,
    setup_file_and_console_loggers,
    upload_loss_template,
)

# --- EDIT ME -----------------------------------------------------------------
TEMPLATE_PATH = "examples/data/loss_template.xlsx"
TEMPLATE_NAME = default_template_name()  # must be unique among your templates
# -----------------------------------------------------------------------------


def main():
    load_local_env()
    setup_file_and_console_loggers("upload_loss_template.log")
    session = AmunSession()
    upload_loss_template(session, TEMPLATE_PATH, TEMPLATE_NAME)


if __name__ == "__main__":
    main()
