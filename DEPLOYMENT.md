# Streamlit Cloud Deployment Guide

This guide will help you deploy the Diet Recommendation System to Streamlit Cloud.

## Prerequisites

1. A GitHub account
2. Git installed on your computer
3. Your project ready for deployment

## Changes Made for Deployment

The following changes were made to make the app work on Streamlit Cloud:

1. **Embedded Backend Logic**: The FastAPI backend logic has been integrated directly into `Streamlit_Frontend/Generate_Recommendations.py`, eliminating the need for a separate backend server.

2. **Updated Requirements**: Created `requirements.txt` in the root directory with all necessary dependencies.

3. **Streamlit Configuration**: Added `.streamlit/config.toml` for proper configuration.

4. **Fixed Path Issues**: Updated file paths to work in both local and cloud environments.

5. **Compatibility Fixes**: Changed `st.rerun()` to `st.experimental_rerun()` for Streamlit 1.16.0 compatibility.

## Deployment Steps

### Step 1: Push Your Code to GitHub

1. **Initialize Git Repository** (if not already done):
   ```bash
   cd Diet-Recommendation-System-main
   git init
   ```

2. **Add all files**:
   ```bash
   git add .
   ```

3. **Commit your changes**:
   ```bash
   git commit -m "Prepare for Streamlit Cloud deployment"
   ```

4. **Create a new repository on GitHub**:
   - Go to https://github.com/new
   - Name it "Diet-Recommendation-System" (or any name you prefer)
   - DO NOT initialize with README, .gitignore, or license
   - Click "Create repository"

5. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit https://share.streamlit.io
   - Click "Sign in with GitHub"
   - Authorize Streamlit to access your GitHub account

2. **Create New App**:
   - Click "New app" button
   - Select your repository from the dropdown
   - Set the following:
     - **Branch**: main
     - **Main file path**: `Streamlit_Frontend/Hello.py`
     - **App URL**: Choose a custom URL (optional)

3. **Advanced Settings** (click Advanced settings before deploying):
   - **Python version**: 3.10 (or 3.9)
   - Keep other settings as default

4. **Deploy**:
   - Click "Deploy!" button
   - Wait for the deployment to complete (this may take 5-10 minutes)

### Step 3: Verify Deployment

1. Once deployed, your app will be available at: `https://YOUR_APP_NAME.streamlit.app`

2. Test all features:
   - ✅ Home page loads correctly
   - ✅ Diet Recommendation page works
   - ✅ Custom Food Recommendation works
   - ✅ Meal Planner works

## File Structure for Deployment

Your repository should have this structure:
```
Diet-Recommendation-System-main/
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── Data/
│   └── dataset.csv          # Dataset file (must be included)
├── Streamlit_Frontend/
│   ├── Hello.py             # Main entry point
│   ├── Generate_Recommendations.py  # Now includes ML model
│   ├── pages/
│   │   ├── 1_💪_Diet_Recommendation.py
│   │   ├── 2_🔍_Custom_Food_Recommendation.py
│   │   └── 3_🍽️_Meal_Planner.py
│   └── ... (other files)
├── requirements.txt         # Python dependencies
├── packages.txt            # System dependencies (if needed)
└── README.md
```

## Important Notes

### What NOT to Push to GitHub

Create a `.gitignore` file with:
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.env
.venv
venv/
ENV/
.DS_Store
```

### Troubleshooting

**Problem**: App crashes on startup
- **Solution**: Check the logs in Streamlit Cloud dashboard for errors

**Problem**: "Module not found" error
- **Solution**: Make sure all dependencies are in `requirements.txt`

**Problem**: Dataset not found
- **Solution**: Ensure `Data/dataset.csv` is committed to your repository

**Problem**: App runs slowly
- **Solution**: This is normal on first load; Streamlit Cloud caches data after the first run

**Problem**: Torch/Transformers installation fails
- **Solution**: These are for the Meal Planner LLM features. If not critical, you can comment them out in requirements.txt

## Updating Your Deployed App

When you push changes to your GitHub repository:
```bash
git add .
git commit -m "Update app"
git push
```

Streamlit Cloud will automatically detect changes and redeploy your app within a few minutes.

## Resource Limits

Streamlit Cloud free tier includes:
- 1 GB RAM
- 1 CPU core
- 1 app per account (unless upgraded)

If your app exceeds these limits, consider:
- Upgrading to Streamlit Cloud paid plan
- Optimizing your code
- Reducing dataset size
- Using caching more effectively

## Alternative: Local Testing

Before deploying, test locally:
```bash
cd Diet-Recommendation-System-main
streamlit run Streamlit_Frontend/Hello.py
```

Your app will open at http://localhost:8501

## Support

- Streamlit Documentation: https://docs.streamlit.io
- Streamlit Community Forum: https://discuss.streamlit.io
- GitHub Issues: Create issues in your repository

## Cost

Streamlit Cloud Community tier is **FREE** and includes:
- 1 private or public app
- 1 GB RAM
- 800 hours/month of compute
- GitHub authentication

Perfect for this project! 🎉
