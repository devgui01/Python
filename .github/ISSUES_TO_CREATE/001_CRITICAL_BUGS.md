# 🔴 CRITICAL BUGS - Priority: HIGH

---

## Issue #1: Prime Number Checker Has Inverted Logic

### Title
[BUG]: Prime number checker returns incorrect results

### Description

**What:** The prime number checking algorithm in `basics/03_control_flow/02_check_prime.py` has a critical logic error that inverts the final result.

**Why it matters:** Students learning from this example will be taught incorrect logic. The program returns `False` for prime numbers and `True` for non-prime numbers.

**Where:** `basics/03_control_flow/02_check_prime.py`, lines 13-16

**Current behavior:**
```python
# Lines 13-16 - Logic is inverted
if(prime):
    prime = False  # Bug: This makes primes return False!
else:
    prime = True   # Bug: This makes non-primes return True!
```

**Expected behavior:**
- Input `7` should return `True` (is prime)
- Input `10` should return `False` (not prime)

**Suggested approach:**
Remove lines 13-16 entirely. The logic before this already correctly sets the `prime` variable.

**Acceptance criteria:**
- [ ] Remove the inverted logic block (lines 13-16)
- [ ] Test with prime numbers: 2, 3, 5, 7, 11 → should return `True`
- [ ] Test with non-prime numbers: 4, 6, 8, 9, 10 → should return `False`
- [ ] Test edge cases: 0, 1, negative numbers → should return `False`

**Labels:** `bug`, `priority: high`, `good first issue`

---

## Issue #2: Function Named 'sum' Performs Division

### Title
[BUG]: Function `sum()` in error handling example performs division instead of addition

### Description

**What:** In `basics/09_error_handling/01_try_except.py`, the function named `sum` actually performs division, which is misleading and confusing.

**Why it matters:** This violates basic naming conventions and will confuse beginners learning about functions and error handling.

**Where:** `basics/09_error_handling/01_try_except.py`, lines 1-3

**Current behavior:**
```python
def sum(a: int, b: int) -> int:  # Name suggests addition
    result = a / b                # But performs division!
    return result
```

**Expected behavior:** Function name should match its operation.

**Suggested approach:**
Rename the function to `divide` and update the type hint to return `float`:

```python
def divide(a: int, b: int) -> float:
    result = a / b
    return result
```

**Acceptance criteria:**
- [ ] Rename function from `sum` to `divide`
- [ ] Update return type hint to `float`
- [ ] Update function call on line 16
- [ ] Add docstring explaining the function

**Labels:** `bug`, `refactor`, `good first issue`, `priority: medium`

---

## Issue #3: No Input Validation in Guess Number Game

### Title
[BUG]: Guess number game crashes on non-integer input

### Description

**What:** The guess number game (`basics/11_projects/01_guess_number.py`) has no try/except handling for invalid input, causing crashes when users enter non-integer values.

**Why it matters:** Poor user experience - the game crashes instead of prompting for valid input.

**Where:** `basics/11_projects/01_guess_number.py`, line 10

**Current behavior:**
```python
user_input = int(input(f"Guess the Number: "))  # Crashes on "abc"
```

**Expected behavior:** Should catch `ValueError` and prompt user to enter a valid number.

**Suggested approach:**
Wrap the input in a try/except block:

```python
try:
    user_input = int(input(f"Guess the Number: "))
except ValueError:
    print("Please enter a valid number!")
    continue
```

**Acceptance criteria:**
- [ ] Add ValueError handling around int() conversion
- [ ] Display friendly error message on invalid input
- [ ] Allow user to try again without crashing
- [ ] Test with inputs: "abc", "12.5", "", special characters

**Labels:** `bug`, `enhancement`, `good first issue`

---

## Issue #4: Rock Paper Scissors Has No Input Validation

### Title
[BUG]: Rock paper scissors game crashes on invalid input

### Description

**What:** The rock-paper-scissors game (`basics/11_projects/03_rock_paper_scissors.py`) doesn't validate user input before using `.upper()` and doesn't handle invalid choices.

**Why it matters:** Game returns "Something Wents Wrong" for any input other than R, P, S.

**Where:** `basics/11_projects/03_rock_paper_scissors.py`, lines 10-26

**Suggested approach:**
Add input validation loop:

```python
while True:
    userinput = input("R - Rock\nP - Paper\nS - Scissor\nChoose: ").upper()
    if userinput in ["R", "P", "S"]:
        break
    print("Invalid choice! Please choose R, P, or S.")
```

**Acceptance criteria:**
- [ ] Validate input is one of R, P, S
- [ ] Loop until valid input is received
- [ ] Fix typo: "Wents" → "Went"
- [ ] Add case-insensitive handling

**Labels:** `bug`, `enhancement`, `good first issue`

---

## Issue #5: File Handling Examples Use Non-Existent Files

### Title
[BUG]: File handling examples reference files that don't exist

### Description

**What:** Multiple file handling examples reference files like `poems.txt`, `newfile.txt` without checking if they exist first or creating them.

**Why it matters:** Examples fail when run, confusing beginners.

**Where:** 
- `basics/07_file_handling/01_file_handling_basics.py` - `newfile.txt`
- `basics/07_file_handling/07_file_find_word.py` - `poems.txt`

**Suggested approach:**
Add file existence check and creation:

```python
import os

filename = "poems.txt"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Twinkle, twinkle, little star...")
```

**Acceptance criteria:**
- [ ] Add os.path.exists() checks before reading
- [ ] Create sample files if they don't exist
- [ ] Add comment explaining the check
- [ ] Test on fresh clone (no existing files)

**Labels:** `bug`, `enhancement`, `good first issue`

---
