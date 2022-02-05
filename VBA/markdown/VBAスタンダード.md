# VBAエキスパート試験

## 1. プロシージャ

### 1-1. 他のプロシージャを呼び出す

A1セルの2倍の値をB1セルに代入せよ

```VB
Sub Sample1()
    Range("B1") = Range("A1").Value
End Sub
```

Sample1プロシージャを呼び出せ

```VB
Sub Sample2()
    Call Sample
End Sub
```

ローカル変数Aを定義し、100を代入せよ

```VB
Sub Sample3()
    Dim A As Long
    A = 100
End Sub
```

モジュールレベル変数Aを定義し、100を代入せよ

```VB
Dim A As Long

Sub Sample4()
    A = 100
End Sub
```

### 1-2. Functionプロシージャ

A1セルの2倍の値を返すFunctionプロシージャを作成せよ

```VB
Function Sample1()
    Sample1 = Range("A1") * 2
End Function
```

ある名前のシートが存在するか確認するFunctionプロシージャCheckSheetを作成せよ

```VB
Function CheckSheet(p_sheet_name As String)
    Dim ws As Worksheet
    For Each ws In Worksheets
        If ws.Name = p_sheet_name Then
            CheckSheet = True
            Exit Function
        End If
    Next
    CheckSheet = False
End Function
```

### 1-3. 引数を渡す

値を引数として受け取り、メッセージボックスとして出力するプロシージャを作成せよ

```VB
Sub Sample1(A As Long)
    MsgBox A
End Sub
```

「ByRef」を使わず、参照渡しで値を2倍にするプロシージャを作成せよ

```VB
' ByValを明言しない場合、勝手に参照渡しとなり危険
Sub Sample(p_value)
    p_value = p_value * 2
End Sub
```

値渡しで値を2倍にするプロシージャを作成せよ

```VB
Sub Sample(ByVal p_value)
    p_value = p_value * 2
End Sub
```

明示的に参照渡しにせよ

```VB
Sub Sample(ByRef p_value)
    p_value = p_value * 2
End Sub
```

### 1-4. 引数を使わないで値を共有する

引数を使わないで、変数に100を代入するプロシージャと、その変数の値をメッセージボックスで出力するプロシージャを作成せよ

```VB
Dim A As Long


Sub Sample1()
    A = 100
    Call Sample2
End Sub


Sub Sample2()
    MsgBox A
End Sub
```

## 2. 変数

### 2-1. 配列

長さ4の配列を宣言せよ

```VB
Sub Sample1()
    Dim A(3) As String
End Sub
```

文字列"a-b-c"を、-区切りで要素数3の配列にせよ

```VB
Sub Sample1()
    Dim A As Variant
    A = Split("a-b-c", "-")
End Sub
```

与えられた配列について、配列の要素数を調べ、インデックスで配列の要素を取得し、Debug.Printするプロシージャを作成せよ

```VB
Sub Sample1(A As Variant)
    Dim i As Long
    For i = 0 To UBound(A)
        Debug.Print A(i)
    Next
End Sub
```

### 2-2. 動的配列

動的配列を宣言し、要素数3に変更せよ

```VB
Sub Sample1()
    Dim A() As String
    ReDim A(2)
End Sub
```

引数として与えられた動的配列に、引数として与えられた変数を追加するプロシージャPushBackを作成せよ

```VB
Sub PushBack(ByRef p_A As Variant, ByVal p_val As Variant)
    Dim len_A As Long
    len_A = UBound(p_A)
    ReDim Preserve p_A(len_A + 1)
    p_A(len_A + 1) = p_val
End Sub

Sub Test()
    Dim A() As Variant, i As Integer
    A = Array()
    For i = 0 To 100
        Call PushBack(A, i)
    Next
    For i = 0 To 100
        Debug.Print A(i)
    Next
End Sub
```

### 2-3. オブジェクト変数

変数にRangeオブジェクトのA1セルを格納せよ

```VB
Sub Sample1()
    Dim rng As Range
    Set rng = Range("A1")
End Sub
```

今開いているワークシートを変数に保持し、新たにシートを追加して名前を「追加」に変更し、元のワークシートをアクティブ化せよ

```VB
Sub Sample1()
    Dim cur_ws As Worksheet, add_ws As Worksheet
    Set cur_ws = ActiveSheet
    Set add_ws = Worksheets.Add()
    add_ws.Name = "追加"
    cur_ws.Activate
End Sub
```

### 2-4. 変数の演算

A1～A10セルに編集されている値のうち、「東京」のものをカウントせよ

```VB
Sub Sample()
    Dim r As Long, cnt As Long
    For r = 1 To 10
        If Cells(r, 1) = "東京" Then
            cnt = cnt + 1
        End If
    Next
    Debug.Print cnt
End Sub
```

SUMIF(A1:A10,"東京", B1:B10)をVBAで組め

