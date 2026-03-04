@echo off
:loop
echo Ты попал, недохакер! > C:\ProgramData\DrMengeleMessage.txt
start notepad C:\ProgramData\DrMengeleMessage.txt
echo Доктор Менгеле захватил твой ПК! > C:\Users\Public\Desktop\WARNING.txt
start "" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
timeout /t 5 >nul
goto loop
