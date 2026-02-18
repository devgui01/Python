# Contributing to Python Mastery

Thanks for wanting to contribute! Here's how to help improve this project.

## Ways to Contribute

### Report Bugs
- Open an issue with `[BUG]` in the title
- Describe what's broken and what you expected
- Include code examples if you can

### Suggest Features
- Open an issue with `[FEATURE]` in the title
- Explain what you'd like to see and why it's useful

### Submit Code Changes

1. **Fork the repository**

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for tricky parts
   - Test your code works

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

---

## Code Style

### Naming Conventions
- **Variables/Functions:** `lowercase_with_underscores`
- **Classes:** `PascalCase`
- **Constants:** `UPPERCASE`

### Comments
- Explain **why** something is done, not just what
- Use `#` for inline comments
- Add docstrings for functions and classes

### Example
```python
# Good
def calculate_circle_area(radius: float) -> float:
    """Calculate circle area from radius."""
    return 3.14159 * radius ** 2

# Avoid
def calc(r):
    return 3.14159 * r * r
```

---

## Commit Messages

Use this format:
```
type: short description

Optional details
```

**Types:**
- `feat:` New feature or example
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Formatting only
- `refactor:` Code restructuring
- `test:` Adding tests

**Examples:**
```
feat: add list comprehension examples
fix: correct typo in calculator.py
docs: update README with quickstart guide
```

---

## Questions?

Open an issue or reach out to the maintainers.

Thanks for helping make this project better! 🐍
