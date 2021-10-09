from pathlib import Path


class PathManager(object):

    @staticmethod
    def root_path() -> Path:
        """
        Returns:
            Path -> APIのルートパス
        """
        return Path(__file__).resolve().parent

    @classmethod
    def data_path(cls) -> Path:
        """
        録音があるdataのディレクトリパス
        Returns:
            Path ->
        """
        return cls.root_path().parent / 'data'


if __name__ == '__main__':
    print(PathManager.data_path())
