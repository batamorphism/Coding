mytableは次の通り

|c1|c2|c3|
|-|-|-|
|a|1|2|
|b|1|2|
|c|2|3|
|d|3|4|

mytable2は次の通り

|c4|c5|c6|
|-|-|-|
|a|10|20|
|b|20|30|
|e|20|30|

# はじめに
## USE
- 使用するデータベースを指定
```sql
USE mydatabase
GO
```
- 初めに使用するデータベースを指定しないと、他のデータベースを加工してしまう事もある。
- 他室の超重要なデータを吹き飛ばしてしまうこともあるので、超注意。
- 特に、INTO、CREATE、UPDATE、ALTER、DROP、TRUNCATE、DELETE、ROLLBACKなどの、データベースを加工する系統のクエリ実行する際は最大限の注意を払う。必ずUSE句を使用すること。怠れば、確実にデータベースを破壊してしまう。
- 逆に、INTOの含まれないSELECT句については、データベースを参照するのみであり、中身を変更しないので、注意せずともよい。
- SELECT、FROM、UNION ALL、LEFT JOIN、RIGHT JOIN、INNER JOIN、WHERE、ORDER BY、GROUP BYあたりは安全。

## クエリの実行
- SSMS上の実行ボタンを押すとクエリが実行される。
- 実行ボタンの左にある、データベースの名前が、適切に設定されていることを確認。（間違えてもmasterを選ばないこと。）
- なお、オブジェクトエクスプローラーで使用するデータベースを予めクリックしておけば問題ない。

# (テーブル取得・加工）SELECT/INSERT/UPDATE/DELETE
## SELECTはデータの取得を行う。
```sql
SELECT *
FROM mytable
```
実行結果

|c1|c2|c3|
|-|-|-|
|a|1|2|
|b|1|2|
|c|2|3|
|d|3|4|

## 特定のカラムだけを取得することも可能
```sql
SELECT c1,c2
FROM mytable
```
実行結果

|c1|c2|c3|
|-|-|
|a|1|2|
|b|1|2|
|c|2|3|
|d|3|4|

## 特殊な利用法として、SELECT句のみでの実行も可能

```sql
SELECT `world' as 'hello'
```
実行結果

|hello|c2|c3|
|-|
|world|1|2|

# INSERT
## INSERT句はデータの追加を行う
```sql
INSERT
INTO mytable
VALUE (e,4,5)
```
実行結果

|c1|c2|c3|
|-|-|-|
|a|1|2|
|b|1|2|
|c|2|3|
|d|3|4|
|e|4|5|

# UPDATE
## UPDATE句はデータの更新を行う
```sql
UPDATE mytable
SET c3 = 0
WHERE c1 = 'a'
```
実行結果

|c1|c2|c3|
|-|-|-|
|a|1|0|
|b|1|2|
|c|2|3|
|d|3|4|

# DELETE
## DELETE句は特定の行を削除する
```sql
DELETE mytable
WHERE c1 = 'a'
```
実行結果

|c1|c2|c3|
|-|-|-|
|b|1|2|
|c|2|3|
|d|3|4|

# 装飾語(INTO/WHERE/TOP)
## INTO句は特定のテーブルに結果を出力する
```sql
SELECT *
INTO tmp
FROM mytable
```
実行結果
([tmp]テーブルが新たに生成される）

|c1|c2|c3|
|-|-|-|
|a|1|2|
|b|1|2|
|c|2|3|
|d|3|4|

## WHERE句は処理するレコードを条件指定する。
```sql
SELECT *
FROM mytable
WHERE c1 = 'a' or c1 = 'b'
```
実行結果

|c1|c2|c3|
|-|-|-|
|a|1|2|
|b|1|2|

```sql
SELECT *
FROM mytable
WHERE c1 in ('a','b')
```
実行結果

|c1|c2|c3|
|-|-|-|
|a|1|2|
|b|1|2|


## TOP句は上位何行かを取得する（軽いのでデバッグに有用）
```sql
SELECT TOP 1 *
FROM mytable
WHERE c1 = a
```
実行結果

|c1|c2|c3|
|-|-|-|
|a|1|2|


# 集計(ORDER BY/GROUP BY)
## ORDER BYはソートを行う
- ASCを指定すると昇順、DESCを指定すると降順
```sql
SELECT *
FROM mytable
ORDER BY c1 DESC
```
実行結果

|c1|c2|c3|
|-|-|-|
|d|3|4|
|c|2|3|
|b|1|2|
|a|1|2|

## GROUP BYは集計を行う。
- 集計用の関数を使用する。
- 集計用関数の例
  * SUM
  * MAX
  * MIN
  * AVG
  * COUNT
```sql
SELECT c2,SUM(c3) as c3
FROM mytable
GROUP BY c2
```
実行結果

|c2|c3|
|-|-|
|1|4|
|2|3|
|3|4|

# 結合(LEFT JOIN/RIGHT JOIN/INNER JOIN/UNION ALL)
## LEFT JOIN
- 左のテーブルに右のテーブルを横につなげることができる
```sql
SELECT *
    FROM mytable
    LEFT JOIN mytable2
    ON mytable.c1 = mytable.c4
