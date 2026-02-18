---
title: "FEATURE: Add coding challenges with test cases"
labels: ["enhancement", "feature", "intermediate"]
assignees: []
---

## Feature Description

Add coding challenges that provide problem descriptions, test cases, and automated verification. This gives learners hands-on practice with real problems.

## Current State

No structured coding challenges exist. Learners only see examples without practice problems.

## Proposed Feature

Coding challenge system with:
- Problem descriptions
- Example inputs/outputs
- Hidden test cases
- Automated verification
- Difficulty levels
- Topic categorization

## Implementation

### 1. Challenge Structure

```python
# challenges/base.py
from dataclasses import dataclass
from typing import List, Callable, Any, Dict
import traceback

@dataclass
class TestCase:
    input_args: tuple
    expected_output: Any
    description: str = ""

@dataclass
class Challenge:
    id: str
    title: str
    description: str
    difficulty: str  # easy, medium, hard
    topic: str
    starter_code: str
    test_cases: List[TestCase]
    hints: List[str]
    solution_explanation: str

class ChallengeChecker:
    def __init__(self, challenge: Challenge):
        self.challenge = challenge
    
    def run_test(self, user_function: Callable, test: TestCase) -> Dict:
        """Run a single test case."""
        try:
            result = user_function(*test.input_args)
            passed = result == test.expected_output
            return {
                'passed': passed,
                'input': test.input_args,
                'expected': test.expected_output,
                'got': result,
                'description': test.description,
                'error': None
            }
        except Exception as e:
            return {
                'passed': False,
                'input': test.input_args,
                'expected': test.expected_output,
                'got': f"Error: {str(e)}",
                'description': test.description,
                'error': traceback.format_exc()
            }
    
    def check_solution(self, user_function: Callable) -> Dict:
        """Check all test cases."""
        results = []
        passed = 0
        
        for test in self.challenge.test_cases:
            result = self.run_test(user_function, test)
            results.append(result)
            if result['passed']:
                passed += 1
        
        return {
            'challenge': self.challenge.title,
            'passed': passed,
            'total': len(self.challenge.test_cases),
            'percentage': (passed / len(self.challenge.test_cases)) * 100,
            'results': results,
            'all_passed': passed == len(self.challenge.test_cases)
        }
```

### 2. Example Challenge

```python
# challenges/basics/01_addition.py
from base import Challenge, TestCase, ChallengeChecker

challenge = Challenge(
    id="basics_01",
    title="Add Two Numbers",
    description="""
Write a function that takes two numbers as input and returns their sum.

Examples:
- add(2, 3) should return 5
- add(-1, 1) should return 0
- add(0, 0) should return 0

Function Signature:
    def add(a, b):
        # Your code here
""",
    difficulty="easy",
    topic="02_variables_types",
    starter_code="""def add(a, b):
    # Write your code here
    pass
""",
    test_cases=[
        TestCase(
            input_args=(2, 3),
            expected_output=5,
            description="Basic addition"
        ),
        TestCase(
            input_args=(-1, 1),
            expected_output=0,
            description="Negative and positive"
        ),
        TestCase(
            input_args=(0, 0),
            expected_output=0,
            description="Zero addition"
        ),
        TestCase(
            input_args=(100, 200),
            expected_output=300,
            description="Larger numbers"
        ),
        TestCase(
            input_args=(-5, -3),
            expected_output=-8,
            description="Both negative"
        ),
    ],
    hints=[
        "Use the + operator for addition",
        "Return the result, don't print it",
        "No need for type conversion - inputs are already numbers"
    ],
    solution_explanation="""
Solution:
    def add(a, b):
        return a + b

Explanation:
The + operator in Python performs addition for numbers.
Simply return the sum of the two parameters.
"""
)

checker = ChallengeChecker(challenge)
```

### 3. Challenge Runner

