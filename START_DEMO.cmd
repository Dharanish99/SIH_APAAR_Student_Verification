@echo off
setlocal
cd /d "%~dp0"
where node >nul 2>nul
if errorlevel 1 (
  echo Install Node.js 24.x, then run this file again.
  pause
  exit /b 1
)
if not exist node_modules (
  call npm ci
  if errorlevel 1 goto failed
)
call npm run build
if errorlevel 1 goto failed
echo Open http://127.0.0.1:4871 - or the PORT configured in .env.
echo Synthetic data only. Keep this terminal open. Ctrl+C stops the demo.
call npm start
if errorlevel 1 goto failed
exit /b 0
:failed
echo The demo could not start. Check Node 24.x, the port and the error above.
pause
exit /b 1
