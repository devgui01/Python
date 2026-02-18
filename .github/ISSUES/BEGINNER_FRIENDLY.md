# 🐛 Good First Issues for Beginners

Perfect for first-time contributors! These issues are small, well-defined, and great for learning.

---

## 🌟 Super Beginner Friendly (No Experience Required)

### #001 - Fix Typos in Documentation
**Difficulty:** ⭐ Easy  
**Time:** 15-30 minutes  
**Skills:** Reading, attention to detail

**Description:**
Find and fix typos in README files, comments, or documentation.

**Tasks:**
- [ ] Check `README.md` for spelling errors
- [ ] Review `GETTING_STARTED.md` for grammar issues
- [ ] Fix any typos found in code comments
- [ ] Submit a PR with corrections

**Files to check:**
- `README.md`
- `GETTING_STARTED.md`
- `CONTRIBUTING.md`
- `basics/*/README.md`

**How to submit:**
1. Note the file and line number
2. Fix the typo
3. Commit with message: `docs: fix typo in [filename]`
4. Open PR

---

### #002 - Add Your Name to Contributors List
**Difficulty:** ⭐ Easy  
**Time:** 10 minutes  
**Skills:** Git basics

**Description:**
Add yourself to the contributors list to get started with open source!

**Tasks:**
- [ ] Create `CONTRIBUTORS.md` if it doesn't exist
- [ ] Add your name, GitHub username, and date
- [ ] Format: `- Your Name (@username) - YYYY-MM-DD`

**Example:**
```markdown
# Contributors

- Pritam (@hackdartstorm) - 2026-02-19
- Your Name (@yourusername) - 2026-02-19
```

---

### #003 - Add Code Comments to Simple Programs
**Difficulty:** ⭐ Easy  
**Time:** 30 minutes  
**Skills:** Basic Python, explaining concepts

**Description:**
Add helpful comments to beginner programs to make them easier to understand.

**Files needing comments:**
- [ ] `basics/01_introduction/01_hello_world.py`
- [ ] `basics/01_introduction/02_user_input_addition.py`
- [ ] `basics/02_variables_types/01_arithmetic.py`

**Example:**
```python
# Get first number from user
first_number = int(input("Enter the Number: "))

# Get second number from user
second_number = int(input("Enter the Number: "))

# Calculate and display the sum
print(f"Addition of {first_number} and {second_number} is {first_number + second_number}")
```

---

### #004 - Create Examples for Basic Operators
**Difficulty:** ⭐ Easy  
**Time:** 45 minutes  
**Skills:** Python operators

**Description:**
Create simple example files demonstrating each Python operator.

**Files to create:**
- [ ] `basics/02_variables_types/14_addition_operator.py`
- [ ] `basics/02_variables_types/15_subtraction_operator.py`
- [ ] `basics/02_variables_types/16_multiplication_operator.py`
- [ ] `basics/02_variables_types/17_division_operator.py`
- [ ] `basics/02_variables_types/18_modulus_operator.py`
- [ ] `basics/02_variables_types/19_exponentiation_operator.py`
- [ ] `basics/02_variables_types/20_floor_division_operator.py`

**Template:**
```python
# Addition Operator Example
# This program adds two numbers and displays the result

num1 = 10
num2 = 5
result = num1 + num2

print(f"{num1} + {num2} = {result}")
```

---

### #005 - Add Print Statements to Show Variable Values
**Difficulty:** ⭐ Easy  
**Time:** 30 minutes  
**Skills:** Print function, debugging

**Description:**
Add print statements to show intermediate values in programs.

**Files to update:**
- [ ] `basics/03_control_flow/01_if_else.py`
- [ ] `basics/03_control_flow/02_check_prime.py`
- [ ] `basics/04_functions/01_functions_basics.py`

**Example addition:**
```python
age = int(input("Enter Your Age: "))
print(f"You entered: {age}")  # Add this line

if age >= 18:
    print("You can vote!")
```

---

## 📝 Beginner Friendly (Basic Python Knowledge)

### #006 - Create Input Validation Examples
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1 hour  
**Skills:** try/except, input validation

**Description:**
Create examples showing how to validate user input safely.

**Files to create:**
- [ ] `basics/09_error_handling/04_validate_number_input.py`
- [ ] `basics/09_error_handling/05_validate_age_input.py`
- [ ] `basics/09_error_handling/06_validate_email_input.py`

