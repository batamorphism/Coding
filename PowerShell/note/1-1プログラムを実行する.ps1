<#-----
プログラム、スクリプト、バッチファイル、その他実行可能なコマンドは、そのファイル名を入力する
拡張子は省略可能である
Program.exe argument
Program.ps1 argument
BatchFile.cmd argument
そのため、既存の資産を使いまわすことができる
-----#>

# メモ帳を起動する
notepad.exe

# フルパスでメモ帳を起動する
C:\WINDOWS\system32\notepad.exe

# 名前にスペースがある場合は、実行演算子&をつかい、シングルクオートで囲む
& 'C:\WINDOWS\system32\notepad.exe'

# カレントディレクトリから実行するには、.\をつける
cd C:\WINDOWS\system32\
.\notepad.exe

# カレントディレクトリからスペースのあるファイルを実行するには、&と'をつける
& '.\notepad.exe'
