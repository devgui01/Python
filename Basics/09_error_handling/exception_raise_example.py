def sum(a:int,b:int) -> int:
    sum = a / b
    return sum

a = int(input("Enter the Number : "))
b = int(input("Enter the Number : "))
if b==0:
    raise ZeroDivisionError("Hehe")
a = sum(a,b)
print(f"\nOutput : {round(a,2)}")