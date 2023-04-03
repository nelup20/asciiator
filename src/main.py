import logging
import multiprocessing
import tempfile
import traceback
from os import makedirs

from src.util.logging import log_and_print, setup_logger
from src.util.options import Options


def main():
    setup_logger()

    try:
        options = Options()

        if not options.inplace:
            makedirs(options.output_path, exist_ok=True)

        for file in options.input:
            file.transform(options)
    except (KeyboardInterrupt, FileNotFoundError, Exception):
        log_and_print(traceback.format_exc(), logging.ERROR)
        log_and_print(
            f"An error occurred. If you were transforming a video, you might want to check and delete any "
            f'"asciiator_" folders in your default temporary directory ({tempfile.gettempdir()}).\nAsciiator stores '
            f"media files in these temporary directories when transforming videos and deletes them at the end, "
            f"but when an error occurs, they might not get deleted.",
            logging.WARNING,
        )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
