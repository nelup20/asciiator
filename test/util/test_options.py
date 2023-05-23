import pytest

from src.file.file import FileType
from src.util.options import Options

from test.helpers import clean_up_sys_argv, handle_sys_args

clean_up_sys_argv()

TEST_IMAGE_PATH = "./test/resource/img/input/test.jpg"
TEST_VIDEO_PATH = "./test/resource/video/input/test.mp4"


class TestOptions:
    @pytest.mark.parametrize("handle_sys_args", [["invalid_arg_123"]], indirect=True)
    def test_options_invalid_argument(self, handle_sys_args):
        try:
            Options()
        except Exception as exception:
            assert (
                f"{exception}" == f"Invalid file type for input: invalid_arg_123\n"
                f"Supported file types: {FileType.get_supported_file_extensions()}"
            )

    @pytest.mark.parametrize(
        "handle_sys_args", [[TEST_IMAGE_PATH, "--inplace"]], indirect=True
    )
    def test_options_inplace(self, handle_sys_args):
        options = Options()

        assert options.inplace

    @pytest.mark.parametrize(
        "handle_sys_args", [[TEST_IMAGE_PATH, "--reduction", "3"]], indirect=True
    )
    def test_options_reduction(self, handle_sys_args):
        options = Options()

        assert options.reduction_factor == 3

    @pytest.mark.parametrize(
        "handle_sys_args", [[TEST_IMAGE_PATH, "--text_file"]], indirect=True
    )
    def test_options_text_file(self, handle_sys_args):
        options = Options()

        assert options.text_file

    @pytest.mark.parametrize(
        "handle_sys_args", [[TEST_IMAGE_PATH, "--inverted"]], indirect=True
    )
    def test_options_inverted(self, handle_sys_args):
        options = Options()

        assert options.inverted_colors

    @pytest.mark.parametrize(
        "handle_sys_args",
        [[TEST_IMAGE_PATH, "--output_path", "./test/123/"]],
        indirect=True,
    )
    def test_options_output_path(self, handle_sys_args):
        options = Options()

        assert options.output_path == "./test/123/"

    @pytest.mark.parametrize("handle_sys_args", [[TEST_VIDEO_PATH]], indirect=True)
    def test_options_input_video_file(self, handle_sys_args):
        options = Options()

        assert len(options.input) == 1
        assert options.input[0].name == "test"
        assert options.input[0].extension == "mp4"
        assert options.input[0].get_name_with_extension() == "test.mp4"
        assert options.input[0].type == FileType.Video

    @pytest.mark.parametrize("handle_sys_args", [[TEST_IMAGE_PATH]], indirect=True)
    def test_options_input_image_file(self, handle_sys_args):
        options = Options()

        assert len(options.input) == 1
        assert options.input[0].name == "test"
        assert options.input[0].extension == "jpg"
        assert options.input[0].get_name_with_extension() == "test.jpg"
        assert options.input[0].type == FileType.Image
