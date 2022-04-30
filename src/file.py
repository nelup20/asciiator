from __future__ import annotations
from enum import Enum, auto
from os.path import abspath


class File:
    name = ""
    relative_path = ""
    absolute_path = ""
    type = None

    def __init__(self, relative_path: str) -> None:
        self.relative_path = relative_path
        self.absolute_path = abspath(relative_path)
        self.name = relative_path.split("/")[-1]
        self.type = FileType.get_file_type(self.name)

    def get_data(self):
        with open(self.absolute_path, "rb") as file:
            return bytearray(file.read())

    @classmethod
    def is_input_file(cls, arg: str) -> bool:
        return True if ".jpg" in arg or ".jpeg" in arg or ".mp4" in arg else False

    # TODO: create as self.name + _asciiator.jpg
    def create_new_file(self, transformed_data):
        with open(abspath(f"./new_test_asciiator.jpg"), "wb") as new_file:
            new_file.write(transformed_data)

    def __str__(self) -> str:
        return f'File @ {hex(id(self))}: name = {self.name}, path = {self.relative_path}, type = {self.type}'


class FileType(Enum):
    Image = auto()
    Video = auto()
    Other = auto()

    @classmethod
    def get_file_type(cls, input_file: str) -> FileType:
        if ".jpg" in input_file or ".jpeg" in input_file:
            return cls.Image

        if ".mp4" in input_file:
            return cls.Video

        return cls.Other
