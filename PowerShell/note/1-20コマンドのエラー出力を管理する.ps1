Copy-Item hoge hoge
$error

# 詳細に表示
$error | Format-List -Force

# 最後のエラーは引数を設定
$error[0]

