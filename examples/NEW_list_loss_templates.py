"""List your available loss templates (newest first) to find the id for a valuation run."""
from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import load_local_env, setup_file_and_console_loggers


def main():
    load_local_env()
    setup_file_and_console_loggers("list_loss_templates.log")
    session = AmunSession()
    templates = session.get_loss_templates()
    if not templates:
        print("No loss templates found.")
        return
    print(f"Found {len(templates)} loss template(s):")
    for template in templates:
        print(f"  id: {template['id']}  name: {template['name']}")


if __name__ == "__main__":
    main()
