---
title: "BUG: Function named 'sum' performs division instead of addition in basics/09_error_handling/01_try_except.py"
labels: ["bug", "good first issue"]
assignees: []
---

## Bug Description

The function `sum()` in `basics/09_error_handling/01_try_except.py` performs division (`a / b`) instead of addition, which is misleading and incorrect based on the function name.

## Problem

```python
def sum(a: int, b: int) -> int:
    result = a / b  # This is division, not addition!
    return result
```

## Expected Behavior

A function named `sum` should perform addition, or it should be renamed to reflect its actual operation (e.g., `divide`).

## Current Behavior

- Function named `sum` performs division
- Type hint says it returns `int` but division returns `float`
- This is confusing for learners

## Files Affected

- `basics/09_error_handling/01_try_except.py`

## Suggested Fix

Option 1 - Fix the operation to match the name:
```python
def sum(a: int, b: int) -> int:
    result = a + b
    return result
```

Option 2 - Rename the function to match the operation:
```python
def divide(a: int, b: int) -> float:
    result = a / b
    return result
```

Option 2 is recommended since the error handling is specifically for division by zero.

## How to Test

1. Run the script and enter `10` and `2`
2. Current output: `5.0` (division)
3. Expected output (if keeping name): `12` (addition)
