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
