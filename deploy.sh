#!/bin/bash
# Quick deployment script for Streamlit Cloud

echo "======================================"
echo "Diet Recommendation System Deployment"
echo "======================================"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
else
    echo "✓ Git repository already initialized"
fi

# Add all files
echo "Adding files to Git..."
git add .

# Commit
echo "Creating commit..."
git commit -m "Prepare for Streamlit Cloud deployment with embedded ML model"

echo ""
echo "======================================"
echo "Next Steps:"
echo "======================================"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo ""
echo "2. Run these commands (replace YOUR_USERNAME and REPO_NAME):"
echo "   git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy on Streamlit Cloud:"
echo "   https://share.streamlit.io"
echo "   - Main file path: Streamlit_Frontend/Hello.py"
echo ""
echo "For detailed instructions, see DEPLOYMENT.md"
echo ""
