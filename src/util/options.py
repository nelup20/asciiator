from argparse import ArgumentParser
from os import path
from typing import List

from src.file.file import File, FileType
from src.file.gif_file import GifFile
from src.file.image_file import ImageFile
from src.file.video_file import VideoFile


class Options:
    def __init__(self) -> None:
        self.input: List[File] = []

        arg_parser = ArgumentParser(
            prog="asciiator",
            description="Transform any Image or Video file into ASCII",
            allow_abbrev=False,
        )

        arg_parser.add_argument(
            "input_files",
            nargs="+",
            help=f"The paths to each input file. Supported file types: {FileType.get_supported_file_extensions()}",
        )

        arg_parser.add_argument(
            "--inplace",
            action="store_true",
            help="Modify the file inplace. The original file will be transformed to ASCII and no new output file will "
            "be generated.",
        )

        arg_parser.add_argument(
            "--inverted",
            action="store_true",
            help="Invert the colors for the background and text. By default, the background color is black (0) and "
            "the text color is white (255). If -inverted is present, the background will be white and the text "
            "color will be black.",
        )

        arg_parser.add_argument(
            "--text_file",
            action="store_true",
            help="Save the transformed ASCII art to a .txt file as well (only applicable when the input is a image)",
        )

        arg_parser.add_argument(
            "--reduction",
            type=int,
            default=4,
            help="Reduce the output by a factor of x (int). Default value: 4. Example: --reduction 2 to convert half "
            "of the pixels to ASCII",
        )

        arg_parser.add_argument(
            "--output_path",
            type=str,
            default=".",
            help="Specify the output path where all new files will be created. By default it's the current directory. "
            "Warning: if the -inplace flag is present, then this flag will be ignored, so the original absolute "
            "path will be used.",
        )

        arg_parser.add_argument(
            "--version", action="version", version="Asciiator 1.0.1"
        )

        args = arg_parser.parse_args()

        self.inplace = args.inplace
        self.inverted_colors = args.inverted
        self.text_file = args.text_file
        self.reduction_factor = args.reduction
        self.output_path = args.output_path

        for file_path in args.input_files:
            if File.is_input_file(file_path):
                file_type = FileType.get_file_type(file_path)

                if not path.exists(file_path):
                    raise FileNotFoundError(file_path)

                if file_type is FileType.Image:
                    self.input.append(ImageFile(file_path))

                if file_type is FileType.Video:
                    self.input.append(VideoFile(file_path))

                if file_type is FileType.Gif:
                    self.input.append(GifFile(file_path))
            else:
                raise Exception(
                    f"Invalid file type for input: {file_path}\n"
                    f"Supported file types: {FileType.get_supported_file_extensions()}"
                )
