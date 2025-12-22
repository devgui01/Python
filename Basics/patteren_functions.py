'''
Write a python function to print first n lines of the following pattern:
***
**               --> for n = 3
*

'''

# Type1
def patt(n):
    if(n==0):
        return
    else:
        print("*" * n)
        patt(n-1)
p = patt(3)


# Type2
def pattern(n):
    for i in range(1,n+1):         
        print(f"*" * ((n+1)-i))

n = int(input("Enter the 'n' : "))
pattern(n)






        