**Example:**
```python
# Validate Number Input
while True:
    try:
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
```

---

### #007 - Add Examples for String Methods
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1 hour  
**Skills:** String manipulation

**Description:**
Create individual example files for each string method.

**Methods to cover:**
- [ ] `upper()` - Convert to uppercase
- [ ] `lower()` - Convert to lowercase
- [ ] `title()` - Title case
- [ ] `capitalize()` - Capitalize first letter
- [ ] `swapcase()` - Swap case
- [ ] `strip()` - Remove whitespace
- [ ] `lstrip()` - Remove left whitespace
- [ ] `rstrip()` - Remove right whitespace
- [ ] `replace()` - Replace substring
- [ ] `split()` - Split string
- [ ] `join()` - Join list elements
- [ ] `find()` - Find substring
- [ ] `count()` - Count occurrences
- [ ] `startswith()` - Check prefix
- [ ] `endswith()` - Check suffix

**File naming:** `basics/06_strings/10_string_upper.py`, etc.

---

### #008 - Create List Method Examples
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1.5 hours  
**Skills:** Lists, methods

**Description:**
Create examples for each list method.

**Methods to cover:**
- [ ] `append()` - Add to end
- [ ] `insert()` - Insert at index
- [ ] `remove()` - Remove by value
- [ ] `pop()` - Remove by index
- [ ] `clear()` - Remove all
- [ ] `index()` - Find index
- [ ] `count()` - Count occurrences
- [ ] `sort()` - Sort list
- [ ] `reverse()` - Reverse list
- [ ] `copy()` - Copy list
- [ ] `extend()` - Add multiple items

**File naming:** `basics/05_data_structures/22_list_append.py`, etc.

---

### #009 - Add Real-World Examples for Basic Concepts
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 2 hours  
**Skills:** Applying concepts to real scenarios

**Description:**
Create examples showing how basic Python is used in real life.

**Examples to create:**
- [ ] `basics/02_variables_types/21_calculate_grocery_bill.py` - Shopping calculator
- [ ] `basics/02_variables_types/22_calculate_tip.py` - Tip calculator
- [ ] `basics/02_variables_types/23_convert_currency.py` - Currency converter
- [ ] `basics/03_control_flow/11_check_voting_eligibility.py` - Voting checker
- [ ] `basics/03_control_flow/12_calculate_discount.py` - Discount calculator
- [ ] `basics/04_functions/12_calculate_bmi.py` - BMI calculator
- [ ] `basics/04_functions/13_convert_temperature.py` - Temperature converter

---

### #010 - Create Practice Problems with Solutions
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 2 hours  
**Skills:** Problem-solving, teaching

**Description:**
Create practice problems for beginners with solution files.

**Problems to create:**
- [ ] `exercises/001_add_two_numbers.py` + `exercises/solutions/001_solution.py`
- [ ] `exercises/002_find_maximum.py` + `exercises/solutions/002_solution.py`
- [ ] `exercises/003_check_even_odd.py` + `exercises/solutions/003_solution.py`
- [ ] `exercises/004_print_table.py` + `exercises/solutions/004_solution.py`
- [ ] `exercises/005_reverse_string.py` + `exercises/solutions/005_solution.py`
- [ ] `exercises/006_count_vowels.py` + `exercises/solutions/006_solution.py`
- [ ] `exercises/007_find_factorial.py` + `exercises/solutions/007_solution.py`
- [ ] `exercises/008_fibonacci_sequence.py` + `exercises/solutions/008_solution.py`
- [ ] `exercises/009_palindrome_check.py` + `exercises/solutions/009_solution.py`
- [ ] `exercises/010_sum_of_digits.py` + `exercises/solutions/010_solution.py`

**Problem template:**
```python
"""
Practice Problem #001: Add Two Numbers

Write a program that:
1. Takes two numbers as input from the user
2. Adds them together
3. Prints the result

Example:
Enter first number: 5
Enter second number: 3
Sum: 8

Hint: Use int() to convert input to integer
"""

# Your code here

```

---

### #011 - Add Comments Explaining Error Messages
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1 hour  
**Skills:** Understanding errors, teaching

**Description:**
Create examples that intentionally cause common errors, with explanations.

