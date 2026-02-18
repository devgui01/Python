# Write a program to calculate the factorial of a given number using for loop.
number = int(input("Enter a Number : "))
factorial = 1
for multiplier in range(1, number + 1):
    factorial = factorial * multiplier
print(factorial)
