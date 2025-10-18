# CITB4_Website
(was renamed to Phoenix simulation)

A modern, responsive website for CITB4(now Phoenix Simulation) - Thermal Simulation service. This website showcases thermal simulation capabilities, technology solutions, and provides contact information for potential clients.

## 🚀 Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional interface with smooth animations
- **Video Background**: Engaging landing page with video background
- **Component-based Structure**: Modular HTML components for easy maintenance
- **Legal Pages**: GDPR-compliant privacy policy and impressum
- **Live Development Server**: Hot-reload development environment

## 📁 Project Structure

```
CITB4_Website/
├── .claude/                    # Claude Code configuration
│   └── settings.local.json
├── .envrc                      # Environment configuration
├── .gitignore                  # Git ignore patterns
├── .python-version             # Python version specification
├── images/                     # Static image assets
│   ├── logo.png               # Company logo
│   ├── pic1.jpg               # Gallery image 1
│   ├── pic2.jpg               # Gallery image 2
│   └── pic3.jpg               # Gallery image 3
├── index.html                  # Main landing page
├── README.md                   # Project documentation
├── src/                        # Source code directory
│   ├── components/            # Reusable HTML components
│   │   ├── footer-subpages.html  # Footer for subpages
│   │   └── footer.html           # Main footer component
│   ├── pages/                 # Individual page templates
│   │   ├── contact.html       # Contact page
│   │   ├── datenschutz.html   # Privacy policy (German)
│   │   ├── impressum.html     # Legal notice (German)
│   │   └── technology.html    # Technology showcase
│   ├── serve.py              # Development server script
│   └── style.css             # Main stylesheet
└── video/                     # Video assets
    └── landing_vid.mp4       # Landing page background video
```

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with responsive design
- **Fonts**: Google Fonts (Inter family)
- **Development Server**: Python with livereload
- **Build System**: None (vanilla HTML/CSS/JS)
- **Package Manager**: uv (Python)

## 📋 Prerequisites

- Python 3.13+ (specified in `.python-version`)
- uv package manager
- Modern web browser
- Git for version control

## 🚀 Getting Started

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CITB4_Website
   ```

2. **Set up Python environment**
   ```bash
   # Using uv (recommended)
   uv python install 3.13
   uv sync
   ```

3. **Start the development server**
   ```bash
   cd src
   uv run serve.py
   ```
   or
   ```bash
   python src/serve.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:5500` (or the port specified by the server)

### Development Workflow

1. **Live Reload**: The development server automatically reloads when files change
2. **File Organization**: Keep components in `src/components/` and pages in `src/pages/`
3. **Asset Management**: Place images in `images/` and videos in `video/`
4. **Styling**: All styles are in `src/style.css` - consider component-specific CSS for larger projects

## 📱 Responsive Design

The website is fully responsive and optimized for:
- **Desktop**: 1920px+ (Full HD and above)
- **Laptop**: 1366px - 1919px
- **Tablet**: 768px - 1365px
- **Mobile**: 320px - 767px

### Breakpoints
```css
/* Mobile First Approach */
/* Base styles: Mobile (320px+) */

@media (min-width: 768px) {
  /* Tablet styles */
}

@media (min-width: 1024px) {
  /* Desktop styles */
}

@media (min-width: 1440px) {
  /* Large desktop styles */
}
```

## 🖼️ Image Guidelines

### Slideshow Images
- **Ideal Dimensions**: 1920x1080 pixels (16:9 aspect ratio)
- **Format**: JPG or PNG
- **File Size**: Optimized for web (< 500KB recommended)
- **Quality**: High resolution for crisp display on all devices

### Logo Requirements
- **Format**: PNG with transparent background
- **Dimensions**: Scalable vector or high-resolution raster
- **Usage**: Header navigation and footer

### Gallery Images
- **Aspect Ratio**: Consistent across all images
- **Resolution**: Minimum 1200px width
- **Optimization**: Use tools like ImageOptim or TinyPNG

## 🎨 Design System

### Color Palette
```css
:root {
  --primary-color: #your-primary-color;
  --secondary-color: #your-secondary-color;
  --accent-color: #your-accent-color;
  --text-primary: #333333;
  --text-secondary: #666666;
  --background: #ffffff;
}
```

### Typography
- **Primary Font**: Inter (Google Fonts)
- **Weights Available**: 400 (Regular), 700 (Bold)
- **Fallback**: system-ui, -apple-system, sans-serif

### Component Structure
```html
<!-- Example component structure -->
<section class="component-name">
  <div class="container">
    <div class="component-content">
      <!-- Content here -->
    </div>
  </div>
</section>
```

## 📄 Pages Overview

### Main Pages
- **index.html**: Landing page with video background and service overview
- **contact.html**: Contact details and company information
- **technology.html**: Technology showcase and capabilities

### Legal Pages
- **impressum.html**: German legal notice (required for German businesses)
- **datenschutz.html**: Privacy policy and GDPR compliance

## 🔧 Development Commands

```bash
# Start development server
uv run src/serve.py

# Install dependencies
uv sync

# Update Python version
uv python install <version>

# Run with specific Python version
uv run --python 3.13 src/serve.py
```

## 🌐 Deployment

### Static Hosting Options
- **Netlify**: Drag and drop deployment
- **Vercel**: Git-based deployment
- **GitHub Pages**: Direct from repository
- **Firebase Hosting**: Google Cloud integration

### Build Process
1. **Optimize Images**: Compress all images for web delivery
2. **Minify CSS**: Optional for production builds
3. **Test Responsiveness**: Verify all breakpoints work correctly
4. **Validate HTML**: Use W3C validator
5. **Check Links**: Ensure all internal/external links work

### Deployment Checklist
- [ ] All images optimized
- [ ] Videos compressed and web-ready
- [ ] Contact details functional
- [ ] Legal pages updated
- [ ] Meta tags and SEO optimized
- [ ] Analytics tracking added (if required)
- [ ] Performance tested (Lighthouse)

## 🔍 SEO Optimization

### Meta Tags
Each page should include:
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Your page description">
<meta name="keywords" content="thermal, simulation, engineering">
<meta name="author" content="Phoenix simulation">
```

### Performance Optimization
- **Image Formats**: Use modern formats (WebP, AVIF) with fallbacks
- **Lazy Loading**: Implement for images and videos
- **Caching**: Set appropriate cache headers
- **CDN**: Consider using a CDN for assets

## 📞 Support and Contact

For technical questions or support regarding this website:
- **Development Issues**: Create an issue in the repository
- **Content Updates**: Contact the content team
- **Hosting Questions**: Refer to your hosting provider's documentation

## 📝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Code Style Guidelines
- **HTML**: Use semantic markup and proper indentation
- **CSS**: Follow BEM methodology for class naming
- **File Naming**: Use kebab-case for all files
- **Comments**: Comment complex CSS and any JavaScript functionality

## 📊 Analytics and Monitoring

### Performance Metrics
- **Page Load Time**: < 3 seconds
- **First Contentful Paint**: < 1.5 seconds
- **Cumulative Layout Shift**: < 0.1
- **Mobile Performance Score**: > 90


## 🔒 Security Considerations

- **HTTPS**: Always use HTTPS in production
- **Content Security Policy**: Implement CSP headers
- **Form Security**: Validate and sanitize form inputs
- **Privacy**: Comply with GDPR and local privacy laws

## 📚 Additional Resources

- [HTML5 Specification](https://html.spec.whatwg.org/)
- [CSS3 Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Web Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Google Fonts Documentation](https://developers.google.com/fonts)

---

**Last Updated**: 13 August 2025  
**Version**: 1.0.0  
