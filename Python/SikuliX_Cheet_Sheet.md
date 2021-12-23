# SikuliX_Cheet_Sheet

## 公式ドキュメント

* https://sikulix-2014.readthedocs.io/en/latest/index.html
* https://sikulix-2014.readthedocs.io/en/latest/toc.html
* 困ったらここを見る事

## 画像をクリックする

### ある画像を一回クリックする

* 最も基本

```Python
click('画像名')
```

* 画像から一定座標動かしたところをクリックすることも可能
* SikuliX上で画像をクリックし、ターゲットオフセットを選択する

```Python
# 画像から右に10, 下に10ピクセル動かしたところをクリック
click(Pattern('画像名').targetOffset(10,10))
```

### 画像が消えるまで画像をクリックし続ける

* clickはたまに失敗することを考慮したロジック
* OKボタンの押下、チェックボックスをすべて外す、ウィンドウをすべて閉じる等応用範囲が広い

```Python
def main():
    remove_img_click('画像名')


def remove_img_click(img):
    while exists(img):
        click(img)
        sleep(1)  # 1回クリックするごとに1秒休ませて、フリーズ回避


main()
```

* 指定回数動かしたら止めたい場合はこっち

```Python
def main():
    remove_img_click('画像名', 10)


def remove_img_click(img, max_cnt=float('inf')):
    cnt = -1
    while exists(img):
        cnt += 1
        if cnt > max_cnt:
            return
        click(img)
        sleep(1)  # 1回クリックするごとに1秒休ませて、フリーズ回避


main()
```

### 画像が存在する限りクリックし続ける

* 画像Aがある(あった)場所を、画像Bが消えるまでクリックし続ける
* まれに使う機会がある

```Python
def main():
    mat = find('クリックする対象')
    x, y = mat.getX(), mat.getY()
    click_while_exists(x, y, '消えるまでクリックする対象の画像')


def click_while_exists(x, y, img):
    while exists(img):
        click(Location(x, y))
        sleep(1)


main()
```

### ある画像から、一定間隔ずらした場所を連続クリックする

* RPAでは極力、画像認識の回数を減らしたい
* リスト上に入力欄が列挙されている場合など、等間隔にクリックする箇所が並んでいる場合は一定間隔ずつずらしてクリックする
* 出現頻度は低い

```Python
dx, dy = 0, 10
cnt = 10
mat = find('ある画像')
x, y = mat.getX(), mat.getY()
for i in range(cnt):
    cur_x, cur_y = x + dx*i, y + dy*i
    click(Location(cur_x, cur_y))
```

## 画像が存在するか確認する

### 画像があるときとないときで分岐

```Python
if exists('画像名'):
    myfnc1()  # 別途作成した処理1
else:
    myfnc2()
```

### 画像が出てくるまで待つ

```Python
wait('画像名', 10)  # 画像が表示されるまで10秒待つ。
```

### 画像を見つける

* 画像を見つけて、Matchとして返す
* 応用の幅が広いが、そんなに使わない

```Python
mat = find('画像名')
print mat.getX()  # マッチした画像のx座標を出力する
```

```Python
mat_gen = findAll('画像名')
for mat in mat_gen:
    print mat.getX()  # マッチした全ての画像のx座標を出力する
```

### マッチした画像を上から順番にクリックする

* findAllの応用例

```Python
mat_list = list(findAll('画像名'))
mat_list.sort(key=lambda mat: mat.getY())
for mat in mat_list:
    x, y = mat.getX(), mat.getY()
    click(Location(x, y))
```

## 出力する

### キーボードから入力する

1文字～数文字の入力に適している

```Python
type('a')  # キーボード[a]をtype
type(Key.Home)  # キーボード[Home]をtype
type('abc123')  # キーボードa, b, c, 1, 2, 3を順にtype
type('s', Key.CTRL)  # Ctrl+[s]を入力
```

### ペーストする

複数文字をまとめて張り付ける

```Python
text = 'Hello World'
paste(text)
```

### メッセージボックスを作る

```Python
text = 'Hello World'
pop(text)
```

### 標準出力

* デバッグするときに使う

```Python
text = 'Hello World'
print text
```

## 入力する

### はいかいいえか

* はい、いいえからなる入力ボックスを作る

```Python
flag = popAsc(u'処理を実行しますか')
if not flag:
    return
```

### ファイルの場所の入力

```Python
csvPath = popFile(u'対象のcsvデータを指定してください')
```

### 任意の文字列の入力

```Python
text = input(u'出力したい文字列を入力してください')
print text
```

### csvを読み込む

* Pythonの標準のcsv読み込み機能と同一

