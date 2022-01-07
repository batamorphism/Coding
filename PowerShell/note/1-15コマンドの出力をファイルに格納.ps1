Set-Location $PSScriptRoot

Get-ChildItem | Out-File unicodeFile.txt
Get-Content filename.cs | Out-File -Encoding ASCII file.txt
Get-ChildItem | Out-File-Width 120 unicodeFile.cs

# PowerShellの書式設定された出力のファイルへのリダイレクトは
# 画面表示をWYSIWYGでまねるように設計されているため、
# 出力行の既定の幅では問題が起こる場合があります。
# 画面の表示幅が80文字の場合、ファイル内の出力行の幅も80文字になります。
Get-ChildItem > files.txt
Get-ChildItem 2> errors.txt
