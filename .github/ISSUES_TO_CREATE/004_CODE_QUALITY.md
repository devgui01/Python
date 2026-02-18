# 🔧 CODE QUALITY & REFACTORING - Priority: MEDIUM

---

## Issue #18: Inconsistent Naming Conventions

### Title
[REFACTOR]: Standardize naming conventions across codebase

### Description

**What:** Files and variables use inconsistent naming conventions (camelCase, snake_case, PascalCase mixed).

**Why it matters:** 
- Confusing for learners
- Violates PEP 8 style guide
- Makes code harder to read

**Where:** Throughout the codebase

**Examples of issues:**
```python
# basics/08_oop/01_class_basics.py
isLifeexist = "Nope"      # Should be: is_life_exists
nearSun = False           # Should be: near_sun
power = 100               # OK

# basics/03_control_flow/02_check_prime.py
prime = False             # OK
random_number = ...       # OK
user_input = ...          # OK
```

**Expected behavior:** All Python code should follow PEP 8:
- Variables/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`

**Suggested approach:**
1. Run automated refactoring tool (e.g., `pyupgrade`, `black`)
2. Manual review for semantic improvements
3. Update all references

**Acceptance criteria:**
- [ ] Rename all variables to snake_case
- [ ] Rename all classes to PascalCase
- [ ] Update all references
- [ ] Add linting to CI/CD
- [ ] Document naming conventions in CONTRIBUTING.md

**Labels:** `refactor`, `code quality`, `priority: medium`

---

## Issue #19: Magic Numbers Without Explanation

### Title
[REFACTOR]: Replace magic numbers with named constants

### Description

**What:** Code contains unexplained numeric literals (magic numbers).

**Why it matters:** 
- Hard to understand intent
- Difficult to maintain
- Error-prone when changes needed

**Where:** Multiple files

**Examples:**
```python
# basics/03_control_flow/02_check_prime.py
for i in range(2, int(num * 0.5) + 1):  # Why 0.5?

# llm_fundamentals/architecture/01_transformer_architecture.py
GPT_CONFIG_500M = {
    "vocab_size": 200256,    # Why this number?
    "context_length": 1024,  # Why 1024?
    "emb_dim": 768,          # Why 768?
}

# basics/11_projects/01_guess_number.py
random_number = random.randint(1, 100)  # OK, but could be named
```

**Suggested approach:**
```python
# Good
PRIME_CHECK_FACTOR = 0.5
DEFAULT_RANGE_MIN = 1
DEFAULT_RANGE_MAX = 100

for i in range(2, int(num * PRIME_CHECK_FACTOR) + 1):
    ...
```

**Acceptance criteria:**
- [ ] Identify all magic numbers > 1
- [ ] Create named constants with explanations
- [ ] Replace literals with constants
- [ ] Add comments explaining non-obvious values
- [ ] Group related constants together

**Labels:** `refactor`, `code quality`, `good first issue`

---

## Issue #20: Code Duplication in Rock Paper Scissors

### Title
[REFACTOR]: Eliminate code duplication in rock-paper-scissors game

### Description

**What:** The game logic has repetitive if/elif blocks that could be simplified.

**Why it matters:** 
- Violates DRY principle
- Hard to maintain
- Easy to introduce bugs

**Where:** `basics/11_projects/03_rock_paper_scissors.py`, lines 11-26

**Current behavior:**
```python
if(userinput == "R" and comp == "P"):
    output = "You Lose, Try Again"
elif(userinput == "R" and comp == "S"):
    output = "You Won"
elif(userinput == "S" and comp == "R"):
    output = "You Lose, Try Again"
# ... 6 total conditions
```

**Suggested approach:**
Use a dictionary-based approach:

```python
WIN_CONDITIONS = {
    ("R", "S"): "You Won",
    ("S", "P"): "You Won",
    ("P", "R"): "You Won",
}

if userinput == comp:
    output = "Draw"
elif (userinput, comp) in WIN_CONDITIONS:
    output = WIN_CONDITIONS[(userinput, comp)]
else:
    output = "You Lose, Try Again"
```

**Acceptance criteria:**
- [ ] Replace if/elif chain with dictionary lookup
- [ ] Reduce lines of code by 50%
- [ ] Add unit tests for all combinations
- [ ] Make win/lose messages configurable

**Labels:** `refactor`, `code quality`, `good first issue`

---

## Issue #21: Missing Type Hints in Most Files

### Title
[REFACTOR]: Add type hints to all functions

### Description

**What:** Most Python files lack type hints, making code harder to understand and debug.

**Why it matters:** 
- Harder to catch type errors
- Poor IDE autocomplete
- Not following modern Python best practices

**Where:** Throughout basics/ folder

**Examples:**
```python
# Current
def add():
    a = int(input("Enter the Number: "))
    b = int(input("Enter the Number: "))
    sum = a + b
    print(sum)