```Python
import csv


csvPath = popFile(u'対象のcsvデータを指定してください')
with open(csvPath, 'rb') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    header = next(reader)
    for row_dat in reader:  # 1行ずつ処理していく
        print row_dat[0]  # 1列目のデータ
        print row_dat[1]  # 2列目のデータ
        print row_dat[2]  # 3列目のデータ
```

## 設計する-基本

* 今まで挙げた機能を組み合わせて、プログラムの設計をしていく

### 変数を使う

* 同じ画像がたくさん出てくる場合は、変数にしてまとめる
* これだと、画像Aがちょっと変わると5箇所メンテが必要となる

```Python
click('画像A')
click('画像A')
click('画像A')
click('画像A')
click('画像A')
```

* 変数を使うことで、コードは1行長くなるがメンテナンス性は各段に向上する

```Python
img_A = '画像A'
click(img_A)
click(img_A)
click(img_A)
click(img_A)
click(img_A)
```

* ただし、変数を設定している個所が遠いと、見通しが悪くなるので注意する
* 設定する系統の変数は最初に宣言するのが通常のPythonでは鉄則だが
* SikuliXの、画面上に画像を表示させる仕様上、変数の宣言をあえて遅らせるのも手である
* コーディングスタイルは開発環境によっても臨機応変に変える必要がある

```Python
# 悪い例: 普通のPythonならそんなに悪くないけど
img_A = '画像A'
# ～処理～
# (中略　100行とか、1画面に収まらない量のプログラム)
click(img_A)  # 記事の都合上省略しているが、
click(img_A)  # img_A = '画像A'と、click(img_A)の間に
click(img_A)  # 間が空きすぎて1画面に収まらない場合
click(img_A)  # ここだけ見ても何してるのかわからず望ましくない
click(img_A)
```

### ループを使う

* 同じ処理を繰り返しているところは、for文、while文を使い重複を減らす

```Python
click('画像A')
click('画像A')
click('画像A')
click('画像A')
click('画像A')
```

* これは次のようにする

```Python
for _ in range(5):
    click('画像A')
```

### 関数を使う

* 同じ処理をしている個所はまとめて、1つの関数にする

```Python
click('画像A')
wait('画像B', 10)
myfnc1()
click('画像A')
wait('画像B', 10)
myfnc2()
click('画像A')  # この処理が重複しているので良くない
wait('画像B', 10)
myfnc3()
```

* 次のように、自作関数wait_image_Bを作り、重複を減らす

```Python
wait_image_B()
myfnc1()
wait_image_B()
myfnc2()
wait_image_B()
myfnc3()

def wait_image_B():
    click('画像A')
    wait('画像B', 10)
```

* さらにfor文を使い縮めることも可能
  * かえってメンテナンス性が落ちるケースもあるので注意

```Python
job_list = [myfnc1, myfnc2, myfnc3]
for job in job_list:
    wait_image_B()
    job()

def wait_image_B():
    click('画像A')
    wait('画像B', 10)
```

### 変数をまとめる

* 構造体を用いて、たくさんの変数をまとめて管理する
* Pythonには構造体がないので、クラスかnamedtupleを用いる
* 変数が多くなりすぎると可読性が著しく下がるので、このようにまとめて管理するとよい

```Python
# 軽量クラスによる方法
class Config():
    def __init__(self):
        self.val1 = 0
        self.val2 = 0
        self.val3 = 0
        self.val4 = 0
        self.val5 = 0

cfg = Config()
cfg.val1 = 10  # cfg.val1として10を編集
cfg.val2 = 20  # classの場合後から変更可能
print cfg.val1  # 10を編集する
```

```Python
# namedtupleによる方法
from collections import namedtuple
Config = namedtuple('Config', ['val1', 'val2', 'val3', 'val4', 'val5'])

cfg = Config(val1=10, val2=20, val3=30, val4=40, val5=50)
# cfg = Config(10, 20, 30, 40, 50)  でも同じ
print cfg.val1  # 10が出力される
# namedtupleは値の変更が不可なので安全性が高い
# cfg.val1 = 20 これはエラー
```

## 設計する-応用

### 画像の重複をなくす

* 画像認識は、ちょっとでも画像が変わると上手く動作しなくなる
* 例えば対象アプリのアップデートで画像がさし替わってしまうと、メンテナンスが発生する
* そのメンテナンス量を極力抑えるために、SikuliXで使っている画像の数を極力減らす事が望ましい
* 同じ画像が2箇所出てきた場合、設計する-基本で挙げた内容を使って、画像の数を減らしていくこと

```Python
def myfnc1():
    # ～何かの処理～
    click('ホーム画面')  # ホーム画面をクリックしてホームに戻る
    # ～何かの処理～

def myfnc2():
    # ～何かの処理～
    click('ホーム画面')  # <-myfnc1と重複
    # ～何かの処理～
```

