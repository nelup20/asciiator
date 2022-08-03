import sys
from typing import List
from warnings import warn

from .file.file import File, FileType
from .file.image_file import ImageFile
from .file.video_file import VideoFile


class Options:
    def __init__(self) -> None:
        self.inplace = False
        self.text_file = False
        self.input: List[File] = []
        self.reduction_factor = 1
        self.inverted_colors = False
        self.output_path = "./"

        self._HELP_FLAG_MESSAGE = "Use -help to see all available arguments."

        if len(sys.argv) > 1:
            for arg in enumerate(sys.argv):
                if arg[0] == 0:
                    continue

                if File.is_input_file(arg[1]):
                    file_path = arg[1]
                    file_type = FileType.get_file_type(file_path)

                    if file_type is FileType.Image:
                        self.input.append(ImageFile(file_path))

                    if file_type is FileType.Video:
                        self.input.append(VideoFile(file_path))

                    continue

                if "--reduction=" in arg[1]:
                    self.reduction_factor = int(arg[1].split("=")[1])
                    continue

                if "--output_path=" in arg[1]:
                    self.output_path = arg[1].split("=")[1]
                    warn(
                        "Warning: if the -inplace flag is present, the original absolute path will be used and "
                        "the custom output_path will be ignored."
                    )
                    continue

                match arg[1]:
                    case "-inplace":
                        self.inplace = True
                    case "-text_file":
                        self.text_file = True
                    case "-help":
                        print("TODO. Sorry can't help ya right now.")
                    case "-inverted":
                        self.inverted_colors = True
                    case _:
                        raise Exception(
                            f"Argument #{arg[0]} is invalid: {arg[1]}. {self._HELP_FLAG_MESSAGE}"
                        )

        else:
            raise Exception(f"No arguments provided. {self._HELP_FLAG_MESSAGE}")
