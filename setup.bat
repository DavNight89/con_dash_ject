@echo off
echo Setting up Construction Project Dashboard...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH. Please install Python first.
    pause
    exit /b 1
)

echo Python found. Installing required packages...
echo.

REM Install required packages
pip install streamlit plotly pandas numpy openpyxl seaborn matplotlib scipy

if errorlevel 1 (
    echo Failed to install packages. Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo Packages installed successfully!
echo.

REM Generate sample data
echo Generating sample construction project data...
python src\data_generator.py

if errorlevel 1 (
    echo Failed to generate data. Please check for errors.
    pause
    exit /b 1
)

echo.
echo Sample data generated successfully!
echo.
echo Setup complete! 
echo.
echo To run the dashboard, use: streamlit run src\dashboard.py
echo.
pause