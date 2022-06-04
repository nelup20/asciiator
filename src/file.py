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
            self.opened_file = Image.open(self.absolute_path).convert("L")

    @classmethod
    def is_input_file(cls, arg: str) -> bool:
        return arg.endswith((".jpg", ".jpeg", ".mp4"))

    @classmethod
    def create_new_file(cls, data, path) -> None:
        with open(abspath(path), "w") as new_file:
            new_file.write(data)

    def get_data(self) -> bytearray:
        return self.opened_file.getdata()

    def get_name_with_extension(self) -> str:
        return f"{self.name}.{self.extension}"

    def get_width(self) -> int:
        return self.opened_file.width

    def get_height(self) -> int:
        return self.opened_file.height

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