**Files to create:**
- [ ] `basics/09_error_handling/07_common_errors_name_error.py`
- [ ] `basics/09_error_handling/08_common_errors_type_error.py`
- [ ] `basics/09_error_handling/09_common_errors_syntax_error.py`
- [ ] `basics/09_error_handling/10_common_errors_index_error.py`
- [ ] `basics/09_error_handling/11_common_errors_key_error.py`
- [ ] `basics/09_error_handling/12_common_errors_attribute_error.py`
- [ ] `basics/09_error_handling/13_common_errors_value_error.py`
- [ ] `basics/09_error_handling/14_common_errors_zero_division.py`

**Example:**
```python
# NameError: name is not defined
# This error occurs when you use a variable that doesn't exist

# Uncomment to see the error:
# print(undefined_variable)

# Fix: Define the variable first
defined_variable = "Hello"
print(defined_variable)  # This works!
```

---

### #012 - Create "What Will This Output?" Quizzes
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1.5 hours  
**Skills:** Code reading, prediction

**Description:**
Create quiz files that ask learners to predict output.

**Files to create:**
- [ ] `exercises/quizzes/quiz_001_variables.py`
- [ ] `exercises/quizzes/quiz_002_operators.py`
- [ ] `exercises/quizzes/quiz_003_conditionals.py`
- [ ] `exercises/quizzes/quiz_004_loops.py`
- [ ] `exercises/quizzes/quiz_005_functions.py`

**Template:**
```python
"""
Quiz #001: Variables and Types

Question 1: What will this code output?
"""

# Code snippet
x = 5
y = 10
x = y
print(x)

# Options:
# A) 5
# B) 10
# C) Error
# D) None

# Write your answer below:
# Answer: 

"""
Run this file to check your answer!
"""

# Solution (scroll down only after trying!)
# 
# 
# 
# 
# Answer: B) 10
# Explanation: y's value (10) is assigned to x, so x becomes 10
```

---

### #013 - Add Examples for f-strings
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1 hour  
**Skills:** String formatting

**Description:**
Create comprehensive f-string examples.

**Files to create:**
- [ ] `basics/06_strings/20_fstring_basics.py`
- [ ] `basics/06_strings/21_fstring_with_variables.py`
- [ ] `basics/06_strings/22_fstring_with_expressions.py`
- [ ] `basics/06_strings/23_fstring_number_formatting.py`
- [ ] `basics/06_strings/24_fstring_currency_format.py`
- [ ] `basics/06_strings/25_fstring_percentage.py`
- [ ] `basics/06_strings/26_fstring_multiline.py`
- [ ] `basics/06_strings/27_fstring_with_functions.py`

---

### #014 - Create Comparison Operators Examples
**Difficulty:** ⭐ Easy  
**Time:** 45 minutes  
**Skills:** Comparison operators

**Description:**
Create examples for each comparison operator.

**Files to create:**
- [ ] `basics/02_variables_types/24_equal_to_operator.py`
- [ ] `basics/02_variables_types/25_not_equal_to_operator.py`
- [ ] `basics/02_variables_types/26_greater_than_operator.py`
- [ ] `basics/02_variables_types/27_less_than_operator.py`
- [ ] `basics/02_variables_types/28_greater_equal_operator.py`
- [ ] `basics/02_variables_types/29_less_equal_operator.py`

---

### #015 - Add Examples Showing Variable Scope
**Difficulty:** ⭐⭐ Easy-Medium  
**Time:** 1 hour  
**Skills:** Variable scope, functions

**Description:**
Create examples demonstrating local vs global scope.

**Files to create:**
- [ ] `basics/04_functions/14_local_scope_example.py`
- [ ] `basics/04_functions/15_global_scope_example.py`
- [ ] `basics/04_functions/16_enclosing_scope_example.py`
- [ ] `basics/04_functions/17_scope_resolution_example.py`

---

## 🎯 How to Get Started

1. **Pick an issue** from the list above
2. **Comment** on the issue to claim it
3. **Fork** the repository
4. **Create a branch**: `git checkout -b issue-XXX-your-name`
5. **Make your changes**
6. **Test** your code works
7. **Commit** with clear message
8. **Push** and create Pull Request
9. **Wait for review** and address feedback

---

## 📚 Resources for Beginners

- [GitHub First PR Guide](https://docs.github.com/en/get-started/quickstart/hello-world)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)

---

## ❓ Need Help?

- **Stuck?** Comment on the issue with your question
- **Code review?** Request in the PR description
- **Git help?** Check GitHub's documentation
- **Python help?** Ask in GitHub Discussions

---

**Remember:** Every expert was once a beginner. Your first contribution matters! 🌟
