---
title: "REFACTOR: Improve OOP examples with better practices"
labels: ["refactor", "oop", "intermediate"]
assignees: []
---

## Refactoring Issue

The OOP examples in `basics/08_oop/` work but don't follow best practices. They can be improved to teach better habits.

## Current Issues

### 1. Class Attribute Naming

**Current:**
```python
# basics/08_oop/01_class_basics.py
class Planets:
    nearSun = False  # Confusing name
    isLifeexist = "Nope"  # Awkward naming
    power = 100
```

**Issues:**
- `nearSun` - unclear what it means
- `isLifeexist` - grammatically awkward
- No docstrings
- Mixed naming conventions

### 2. Method Naming

**Current:**
```python
def Power(self):  # Capitalized method name
    print(self.power)
```

**Issues:**
- Method names should be lowercase
- Should return value, not just print
- No docstring

### 3. Missing `__init__` Examples

Many examples don't show proper constructor usage.

### 4. Property Decorators

**Current:**
```python
# basics/08_oop/13_property_decorator.py
# Property decorator example exists but could be clearer
```

## Improvements

### 1. Better Class Design

**Before:**
```python
class Planets:
    nearSun = False
    isLifeexist = "Nope"
    power = 100

    def Power(self):
        print(self.power)
```

**After:**
```python
class Planet:
    """Represents a planet in our solar system."""

    def __init__(self, name: str, distance_from_sun: float):
        """
        Initialize a planet.

        Args:
            name: Planet name
            distance_from_sun: Distance in million km
        """
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.has_life = False
        self.supports_human_life = False

    def can_support_life(self) -> bool:
        """Check if planet can support life."""
        # Simplified: life needs moderate distance from sun
        return 100 <= self.distance_from_sun <= 200

    def colonize(self) -> str:
        """Attempt to colonize the planet."""
        if self.can_support_life():
            self.supports_human_life = True
            return f"{self.name} can be colonized!"
        return f"{self.name} is not suitable for colonization."
```

### 2. Better Examples

Add comprehensive examples:

```python
# New file: basics/08_oop/17_bank_account.py
"""
Bank Account Example - Demonstrates OOP principles

This example shows:
- Encapsulation (private attributes)
- Data validation
- Method design
- String representation
"""

class BankAccount:
    """A simple bank account class."""

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Initialize a bank account.

        Args:
            owner: Account owner's name
            balance: Initial balance (default: 0)
        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self._balance = balance  # Protected attribute

    def deposit(self, amount: float) -> float:
        """
        Deposit money into the account.

        Args:
            amount: Amount to deposit

        Returns:
            New balance
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraw money from the account.

        Args:
            amount: Amount to withdraw

        Returns:
            New balance

        Raises:
            ValueError: If insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Available: ${self._balance}")

        self._balance -= amount
        return self._balance

    @property
    def balance(self) -> float:
        """Get current balance (read-only)."""
        return self._balance

    def __str__(self) -> str:
        """String representation."""
        return f"BankAccount(owner='{self.owner}', balance=${self._balance:.2f})"

    def __repr__(self) -> str:
        """Developer representation."""
        return f"BankAccount('{self.owner}', {self._balance})"


# Example usage
if __name__ == "__main__":
    # Create account
    account = BankAccount("Alice", 1000)
    print(account)  # BankAccount(owner='Alice', balance=$1000.00)

    # Deposit
    account.deposit(500)
    print(f"After deposit: ${account.balance}")

    # Withdraw
    account.withdraw(200)
    print(f"After withdrawal: ${account.balance}")

    # Try to withdraw too much
    try:
        account.withdraw(5000)
    except ValueError as e:
        print(f"Error: {e}")
```

### 3. Inheritance Examples

**Add new file:**
```python
# basics/08_oop/18_inheritance_example.py
"""
Inheritance Example - Employee Hierarchy

Demonstrates:
- Single inheritance
- Method overriding
- super() usage
- Abstract base classes
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    """Base employee class."""

    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self) -> float:
        """Calculate employee salary."""
        pass

    def get_info(self) -> str:
        """Get employee information."""
        return f"{self.name} (ID: {self.employee_id})"


class SalariedEmployee(Employee):
    """Employee with fixed salary."""

    def __init__(self, name: str, employee_id: int, annual_salary: float):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary

    def calculate_salary(self) -> float:
        return self.annual_salary / 12  # Monthly

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info} - Salaried: ${self.calculate_salary():.2f}/month"


class HourlyEmployee(Employee):
    """Employee paid by hour."""

    def __init__(self, name: str, employee_id: int, hourly_rate: float, hours_worked: float):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info} - Hourly: ${self.calculate_salary():.2f}"


# Usage
if __name__ == "__main__":
    employees = [
        SalariedEmployee("Alice", 1, 60000),
        HourlyEmployee("Bob", 2, 25, 160),
    ]

    for emp in employees:
        print(emp.get_info())
```

## Files to Create/Modify

### Modify:
- [ ] `basics/08_oop/01_class_basics.py` - Improve naming and structure
- [ ] `basics/08_oop/02_class_calculator.py` - Add docstrings, better design
- [ ] `basics/08_oop/03_class_constructor.py` - Better examples
- [ ] `basics/08_oop/04_class_encapsulation.py` - Show proper encapsulation

### Create:
- [ ] `basics/08_oop/17_bank_account.py` - Comprehensive example
- [ ] `basics/08_oop/18_inheritance_example.py` - Inheritance hierarchy
- [ ] `basics/08_oop/19_polymorphism_example.py` - Polymorphism
- [ ] `basics/08_oop/20_abstract_classes.py` - ABC examples
- [ ] `basics/08_oop/README_OOP.md` - OOP principles guide

## Documentation

Add OOP principles guide:

```markdown
# Object-Oriented Programming Principles

## The Four Pillars

### 1. Encapsulation
Hide internal state, expose through methods.

### 2. Inheritance
Create new classes based on existing ones.

### 3. Polymorphism
Same interface, different implementations.

### 4. Abstraction
Hide complexity, show essentials.

## Best Practices

1. **Single Responsibility**
   - One class, one purpose

2. **Clear Naming**
   - Classes: PascalCase
   - Methods: lowercase_with_underscore
   - Private: _prefix

3. **Docstrings**
   - Document every class and method

4. **Type Hints**
   - Specify parameter and return types
```

## Benefits

- ✅ Teaches best practices
- ✅ Better code examples
- ✅ Real-world scenarios
- ✅ Professional habits
- ✅ Clearer learning
