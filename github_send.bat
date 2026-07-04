@echo off

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd HH:mm:ss"') do set DATETIME=%%i

git add .
git commit -m "Commit %DATETIME% + aplikacja etykiet"
git push -u origin main