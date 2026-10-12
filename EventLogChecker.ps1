
# Show recent system errors and warnings

Write-Host "=== Recent System Events ==="

Get-WinEvent -FilterHashtable @{
    LogName = "System"
    Level = 2, 3
} -MaxEvents 10 -ErrorAction SilentlyContinue |
    Select-Object TimeCreated, LevelDisplayName,
        ProviderName, Message |
    Format-List
