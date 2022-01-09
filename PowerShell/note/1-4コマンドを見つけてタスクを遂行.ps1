# textを含むコマンドを検索する
Get-Command *text*
# より詳細に検索するには、パイプラインを使用する
Get-Command Context | Format-List
# Get動詞を使用するすべてのコマンドを検索するには、-Verbを使う
Get-Command -Verb Get
# Serviceに関する処理を行うすべてのコマンドを検索するには-Nounを使う
Get-Command -Noun Service
# PowerShellのコマンド名は動詞-名詞の一貫性がある
