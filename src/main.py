import sys

from src.file.file import File, FileType
from src.file.image_file import ImageFile
from src.file.video_file import VideoFile
from options import Options
from transform import transform_image, transform_video

REDUCTION_FACTOR = 'reduction_factor'
INVERTED_COLORS = "inverted_colors"
INPUT = "input"
INPLACE = "inplace"
TEXT_FILE = "text_file"

HELP_FLAG_MESSAGE = "Use -help to see all available arguments."

options: Options = {
    "inplace": False,
    "text_file": False,
    "input": [],
    "reduction_factor": 1,
    "inverted_colors": False
}


def init():
    if len(sys.argv) > 1:
        for arg in enumerate(sys.argv):
            if arg[0] == 0:
                continue

            if File.is_input_file(arg[1]):
                file_path = arg[1]
                file_type = FileType.get_file_type(file_path)

                if file_type is FileType.Image:
                    options[INPUT].append(ImageFile(file_path))
                elif file_type is FileType.Video:
                    options[INPUT].append(VideoFile(file_path))
                else:
                    print(f"Unsupported file type provided: {file_path}. Supported types: .jpg, .png, .mp4, .avi")

                continue

            if "--reduction=" in arg[1]:
                options[REDUCTION_FACTOR] = int(arg[1].split("=")[1])
                continue

            if "--output_path=" in arg[1]:
                print("--output_path hasn't been implemented yet")

            match arg[1]:
                case "-inplace":
                    options[INPLACE] = True
                case "-text_file":
                    options[TEXT_FILE] = True
                case "-help":
                    print("TODO. Sorry can't help ya right now.")
                case "-inverted":
                    options[INVERTED_COLORS] = True
                case _:
                    raise Exception(f"Argument #{arg[0]} is invalid: {arg[1]}. {HELP_FLAG_MESSAGE}")

    else:
        raise Exception(f"No arguments provided. {HELP_FLAG_MESSAGE}")


if __name__ == "__main__":
    init()

    for file in options[INPUT]:
        if isinstance(file, ImageFile):
            transformed_data = transform_image(file, options[REDUCTION_FACTOR])

            if options[TEXT_FILE]:
                File.create_new_file(transformed_data, f"./{file.name}_asciiator.txt")

            new_image_path = file.absolute_path if options[INPLACE] else f"./{file.name}_asciiator.{file.extension}"

            ImageFile.create_new_image_from_string(transformed_data,
                                                   (
                                                       int(file.get_width() * 6 / options[REDUCTION_FACTOR]),
                                                       int(file.get_height() * 7.5 / options[REDUCTION_FACTOR])
                                                   ),
                                                   new_image_path,
                                                   options[INVERTED_COLORS])

        if isinstance(file, VideoFile):
            transform_video(file)
