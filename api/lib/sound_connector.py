import os
import shutil

from pydub import AudioSegment

from api.path_manager import PathManager


class SoundConnector(object):
    """
    音声ファイルを連結するためのクラス
    """

    @staticmethod
    def connect_sound(file_path_list: list, file_name: str):
        """
        指定されたパスの音声を連結して保存する
        Args:
            file_path_list: 音声のパスのリスト
            file_name: 連結した後のファイル名
        """
        full_sound = AudioSegment.empty()
        for file_path in file_path_list:
            sound = AudioSegment.from_mp3(str(file_path))
            full_sound += sound

        output_dir_path = PathManager.root_path() / 'tmp'
        shutil.rmtree(str(output_dir_path))
        os.makedirs(str(output_dir_path), exist_ok=True)
        output_path = output_dir_path / f"{file_name}.mp3"
        print(type(full_sound))
        with output_path.open(mode='wb') as f:
            full_sound.export(f, format='mp3')

