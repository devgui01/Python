'''
Write a python function to print first n lines of the following pattern:
***
**               --> for n = 3
*

'''

# Type1
def print_pattern(rows):
    if(rows == 0):
        return
    else:
        print("*" * rows)
        print_pattern(rows - 1)
result = print_pattern(3)


# Type2
def generate_pattern(n):
    for row in range(1, n + 1):
        print(f"*" * ((n + 1) - row))

rows = int(input("Enter the 'n' : "))
generate_pattern(rows)
