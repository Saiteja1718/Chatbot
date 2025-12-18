# Quick deployment script for Streamlit Cloud (Windows PowerShell)

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Diet Recommendation System Deployment" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "✓ Git repository already initialized" -ForegroundColor Green
}

# Add all files
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add .

# Commit
Write-Host "Creating commit..." -ForegroundColor Yellow
git commit -m "Prepare for Streamlit Cloud deployment with embedded ML model"

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Create a new repository on GitHub:" -ForegroundColor White
Write-Host "   https://github.com/new" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. Run these commands (replace YOUR_USERNAME and REPO_NAME):" -ForegroundColor White
Write-Host '   git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git' -ForegroundColor Yellow
Write-Host '   git branch -M main' -ForegroundColor Yellow
Write-Host '   git push -u origin main' -ForegroundColor Yellow
Write-Host ""
Write-Host "3. Deploy on Streamlit Cloud:" -ForegroundColor White
Write-Host "   https://share.streamlit.io" -ForegroundColor Yellow
Write-Host "   - Main file path: Streamlit_Frontend/Hello.py" -ForegroundColor Yellow
Write-Host ""
Write-Host "For detailed instructions, see DEPLOYMENT.md" -ForegroundColor Green
Write-Host ""
