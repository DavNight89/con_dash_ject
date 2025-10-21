@echo off
echo Starting Construction Project Dashboard...
echo.

REM Check if data files exist
if not exist "data\schedule_data.csv" (
    echo Data files not found. Running setup first...
    call setup.bat
    if errorlevel 1 (
        echo Setup failed. Please run setup.bat manually.
        pause
        exit /b 1
    )
)

echo Launching dashboard...
streamlit run src\dashboard.py

pause