
# Check basic network connectivity

Write-Host "=== Network Troubleshooter ==="

# Display IP configuration
ipconfig

# Test connectivity
Write-Host "`nTesting internet connectivity..."
Test-Connection 8.8.8.8 -Count 2

# Check DNS resolution
Write-Host "`nTesting DNS..."
Resolve-DnsName google.com
