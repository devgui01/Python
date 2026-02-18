"""
Exercise Validator - Automatic solution testing

Usage:
    python validate.py exercise_001
    python validate.py 001
"""

import sys
import os
import importlib.util
from pathlib import Path


class ExerciseValidator:
    """Validates exercise solutions against test cases"""
    
    def __init__(self, exercise_number):
        self.exercise_number = exercise_number.zfill(3)
        self.exercise_file = f"exercises/{self.exercise_number}_*.py"
        self.solution_file = f"exercises/solutions/{self.exercise_number}_solution.py"
    
    def load_solution(self, filepath):
        """Dynamically load a Python module"""
        spec = importlib.util.spec_from_file_location("solution", filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    def validate_hello_user(self, module):
        """Validate Exercise 001: Hello User"""
        tests_passed = 0
        
        # Test 1: Function exists
        if hasattr(module, 'greet_user'):
            tests_passed += 1
            print("✓ Function greet_user exists")
        else:
            print("✗ Function greet_user not found")
            return tests_passed, 1
        
        # Test 2: Returns string
        try:
            # Mock input
            import io
            import sys
            sys.stdin = io.StringIO('Alice\n')
            result = module.greet_user()
            if isinstance(result, str) and 'Alice' in result:
                tests_passed += 1
                print("✓ Returns personalized greeting")
            else:
                print("✗ Greeting doesn't contain name")
        except Exception as e:
            print(f"✗ Error testing function: {e}")
        
        return tests_passed, 2
    
    def validate_calculator(self, module):
        """Validate Exercise 002: Simple Calculator"""
        tests_passed = 0
        total_tests = 4
        
        if hasattr(module, 'calculate'):
            tests_passed += 1
            print("✓ Function calculate exists")
            
            # Test operations
            if module.calculate(5, 3, '+') == 8:
                tests_passed += 1
                print("✓ Addition works")
            
            if module.calculate(10, 2, '/') == 5.0:
                tests_passed += 1
                print("✓ Division works")
            
            if module.calculate(5, 0, '/') == "Error: Division by zero":
                tests_passed += 1
                print("✓ Division by zero handled")
        else:
            print("✗ Function calculate not found")
        
        return tests_passed, total_tests
    
    def validate_is_prime(self, module):
        """Validate Exercise 006: Prime Number Checker"""
        tests_passed = 0
        total_tests = 6
        
        if hasattr(module, 'is_prime'):
            tests_passed += 1
            print("✓ Function is_prime exists")
            
            test_cases = [
                (2, True), (3, True), (4, False),
                (17, True), (1, False), (0, False),
                (-5, False), (97, True)
            ]
            
            for num, expected in test_cases:
                result = module.is_prime(num)
                if result == expected:
                    tests_passed += 1
                    print(f"✓ is_prime({num}) = {result}")
                else:
                    print(f"✗ is_prime({num}) = {result}, expected {expected}")
        else:
            print("✗ Function is_prime not found")
        
        return tests_passed, total_tests
    
    def validate(self):
        """Run validation for the exercise"""
        print(f"\n{'='*50}")
        print(f"Validating Exercise {self.exercise_number}")
        print(f"{'='*50}\n")
        
        # Find exercise file
        exercise_files = list(Path('exercises').glob(f"{self.exercise_number}_*.py"))
        
        if not exercise_files:
            print(f"✗ Exercise file not found: {self.exercise_file}")
            return False
        
        exercise_file = exercise_files[0]
        print(f"Found: {exercise_file}")
        
        # Load solution
        try:
            module = self.load_solution(exercise_file)
        except Exception as e:
            print(f"✗ Error loading module: {e}")
            return False
        
        # Run appropriate validator
        if self.exercise_number == '001':
            passed, total = self.validate_hello_user(module)
        elif self.exercise_number == '002':
            passed, total = self.validate_calculator(module)
        elif self.exercise_number == '006':
            passed, total = self.validate_is_prime(module)
        else:
            print("⚠ Validator not implemented for this exercise yet")
            print("  Manual review required")
            return True
        
        # Show results
        print(f"\n{'='*50}")
        print(f"Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All tests passed! Exercise complete!")
            return True
        else:
            print("❌ Some tests failed. Keep practicing!")
            return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <exercise_number>")
        print("Example: python validate.py 001")
        sys.exit(1)
    
    exercise_number = sys.argv[1]
    validator = ExerciseValidator(exercise_number)
    success = validator.validate()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
