echo 1
Get-History
Invoke-History 1
Get-History | Export-Clixml log.xml
Import-Clixml log.xml | Add-History
