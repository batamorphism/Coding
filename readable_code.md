# The_Art_of_Readable_Code

## 初めに

The Art of Readable Codeを読んで重要な所をピックアップした。

**これは重要な所**

> これは私の感想、解釈、捕捉

---

### Part0-Chapter 1

#### Code Should Be Easy To Understand

**すなわち、コードは、他の人が理解するのに必要な時間を最小限にするように書くべき**ということ。

読みやすいコードを書く上で、最も重要な原則である。この原則は、以後紹介するあらゆるルールや原則より優先される。

コードの行数を減らすことはよい目標だが、理解するまでの時間を最小限にするために加筆することはさらに良いことである。

悪い例

```C++
assert((!(bucket = FindBucket(key))) || !bucket->IsOccupied());
```

> 括弧が多すぎるしor演算子||やnot演算子!が使われていたりしてどう処理されるかわからない

これは二行に分けたほうが読みやすい

```C++
bucket = FindBucket(key);
if (bucket != NULL) assert(!bucket->IsOccupied());
```

> if文をかませたりbucketを先に計算することで、バケツが存在する場合にのみバケツの中身を確認し、中身が既に埋まってしまっていないかを確認するロジックであることがわかる。

また、コメントは行数を増やすにもかかわらず、あったほうが内容を早く理解できる。

```C++
// Fast version of "hash = (65599*hash)+c"
hash = (hash<<6)+(hash<<16)-hash+c;
```

> hash<<16でhash*2^16を意味するのだが、コメントがなければhashを高速に65599倍したい処理だと理解するのに時間がかかる。2^6+2^16-1=65599を手で計算しなければいけない。

---

## Part1-Surface-Level Improvements

まずは、良い名前を選ぶ、良いコメントを書く、コードをきれいにフォーマットする等の表面的な改善から始める。これは簡単に行うことができ、今すぐ実践できる。

---

### Part1-Chapter2

#### Packing Information into Names

**すなわち、名前は小さなコメントのように扱いたい**ということ。

tmpのようなあいまいな名前を使いがちだが避けるべきである。具体的な6つの手法を紹介する。

* Choose Specific Words
* Avoiding generic names (or knowing when to use them)
* Using concrete names instead of abstract names
* Attaching extra information to a name, by using a suffix or prefix
* Deciding how long a name should be
* Using name formatting to pack extra information

---

#### Choose Specific Words

具体的な言葉を選ぶこと。

悪い例

```Python
def GetPage(url):
    ...
```

このgetはあまり意味を持っていない。Pageの何を、どうgetするのか分かるようにすべきである。例えば、FetchPageやDownloadPageが考えられる。

良い例

```Python
def DownloadPage(url):
    ...
```

悪い例-このsizeはTreeの高さを返すのか、Nodeの数を返すのか不明である。

```C++
class BinaryTree{
    int Size();
}
```

良い例

```C++
class BinaryTree{
    int Height();
}
```

> BinaryTree(二分木)は、データ構造の一つであり、木構造によりデータを管理するものである。最適化のために、部分木のSizeを持たせるのが一般的だが、要素数や木の高さなど様々なものがSizeとして使われるため、Sizeでは中身が何かわからない。

悪い例-stopは停止させる場合にはよいのだが、元に戻せないような重い処理の場合はKillとしたり、Resumeできる場合はPauseとすべきかもしれない

悪い例

```C++
class Thread{
    void Stop();
}
```

良い例

```C++
class Thread{
    void Kill();
}
```

---

#### Finding More "Colorful" Words

恐れずに**類義語辞典を使ったり、同僚に聞いていろいろなカラフルな候補を探し、はっきりとした・正確な単語を選ぶ**こと。

例えば、次のようなカラフルな類義語がある。

|Word|Alternatives|
|-|-|
|send|deliver, dispatch, announce, distribute, route|
|find|search, extract, locate, recover|
|start|launch, create, begin, open|
|make|create, set up, build, generate, compose, add, new|

ただし、気分が乗りすぎて変な単語を選ばないように注意。文字列を分割するのにexplodeを使うのは、splitを使ったほうが明確だろう。

---

#### Avoid Generic Names Like tmp and retval

