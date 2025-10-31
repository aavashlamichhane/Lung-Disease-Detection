# Architecture Documentation

This document provides detailed information about the Lung Disease Detection system architecture, design decisions, and technical implementation.

## System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE                              │
│                    (React 18 + Vite 5 Frontend)                      │
│                                                                       │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐   │
│  │    Home    │  │   Result   │  │  About Us  │  │  Contact   │   │
│  │    Page    │  │    Page    │  │    Page    │  │    Page    │   │
│  └────────────┘  └────────────┘  └────────────┘  └────────────┘   │
│         │              │                                              │
│         └──────────────┴─────────────────┐                          │
│                                           │                          │
│                                    ┌──────▼──────┐                  │
│                                    │   Axios     │                  │
│                                    │ HTTP Client │                  │
│                                    └──────┬──────┘                  │
└───────────────────────────────────────────┼──────────────────────────┘
                                            │
                                    HTTP/JSON (CORS)
                                            │
┌───────────────────────────────────────────▼──────────────────────────┐
│                      BACKEND API SERVER                               │
│                      (Django 5.0 REST API)                            │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                      API Endpoints                              │ │
│  │                                                                  │ │
│  │  POST /upload                                                    │ │
│  │   - Accepts multipart/form-data                                 │ │
│  │   - Validates image file                                        │ │
│  │   - Returns JSON response                                       │ │
│  └────────────────────┬───────────────────────────────────────────┘ │
│                       │                                               │
│                       ▼                                               │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                   Request Handler                               │ │
│  │   (home/views.py - upload function)                             │ │
│  │                                                                  │ │
│  │   1. Receive image file                                         │ │
│  │   2. Save to media/downloads/                                   │ │
│  │   3. Call prediction pipeline                                   │ │
│  │   4. Generate annotated image                                   │ │
│  │   5. Return results                                             │ │
│  └────────────────────┬───────────────────────────────────────────┘ │
└────────────────────────┼──────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  MACHINE LEARNING PIPELINE                           │
│                   (TensorFlow 2.15 + Keras)                          │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  Step 1: Image Preprocessing                                    │ │
│  │   - Load image with PIL                                         │ │
│  │   - Convert to grayscale if needed                              │ │
│  │   - Resize to 256x256                                           │ │
│  │   - Normalize pixel values                                      │ │
│  │   - Add batch dimension                                         │ │
│  └────────────────────┬───────────────────────────────────────────┘ │
│                       │                                               │
│                       ▼                                               │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  Step 2: Model Inference (U-Net)                                │ │
│  │                                                                  │ │
│  │   Input: [batch_size, 256, 256, 1]                              │ │
│  │                                                                  │ │
│  │   ┌─────────────────────────────────────┐                       │ │
│  │   │  Encoder (Downsampling Path)        │                       │ │
│  │   │   - Conv2D + BatchNorm + ReLU       │                       │ │
│  │   │   - MaxPooling                      │                       │ │
│  │   │   - Feature extraction              │                       │ │
│  │   └─────────────┬───────────────────────┘                       │ │
│  │                 │                                                 │ │
│  │                 ▼                                                 │ │
│  │   ┌─────────────────────────────────────┐                       │ │
│  │   │  Bottleneck                         │                       │ │
│  │   │   - Dense feature representation    │                       │ │
│  │   └─────────────┬───────────────────────┘                       │ │
│  │                 │                                                 │ │
│  │                 ▼                                                 │ │
│  │   ┌─────────────────────────────────────┐                       │ │
│  │   │  Decoder (Upsampling Path)          │                       │ │
│  │   │   - Conv2DTranspose (upsampling)    │                       │ │
│  │   │   - Concatenate with encoder        │                       │ │
│  │   │   - Conv2D + BatchNorm + ReLU       │                       │ │
│  │   └─────────────┬───────────────────────┘                       │ │
│  │                 │                                                 │ │
│  │                 ▼                                                 │ │
│  │   Output: [batch_size, 256, 256, 1]                              │ │
│  │   (Segmentation mask with probability values 0-1)                │ │
│  │                                                                  │ │
│  └────────────────────┬───────────────────────────────────────────┘ │
│                       │                                               │
│                       ▼                                               │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  Step 3: Post-Processing                                        │ │
│  │                                                                  │ │
│  │   a) Threshold mask at 0.5                                      │ │
│  │      binary_mask = (prediction > 0.5)                           │ │
│  │                                                                  │ │
│  │   b) Connected Components Analysis                              │ │
│  │      - Label connected regions (scikit-image)                   │ │
│  │      - Extract region properties                                │ │
│  │                                                                  │ │
│  │   c) Bounding Box Generation                                    │ │
│  │      - For each region: (x, y, width, height)                   │ │
│  │                                                                  │ │
│  │   d) Confidence Calculation                                     │ │
│  │      - Max probability in prediction                            │ │
│  │      - Convert to percentage                                    │ │
│  │                                                                  │ │
│  │   e) Classification                                             │ │
│  │      - Positive: any region detected                            │ │
│  │      - Negative: no regions detected                            │ │
│  │                                                                  │ │
│  └────────────────────┬───────────────────────────────────────────┘ │
│                       │                                               │
│                       ▼                                               │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  Step 4: Visualization                                          │ │
│  │                                                                  │ │
│  │   - Plot original image (matplotlib)                            │ │
│  │   - Overlay bounding boxes (blue rectangles)                    │ │
│  │   - Add title (positive/negative)                               │ │
│  │   - Save annotated image                                        │ │
│  │   - Crop to remove borders                                      │ │
│  │                                                                  │ │
│  └────────────────────┬───────────────────────────────────────────┘ │
└────────────────────────┼──────────────────────────────────────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │   Response   │
                  │              │
                  │  pred: 0/1   │
                  │  conf: 0-100 │
                  │  url: image  │
                  └──────────────┘
