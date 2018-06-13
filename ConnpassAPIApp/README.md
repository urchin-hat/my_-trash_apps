# Compassサンプルアプリ
Connpass apiを利用した簡単なWEBアプリです。

![ConnpassApp](https://github.com/urchin-hat/my_trash_apps/blob/master/images/ConnpassApp.gif)

## 環境
|||
|:---:|:---:|
|Python|3.6.5|
|Flask|1.0.2|

### 構築手順

アプリフォルダのルートで以下のコマンドを実行
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
