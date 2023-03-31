import os

import pytest

from src.file.file import FileType
from src.file.image_file import ImageFile
from os import path

from src.options import Options
from ..helpers import clean_up_sys_argv, handle_sys_args

clean_up_sys_argv()


class TestImageFileInstance:
    file = ImageFile("./test/resource/img/input/test.jpg")

    def test_image_file_get_width(self):
        assert self.file.get_width() == 800

    def test_image_file_get_height(self):
        assert self.file.get_height() == 800

    def test_image_file_get_data(self):
        assert len(self.file.get_data()) == 800**2

    def test_image_file_instance(self):
        assert self.file.name == "test"
        assert self.file.extension == "jpg"
        assert self.file.relative_path == "./test/resource/img/input/test.jpg"
        assert self.file.type == FileType.Image

    def test_get_name_with_extension(self):
        assert self.file.get_name_with_extension() == "test.jpg"

    def test_file_instance_to_string(self):
        assert (
            f"{self.file}"
            == f"File @ {hex(id(self.file))}: name = test, path = ./test/resource/img/input/test.jpg, type = FileType.Image"
        )


@pytest.mark.parametrize(
    "handle_sys_args", [["./test/resource/img/input/test.jpg"]], indirect=True
)
class TestCreateNewImageFromString:
    def test_create_new_image_from_string(self, handle_sys_args):
        new_image_file_path = "./test_new_image_from_string.jpeg"

        try:
            ImageFile.create_new_image_from_string(
                "abc123", (100, 100), new_image_file_path, Options()
            )
            assert path.exists(new_image_file_path)
            assert path.getsize(new_image_file_path) == 791
        finally:
            os.remove(new_image_file_path)


@pytest.mark.parametrize(
    "handle_sys_args",
    [["./test/resource/img/input/test.jpg", "--reduction=3"]],
    indirect=True,
)
class TestTransformImage:
    def test_transform_image(self, handle_sys_args):
        options = Options()
        transformed_data = ImageFile(
            "./test/resource/img/input/test.jpg"
        ).transform_data(options)

        with open(
            "./test/resource/img/output/test_image_expected_text_output.txt"
        ) as expected_output_file:
            expected_output = expected_output_file.read()
            assert transformed_data == expected_output
