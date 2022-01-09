#####
##
## Search-Help.ps1
##
## 指定されたキーワード又は正規表現をPowerShellヘルプドキュメントから検索する
##
## 例:
##  Search-Help hashtable
##  Search-Help "(datetime|ticks)"
#####

param($pattern = $(throw "Please specify content to search for"))

$ helpNames = $(Get-Help * | Where-Object { $_.Category -ne "Alias"})

foreach($helpTopic in $helpNames) {
    $content = Get-Help -Full $helpTopic.Name | Out-String
    if($content -match $pattern) {
        $helpTopic | Select-Object Name, Synopsis
    }
}
