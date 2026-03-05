param(
    [string]$ExePath = "doctor_mengele.exe"
)

$processName = [System.IO.Path]::GetFileNameWithoutExtension($ExePath)

Write-Host "Watcher запущен. Следим за $processName..."

while ($true) {
    $running = Get-Process -Name $processName -ErrorAction SilentlyContinue
    if (-not $running) {
        Write-Host "Процесс мёртв → перезапускаем..."
        Start-Process -FilePath $ExePath -WindowStyle Hidden
    }
    Start-Sleep -Seconds 2
}