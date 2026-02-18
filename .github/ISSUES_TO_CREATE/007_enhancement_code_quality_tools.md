---
title: "ENHANCEMENT: Add code quality tools (linters, formatters, type checkers)"
labels: ["enhancement", "code quality", "intermediate"]
assignees: []
---

## Enhancement Description

The codebase lacks consistent code style and quality checks. Adding automated tools would improve readability, catch bugs early, and teach learners about professional Python development practices.

## Current Issues

- Inconsistent naming conventions across files
- Missing type hints in many files
- No automated formatting
- No linting to catch common errors
- Inconsistent docstrings

## Proposed Tools

### 1. Code Formatter: Black
```bash
pip install black
```
Automatically formats code to follow PEP 8.

### 2. Linter: Ruff (or Flake8)
```bash
pip install ruff
```
Fast linting to catch errors and style issues.

### 3. Type Checker: mypy
```bash
pip install mypy
```
Static type checking to catch type-related bugs.

### 4. Import Sorter: isort (or use Ruff)
```bash
pip install isort
```
Automatically sorts imports alphabetically.

## Implementation Plan

### Phase 1: Configuration Files

1. **pyproject.toml** - Central configuration:
   ```toml
   [tool.black]
   line-length = 100
   target-version = ['py310']
   
   [tool.ruff]
   line-length = 100
   select = ["E", "F", "W", "I", "N", "D", "UP"]
   
   [tool.mypy]
   python_version = "3.10"
   warn_return_any = true
   warn_unused_configs = true
   ```

2. **.editorconfig** - Editor settings:
   ```editorconfig
   root = true
   
   [*]
   charset = utf-8
   end_of_line = lf
   indent_size = 4
   indent_style = space
   ```

### Phase 2: Pre-commit Hooks

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      
  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
      
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.14
    hooks:
      - id: ruff
```

### Phase 3: Fix Existing Code

Run tools on entire codebase:
```bash
black .
ruff check --fix .
mypy --ignore-missing-imports .
```

### Phase 4: CI/CD Integration

Add to GitHub Actions workflow:
```yaml
- name: Code Quality
  run: |
    black --check .
    ruff check .
    mypy --ignore-missing-imports .
```

## Files to Create/Modify

- [ ] `pyproject.toml` (create)
- [ ] `.pre-commit-config.yaml` (create)
- [ ] `.editorconfig` (create)
- [ ] `requirement.txt` (add dev dependencies)
- [ ] `.github/workflows/code-quality.yml` (create)
- [ ] All Python files (fix formatting)

## Benefits for Learners

- Learn industry-standard tools
- Understand importance of code quality
- See examples of clean, consistent code
- Catch bugs before running code

## Documentation

Update CONTRIBUTING.md with:
- How to install and run tools
- Code style guidelines
- Pre-commit setup instructions
