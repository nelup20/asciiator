import os
import subprocess

import pytest

from src.file.image_file import ImageFile
from src.file.video_file import VideoFile
from src.main import main
from .helpers import clean_up_sys_argv, handle_sys_args

clean_up_sys_argv()


class TestMain:
    output_image_path = "./test_asciiator.jpg"
    output_video_path = "./test_asciiator.mp4"

    @pytest.mark.parametrize(
        "handle_sys_args",
        [["./test/resource/img/input/test.jpg", "--reduction=1"]],
        indirect=True,
    )
    def test_main_image_file_no_reduction(self, handle_sys_args):
        try:
            main()

            output_file = ImageFile(self.output_image_path)
            expected_output_file = ImageFile(
                "./test/resource/img/output/test_image_expected_output.jpg"
            )

            assert output_file.get_width() == (expected_output_file.get_width())
            assert output_file.get_height() == (expected_output_file.get_height())
            assert len(output_file.get_data()) == len(expected_output_file.get_data())
        finally:
            os.remove(self.output_image_path)

    @pytest.mark.parametrize(
        "handle_sys_args",
        [["./test/resource/img/input/test.jpg", "--reduction=2"]],
        indirect=True,
    )
    def test_main_image_file_2_reduction(self, handle_sys_args):
        try:
            main()

            output_file = ImageFile(self.output_image_path)
            expected_output_file = ImageFile(
                "./test/resource/img/output/test_image_expected_output_2.jpg"
            )

            assert output_file.get_width() == (expected_output_file.get_width())
            assert output_file.get_height() == (expected_output_file.get_height())
            assert len(output_file.get_data()) == len(expected_output_file.get_data())
        finally:
            os.remove(self.output_image_path)

    @pytest.mark.parametrize(
        "handle_sys_args", [["./test/resource/img/input/test.jpg"]], indirect=True
    )
    def test_main_image_file_default_reduction(self, handle_sys_args):
        try:
            main()

            output_file = ImageFile(self.output_image_path)
            expected_output_file = ImageFile(
                "./test/resource/img/output/test_image_expected_output_3.jpg"
            )

            assert output_file.get_width() == (expected_output_file.get_width())
            assert output_file.get_height() == (expected_output_file.get_height())
            assert len(output_file.get_data()) == len(expected_output_file.get_data())
        finally:
            os.remove(self.output_image_path)

    @pytest.mark.parametrize(
        "handle_sys_args",
        [["./test/resource/video/input/test.mp4", "--reduction=8"]],
        indirect=True,
    )
    def test_main_video_file_8_reduction(self, handle_sys_args):
        try:
            main()

            input_file = VideoFile("./test/resource/video/input/test.mp4")
            output_file = VideoFile(self.output_video_path)
            expected_output_file = VideoFile(
                "./test/resource/video/output/test_video_expected_output_1.mp4"
            )

            input_info = str(
                subprocess.run(
                    f'ffprobe -v 0 -of compact=p=0 -select_streams 0 -show_entries stream=width,height,r_frame_rate,duration "{input_file.absolute_path}"',
                    capture_output=True,
                    shell=True,
                ).stdout,
                "utf-8",
            )

            output_info = str(
                subprocess.run(
                    f'ffprobe -v 0 -of compact=p=0 -select_streams 0 -show_entries stream=width,height,r_frame_rate,duration "{output_file.absolute_path}"',
                    capture_output=True,
                    shell=True,
                ).stdout,
                "utf-8",
            )

            expected_output_info = str(
                subprocess.run(
                    f'ffprobe -v 0 -of compact=p=0 -select_streams 0 -show_entries stream=width,height,r_frame_rate,duration "{expected_output_file.absolute_path}"',
                    capture_output=True,
                    shell=True,
                ).stdout,
                "utf-8",
            )

            assert input_info != output_info
            assert output_info == expected_output_info
        finally:
            os.remove(self.output_video_path)
