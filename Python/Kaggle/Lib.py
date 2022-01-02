import pandas as pd
import numpy as np
import os
from collections import Counter


class FeatureEng:
    """
    特徴量エンジニアリングクラス
    dfの欠損値の補完、数値への変換等を行う
    """
    def __init__(self, df: pd.DataFrame = None):
        self._df = df
        self._Zipper_of: dict = None

    def get_df(self) -> pd.DataFrame:
        """変換後のDataFrameを返す
        """
        return self._df

    def save_bin(self, path=None, name=None):
        """現在の状況をバイナリデータとして保存する

        Args:
            path ([string]): 保存先のフォルダ
            path ([string]): 保存先のファイル名
        """
        if path == None:
            print('保存先のファイル名を入力してください')
            path = input()
        if name == None:
            # pathがファイル名も含んでいると判断する
            list_ = list(path.split('.'))
            not_have_period = len(list_) <= 1
            not_pickle = not(list_[-1] == 'pickle')
            if not_have_period or not_pickle:
                # 拡張子すらない場合
                # 拡張子はあるが、pickle出ない場合
                # pathはフォルダのみをさしていると判定する
                print('保存するファイル名を入力してください')
                name = input()
            else:
                name = list_[-1]
            if len(name) <= len('.pkl') or name[-len('.pkl')] != '.pkl':
                name += '.pkl'
        if path[-1] != '\\':
            path += '\\'
        if not os.path.isdir(path):
            # create folder
            print('create folder')
            os.mkdir(path)
        self._df.to_pickle(path + name)

    def load_bin(self, path=None, name=None):
        """前の状況をバイナリデータから読み込む

        Args:
            path ([string]): 保存先のフォルダ
            path ([string]): 保存先のファイル名
        """
        if path == None:
            print('読み込むファイル名を入力してください')
            path = input()
        if name == None:
            # pathがファイル名も含んでいると判断する
            list_ = list(path.split('.'))
            not_have_period = len(list_) <= 1
            not_pickle = not(list_[-1] == 'pickle')
            if not_have_period or not_pickle:
                # 拡張子すらない場合
                # 拡張子はあるが、pickle出ない場合
                # pathはフォルダのみをさしていると判定する
                print('読み込むファイル名を入力してください')
                name = input()
            else:
                name = list_[-1]
            if len(name) <= len('.pkl') or name[-len('.pkl')] != '.pkl':
                name += '.pkl'
        if path[-1] != '\\':
            path += '\\'
        if not os.path.isdir(path):
            raise path + 'is not found'
        self._df = pd.read_pickle(path + name)

    def get_Zipper_of(self):
        """変換後のデータと変換前データの対応がわかる辞書を取得する
        Zipper_of = get_Zipper_of()
        bef_value = Zipper_of[col_name][aft_value]

        Returns:
            dict: 変換後データと変換前データの対応を与える辞書
        """
        return self._Zipper_of

    def convert_int(self):
        """非数値の統計量を、出現頻度順に整数に変換する

        Args:
            df (pd.DataFrame): 変換対象のデータ
        """
        df = self._df
        numeric_set = [np.int64, np.float64]  # なんでかsetにするとうまくいかない
        Zipper_of = {}
        col_label_list = []
        for col_label, col_series in df.iteritems():
            col_type = col_series.dtype
            if col_type in numeric_set:
                # 数値型は処理しない
                continue
            col_label_list.append(col_label)
            Zipper = self._get_Zipper(col_series)
            Zipper_of[col_label] = Zipper
        # 座標圧縮して得られた辞書を、各列に適用し
        # dfの数値以外もデータを整数に変換する
        for col_label in col_label_list:
            df[col_label] = df[col_label].apply(lambda x: Zipper_of[col_label][x])
        self._Zipper_of = Zipper_of

    def _get_Zipper(self, series: pd.Series):
        # 出現頻度淳に座標圧縮
        series.dropna()  # TODO 欠損値の取り扱いは要確認。多分今はNaNのままにできてるはず・・・
        cnt = Counter(series)
        sorted_series = sorted(list(set(series)), key=lambda x: cnt[x], reverse=True)
        Zipper = {a: i for i, a in enumerate(sorted_series)}
        return Zipper


def main():
    path_train = "C:\\Users\\batam\\Documents\\Kaggle\\Titanic\\train.csv"
    path_test = "C:\\Users\\batam\\Documents\\Kaggle\\Titanic\\train.csv"
    path_gs = "C:\\Users\\batam\\Documents\\Kaggle\\Titanic\\train.csv"
    save_path = "C:\\Users\\batam\\Documents\\Kaggle\\Titanic"
    train = pd.read_csv(path_train)
    test = pd.read_csv(path_test)
    gender_submission = pd.read_csv(path_gs)
    # print(train)

    # 特徴エンジニアリング
    FE = FeatureEng(train)
    FE.convert_int()
    FE.save_bin(save_path, 'hoge.pkl')
    train = FE.get_df()
    print(train)


main()
