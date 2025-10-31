# Changelog

All notable changes to the Lung Disease Detection project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- User authentication system
- Batch image processing
- Export results as PDF reports
- User dashboard with history
- Mobile application
- Docker containerization
- Cloud deployment support

## [1.0.0] - 2024-10-31

### Added
- Initial release of Lung Disease Detection system
- Django backend with TensorFlow/Keras model integration
- React + Vite frontend with modern UI
- U-Net based deep learning model for pneumonia detection
- Image segmentation with bounding box visualization
- Confidence score calculation
- Real-time image upload and analysis
- CORS-enabled REST API
- Responsive design for all devices
- Background video on landing page
- Navigation system with multiple pages (Home, Result, About, Contact)
- Support for PNG, JPG, JPEG image formats

### Features
- **AI-Powered Detection**: Pneumonia detection from chest X-rays
- **Visual Feedback**: Bounding boxes around infected regions
- **Confidence Scoring**: Percentage confidence for each prediction
- **User-Friendly Interface**: Simple upload and view results workflow
- **Fast Processing**: Quick analysis and response

### Documentation
- Comprehensive README with installation and usage instructions
- API documentation with examples
- Contributing guidelines
- Frontend-specific documentation
- Project structure overview
- Troubleshooting guide

### Technical Details
- **Backend**: Django 5.0, TensorFlow 2.15, Python 3.9+
- **Frontend**: React 18.2, Vite 5.0, Axios 1.6
- **Model**: U-Net architecture with IoU + BCE loss
- **Image Processing**: OpenCV, Scikit-image, Matplotlib
- **API**: RESTful endpoint for image upload

## [0.1.0] - Initial Development

### Added
- Basic project structure
- Model training infrastructure
- Initial UI prototype
- Core image processing pipeline

---

## Version History

### Versioning Scheme

- **Major version** (X.0.0): Breaking changes, major new features
- **Minor version** (0.X.0): New features, backward compatible
- **Patch version** (0.0.X): Bug fixes, minor improvements

### Release Notes Template

```markdown
## [Version] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes to existing functionality

### Deprecated
- Features marked for removal

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security improvements
```

---

**Note**: This changelog will be updated with each new release. For detailed commit history, see the [Git log](https://github.com/aavashlamichhane/Lung-Disease-Detection/commits/).
