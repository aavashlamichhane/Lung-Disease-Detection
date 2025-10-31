# Lung Disease Detection - Frontend

This is the frontend application for the Lung Disease Detection system, built with React 18 and Vite 5. It provides a modern, responsive user interface for uploading chest X-ray images and viewing pneumonia detection results.

## 🛠️ Technology Stack

- **React** 18.2.0 - UI library
- **Vite** 5.0.0 - Build tool and development server
- **React Router DOM** 6.20.0 - Client-side routing
- **Axios** 1.6.3 - HTTP client for API requests
- **Framer Motion** 10.16.16 - Animation library
- **ESLint** 8.53.0 - Code linting

## 📁 Project Structure

```
Frontend/
├── src/
│   ├── Components/
│   │   ├── pages/
│   │   │   ├── Home.jsx          # Landing page
│   │   │   ├── Result.jsx        # X-ray upload & results page
│   │   │   ├── AboutUs.jsx       # About page
│   │   │   └── ContactUs.jsx     # Contact page
│   │   ├── python_preds/         # ML model output images (created at runtime)
│   │   ├── NavBar.jsx            # Navigation component
│   │   ├── HowHelp.jsx           # Information component
│   │   └── WhatHelp.jsx          # Information component
│   ├── assets/                   # Static assets
│   ├── App.jsx                   # Main application component
│   ├── App.css                   # App styles
│   ├── main.jsx                  # Entry point
│   └── index.css                 # Global styles
├── public/
│   ├── LogoLDD.png              # Application logo
│   ├── undraw_doctors_*.png/svg # Illustrations
│   └── vite.svg                 # Vite logo
├── BackVideo.mp4                # Background video
├── video-background.mp4         # Alternative background video
├── index.html                   # HTML template
├── package.json                 # Dependencies
├── vite.config.js              # Vite configuration
└── .eslintrc.cjs               # ESLint configuration
```

## 🚀 Getting Started

### Prerequisites

- Node.js 16.x or higher
- npm 8.x or higher
- Backend server running on `http://127.0.0.1:8000`
- http-server for serving prediction images

### Installation

```bash
# Install dependencies
npm install

# Create directory for prediction outputs
mkdir -p src/Components/python_preds
```

### Development

```bash
# Start development server (localhost only)
npm run dev

# Start development server with network access
npm run host
```

The application will be available at:
- Local: `http://localhost:5173`
- Network: `http://<your-ip>:5173` (when using `npm run host`)

### Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

### Linting

```bash
# Run ESLint
npm run lint
```

## 🔌 API Integration

The frontend communicates with the Django backend API:

### Configuration

API endpoint is configured in `src/Components/pages/Result.jsx`:

```javascript
const response = await axios.post(
  "http://127.0.0.1:8000/upload",
  formData
);
```

To change the API URL, update this endpoint or create an environment variable:

```javascript
// .env file
VITE_API_URL=http://127.0.0.1:8000

// In code
const API_URL = import.meta.env.VITE_API_URL;
const response = await axios.post(`${API_URL}/upload`, formData);
```

### API Usage

The Result page handles image upload and displays results:

```javascript
// Upload flow
1. User selects image file
2. File is validated and previewed
3. FormData is created with image
4. POST request sent to /upload endpoint
5. Response contains prediction, confidence, and image URL
6. Results are displayed to user
```

## 📄 Pages

### Home (`/`)
- Landing page with project introduction
- Background video
- "Let's Begin" button to start analysis

### Result (`/result`)
- Image upload interface
- Real-time preview of uploaded image
- Analysis results display:
  - Prediction (Normal/Pneumonia)
  - Confidence score
  - Annotated image with bounding boxes

### About Us (`/AboutUs`)
- Project information
- Team details

### Contact Us (`/Contactus`)
- Contact form
- Support information

## 🎨 Styling

The application uses CSS modules for component-specific styling:

- `Home.css` - Landing page styles
- `Result.css` - Results page styles
- `NavBar.css` - Navigation styles
- `index.css` - Global styles

### Responsive Design

The UI is responsive and works across:
- Desktop (1920px+)
- Laptop (1366px - 1919px)
- Tablet (768px - 1365px)
- Mobile (< 768px)

## 🔧 Configuration

### Vite Configuration (`vite.config.js`)

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    host: true // Enable network access with --host flag
  }
})
```

### ESLint Configuration (`.eslintrc.cjs`)

The project uses ESLint with React-specific rules:
- React hooks validation
- React refresh compatibility
- Unused directives reporting

## 📦 Dependencies

### Production Dependencies

- **react**: ^18.2.0 - Core React library
- **react-dom**: ^18.2.0 - React DOM rendering
- **react-router-dom**: ^6.20.0 - Routing
- **axios**: ^1.6.3 - HTTP requests
- **framer-motion**: ^10.16.16 - Animations

### Development Dependencies

- **@vitejs/plugin-react**: ^4.2.0 - Vite React plugin
- **vite**: ^5.0.0 - Build tool
- **eslint**: ^8.53.0 - Linting
- **eslint-plugin-react**: ^7.33.2 - React linting
- **eslint-plugin-react-hooks**: ^4.6.0 - Hooks linting
- **eslint-plugin-react-refresh**: ^0.4.4 - Fast Refresh

## 🌐 HTTP Server for Images

The frontend requires an HTTP server to serve model output images:

```bash
cd src/Components/python_preds
http-server ./
```

This serves images at `http://127.0.0.1:8080/`

Images are accessed in the Result component:
```javascript
const imageUrl = `http://127.0.0.1:8080/${response.data.url}`;
```

## 🚨 Common Issues

### Issue: Images not displaying in results

**Solution:**
1. Ensure `python_preds` directory exists
2. Verify http-server is running on port 8080
3. Check backend is saving images to correct directory

### Issue: CORS errors

**Solution:**
1. Verify backend CORS settings allow `http://localhost:5173`
2. Check backend is running
3. Ensure request URL is correct

### Issue: Build fails

**Solution:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

## 🔮 Future Enhancements

- [ ] Real-time image processing feedback
- [ ] Image history and comparison
- [ ] Export results as PDF
- [ ] Multi-image batch upload
- [ ] User authentication
- [ ] Dark mode toggle
- [ ] Accessibility improvements
- [ ] Progressive Web App (PWA)
- [ ] Internationalization (i18n)

## 📝 Development Tips

### Adding New Pages

1. Create component in `src/Components/pages/`
2. Add route in `App.jsx`:
```javascript
<Route path="/new-page" element={<NewPage />} />
```
3. Add navigation link in `NavBar.jsx`

### API Request Pattern

Use this pattern for new API integrations:

```javascript
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

const handleRequest = async () => {
  setLoading(true);
  setError(null);
  
  try {
    const response = await axios.post(endpoint, data);
    // Handle success
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
};
```

### Performance Optimization

- Use React.memo() for expensive components
- Implement lazy loading for routes
- Optimize images (WebP format, proper sizing)
- Use Vite's code splitting features

## 📚 Resources

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [React Router Documentation](https://reactrouter.com/)
- [Axios Documentation](https://axios-http.com/)
- [Framer Motion Documentation](https://www.framer.com/motion/)

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for frontend development guidelines.

## 📄 License

This project is part of the Lung Disease Detection system and follows the same MIT License.

---

Built with ❤️ using React + Vite
