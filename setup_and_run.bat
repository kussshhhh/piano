@echo off

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Installing Python...
    REM Install Python using the Microsoft Store (requires Windows 10 or later)
    start /wait ms-windows-store://pdp/?productid=9PJPW5LDXLZ5
    REM Wait for the user to install Python
    pause
)

REM Check if pip is installed
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

REM Check if requirements.txt exists
IF NOT EXIST requirements.txt (
    echo requirements.txt not found!
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Set environment variable for UTF-8 encoding
set PYTHONIOENCODING=utf-8

REM Run the main Python script
echo Running the main script...
python main.py
