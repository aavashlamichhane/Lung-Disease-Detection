# Quick Start Guide

Get Lung Disease Detection up and running in 10 minutes!

## ⚡ Prerequisites

Make sure you have:
- Python 3.9+ installed
- Node.js 16+ and npm
- At least 8GB RAM
- 2GB free disk space

## 🚀 Installation (5 steps)

### 1. Clone and Setup

```bash
git clone https://github.com/aavashlamichhane/Lung-Disease-Detection.git
cd Lung-Disease-Detection
```

### 2. Download Model

Download [model.h5](https://drive.google.com/file/d/15UNsIE3aIHudTiRVSqAT4S3AT3veFb2S/view?usp=sharing) (90MB) and save to:
```
Django/LD/model.h5
```

### 3. Install Backend Dependencies

```bash
# Create virtual environment
python -m venv env

# Activate (Windows)
env\Scripts\activate

# Activate (macOS/Linux)
source env/bin/activate

# Install packages
pip install -r requirements.txt

# Setup Django
cd Django/LD
mkdir -p media/downloads
python manage.py migrate
cd ../..
```

### 4. Install Frontend Dependencies

```bash
cd Frontend
npm install
mkdir -p src/Components/python_preds
cd ..
```

### 5. Install http-server

```bash
npm install -g http-server
```

## 🎯 Running the Application

Open **3 terminal windows**:

### Terminal 1: Backend (Django)
```bash
cd Django/LD
python manage.py runserver
```
✅ Backend running at http://127.0.0.1:8000

### Terminal 2: Frontend (React)
```bash
cd Frontend
npm run dev
```
✅ Frontend running at http://localhost:5173

### Terminal 3: Image Server
```bash
cd Frontend/src/Components/python_preds
http-server ./
```
✅ Image server running at http://127.0.0.1:8080

## 🎉 Use the Application

1. Open browser → http://localhost:5173
2. Click "Let's Begin"
3. Upload a chest X-ray image
4. View results (prediction + confidence + annotated image)

## 🆘 Quick Troubleshooting

### "Module not found"
```bash
source env/bin/activate  # Activate virtual environment
pip install -r requirements.txt
```

### "Port already in use"
```bash
# Find and kill process (example for port 8000)
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -ti:8000 | xargs kill -9
```

### "CORS error"
- Ensure backend is running
- Check frontend is at http://localhost:5173
- Verify CORS settings in Django/LD/LD/settings.py

### "Model file not found"
- Ensure model.h5 is in Django/LD/ directory
- Check file size is ~90MB
- Re-download if corrupted

### "Images not showing in results"
- Verify http-server is running
- Check python_preds folder exists
- Ensure port 8080 is not blocked

## 📚 Next Steps

- Read full [README.md](README.md) for detailed information
- Check [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API details
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Review [TROUBLESHOOTING.md](README.md#-troubleshooting) for common issues

## 💡 Tips

- Use sample X-ray images for testing (search online for "chest x-ray dataset")
- Images work best at 256x256 to 1024x1024 resolution
- Supported formats: PNG, JPG, JPEG
- Maximum recommended file size: 5MB

## 🎬 Video Tutorial

Coming soon! Watch this space for video walkthroughs.

## ❓ Need Help?

- Check [Troubleshooting](README.md#-troubleshooting) section
- Open an [issue](https://github.com/aavashlamichhane/Lung-Disease-Detection/issues)
- Read the [FAQ](README.md) in README.md

---

Happy analyzing! 🎉
