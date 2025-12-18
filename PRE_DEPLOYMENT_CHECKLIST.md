# Pre-Deployment Checklist ✅

Use this checklist before deploying to Streamlit Cloud.

## 1. Local Testing
- [ ] App runs locally without errors: `streamlit run Streamlit_Frontend/Hello.py`
- [ ] Diet Recommendation feature works (generates recipes)
- [ ] Custom Food Recommendation works
- [ ] Meal Planner works (if using LLM features)
- [ ] No backend connection errors (backend is now embedded)

## 2. Files Check
- [ ] `requirements.txt` exists in root directory
- [ ] `.streamlit/config.toml` exists
- [ ] `Data/dataset.csv` exists and will be committed
- [ ] `.gitignore` exists
- [ ] All `__pycache__` folders are ignored

## 3. Code Quality
- [ ] No hardcoded local paths (like `C:\Users\...`)
- [ ] No API keys or secrets in code
- [ ] All imports work correctly
- [ ] No unnecessary large files

## 4. GitHub Setup
- [ ] GitHub account created
- [ ] Git installed on your computer
- [ ] Ready to create new repository

## 5. Streamlit Cloud Account
- [ ] Streamlit Cloud account (sign up at https://share.streamlit.io)
- [ ] GitHub connected to Streamlit Cloud

## 6. Documentation
- [ ] Read `DEPLOYMENT.md` for full instructions
- [ ] Understand the deployment process
- [ ] Know how to check logs if issues occur

## 7. Performance Considerations

### Current Setup:
- **Dataset size**: Check `Data/dataset.csv` size
- **Memory usage**: Should be under 1GB for free tier
- **Dependencies**: Heavy packages (torch, transformers) may increase deployment time

### Optional Optimizations:
- [ ] Consider removing unused dependencies from `requirements.txt`
- [ ] If torch/transformers aren't critical, comment them out for faster deployment
- [ ] Dataset is gzipped to save space

## 8. Deployment Configuration

When deploying on Streamlit Cloud, use:
- **Main file path**: `Streamlit_Frontend/Hello.py`
- **Python version**: 3.10 or 3.9
- **Branch**: main (or master)

## 9. Post-Deployment

After deployment:
- [ ] App loads successfully
- [ ] Test Diet Recommendation with sample inputs
- [ ] Test Custom Food Recommendation
- [ ] Test Meal Planner
- [ ] Check for any error messages in Streamlit Cloud logs
- [ ] Share your app URL!

## 10. Troubleshooting Resources

If issues occur:
1. Check Streamlit Cloud logs (click "Manage app" → "Logs")
2. See `DEPLOYMENT.md` troubleshooting section
3. Visit Streamlit Community Forum: https://discuss.streamlit.io
4. Check requirements.txt for version conflicts

---

## Quick Command Reference

### Test Locally
```powershell
streamlit run Streamlit_Frontend/Hello.py
```

### Deploy to GitHub
```powershell
git init
git add .
git commit -m "Initial commit for deployment"
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

### Update Deployed App
```powershell
git add .
git commit -m "Update app"
git push
```

---

## ✨ You're Ready!

Once all items are checked, proceed with deployment using the instructions in `DEPLOYMENT.md` or `DEPLOYMENT_SUMMARY.md`.

Good luck! 🚀