* プログラム全体を通してみて、同じ画像が2箇所出てきた場合は、次のようにまとめることを検討
* 同じ画像を使っている処理は、大抵、関数として切り出すに足る共通処理をしていることが多いので
* 関数として切り出すとプログラム全体として見通しが良くなる傾向にある

```Python
def myfnc1():
    # ～何かの処理～
    back_home()
    # ～何かの処理～

def myfnc2():
    # ～何かの処理～
    back_home()
    # ～何かの処理～

def back_home():
    # ホーム画面をクリックするという動作を
    # back homeという名前を付けて
    # ホーム画面に戻るという操作に抽象化できる
    # 加えて、使用する画像も減らせる
    click('ホーム画面')
```

* 悪いアイデア
* 辞書を使って処理をまとめるのはPythonでは典型だが
* SikuliXで画像をまとめるのは、画面上、画像を表示してくれなくなるので望ましくない
* それ以外の方向で画像の重複を避けるように工夫しよう

```Python
img_of = {'home': 'ホーム画面'}

def myfnc1():
    # 悪い例
    # エラーが出たときに、毎回img_ofの定義を見ないといけなくなる
    click(img_of['home'])  # 処理も抽象化されておらず、何してるかわからない

def myfnc2():
    click(img_of['home'])
```

### 画像処理を使わない

* SikuliXは画像処理を得意とするアプリだが、極力画像処理をする個所は減らしたほうがいい
* 悪い例

```Python
click('画像1')
type('a')
click('画像2')
type('b')
click('画像3')
type('c')
click('画像4')
type('d')
```

* 画像1をクリックした段階で、Tabキーを押すと次の入力欄に行ける場合、次のようにする

```Python
click('画像1')
char_list = ['a', 'b', 'c', 'd']
for char in char_list:
    type(char)
    type(Key.TAB)  # 次の入力欄に
```

* 画像2～4の入力欄が等間隔で並んでいる場合は、次のようにする

```Python
mat = find('画像1')
x, y = mat.getX(), mat.getY()
dx, dy = 10, 0  # 右に10ピクセルずつ動かしながらクリック
for i in range(4):
    click(Location(x + dx*i, y + dy*i))
```

### 処理を順番に繰り返す

* myfnc1～3を順番に無限に繰り返す

```Python
while True:
    myfnc1()
    myfnc2()
    myfnc3()
```

* myfnc1～3を10回繰り返す

```Python
for _ in range(10):
    myfnc1()
    myfnc2()
    myfnc3()
```

### csvから読んだデータに応じて処理を繰り返す

* csvから読んだデータを元に処理を順番に行う

```Python
import csv
from collections import namedtuple
Condition = namedtuple('Condition', ['val1', 'val2', 'val3'])

def main():
    for cond in gen_csv():  # csvデータをcondに編集して繰り返す
        myfnc1(cond)

def gen_csv():
    # csvの内容を1行ずつ読んで、Conditionに渡すジェネレータ
    csvPath = popFile(u'対象のcsvデータを指定してください')
    with open(csvPath, 'rb') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        header = next(reader)
        for row_dat in reader:  # 1行ずつ処理していく
            val1 = row_dat[0]  # 1列目のデータ
            val2 = row_dat[1]  # 2列目のデータ
            val3 = row_dat[2]  # 3列目のデータ
            # for文を回しても実装可能だが
            # 実務上は、各列ごとに型の変換やデータの加工が入る事が大半であり、
            # 1列ずつ列挙していくことになろう
            cond = Condition(val1=val1, val2=val2, val3=val3)
            yield cond  # yieldで、condを一回返して、処理を一時停止


def myfnc1(cond):
    # condの内容に応じた処理を実行
    print cond.val1
    print cond.val2
    print cond.val3


main()
```

### 指定時間間隔で処理を実行

* 処理を開始->次に実行開始する時間を登録->その時間まで待機
* 複数の処理がある場合は、開始時刻が早いものから順に行う

```Python
import heapq
import datetime


def main():
    # myfnc1は10分毎、myfnc2は20分事・・・に行う
    job_list = [(myfnc1, datetime.timedelta(minutes=10))
              , (myfnc2, datetime.timedelta(minutes=20))
              , (myfnc3, datetime.timedelta(minutes=30))]

    # 優先度付きキューの初期化
    que = []
    now_ = datetime.datetime.now()
    for job in job_list:
        que.append((now_, job))
    heapq.heapify(que)

    while que:
        sleep(1)  # フリーズ回避
        now_ = datetime.datetime.now()
        if que[0][0] < now_:
            # 最も開始時刻が早いものが、現在時刻より小さい場合は処理開始
            _, job = heapq.heappop(que)
            fnc, delta = job
            heapq.heappush(que, (now_+delta, job))
            fnc()

def myfnc1():
    print '1'

def myfnc2():
    print '2'

def myfnc3():
    print '3'

main()
```


