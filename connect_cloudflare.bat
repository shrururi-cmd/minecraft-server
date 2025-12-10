@echo off
chcp 65001 >nul
title Cloudflare Tunnel Connector
cls

echo ===================================================
echo      Cloudflare Tunnel Connector for Minecraft
echo ===================================================
echo.

:: 1. Check if cloudflared exists
if not exist "cloudflared.exe" (
    echo [INFO] Downloading cloudflared for Windows...
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe' -OutFile 'cloudflared.exe'"
    if exist "cloudflared.exe" (
        echo [OK] Download complete.
    ) else (
        echo [ERROR] Download failed. Check your internet.
        pause
        exit /b
    )
)

:: 2. Ask for the Link
echo.
echo [STEP 1] Go to your GitHub Actions logs.
echo [STEP 2] Find the link looking like: https://something-random.trycloudflare.com
echo.
set /p CLOUDFLARE_URL="Paste the Cloudflare Link here: "

:: 3. Start the Bridge
echo.
echo [INFO] Establishing connection...
echo [INFO] Keep this window OPEN while playing!
echo.
echo [GAME] In Minecraft, connect to IP: localhost
echo.
echo ===================================================

cloudflared.exe access tcp --hostname %CLOUDFLARE_URL% --url localhost:25565

pause
