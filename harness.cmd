@echo off
rem ------------------------------------------------------------------
rem  Cap Aging Diagnosis Research Harness - launcher for cmd.exe / double-click
rem  Runs harness.ps1 with the execution policy bypassed for this process only.
rem  Usage:  harness [profile] [request words...]     (same arguments as harness.ps1)
rem  Prefers PowerShell 7 (pwsh.exe) and falls back to Windows PowerShell 5.1.
rem ------------------------------------------------------------------
setlocal
set "PS_EXE=pwsh.exe"
where pwsh.exe >nul 2>nul || set "PS_EXE=powershell.exe"
"%PS_EXE%" -NoProfile -ExecutionPolicy Bypass -File "%~dp0harness.ps1" %*
set "RC=%ERRORLEVEL%"
endlocal & exit /b %RC%
