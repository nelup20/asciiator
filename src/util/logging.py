import logging
import warnings
from datetime import date
from os import makedirs
from pathlib import Path

LOG_DIRECTORY = f"{Path.home()}/.asciiator/logs"
LOG_FILE_PATH = f"{LOG_DIRECTORY}/asciiator_{date.today()}.log"


def setup_logger() -> None:
    makedirs(LOG_DIRECTORY, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter("\n%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(file_handler)


def log_and_print(message: str, level: int) -> None:
    logging.getLogger().log(level, message)

    if level == logging.WARNING:
        warnings.warn(message)
    else:
        print(message)
