---
title: "BUG: Prime number checker has inverted logic in basics/03_control_flow/02_check_prime.py"
labels: ["bug", "good first issue"]
assignees: []
---

## Bug Description

The prime number checking logic in `basics/03_control_flow/02_check_prime.py` is inverted, causing incorrect results.

## Problem

The final if-else block has the logic reversed:

```python
if(prime):
    prime = False  # This should be True
else:
    prime = True   # This should be False
```

## Expected Behavior

- Prime numbers (2, 3, 5, 7, 11, etc.) should return `True`
- Non-prime numbers should return `False`

## Current Behavior

- Prime numbers return `False`
- Non-prime numbers return `True`

## Files Affected

- `basics/03_control_flow/02_check_prime.py`

## Suggested Fix

Swap the assignments in the final if-else block:

```python
if(prime):
    prime = True
else:
    prime = False
```

Or simply remove the final if-else block entirely since the logic is already correct before it.

## How to Test

1. Run the script with input `7` (prime number) - should output `True`
2. Run the script with input `10` (non-prime) - should output `False`
