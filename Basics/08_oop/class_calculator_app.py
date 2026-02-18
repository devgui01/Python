"""
1. Write a class "Calculator" capable of finding square, cube and square root of a number.
"""

class Calculator:
    def __init__(self, choice, number):
        self.choice = choice
        self.number = number

    def calculate_square(self, num):
        self.num = num
        squared_result = num ** 2  # For Square
        rounded_result = round(squared_result, 2)
        print(f"Here is Your Square: {rounded_result}")

    def calculate_cube(self, num):
        self.num = num
        cubed_result = num ** 3  # For Cube
        rounded_result = round(cubed_result, 2)
        print(f"Here is Your Cube: {rounded_result}")

    def calculate_square_root(self, num):
        self.num = num
        sqrt_result = num ** 0.5  # For Square Root
        rounded_result = round(sqrt_result, 2)
        print(f"Here is Your SquareRoot: {rounded_result}")

    @staticmethod
    def invalid_choice():
        print("Wrong Number!")


user_choice = int(input("\n\t\tYour Calculator!\nType 1 for Square\nType 2 for Cube\nType 3 for SquareRoot\n\nType Your Choice: "))
input_number = int(input("Enter the Number: "))
calculator = Calculator(user_choice, input_number)

if user_choice == 1:
    calculator.calculate_square(input_number)
elif user_choice == 2:
    calculator.calculate_cube(input_number)
elif user_choice == 3:
    calculator.calculate_square_root(input_number)
else:
    calculator.invalid_choice()
