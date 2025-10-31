# Contributing to Lung Disease Detection

First off, thank you for considering contributing to Lung Disease Detection! It's people like you that make this project better for everyone. This document provides guidelines and steps for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Harassment, trolling, or discriminatory comments
- Publishing others' private information
- Unprofessional conduct

## Getting Started

### Prerequisites

Before contributing, make sure you have:
- Python 3.9+ installed
- Node.js 16+ and npm
- Git for version control
- A GitHub account
- Basic knowledge of Django and React

### First-Time Contributors

If you're new to open source contribution:
1. Look for issues labeled `good first issue` or `beginner-friendly`
2. Read through existing code to understand the structure
3. Don't hesitate to ask questions in issue comments

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**When filing a bug report, include:**
- **Clear title** - Descriptive and specific
- **Description** - What happened vs. what you expected
- **Steps to reproduce** - Detailed steps to recreate the issue
- **Environment** - OS, Python version, Node version, browser
- **Screenshots** - If applicable
- **Error messages** - Complete stack traces
- **Possible solution** - If you have ideas

**Example Bug Report:**

```markdown
**Title:** Model fails to load when path contains spaces

**Description:** 
The application crashes when model.h5 is in a directory path containing spaces.

**Steps to Reproduce:**
1. Place model.h5 in folder: `C:\My Projects\Lung Detection\`
2. Start Django server
3. Upload an image

**Expected:** Model loads successfully
**Actual:** FileNotFoundError

**Environment:**
- OS: Windows 11
- Python: 3.10.5
- Django: 5.0

**Error:**
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\My'
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.

**When suggesting an enhancement, include:**
- **Clear title** - What feature you want
- **Use case** - Why this feature is needed
- **Proposed solution** - How you envision it working
- **Alternatives** - Other approaches considered
- **Examples** - Similar features in other projects

### Code Contributions

1. **Find or create an issue** - Ensure the change is wanted
2. **Fork the repository**
3. **Create a branch** - Use descriptive branch names
4. **Make your changes** - Follow coding standards
5. **Test thoroughly** - Ensure nothing breaks
6. **Submit a pull request**

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/Lung-Disease-Detection.git
cd Lung-Disease-Detection
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv env

# Activate
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Set Up Frontend

```bash
cd Frontend
npm install
cd ..
```

### 4. Download Model

Download [model.h5](https://drive.google.com/file/d/15UNsIE3aIHudTiRVSqAT4S3AT3veFb2S/view?usp=sharing) to `Django/LD/`

### 5. Create Required Directories

```bash
mkdir -p Django/LD/media/downloads
mkdir -p Frontend/src/Components/python_preds
```

### 6. Run Database Migrations

```bash
cd Django/LD
python manage.py migrate
cd ../..
```

### 7. Configure Git

```bash
git remote add upstream https://github.com/aavashlamichhane/Lung-Disease-Detection.git
```

## Coding Standards

### Python Code Style (Django Backend)

Follow **PEP 8** guidelines:

```python
# Good
def calculate_confidence_score(prediction_mask, threshold=0.5):
    """
    Calculate confidence score from prediction mask.
    
    Args:
        prediction_mask (np.ndarray): Model output mask
        threshold (float): Confidence threshold
        
    Returns:
        float: Confidence score (0-100)
    """
    binary_mask = (prediction_mask > threshold).astype(np.uint8)
    confidence = np.max(prediction_mask) * 100
    return confidence

# Bad
def calc(p,t=0.5):
    b=(p>t).astype(np.uint8)
    c=np.max(p)*100
    return c
```

**Key Points:**
- Use 4 spaces for indentation
- Max line length: 100 characters
- Use snake_case for functions and variables
- Add docstrings to all functions
- Import order: standard library, third-party, local
- Add type hints where beneficial

### JavaScript Code Style (React Frontend)

Follow **Airbnb React Style Guide**:

```javascript
// Good
const UploadButton = ({ onFileSelect, disabled = false }) => {
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) return;
    
    setIsLoading(true);
    try {
      await onFileSelect(file);
    } catch (error) {
      console.error('Upload failed:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <button onClick={handleFileChange} disabled={disabled || isLoading}>
      {isLoading ? 'Uploading...' : 'Upload X-ray'}
    </button>
  );
};

// Bad
function Button(props) {
  var loading = false;
  function change(e) {
    props.onFileSelect(e.target.files[0]);
  }
  return <button onClick={change}>{props.text}</button>;
}
```

**Key Points:**
- Use 2 spaces for indentation
- Prefer functional components with hooks
- Use const/let, never var
- Use meaningful variable names
- Add PropTypes or TypeScript types
- Extract reusable logic into custom hooks

### CSS Style

```css
/* Good - BEM naming convention */
.upload-button {
  padding: 12px 24px;
  background-color: #4CAF50;
  border: none;
  border-radius: 4px;
}

.upload-button--disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.upload-button__icon {
  margin-right: 8px;
}

