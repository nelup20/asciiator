from typing import TypedDict, List
from src.file.file import File


class Options(TypedDict):
    inplace: bool
    input: List[File]
    reduction_factor: int
    inverted_colors: bool
