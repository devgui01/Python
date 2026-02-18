"""
Write a program to open three files 1.txt, 2.txt and 3.txt.
If any of these files are not present, print a message without exiting.
"""

try:
    with (open("1.txt") as a,
          open("2.txt") as b,
          open("3.txt") as c):
        pass
except FileNotFoundError:
    print("\n\t\t\t\t\tFile Not Found\n")


