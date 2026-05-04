@echo off

echo Starting Docker...

start cmd /k docker-compose up --build

echo Waiting for app...

:loop
curl http://localhost:8501 >nul 2>&1
if %errorlevel% neq 0 (
    timeout /t 2 >nul
    goto loop
)

start http://localhost:8501