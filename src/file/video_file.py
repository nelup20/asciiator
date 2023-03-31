import os
import subprocess
import tempfile
from glob import glob

from .file import File
from .image_file import ImageFile


def _transform_frame(frame: str, options) -> None:
    frame_file = ImageFile(frame)

    transformed_data = frame_file.transform_data(options)

    ImageFile.create_new_image_from_string(
        transformed_data,
        (
            int(frame_file.get_width() * 6 / options.reduction_factor),
            int(frame_file.get_height() * 7.5 / options.reduction_factor),
        ),
        frame_file.absolute_path,
        options,
    )


class VideoFile(File):
    def __init__(self, relative_path: str) -> None:
        super().__init__(relative_path)

    def transform(self, options) -> None:
        with tempfile.TemporaryDirectory(prefix="asciiator_") as temp_dir:
            # Get framerate
            get_framerate_subprocess = subprocess.run(
                f'ffprobe -v 0 -of compact=p=0 -select_streams 0 -show_entries stream=r_frame_rate "{self.absolute_path}"',
                capture_output=True,
                shell=True,
            )
            framerate = (
                str(get_framerate_subprocess.stdout, "utf-8").strip().split("=")[1]
            )

            # Extract frames
            subprocess.run(
                f'ffmpeg -i "{self.absolute_path}" -vsync 0 "{temp_dir}/frame_$filename%06d.jpg"',
                shell=True
            )

            # Extract audio
            subprocess.run(
                f'ffmpeg -i "{self.absolute_path}" -q:a 0 -map a "{temp_dir}/audio.mp3"',
                shell=True
            )

            # Transform frames
            frame_list = glob(os.path.join(temp_dir, "*.jpg"))

            for frame in frame_list:
                _transform_frame(frame, options)

            # Combine frames back into video
            subprocess.run(
                f'ffmpeg -framerate {framerate} -i "{temp_dir}/frame_$filename%06d.jpg" -vf pad="width=ceil(iw/2)*2:height=ceil(ih/2)*2" -shortest -pix_fmt yuv420p "{temp_dir}/combined.mp4"',
                shell=True
            )

            # Add audio back to video
            new_video_path = (
                self.absolute_path
                if options.inplace
                else f"{options.output_path}/{self.name}_asciiator.mp4"
            )

            subprocess.run(
                f'ffmpeg -i "{temp_dir}/combined.mp4" -i "{temp_dir}/audio.mp3" -c copy -map 0:v:0 -map 1:a:0 "{new_video_path}"',
                shell=True
            )
