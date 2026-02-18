# 🔧 Intermediate Issues

For contributors comfortable with Python basics, ready for more challenging tasks.

---

## 💻 Code & Features

### #101 - Add Type Hints to Functions
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 2-3 hours  
**Skills:** Type hints, function signatures

**Description:**
Add type hints to all function definitions to improve code clarity and enable better IDE support.

**Files to update:**
- [ ] `basics/04_functions/*.py` - Add parameter and return type hints
- [ ] `basics/08_oop/*.py` - Add type hints to methods
- [ ] `fastapi/main.py` - Ensure all endpoints have type hints
- [ ] `rest_api/main.py` - Add type hints to route handlers

**Example:**
```python
# Before
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# After
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

**Acceptance criteria:**
- All functions have parameter type hints
- All functions have return type hints
- Type hints are correct and consistent
- Code still runs without errors

---

### #102 - Create Data Structure Practice Problems
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 3-4 hours  
**Skills:** Lists, dicts, sets, tuples

**Description:**
Create intermediate-level practice problems for data structures.

**Problems to create:**
- [ ] Find duplicates in a list
- [ ] Remove duplicates while preserving order
- [ ] Merge two dictionaries
- [ ] Find common elements in two lists
- [ ] Count word frequency in text
- [ ] Group list items by first letter
- [ ] Flatten a nested list
- [ ] Find pairs that sum to target
- [ ] Rotate a list by n positions
- [ ] Find second largest number in list

**File format:** `exercises/020_*.py` with solutions

---

### #103 - Add Docstrings to All Functions
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 3-4 hours  
**Skills:** Documentation, docstring format

**Description:**
Add comprehensive docstrings to all functions using Google style.

**Docstring format:**
```python
def calculate_area(radius: float) -> float:
    """Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle (must be positive)
    
    Returns:
        The area of the circle
    
    Raises:
        ValueError: If radius is negative
    
    Example:
        >>> calculate_area(5)
        78.53981633974483
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius ** 2
```

**Files to update:**
- All files in `basics/04_functions/`
- All files in `basics/08_oop/`
- All files in `fastapi/`
- All files in `rest_api/`

---

### #104 - Create File Handling Examples
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 2-3 hours  
**Skills:** File I/O, CSV, JSON

**Description:**
Create comprehensive file handling examples.

**Files to create:**
- [ ] `basics/07_file_handling/15_read_csv_file.py` - Read CSV with csv module
- [ ] `basics/07_file_handling/16_write_csv_file.py` - Write CSV file
- [ ] `basics/07_file_handling/17_read_json_file.py` - Read JSON file
- [ ] `basics/07_file_handling/18_write_json_file.py` - Write JSON file
- [ ] `basics/07_file_handling/19_read_large_file.py` - Read file line by line
- [ ] `basics/07_file_handling/20_append_to_file.py` - Append content
- [ ] `basics/07_file_handling/21_count_lines_words.py` - File statistics
- [ ] `basics/07_file_handling/22_find_replace_in_file.py` - Search and replace

---

### #105 - Add Logging Examples
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 2 hours  
**Skills:** logging module, best practices

**Description:**
Replace print statements with proper logging in examples.

**Files to create:**
- [ ] `basics/10_advanced/12_logging_basics.py` - Basic logging setup
- [ ] `basics/10_advanced/13_logging_levels.py` - DEBUG, INFO, WARNING, ERROR, CRITICAL
- [ ] `basics/10_advanced/14_logging_to_file.py` - File handler
- [ ] `basics/10_advanced/15_logging_format.py` - Custom log format
- [ ] `basics/10_advanced/16_logging_multiple_modules.py` - Module-specific logging

**Update existing files:**
- Replace `print()` debug statements with `logging.debug()`
- Add logging to error handling examples

---

### #106 - Create Decorator Examples
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 3 hours  
**Skills:** Decorators, higher-order functions

**Description:**
Create comprehensive decorator examples from basic to advanced.

**Files to create:**
- [ ] `basics/10_advanced/17_decorator_basics.py` - Simple decorator
- [ ] `basics/10_advanced/18_decorator_with_arguments.py` - Decorator factory
- [ ] `basics/10_advanced/19_class_decorator.py` - Class-based decorator
- [ ] `basics/10_advanced/20_timing_decorator.py` - Measure function time
- [ ] `basics/10_advanced/21_caching_decorator.py` - Memoization
- [ ] `basics/10_advanced/22_authentication_decorator.py` - Simple auth check
- [ ] `basics/10_advanced/23_retry_decorator.py` - Retry on failure
- [ ] `basics/10_advanced/24_chaining_decorators.py` - Multiple decorators

---

### #107 - Add Context Manager Examples
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 2-3 hours  
**Skills:** Context managers, `with` statement

**Description:**
Create examples showing custom context managers.

**Files to create:**
- [ ] `basics/10_advanced/25_context_manager_basics.py` - Using `with`
- [ ] `basics/10_advanced/26_custom_context_manager_class.py` - Class-based
- [ ] `basics/10_advanced/27_context_manager_with_contextlib.py` - @contextmanager
- [ ] `basics/10_advanced/28_database_connection_context.py` - DB connection
- [ ] `basics/10_advanced/29_file_lock_context.py` - File locking

---

### #108 - Create Generator Examples
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 2-3 hours  
**Skills:** Generators, yield, iterators

**Description:**
Create examples demonstrating generators and their benefits.

**Files to create:**
- [ ] `basics/10_advanced/30_generator_basics.py` - yield keyword
- [ ] `basics/10_advanced/31_generator_vs_list.py` - Memory efficiency
- [ ] `basics/10_advanced/32_generator_expressions.py` - Generator comprehensions
- [ ] `basics/10_advanced/33_infinite_generator.py` - Infinite sequences
- [ ] `basics/10_advanced/34_generator_pipeline.py` - Chaining generators
- [ ] `basics/10_advanced/35_send_to_generator.py` - Two-way communication

---

### #109 - Add Regular Expression Examples
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 3-4 hours  
**Skills:** Regex, pattern matching

**Description:**
Create comprehensive regex examples.

**Files to create:**
- [ ] `basics/10_advanced/36_regex_basics.py` - Pattern matching
- [ ] `basics/10_advanced/37_regex_email_validation.py` - Email validation
- [ ] `basics/10_advanced/38_regex_phone_numbers.py` - Phone number extraction
- [ ] `basics/10_advanced/39_regex_url_extraction.py` - URL extraction
- [ ] `basics/10_advanced/40_regex_find_replace.py` - Search and replace
- [ ] `basics/10_advanced/41_regex_groups.py` - Capturing groups
- [ ] `basics/10_advanced/42_regex_lookahead_lookbehind.py` - Advanced patterns

---

### #110 - Create API Integration Examples
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 4-5 hours  
**Skills:** APIs, requests, JSON

**Description:**
Create examples showing how to work with public APIs.

**Files to create:**
- [ ] `basics/10_advanced/43_api_requests_basics.py` - GET request
- [ ] `basics/10_advanced/44_api_post_request.py` - POST request
- [ ] `basics/10_advanced/45_api_error_handling.py` - Handle API errors
- [ ] `basics/10_advanced/46_api_rate_limiting.py` - Rate limit handling
- [ ] `basics/10_advanced/47_api_authentication.py` - API key auth
- [ ] `basics/10_advanced/48_api_pagination.py` - Handle pagination

**APIs to use:**
- JSONPlaceholder (free, no auth)
- OpenWeatherMap (free tier)
- PokeAPI (free, no auth)
- Random User Generator (free)

---

## 📝 Documentation

### #111 - Create Topic-Specific README Files
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 3-4 hours  
**Skills:** Technical writing, organization

**Description:**
Create detailed README files for each topic folder.

**READMEs to create:**
- [ ] `basics/01_introduction/README.md` - Introduction to Python
- [ ] `basics/02_variables_types/README.md` - Variables and types guide
- [ ] `basics/03_control_flow/README.md` - Control flow patterns
- [ ] `basics/04_functions/README.md` - Functions best practices
- [ ] `basics/05_data_structures/README.md` - Data structures guide
- [ ] `basics/06_strings/README.md` - String manipulation
- [ ] `basics/07_file_handling/README.md` - File I/O patterns
- [ ] `basics/08_oop/README.md` - OOP concepts in Python
- [ ] `basics/09_error_handling/README.md` - Error handling strategies
- [ ] `basics/10_advanced/README.md` - Advanced Python features

**Each README should include:**
- Topic overview
- Key concepts
- Common pitfalls
- Examples index
- Practice exercises
- Additional resources

---

### #112 - Add Video Tutorial Scripts
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 4-6 hours  
**Skills:** Teaching, scripting

**Description:**
Write scripts for video tutorials on key topics.

**Scripts to create:**
- [ ] `docs/videos/001_python_introduction.md` - 10 min intro
- [ ] `docs/videos/002_variables_types.md` - 15 min tutorial
- [ ] `docs/videos/003_control_flow.md` - 20 min tutorial
- [ ] `docs/videos/004_functions.md` - 20 min tutorial
- [ ] `docs/videos/005_data_structures.md` - 25 min tutorial
- [ ] `docs/videos/006_file_handling.md` - 15 min tutorial
- [ ] `docs/videos/007_oop_basics.md` - 25 min tutorial
- [ ] `docs/videos/008_error_handling.md` - 15 min tutorial

**Script format:**
```markdown
# Video Title: [Topic Name]
Duration: XX minutes

## Introduction (0:00-0:30)
- Hook
- What we'll learn

## Main Content (0:30-XX:00)
- Concept 1 with example
- Concept 2 with example
- Common mistakes

## Practice (XX:00-XX:30)
- Exercise to try

## Summary (XX:30-end)
- Key takeaways
- Next steps
```

---

### #113 - Create Glossary of Python Terms
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 2-3 hours  
**Skills:** Technical writing

**Description:**
Create a comprehensive glossary of Python terminology.

**File:** `docs/glossary.md`

**Terms to include:**
- Variable
- Function
- Class
- Object
- Method
- Module
- Package
- Import
- Exception
- Iterator
- Generator
- Decorator
- Context Manager
- List Comprehension
- Lambda Function
- And 50+ more terms

---

## 🧪 Testing

### #114 - Write Unit Tests for Basics Examples
**Difficulty:** ⭐⭐⭐ Medium  
**Time:** 4-5 hours  
**Skills:** pytest, testing

**Description:**
Add comprehensive unit tests for existing examples.

**Test files to create:**
- [ ] `tests/test_control_flow.py` - Test if/else, loops
- [ ] `tests/test_functions.py` - Test function examples
- [ ] `tests/test_file_handling.py` - Test file operations
- [ ] `tests/test_oop.py` - Test class examples
- [ ] `tests/test_string_methods.py` - Test string operations

**Requirements:**
- Minimum 80% code coverage
- Test both success and error cases
- Use pytest fixtures where appropriate
- Add docstrings to test functions

---

### #115 - Add Integration Tests for APIs
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 3-4 hours  
**Skills:** API testing, pytest

**Description:**
Create integration tests for FastAPI and Flask APIs.

**Test files to create:**
- [ ] `tests/test_fastapi_endpoints.py` - Test FastAPI routes
- [ ] `tests/test_flask_endpoints.py` - Test Flask routes
- [ ] `tests/test_api_validation.py` - Test input validation
- [ ] `tests/test_api_errors.py` - Test error responses

---

## 🎨 UI/UX (Optional)

### #116 - Create Progress Dashboard UI
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 6-8 hours  
**Skills:** HTML, CSS, JavaScript (optional)

**Description:**
Create a simple web dashboard to track learning progress.

**Features:**
- Display completed exercises
- Show progress bars
- List available exercises
- Mark exercises complete
- Save progress to JSON file

**Tech stack options:**
- Simple: HTML + JavaScript + localStorage
- Medium: Flask + SQLite
- Advanced: FastAPI + React

---

## 🔒 Security

### #117 - Add Security Best Practices Examples
**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Time:** 3-4 hours  
**Skills:** Security, best practices

**Description:**
Create examples showing secure coding practices.

**Files to create:**
- [ ] `basics/10_advanced/49_secure_password_storage.py` - Hash passwords
- [ ] `basics/10_advanced/50_secure_input_validation.py` - Validate input
- [ ] `basics/10_advanced/51_secure_file_permissions.py` - File permissions
- [ ] `basics/10_advanced/52_secure_api_keys.py` - Environment variables
- [ ] `basics/10_advanced/53_sql_injection_prevention.py` - Parameterized queries

---

## 📊 How to Choose

**First-time contributor?** Start with #101 (Type Hints) or #111 (README files)

**Want to teach?** Try #102 (Practice Problems) or #112 (Video Scripts)

**Like testing?** Check out #114 (Unit Tests)

**Security-minded?** Look at #117 (Security Examples)

---

## 🏆 Recognition

Contributors who complete 3+ intermediate issues:
- Featured in CONTRIBUTORS.md
- "Intermediate Contributor" badge on GitHub profile
- Invitation to join core team

---

**Ready to level up? Pick an intermediate issue and make your mark! 🚀**
