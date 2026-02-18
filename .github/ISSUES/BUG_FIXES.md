# 🐛 Bug Fixes Needed

Critical and important bugs that need fixing.

---

## 🔴 Critical Bugs (Fix Immediately)

### #BUG001 - Prime Checker Has Logic Error
**Severity:** 🔴 Critical  
**File:** `basics/03_control_flow/02_check_prime.py`  
**Difficulty:** ⭐ Easy

**Problem:**
The prime number checker returns incorrect results - it says prime numbers are not prime and vice versa.

**Current behavior:**
```python
# Lines 13-16 have inverted logic
if(prime):
    prime = False  # Bug! This makes primes return False
else:
    prime = True   # Bug! This makes non-primes return True
```

**Expected behavior:**
- `is_prime(7)` should return `True`
- `is_prime(10)` should return `False`

**Fix:**
Remove lines 13-16 entirely. The logic before this already correctly sets the `prime` variable.

**Acceptance criteria:**
- [ ] Remove inverted logic block
- [ ] Test with primes: 2, 3, 5, 7, 11 → should return `True`
- [ ] Test with non-primes: 4, 6, 8, 9, 10 → should return `False`
- [ ] Test edge cases: 0, 1, negative → should return `False`

---

### #BUG002 - Function Named 'sum' Performs Division
**Severity:** 🔴 Critical  
**File:** `basics/09_error_handling/01_try_except.py`  
**Difficulty:** ⭐ Easy

**Problem:**
Function named `sum` actually performs division, which is misleading and confusing.

**Current code:**
```python
def sum(a: int, b: int) -> int:  # Name suggests addition
    result = a / b                # But performs division!
    return result
```

**Fix:**
Rename function to `divide` and update return type to `float`.

**Acceptance criteria:**
- [ ] Rename function from `sum` to `divide`
- [ ] Update return type hint to `float`
- [ ] Update all function calls
- [ ] Add docstring

---

### #BUG003 - Guess Number Game Crashes on Invalid Input
**Severity:** 🔴 Critical  
**File:** `basics/11_projects/01_guess_number.py`  
**Difficulty:** ⭐⭐ Easy-Medium

**Problem:**
Game crashes when user enters non-integer input.

**Current code:**
```python
user_input = int(input(f"Guess the Number: "))  # Crashes on "abc"
```

**Fix:**
Add try/except block to handle `ValueError`.

**Acceptance criteria:**
- [ ] Catch `ValueError` around `int()` conversion
- [ ] Display friendly error message
- [ ] Allow user to try again without crashing
- [ ] Test with: "abc", "12.5", "", special characters

---

### #BUG004 - Rock Paper Scissors Crashes on Invalid Input
**Severity:** 🔴 Critical  
**File:** `basics/11_projects/03_rock_paper_scissors.py`  
**Difficulty:** ⭐⭐ Easy-Medium

**Problem:**
Game doesn't validate input before using `.upper()` and crashes on invalid choices.

**Fix:**
Add input validation loop to ensure input is R, P, or S.

**Acceptance criteria:**
- [ ] Validate input is one of R, P, S
- [ ] Loop until valid input received
- [ ] Fix typo: "Wents" → "Went"
- [ ] Add case-insensitive handling

---

### #BUG005 - File Examples Reference Non-Existent Files
**Severity:** 🔴 Critical  
**Files:** Multiple in `basics/07_file_handling/`  
**Difficulty:** ⭐⭐ Easy-Medium

**Problem:**
Examples reference files like `poems.txt`, `newfile.txt` without creating them first.

**Affected files:**
- `01_file_handling_basics.py` - `newfile.txt`
- `07_file_find_word.py` - `poems.txt`
- `11_file_copy.py` - `this.txt`

**Fix:**
Add file existence check and create sample files if missing.

**Acceptance criteria:**
- [ ] Add `os.path.exists()` checks before reading
- [ ] Create sample files if they don't exist
- [ ] Add comment explaining the check
- [ ] Test on fresh clone (no existing files)

---

## 🟡 High Priority Bugs

### #BUG006 - Division by Zero in Average Calculation
**Severity:** 🟡 High  
**File:** `basics/02_variables_types/02_average.py`  
**Difficulty:** ⭐ Easy

**Problem:**
No validation to prevent division by zero if user enters 0.

**Fix:**
Add check for zero before division.

---

### #BUG007 - Infinite Loop in While Example
**Severity:** 🟡 High  
**File:** `basics/03_control_flow/03_for_while_loops.py`  
**Difficulty:** ⭐ Easy

**Problem:**
One of the while loop examples doesn't increment counter, causing infinite loop.

**Fix:**
Ensure counter is incremented in all while loops.

