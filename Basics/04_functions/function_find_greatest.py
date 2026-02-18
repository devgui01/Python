# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>=b and a>c):
        return f"{a} is Greater among {b} and {c}"
    elif(b>=c and b>=a):
        return f"{b} is Greater among {a} and {c}"
    elif(c>=a and c>=b):
        return f"{c} is Greater among {a} and {b}"
    else:
        return f"Invalid Numbers : {a}{b}{c} "
count = 0
numbers = []
while True:
    i = int(input("Enter the Numbers : "))
    numbers.append(i)
    count+=1
    if(count==3):
        break
print(f"ok! I Found Your Numbers : {numbers}")
a = numbers[0]
b = numbers[1]
c = numbers[2]
check = greatest(a,b,c)
print(f"{check}")


