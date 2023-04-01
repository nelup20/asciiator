import logging
import shutil
import sys
from os import path

import pytest

from src.util.logging import setup_logger, LOG_DIRECTORY, LOG_FILE_PATH, log_and_print


class TestLogging:
    def test_setup_logger(self):
        if path.exists(LOG_DIRECTORY):
            shutil.rmtree(LOG_DIRECTORY)

        assert not path.exists(LOG_DIRECTORY)

        setup_logger()

        assert path.exists(LOG_DIRECTORY)
        assert path.exists(LOG_FILE_PATH)

        logging.getLogger().info("Test log")

        with open(LOG_FILE_PATH) as log_file:
            log_data = log_file.readlines()
            assert " - root - INFO - Test log" in log_data[1]

    def test_log_and_print(self, capsys):
        if path.exists(LOG_DIRECTORY):
            shutil.rmtree(LOG_DIRECTORY)

        assert not path.exists(LOG_DIRECTORY)

        setup_logger()

        log_and_print("Info message", logging.INFO)
        assert capsys.readouterr().out == "Info message\n"

        log_and_print("Warning message", logging.WARNING)

        log_and_print("Error message", logging.ERROR)
        assert capsys.readouterr().out == "Error message\n"

        with open(LOG_FILE_PATH, "r") as log_file:
            log_data = log_file.readlines()
            assert " - root - INFO - Info message\n" in log_data[1]
            assert " - root - WARNING - Warning message\n" in log_data[3]
            assert " - root - ERROR - Error message\n" in log_data[5]
