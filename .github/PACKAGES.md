# GitHub Packages Configuration

This repository uses GitHub Packages for distributing Python learning resources.

## Package Types

### 1. Python Package (PyPI)
**Status:** Planned  
**Registry:** GitHub Packages  
**Format:** Wheel, Source Distribution

```bash
# Install from GitHub Packages
pip install git+https://github.com/hackdartstorm/Python.git@v1.0.0
```

### 2. Docker Container
**Status:** Planned  
**Registry:** ghcr.io  
**Format:** Container Image

```bash
# Pull Docker image
docker pull ghcr.io/hackdartstorm/python-learning:latest
```

### 3. Documentation Site
**Status:** Planned  
**Registry:** GitHub Pages  
**Format:** Static Site

## Publishing

### Python Package

```bash
# Build package
python -m build

# Upload to GitHub Packages
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### Docker Image

```bash
# Build image
docker build -t ghcr.io/hackdartstorm/python-learning:latest .

# Push to registry
docker push ghcr.io/hackdartstorm/python-learning:latest
```

## Versioning

Follows Semantic Versioning (SemVer):
- **Major:** Breaking changes
- **Minor:** New features (backward compatible)
- **Patch:** Bug fixes (backward compatible)

## Access

### Public Access
All packages are publicly available.

### Authentication
For publishing:
```bash
# Login to GitHub Packages
echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin
```

## Package Contents

### Python Package
- Learning materials
- Example code
- Exercise templates
- Documentation

### Docker Image
- Python 3.11 runtime
- All dependencies
- Example code
- Development tools

## Support

- **Issues:** https://github.com/hackdartstorm/Python/issues
- **Discussions:** https://github.com/hackdartstorm/Python/discussions

---

**Last Updated:** February 2026
