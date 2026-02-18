---
title: "ENHANCEMENT: Improve error messages for better learning"
labels: ["enhancement", "user experience", "good first issue"]
assignees: []
---

## Enhancement Description

Many error messages in the codebase are generic or unhelpful for learners. Improving error messages will help beginners understand what went wrong and how to fix it.

## Current State

Examples of poor error messages:

```python
# basics/09_error_handling/01_try_except.py
except ZeroDivisionError:
    print("A Number Can't be Divide by Zero")  # Grammatically incorrect

except ValueError:
    print("Enter a Valid Number!")  # Not specific enough

# basics/03_control_flow/08_pattern_hollow_square.py
# No error handling at all

# rest_api/main.py
return jsonify({"error": "Destination not found!"}), 404
# Doesn't explain what to do next
```

## Problems

- Grammatical errors
- Not actionable
- Don't explain the "why"
- No suggestions for fixing
- Inconsistent format

## Solution

Improve all error messages to be:
1. Grammatically correct
2. Specific about what went wrong
3. Actionable (suggest how to fix)
4. Educational (explain why)
5. Consistent in format

## Examples of Improved Error Messages

### Input Validation

**Before:**
```python
except ValueError:
    print("Enter a Valid Number!")
```

**After:**
```python
except ValueError:
    print("Error: Invalid input!")
    print("Please enter a whole number (e.g., 5, 10, 100)")
    print("Example: If asked for age, enter '25' not 'twenty-five'")
```

### Division by Zero

**Before:**
```python
except ZeroDivisionError:
    print("A Number Can't be Divide by Zero")
```

**After:**
```python
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    print("Mathematical Note: Division by zero is undefined")
    print("Fix: Enter a non-zero number as the divisor")
```

### File Not Found

**Before:**
```python
# FileNotFoundError crashes the program
```

**After:**
```python
try:
    with open("file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print(f"Error: File 'file.txt' not found!")
    print(f"Current directory: {os.getcwd()}")
    print("Possible fixes:")
    print("  1. Check if the file exists")
    print("  2. Check the file path")
    print("  3. Create the file first")
```

### API Errors

**Before:**
```python
return jsonify({"error": "Destination not found!"}), 404
```

**After:**
```python
return jsonify({
    "error": "Destination not found",
    "message": f"No destination exists with ID {destination_id}",
    "suggestions": [
        "Check if the ID is correct",
        "Use GET /destinations to see available IDs",
        "Create a new destination with POST /destinations"
    ]
}), 404
```

## Implementation Guidelines

### Error Message Template

```python
def format_error(error_type: str, message: str, suggestions: list[str]) -> str:
    """Format a helpful error message."""
    output = [f"Error: {error_type}!", f"Details: {message}"]
    if suggestions:
        output.append("Suggestions:")
        for i, suggestion in enumerate(suggestions, 1):
            output.append(f"  {i}. {suggestion}")
    return "\n".join(output)
```

### Usage Example

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print(format_error(
        error_type="Invalid Input",
        message="Age must be a whole number",
        suggestions=[
            "Enter a number without decimals (e.g., 25)",
            "Don't include words (e.g., enter '25' not 'twenty-five')",
            "Remove any special characters"
        ]
    ))
```

## Files to Update

Priority order:

1. [ ] `basics/09_error_handling/` - All files
2. [ ] `basics/02_variables_types/` - Input validation
3. [ ] `basics/07_file_handling/` - File errors
4. [ ] `rest_api/main.py` - API errors
5. [ ] `fastapi/main.py` - Already good, minor improvements
6. [ ] `basics/11_projects/` - Game errors

## Error Message Standards

### DO ✅
- Use clear, simple language
- Explain what went wrong
- Suggest how to fix
- Include examples when helpful
- Be specific about values

### DON'T ❌
- Use technical jargon without explanation
- Blame the user
- Be vague ("Something went wrong")
- Show raw stack traces to users
- Use grammatical errors

## Examples by Category

### Type Errors
```python
# Good
print("Error: Expected a number, got text")
print("Fix: Convert input to number using int() or float()")
print("Example: age = int(input('Enter age: '))")
```

### Index Errors
```python
# Good
print(f"Error: List index {index} is out of range")
print(f"The list has {len(items)} items (indices 0 to {len(items)-1})")
print("Fix: Use an index within the valid range")
```

### Key Errors
```python
# Good
print(f"Error: Key '{key}' not found in dictionary")
print(f"Available keys: {list(dictionary.keys())}")
print("Fix: Use one of the available keys or check if key exists first")
```

### Import Errors
```python
# Good
print(f"Error: Cannot import module '{module_name}'")
print("Possible reasons:")
print("  1. Module is not installed")
print("  2. Module name is misspelled")
print("  3. Module is not in Python path")
print(f"Fix: Run 'pip install {module_name}'")
```

## Testing

Create tests for error messages:

```python
# tests/test_error_messages.py
def test_division_error_message():
    """Test that division error message is helpful."""
    import io, sys
    from basics.09_error_handling.01_try_except import divide
    
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    assert "cannot divide by zero" in output.lower()
    assert "fix" in output.lower() or "suggestion" in output.lower()
```

## Benefits

- ✅ Better learning experience
- ✅ Faster debugging
- ✅ Less frustration
- ✅ Educational value
- ✅ Professional quality
