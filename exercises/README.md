# Interactive Coding Exercises

Hands-on coding challenges with automatic validation.

---

## How to Use

1. Choose an exercise based on your skill level
2. Read the problem description
3. Write your solution in the `solutions/` folder
4. Run validation: `python validate.py exercise_001`
5. Check hints if stuck

---

## Beginner Exercises (001-020)

### Exercise 001: Hello User
**Topic:** Input/Output  
**Difficulty:** ⭐ Easy

Create a program that asks for the user's name and greets them personally.

**Requirements:**
- Use `input()` to get the name
- Print a personalized greeting
- Example: "Hello, Alice! Welcome to Python!"

**Starter Code:**
```python
# exercises/001_hello_user.py
def greet_user():
    # Your code here
    pass

if __name__ == "__main__":
    greet_user()
```

---

### Exercise 002: Simple Calculator
**Topic:** Arithmetic Operators  
**Difficulty:** ⭐ Easy

Build a calculator that takes two numbers and an operation (+, -, *, /) and returns the result.

**Requirements:**
- Get two numbers from user
- Get the operation choice
- Display the result
- Handle division by zero

---

### Exercise 003: Even or Odd
**Topic:** Conditional Statements  
**Difficulty:** ⭐ Easy

Write a program that checks if a number is even or odd.

**Requirements:**
- Take a number as input
- Print "Even" or "Odd"
- Handle negative numbers

---

### Exercise 004: Multiplication Table
**Topic:** Loops  
**Difficulty:** ⭐⭐ Medium

Generate a multiplication table for a given number (1-10).

**Requirements:**
- Take a number as input
- Print table from 1 to 10
- Format: "5 x 3 = 15"

---

### Exercise 005: Factorial Calculator
**Topic:** Functions & Loops  
**Difficulty:** ⭐⭐ Medium

Calculate the factorial of a number using both iterative and recursive approaches.

**Requirements:**
- Create `factorial_iterative(n)` function
- Create `factorial_recursive(n)` function
- Both should return the same result

---

### Exercise 006: Prime Number Checker
**Topic:** Functions & Logic  
**Difficulty:** ⭐⭐ Medium

Check if a number is prime.

**Requirements:**
- Create `is_prime(n)` function
- Return True for prime, False otherwise
- Handle edge cases (0, 1, negative numbers)

---

### Exercise 007: List Statistics
**Topic:** Lists  
**Difficulty:** ⭐⭐ Medium

Calculate statistics for a list of numbers.

**Requirements:**
- Find sum, average, min, max
- Count even and odd numbers
- Return as a dictionary

---

### Exercise 008: Password Validator
**Topic:** Strings & Conditions  
**Difficulty:** ⭐⭐ Medium

Validate passwords based on security rules.

**Requirements:**
- At least 8 characters
- Contains uppercase and lowercase
- Contains at least one number
- Contains at least one special character (!@#$%)

---

### Exercise 009: Word Counter
**Topic:** Strings & Dictionaries  
**Difficulty:** ⭐⭐ Medium

Count word frequency in a text.

**Requirements:**
- Take text as input
- Count each word's occurrences
- Return dictionary with word counts

---

### Exercise 010: Temperature Converter
**Topic:** Functions  
**Difficulty:** ⭐ Easy

Convert between Celsius, Fahrenheit, and Kelvin.

**Requirements:**
- `celsius_to_fahrenheit(c)`
- `fahrenheit_to_celsius(f)`
- `celsius_to_kelvin(c)`
- `kelvin_to_celsius(k)`

---

## Intermediate Exercises (011-030)

### Exercise 011: Contact Book
**Topic:** Dictionaries & File I/O  
**Difficulty:** ⭐⭐⭐ Hard

Create a contact management system.

**Requirements:**
- Add, delete, update contacts
- Search by name or phone
- Save to file
- Load from file

---

### Exercise 012: Number Guessing Game
**Topic:** Random & Loops  
**Difficulty:** ⭐⭐ Medium

Build the classic number guessing game.

**Requirements:**
- Computer picks random number (1-100)
- User has 10 attempts
- Provide hints (higher/lower)
- Track score

---

### Exercise 013: Tic-Tac-Toe
**Topic:** 2D Lists & Game Logic  
**Difficulty:** ⭐⭐⭐ Hard

Create a two-player Tic-Tac-Toe game.

**Requirements:**
- 3x3 game board
- Two players (X and O)
- Check for win/draw conditions
- Display board after each move

---

### Exercise 014: File Organizer
**Topic:** OS Module & File I/O  
**Difficulty:** ⭐⭐⭐ Hard

Organize files in a folder by extension.

**Requirements:**
- Scan a directory
- Create folders by extension (.pdf, .jpg, .py)
- Move files to appropriate folders
- Generate report

---

### Exercise 015: Expense Tracker
**Topic:** Classes & File I/O  
**Difficulty:** ⭐⭐⭐ Hard

Track daily expenses with categories.

**Requirements:**
- Add expenses with category
- View expenses by date/category
- Calculate totals
- Save to CSV

---

## Advanced Exercises (031-050)

### Exercise 031: API Client
**Topic:** Requests & APIs  
**Difficulty:** ⭐⭐⭐⭐ Expert

Build a client for a public API.

**Requirements:**
- Fetch data from API
- Parse JSON response
- Handle errors
- Cache responses

---

### Exercise 032: Web Scraper
**Topic:** BeautifulSoup & Requests  
**Difficulty:** ⭐⭐⭐⭐ Expert

Scrape data from a website.

**Requirements:**
- Fetch webpage
- Extract specific data
- Save to CSV
- Respect robots.txt

---

### Exercise 033: REST API with FastAPI
**Topic:** FastAPI  
**Difficulty:** ⭐⭐⭐⭐ Expert

Create a REST API for a blog.

**Requirements:**
- CRUD operations for posts
- User authentication
- Input validation
- Database integration

---

## Running Exercises

```bash
# Run a specific exercise
python exercises/001_hello_user.py

# Validate solution
python tools/validate.py 001

# Run all tests
pytest tests/ -v
```

---

## Getting Help

- **Hints:** Check `hints/` folder for each exercise
- **Solutions:** Reference solutions in `solutions/` folder
- **Discussions:** Open an issue for questions

---

## Progress Tracking

Track your completed exercises:

```bash
python tools/progress.py mark 001
python tools/progress.py status
```

---

**Next Steps:** After completing exercises, move to [Capstone Projects](../projects/README.md)
