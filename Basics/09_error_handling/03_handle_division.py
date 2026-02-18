"""Write a program to divide a/b where a and b are integers. If b=0, display infinite by
handling the ‘ZeroDivisionError’."""

try:
    a = int(input("Enter the 1st Number : "))
    b = int(input("Enter the 2st Number : "))
    d = a/b
    print(round(d,2))
except ZeroDivisionError:
    print("Infinite")
except ValueError:
    print("Give a Valid Value")
    