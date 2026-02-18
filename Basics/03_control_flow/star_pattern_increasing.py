"""Write a program to print the following star pattern:
*
**
*** for n = 3"""

size = int(input("Enter the Number :"))
for row in range(1, size + 1):
    print("*" * row, end="")
    print("")
