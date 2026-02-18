# Write a program to find whether a given number is prime or not.
number = int(input("Enter a Number : "))
if(number <= 0):
    is_prime = False
elif(number == 2):
    is_prime = True
else:
    is_prime = True
    for divisor in range(2, int(number * 0.5) + 1):
        if((number % divisor) == 0):
            is_prime = False
            break
    if(is_prime):
        is_prime = False
    else:
        is_prime = True
print(f"Is Prime Number :{is_prime}")
