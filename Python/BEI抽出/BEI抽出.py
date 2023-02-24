import re
import requests
import ast
import numpy as np
import pandas as pd
import datetime

def main():
    url = "https://www.bb.jbts.co.jp/ja/historical/marketdata05.html"
    response = requests.get(url)
    html = response.content.decode("utf-8")

    # JavaScriptのコードを含むscriptタグを正規表現で検索
    pattern = r"<script>\n\s*initChart\((.*?)\);\n\s*</script>"
    match = re.search(pattern, html, re.DOTALL)

    if match:
        # 検索に成功した場合、括弧内のデータを取得
        text = match.group(1)
        df = make_df(text)
        df.to_csv(datetime.datetime.today().strftime("%Y-%m-%d")+"BEI.csv", encoding="utf-8-sig")
    else:
        print("データが見つかりませんでした。")

def make_df(text):
    text_list = split_csv_string(text)  # 巨大な文字列を、属性ごとに文字列のlistにする

    # 18番目の要素が、日付が羅列された文字列なので、listに変換する
    # date = ["2019/01/02", "2019/01/03", ...]
    date = text_list[18]
    date = split_string_to_list(date)
    # headerも同様
    header = text_list[20]
    header = split_string_to_list(header)
    # BEIなどの値が入っている個所については、[がネストしているので別処理
    # values_list = [[1, 2, 3, ...], [4, 5, 6, ...], ...]
    values_list = text_list[22]
    values_list = ast.literal_eval(values_list)
    values_list = np.array(values_list)
    # DataFrameにするためには、行ごとのレコードにする必要があるため、転置する。
    records = values_list.T

    df = pd.DataFrame(records, columns=header, index = date)
    df.index.name = "Date"
    return df

def split_string_to_list(string):
    string = string.replace("\\", "")
    ret = ast.literal_eval(string)
    return ret

def split_csv_string(csv_string):
    # 元データが"囲みで与えられているため、"で囲まれている順にデータを取得する
    # "で囲まれているエリアをlistにpushする。
    # ただし、\"の場合は"を無視する。
    res_list = []
    stack = []
    for i, c_i in enumerate(csv_string):
        if stack and c_i == "\"" and csv_string[i-1] != "\\":
            res_list.append("".join(stack))
            stack = []
        else:
            stack.append(c_i)
    return res_list


main()
