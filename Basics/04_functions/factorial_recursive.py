# Factorial Number
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)


answer = factorial(n = int(input("Enter a Number : ")))
print(answer)
