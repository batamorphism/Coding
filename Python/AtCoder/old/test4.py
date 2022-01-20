from googletrans import Translator
import time

# Translatorクラスのインスタンスを生成
translator = Translator(service_urls=['translate.googleapis.com'])

# 翻訳元の文章
string_ja = "今日も頑張ってPythonを勉強しよう。"

time.sleep(10)
# 文章を英語に翻訳する
while True:
    try:
        trans_en = translator.translate(string_ja, dest='en', src='ja')
        break
    except Exception as e:
        translator = Translator(service_urls=['translate.googleapis.com'])
        time.sleep(10)
        print('err')

print(trans_en.text)
