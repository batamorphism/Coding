Set-Location $PSScriptRoot

Get-ChildItem | Out-File -Append files.txt
Get-ChildItem >> files.txt
