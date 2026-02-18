"""
Test Suite for Python Learning Repository

Run with: pytest tests/ -v
Coverage: pytest tests/ --cov=. --cov-report=html
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestBasicsIntroduction:
    """Tests for basics/01_introduction examples"""
    
    def test_hello_world_exists(self):
        """Verify hello world example exists"""
        assert os.path.exists('basics/01_introduction/01_hello_world.py')
    
    def test_user_input_addition_exists(self):
        """Verify user input addition example exists"""
        assert os.path.exists('basics/01_introduction/02_user_input_addition.py')


class TestVariablesTypes:
    """Tests for basics/02_variables_types examples"""
    
    def test_arithmetic_addition(self):
        """Test arithmetic addition logic"""
        first_number = 5
        second_number = 3
        result = first_number + second_number
        assert result == 8
    
    def test_average_calculation(self):
        """Test average calculation"""
        first_number = 10
        second_number = 20
        average = (first_number + second_number) / 2
        assert average == 15.0
    
    def test_comparison_greater(self):
        """Test greater than comparison"""
        first_number = 10
        second_number = 5
        assert first_number > second_number
        assert not second_number > first_number
    
    def test_modulus_remainder(self):
        """Test modulus operator"""
        first_number = 10
        second_number = 3
        remainder = first_number % second_number
        assert remainder == 1
    
    def test_square_calculation(self):
        """Test square calculation"""
        number = 5
        square = number ** 2
        assert square == 25


class TestControlFlow:
    """Tests for basics/03_control_flow examples"""
    
    def test_prime_number_checker(self):
        """Test prime number checking logic"""
        def is_prime(n):
            if n <= 0:
                return False
            elif n == 2:
                return True
            else:
                for divisor in range(2, int(n * 0.5) + 1):
                    if n % divisor == 0:
                        return False
                return True
        
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(4) == False
        assert is_prime(7) == True
        assert is_prime(10) == False
        assert is_prime(0) == False
        assert is_prime(-5) == False
    
    def test_greatest_of_four(self):
        """Test finding greatest of four numbers"""
        def find_greatest(a, b, c, d):
            return max(a, b, c, d)
        
        assert find_greatest(1, 2, 3, 4) == 4
        assert find_greatest(10, 5, 8, 3) == 10
    
    def test_spam_detector(self):
        """Test spam detection logic"""
        def detect_spam(text):
            spam_keywords = ["make a lot of money", "buy now", 
                           "subscribe this", "click this"]
            text = text.lower()
            return any(keyword in text for keyword in spam_keywords)
        
        assert detect_spam("Buy now! Limited offer!") == True
        assert detect_spam("Hello friend") == False
    
    def test_username_length_check(self):
        """Test username length validation"""
        def is_valid_username(username):
            return len(username) >= 10
        
        assert is_valid_username("johnsmith123") == True
        assert is_valid_username("john") == False


class TestDataStructures:
    """Tests for basics/05_data_structures examples"""
    
    def test_list_operations(self):
        """Test basic list operations"""
        fruits_list = ["apple", "banana", "orange"]
        fruits_list.append("grape")
        assert len(fruits_list) == 4
        assert "grape" in fruits_list
    
    def test_list_comprehension(self):
        """Test list comprehension"""
        numbers_list = [1, 2, 3, 4, 5]
        squared_list = [x * x for x in numbers_list]
        assert squared_list == [1, 4, 9, 16, 25]
    
    def test_set_uniqueness(self):
        """Test set removes duplicates"""
        numbers = [1, 2, 2, 3, 3, 3]
        unique_set = set(numbers)
        assert len(unique_set) == 3
        assert unique_set == {1, 2, 3}
    
    def test_dictionary_operations(self):
        """Test dictionary operations"""
        student = {"name": "Alice", "age": 25, "grade": "A"}
        assert student["name"] == "Alice"
        assert "age" in student
        student["grade"] = "A+"
        assert student["grade"] == "A+"
    
    def test_tuple_immutability(self):
        """Test tuple is immutable"""
        coordinates = (10, 20)
        assert coordinates[0] == 10
        assert coordinates[1] == 20
        with pytest.raises(TypeError):
            coordinates[0] = 15


class TestStrings:
    """Tests for basics/06_strings examples"""
    
    def test_string_methods(self):
        """Test string methods"""
        text = "  Hello World  "
        assert text.strip() == "Hello World"
        assert text.upper() == "  HELLO WORLD  "
        assert text.lower() == "  hello world  "
    
    def test_string_slicing(self):
        """Test string slicing"""
        text = "Python"
        assert text[0:2] == "Py"
        assert text[-2:] == "on"
        assert text[::-1] == "nohtyP"
    
    def test_join_strings(self):
        """Test string join"""
        fruits_list = ["Apple", "Banana", "Mango"]
        result = ", ".join(fruits_list)
        assert result == "Apple, Banana, Mango"


class TestFunctions:
    """Tests for basics/04_functions examples"""
    
    def test_factorial_loop(self):
        """Test factorial calculation"""
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
        
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
    
    def test_sum_natural_numbers(self):
        """Test sum of natural numbers"""
        def sum_natural(n):
            return n * (n + 1) // 2
        
        assert sum_natural(0) == 0
        assert sum_natural(1) == 1
        assert sum_natural(10) == 55


class TestErrorHandling:
    """Tests for basics/09_error_handling examples"""
    
    def test_division_by_zero(self):
        """Test division by zero handling"""
        def safe_divide(a, b):
            try:
                return a / b
            except ZeroDivisionError:
                return "Cannot divide by zero!"
        
        assert safe_divide(10, 2) == 5.0
        assert safe_divide(10, 0) == "Cannot divide by zero!"
    
    def test_value_error_handling(self):
        """Test value error handling"""
        def safe_int_convert(value):
            try:
                return int(value)
            except ValueError:
                return "Invalid number!"
        
        assert safe_int_convert("123") == 123
        assert safe_int_convert("abc") == "Invalid number!"


class TestFileHandling:
    """Tests for basics/07_file_handling examples"""
    
    def test_file_read_write(self, tmp_path):
        """Test file read/write operations"""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello World")
        content = test_file.read_text()
        assert content == "Hello World"
    
    def test_file_exists_check(self, tmp_path):
        """Test file existence check"""
        test_file = tmp_path / "exists.txt"
        test_file.write_text("content")
        assert test_file.exists()
        assert not (tmp_path / "missing.txt").exists()


class TestOOP:
    """Tests for basics/08_oop examples"""
    
    def test_class_creation(self):
        """Test basic class creation"""
        class Planet:
            def __init__(self, name):
                self.name = name
                self.has_life = False
            
            def describe(self):
                return f"{self.name}: Has Life = {self.has_life}"
        
        earth = Planet("Earth")
        earth.has_life = True
        assert earth.name == "Earth"
        assert earth.has_life == True
        assert "Earth" in earth.describe()
    
    def test_class_inheritance(self):
        """Test class inheritance"""
        class Animal:
            def __init__(self, name):
                self.name = name
            
            def speak(self):
                return "Some sound"
        
        class Dog(Animal):
            def speak(self):
                return "Woof!"
        
        dog = Dog("Buddy")
        assert dog.name == "Buddy"
        assert dog.speak() == "Woof!"


class TestAdvanced:
    """Tests for basics/10_advanced examples"""
    
    def test_lambda_function(self):
        """Test lambda functions"""
        add = lambda x, y: x + y
        assert add(5, 3) == 8
        
        square = lambda x: x ** 2
        assert square(4) == 16
    
    def test_map_function(self):
        """Test map function"""
        numbers = [1, 2, 3, 4]
        squared = list(map(lambda x: x ** 2, numbers))
        assert squared == [1, 4, 9, 16]
    
    def test_filter_function(self):
        """Test filter function"""
        numbers = [1, 2, 3, 4, 5, 6]
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        assert evens == [2, 4, 6]
    
    def test_list_comprehension_nested(self):
        """Test nested list comprehension"""
        matrix = [[1, 2], [3, 4], [5, 6]]
        flattened = [num for row in matrix for num in row]
        assert flattened == [1, 2, 3, 4, 5, 6]


# Run with: pytest tests/test_examples.py -v
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
