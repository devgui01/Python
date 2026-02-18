# Write a python function to print multiplication table of a given number.
def table(n):
    i = 1
    while (i<11):
        print (f"{n} * {i} = {n*i} ")
        i+=1


table(n=3)