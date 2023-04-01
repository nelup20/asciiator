import logging
import warnings
from datetime import date
from os import makedirs
from pathlib import Path


def setup_logger() -> None:
    makedirs(f"{Path.home()}/.asciiator/logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        f"{Path.home()}/.asciiator/logs/asciiator_{date.today()}.log"
    )
    file_handler.setLevel(logging.DEBUG)
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
