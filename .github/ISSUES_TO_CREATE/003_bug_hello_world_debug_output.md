---
title: "BUG: Debug/test output in basics/01_introduction/01_hello_world.py"
labels: ["bug", "good first issue"]
assignees: []
---

## Bug Description

The first Python file that beginners encounter (`01_hello_world.py`) contains what appears to be debug or test output that should be removed.

## Problem

```python
print("ram")  # This appears to be debug/test output
print("Hello World")
```

## Expected Behavior

The first program should only print "Hello World" without any extraneous output.

## Current Behavior

Prints two lines:
```
ram
Hello World
```

## Files Affected

- `basics/01_introduction/01_hello_world.py`

## Suggested Fix

Remove the first print statement:

```python
print("Hello World")
```

## Why This Matters

This is the very first file beginners run. Extra output that doesn't match the expected "Hello World" can be confusing and suggests the code is unfinished or has errors.

## How to Test

1. Run `python 01_hello_world.py`
2. Should only output: `Hello World`
