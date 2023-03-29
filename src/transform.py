import os
import subprocess
import tempfile
from glob import glob
from math import floor

from .file.image_file import ImageFile
from .file.video_file import VideoFile
from .options import Options

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


def transform_video(video_file: VideoFile, options: Options) -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Get framerate
        get_framerate_subprocess = subprocess.run(
            f'ffprobe -v 0 -of compact=p=0 -select_streams 0 -show_entries stream=r_frame_rate "{video_file.absolute_path}"',
            capture_output=True,
        )
        framerate = str(get_framerate_subprocess.stdout, "utf-8").strip().split("=")[1]

        # Extract frames
        subprocess.run(
            f'ffmpeg -i "{video_file.absolute_path}" -vsync 0 "{temp_dir}/frame_$filename%06d.jpg"'
        )

        # Extract audio
        subprocess.run(
            f'ffmpeg -i "{video_file.absolute_path}" -q:a 0 -map a "{temp_dir}/audio.mp3"'
        )

        # Transform frames
        # TODO: refactor
        frame_list = glob(os.path.join(temp_dir, "*.jpg"))
        number_of_frames = len(frame_list)
        for i, frame in enumerate(frame_list):
            print(f"Transforming frame {i+1}/{number_of_frames}")

            frame_file = ImageFile(frame)

            transformed_data = transform_image(frame_file, options.reduction_factor)

            ImageFile.create_new_image_from_string(
                transformed_data,
                (
                    int(frame_file.get_width() * 6 / options.reduction_factor),
                    int(frame_file.get_height() * 7.5 / options.reduction_factor),
                ),
                frame_file.absolute_path,
                options.inverted_colors,
            )

        # Combine frames back into video
        subprocess.run(
            f'ffmpeg -framerate {framerate} -i "{temp_dir}/frame_$filename%06d.jpg" -vf pad="width=ceil(iw/2)*2:height=ceil(ih/2)*2" -shortest -pix_fmt yuv420p "{temp_dir}/combined.mp4"'
        )

        new_video_path = (
            video_file.absolute_path
            if options.inplace
            else f"{options.output_path}/{video_file.name}_asciiator.mp4"
        )

        # Add audio back to video
        subprocess.run(
            f'ffmpeg -i "{temp_dir}/combined.mp4" -i "{temp_dir}/audio.mp3" -c copy -map 0:v:0 -map 1:a:0 "{new_video_path}"'
        )
