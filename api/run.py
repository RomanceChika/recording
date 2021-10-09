from flask import Flask, request, jsonify, send_file

from lib.file_selector import FileSelector
from lib.sound_connector import SoundConnector
from lib.utility import Utility

app = Flask(__name__)


@app.route('/download', methods=['GET'])
def download():
    minute = request.args.get('minute')
    file_name = request.args.get('filename')
    #  引数が存在するときのみ処理
    if minute is not None:
        fs = FileSelector(int(minute))
        file_list = fs.select_files()
        # 命名が指定されていない場合は自動的につける
        if file_name is None or file_name is '':
            file_name = Utility.default_file_name(file_list)
        sc = SoundConnector()
        sc.connect_sound(file_list, file_name)
        download_file_name = f"{file_name}.mp3"
        download_file = f"tmp/{file_name}.mp3"
        return send_file(download_file, as_attachment=True, attachment_filename=download_file_name,
                         mimetype='audio/mpeg')
    else:
        return jsonify({'message': 'minute is required'}), 500


if __name__ == '__main__':
    app.run()
