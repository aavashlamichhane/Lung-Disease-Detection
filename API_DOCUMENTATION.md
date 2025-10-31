# API Documentation

This document provides detailed information about the Lung Disease Detection API endpoints, request/response formats, and integration examples.

## 📋 Table of Contents

- [Overview](#overview)
- [Base URL](#base-url)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Request Examples](#request-examples)
- [Response Codes](#response-codes)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)
- [Integration Examples](#integration-examples)

## Overview

The Lung Disease Detection API is a RESTful API that provides pneumonia detection capabilities for chest X-ray images. The API accepts image uploads and returns predictions with confidence scores and annotated images showing detected regions.

### API Version
**Current Version:** 1.0

### Content Types
- **Request:** `multipart/form-data`
- **Response:** `application/json`

## Base URL

### Development
```
http://127.0.0.1:8000
```

### Production
```
https://your-domain.com
```

## Authentication

**Current Version:** No authentication required (development)

**Future Versions:** Will implement token-based authentication (JWT)

## Endpoints

### 1. Upload and Analyze X-ray Image

Uploads a chest X-ray image and returns pneumonia detection results.

#### Endpoint
```
POST /upload
```

#### Request

**Content-Type:** `multipart/form-data`

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| image | File | Yes | Chest X-ray image file (PNG, JPG, JPEG) |

**Constraints:**
- **Supported formats:** PNG, JPG, JPEG
- **Maximum file size:** 10 MB (recommended: < 5 MB)
- **Recommended resolution:** 256x256 to 1024x1024 pixels
- **Color mode:** Grayscale or RGB (will be converted to grayscale)

#### Response

**Success Response:**

**Code:** `200 OK`

**Content:**
```json
{
  "pred": 1,
  "url": "patient_xray_001.jpg",
  "conf": 87.52
}
```

**Response Fields:**

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| pred | Integer | 0 or 1 | Prediction result:<br>• `0` = Normal (no pneumonia detected)<br>• `1` = Pneumonia (infection detected) |
| url | String | - | Filename of the annotated image with bounding boxes.<br>Image is saved in `Frontend/src/Components/python_preds/` |
| conf | Float | 0.0 - 100.0 | Confidence score of the prediction in percentage |

**Error Response:**

**Code:** `400 Bad Request`

**Content:**
```json
{
  "status": "error"
}
```

**Possible reasons:**
- No image file provided
- Invalid file format
- File corrupted or unreadable

#### cURL Example

```bash
curl -X POST http://127.0.0.1:8000/upload \
  -H "Content-Type: multipart/form-data" \
  -F "image=@/path/to/chest_xray.jpg"
```

**Example Response:**
```json
{
  "pred": 1,
  "url": "chest_xray.jpg",
  "conf": 92.35
}
```

#### Python Example

```python
import requests

# Upload image
url = "http://127.0.0.1:8000/upload"
files = {'image': open('chest_xray.jpg', 'rb')}

response = requests.post(url, files=files)

if response.status_code == 200:
    result = response.json()
    prediction = "Pneumonia" if result['pred'] == 1 else "Normal"
    confidence = result['conf']
    annotated_image = result['url']
    
    print(f"Prediction: {prediction}")
    print(f"Confidence: {confidence:.2f}%")
    print(f"Annotated image: {annotated_image}")
else:
    print("Error:", response.json())
```

#### JavaScript/Axios Example

```javascript
import axios from 'axios';

async function analyzeXRay(imageFile) {
  const formData = new FormData();
  formData.append('image', imageFile);

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/upload',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
    );

    const { pred, conf, url } = response.data;
    
    return {
      prediction: pred === 1 ? 'Pneumonia' : 'Normal',
      confidence: conf,
      annotatedImageUrl: url
    };
  } catch (error) {
    console.error('Error analyzing X-ray:', error);
    throw error;
  }
}

// Usage
const fileInput = document.getElementById('xray-input');
const file = fileInput.files[0];

analyzeXRay(file).then(result => {
  console.log('Prediction:', result.prediction);
  console.log('Confidence:', result.confidence.toFixed(2) + '%');
});
```

#### React Hook Example

```javascript
import { useState } from 'react';
import axios from 'axios';

function useXRayAnalysis() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const analyzeImage = async (imageFile) => {
    setLoading(true);
    setError(null);
    
    const formData = new FormData();
    formData.append('image', imageFile);

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/upload',
        formData
      );

      setResult({
        prediction: response.data.pred === 1 ? 'Pneumonia' : 'Normal',
        confidence: response.data.conf,
        imageUrl: response.data.url
      });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { analyzeImage, loading, result, error };
}

// Component usage
function XRayUploader() {
  const { analyzeImage, loading, result, error } = useXRayAnalysis();

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      analyzeImage(file);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} accept="image/*" />
      {loading && <p>Analyzing...</p>}
      {result && (
        <div>
          <p>Prediction: {result.prediction}</p>
          <p>Confidence: {result.confidence.toFixed(2)}%</p>
        </div>
      )}
      {error && <p>Error: {error}</p>}
    </div>
  );
}
```

## Response Codes

### HTTP Status Codes

| Code | Description | Meaning |
|------|-------------|---------|
| 200 | OK | Request successful, image analyzed |
| 400 | Bad Request | Invalid request (missing image, wrong format) |
| 500 | Internal Server Error | Server error during processing |
| 503 | Service Unavailable | Server overloaded or under maintenance |

### Application Response Codes

The API uses standard HTTP status codes. Application-specific errors are returned in the response body:

**Success:**
```json
{
  "pred": 0,
  "url": "image_name.jpg",
  "conf": 95.67
}
```

**Error:**
```json
{
  "status": "error"
}
```

## Error Handling

### Common Errors

#### 1. Missing Image File

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/upload
```

**Response:**
```json
{
  "status": "error"
}
```

**Solution:** Include image file in the request

#### 2. Invalid File Format

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/upload \
  -F "image=@document.pdf"
```

**Response:**
```json
{
  "status": "error"
}
```

**Solution:** Use PNG, JPG, or JPEG image formats

#### 3. File Too Large

**Error:** Connection timeout or 413 Payload Too Large

**Solution:** Resize image to < 5 MB before upload

#### 4. CORS Error (Browser)

**Error:** 
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solution:** 
- Ensure request is from allowed origin (http://localhost:5173)
- Check `CORS_ALLOWED_ORIGINS` in Django settings

### Error Handling Best Practices

```javascript
async function uploadWithErrorHandling(imageFile) {
  // Validate file size
  const maxSize = 5 * 1024 * 1024; // 5 MB
  if (imageFile.size > maxSize) {
    throw new Error('File too large. Maximum size is 5 MB.');
  }

  // Validate file type
  const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
  if (!validTypes.includes(imageFile.type)) {
    throw new Error('Invalid file type. Use JPG or PNG.');
  }

  const formData = new FormData();
  formData.append('image', imageFile);

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/upload',
      formData,
      {
        timeout: 30000, // 30 second timeout
        validateStatus: (status) => status < 500
      }
    );

    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error('Upload failed');
    }
  } catch (error) {
    if (error.code === 'ECONNABORTED') {
      throw new Error('Request timeout. Please try again.');
    } else if (error.response) {
      throw new Error(`Server error: ${error.response.status}`);
    } else if (error.request) {
      throw new Error('No response from server. Check your connection.');
    } else {
      throw new Error('Upload failed: ' + error.message);
    }
  }
}
```

## Rate Limiting

**Current Version:** No rate limiting

**Recommended for Production:**
- **Rate:** 10 requests per minute per IP
- **Burst:** 20 requests
- **Reset:** Every minute

**Headers (future):**
```
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1635724800
```

## CORS Configuration

### Allowed Origins

The API accepts requests from:
- `http://localhost:5173` (Development frontend)

### CORS Headers

**Request Headers Allowed:**
- `Content-Type`
- `Authorization` (future)

**Response Headers Exposed:**
- `Content-Type`

### Modifying CORS Settings

Edit `Django/LD/LD/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://your-production-domain.com",
]

# For development (not recommended for production):
# CORS_ALLOW_ALL_ORIGINS = True
```

## Integration Examples

### Complete React Component

```javascript
import React, { useState } from 'react';
import axios from 'axios';

function XRayAnalyzer() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileSelect = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Validate file
    if (!file.type.startsWith('image/')) {
      setError('Please select an image file');
      return;
    }

    if (file.size > 5 * 1024 * 1024) {
      setError('File size must be less than 5 MB');
      return;
    }

    setSelectedFile(file);
    setError(null);

    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => setPreview(e.target.result);
    reader.readAsDataURL(file);
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/upload',
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
          timeout: 30000
        }
      );

      if (response.data.status === 'error') {
        throw new Error('Analysis failed');
      }

      setResult({
        prediction: response.data.pred === 1 ? 'Pneumonia Detected' : 'Normal',
        confidence: response.data.conf,
        imageUrl: `http://127.0.0.1:8080/${response.data.url}`
      });
    } catch (err) {
      setError(err.message || 'Failed to analyze image');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="xray-analyzer">
      <h2>Chest X-Ray Analysis</h2>
      
      <input
        type="file"
        accept="image/*"
        onChange={handleFileSelect}
        disabled={loading}
      />

      {preview && (
        <div className="preview">
          <h3>Selected Image:</h3>
          <img src={preview} alt="Preview" style={{ maxWidth: '400px' }} />
        </div>
      )}

      <button
        onClick={handleUpload}
        disabled={!selectedFile || loading}
      >
        {loading ? 'Analyzing...' : 'Analyze X-Ray'}
      </button>

      {error && (
        <div className="error">
          <p>Error: {error}</p>
        </div>
      )}

      {result && (
        <div className="result">
          <h3>Analysis Result:</h3>
          <p><strong>Prediction:</strong> {result.prediction}</p>
          <p><strong>Confidence:</strong> {result.confidence.toFixed(2)}%</p>
          <div className="annotated-image">
            <h4>Annotated Image:</h4>
            <img src={result.imageUrl} alt="Annotated" style={{ maxWidth: '400px' }} />
          </div>
        </div>
      )}
    </div>
  );
}

export default XRayAnalyzer;
```

### Python CLI Tool

```python
#!/usr/bin/env python3
"""
Command-line tool for X-ray analysis
Usage: python analyze_xray.py <image_path>
"""

import sys
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:8000/upload"

def analyze_xray(image_path):
    """Analyze X-ray image using the API"""
    
    # Validate file
    if not Path(image_path).exists():
        print(f"Error: File not found: {image_path}")
        return None
    
    # Upload image
    with open(image_path, 'rb') as f:
        files = {'image': f}
        
        try:
            response = requests.post(API_URL, files=files, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get('status') == 'error':
                print("Error: Analysis failed")
                return None
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_xray.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    result = analyze_xray(image_path)
    
    if result:
        prediction = "Pneumonia" if result['pred'] == 1 else "Normal"
        confidence = result['conf']
        
        print("\n" + "="*50)
        print("X-RAY ANALYSIS RESULT")
        print("="*50)
        print(f"Prediction: {prediction}")
        print(f"Confidence: {confidence:.2f}%")
        print(f"Annotated image: {result['url']}")
        print("="*50 + "\n")

if __name__ == '__main__':
    main()
```

**Usage:**
```bash
python analyze_xray.py patient_001.jpg
```

## Future API Enhancements

Planned features for future versions:

### Authentication
```
POST /api/auth/login
POST /api/auth/logout
POST /api/auth/refresh
```

### Batch Processing
```
POST /api/batch-upload
GET /api/batch-upload/{batch_id}
```

### History
```
GET /api/history
GET /api/history/{analysis_id}
DELETE /api/history/{analysis_id}
```

### User Management
```
POST /api/users/register
GET /api/users/profile
PUT /api/users/profile
```

---

## Support

For API support:
- **Issues:** [GitHub Issues](https://github.com/aavashlamichhane/Lung-Disease-Detection/issues)
- **Documentation:** [README.md](README.md)

## Changelog

### v1.0 (Current)
- Initial API release
- Single image upload and analysis
- Pneumonia detection with confidence scores
- Bounding box generation

---

*Last Updated: October 2024*
