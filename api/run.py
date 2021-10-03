from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/download', methods=['GET'])
def download():
    minute = request.args.get('minute')
    if minute is not None:
        # TODO: 処理
        return jsonify({'message': 'ok'}), 400
    else:
        return jsonify({'message': 'minute is required'}), 500


if __name__ == '__main__':
    app.run()
