
# Display disk space and warn about low free space

Write-Host "=== Disk Space Monitor ==="

Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
ForEach-Object {
    $free = [math]::Round($_.FreeSpace / 1GB, 2)
    $size = [math]::Round($_.Size / 1GB, 2)

    Write-Host "$($_.DeviceID) Free: $free GB / $size GB"

    if ($_.Size -gt 0 -and ($_.FreeSpace / $_.Size) -lt 0.15) {
        Write-Host "WARNING: Low disk space!" -ForegroundColor Red
    }
}
