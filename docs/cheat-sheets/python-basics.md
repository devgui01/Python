# Python Cheat Sheet

Quick reference for Python syntax and common operations.

---

## Basics

### Variables & Data Types
```python
# Variables (no declaration needed)
name = "Alice"           # String
age = 25                 # Integer
height = 5.9             # Float
is_student = True        # Boolean
hobbies = ["reading"]    # List
person = {"name": "Bob"} # Dictionary
coordinates = (10, 20)   # Tuple
unique_nums = {1, 2, 3}  # Set

# Type checking
type(name)      # <class 'str'>
isinstance(age, int)  # True

# Type conversion
int("42")       # 42
str(42)         # "42"
float(5)        # 5.0
list("abc")     # ['a', 'b', 'c']
```

### Operators
```python
# Arithmetic
+  -  *  /      # Add, subtract, multiply, divide
//              # Floor division (5 // 2 = 2)
%               # Modulus/remainder (5 % 2 = 1)
**              # Exponentiation (2 ** 3 = 8)

# Comparison
==  !=  >  <  >=  <=

# Logical
and  or  not

# Assignment
=  +=  -=  *=  /=  //=  %=  **=
```

---

## Control Flow

### If-Elif-Else
```python
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Ternary operator
status = "adult" if age >= 18 else "minor"
```

### Loops
```python
# For loop
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
break       # Exit loop
continue    # Skip to next iteration
else        # Run when loop completes (no break)
```

---

## Data Structures

### Lists
```python
fruits = ["apple", "banana", "orange"]

# Access
fruits[0]        # "apple"
fruits[-1]       # "orange" (last)
fruits[1:3]      # ["banana", "orange"]

# Modify
fruits.append("grape")      # Add to end
fruits.insert(1, "mango")   # Insert at index
fruits.extend(["kiwi"])     # Add multiple
fruits.remove("banana")     # Remove by value
popped = fruits.pop()       # Remove and return last
fruits.pop(0)               # Remove at index

# Other
len(fruits)                 # Length
"apple" in fruits           # True
fruits.index("orange")      # Find index
fruits.count("apple")       # Count occurrences
fruits.sort()               # Sort in place
sorted(fruits)              # Return sorted copy
fruits.reverse()            # Reverse in place

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Dictionaries
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Access
person["name"]          # "Alice"
person.get("age")       # 25
person.get("job", "N/A") # "N/A" (default)

# Modify
person["age"] = 26              # Update
person["job"] = "Engineer"      # Add new
del person["city"]              # Delete

# Methods
person.keys()       # dict_keys(['name', 'age', 'job'])
person.values()     # dict_values(['Alice', 26, 'Engineer'])
person.items()      # dict_items([('name', 'Alice'), ...])

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

### Tuples
```python
coordinates = (10, 20)
point = 30, 40          # Parentheses optional
single = (5,)           # Comma required for single item

# Access
x, y = coordinates      # Unpacking
coordinates[0]          # 10

# Immutable - cannot modify after creation
# coordinates[0] = 15   # ERROR!
```

### Sets
```python
unique = {1, 2, 3, 3, 2}  # {1, 2, 3}

# Operations
unique.add(4)             # Add element
unique.remove(2)          # Remove (error if missing)
unique.discard(5)         # Remove (no error)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

a | b    # Union: {1, 2, 3, 4, 5}
a & b    # Intersection: {3}
a - b    # Difference: {1, 2}
a ^ b    # Symmetric difference: {1, 2, 4, 5}
```

---

## Functions

### Defining Functions
```python
def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"

# Call
greet("Alice")                  # "Hello, Alice!"
greet("Bob", "Hi")              # "Hi, Bob!"
greet(name="Charlie")           # "Hello, Charlie!"

# Default arguments
def create_user(name, role="user"):
    pass

# Variable arguments
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# Keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

# Lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y
```

---

## String Operations

```python
text = "  Hello, World!  "

# Case
text.upper()        # "  HELLO, WORLD!  "
text.lower()        # "  hello, world!  "
text.title()        # "  Hello, World!  "
text.capitalize()   # "  hello, world!  "

# Strip whitespace
text.strip()        # "Hello, World!"
text.lstrip()       # "Hello, World!  "
text.rstrip()       # "  Hello, World!"

# Search
text.find("World")  # 9
text.count("l")     # 3
text.startswith(" ") # True
text.endswith("!")   # True

# Replace
text.replace("World", "Python")

# Split & Join
"apple,banana,cherry".split(",")  # ['apple', 'banana', 'cherry']
"-".join(["a", "b", "c"])         # "a-b-c"

# Format
name = "Alice"
age = 25
f"Name: {name}, Age: {age}"       # "Name: Alice, Age: 25"
"{} is {}".format(name, age)      # "Alice is 25"

# Slice
text[0:5]     # "  Hel"
text[-6:-1]   # "World"
text[::-1]    # Reverse string
```

---

## File Handling

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Write to file
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Append to file
with open("file.txt", "a") as f:
    f.write("\nMore content")

# Modes: r (read), w (write), a (append), b (binary)
```

---

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")
finally:
    print("Always runs")

# Raise exceptions
raise ValueError("Invalid value!")

# Custom exceptions
class MyError(Exception):
    pass
```

---

## Classes (OOP)

```python
class Person:
    # Class attribute
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    @classmethod
    def get_species(cls):
        return cls.species

# Inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    # Override method
    def greet(self):
        return f"Hi, I'm {self.name}, a student"

# Usage
person = Person("Alice", 25)
person.greet()
Person.is_adult(20)
```

---

## Modules & Imports

```python
# Import entire module
import math
math.sqrt(16)

# Import specific functions
from math import sqrt, pi
sqrt(16)

# Import with alias
import numpy as np
import pandas as pd

# Import from local file
from mymodule import my_function
```

---

## Built-in Functions

```python
# Common built-ins
len()       # Length
range()     # Generate sequence
sum()       # Sum of iterable
min()       # Minimum value
max()       # Maximum value
abs()       # Absolute value
round()     # Round number
int()       # Convert to int
str()       # Convert to string
list()      # Convert to list
dict()      # Create dictionary
set()       # Create set
zip()       # Combine iterables
enumerate() # Add counter to iterable
map()       # Apply function to all items
filter()    # Filter items by function
sorted()    # Return sorted copy
reversed()  # Return reversed iterator
```

---

## Useful One-Liners

```python
# Reverse a list
reversed_list = my_list[::-1]

# Remove duplicates
unique = list(set(my_list))

# Flatten nested list
flattened = [item for sublist in nested for item in sublist]

# Count word frequency
word_count = {word: text.split().count(word) for word in set(text.split())}

# Check if all elements meet condition
all_positive = all(x > 0 for x in numbers)

# Check if any element meets condition
any_negative = any(x < 0 for x in numbers)

# Swap variables
a, b = b, a

# Merge dictionaries
merged = {**dict1, **dict2}

# Remove falsy values from list
filtered = list(filter(None, my_list))
```

---

**Quick Reference Card** | Print this page for offline use!
