"""List your available loss templates (newest first) to find the id for a valuation run."""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import load_local_env, setup_file_and_console_loggers


def main():
    load_local_env()
    setup_file_and_console_loggers("list_loss_templates.log")
    session = AmunSession()
    loss_files = session.get_loss_files()
    if not loss_files:
        print("No loss files found.")
        return
    print(f"Found {len(loss_files)} loss file(s):")
    for loss_file in loss_files:
        print(f"  id: {loss_file['id']}  name: {loss_file['name']}")


if __name__ == "__main__":
    main()
