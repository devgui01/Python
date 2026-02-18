"""
Write a program to filter a list of numbers which are divisible by 5.
"""

l1 = [1,2,3,4,5,6,7,8,9,10]
def div(n):
        if((n%5)==0):
            return True
        return False

f = filter(div,l1)
print(list(f))

