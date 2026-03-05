# Blackout.ps1 - экран в чёрный + инверсия + отключение настроек дисплея

# Максимальная инверсия цветов (Win+Ctrl+C симуляция)
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("#{^c}")

# Чёрный экран через полноэкранное окно (но лучше в Python)
# Отключение адаптивной яркости
powercfg -setacvalueindex SCHEME_CURRENT SUB_VIDEO VIDEOCONLOCK 0
powercfg -setactive SCHEME_CURRENT

# Отключение изменения яркости пользователем (частично)
sp "HKCU:\Control Panel\Desktop" "Win8DpiScaling" 1 -Type DWord -Force
sp "HKCU:\Control Panel\Desktop\WindowMetrics" "MinAnimate" 0 -Type String -Force

Write-Output "Экран потух. Нереально работать. 🍋"