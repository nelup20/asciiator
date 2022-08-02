import sys

import pytest

from src.file.file import FileType
from src.options import Options
from .helpers import handle_sys_args

args_to_remove = ["--cov-fail-under=85", "--cov=src", "test"]

for arg in args_to_remove:
    sys.argv.remove(arg)


class TestOptions:
    def test_options_no_arguments(self):
        try:
            Options()
        except Exception as exception:
            assert (
                f"{exception}"
                == "No arguments provided. Use -help to see all available arguments."
            )

    @pytest.mark.parametrize("handle_sys_args", ["invalid_arg_123"], indirect=True)
    def test_options_invalid_argument(self, handle_sys_args):
        try:
            Options()
        except Exception as exception:
            assert (
                f"{exception}"
                == "Argument #1 is invalid: invalid_arg_123. Use -help to see all available arguments."
            )

    @pytest.mark.parametrize("handle_sys_args", ["-inplace"], indirect=True)
    def test_options_inplace(self, handle_sys_args):
        options = Options()

        assert options.inplace

    @pytest.mark.parametrize("handle_sys_args", ["--reduction=3"], indirect=True)
    def test_options_reduction(self, handle_sys_args):
        options = Options()

        assert options.reduction_factor == 3

    @pytest.mark.parametrize("handle_sys_args", ["-text_file"], indirect=True)
    def test_options_text_file(self, handle_sys_args):
        options = Options()

        assert options.text_file

    @pytest.mark.parametrize("handle_sys_args", ["-inverted"], indirect=True)
    def test_options_inverted(self, handle_sys_args):
        options = Options()

        assert options.inverted_colors

    @pytest.mark.parametrize(
        "handle_sys_args", ["--output_path=./test/123/"], indirect=True
    )
    def test_options_output_path(self, handle_sys_args):
        options = Options()

        assert options.output_path == "./test/123/"

    @pytest.mark.parametrize("handle_sys_args", ["test123.mp4"], indirect=True)
    def test_options_input_video_file(self, handle_sys_args):
        options = Options()

        assert len(options.input) == 1
        assert options.input[0].name == "test123"
        assert options.input[0].extension == "mp4"
        assert options.input[0].get_name_with_extension() == "test123.mp4"
        assert options.input[0].type == FileType.Video

    @pytest.mark.parametrize(
        "handle_sys_args", ["./test/resource/img/test.jpg"], indirect=True
    )
    def test_options_input_image_file(self, handle_sys_args):
        options = Options()

        assert len(options.input) == 1
        assert options.input[0].name == "test"
        assert options.input[0].extension == "jpg"
        assert options.input[0].get_name_with_extension() == "test.jpg"
        assert options.input[0].type == FileType.Image

    @pytest.mark.parametrize("handle_sys_args", ["-help"], indirect=True)
    def test_options_input_video_file(self, handle_sys_args, capsys):
        Options()

        assert capsys.readouterr().out == "TODO. Sorry can't help ya right now.\n"