# Should be
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b
```

**Suggested approach:**
1. Add type hints to all function parameters
2. Add return type annotations
3. Use `Optional`, `Union`, `List` where appropriate
4. Run mypy to validate

**Acceptance criteria:**
- [ ] Add type hints to all functions in basics/
- [ ] Add docstrings to all functions
- [ ] Configure mypy in CI/CD
- [ ] Fix all type errors
- [ ] Document type hint standards

**Labels:** `refactor`, `code quality`, `priority: medium`

---

## Issue #22: Overly Complex Functions

### Title
[REFACTOR]: Break down complex functions into smaller units

### Description

**What:** Several functions are too long and do too many things.

**Why it matters:** 
- Hard to test
- Hard to understand
- Violates single responsibility principle

**Where:** Multiple files

**Examples:**
```python
# basics/11_projects/01_guess_number.py - Multiplayer function
def Multiplayer():
    # Does too many things:
    # 1. Manages game loop
    # 2. Tracks guesses
    # 3. Determines winner
    # 4. Prints results
    ...
```

**Suggested approach:**
Split into smaller functions:

```python
def play_single_game() -> int:
    """Play one game and return number of guesses."""
    ...

def track_player_guesses(player_num: int) -> dict:
    """Track guesses for one player."""
    ...

def determine_winner(guesses: dict) -> str:
    """Determine the winner based on guesses."""
    ...

def multiplayer_mode():
    """Orchestrate multiplayer game."""
    guesses = {}
    for i in range(2):
        guesses[f"Player {i}"] = track_player_guesses(i)
    winner = determine_winner(guesses)
    print_winner(winner)
```

**Acceptance criteria:**
- [ ] No function longer than 30 lines
- [ ] Each function has single responsibility
- [ ] Add docstrings to all functions
- [ ] Maintain same functionality
- [ ] Add tests for each new function

**Labels:** `refactor`, `code quality`, `priority: medium`

---

## Issue #23: Using Built-in Names as Variables

### Title
[REFACTOR]: Avoid using Python built-in names as variables

### Description

**What:** Code uses Python built-in names (sum, list, dict, etc.) as variable names.

**Why it matters:** 
- Shadows built-in functions
- Can cause subtle bugs
- Confusing for learners

**Where:** Multiple files

**Examples:**
```python
# basics/04_functions/01_functions_basics.py
def add():
    sum = a + b  # Shadows built-in sum()!
    print(sum)

# basics/05_data_structures/01_list_basics.py
isFoods = [...]  # Confusing name
```

**Suggested approach:**
```python
# Good
def add():
    total = a + b
    print(total)

# Good
foods = [...]
```

**Acceptance criteria:**
- [ ] Find all uses of built-in names (sum, list, dict, str, int, etc.)
- [ ] Rename to descriptive alternatives
- [ ] Update all references
- [ ] Add to code review checklist

**Labels:** `refactor`, `code quality`, `good first issue`

---

## Issue #24: Inconsistent Error Messages

### Title
[REFACTOR]: Standardize error message format

### Description

**What:** Error messages have inconsistent formatting, capitalization, and tone.

**Why it matters:** 
- Unprofessional appearance
- Confusing for users
- Hard to internationalize later

**Where:** Throughout codebase

**Examples:**
```python
"A Number Can't be Divide by Zero"     # basics/09_error_handling/01_try_except.py
"Enter a Valid Number!"                # Inconsistent capitalization
"Something Wrong Happen!"              # Grammar error
"Something Wents Wrong"                # Grammar error + inconsistency
```

**Suggested approach:**
Standardize on sentence case, no exclamation marks:

```python
"Number cannot be divided by zero"
"Please enter a valid number"
"An error occurred"
```

**Acceptance criteria:**
- [ ] Create error message style guide
- [ ] Update all error messages
- [ ] Use consistent capitalization
- [ ] Fix grammar errors
- [ ] Remove exclamation marks

**Labels:** `refactor`, `code quality`, `good first issue`

---

## Issue #25: Dead Code and Commented-Out Blocks

### Title
[REFACTOR]: Remove dead code and commented-out blocks

### Description

**What:** Codebase contains commented-out code and unreachable blocks.

**Why it matters:** 
- Clutters codebase
- Confuses readers
- Version control already preserves history

**Where:** Multiple files

**Examples:**
```python
# llm_fundamentals/weight_loading/03_gpt_download.py
"""
def download_file(url, destination):
    # 70 lines of commented-out code
"""

# basics/08_oop/01_class_basics.py
# Neptune.Power()  # Both are same
# Planets.Power(Neptune)
```

**Suggested approach:**
1. Delete all commented-out code blocks
2. If explanation needed, add brief comment
3. Git history preserves the code if needed

**Acceptance criteria:**
- [ ] Remove all multi-line commented code blocks
- [ ] Keep only explanatory single-line comments
- [ ] Verify no functionality is removed
- [ ] Run tests after cleanup

**Labels:** `refactor`, `code quality`, `good first issue`

---
