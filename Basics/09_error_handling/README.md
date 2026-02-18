# 09 Error Handling

Handle exceptions gracefully in Python.

## Files

| File | Description |
|------|-------------|
| `exception_handling_try_except.py` | Try-except basics |
| `exception_raise_example.py` | Raise exceptions |
| `handle_zero_division.py` | Handle division by zero |

## Topics Covered
- Try-except blocks
- Multiple exceptions
- Raise keyword
- Else clause
- Finally clause
- Custom exceptions

## Quick Start
```bash
python exception_handling_try_except.py
python handle_zero_division.py
```

## Example
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always runs")
```
