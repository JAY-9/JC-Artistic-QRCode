# Deployment Guide - Artistic QR Code Generator

## 🚀 Quick Deploy to Streamlit Cloud (Recommended)

### Prerequisites
- GitHub account
- Git installed on your computer

### Step-by-Step Instructions

#### 1. Initialize Git Repository
```bash
cd d:\Projects\TMP
git init
git add .
git commit -m "Initial commit - Artistic QR Code Generator"
```

#### 2. Create GitHub Repository
1. Go to [github.com](https://github.com) and sign in
2. Click "+" → "New repository"
3. Name it: `artistic-qr-generator` (or any name you like)
4. **Keep it PUBLIC** (required for free Streamlit Cloud)
5. Don't initialize with README (we already have files)
6. Click "Create repository"

#### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/artistic-qr-generator.git
git branch -M main
git push -u origin main
```

#### 4. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Authorize Streamlit
4. Click "New app"
5. Select:
   - **Repository**: `YOUR_USERNAME/artistic-qr-generator`
   - **Branch**: `main`
   - **Main file path**: `app.py`
6. Click "Deploy!"

#### 5. Wait for Deployment
- First deployment takes 2-3 minutes
- You'll get a URL like: `https://your-app-name.streamlit.app`
- Share this URL with anyone!

---

## 🔄 Updating Your Deployed App

After making changes:
```bash
git add .
git commit -m "Description of changes"
git push
```

Streamlit Cloud will automatically redeploy within 1-2 minutes!

---

## 🌐 Alternative: Hugging Face Spaces

### Steps:
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Name: `artistic-qr-generator`
4. License: Apache 2.0
5. SDK: **Streamlit**
6. Click "Create Space"
7. Upload files:
   - `app.py`
   - `requirements.txt`
   - `packages.txt` (optional)
8. Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/artistic-qr-generator`

---

## 🐳 Alternative: Docker Deployment

If you want to deploy on your own server or cloud platform:

### Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Deploy:
```bash
docker build -t qr-generator .
docker run -p 8501:8501 qr-generator
```

---

## 📊 Deployment Comparison

| Platform | Cost | Ease | Performance | Custom Domain |
|----------|------|------|-------------|---------------|
| **Streamlit Cloud** | Free | ⭐⭐⭐⭐⭐ | Good | Yes (paid) |
| **Hugging Face** | Free | ⭐⭐⭐⭐ | Good | Limited |
| **Railway** | $5/mo free | ⭐⭐⭐⭐ | Excellent | Yes |
| **Render** | Free tier | ⭐⭐⭐ | Good | Yes |

---

## ⚠️ Important Notes

1. **Public Repository**: Streamlit Cloud free tier requires public GitHub repos
2. **Resource Limits**: Free tiers have CPU/memory limits (fine for this app)
3. **Cold Starts**: Free apps may sleep after inactivity (wake up in ~30 seconds)
4. **File Storage**: Temporary files are cleared periodically (our app handles this)

---

## 🎉 You're Done!

Once deployed, your QR code generator will be accessible worldwide at your custom URL!
