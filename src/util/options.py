import sys
from os import path
from typing import List
from warnings import warn

from src.file.file import File, FileType
from src.file.gif_file import GifFile
from src.file.image_file import ImageFile
from src.file.video_file import VideoFile

HELP_MESSAGE = """
Asciiator has the following optional flags:
-inplace                Modify the file inplace. 
                        The original file will be transformed to ASCII and no new output file will be generated.

-help                   Display the help documentation

-inverted               Invert the colors for the background and text. 
                        By default, the background color is white (255) and the text color is black (0). 
                        If -inverted is present, the background will be black and the text color will be white.

-text_file              Save the transformed ASCII art to a .txt file as well 
                        (only applicable when the input is a image)

--reduction=x           Reduce the output by a factor of x (int). Default value: 4. 
                        Example: --reduction=2 to convert half of the pixels to ASCII

--output_path="x"       Specify the output path where all new files will be created. 
                        By default it's the current directory. 
                        Warning: if the -inplace flag is present, then this flag will be ignored, 
                        so the original absolute path will be used.
"""


class Options:
    def __init__(self) -> None:
        self.inplace = False
        self.text_file = False
        self.input: List[File] = []
        self.reduction_factor = 4
        self.inverted_colors = False
        self.output_path = "."

        self._HELP_FLAG_MESSAGE = "Use -help to see all available flags."

        if len(sys.argv) > 1:
            for arg in enumerate(sys.argv):
                if arg[0] == 0:
                    continue

                if File.is_input_file(arg[1]):
                    file_path = arg[1]
                    file_type = FileType.get_file_type(file_path)

                    if not path.exists(file_path):
                        raise FileNotFoundError(file_path)

                    if file_type is FileType.Image:
                        self.input.append(ImageFile(file_path))

                    if file_type is FileType.Video:
                        self.input.append(VideoFile(file_path))

                    if file_type is FileType.Gif:
                        self.input.append(GifFile(file_path))

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
                        sys.exit(HELP_MESSAGE)
                    case "-inverted":
                        self.inverted_colors = True
                    case _:
                        raise Exception(
                            f"Argument #{arg[0]} is invalid: {arg[1]}. {self._HELP_FLAG_MESSAGE}"
                        )
        else:
            raise Exception(f"No arguments provided. {self._HELP_FLAG_MESSAGE}")
