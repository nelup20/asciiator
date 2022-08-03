from math import floor

from .file.image_file import ImageFile
from .file.video_file import VideoFile

ASCII_MAPPING_INTERVAL = 11

ASCII_MAPPING = {
    (0, 11): " ",
    (11, 22): "'",
    (22, 33): ":",
    (33, 44): "<",
    (44, 55): ">",
    (55, 66): "!",
    (66, 77): "?",
    (77, 88): ";",
    (88, 99): "@",
    (99, 110): "=",
    (110, 121): "$",
    (121, 132): "#",
    (132, 143): "%",
    (143, 154): "&",
    (154, 165): "[",
    (165, 176): "]",
    (176, 187): "{",
    (187, 198): "}",
    (198, 209): "(",
    (209, 220): ")",
    (220, 231): "-",
    (231, 242): ",",
    (242, 253): ".",
}


# TODO: This reduction_factor essentially just skips lines/pixels, so I'm assuming it's not ideal. Maybe take the
#  average value of the surrounding/grouped pixels instead?
def transform_image(file: ImageFile, reduction_factor: int) -> str:
    image_data = file.get_data()

    ascii_data = []

    for row in range(0, file.get_height(), reduction_factor * 2):
        for column in range(
            row * file.get_width(), (row + 1) * file.get_width(), reduction_factor
        ):
            pixel = image_data[column]
            upper_bound = floor(pixel / ASCII_MAPPING_INTERVAL) * ASCII_MAPPING_INTERVAL
            char = (
                " "
                if upper_bound == 0
                else ASCII_MAPPING[(upper_bound - ASCII_MAPPING_INTERVAL, upper_bound)]
            )

            ascii_data.append(char)

            if column % file.get_width() == 0:
                ascii_data.append("\n")

    return "".join(ascii_data)


def transform_video(file: VideoFile) -> bytearray:
    return file.get_data()
