# DisableKeys.ps1 - блокировка клавиш и SAS

# Отключение Win-комбинаций
ni "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Force | Out-Null
sp "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" "NoWinKeys" 1 -Type DWord -Force

# Отключение Ctrl+Alt+Del (работает только на Pro/Enterprise)
ni "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Force | Out-Null
sp "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" "DisableCAD" 1 -Type DWord -Force

# Блокировка Alt+Tab через реестр (частично)
sp "HKCU:\Control Panel\Desktop" "UserPreferencesMask" ([byte[]](0x90,0x12,0x20,0x00,0x00,0x00,0x00,0x00)) -Type Binary -Force

# Запуск фильтра клавиш (через Python или отдельный процесс, но здесь просто реестр)
Write-Output "Клавиши заблокированы. Для отмены перезагрузи в безопасном режиме."