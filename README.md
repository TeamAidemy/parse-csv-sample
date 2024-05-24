# Lab Bank CSVエクスポートデータ活用サンプル

本リポジトリは[Lab Bank](https://labbank.jp/)で出力されたCSVエクスポートデータを活用するための、サンプルコードを格納しております。

```
.
├── README.md ... 本ドキュメント
├── export ... サンプルコード向けのダミーのエクスポートデータ
├── libs ... pandasを簡単に扱うための関数
└── sample.ipynb ... サンプルコード
```

## 使い方

### 動作環境

- [Python@3.11](https://www.python.org/downloads/)


```sh
# virtualenvを有効化
$ python3 -m venv sample
$ source sample/bin/activate

# 必要なライブラリのインストール
$ pip install -r requirements.txt

# Jupyter Labを起動
$ jupyter lab --NotebookApp.token='' --NotebookApp.password=''
```

[http://localhost:8888/lab](http://localhost:8888/lab)にアクセスし、sample.ipynbを実行してください。
![サンプルコードの開き方](./img/サンプルコードの開き方.png)

```sh
# virtualenvを終了
$ exit
```
