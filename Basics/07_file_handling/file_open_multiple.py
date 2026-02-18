"""
Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
present, a message without exiting the program must be printed prompting the same.
"""

try:
    with (open("/Users/dartstorm/Desktop/Github/Python/Basics/1.txt") as a,\
        open("/Users/dartstorm/Desktop/Github/Python/Basics/2.txt") as b,\
        open("/Users/dartstorm/Desktop/Github/Python/Basics/3.txt") as c):
            pass
    
except FileNotFoundError:
      print(f"\n\t\t\t\t\tFile Not Found\n")


