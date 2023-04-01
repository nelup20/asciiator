import os
from os import path

from src.file.file import File, FileType


class TestIsInputFile:
    def test_is_input_file_jpeg_success(self):
        assert File.is_input_file("test.jpeg")

    def test_is_input_file_jpg_success(self):
        assert File.is_input_file("test.jpg")

    def test_is_input_file_png_success(self):
        assert File.is_input_file("test.png")

    def test_is_input_file_mp4_success(self):
        assert File.is_input_file("test.mp4")

    def test_is_input_file_avi_success(self):
        assert File.is_input_file("test.avi")

    def test_is_input_file_failure(self):
        assert not File.is_input_file("test.abc")


class TestGetFileType:
    def test_get_file_type_jpeg_success(self):
        assert FileType.get_file_type("test.jpeg") == FileType.Image

    def test_get_file_type_jpg_success(self):
        assert FileType.get_file_type("test.jpg") == FileType.Image

    def test_get_file_type_png_success(self):
        assert FileType.get_file_type("test.png") == FileType.Image

    def test_get_file_type_mp4_success(self):
        assert FileType.get_file_type("test.mp4") == FileType.Video

    def test_get_file_type_avi_success(self):
        assert FileType.get_file_type("test.avi") == FileType.Video

    def test_get_file_type_other(self):
        assert FileType.get_file_type("test.abc") == FileType.Other


class TestCreateNewFile:
    def test_create_new_text_file_success(self):
        new_file_path = "./test_output.txt"
        new_file_data = "abc123"

        File.create_new_file(new_file_data, new_file_path)

        assert path.exists(new_file_path)

        try:
            with open(new_file_path) as created_file:
                created_file_data = created_file.readlines()
                assert created_file_data[0] == new_file_data
        finally:
            os.remove(new_file_path)
