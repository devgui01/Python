---
title: "FEATURE: Add interactive exercises with automated checking"
labels: ["enhancement", "feature", "advanced"]
assignees: []
---

## Feature Description

Add interactive exercises that automatically check learner solutions and provide feedback. This transforms passive reading into active learning.

## Current State

Learners currently:
- Read code examples
- Manually run files
- No feedback on understanding
- No practice exercises with solutions

## Proposed Feature

Interactive exercise system with:
- Problem descriptions
- Test cases
- Automated solution checking
- Hints system
- Progress tracking

## Implementation

### 1. Exercise Runner

```python
# exercises/runner.py
import importlib.util
import sys
from io import StringIO
from typing import Callable, Any

class ExerciseChecker:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tests = []
        self.hints = []
    
    def add_test(self, test_func: Callable, expected: Any, description: str):
        """Add a test case."""
        self.tests.append({
            'func': test_func,
            'expected': expected,
            'description': description
        })
        return self
    
    def add_hint(self, hint: str):
        """Add a hint for this exercise."""
        self.hints.append(hint)
        return self
    
    def check_solution(self, solution_file: str) -> dict:
        """Check if solution passes all tests."""
        results = {
            'passed': 0,
            'failed': 0,
            'errors': []
        }
        
        # Load student's solution
        spec = importlib.util.spec_from_file_location("solution", solution_file)
        module = importlib.util.module_from_spec(spec)
        
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            spec.loader.exec_module(module)
            output = sys.stdout.getvalue()
        except Exception as e:
            results['errors'].append(f"Execution error: {e}")
            return results
        finally:
            sys.stdout = old_stdout
        
        # Run tests
        for test in self.tests:
            try:
                result = test['func'](module)
                if result == test['expected']:
                    results['passed'] += 1
                else:
                    results['failed'] += 1
                    results['errors'].append(
                        f"Failed: {test['description']}. "
                        f"Expected {test['expected']}, got {result}"
                    )
            except Exception as e:
                results['failed'] += 1
                results['errors'].append(f"Test error: {e}")
        
        return results
```

### 2. Example Exercise

```python
# exercises/basics/ex_01_hello.py
from runner import ExerciseChecker

exercise = ExerciseChecker(
    name="Hello World",
    description="Print 'Hello World' to the console"
)

# Test 1: Check if output contains Hello World
def test_output(module):
    # Re-run and capture output
    import io, sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    # Module already executed in checker
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output.strip()

exercise.add_test(
    test_func=test_output,
    expected="Hello World",
    description="Output should be 'Hello World'"
)

exercise.add_hint("Use the print() function")
exercise.add_hint("Remember to use quotes for strings")
exercise.add_hint("Make sure there's no extra text")
```

### 3. Student Template

```python
# exercises/basics/solutions/ex_01_hello_template.py
"""
Exercise 1: Hello World

Task: Print 'Hello World' to the console

Expected Output:
Hello World
"""

# Your code here


```

### 4. CLI Runner

```python
# scripts/check_exercise.py
import sys
import json
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_exercise.py <exercise_number>")
        sys.exit(1)
    
    exercise_num = sys.argv[1]
    exercise_file = f"exercises/basics/ex_{exercise_num}.py"
    solution_file = f"exercises/basics/solutions/ex_{exercise_num}_solution.py"
    
    # Load and run exercise
    import importlib.util
    spec = importlib.util.spec_from_file_location("exercise", exercise_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    checker = module.exercise
    results = checker.check_solution(solution_file)
    
    # Display results
    print(f"\n{'='*50}")
    print(f"Exercise {exercise_num}: {checker.name}")
    print(f"{'='*50}")
    print(f"Passed: {results['passed']}/{len(checker.tests)}")
    
    if results['errors']:
        print("\nFeedback:")
        for error in results['errors']:
            print(f"  ❌ {error}")
        
        if results['failed'] > 0:
            print("\n💡 Hints:")
            for hint in checker.hints[:2]:  # Show first 2 hints
                print(f"  - {hint}")
    else:
        print("\n🎉 All tests passed! Great job!")
    
    print(f"{'='*50}\n")
```

### 5. Exercise Topics

Create exercises for:

**Basics:**
- [ ] Hello World
- [ ] Variables and Types
- [ ] Basic Operations
- [ ] Input/Output
- [ ] If-Else Conditions
- [ ] Loops
- [ ] Functions
- [ ] Lists
- [ ] Dictionaries
- [ ] File I/O

**Intermediate:**
- [ ] Classes
- [ ] Error Handling
- [ ] Lambda Functions
- [ ] List Comprehensions

**Advanced:**
- [ ] API Endpoints
- [ ] Database Operations
- [ ] Async Functions

### 6. Progress Tracking

```python
# exercises/progress.py
import json
from pathlib import Path
from datetime import datetime

class ProgressTracker:
    def __init__(self):
        self.progress_file = Path(".exercise_progress.json")
        self.progress = self.load()
    
    def load(self):
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                return json.load(f)
        return {"completed": [], "attempts": {}}
    
    def record_completion(self, exercise_id: str):
        self.progress["completed"].append(exercise_id)
        self.progress["attempts"][exercise_id] = {
            "completed_at": datetime.now().isoformat(),
            "tries": self.progress["attempts"].get(exercise_id, {}).get("tries", 0) + 1
        }
        self.save()
    
    def save(self):
        with open(self.progress_file, "w") as f:
            json.dump(self.progress, f, indent=2)
    
    def get_stats(self):
        total = len(self.progress["completed"])
        return f"Completed: {total} exercises"
```

## Files to Create

- [ ] `exercises/runner.py`
- [ ] `exercises/progress.py`
- [ ] `exercises/basics/` (exercise definitions)
- [ ] `exercises/basics/solutions/` (templates)
- [ ] `scripts/check_exercise.py`
- [ ] `exercises/README.md`

## Usage

```bash
# Student workflow
cd exercises/basics/solutions
cp ex_01_hello_template.py my_solution.py
# Edit my_solution.py
python ../../scripts/check_exercise.py 01
```

## Benefits

- ✅ Active learning vs passive reading
- ✅ Immediate feedback
- ✅ Self-paced progression
- ✅ Track learning progress
- ✅ Gamification potential