## エラーを読む/作る

### エラーを読む

* RPAでは、画像が存在する／しないによって頻繁にエラーが発生する
* したがって、エラーを読む能力も重要である
* Pythonでは、Traceback機能があるため、エラーは非常に読みやすい

```Python
def main():
    myfnc1()

def myfnc1():
    myfnc2()

def myfnc2():
    print 1/0


main()
```

* このコードは、main->myfnc1->myfnc2と呼ばれ、myfnc2で初めてエラーとなる
* エラー発生時には、myfnc2でエラーが発生しました、という情報だけでなく
* mainのmyfnc1が読んだmyfnc2でエラーが発生したことが分かるようになっている

> [error] --- Traceback --- error source first  
> line: module ( function ) statement  
> 8: main (  myfnc2 )     print 1/0  
> 5: main (  myfnc1 )     myfnc2()  
> 2: main (  main )     myfnc1()  
> 11: main (  <module> )     main()  
> [error] --- Traceback --- end --------------  

* したがって、Tracebackを読めば、どのタイミングでエラーが発生したか特定できるようになっている

### エラーを書く

* 自動化対象のアプリが警告を出しているとき等、自作のエラーを作りたいときがある
* 次のようにする

```Python
# ～処理～
if exists('Error_Image'):
    raise 'Error Name'
```

* raise句を使うことで、自作のエラー処理を新たに作ることができる

### エラーで落とすか、処理を続行させるか

* エラーが発生した時に、安全に停止させるのか、そのまま処理を続行させるのか
* 前者を「fail safe」、後者を「fail soft」という
* fail safeのほうが安全だが、全てをfail safeにすると頻繁にエラーが発生し、機能しなくなる可能性がある
* 「画像を1回クリックして、あるべき画像が表示されてなかったら止める」はfail safeといえる
* 「画像が消えるまで画像をクリックし続ける」はfail softといえる
* 画像をクリックするのセクションで挙げたロジックと、前述のraiseを組み合わせて、fail safeとfail softのバランスを取るのがいいRPAを作るコツとなる

## 画像を差し替える

* 対象アプリのアップデートで画像がさし替わった時は、次のように対応する

1. SikuliXを動かす(この場合スローモーションで実行 機能も役立つ)
2. 画像がないと、エラーになったところで止める(というより止まる)
3. エラーとなった個所について、その画像の名前を調べる(その行をコピーし、メモ帳に貼ると調べられる)
4. その画像を差し替える
5. 3で特定した名前が、プログラム上のほかの個所にないかを調べ(Ctrl+[f] -> Ctrl+[g])、同様に差し替えていく
6. 上記1～5を繰り返す

1, 2の回数を減らすためにも、使用する画像の枚数は少ないほうが良い
4の回数を減らすためにも、同じ画像を使用している個所は少ないほうが良い

## その他-Pythonの機能

### コマンドプロンプトを実行

* コマンドプロンプト経由で、アプリの起動などを直接行うことができる

```Python
import subprocess

try:
    # コマンドプロンプト上で、[echo %computername%]を実行し、処理の完了を待つ
    print subprocess.check_output('echo %computername%', shell=True).decode()
    # コマンドプロンプト上で、[notepad]を実行し、処理の完了を待たずに次に進む
    print subprocess.Popen(['notepad'])

except:
    print 'Fail'
```

### 文字列操作

```Python
text = 'abcdefghijklmn'
print text[3]  # d - 4文字目を取得
print text[:3]  # abc - 先頭3文字を取得
print text[3:]   # defghijklmn  - 4文字目以降を取得
print text[-3:]  #lmn  # 後ろから3文字を取得
print text[:-3]  # abcdefghijk  # 後ろから3文字までを取得
print text[::-1]  # nmlkjihgfedcba  # 反転
```

### キー一覧

* https://sikulix-2014.readthedocs.io/en/latest/keys.html

```Python
ENTER, TAB, ESC, BACKSPACE, DELETE, INSERT
SPACE
F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15
HOME, END, LEFT, RIGHT, DOWN, UP, PAGE_DOWN, PAGE_UP
PRINTSCREEN, PAUSE, CAPS_LOCK, SCROLL_LOCK, NUM_LOCK
NUM0, NUM1, NUM2, NUM3, NUM4, NUM5, NUM6, NUM7, NUM8, NUM9
SEPARATOR, ADD, MINUS, MULTIPLY, DIVIDE
ALT, CMD, CTRL, META, SHIFT, WIN, ALTGR
```
