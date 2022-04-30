from typing import TypedDict, List
from file import File


class Options(TypedDict):
    inplace: bool
    input: List[File]
