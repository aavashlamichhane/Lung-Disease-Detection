# Lung Disease Detection

<div align="center">

**An AI-powered web application for detecting pneumonia and lung infections from chest X-ray images**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18.2-61dafb.svg)](https://reactjs.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange.svg)](https://www.tensorflow.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Information](#-model-information)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

> **📚 Complete Documentation**: See [DOCS_INDEX.md](DOCS_INDEX.md) for a full list of available documentation including quick start guides, API reference, architecture details, and more.

---

## 🔍 Overview

Lung Disease Detection is a comprehensive web application that leverages deep learning to detect pneumonia and other lung infections from chest X-ray images. The system uses a U-Net based convolutional neural network for semantic segmentation, providing both classification (normal vs. pneumonia) and localization (bounding boxes around infected regions) of lung abnormalities.

### Key Highlights

- **Accurate Detection**: Deep learning model trained on medical imaging data
- **Visual Feedback**: Highlights infected regions with bounding boxes
- **Confidence Scores**: Provides prediction confidence percentages
- **User-Friendly Interface**: Modern, responsive web interface built with React
- **Fast Processing**: Real-time image analysis and results

---

## ✨ Features

- **🔬 AI-Powered Analysis**: Uses TensorFlow/Keras deep learning model for pneumonia detection
- **📊 Semantic Segmentation**: U-Net architecture for precise region identification
- **🎯 Confidence Scoring**: Displays prediction confidence for each diagnosis
- **🖼️ Visual Indicators**: Bounding boxes highlight infected lung regions
- **📱 Responsive Design**: Works seamlessly across desktop and mobile devices
- **⚡ Fast Processing**: Quick image upload and analysis
- **🔒 Secure**: CORS-enabled backend for secure cross-origin requests
- **📈 Detailed Results**: Side-by-side comparison of input and annotated output images

---

## 🛠️ Technology Stack

### Frontend
- **React** 18.2 - UI framework
- **Vite** 5.0 - Build tool and dev server
- **React Router** 6.20 - Client-side routing
- **Axios** 1.6.3 - HTTP client
- **Framer Motion** 10.16 - Animation library

### Backend
- **Django** 5.0 - Web framework
- **Django REST Framework** - API development
- **Django CORS Headers** - Cross-origin resource sharing

### Machine Learning
- **TensorFlow** 2.15 - Deep learning framework
- **Keras** 2.15 - High-level neural networks API
- **NumPy** 1.26.2 - Numerical computing
- **OpenCV** 4.9.0 - Image processing
- **Scikit-image** 0.22.0 - Image segmentation
- **Matplotlib** 3.8.2 - Visualization

### Additional Libraries
- **Pandas** 2.1.4 - Data manipulation
- **Pillow** 10.1.0 - Image handling

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Client (Browser)                      │
│                     React + Vite Frontend                    │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP Requests
                       │ (Image Upload)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                     Django Backend Server                    │
│                         (Port 8000)                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              /upload API Endpoint                    │   │
│  └────────────────────┬────────────────────────────────┘   │
│                       │                                      │
│                       ▼                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         TensorFlow/Keras Model (model.h5)           │   │
│  │         - U-Net Architecture                         │   │
│  │         - Semantic Segmentation                      │   │
│  │         - IoU + BCE Loss Function                    │   │
│  └────────────────────┬────────────────────────────────┘   │
│                       │                                      │
│                       ▼                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │        Image Processing Pipeline                     │   │
│  │        - Resize & Normalize                          │   │
│  │        - Predict Segmentation Mask                   │   │
│  │        - Apply Connected Components                  │   │
│  │        - Generate Bounding Boxes                     │   │
│  │        - Calculate Confidence Score                  │   │
│  └────────────────────┬────────────────────────────────┘   │
└────────────────────────┼────────────────────────────────────┘
                         │
                         ▼
                  ┌────────────────┐
                  │  JSON Response  │
                  │  + Annotated    │
                  │    Image        │
                  └────────────────┘
```

### Workflow

1. **User uploads chest X-ray image** through the React frontend
2. **Frontend sends POST request** to Django backend `/upload` endpoint
3. **Backend receives and saves image** to media/downloads folder
4. **Deep learning model processes image**:
   - Resizes image to 256x256
   - Predicts segmentation mask
   - Applies connected components analysis
   - Generates bounding boxes around infected regions
   - Calculates confidence score
5. **Backend generates annotated image** with bounding boxes
6. **Response sent back to frontend** with:
   - Prediction result (Normal/Pneumonia)
   - Confidence score
   - URL to annotated image
7. **Frontend displays results** to user

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.9 or higher
- **Node.js** 16.x or higher
- **npm** 8.x or higher
- **http-server** (install globally: `npm install -g http-server`)
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### System Requirements

- **RAM**: Minimum 8GB (16GB recommended for model inference)
- **Storage**: At least 2GB free space
- **OS**: Windows, macOS, or Linux

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/aavashlamichhane/Lung-Disease-Detection.git
cd Lung-Disease-Detection
```

### Step 2: Download the Pre-trained Model

Download the trained model file from Google Drive:

**[Download model.h5](https://drive.google.com/file/d/15UNsIE3aIHudTiRVSqAT4S3AT3veFb2S/view?usp=sharing)**

Save `model.h5` in the Django backend directory:
```
Lung-Disease-Detection/Django/LD/model.h5
```

### Step 3: Set Up Python Environment

#### Option A: Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Using Conda

```bash
conda create -n lung-detection python=3.9
conda activate lung-detection
pip install -r requirements.txt
```

### Step 4: Set Up Django Backend

```bash
# Navigate to Django directory
cd Django/LD

# Create required directories
mkdir -p media/downloads

# Run migrations
python manage.py migrate

# (Optional) Create superuser for admin access
python manage.py createsuperuser
```

### Step 5: Set Up React Frontend

```bash
# Navigate to Frontend directory
cd ../../Frontend

# Install dependencies
npm install

# Create directory for prediction outputs
mkdir -p src/Components/python_preds
```

### Step 6: Install http-server (if not already installed)

```bash
npm install -g http-server
```

---

## 💻 Usage

The application requires three concurrent processes to run. Open **three separate terminal windows/tabs**:

### Terminal 1: Start Django Backend

```bash
cd Django/LD
python manage.py runserver
```

The backend will start at `http://127.0.0.1:8000/`

### Terminal 2: Start React Frontend

```bash
cd Frontend
npm run dev
```

The frontend will start at `http://localhost:5173/`

**For LAN access:**
```bash
npm run host
```

### Terminal 3: Start HTTP Server for Prediction Images

```bash
cd Frontend/src/Components/python_preds
http-server ./
```

This serves the model output images at `http://127.0.0.1:8080/`

### Accessing the Application

1. Open your browser and navigate to `http://localhost:5173/`
2. Click on "Let's Begin" to access the detection page
3. Upload a chest X-ray image (PNG, JPG, JPEG formats supported)
4. Wait for the model to process the image
5. View results:
   - **Prediction**: Normal or Pneumonia
   - **Confidence Score**: Percentage confidence of the prediction
   - **Annotated Image**: Original image with bounding boxes around infected regions (if any)

---

## 📁 Project Structure

```
Lung-Disease-Detection/
│
├── Django/                          # Backend Django application
│   └── LD/                          # Django project
│       ├── LD/                      # Project settings
│       │   ├── settings.py          # Django configuration
│       │   ├── urls.py              # URL routing
│       │   ├── wsgi.py              # WSGI configuration
│       │   └── asgi.py              # ASGI configuration
│       ├── home/                    # Main Django app
│       │   ├── views.py             # API views and ML logic
│       │   ├── models.py            # Database models
│       │   ├── admin.py             # Admin configuration
│       │   └── tests.py             # Unit tests
│       ├── media/                   # User uploaded images
│       │   └── downloads/           # Temporary storage
│       ├── model.h5                 # Trained ML model (download separately)
│       ├── manage.py                # Django management script
│       └── db.sqlite3               # SQLite database
│
├── Frontend/                        # React frontend application
│   ├── src/
│   │   ├── Components/
│   │   │   ├── pages/
│   │   │   │   ├── Home.jsx         # Landing page
│   │   │   │   ├── Result.jsx       # Detection page
│   │   │   │   ├── AboutUs.jsx      # About page
│   │   │   │   └── ContactUs.jsx    # Contact page
│   │   │   ├── python_preds/        # Model output images
│   │   │   ├── NavBar.jsx           # Navigation component
│   │   │   ├── HowHelp.jsx          # Info component
│   │   │   └── WhatHelp.jsx         # Info component
│   │   ├── App.jsx                  # Main app component
│   │   ├── main.jsx                 # App entry point
│   │   └── index.css                # Global styles
│   ├── public/                      # Static assets
│   ├── package.json                 # Node dependencies
│   ├── vite.config.js               # Vite configuration
│   └── index.html                   # HTML template
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── .gitignore                       # Git ignore rules
└── Lung Disease Detection Report.docx.pdf  # Project report
```

---

## 🧠 Model Information

### Architecture: U-Net

The model uses a **U-Net architecture**, specifically designed for biomedical image segmentation. U-Net consists of:

- **Encoder (Contracting Path)**: Captures context through successive convolution and pooling layers
- **Decoder (Expanding Path)**: Enables precise localization through upsampling and concatenation
- **Skip Connections**: Combines high-resolution features from encoder with upsampled features

### Model Specifications

- **Input Size**: 256x256 grayscale images
- **Output**: Binary segmentation mask (256x256)
- **Loss Function**: Combined IoU (Jaccard) + Binary Cross-Entropy
  - `Loss = 0.5 × BCE + 0.5 × IoU_Loss`
- **Optimizer**: Adam with cosine annealing learning rate
- **Metrics**: Mean IoU (Intersection over Union)

### Training Details

- **Dataset**: Medical chest X-ray images with pneumonia annotations
- **Image Augmentation**: Horizontal flipping
- **Batch Size**: 32
- **Image Size**: 256×256 pixels
- **Learning Rate**: Cosine annealing (0.001 initial)
- **Epochs**: 25

### Prediction Process

1. **Preprocessing**: Resize and normalize input image
2. **Inference**: Generate segmentation mask
3. **Post-processing**:
   - Threshold mask at 0.5 confidence
   - Apply connected components analysis
   - Extract bounding boxes from regions
   - Calculate overall confidence score
4. **Classification**:
   - **Positive (Pneumonia)**: If any pixels exceed threshold
   - **Negative (Normal)**: If no significant regions detected

### Performance

The model provides:
- **Binary Classification**: Normal vs. Pneumonia
- **Localization**: Bounding boxes around infected regions
- **Confidence Score**: Percentage certainty of prediction

---

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### Upload and Analyze X-ray Image

**Endpoint:** `/upload`

**Method:** `POST`

**Content-Type:** `multipart/form-data`

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| image | File | Yes | Chest X-ray image (PNG, JPG, JPEG) |

**Example Request (cURL):**

```bash
curl -X POST http://127.0.0.1:8000/upload \
  -H "Content-Type: multipart/form-data" \
  -F "image=@/path/to/xray.jpg"
```

**Example Request (JavaScript/Axios):**

```javascript
const formData = new FormData();
formData.append('image', file);

const response = await axios.post(
  'http://127.0.0.1:8000/upload',
  formData,
  {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }
);
```

**Success Response:**

**Code:** `200 OK`

**Content:**
```json
{
  "pred": 1,
  "url": "xray_image_name.jpg",
  "conf": 87.5
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| pred | Integer | Prediction result: `0` = Normal, `1` = Pneumonia |
| url | String | Filename of the annotated image with bounding boxes |
| conf | Float | Confidence score (0-100) |

**Error Response:**

**Code:** `400 Bad Request`

**Content:**
```json
{
  "status": "error"
}
```

### CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:5173` (React dev server)

To modify allowed origins, edit `Django/LD/LD/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    # Add your custom origins here
]
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Module Not Found Error

**Problem:** `ModuleNotFoundError: No module named 'X'`

**Solution:**
```bash
# Ensure virtual environment is activated
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt
```

#### 2. Model File Not Found

**Problem:** `FileNotFoundError: model.h5 not found`

**Solution:**
- Ensure `model.h5` is placed in `Django/LD/` directory
- Verify the file is not corrupted (should be ~90MB)
- Re-download from the Google Drive link if necessary

#### 3. Port Already in Use

**Problem:** `Error: That port is already in use`

**Solution for Django (Port 8000):**
```bash
# Find process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9

# Or run on different port:
python manage.py runserver 8001
```

**Solution for React (Port 5173):**
```bash
# Kill process on port 5173
# Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:5173 | xargs kill -9
```

#### 4. CORS Error

**Problem:** `Access to XMLHttpRequest blocked by CORS policy`

**Solution:**
- Verify Django CORS settings in `settings.py`
- Ensure `django-cors-headers` is installed
- Check that frontend URL is in `CORS_ALLOWED_ORIGINS`

#### 5. Image Not Displaying in Results

**Problem:** Annotated image doesn't show in results

**Solution:**
- Ensure `python_preds` folder exists in `Frontend/src/Components/`
- Verify http-server is running on port 8080
- Check file permissions on the python_preds directory

#### 6. TensorFlow Import Error

**Problem:** `ImportError: Could not import tensorflow`

**Solution:**
```bash
# For Windows with Intel CPU:
pip install tensorflow-intel==2.15.0

# For macOS with Apple Silicon:
pip install tensorflow-macos==2.15.0
pip install tensorflow-metal

# For Linux/others:
pip install tensorflow==2.15.0
```

#### 7. Memory Error During Prediction

**Problem:** `MemoryError` or system slowdown during prediction

**Solution:**
- Close unnecessary applications
- Reduce image size before upload
- Increase system swap space
- Consider using a machine with more RAM (16GB recommended)

#### 8. Database Migration Issues

**Problem:** Database errors or migration failures

**Solution:**
```bash
cd Django/LD

# Delete database and migrations
rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
```

---

## 🤝 Contributing

We welcome contributions to improve the Lung Disease Detection system! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation as needed
4. **Test your changes**
   - Ensure all existing functionality works
   - Add tests for new features
5. **Commit your changes**
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/YourFeatureName
   ```
7. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features (e.g., additional disease detection)
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🧪 Additional test coverage
- 🌐 Internationalization

### Code Style Guidelines

**Python (Backend):**
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Maximum line length: 100 characters

**JavaScript (Frontend):**
- Use ES6+ syntax
- Follow Airbnb React style guide
- Use functional components with hooks
- Use meaningful component and variable names

### Reporting Issues

Found a bug or have a suggestion? Please open an issue with:
- Clear, descriptive title
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Screenshots (if applicable)
- System information (OS, Python version, etc.)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ⚠️ Provided "as is" without warranty

---

## 🙏 Acknowledgments

- **TensorFlow/Keras Team** - For the amazing deep learning framework
- **U-Net Authors** - For the groundbreaking medical image segmentation architecture
- **React & Vite Teams** - For excellent frontend development tools
- **Django Team** - For the robust web framework
- **Medical Imaging Community** - For making datasets and research available
- **Open Source Contributors** - For the numerous libraries that made this project possible

---

## 📞 Contact

**Project Maintainer:** Aavash Lamichhane

**Repository:** [github.com/aavashlamichhane/Lung-Disease-Detection](https://github.com/aavashlamichhane/Lung-Disease-Detection)

For questions, suggestions, or support, please:
- Open an issue on GitHub
- Contact through the repository

---

## 🔮 Future Enhancements

- [ ] Support for multiple lung disease types (TB, COVID-19, etc.)
- [ ] Batch processing of multiple images
- [ ] Export results as PDF reports
- [ ] User authentication and history tracking
- [ ] REST API with authentication
- [ ] Docker containerization
- [ ] Cloud deployment (AWS, GCP, Azure)
- [ ] Mobile application (React Native)
- [ ] Model retraining interface
- [ ] Integration with PACS systems
- [ ] Multi-language support

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ by Aavash Lamichhane

</div>