```

## Component Details

### Frontend Architecture

#### Component Hierarchy
```
App (BrowserRouter)
├── Route: / → Home
├── Route: /result → Result
├── Route: /AboutUs → AboutUs
└── Route: /Contactus → ContactUs

Shared Components:
├── NavBar (navigation menu)
├── HowHelp (information section)
└── WhatHelp (information section)
```

#### State Management
- **Local State**: React useState hooks
- **No Global State**: Simple app doesn't require Redux/Context
- **Form State**: Managed in Result component

#### Data Flow
```
User Action (File Upload)
    │
    ▼
handleImageChange()
    │
    ├─→ FileReader (preview image)
    │
    └─→ FormData creation
         │
         ▼
    axios.post('/upload')
         │
         ▼
    Response handling
         │
         ├─→ setPred() (set prediction)
         ├─→ setConf() (set confidence)
         └─→ setResultImage() (set image URL)
              │
              ▼
         Render results
```

### Backend Architecture

#### Django Project Structure
```
LD/ (project)
├── LD/ (settings)
│   ├── settings.py (configuration)
│   ├── urls.py (URL routing)
│   ├── wsgi.py (WSGI config)
│   └── asgi.py (ASGI config)
│
└── home/ (app)
    ├── views.py (API logic)
    ├── models.py (database models - minimal)
    ├── admin.py (admin config)
    └── tests.py (unit tests)
```

#### Request Flow
```
HTTP Request
    │
    ▼
Django Middleware
    │
    ├─→ CORS Headers
    ├─→ CSRF Protection (disabled for API)
    └─→ Session Management
         │
         ▼
URL Router (urls.py)
    │
    ▼
View Function (upload)
    │
    ├─→ Validate request
    ├─→ Save file
    ├─→ Process with ML
    └─→ Return JSON
         │
         ▼
HTTP Response
```

### Machine Learning Pipeline

#### Model Architecture (U-Net)

```
Input: 256×256×1
    │
    ▼
┌─────────────────┐
│  Encoder Block 1│  64 filters
│  Conv2D + BN    │
└────────┬────────┘
         │ ─────────────────┐ (skip connection)
         ▼                  │
    MaxPooling2D           │
         │                  │
         ▼                  │
