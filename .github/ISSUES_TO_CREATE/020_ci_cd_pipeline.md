---
title: "ENHANCEMENT: Set up comprehensive CI/CD pipeline"
labels: ["enhancement", "ci/cd", "advanced"]
assignees: []
---

## Enhancement Description

The current CI/CD setup only has a basic conda workflow. We need a comprehensive pipeline that runs tests, checks code quality, builds documentation, and deploys examples.

## Current State

Only one workflow exists:
- `.github/workflows/python-package-conda.yml` - Basic conda setup

Missing:
- Automated testing
- Code quality checks
- Documentation building
- Deployment
- Security scanning

## Proposed CI/CD Pipeline

### 1. Test Workflow

```yaml
# .github/workflows/test.yml
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirement.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: |
          pytest tests/ --cov=. --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
```

### 2. Code Quality Workflow

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install linters
        run: |
          pip install black ruff mypy

      - name: Run Black (formatting)
        run: black --check .

      - name: Run Ruff (linting)
        run: ruff check .

      - name: Run mypy (type checking)
        run: mypy --ignore-missing-imports .
```

### 3. Documentation Workflow

```yaml
# .github/workflows/docs.yml
name: Documentation

on:
  push:
    branches: [main]
    paths:
      - "**.md"
      - "docs/**"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Check Markdown links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          use-quiet-mode: "yes"
          config-file: ".github/link-check-config.json"

      - name: Validate code blocks
        run: |
          # Add script to validate Python code blocks in docs
          python scripts/validate_docs.py
```

### 4. Security Scan Workflow

```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: "0 0 * * 0"  # Weekly

jobs:
  security:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install safety
        run: pip install safety

      - name: Check dependencies
        run: safety check -r requirement.txt

      - name: Run Bandit (security linter)
        run: |
          pip install bandit
          bandit -r . -ll
```

### 5. Example Validation Workflow

```yaml
# .github/workflows/validate-examples.yml
name: Validate Examples

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirement.txt

      - name: Run basic examples
        run: |
          python basics/01_introduction/01_hello_world.py
          python basics/02_variables_types/01_arithmetic.py
          # Add more examples

      - name: Validate FastAPI
        run: |
          timeout 30 uvicorn fastapi.main:app --host 0.0.0.0 &
          sleep 5
          curl http://localhost:8000/
          curl http://localhost:8000/campaigns

      - name: Validate Flask
        run: |
          timeout 30 python rest_api/main.py &
          sleep 5
          curl http://localhost:5000/
          curl http://localhost:5000/destinations
```

### 6. Auto-label PR Workflow

```yaml
# .github/workflows/auto-label.yml
name: Auto Label PR

on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  label:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/labeler@v4
        with:
          repo-token: "${{ secrets.GITHUB_TOKEN }}"
```

### 7. Labeler Configuration

```yaml
# .github/labeler.yml
documentation:
  - "**/*.md"
  - "docs/**/*"

code-quality:
  - "**/*.py"

ci-cd:
  - ".github/workflows/**"
  - ".github/labeler.yml"

examples:
  - "basics/**/*"
  - "fastapi/**/*"
  - "rest_api/**/*"

llm:
  - "llm_fundamentals/**/*"
```

### 8. Deployment Workflow (Optional)

```yaml
# .github/workflows/deploy.yml
name: Deploy Examples

on:
  push:
    branches: [main]
    tags:
      - "v*"

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/_build/html

      - name: Deploy API examples
        # Add deployment steps for cloud platform
```

## Files to Create

- [ ] `.github/workflows/test.yml`
- [ ] `.github/workflows/code-quality.yml`
- [ ] `.github/workflows/docs.yml`
- [ ] `.github/workflows/security.yml`
- [ ] `.github/workflows/validate-examples.yml`
- [ ] `.github/workflows/auto-label.yml`
- [ ] `.github/labeler.yml`
- [ ] `.github/link-check-config.json`
- [ ] `scripts/validate_docs.py`

## Badges to Add

Update README.md with:

```markdown
![Tests](https://github.com/username/python/actions/workflows/test.yml/badge.svg)
![Code Quality](https://github.com/username/python/actions/workflows/code-quality.yml/badge.svg)
![Security](https://github.com/username/python/actions/workflows/security.yml/badge.svg)
![Coverage](https://codecov.io/gh/username/python/branch/main/graph/badge.svg)
```

## Benefits

- ✅ Automated testing
- ✅ Catch bugs before merge
- ✅ Consistent code quality
- ✅ Security scanning
- ✅ Documentation validation
- ✅ Example verification
- ✅ Professional workflow
