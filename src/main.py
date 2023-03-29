from os import makedirs, path

from .file.file import File
from .file.image_file import ImageFile
from .file.video_file import VideoFile
from .options import Options
from .transform import transform_image, transform_video


def main():
    options = Options()

    if not options.inplace and not path.exists(options.output_path):
        makedirs(options.output_path)

    for file in options.input:
        if isinstance(file, ImageFile):
            transformed_data = transform_image(file, options.reduction_factor)

            if options.text_file:
                File.create_new_file(
                    transformed_data, f"{options.output_path}/{file.name}_asciiator.txt"
                )

            new_image_path = (
                file.absolute_path
                if options.inplace
                else f"{options.output_path}/{file.name}_asciiator.{file.extension}"
            )

            ImageFile.create_new_image_from_string(
                transformed_data,
                (
                    int(file.get_width() * 6 / options.reduction_factor),
                    int(file.get_height() * 7.5 / options.reduction_factor),
                ),
                new_image_path,
                options.inverted_colors,
            )

        if isinstance(file, VideoFile):
            transform_video(file, options)


if __name__ == "__main__":
    main()
