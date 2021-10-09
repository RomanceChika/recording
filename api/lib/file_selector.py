import datetime
import os

from time import sleep
from pathlib import Path

from api.path_manager import PathManager


class FileSelector(object):
    """
    対象ファイルを選択するためのクラス
    Usage:
        file_selector = FileSelector(minute)
        file_list = file_selector.select_files()
    """

    def __init__(self, minute: int):
        """
        コンストラクタが呼ばれた段階のタイムスタンプによって対象ファイルを確定される
        Args:
            minute(int): 何分間のデータを取るか
        """
        self.minute = minute
        self.current_time = self._current_time()

    def select_files(self) -> list:
        """
        対象ファイルのパスのリストをソートした状態で返す
        Returns:
            list(Path)
        """
        time_list = self.get_time_list(self.current_time, self.minute)
        file_list = list()
        current_time_data_path = PathManager.data_path() / f"{time_list[-1]}.mp3"
        # 1日前の現在時刻ファイルを判定に使うと音声がおかしくなるので一旦削除
        if os.path.exists(str(current_time_data_path)):
            os.remove(str(current_time_data_path))
        count = 0
        # 現在時刻分が生成されるまで待つ
        while not os.path.exists((str(current_time_data_path))):
            sleep(5)
            count += 1
            # 1分待ってもできない場合は何かしらの理由でもうできないので抜ける
            if count > 12:
                break
        # 録音が存在する場合にリストに追加していく
        for target_time in time_list:
            data_path = PathManager.data_path() / f"{target_time}.mp3"
            if os.path.exists(str(data_path)):
                file_list.append(data_path)

        return file_list

    @staticmethod
    def get_time_list(current_time, minute) -> list:
        """
        対象となる時間のリストを取得する
        テストしやすいようにstatic
        Args:
            current_time: hh_mm
            minute: 1以上の整数

        Returns:
            list(str)
        """
        time_list = list()
        time_list.append(current_time)
        tmp_time = current_time
        # 対象分間分ループを回して追加していく
        for i in range(0, minute-1):
            tmp_hour = int(tmp_time[0:2])
            tmp_minute = int(tmp_time[3:5])
            # 日付をまたいで遡る場合
            if tmp_hour == 0 and tmp_minute == 0:
                tmp_time = '23_59'
            # 時間0分をまたいで遡る場合
            elif tmp_minute == 0:
                tmp_time = f"{str(tmp_hour-1).zfill(2)}_59"
            # その他
            else:
                tmp_time = f"{str(tmp_hour).zfill(2)}_{str(tmp_minute-1).zfill(2)}"
            time_list.append(tmp_time)

        # 古い順にソートしなおす
        return list(reversed(time_list))

    @staticmethod
    def _current_time() -> str:
        """
        現在の時刻をhh_mmで取得
        Returns:
            str -> hh_mm
        """
        now_datetime = datetime.datetime.now()
        return f"{str(now_datetime.hour).zfill(2)}_{str(now_datetime.minute).zfill(2)}"


if __name__ == '__main__':
    file_selector = FileSelector(3)
    print(file_selector.select_files())
