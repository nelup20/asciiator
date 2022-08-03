from src.file.video_file import VideoFile


class TestVideoFileInstance:
    file = VideoFile("./test/resource/video/test.mp4")

    def test_video_file_get_data(self):
        assert len(self.file.get_data()) == 0
