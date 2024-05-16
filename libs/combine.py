import pandas as pd


def merge_columns_df(df: pd.DataFrame, target_keys: list[str], merged_key: str) -> pd.DataFrame:
    """
    target_keysで指定された列を結合し、新しくmerged_keyで指定された列を作成する。
    同じ行の中でNaNではない値が存在する場合はそれを採用する、そのため欠損値がNaN以外の場合は動作しない。
    複数の列でNaN以外が存在する場合は、target_keysのインデックスが小さい値が優先される。
    また関数が実行されると、引数で渡されたdfの元の変数も書き換わる。

    ex.
    --- code ---
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, NaN, 6],
        'c': [NaN, 8, NaN]
    })
    merge_columns_df(df, ['b', 'c'], 'd')
    print(df)

    --- output ---
    0  a  d
    1  1  4
    2  2  8
    3  3  6
    """

    def merge_value(row: pd.Series) -> str:
        return list(filter(lambda v: not pd.isna(v), [row[k] for k in target_keys]))[0]

    df[merged_key] = df.apply(merge_value, axis=1)
    df.drop(target_keys, axis=1, inplace=True)
    return df
