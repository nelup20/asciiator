import os

import pytest

from src.file.image_file import ImageFile
from src.main import main
from .helpers import clean_up_sys_argv, handle_sys_args

clean_up_sys_argv()


class TestMain:
    @pytest.mark.parametrize(
        "handle_sys_args", ["./test/resource/img/test.jpg"], indirect=True
    )
    def test_main_image_file(self, handle_sys_args):
        output_file_path = "./test_asciiator.jpg"

        try:
            main()

            output_file = ImageFile(output_file_path)
            expected_output_file = ImageFile(
                "./test/resource/test_image_expected_output.jpg"
            )

            assert output_file.get_width() == expected_output_file.get_width()
            assert output_file.get_height() == expected_output_file.get_height()
            assert len(output_file.get_data()) == len(expected_output_file.get_data())
        finally:
            os.remove(output_file_path)
