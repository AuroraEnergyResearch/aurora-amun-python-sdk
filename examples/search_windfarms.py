import logging
import logging
import logging.handlers
import os
from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json

log = logging.getLogger(__name__)

# Sets Up root loging console(INFO) and file (DEBUG) handlers
def setup_file_and_console_loggers(fileName):
    os.makedirs("logs", exist_ok=True)
    rotFileHandler = logging.handlers.RotatingFileHandler(
        f"logs/{fileName}", "a", 30 * 1024 * 1024, 10
    )
    f = logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    rotFileHandler.setFormatter(f)
    rotFileHandler.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    )
    logger = logging.getLogger()
    logger.addHandler(rotFileHandler)
    logger.addHandler(consoleHandler)
    log.setLevel(logging.DEBUG)  # Set Level for main logging in this file
    # Set Level for Amun SDK
    logging.getLogger("aurora.amun").setLevel(logging.DEBUG)


def main():
    setup_file_and_console_loggers("windfarms_example.log")
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()

    windfarmsFound = session.get_windfarms(search="")
    save_to_json(f"windfarms/windfarms.json", windfarmsFound)

    windfarmFound = session.get_windfarm(uuid="6e64363f-b167-4b01-a72b-3fb331916651")
    save_to_json(f"windfarms/windfarm.json", windfarmFound)

    print("Done")


if __name__ == "__main__":
    main()