/* Bad */
.btn {
  padding: 12px 24px;
}
.disabled {
  opacity: 0.5;
}
```

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good commits
feat(frontend): add image preview before upload
fix(backend): resolve CORS issue for localhost
docs(readme): update installation instructions
refactor(model): optimize image preprocessing pipeline
test(api): add unit tests for upload endpoint

# Bad commits
update stuff
fixed bug
changes
```

### Commit Best Practices

1. **Use present tense** - "Add feature" not "Added feature"
2. **Be specific** - "Fix null pointer in image processing" not "Fix bug"
3. **One logical change per commit** - Don't bundle unrelated changes
4. **Reference issues** - "Closes #123" in commit body

## Pull Request Process

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Added tests for new features
- [ ] Updated documentation
- [ ] No unnecessary files committed
- [ ] Commits are well-organized

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Related Issue
Closes #(issue number)

## Testing
Describe testing performed:
- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] Tested on: [OS/Browser]

## Screenshots (if applicable)
[Add screenshots]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings
```

### Review Process

1. **Automated checks** - Must pass CI/CD
2. **Code review** - At least one approval needed
3. **Testing** - Reviewer tests changes
4. **Merge** - Maintainer merges PR

### After PR is Merged

1. Delete your feature branch
2. Update your fork:
```bash
git checkout main
git pull upstream main
git push origin main
```

## Testing Guidelines

### Running Tests

```bash
# Backend tests
cd Django/LD
python manage.py test

# Frontend tests
cd Frontend
npm test
```

### Writing Tests

**Django (Backend):**

```python
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile

class ImageUploadTests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_upload_valid_image(self):
        """Test uploading a valid X-ray image"""
        with open('test_images/sample_xray.jpg', 'rb') as img:
            response = self.client.post('/upload', {
                'image': SimpleUploadedFile('xray.jpg', img.read())
            })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('pred', response.json())
        self.assertIn('conf', response.json())
        
    def test_upload_no_image(self):
        """Test upload with no image"""
        response = self.client.post('/upload')
        self.assertEqual(response.status_code, 400)
```

**React (Frontend):**

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import UploadButton from './UploadButton';

describe('UploadButton', () => {
  test('renders upload button', () => {
    render(<UploadButton onFileSelect={jest.fn()} />);
    expect(screen.getByText(/upload/i)).toBeInTheDocument();
  });
  
  test('calls onFileSelect when file chosen', async () => {
    const mockOnFileSelect = jest.fn();
    render(<UploadButton onFileSelect={mockOnFileSelect} />);
    
    const file = new File(['xray'], 'xray.jpg', { type: 'image/jpeg' });
    const input = screen.getByLabelText(/upload/i);
    
    fireEvent.change(input, { target: { files: [file] } });
    
    expect(mockOnFileSelect).toHaveBeenCalledWith(file);
  });
});
```

### Test Coverage

Aim for:
- **Backend**: 80%+ coverage
- **Frontend**: 70%+ coverage
- **Critical paths**: 100% coverage

## Documentation

### Code Documentation

**Python:**
```python
def process_xray_image(image_path, model, threshold=0.5):
    """
    Process X-ray image and detect pneumonia.
    
    This function loads an X-ray image, preprocesses it, runs inference
    using the provided model, and extracts regions of interest.
    
    Args:
        image_path (str): Path to the X-ray image file
        model (keras.Model): Trained TensorFlow/Keras model
        threshold (float, optional): Confidence threshold. Defaults to 0.5.
    
    Returns:
        tuple: (prediction, confidence, annotated_image)
            - prediction (int): 0 for normal, 1 for pneumonia
            - confidence (float): Confidence score (0-100)
            - annotated_image (np.ndarray): Image with bounding boxes
    
    Raises:
        FileNotFoundError: If image_path doesn't exist
        ValueError: If image format is unsupported
    
    Example:
        >>> pred, conf, img = process_xray_image('xray.jpg', model)
        >>> print(f"Prediction: {pred}, Confidence: {conf}%")
    """
    pass
```

**JavaScript:**
```javascript
/**
 * Upload X-ray image to backend for analysis
 * 
 * @param {File} imageFile - The X-ray image file to upload
 * @param {string} endpoint - API endpoint URL
 * @returns {Promise<Object>} Analysis results
 * @property {number} returns.pred - Prediction (0=normal, 1=pneumonia)
 * @property {number} returns.conf - Confidence score (0-100)
 * @property {string} returns.url - URL of annotated image
 * 
 * @throws {Error} If upload fails or image is invalid
 * 
 * @example
 * const result = await uploadXRay(file, '/upload');
 * console.log(`Prediction: ${result.pred}`);
 */
async function uploadXRay(imageFile, endpoint) {
  // Implementation
}
```

### README Updates

When adding features, update:
- [ ] Features section
- [ ] Usage examples
- [ ] API documentation
- [ ] Troubleshooting (if applicable)

## Questions?

- **General questions**: Open a discussion on GitHub
- **Bug reports**: Create an issue
- **Security issues**: Email maintainer directly (don't open public issue)

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Project acknowledgments
- Release notes (for significant contributions)

---

Thank you for contributing to Lung Disease Detection! Your efforts help make medical AI more accessible. 🙏

