import time
import pyautogui
import pyperclip
import re
from urllib.parse import urlparse, parse_qs
import random

# ブラウザのウィンドウをアクティブにする
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

# タブを切り替えながら、各タブのURLを取得する
tab_urls = set()
bef_url = ""
cnt = 0
while True:
    # 現在のタブのURLを取得する
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'c')
    tab_url = pyperclip.paste()
    print(tab_url)

    if tab_url in tab_urls and bef_url != tab_url:
        cnt += 1
    else:
        cnt = 0
    if cnt >= 5:
        break

    tab_urls.add(tab_url)
    bef_url = tab_url

    # 次のタブに移動する
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.1)

# 結果を表示する
word_list = set()
for url in tab_urls:
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    english_word = query_dict.get("q", [""])[0]
    cleaned_english_word = re.sub(r'[^a-zA-Z\s]', '', english_word)
    word_list.add(cleaned_english_word)

word_list = list(word_list)

# シャッフルする
word_list = random.sample(word_list, len(word_list))

# 7単語毎に出力する
for i in range(0, len(word_list), 7):
    print(*word_list[i:i+7])

