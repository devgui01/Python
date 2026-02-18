"""
Write a list comprehension to print a list which contains the multiplication table of a
user entered number.
"""

j = int(input("Enter the n : "))
h = [ i*j for i in range(11)]
print(f"{h}")