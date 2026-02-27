# Quick Setup Script for CAD Prompt Generator
# Run this script to set up the project automatically

Write-Host "🔧 AI-Assisted CAD Prompt Generator - Setup Script" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "1️⃣ Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "   ✅ Found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "   ❌ Python not found! Please install Python 3.10+ from python.org" -ForegroundColor Red
    exit 1
}

# Check Ollama installation
Write-Host ""
Write-Host "2️⃣ Checking Ollama installation..." -ForegroundColor Yellow
try {
    $ollamaVersion = ollama --version 2>&1
    Write-Host "   ✅ Found: $ollamaVersion" -ForegroundColor Green
}
catch {
    Write-Host "   ❌ Ollama not found! Please install from ollama.ai" -ForegroundColor Red
    Write-Host "   Download: https://ollama.ai/download" -ForegroundColor Yellow
    exit 1
}

# Check if Ollama is running
Write-Host ""
Write-Host "3️⃣ Checking if Ollama service is running..." -ForegroundColor Yellow
try {
    ollama list 2>&1 | Out-Null
    Write-Host "   ✅ Ollama service is running" -ForegroundColor Green
}
catch {
    Write-Host "   ⚠️ Ollama service might not be running" -ForegroundColor Yellow
    Write-Host "   Starting Ollama service..." -ForegroundColor Yellow
    Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 3
}

# Check for Llama models
Write-Host ""
Write-Host "4️⃣ Checking for Llama models..." -ForegroundColor Yellow
$models = ollama list 2>&1
if ($models -match "llama3.2" -or $models -match "llama3.1" -or $models -match "llama2") {
    Write-Host "   ✅ Llama model found" -ForegroundColor Green
}
else {
    Write-Host "   ⚠️ No Llama model found. Pulling llama3.2..." -ForegroundColor Yellow
    Write-Host "   This may take several minutes..." -ForegroundColor Yellow
    ollama pull llama3.2
    Write-Host "   ✅ Model downloaded successfully" -ForegroundColor Green
}

# Create virtual environment
Write-Host ""
Write-Host "5️⃣ Creating Python virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "   ⚠️ Virtual environment already exists, skipping..." -ForegroundColor Yellow
}
else {
    python -m venv venv
    Write-Host "   ✅ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment and install dependencies
Write-Host ""
Write-Host "6️⃣ Installing Python dependencies..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
pip install -r requirements.txt --quiet
Write-Host "   ✅ Dependencies installed" -ForegroundColor Green

# Final instructions
Write-Host ""
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "✅ Setup Complete!" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Yellow
Write-Host "  1. Activate virtual environment: .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  2. Run the app: streamlit run app.py" -ForegroundColor White
Write-Host ""
Write-Host "Or simply run: .\run.ps1" -ForegroundColor Cyan
Write-Host ""