```python
# scripts/challenge_runner.py
import sys
import importlib.util
import os

def load_user_solution(solution_file: str):
    """Load user's solution from file."""
    spec = importlib.util.spec_from_file_location("solution", solution_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def display_challenge(challenge):
    """Display challenge details."""
    print("\n" + "="*70)
    print(f"📝 Challenge: {challenge.title}")
    print(f"Difficulty: {challenge.difficulty}")
    print(f"Topic: {challenge.topic}")
    print("="*70)
    print(challenge.description)
    print("\n📋 Starter Code:")
    print("-"*40)
    print(challenge.starter_code)
    print("-"*40)

def display_results(results, challenge):
    """Display test results."""
    print("\n" + "="*70)
    print("📊 Results")
    print("="*70)
    print(f"Passed: {results['passed']}/{results['total']}")
    print(f"Score: {results['percentage']:.1f}%")
    
    if results['all_passed']:
        print("\n🎉 All tests passed! Excellent work!")
        print("\n💡 Solution Explanation:")
        print(challenge.solution_explanation)
    else:
        print("\n❌ Some tests failed. Here's feedback:")
        for i, result in enumerate(results['results'], 1):
            if not result['passed']:
                print(f"\n  Test {i}: {result['description']}")
                print(f"    Input: {result['input']}")
                print(f"    Expected: {result['expected']}")
                print(f"    Got: {result['got']}")
                if result['error']:
                    print(f"    Error: {result['error']}")
        
        print("\n💡 Hints:")
        for hint in challenge.hints[:2]:
            print(f"  - {hint}")
    
    print("\n" + "="*70)

def main():
    if len(sys.argv) < 2:
        print("Usage: python challenge_runner.py <challenge_id>")
        print("Example: python challenge_runner.py basics_01")
        sys.exit(1)
    
    challenge_id = sys.argv[1]
    challenge_file = f"challenges/basics/{challenge_id}.py"
    solution_file = f"solutions/{challenge_id}_solution.py"
    
    # Load challenge
    spec = importlib.util.spec_from_file_location("challenge_module", challenge_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    challenge = module.challenge
    checker = module.checker
    
    # Display challenge
    display_challenge(challenge)
    
    input("Press Enter to check your solution...")
    
    # Load and check user solution
    try:
        user_module = load_user_solution(solution_file)
        user_function = getattr(user_module, 'add')  # Get function by name
        results = checker.check_solution(user_function)
        display_results(results, challenge)
    except FileNotFoundError:
        print(f"\n❌ Solution file not found: {solution_file}")
        print("Copy the starter code and save it as the solution file first.")
    except AttributeError as e:
        print(f"\n❌ Function not found in solution: {e}")
```

### 4. Challenge Topics

**Basics (Easy):**
- [ ] Add Two Numbers
- [ ] Find Maximum
- [ ] Check Even/Odd
- [ ] Reverse String
- [ ] Count Vowels
- [ ] Sum of List

**Basics (Medium):**
- [ ] Prime Number Check
- [ ] Fibonacci Sequence
- [ ] Palindrome Check
- [ ] Find Duplicates
- [ ] Factorial

**Intermediate:**
- [ ] Dictionary Operations
- [ ] File Processing
- [ ] Class Implementation
- [ ] Error Handling

**Advanced:**
- [ ] API Endpoint
- [ ] Database Query
- [ ] Algorithm Implementation

## Files to Create

- [ ] `challenges/base.py`
- [ ] `challenges/basics/` (challenge definitions)
- [ ] `challenges/intermediate/`
- [ ] `challenges/advanced/`
- [ ] `solutions/` (templates)
- [ ] `scripts/challenge_runner.py`
- [ ] `challenges/README.md`

## Usage

```bash
# View and solve a challenge
python scripts/challenge_runner.py basics_01

# List all challenges
python scripts/challenge_runner.py list
```

## Benefits

- ✅ Hands-on practice
- ✅ Immediate feedback
- ✅ Progressive difficulty
- ✅ Build problem-solving skills
- ✅ Portfolio of solutions
