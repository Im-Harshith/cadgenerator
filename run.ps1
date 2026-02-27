# Quick Run Script for CAD Prompt Generator
# This script activates the virtual environment and runs the Streamlit app

Write-Host "🚀 Starting AI-Assisted CAD Prompt Generator..." -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "❌ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run setup.ps1 first: .\setup.ps1" -ForegroundColor Yellow
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Check if Ollama is running
Write-Host "Checking Ollama service..." -ForegroundColor Yellow
try {
    ollama list | Out-Null
    Write-Host "✅ Ollama is running" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Starting Ollama service..." -ForegroundColor Yellow
    Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 3
}

# Run Streamlit app
Write-Host ""
Write-Host "Starting Streamlit app..." -ForegroundColor Green
Write-Host "The app will open in your browser at http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
streamlit run app.py
