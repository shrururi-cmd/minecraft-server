@echo off
title Minecraft Server Rescue Tool 🚀
color 0A

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo Please install Python from python.org and try again.
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

echo [1/2] Installing Dependencies...
pip install -r tool\requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b
)

echo.
echo [2/2] Launching Rescue Tool...
python tool\setup_server.py

pause
