#!/usr/bin/env pwsh

Write-Host "🏗️ Construction Dashboard Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Check Python installation
Write-Host "`n📋 Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
    } else {
        Write-Host "❌ Python not found in PATH" -ForegroundColor Red
        Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
        exit 1
    }
} catch {
    Write-Host "❌ Python not found" -ForegroundColor Red
    exit 1
}

# Install requirements
Write-Host "`n📦 Installing required packages..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Gray

$packages = @(
    "streamlit>=1.28.0",
    "plotly>=5.15.0", 
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "openpyxl>=3.1.0",
    "seaborn>=0.12.0",
    "matplotlib>=3.7.0",
    "scipy>=1.11.0"
)

foreach ($package in $packages) {
    Write-Host "Installing $package..." -ForegroundColor Gray
    python -m pip install $package --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ $package installed" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Failed to install $package" -ForegroundColor Yellow
    }
}

# Generate data if needed
Write-Host "`n📊 Checking data files..." -ForegroundColor Yellow
$dataFiles = @(
    "data/schedule_data.csv",
    "data/cost_data.csv", 
    "data/productivity_data.csv",
    "data/safety_data.csv",
    "data/quality_data.csv",
    "data/critical_path_tasks.csv",
    "data/cost_breakdown.csv"
)

$missingFiles = @()
foreach ($file in $dataFiles) {
    if (-not (Test-Path $file)) {
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-Host "📊 Generating sample data..." -ForegroundColor Yellow
    python src/data_generator.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Sample data generated successfully!" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to generate data" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✅ All data files present" -ForegroundColor Green
}

Write-Host "`n🎉 Setup complete!" -ForegroundColor Green
Write-Host "`nTo launch the dashboard, run:" -ForegroundColor Cyan
Write-Host "  streamlit run src/dashboard.py" -ForegroundColor White
Write-Host "`nOr use the launcher:" -ForegroundColor Cyan  
Write-Host "  python launch_dashboard.py" -ForegroundColor White

# Ask if user wants to launch now
Write-Host "`n"
$launch = Read-Host "Would you like to launch the dashboard now? (y/N)"
if ($launch -eq "y" -or $launch -eq "Y" -or $launch -eq "yes") {
    Write-Host "`n🚀 Launching dashboard..." -ForegroundColor Green
    Write-Host "Opening browser to http://localhost:8501" -ForegroundColor Gray
    Write-Host "Press Ctrl+C to stop the dashboard" -ForegroundColor Gray
    Write-Host "================================" -ForegroundColor Cyan
    streamlit run src/dashboard.py
}