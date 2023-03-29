from src.file.image_file import ImageFile
from src.file.video_file import VideoFile
from src.transform import transform_video, transform_image


class TestTransform:
    def test_transform_image(self):
        transformed_data = transform_image(ImageFile("./test/resource/img/test.jpg"), 3)

        with open(
            "./test/resource/test_image_expected_text_output.txt"
        ) as expected_output_file:
            expected_output = expected_output_file.read()
            assert transformed_data == expected_output

    def test_transform_video(self):
        # TODO
        # assert len(transform_video(VideoFile("test.mp4"))) == 0
        pass
