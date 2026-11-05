param([string]$Sound)
$ErrorActionPreference = 'Continue'
$e = { param($s) [System.Security.SecurityElement]::Escape([string]$s) }
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml("<toast><visual><binding template='ToastGeneric'><text>$(& $e $env:T)</text><text>$(& $e $env:B)</text></binding></visual><audio silent='true'/></toast>")
$id = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($id).Show((New-Object Windows.UI.Notifications.ToastNotification $xml))
if (Test-Path -LiteralPath $Sound) { (New-Object Media.SoundPlayer $Sound).PlaySync(); "played $Sound" } else { "sound not found: $Sound" }
