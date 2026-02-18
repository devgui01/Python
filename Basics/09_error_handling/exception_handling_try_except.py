def sum(a: int, b: int) -> int:
    result = a / b
    return result

try:
    a = int(input("Enter the Number: "))
    b = int(input("Enter the Number: "))
    a = sum(a, b)
    print(f"\nOutput: {round(a, 2)}")

except ZeroDivisionError:
    print("A Number Can't be Divide by Zero")

except ValueError:
    print("Enter a Valid Number!")

except Exception as e:
    print(e)

else:
    print("Else: Program Worked")

finally:
    print("Finally: I work all time")
