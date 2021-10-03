import datetime
import signal
import subprocess
import threading

from time import sleep


def recording():
    """
    録音を行うメインメソッド
    1分ごとに録音をして保存する
    日付は特定しないので1日後には上書きされる仕様
    """
    # ハンドラの設定
    signal.signal(signal.SIGALRM, sig)

    # インターバルタイマー設定
    # 最初の開始タイミング0.1秒後、以後60秒間
    signal.setitimer(signal.ITIMER_REAL, 0.1, 60)

    # ハンドラが定時で動くのでsleepでプロセスを生かし続ける
    try:
        while True:
            sleep(3600)
    except Exception as e:
        print(e)
    pass


def sig(signum, frame):
    """
    定時実行されるプログラム
    引数は自動的に渡されるもので、特に使用しない
    Args:
        signum:
        frame:
    """
    # シグナルに対して毎分実行するために一応非同期で処理を走らせる
    current_time = get_current_time()
    t1 = threading.Thread(target=record_by_sox, args=(current_time,))
    t1.start()


def record_by_sox(current_time: str):
    """
    1分間の録音を行う

    Args:
        current_time: hh_mmで指定される現在時刻文字列
    """
    # SOXのコマンドで録音をする
    ps = subprocess.Popen(("rec", "-q", f"../data/{current_time}.mp3"))
    # 1分間経ったらプロセスを止めて録音を確定させる
    sleep(60)
    ps.terminate()


def get_current_time() -> str:
    """
    hh_mm形式で今の時間を取得する
    Returns:
        str -> hh_mm
    """
    now_datetime = datetime.datetime.now()
    return f"{str(now_datetime.hour).zfill(2)}_{str(now_datetime.minute).zfill(2)}"


if __name__ == '__main__':
    # 録音を実行
    recording()

