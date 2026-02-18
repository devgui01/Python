---
title: "FEATURE: Add cheat sheets for quick reference"
labels: ["enhancement", "documentation", "good first issue"]
assignees: []
---

## Feature Description

Create quick-reference cheat sheets for each major topic. These one-page summaries help learners quickly look up syntax and concepts.

## Current State

No quick reference materials exist. Learners must read through full examples to find specific syntax.

## Proposed Cheat Sheets

### 1. Python Basics Cheat Sheet

```markdown
# 🐍 Python Basics - Quick Reference

## Variables & Data Types

```python
# Variable assignment
name = "Alice"           # str
age = 25                 # int
height = 5.9             # float
is_student = False       # bool

# Type checking
type(name)               # <class 'str'>
isinstance(age, int)     # True

# Type conversion
int("5")                 # 5
str(100)                 # "100"
float("3.14")            # 3.14
```

## Operators

```python
# Arithmetic
+  -  *  /               # Add, subtract, multiply, divide
//                       # Floor division (5 // 2 = 2)
%                        # Modulus (5 % 2 = 1)
**                       # Exponent (2 ** 3 = 8)

# Comparison
==  !=  >  <  >=  <=     # Equal, not equal, greater, less, etc.

# Logical
and  or  not             # Logical operators

# Assignment
=  +=  -=  *=  /=        # Assignment operators
```

## Strings

```python
# Creation
text = "Hello"
text = 'Hello'
text = """Multi
line"""

# Slicing
text[0]                  # 'H'
text[1:4]                # 'ell'
text[-1]                 # 'o'
text[::-1]               # Reverse

# Methods
text.lower()             # 'hello'
text.upper()             # 'HELLO'
text.strip()             # Remove whitespace
text.replace('l', 'x')   # 'Hexxo'
text.split()             # ['Hello']
','.join(['a', 'b'])     # 'a,b'
len(text)                # 5
```

## Lists

```python
# Creation
numbers = [1, 2, 3, 4, 5]

# Access
numbers[0]               # 1
numbers[-1]              # 5
numbers[1:3]             # [2, 3]

# Methods
numbers.append(6)        # Add to end
numbers.insert(0, 0)     # Insert at index
numbers.remove(3)        # Remove value
numbers.pop()            # Remove last
numbers.sort()           # Sort
numbers.reverse()        # Reverse

# Comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

## Dictionaries

```python
# Creation
person = {"name": "Alice", "age": 25}

# Access
person["name"]           # 'Alice'
person.get("age")        # 25
person.get("job", "N/A") # 'N/A' (default)

# Methods
person.keys()            # dict_keys(['name', 'age'])
person.values()          # dict_values(['Alice', 25])
person.items()           # dict_items([...])
person.update({"job": "Dev"})  # Add/update
```

## Control Flow

```python
# If-elif-else
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
else:
    print("Adult")

# For loop
for i in range(5):       # 0 to 4
    print(i)

for item in [1, 2, 3]:
    print(item)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
break                    # Exit loop
continue                 # Next iteration
```

## Functions

```python
# Definition
def greet(name):
    return f"Hello, {name}"

# Default arguments
def greet(name="Guest"):
    return f"Hello, {name}"

# Variable arguments
def sum_all(*args):
    return sum(args)

# Keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x ** 2
```

## File I/O

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()

# Write
with open("file.txt", "w") as f:
    f.write("Hello")

# Append
with open("file.txt", "a") as f:
    f.write("More text")

# Read lines
with open("file.txt") as f:
    for line in f:
        print(line)
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors")
finally:
    print("Always runs")
```

## Classes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

# Inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
```
```

### 2. FastAPI Cheat Sheet

```markdown
# ⚡ FastAPI - Quick Reference

## Basic App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## Run Server

```bash
uvicorn main:app --reload
# Docs: http://127.0.0.1:8000/docs
```

## Path Parameters

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

## Query Parameters

```python
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

## Request Body

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return item
```

## Response Model

```python
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
```

## Status Codes

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item():
    pass
```

## Error Handling

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
```

## Dependencies

```python
async def common_params(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_params)):
    return commons
```

## Authentication

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Validate token
    return {"token": token}
```
```

### 3. Data Structures Cheat Sheet

```markdown
# 📊 Python Data Structures - Quick Reference

## When to Use What

| Structure | Use Case | Ordered | Mutable | Indexed |
|-----------|----------|---------|---------|---------|
| list      | Ordered collection | ✅ | ✅ | ✅ |
| tuple     | Immutable data | ✅ | ❌ | ✅ |
| set       | Unique items | ❌ | ✅ | ❌ |
| dict      | Key-value pairs | ✅* | ✅ | Keys |
| frozenset | Immutable set | ❌ | ❌ | ❌ |

*Python 3.7+ maintains insertion order

## List Operations

```python
# Create
my_list = [1, 2, 3]
my_list = list(range(5))

# Add
my_list.append(4)          # [1, 2, 3, 4]
my_list.insert(0, 0)       # [0, 1, 2, 3, 4]
my_list.extend([5, 6])     # [0, 1, 2, 3, 4, 5, 6]

# Remove
my_list.pop()              # Remove last
my_list.pop(0)             # Remove at index
my_list.remove(3)          # Remove by value
del my_list[0]             # Delete at index

# Access
my_list[0]                 # First element
my_list[-1]                # Last element
my_list[1:3]               # Slice

# Other
len(my_list)               # Length
my_list.count(2)           # Count occurrences
my_list.index(3)           # Find index
```

## Dictionary Operations

```python
# Create
my_dict = {"a": 1, "b": 2}
my_dict = dict(a=1, b=2)
my_dict = {k: v for k, v in pairs}

# Access
my_dict["a"]               # 1
my_dict.get("a")           # 1
my_dict.get("c", 0)        # 0 (default)

# Modify
my_dict["c"] = 3           # Add/update
my_dict.update({"d": 4})   # Bulk update

# Remove
del my_dict["a"]           # Delete
my_dict.pop("b")           # Remove and return
my_dict.popitem()          # Remove last

# Iterate
for key in my_dict:        # Keys
    pass

for value in my_dict.values():  # Values
    pass

for key, value in my_dict.items():  # Both
    pass
```

## Set Operations

```python
# Create
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

# Add
my_set.add(4)
my_set.update([5, 6])

# Remove
my_set.remove(3)           # Error if not exists
my_set.discard(3)          # No error
my_set.pop()               # Remove random

# Operations
set1 | set2                # Union
set1 & set2                # Intersection
set1 - set2                # Difference
set1 ^ set2                # Symmetric difference

# Comparison
set1.issubset(set2)        # ⊆
set1.issuperset(set2)      # ⊇
set1.isdisjoint(set2)      # No common elements
```
```

## Files to Create

- [ ] `cheatsheets/python_basics.md`
- [ ] `cheatsheets/data_structures.md`
- [ ] `cheatsheets/fastapi.md`
- [ ] `cheatsheets/flask.md`
- [ ] `cheatsheets/oop.md`
- [ ] `cheatsheets/file_handling.md`
- [ ] `cheatsheets/error_handling.md`
- [ ] `cheatsheets/README.md` (index)

## Format

Each cheat sheet should:
- Fit on 1-2 pages
- Use clear headings
- Include code examples
- Show common patterns
- Link to full documentation

## Distribution

- Print-friendly PDFs
- Include in repository
- Link from main README
- Add to documentation

## Benefits

- ✅ Quick reference
- ✅ Memory aid
- ✅ Print-friendly
- ✅ Interview prep
- ✅ On-the-job reference
