---
title: "ENHANCEMENT: Add unit tests for all Python examples"
labels: ["enhancement", "testing", "advanced"]
assignees: []
---

## Enhancement Description

This project currently has no automated tests. Adding unit tests would:
- Ensure code examples work correctly
- Prevent regressions when code is modified
- Teach learners about testing best practices
- Make the project more professional and production-ready

## Current State

- ❌ No test files exist
- ❌ No test framework configured
- ❌ No CI/CD integration for running tests

## Expected Behavior

Each module should have corresponding tests:
- `basics/01_introduction/` → `tests/test_introduction.py`
- `basics/02_variables_types/` → `tests/test_variables_types.py`
- `fastapi/main.py` → `tests/test_fastapi.py`
- `rest_api/main.py` → `tests/test_rest_api.py`
- etc.

## Files to Create

```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration
├── test_basics/
│   ├── test_introduction.py
│   ├── test_variables_types.py
│   ├── test_control_flow.py
│   ├── test_functions.py
│   └── ...
├── test_fastapi/
│   └── test_campaign_api.py
├── test_rest_api/
│   └── test_travel_api.py
└── test_llm/
    ├── test_architecture.py
    └── test_pretraining.py
```

## Suggested Approach

1. **Add pytest to requirements:**
   ```
   pytest==8.0.0
   pytest-cov==4.1.0
   pytest-asyncio==0.23.0
   ```

2. **Create test structure** as shown above

3. **Write tests for each module:**
   ```python
   # Example: tests/test_basics/test_functions.py
   def test_sum_function():
       from basics.04_functions.01_functions_basics import add
       assert add(2, 3) == 5
       assert add(-1, 1) == 0
   ```

4. **Add pytest configuration:**
   ```ini
   # pytest.ini
   [pytest]
   testpaths = tests
   python_files = test_*.py
   python_functions = test_*
   ```

5. **Update CI/CD** to run tests on push

## Benefits

- ✅ Catches bugs before they reach users
- ✅ Documents expected behavior
- ✅ Makes refactoring safer
- ✅ Teaches testing to learners

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [Python testing best practices](https://docs.python-guide.org/writing/tests/)