---

### #BUG008 - List Index Out of Range
**Severity:** 🟡 High  
**File:** `basics/05_data_structures/02_list_fruits.py`  
**Difficulty:** ⭐ Easy

**Problem:**
Code tries to access list indices that don't exist if user enters fewer than 7 fruits.

**Fix:**
Add length check before accessing indices or use `.append()`.

---

### #BUG009 - KeyError in Dictionary Example
**Severity:** 🟡 High  
**File:** `basics/05_data_structures/16_dict_basics.py`  
**Difficulty:** ⭐ Easy

**Problem:**
Accessing dictionary key that doesn't exist without using `.get()`.

**Fix:**
Use `.get()` method or check key existence first.

---

### #BUG010 - Type Error in String Concatenation
**Severity:** 🟡 High  
**File:** `basics/06_strings/03_string_format.py`  
**Difficulty:** ⭐ Easy

**Problem:**
Trying to concatenate string with integer without conversion.

**Fix:**
Convert integers to strings with `str()`.

---

## 🟢 Medium Priority Bugs

### #BUG011 - Inconsistent Output Formatting
**Severity:** 🟢 Medium  
**Files:** Multiple  
**Difficulty:** ⭐ Easy

**Problem:**
Output messages have inconsistent formatting (some with spaces, some without).

**Fix:**
Standardize output format across all examples.

---

### #BUG012 - Missing Error Messages
**Severity:** 🟢 Medium  
**Files:** `basics/09_error_handling/*.py`  
**Difficulty:** ⭐ Easy

**Problem:**
Some error handlers don't display helpful error messages.

**Fix:**
Add descriptive error messages to all exception handlers.

---

### #BUG013 - Hardcoded File Paths
**Severity:** 🟢 Medium  
**Files:** File handling examples  
**Difficulty:** ⭐⭐ Easy-Medium

**Problem:**
Some examples use absolute paths that won't work on other systems.

**Fix:**
Use relative paths or `pathlib.Path`.

---

### #BUG014 - Magic Numbers in Code
**Severity:** 🟢 Medium  
**Files:** Multiple  
**Difficulty:** ⭐ Easy

**Problem:**
Unexplained numbers like `0.5`, `100`, `1000` without context.

**Fix:**
Replace with named constants and add comments.

---

### #BUG015 - Inconsistent Variable Naming
**Severity:** 🟢 Medium  
**Files:** Multiple  
**Difficulty:** ⭐ Easy

**Problem:**
Some files use `camelCase`, others use `snake_case`.

**Fix:**
Standardize on `snake_case` per Python conventions.

---

## 🔵 Low Priority Bugs

### #BUG016 - Typos in Comments
**Severity:** 🔵 Low  
**Files:** Multiple  
**Difficulty:** ⭐ Easy

**Problem:**
Spelling mistakes in code comments.

**Fix:**
Proofread and correct all comments.

---

### #BUG017 - Outdated Examples
**Severity:** 🔵 Low  
**Files:** `basics/10_advanced/`  
**Difficulty:** ⭐ Easy

**Problem:**
Some examples use outdated Python 2 syntax.

**Fix:**
Update to Python 3 syntax.

---

### #BUG018 - Missing Period in Print Statements
**Severity:** 🔵 Low  
**Files:** Multiple  
**Difficulty:** ⭐ Easy

**Problem:**
Some output messages don't end with periods.

**Fix:**
Add periods for consistency.

---

## 📊 Bug Status

| ID | Status | Assignee | PR |
|----|--------|----------|-----|
| #BUG001 | 🔴 Open | - | - |
| #BUG002 | 🔴 Open | - | - |
| #BUG003 | 🔴 Open | - | - |
| #BUG004 | 🔴 Open | - | - |
| #BUG005 | 🔴 Open | - | - |
| #BUG006 | 🟡 Open | - | - |
| #BUG007 | 🟡 Open | - | - |
| #BUG008 | 🟡 Open | - | - |
| #BUG009 | 🟡 Open | - | - |
| #BUG010 | 🟡 Open | - | - |

---

## 🐛 How to Report a Bug

Found a bug not on this list?

1. **Check existing issues** - It might already be reported
2. **Open new issue** - Use bug report template
3. **Include:**
   - File path
   - Expected behavior
   - Actual behavior
   - Steps to reproduce
   - Python version
   - Error message (if any)

---

## 🏆 Bug Hunter Recognition

Fix 5+ bugs and receive:
- "Bug Hunter" badge on GitHub
- Featured in CONTRIBUTORS.md
- Special thanks in release notes

---

**Help us squash bugs and make this resource better for everyone! 🐛🔨**
