---
title: "ENHANCEMENT: Add comprehensive type hints throughout codebase"
labels: ["enhancement", "type hints", "intermediate"]
assignees: []
---

## Enhancement Description

Many Python files lack type hints, making it harder for learners to understand expected types and for tools to catch type-related bugs.

## Current State

Mixed type hint usage:
- Some files have type hints (e.g., `01_try_except.py`)
- Many files have no type hints
- Inconsistent usage patterns
- Some incorrect type hints

## Examples of Current Issues

### File with type hints but wrong return type:
```python
# basics/09_error_handling/01_try_except.py
def sum(a: int, b: int) -> int:  # Returns float from division!
    result = a / b
    return result
```

### Files without type hints:
```python
# basics/04_functions/01_functions_basics.py
def add(a, b):  # No type hints
    return a + b
```

### Inconsistent union types:
```python
# basics/02_variables_types/10_union_types.py
from typing import List, Union, Tuple  # Importing unused types
def sum(a:Union[int,str],b:int) -> int:  # Inconsistent spacing
```

## Solution

Add comprehensive, correct type hints following PEP 484.

## Type Hint Guidelines

### Basic Types
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b
```

### Optional Types
```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest"
    return f"Hello, {name}"
```

### Collection Types
```python
from typing import List, Dict, Set, Tuple

def process_items(items: List[str]) -> List[int]:
    return [len(item) for item in items]

def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    return {word: words.count(word) for word in set(words)}
```

### Union Types (Python 3.10+)
```python
def process(value: int | str) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"
```

### Callable Types
```python
from typing import Callable

def apply_operation(
    x: int,
    y: int,
    operation: Callable[[int, int], int]
) -> int:
    return operation(x, y)
```

### Type Aliases
```python
from typing import TypeAlias

Coordinates: TypeAlias = tuple[int, int]

def move(position: Coordinates, offset: Coordinates) -> Coordinates:
    return (position[0] + offset[0], position[1] + offset[1])
```

### Generics
```python
from typing import TypeVar

T = TypeVar('T')

def first_element(items: list[T]) -> T:
    return items[0]
```

## Implementation Plan

### Phase 1: Basics Directory

Add type hints to all files in `basics/`:

```python
# Before
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# After
def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Phase 2: API Files

Add type hints to FastAPI and Flask apps:

```python
# fastapi/main.py - Already has good type hints!
# Use as example for other files

# rest_api/main.py - Add type hints
from typing import TypedDict

class DestinationDict(TypedDict):
    id: int
    destination: str
    country: str
    rating: float

def get_destinations() -> list[DestinationDict]:
    destinations = Destination.query.all()
    return [destination.to_dict() for destination in destinations]
```

### Phase 3: LLM Files

Add type hints to complex LLM code:

```python
# llm_fundamentals/architecture/01_transformer_architecture.py
import torch
import torch.nn as nn
from typing import Dict, Any

class GPTModel(nn.Module):
    def __init__(self, cfg: Dict[str, Any]) -> None:
        super().__init__()
        # ...

    def forward(self, in_idx: torch.Tensor) -> torch.Tensor:
        # ...
```

## Files to Modify

Priority order:
1. [ ] `basics/04_functions/` - All files
2. [ ] `basics/05_data_structures/` - All files
3. [ ] `basics/08_oop/` - All files
4. [ ] `basics/10_advanced/` - All files
5. [ ] `rest_api/main.py`
6. [ ] `llm_fundamentals/**/*.py`

## Type Checking

Add mypy configuration:

```ini
# mypy.ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = False  # Start lenient
check_untyped_defs = True

# Gradually increase strictness
[mypy-basics.04_functions.*]
disallow_untyped_defs = True
```

## Documentation

Add type hints guide to CONTRIBUTING.md:

```markdown
## Type Hints

We use type hints to make code clearer and catch bugs early.

### Basic Rules
1. Always add type hints to function parameters
2. Always add return type hints
3. Use `Optional` for values that can be `None`
4. Use `Union` or `|` for multiple possible types
5. Add type hints to class attributes

### Examples
[Link to examples]
```

## Benefits

- ✅ Clearer code for learners
- ✅ Catch type bugs early
- ✅ Better IDE support
- ✅ Self-documenting code
- ✅ Professional practice

## Resources

- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [Python typing module](https://docs.python.org/3/library/typing.html)
