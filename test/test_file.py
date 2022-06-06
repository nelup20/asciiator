import unittest

from src.file.file import File, FileType


class TestIsInputFile(unittest.TestCase):
    def test_is_input_file_jpeg_success(self):
        self.assertEqual(True, File.is_input_file("test.jpeg"))

    def test_is_input_file_jpg_success(self):
        self.assertEqual(True, File.is_input_file("test.jpg"))

    def test_is_input_file_png_success(self):
        self.assertEqual(True, File.is_input_file("test.png"))

    def test_is_input_file_mp4_success(self):
        self.assertEqual(True, File.is_input_file("test.mp4"))

    def test_is_input_file_avi_success(self):
        self.assertEqual(True, File.is_input_file("test.avi"))

    def test_is_input_file_failure(self):
        self.assertEqual(False, File.is_input_file("test.abc"))


class TestGetFileType(unittest.TestCase):
    def test_get_file_type_jpeg_success(self):
        self.assertEqual(FileType.Image, FileType.get_file_type("test.jpeg"))

    def test_get_file_type_jpg_success(self):
        self.assertEqual(FileType.Image, FileType.get_file_type("test.jpg"))

    def test_get_file_type_png_success(self):
        self.assertEqual(FileType.Image, FileType.get_file_type("test.png"))

    def test_get_file_type_mp4_success(self):
        self.assertEqual(FileType.Video, FileType.get_file_type("test.mp4"))

    def test_get_file_type_avi_success(self):
        self.assertEqual(FileType.Video, FileType.get_file_type("test.avi"))

    def test_get_file_type_other(self):
        self.assertEqual(FileType.Other, FileType.get_file_type("test.abc"))


if __name__ == '__main__':
    unittest.main()