┌─────────────────┐        │
│  Encoder Block 2│  128 filters
│  Conv2D + BN    │        │
└────────┬────────┘        │
         │ ─────────────┐  │
         ▼              │  │
    MaxPooling2D       │  │
         │              │  │
         ▼              │  │
┌─────────────────┐    │  │
│  Encoder Block 3│  256 filters
│  Conv2D + BN    │    │  │
└────────┬────────┘    │  │
         │ ──────────┐ │  │
         ▼           │ │  │
    MaxPooling2D    │ │  │
         │           │ │  │
         ▼           │ │  │
┌─────────────────┐ │ │  │
│   Bottleneck    │ 512 filters
│  Conv2D + BN    │ │ │  │
└────────┬────────┘ │ │  │
         │           │ │  │
         ▼           │ │  │
  UpSampling2D      │ │  │
         │           │ │  │
         ├───────────┘ │  │
         ▼              │  │
┌─────────────────┐   │  │
│  Decoder Block 3│ 256 filters
│ Concat + Conv2D │   │  │
└────────┬────────┘   │  │
         │              │  │
         ▼              │  │
  UpSampling2D         │  │
         │              │  │
         ├──────────────┘  │
         ▼                 │
┌─────────────────┐       │
│  Decoder Block 2│ 128 filters
│ Concat + Conv2D │       │
└────────┬────────┘       │
         │                 │
         ▼                 │
  UpSampling2D            │
         │                 │
         ├─────────────────┘
         ▼
┌─────────────────┐
│  Decoder Block 1│ 64 filters
│ Concat + Conv2D │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Output Layer   │ 1 filter
│  Conv2D+Sigmoid │
└────────┬────────┘
         │
         ▼
Output: 256×256×1
(Probability map: 0-1)
```

#### Loss Function

```python
def iou_loss(y_true, y_pred):
    """
    Intersection over Union (Jaccard) loss
    
    IoU = (Intersection) / (Union)
        = (TP) / (TP + FP + FN)
    """
    intersection = sum(y_true * y_pred)
    union = sum(y_true) + sum(y_pred) - intersection
    iou = (intersection + 1) / (union + 1)
    return 1 - iou

def iou_bce_loss(y_true, y_pred):
    """
    Combined loss function
    
    Loss = 0.5 * BCE + 0.5 * IoU_Loss
    
    - BCE: Pixel-wise binary cross-entropy
    - IoU: Region overlap optimization
    """
    bce = binary_crossentropy(y_true, y_pred)
    iou = iou_loss(y_true, y_pred)
    return 0.5 * bce + 0.5 * iou
```

## Data Flow Diagram

### Image Upload and Processing

```
┌──────────────┐
│   User       │
│  Selects     │
│  X-ray Image │
└──────┬───────┘
       │
       ▼
┌──────────────────────┐
│  Frontend Validation │
│  - File type check   │
│  - Size check        │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Create FormData     │
│  append('image', file)│
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  HTTP POST Request   │
│  /upload endpoint    │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Django receives     │
│  request.FILES       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Save to             │
│  media/downloads/    │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Load Model          │
│  model.h5            │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Preprocess Image    │
│  - Resize 256×256    │
│  - Normalize         │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Model Prediction    │
│  Get segmentation    │
│  mask                │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Post-process        │
│  - Threshold         │
│  - Find regions      │
│  - Calc confidence   │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Generate Annotated  │
│  Image with boxes    │
└──────┬───────────────┘
       │
       ├─→ Save to python_preds/
       │
       ▼
┌──────────────────────┐
│  Return JSON         │
│  {pred, conf, url}   │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Frontend receives   │
│  and displays results│
└──────────────────────┘
```

## Database Schema

Currently uses SQLite with minimal database usage:

```sql
-- Django default tables
- auth_user
- auth_group
- auth_permission
- django_session
- django_content_type
- django_migrations

