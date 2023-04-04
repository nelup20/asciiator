from PIL import Image, ImageDraw, ImageFont

from src.file.image_file import ImageFile


class GifFile(ImageFile):
    def __init__(self, relative_path: str) -> None:
        # Original image can't be converted to greyscale, only individual frames (otherwise end result is a still image)
        super().__init__(relative_path, greyscale=False)

    def transform(self, options):
        new_frame_list = [
            self.transform_frame(frame, options)
            for frame in range(0, self.opened_file.n_frames)
        ]

        new_frame_list[0].save(
            self.get_new_image_path(options),
            save_all=True,
            append_images=new_frame_list[1:],
            duration=self.opened_file.info["duration"],
            loop=0,
        )

    def transform_frame(self, frame: int, options) -> Image.Image:
        self.opened_file.seek(frame)
        transformed_data = self.transform_data(
            options, self.opened_file.convert("L").getdata()
        )

        background_color, text_color = self.get_new_image_colors(options)

        new_frame = Image.new(
            "L", size=self.get_new_image_size(options), color=background_color
        )
        ImageDraw.Draw(new_frame).text(
            (0, 0), transformed_data, font=ImageFont.load_default(), fill=text_color
        )

        return new_frame
