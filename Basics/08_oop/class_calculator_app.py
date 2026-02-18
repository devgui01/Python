"""
1. Write a class "Calculator" capable of finding square, cube and square root of a number.
"""

class Calculator:
    def __init__(self, choose, num):
        self.choose = choose
        self.num = num

    def Square(self, Num):
        self.Num = Num
        Num = Num ** 2  # For Square
        r = round(Num, 2)
        print(f"Here is Your Square: {r}")

    def Cube(self, Num):
        self.Num = Num
        Num = Num ** 3  # For Cube
        r = round(Num, 2)
        print(f"Here is Your Cube: {r}")

    def SquareRoot(self, Num):
        self.Num = Num
        Num = Num ** 0.5  # For Square Root
        r = round(Num, 2)
        print(f"Here is Your SquareRoot: {r}")

    @staticmethod
    def Wrong():
        print("Wrong Number!")


choose = int(input("\n\t\tYour Calculator!\nType 1 for Square\nType 2 for Cube\nType 3 for SquareRoot\n\nType Your Choice: "))
Number = int(input("Enter the Number: "))
num = Calculator(choose, Number)

if choose == 1:
    num.Square(Number)
elif choose == 2:
    num.Cube(Number)
elif choose == 3:
    num.SquareRoot(Number)
else:
    num.Wrong()
