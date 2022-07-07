import os

from src.file.image_file import ImageFile
from os import path


class TestImageFileInstance:
    file = ImageFile("./test/resource/img/test.jpg")

    def test_image_file_get_width(self):
        assert self.file.get_width() == 800

    def test_image_file_get_height(self):
        assert self.file.get_height() == 800

    def test_image_file_get_data(self):
        assert len(self.file.get_data()) == 800**2


class TestCreateNewImageFromString:
    def test_create_new_image_from_string(self):
        new_image_file_path = "./test_new_image_from_string.jpeg"

        try:
            ImageFile.create_new_image_from_string(
                "abc123", (100, 100), new_image_file_path, False
            )
            assert path.exists(new_image_file_path)
            assert path.getsize(new_image_file_path) == 791
        finally:
            os.remove(new_image_file_path)
