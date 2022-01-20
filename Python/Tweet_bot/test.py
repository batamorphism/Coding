import twitter
import requests_html
import datetime


class Tweet:
    def __init__(self):
        auth = twitter.OAuth(
            consumer_key="",
            consumer_secret="",
            token="",
            token_secret=""
        )

        tw = twitter.Twitter(auth=auth)

        # ツイートのみ
        status = "Hello,World"  # 投稿するツイート
        tw.statuses.update(status=status)  # Twitterに投稿


class Nikkei:
    """
    日経新聞電子版から、タイトルに保険が入ったのニュースを取得する
    """
    def __init__(self):
        self.htmlgetter = HTMLGetter()
        self.history = set()

    def get_news(self):
        # 保険がタイトルにあるニュースだけを抽出する
        today = datetime.datetime.today().date()
        yesterday = today - datetime.timedelta(days=1)
        url = 'https://www.nikkei.com/search?keyword=from%3A' + str(yesterday.year) + '%2F' + str(yesterday.month).zfill(2) + '%2F' + str(yesterday.day).zfill(2) + '++to%3A' + str(today.year) + '%2F' + str(today.month).zfill(2) + '%2F' + str(today.day).zfill(2) + '+%E4%BF%9D%E9%99%BA&volume=9999'
        print(url)
        id = '.nui-card__title'
        for title, link in self.htmlgetter.get_links(url, id):
            if '保険' not in title:
                continue
            if title in self.history:
                continue
            self.history.add(title)
            yield title, link


class HTMLGetter:
    def __init__(self):
        pass

    def get_links(self, url, id):
        """
        url: リンク先のURL
        id: CSSセレクタ
        https://www.w3schools.com/cssref/css_selectors.asp
        class = は、.class
        #id は #id
        """
        session = requests_html.HTMLSession()
        r = session.get(url)
        finder = r.html.find(id)
        for find in finder:
            text = find.text
            for link in find.absolute_links:
                yield text, link


get_news = Nikkei()
for title, news in get_news.get_news():
    print(title, news)
