
# Display processes using the most memory

Write-Host "=== Top 10 Memory-Using Processes ==="

Get-Process |
    Sort-Object WorkingSet64 -Descending |
    Select-Object -First 10 ProcessName,
        Id,
        @{Name="Memory (MB)"; Expression={
            [math]::Round($_.WorkingSet64 / 1MB, 2)
        }} |
    Format-Table -AutoSize
