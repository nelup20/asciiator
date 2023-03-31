from __future__ import annotations

from math import floor

from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as PillowImage

from .file import File

_ASCII_MAPPING_INTERVAL = 11

_ASCII_MAPPING = {
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


class ImageFile(File):
    def __init__(self, relative_path: str) -> None:
        super().__init__(relative_path)

        self.opened_file: PillowImage = Image.open(self.absolute_path).convert("L")

    def transform(self, options) -> None:
        transformed_data = self.transform_data(options)

        if options.text_file:
            File.create_new_file(
                transformed_data, f"{options.output_path}/{self.name}_asciiator.txt"
            )

        new_image_path = (
            self.absolute_path
            if options.inplace
            else f"{options.output_path}/{self.name}_asciiator.{self.extension}"
        )

        ImageFile.create_new_image_from_string(
            transformed_data,
            (
                int(self.get_width() * 6 / options.reduction_factor),
                int(self.get_height() * 7.5 / options.reduction_factor),
            ),
            new_image_path,
            options,
        )

    @staticmethod
    def create_new_image_from_string(
        data: str, size: tuple[int, int], path: str, options
    ) -> None:
        background_color = 0 if options.inverted_colors else 255
        text_color = 255 if options.inverted_colors else 0

        new_image = Image.new("L", size=size, color=background_color)
        ImageDraw.Draw(new_image).text(
            (0, 0), data, font=ImageFont.load_default(), fill=text_color
        )

        new_image.save(path)

    # This reduction_factor essentially just skips lines/pixels, so I'm assuming it's not an ideal algorithm.
    # Maybe take the average value of the surrounding/grouped pixels instead?
    def transform_data(self, options) -> str:
        image_data = self.get_data()

        ascii_data = []

        for row in range(0, self.get_height(), options.reduction_factor * 2):
            for column in range(
                row * self.get_width(),
                (row + 1) * self.get_width(),
                options.reduction_factor,
            ):
                pixel = image_data[column]
                upper_bound = (
                    floor(pixel / _ASCII_MAPPING_INTERVAL) * _ASCII_MAPPING_INTERVAL
                )
                char = (
                    " "
                    if upper_bound == 0
                    else _ASCII_MAPPING[
                        (upper_bound - _ASCII_MAPPING_INTERVAL, upper_bound)
                    ]
                )

                ascii_data.append(char)

                if column % self.get_width() == 0:
                    ascii_data.append("\n")

        return "".join(ascii_data)

    def get_data(self) -> bytearray:
        return self.opened_file.getdata()

    def get_width(self) -> int:
        return self.opened_file.width

    def get_height(self) -> int:
        return self.opened_file.height
