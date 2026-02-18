"""
Prime Number Checker
Check if a given number is prime or not.
"""
import math

number = int(input("Enter a Number: "))

if number <= 1:
    is_prime = False
elif number == 2:
    is_prime = True
else:
    is_prime = True
    # Only check up to square root of number for efficiency
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            is_prime = False
            break

print(f"Is Prime Number: {is_prime}")
