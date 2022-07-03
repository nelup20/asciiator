import sys
from warnings import warn

from src.file.file import File, FileType
from src.file.image_file import ImageFile
from src.file.video_file import VideoFile


class Options:
    inplace = False
    text_file = False
    input = []
    reduction_factor = 1
    inverted_colors = False
    output_path = "./"

    _HELP_FLAG_MESSAGE = "Use -help to see all available arguments."

    def __init__(self) -> None:
        if len(sys.argv) > 1:
            for arg in enumerate(sys.argv):
                if arg[0] == 0:
                    continue

                if File.is_input_file(arg[1]):
                    file_path = arg[1]
                    file_type = FileType.get_file_type(file_path)

                    if file_type is FileType.Image:
                        self.input.append(ImageFile(file_path))
                    elif file_type is FileType.Video:
                        self.input.append(VideoFile(file_path))
                    else:
                        print(f"Unsupported file type provided: {file_path}. Supported types: .jpg, .png, .mp4, .avi")

                    continue

                if "--reduction=" in arg[1]:
                    self.reduction_factor = int(arg[1].split("=")[1])
                    continue

                if "--output_path=" in arg[1]:
                    self.output_path = arg[1].split("=")[1]
                    warn("Warning: if the -inplace flag is present, the original absolute path will be used and "
                         "the custom output_path will be ignored.")
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
                        raise Exception(f"Argument #{arg[0]} is invalid: {arg[1]}. {self._HELP_FLAG_MESSAGE}")

        else:
            raise Exception(f"No arguments provided. {self._HELP_FLAG_MESSAGE}")