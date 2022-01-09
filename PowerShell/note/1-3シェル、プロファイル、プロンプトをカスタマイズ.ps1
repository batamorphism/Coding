# プロファイルを新規作成
New-Item -type file -force $profile
# プロファイルを開く
notepad $profile

# プロファイルを使えば、エイリアス、関数、変数、その他のカスタマイズも定義できる
# 特にエイリアスは最もよく使われるカスタマイズ
# プロファイルに次を記載すると、エイリアスを追加できる
Set-Alias new New-Object
Set-Alias iexplore 'C:\Program Files\Internet Explorer\iexplore.exe'

# これで、newと打つとNew-Objectが実行される
# 変更を有効にするには、プロファイルを保存してからPowerShellを再起動する
# もしくは
. $profile
# を実行する
