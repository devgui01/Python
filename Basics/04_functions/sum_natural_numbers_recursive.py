# Write a recursive function to calculate the sum of first n natural numbers.

def calculate_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + calculate_sum(n - 1)

number = int(input("Enter the Number to check its sum of first 'n' natural numbers : "))
result = calculate_sum(number)
print(result)
