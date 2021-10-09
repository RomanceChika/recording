# 録音API

常時録音をして必要な時に必要な時間分のmp3を取得するためのAPI

## 環境構築

1. SOXのインストール
2. ffmpegのインストール
3. Pythonの環境構築
4. requirements.txtのインストール
5. サーバの設定(nginxなど)

## 使い方

- 録音

recording/main.pyを実行すると1分ごとに録音が行われる  
24時間以降は上書きされる

- 取得

api/run.pyでAPIを起動  

#### エンドポイント

/donwload
/downloadエンドポイントにGETリクエストを送ると
