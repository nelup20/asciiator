from __future__ import annotations
from enum import Enum, auto
from os.path import abspath
from PIL import Image


class File:
    name = ""
    extension = ""
    relative_path = ""
    absolute_path = ""
    type = None
    opened_file = None

    def __init__(self, relative_path: str) -> None:
        self.relative_path = relative_path
        self.absolute_path = abspath(relative_path)

        name = relative_path.split("/")[-1]
        self.extension = name.split(".")[-1]
        self.name = name.removesuffix(f".{self.extension}")

        self.type = FileType.get_file_type(self.get_name_with_extension())

        if self.type is FileType.Image:
            self.opened_file = Image.open(self.absolute_path)

    @classmethod
    def is_input_file(cls, arg: str) -> bool:
        return arg.endswith((".jpg", ".jpeg", ".mp4"))

    def get_data(self) -> bytearray:
        return self.opened_file.getdata()

    def get_name_with_extension(self) -> str:
        return f"{self.name}.{self.extension}"

    def create_new_file(self, transformed_data) -> None:
        new_file = Image.new(self.opened_file.mode, self.opened_file.size)
        new_file.putdata(transformed_data)
        new_file.save(abspath(f"./{self.name}_asciiator.{self.extension}"))

    def __str__(self) -> str:
        return f'File @ {hex(id(self))}: name = {self.name}, path = {self.relative_path}, type = {self.type}'


class FileType(Enum):
    Image = auto()
    Video = auto()
    Other = auto()

    @classmethod
    def get_file_type(cls, input_file: str) -> FileType:
        if input_file.endswith((".jpg", ".jpeg")):
            return cls.Image

        if input_file.endswith((".mp4", ".avi")):
            return cls.Video

        return cls.Other
