# Translate Shell (旧: Google Translate CLI)をインストールしてね
import PySimpleGUI as sg
import requests_html
from googletrans import Translator
import random
import time
import datetime
from threading import Thread


class Trans:
    def __init__(self):
        self.tr = Translator(service_urls=['translate.googleapis.com'])
        self.sleeptime = datetime.timedelta(seconds=15)
        self.bef_time = datetime.datetime.now()

    def trans(self, ptext):
        while datetime.datetime.now() - self.bef_time <= self.sleeptime:
            time.sleep(1)

        print('test')
        while True:
            try:
                text = self.translator.translate(ptext, dest='en', src='ja')
                break
            except Exception as e:
                self.translator = Translator(service_urls=['translate.googleapis.com'])
                print('err')
        self.bef_time = datetime.datetime.now()
        return text.text


def get_nobel(base_url, cnt):
    """
    指定したurlの、cnt番目の小説本文を取得する
    取得した小説本文は、改行で区切ったリストとして返す
    """
    # base_url = 'https://ncode.syosetu.com/n6475db/'
    if base_url[-1] != '/':
        base_url += '/'
    # cnt = 532
    url = base_url + str(cnt) + '/'
    session = requests_html.HTMLSession()
    r = session.get(url)
    # texts = r.html.full_text
    id = 'novel_honbun'
    nobel = r.html.find('#' + id, first=True)
    if nobel is None:
        return None
    return nobel.text.split('\n')


def randTranslator(ptext_list, rate):
    # text_listのランダムな要素を英訳したものを返す
    # 翻訳する割合はrate
    text_list = ptext_list[:]  # イミュータブルのリストは浅いコピー
    tr = Trans()

    for i, text in enumerate(text_list):
        if len(text) >= 3 and random.random() <= rate:
            trans_text = tr.trans(text)
            text_list[i] = trans_text

    return text_list


def test():
    # text_list = ['こんにちは']
    base_url = 'https://ncode.syosetu.com/n6475db/'
    cnt = 999
    text_list = get_nobel(base_url, cnt)
    if text_list:
        trans_text_list = randTranslator(text_list, 0.1)
    print('\n'.join(trans_text_list))


def test_slow():
    time.sleep(10)
    return 1


def main():
    # sg.theme('Default')   # デザインテーマの設定

    # ウィンドウに配置するコンポーネント
    layout = [[sg.Text('対象の小説url'), sg.InputText('https://ncode.syosetu.com/n6475db/', size=50, key='base_url')],
            [sg.Text('対象の小説和数'), sg.InputText(500, size=5, key='cnt')],
            [sg.Multiline(size=(80, 40), key='text')],
            [sg.Button('Run', bind_return_key=True), sg.Button('Next')]]

    # ウィンドウの生成
    window = sg.Window('Narou', layout)

    def run():
        # get input
        base_url = values['base_url']
        cnt = values['cnt']

        # set output
        values['text'] = 'hogehogehogehogehoge'

        window.Element('text').update(values['text'])
        window.read()

    # イベントループ
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Run':
            run()
            Thread(target=test_slow, args=(), daemon=True).start()

    window.close()


main()
