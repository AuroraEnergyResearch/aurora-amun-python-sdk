from aurora.amun.client.session import AmunSession
import logging
import logging.handlers
import os

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


if __name__ == "__main__":
    setup_file_and_console_loggers("authentication_example.log")
    log.setLevel(logging.DEBUG)  # Set Level for main logging in this file

    # Set Level for Amun SDK
    logging.getLogger("aurora.amun").setLevel(logging.DEBUG)
    # Set Log Level for root logger
    # logging.getLogger().setLevel(
    #    logging.DEBUG
    # )

    # making a request with an invalid token throws runtime error
    session = AmunSession(token="Not a Real Token")
    log.debug("Starting")
    log.info("Getting Turbines with bad token")
    try:

        session.get_turbines()
    except RuntimeError as ex:
        log.error(ex)

    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()
    log.info("Getting Turbines")
    turbines = session.get_turbines()
    log.info(f"found {len(turbines)} turbines")

    log.debug("Done")
