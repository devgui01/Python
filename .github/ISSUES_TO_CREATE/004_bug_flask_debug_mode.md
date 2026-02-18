---
title: "BUG: Flask debug mode enabled in production code in rest_api/main.py"
labels: ["bug", "security", "intermediate"]
assignees: []
---

## Bug Description

The Flask application in `rest_api/main.py` has debug mode enabled, which is a security risk and should not be used in production.

## Problem

```python
if __name__ == "__main__":
    app.run(debug=True)  # Debug mode is a security risk!
```

## Security Implications

Debug mode in Flask:
- Enables the interactive debugger that allows code execution
- Shows detailed error messages with stack traces
- Exposes sensitive application information
- Should NEVER be used in production

## Expected Behavior

Debug mode should be:
- Disabled by default
- Controlled via environment variable
- Only enabled during development

## Files Affected

- `rest_api/main.py`

## Suggested Fix

```python
import os

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1", "yes")
    app.run(debug=debug_mode)
```

Or simply disable it by default:

```python
if __name__ == "__main__":
    app.run(debug=False)
```

## Additional Recommendations

1. Add a `.env.example` file with `FLASK_DEBUG=False`
2. Update README to explain how to enable debug mode for development
3. Consider using a proper WSGI server (gunicorn) for production

## How to Test

1. Run the Flask application
2. Verify debug mode is disabled by default
3. Try triggering an error - should not show the interactive debugger
