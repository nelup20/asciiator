from .file import File


class VideoFile(File):
    def __init__(self, relative_path: str) -> None:
        super().__init__(relative_path)

    def get_data(self) -> bytearray:
        return bytearray()
