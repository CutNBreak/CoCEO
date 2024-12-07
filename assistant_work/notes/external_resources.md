# External Resources

## Overview
This document catalogs external tools, libraries, dependencies, and references used by the system.

## Core Dependencies

### AI/ML Libraries
| Library | Version | Purpose | Status |
|---------|---------|---------|---------|
| PyTorch | 2.0+ | Vision processing | Production |
| OpenCV | 4.8+ | Image processing | Production |
| Tesseract | 5.0+ | OCR processing | Production |
| Moondream | Latest | Vision model | Production |

### Browser Automation
| Library | Version | Purpose | Status |
|---------|---------|---------|---------|
| Selenium | 4.0+ | Browser control | Production |
| Playwright | Latest | Modern automation | Evaluation |
| Puppeteer | Latest | Chrome automation | Evaluation |
| ChromeDriver | Latest | Chrome interface | Production |

### System Integration
| Library | Version | Purpose | Status |
|---------|---------|---------|---------|
| PyAutoGUI | 0.9+ | UI automation | Production |
| Pillow | 10.0+ | Image handling | Production |
| psutil | 5.9+ | Process management | Production |
| pywin32 | Latest | Windows API | Production |

## Development Tools

### Testing Tools
| Tool | Version | Purpose | Status |
|------|---------|---------|---------|
| pytest | 7.0+ | Testing framework | Production |
| coverage.py | Latest | Coverage analysis | Production |
| pytest-cov | Latest | Coverage reporting | Production |
| pytest-mock | Latest | Test mocking | Production |

### Code Quality
| Tool | Version | Purpose | Status |
|------|---------|---------|---------|
| pylint | Latest | Code linting | Production |
| black | Latest | Code formatting | Production |
| mypy | Latest | Type checking | Production |
| isort | Latest | Import sorting | Production |

### Documentation
| Tool | Version | Purpose | Status |
|------|---------|---------|---------|
| Sphinx | Latest | Doc generation | Production |
| MkDocs | Latest | Doc hosting | Evaluation |
| pdoc | Latest | API docs | Production |
| Docusaurus | Latest | Doc website | Evaluation |

## External Services

### Cloud Services
| Service | Purpose | Status |
|---------|---------|---------|
| AWS S3 | File storage | Evaluation |
| Azure Blob | Backup storage | Evaluation |
| GCP Vision | Vision API | Evaluation |
| AWS Lambda | Serverless | Evaluation |

### CI/CD Services
| Service | Purpose | Status |
|---------|---------|---------|
| GitHub Actions | CI/CD pipeline | Production |
| SonarCloud | Code analysis | Evaluation |
| CodeCov | Coverage tracking | Evaluation |
| Dependabot | Dependency updates | Production |

## Documentation References

### Official Documentation
- [Python Documentation](https://docs.python.org/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [OpenCV Documentation](https://docs.opencv.org/)

### Design Patterns
- [Python Design Patterns](https://python-patterns.guide/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

### Best Practices
- [Python Best Practices](https://gist.github.com/sloria/7001839)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [Code Review Guidelines](https://google.github.io/eng-practices/review/)

## Community Resources

### Forums & Discussion
- [Python Discord](https://discord.gg/python)
- [PyTorch Forums](https://discuss.pytorch.org/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Reddit r/Python](https://www.reddit.com/r/Python/)

### Learning Resources
- [Real Python](https://realpython.com/)
- [Python Weekly](https://www.pythonweekly.com/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

## Installation & Setup

### Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Testing Environment
```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run tests
pytest tests/
pytest --cov=src tests/

# Run linting
pylint src/
black src/
mypy src/
```

## Version Control

### Git Configuration
```bash
# Configure git hooks
git config core.hooksPath .githooks/

# Configure git flow
git flow init
git flow feature start feature_name
git flow feature finish feature_name
```

## Related Documents
- analysis/technology_assessment.md
- notes/architecture_notes.md
- notes/dependency_map.md
- notes/glossary.md