-- No custom models currently defined
-- All processing is stateless
```

## File Storage

```
Project Root
│
├── Django/LD/
│   ├── media/                    # Media files (gitignored)
│   │   └── downloads/            # Uploaded images (temporary)
│   ├── model.h5                  # ML model (gitignored, 90MB)
│   └── db.sqlite3                # Database (gitignored)
│
└── Frontend/
    └── src/Components/
        └── python_preds/         # Model outputs (gitignored)
```

## Security Architecture

### Current Security Measures

1. **CORS Protection**
   - Allowed origins specified
   - No wildcard origins

2. **File Validation**
   - File type checking
   - File size limits

3. **Django Security**
   - CSRF tokens (for forms)
   - SQL injection prevention (ORM)
   - XSS protection headers

### Security Limitations (Development)

⚠️ **Not production-ready** ⚠️

Missing in current version:
- Authentication/Authorization
- Rate limiting
- HTTPS enforcement
- Input sanitization
- File content validation
- Secure secret key management

## Performance Considerations

### Bottlenecks

1. **Model Inference**
   - Time: ~2-5 seconds per image
   - CPU-intensive (no GPU support)
   - Largest bottleneck

2. **Image Processing**
   - Matplotlib rendering
   - File I/O operations

3. **Network Transfer**
   - Image upload time
   - Depends on file size and connection

### Optimization Opportunities

1. **GPU Acceleration**
   ```python
   # Enable GPU support
   import tensorflow as tf
   gpus = tf.config.list_physical_devices('GPU')
   if gpus:
       tf.config.experimental.set_memory_growth(gpus[0], True)
   ```

2. **Model Optimization**
   - Convert to TensorFlow Lite
   - Use quantization
   - Reduce model size

3. **Caching**
   - Cache model in memory
   - Redis for result caching

4. **Async Processing**
   - Celery for background tasks
   - WebSocket for real-time updates

## Scalability

### Current Limitations

- Single-threaded processing
- No load balancing
- No horizontal scaling
- SQLite (not suitable for production)

### Scaling Recommendations

1. **Database**: PostgreSQL + connection pooling
2. **Web Server**: Gunicorn + Nginx
3. **Caching**: Redis
4. **Queue**: Celery + RabbitMQ
5. **Storage**: S3 or cloud storage
6. **Container**: Docker + Kubernetes

## Technology Choices

### Why Django?
- Rapid development
- Built-in ORM
- Easy integration with Python ML libraries
- Good documentation

### Why React + Vite?
- Fast development server
- Modern build tool
- Hot module replacement
- Component-based architecture

### Why U-Net?
- State-of-art for medical image segmentation
- Skip connections preserve spatial information
- Proven performance on biomedical images
- Efficient training with limited data

### Why TensorFlow/Keras?
- Extensive ecosystem
- Pre-trained models available
- Good documentation
- Production-ready

## Future Architecture

### Planned Improvements

```
┌─────────────────────────────────────────┐
│          Load Balancer (Nginx)          │
└─────────────────┬───────────────────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
┌─────────────────┐ ┌─────────────────┐
│  Django Server  │ │  Django Server  │
│   (Gunicorn)    │ │   (Gunicorn)    │
└────────┬────────┘ └────────┬────────┘
         │                    │
         └──────────┬─────────┘
                    ▼
         ┌─────────────────────┐
         │  Message Queue      │
         │  (RabbitMQ/Redis)   │
         └──────────┬──────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
┌─────────────────┐   ┌─────────────────┐
│  Celery Worker  │   │  Celery Worker  │
│  (ML Processing)│   │  (ML Processing)│
└─────────────────┘   └─────────────────┘
         │                     │
         └──────────┬──────────┘
                    ▼
         ┌─────────────────────┐
         │   PostgreSQL DB     │
         └─────────────────────┘
                    │
         ┌─────────────────────┐
         │    Redis Cache      │
         └─────────────────────┘
                    │
         ┌─────────────────────┐
         │  S3 Storage         │
         │  (Images & Models)  │
         └─────────────────────┘
```

---

*Last Updated: October 31, 2024*