```
実行結果

|c1|c2|c3|c4|c5|c6|
|-|-|-|-|-|-|
|a|1|2|a|10|20|
|b|1|2|b|20|30|
|c|2|3|NULL|NULL|NULL|
|d|3|4|NULL|NULL|NULL|

## RIGHT JOIN
- 右のテーブルに左のテーブルを横につなげることができる。
```sql
SELECT *
    FROM mytable
    RIGHT JOIN mytable2
    ON mytable.c1 = mytable.c4
```
実行結果

|c1|c2|c3|c4|c5|c6|
|-|-|-|-|-|-|
|a|1|2|a|10|20|
|b|1|2|b|20|30|
|NULL|NULL|NULL|e|20|30|

## INNER JOIN
- テーブルの共通部分だけを横につなげることができる
```sql
SELECT *
    FROM mytable
    INNER JOIN mytable2
    ON mytable.c1 = mytable.c4
```
実行結果

|c1|c2|c3|c4|c5|c6|
|-|-|-|-|-|-|
|a|1|2|a|10|20|
|b|1|2|b|20|30|

## UNION ALL
- テーブルを縦につなげることができる。
```sql
SELECT 'world' as hello
UNION ALL
SELECT 'world' as hello
```
実行結果

|hello|
|-|
|world|
|world|

# 副問い合わせ
## FROM句の中にSELECT句を設定できる。
```sql
SELECT tmp.c2,SUM(tmp.c6) as c6
FROM (
    SELECT *
        FROM mytable
        INNER JOIN mytable2
        ON mytable.c1 = mytable.c4
    ) as tmp
GROUP BY tmp.c2
```
実行結果

|c2|c6|
|-|-|
|1|50|

# テーブル制御(CREATE/ALTER/DROP/TRUNCATE)
## CREATE TABLE
- 新たにテーブルを生成する。
## ALTER TABLE
- 既存のテーブルを定義しなおす。
## TRUNCATE TABLE
- テーブルの中身を空にする。
## DROP TABLE
- テーブルそのものを削除する

# その他
初学者にとって重要ではない、必要に応じて参照すればよいものを列挙する。
## 演算子
- 使用可能な論理演算子の例
  - AND/NOT/OR/=/</>/<=/>=/<>
- 使用可能な算術演算子の例
  - +-*/
  - 文字列の結合は||
  - 条件分岐はIIF(条件文,TUREの場合,TRUE以外の場合)
    - SQLは3値理論を適用しているため、条件文の判定結果はTRUE/FALSE/UNKNOWNの3種類となる。
## GO/;
- GOはSQL文を実行させる命令（通常は暗黙の内に処理される）
- ;はSQL文を区切るための文字（複雑なSQL文になると;がないと文法が通らなくなる）
## IS NULL
- [column_name] IS NULLでNULL判定可能。
## DISTINCT
- 重複行を削除
## EXPECT
- 差分を取得
## CASE
- 複雑な条件分岐用
## ROUND
- 四捨五入
## POWER
- べき乗
## SHRINKDATABASE
- データベースの圧縮（容量が軽くなる）
## BULK INSERT
- CSVデータから取り込み
## DECLARE
- 変数の定義(変数は@から始まる)
## CURSOR
- カーソルの定義（一行ずつ処理したい場合に使用）
  - カーソルを使用するとIF文やWHILE文を用いた、構造化プログラミングライクの書き方になる。
  - 処理が遅いので、やむを得ない場合以外は使用しない。
## TRY-CATCH
- エラー発生時の条件分岐
## ROLLBACK/COMMIT
- トランザクション処理(ctrl+zに類似）（アクチュアリーは確実に使わない。）
## PRINT
- テキストを出力
