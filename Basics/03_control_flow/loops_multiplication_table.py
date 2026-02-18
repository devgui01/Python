# Write a program to print multiplication table of a given number using loops.

#Using ForLoops
number = int(input("Enter the number : "))
for multiplier in range(10):
    print(f"{number} * {multiplier + 1} = {number * (multiplier + 1)} ")

multiplier = 1
#Using WhileLoops
number = int(input("Enter the number : "))
while(multiplier < 11):
    print(f"{number} * {multiplier} = {number * multiplier}")
    multiplier = multiplier + 1
