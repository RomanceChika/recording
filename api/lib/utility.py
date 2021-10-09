import datetime


class Utility(object):
    """
    ユーティリティークラス
    """

    @staticmethod
    def default_file_name(file_path_list: list) -> str:
        """
        デフォルトで名前がついてない場合の命名
        yyyy-MM-dd-hh_mm-hh-mm
        Args:
            file_path_list:

        Returns:
            str ->
        """
        today = datetime.date.today()
        start_file_name = file_path_list[0].stem
        end_file_name = file_path_list[-1].stem
        return f"{today}-{start_file_name}-{end_file_name}"
