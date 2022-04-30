from __future__ import annotations
from enum import Enum, auto

class Input:
    fileName = ""
    filePath = ""
    inputType = None

    @classmethod
    def is_input_file(cls, arg: str) -> bool:
        return True if ".jpg" in arg or ".jpeg" in arg or ".mp4" in arg else False

class InputType(Enum):
    Image = auto()
    Video = auto()
    Other = auto()

    @classmethod
    def get_input_type(cls, input_file: str) -> InputType:
        if ".jpg" in input_file or ".jpeg" in input_file:
            return cls.Image

        if ".mp4" in input_file:
            return cls.Video

        return cls.Other
