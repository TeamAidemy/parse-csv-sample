import pandas as pd


def csv_to_df(path: str):
    """
    CSVデータを読み込んでpandasのDataFrameに変換する
    """

    # CSVは3行のヘッダがある
    # 英語カラム名: CSVの中で一意、操作やクエリの実行は英語カラム名を指定
    # 日本語カラム名: CSVの中で一意ではないため操作やクエリには使わない、表示などに使用する
    # 型: text, number, dateなどそれぞれの値をどういった型として扱うべきかを示す

    # CSVの型表記とpandasのdtype表記の対応
    to_dtype = {
        "number": "float",
        "boolean": "bool",
        "text": "object",
        "date": "object",
        "datetime": "object",
    }
    type_df = (pd.read_csv(path, header=0, na_filter=True))[1:2]
    dtypes = {k: to_dtype[type_df[k][1]] for k in type_df.columns}

    # データフレームのヘッダとして扱うのは0=1行目、以降2行(日本語カラム名、型)を読み飛ばし
    data = pd.read_csv(path, header=0, na_filter=True).drop([0, 1])
    return data.astype(dtypes)


def key_to_display_name(paths: list[str]):
    """
    DataFrameのヘッダと表示用の日本語表記の対応を辞書型で返す
    """
    res = dict()
    for p in paths:
        df = pd.read_csv(p, header=0, na_filter=True)[0:1]
        for k in df.columns:
            res[k] = df[k][0]
    return res
