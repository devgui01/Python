"""Write a program to divide a/b where a and b are integers. If b=0, display infinite by
handling the 'ZeroDivisionError'."""

try:
    numerator = int(input("Enter the 1st Number : "))
    denominator = int(input("Enter the 2st Number : "))
    division_result = numerator / denominator
    print(round(division_result, 2))
except ZeroDivisionError:
    print("Infinite")
except ValueError:
    print("Give a Valid Value")
    