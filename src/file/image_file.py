from __future__ import annotations

from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as PillowImage

from .file import File


class ImageFile(File):
    def __init__(self, relative_path: str) -> None:
        super().__init__(relative_path)

        self.opened_file: PillowImage = Image.open(self.absolute_path).convert("L")

    @staticmethod
    def create_new_image_from_string(
        data: str, size: tuple[int, int], path: str, inverted_colors: bool
    ) -> None:
        background_color = 0 if inverted_colors else 255
        text_color = 255 if inverted_colors else 0

        new_image = Image.new("L", size=size, color=background_color)
        ImageDraw.Draw(new_image).text(
            (0, 0), data, font=ImageFont.load_default(), fill=text_color
        )

        new_image.save(path)

    def get_data(self) -> bytearray:
        return self.opened_file.getdata()

    def get_width(self) -> int:
        return self.opened_file.width

    def get_height(self) -> int:
        return self.opened_file.height
