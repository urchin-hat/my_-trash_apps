# MeCabサンプルアプリ
青空文庫の作品のXHTML版の形態解析をします。
![MeCabApp](https://raw.githubusercontent.com/urchin-hat/my_trash_apps/master/images/MeCabApp.gif)

## 環境
Python 3.6.5
Flask          1.0.2
mecab-python3  0.7

### 構築手順

アプリのルートで以下のコマンドを実行
```shell
$ virtualenv env && source env/bin/activate
```

対象パッケージの導入
```shell
$ pip install -r requirements.txt
```

アプリケーションの起動
```shell
$ python app.py
```

`http://127.0.0.1:8000/`に接続すると表示されます。
