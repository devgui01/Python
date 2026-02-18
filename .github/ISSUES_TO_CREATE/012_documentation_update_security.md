---
title: "DOCUMENTATION: Update SECURITY.md with actual security policy"
labels: ["documentation", "security", "good first issue"]
assignees: []
---

## Documentation Issue

The current `SECURITY.md` file contains placeholder content that doesn't reflect the actual project state.

## Current Content

```markdown
## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.
```

## Problems

- Version numbers don't match this project (no releases yet)
- No actual reporting instructions
- Placeholder text not replaced
- Doesn't help users report security issues

## Expected Content

### Supported Versions

Since this is a learning project without formal releases:

```markdown
## Supported Versions

This is an educational project. We recommend always using the latest version from the main branch.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
```

### Reporting a Vulnerability

```markdown
## Reporting a Vulnerability

We take security seriously! If you discover a security issue, please follow these steps:

### How to Report

1. **Do NOT** create a public GitHub issue
2. Email us at: [security-email@example.com](mailto:security-email@example.com)
3. Or use GitHub's private vulnerability reporting (if enabled)

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Time

- We aim to respond within 48 hours
- We'll keep you updated on our progress
- We appreciate responsible disclosure

### Security Considerations for This Project

Since this is a learning project, be aware of:

- **Example code**: Some examples intentionally show insecure practices for educational purposes
- **Debug mode**: Some examples have debug mode enabled - not for production
- **Hardcoded values**: Examples may contain hardcoded secrets for demonstration

Please clearly indicate if you're reporting:
1. A real security vulnerability
2. An educational example that should be labeled as "insecure"
```

### Known Security Considerations

```markdown
## Known Security Considerations

This project contains educational examples that demonstrate both secure and insecure practices:

| File | Issue | Purpose |
|------|-------|---------|
| `rest_api/main.py` | Debug mode enabled | Teaching Flask setup |
| Various examples | Hardcoded secrets | Demonstration only |

⚠️ **Never use example code in production without reviewing security implications!**
```

## Files to Modify

- [ ] `SECURITY.md` (complete rewrite)

## Additional Recommendations

1. Add security contact email (or use GitHub's feature)
2. Enable private vulnerability reporting in repository settings
3. Add security notes to examples that demonstrate insecure practices
4. Create a `SECURITY_NOTES.md` in each directory with security-sensitive examples

## Benefits

- Clear process for reporting vulnerabilities
- Protects users from insecure example code
- Demonstrates security best practices
- Professional project maintenance
