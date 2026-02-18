"""
 Write a program to find the maximum of the numbers in a list using the reduce
function.
"""
from functools import reduce

l1 = [23,23,56,87,34,776,4443,3,33,222,533,2,22,2]
def max(a,b):
    if(a>b):
        return a
    elif(a<b):
        return b
    elif(a==b):
        return a
    else:
        pass

d = reduce(max,l1)
print(d)

    