```VB
Sub Sample()
    Dim r As Long, sum_val As Long
    For r = 1 To 10
        If Cells(r, 1) = "東京" Then
            sum_val = sum_val + Cells(r, 2)
        End If
    Next
    Debug.Print sum_val
End Sub
```

### 2-5. 文字列を結合

A1～A3セルの文字列を結合せよ

```VB
Sub Sample()
    Dim s As String, r As Long
    For r = 1 To 3
        s = s & Cells(r, 1)
    Next
    Debug.Print s
End Sub
```

## 3. ステートメント

### 3-1. Exitステートメント

プロシージャを作成し、即時にExitステートメントで抜けよ。

```VB
Sub Sample()
    Exit Sub
End Sub


Function Sample2()
    Exit Function
End Function
```

ForループとWhileループを作成し、即時にExitステートメントで抜けよ。

```VB
Sub Sample1()
    Dim i As Integer
    For i = 0 To 100
        Exit For
    Next
    Do While True
        Exit Do
    Loop
End Sub

```

### 3-2. Select Caseステートメント

整数値による分岐をSelectを用い作成せよ

```VB
Sub Sample1()
    Dim val As Long
    val = 1
    Select Case val
        Case 1
            Debug.Print "hoge"
        Case 2
            Debug.Print "piyo"
        Case 3
            Debug.Print "fuga"
    End Select
End Sub
```

文字列による分岐をSelectを用い作成せよ

```VB
Sub Sample1()
    Dim s As String
    s = "月曜"
    Select Case s
        Case "月曜"
            Debug.Print "hoge"
        Case "火曜"
            Debug.Print "piyo"
        Case "水曜"
            Debug.Print "fuga"
    End Select
End Sub
```

A1セルに入力された値が10未満の場合と20以上の場合とそれ以外で処理を分岐させよ

```VB
Sub Sample1()
    Dim val As Long
    val = Range("A1").Value
    Select Case val
        Case Is < 10
            Debug.Print "hoge"
        Case Is >= 20
            Debug.Print "piyo"
        Case Else
            Debug.Print "fuga"
    End Select
End Sub
```

### 3-3. Do...Loopステートメント

WhileループとDo Whileループを作成し、即座にExitで抜けよ

```VB
Sub Sample1()
    Do While True
        Exit Do
    Loop
    Do
        Exit Do
    Loop While True
End Sub
```

Untilを用い、A1セルが空欄の間は処理を繰り返せ

```VB
Sub Sample1()
    Do Until Range("A1").Value <> ""
        Exit Do
    Loop
End Sub
```

### 3-4. For Each ステートメント

ワークシートの名前を列挙せよ

```VB
Sub Sample1()
    Dim ws As Worksheet
    For Each ws In Worksheets
        Debug.Print ws.Name
    Next
End Sub
```

Range("A1:A3")の全ての値を2倍にせよ

```VB
Sub Sample1()
    Dim rng As Range
    For Each rng In Range("A1:A3")
        rng.Value = rng.Value * 2
    Next
End Sub
```

選択されているセル全ての値を2倍にせよ

```VB
Sub Sample1()
    Dim rng As Range
    For Each rng In Selection
        rng.Value = rng.Value * 2
    Next
End Sub
```

長さ3、要素10, 20, 30の配列を作成し、総和をとれ

```VB
Sub Sample1()
    Dim A As Variant: A = Array(10, 20, 30)
    Dim a_i As Variant
    Dim sum_a As Long
    For Each a_i In A
        sum_a = sum_a + a_i
    Next
    Debug.Print sum_a
End Sub
```

### 3-5. Ifステートメント

今日が月曜日の場合、1を、それ以外の時は0を出力せよ

```VB
Sub Sample1()
    Dim wd As String
    wd = WeekdayName(Weekday(Now()))
    If wd = "月曜日" Then
        Debug.Print 1
    Else
        Debug.Print 0
    End If
End Sub
```

## 4. ファイルの操作

### 4-1. ブックを開く

新しいファイルを作成し、ファイルを保存し、ファイルを閉じ、そのファイルを開け

```VB
Sub Sample1()
    Dim wb As Workbook, fn As String
    Set wb = Workbooks.Add
    Call wb.SaveAs(Filename:="test")
    fn = wb.FullName
    wb.Close
    Call Workbooks.Open(Filename:=fn)
End Sub
```

今日の西暦、月、日付を文字列で表示せよ

```VB
Sub Sample1()
    Debug.Print Format(Now(), "yyyymmdd")
End Sub
```

### 4-3. ファイルをコピーする

新しいファイルを作成し、ファイルを保存し、ファイルを別名でコピーせよ

```VB
Sub Sample1()
    Dim wb As Workbook, fn As String
    Set wb = Workbooks.Add
    wb.SaveAs Filename:="test"
    fn = wb.FullName
    wb.Close
    Call FileCopy(fn, "test2.xlsx")
End Sub
```

### 4-4. フォルダーを作成せよ

フォルダーを作成せよ

```VB
Sub Sample1()
    MkDir "test"
End Sub
```
